import { h, replace, focusEl } from '../common/dom.js';
import { mountShell, panel } from '../common/shell.js';
import { button, stat } from '../common/controls.js';
import { stackTable } from '../common/table.js';
import { ils, num, plural } from '../common/format.js';
import { createState, currentInject, activeDecisions, injectInfo, decide, exposed, debrief, QUALITY } from './model.js';
import { PRESETS, DEFAULT_PRESET } from './presets.js';

const ABOUT = {
  intro: 'A scripted incident in hours. What you learn at each point is fixed; what happens to customers, trust and the record depends on your choices.',
  equations: [
    'Harm: customers who received a reply outside policy or someone else’s data. Between two points in time, more customers are harmed while the feature is fully on and the cause is not fixed. Harm score = 100 − 6 per customer harmed after you were told.',
    'Time to contain: hours from detection until the harm stopped for good (a pause, a narrower switch, or a tested fix). 30 minutes or less scores 100; within an hour 85; within 3 hours 60; within 6 hours 40; within a day 20; later 5; never 0.',
    'Trust: three meters from 0 to 100 (customers, staff, leaders), moved by each choice; the score is their average.',
    'Documentation: points for the incident log, the decisions recorded, the briefings and the review, as a share of the best possible.',
    'The debrief compares each of your choices with the runbook step it belongs to.',
  ],
  assumptions: [
    'The facts arrive at the same hour whatever you do; in a real incident good choices also make facts arrive sooner.',
    'Reporting rules are not modelled. Whether a privacy incident must be reported, to whom and by when is a question for the DPO or counsel; the model scores sending it to them, not guessing.',
  ],
  leftOut: [
    'Insurance, contracts with the vendor and the cost of the hours spent on the incident.',
    'The second incident that a missing change-control rule makes likely.',
  ],
};

let shell;
let scenario;
let state;
let picks = {};
let view = {};

function start(key) {
  scenario = PRESETS[key];
  state = createState(scenario);
  picks = {};
  build();
  renderAll();
}

function build() {
  view.status = h('div', { class: 'stats' });
  const now = panel('Now', { id: 'now' });
  view.nowHeading = now.heading;
  view.now = h('div');
  now.body.append(view.now);

  const log = panel('What happened so far', { id: 'log' });
  view.log = h('ol', { class: 'timeline' });
  log.body.append(view.log);
  if (scenario.notes && scenario.notes.length) {
    log.body.append(h('details', { class: 'notes' }, h('summary', {}, 'Where these numbers come from'),
      h('ul', {}, scenario.notes.map((n) => h('li', {}, n)))));
  }

  const result = panel('Debrief', { id: 'result', className: 'debrief' });
  view.resultPanel = result.el;
  view.resultHeading = result.heading;
  view.result = h('div');
  result.body.append(view.result);
  view.resultPanel.hidden = true;

  replace(shell.main,
    view.status,
    h('div', { class: 'layout layout-2' },
      h('div', { class: 'stack' }, now.el),
      h('div', { class: 'stack' }, log.el)),
    result.el);
}

function renderAll() {
  renderStatus();
  renderNow();
  renderLog();
}

function containedText() {
  if (state.containedAt !== null) return `contained after ${num(state.containedAt, 2)} h`;
  return exposed(state, scenario) ? 'still happening' : 'not yet';
}

function renderStatus() {
  const t = state.trust;
  replace(view.status,
    stat('Customers harmed', num(state.harmed), state.newlyHarmed ? `${num(state.newlyHarmed)} after you were told` : 'all before you were told', state.newlyHarmed ? 'bad' : ''),
    stat('Harm', containedText(), null, state.containedAt !== null ? 'good' : exposed(state, scenario) ? 'bad' : 'warn'),
    stat('Trust', `${num(t.customers)} · ${num(t.staff)} · ${num(t.leaders)}`, 'customers · staff · leaders (0–100)'),
    stat('Incident record', `${num(state.docs)} points`, state.cost ? `cost so far ${ils(state.cost)}` : null),
  );
}

function renderNow() {
  const inj = currentInject(state, scenario);
  if (!inj) {
    view.nowHeading.textContent = 'The tabletop is over';
    replace(view.now, h('p', {}, 'Your scores and the runbook comparison are in the debrief below.'));
    return;
  }
  view.nowHeading.textContent = inj.when;
  const decisions = activeDecisions(state, inj);
  const err = h('p', { class: 'callout callout-warn', role: 'alert', hidden: true }, 'Choose one option in every group first.');
  const groups = decisions.map((d) => h('fieldset', { class: 'group choices' },
    h('legend', {}, d.label),
    d.options.map((o) => {
      const id = `${inj.id}-${d.id}-${o.id}`;
      const r = h('input', { type: 'radio', name: `${inj.id}-${d.id}`, id, value: o.id, checked: picks[d.id] === o.id });
      r.addEventListener('change', () => { if (r.checked) picks[d.id] = o.id; });
      return h('div', { class: 'choice' }, r, h('label', { for: id }, o.text));
    })));
  const next = scenario.injects[state.index + 1];
  replace(view.now,
    injectInfo(state, inj).map((t, i) => h('p', { class: i ? 'info extra' : 'info' }, t)),
    groups,
    err,
    h('div', { class: 'btn-row' }, button(next ? `Decide, then go to ${next.when}` : 'Decide and close the incident', () => {
      if (decisions.some((d) => !picks[d.id])) { err.hidden = false; return; }
      onDecide();
    })),
  );
}

function onDecide() {
  const res = decide(state, scenario, picks);
  state = res.state;
  picks = {};
  renderAll();
  const said = res.entries.map((e) => e.result).join(' ');
  if (state.done) {
    renderDebrief();
  } else {
    focusEl(view.nowHeading);
    shell.announce(`${said}${res.added ? ` ${plural(res.added, 'more customer')} harmed before ${view.nowHeading.textContent}.` : ''} Now ${view.nowHeading.textContent}.`);
  }
}

function renderLog() {
  if (!state.log.length) {
    replace(view.log, h('li', { class: 'muted empty' }, 'Nothing decided yet.'));
    return;
  }
  const byInject = [];
  for (const e of state.log) {
    let g = byInject.find((x) => x.inject === e.inject);
    if (!g) { g = { inject: e.inject, when: e.when, items: [], added: e.harmedAfter }; byInject.push(g); }
    g.items.push(e);
  }
  replace(view.log, byInject.map((g) => h('li', { class: 'tl-item' },
    h('p', { class: 'tl-when' }, g.when),
    h('ul', {}, g.items.map((e) => h('li', {}, h('strong', {}, `${e.label}: `), e.text, h('br'), h('span', { class: 'small' }, e.result)))),
    g.added ? h('p', { class: 'small bad-text' }, `Meanwhile ${plural(g.added, 'more customer')} got a bad reply.`) : null,
  )));
}

function scoreTone(v) {
  return v >= 80 ? 'good' : v >= 50 ? 'warn' : 'bad';
}

function renderDebrief() {
  const d = debrief(state, scenario);
  const s = d.scores;
  view.resultPanel.hidden = false;
  const headline = d.verdict === 'strong' ? 'A well-run incident.' : d.verdict === 'mixed' ? 'Contained, with costs you could have avoided.' : 'The incident ran you.';
  replace(view.result,
    h('div', { class: `callout callout-${d.verdict === 'strong' ? 'good' : d.verdict === 'mixed' ? 'warn' : 'bad'}` },
      h('p', {}, h('strong', {}, headline)),
      h('p', {}, `${num(d.harmedTotal)} customers harmed in total, ${num(d.newlyHarmed)} of them after you were told. ` +
        `${s.containedAt !== null ? `Harm contained ${num(s.containedAt, 2)} hours after detection.` : 'The harm was never fully contained.'}` +
        `${d.cost ? ` Direct cost: ${ils(d.cost)}.` : ''}`)),
    h('div', { class: 'stats' },
      stat('Harm', `${num(s.harm)} / 100`, `${num(d.newlyHarmed)} harmed on your watch`, scoreTone(s.harm)),
      stat('Time to contain', `${num(s.contain)} / 100`, s.containedAt !== null ? `${num(s.containedAt, 2)} h` : 'never', scoreTone(s.contain)),
      stat('Trust', `${num(s.trust)} / 100`, `customers ${num(state.trust.customers)} · staff ${num(state.trust.staff)} · leaders ${num(state.trust.leaders)}`, scoreTone(s.trust)),
      stat('Documentation', `${num(s.docs)} / 100`, `${num(state.docs)} of ${num(s.docsMax)} points`, scoreTone(s.docs)),
    ),
    h('h3', {}, 'You against the runbook'),
    stackTable({
      caption: 'Each runbook step, what it says and what you did',
      head: ['Runbook step', 'What it says', 'What you did'],
      rows: d.runbook.map((r) => ({
        th: [r.title, ' ', h('span', { class: `tag tag-${r.status === 'skipped' ? 'bad' : QUALITY[r.status].tone}` }, r.status === 'skipped' ? 'skipped' : QUALITY[r.status].label)],
        cells: [
          h('span', { class: 'small' }, r.text),
          r.did.length
            ? h('ul', { class: 'compact small' }, r.did.map((e) => h('li', {}, `${e.when}: ${e.text}`)))
            : h('span', { class: 'small' }, 'Nothing at this step.'),
        ],
      })),
    }),
    d.notes.length ? h('div', {}, h('h3', {}, 'Worth a second look'), h('ul', {}, d.notes.map((n) => h('li', {}, n.text)))) : null,
    h('h3', {}, 'The point of this lesson'),
    h('p', { class: 'lesson-point' }, scenario.lessonPoint),
    h('div', { class: 'btn-row' }, button('Run the incident again', () => { start(shell.presetKey); focusEl(view.nowHeading); }, { variant: 'secondary' })),
  );
  focusEl(view.resultHeading);
  shell.announce(`${headline} Overall ${s.overall} out of 100.`);
}

shell = mountShell({
  title: 'Incident tabletop',
  tagline: 'An AI incident hour by hour: contain, communicate, fix, report.',
  presets: PRESETS,
  defaultPreset: DEFAULT_PRESET,
  about: ABOUT,
  onPreset: start,
});
start(shell.presetKey);
