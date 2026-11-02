import { h, replace, focusEl } from '../common/dom.js';
import { mountShell, panel } from '../common/shell.js';
import { button, stat } from '../common/controls.js';
import { num } from '../common/format.js';
import { tally, debrief, STATUSES, KINDS } from './model.js';
import { PRESETS, DEFAULT_PRESET } from './presets.js';

const ABOUT = {
  intro: 'A pile of evidence with a true status for each item, written in advance. You sort it, choose a verdict, and see how a steering group reacts.',
  equations: [
    'Verified: you checked it against data you hold, or saw it yourself. Reported: someone says so and you have not checked. Contradicted: data you hold says otherwise.',
    'An interview that the data confirms counts as verified; a vendor’s statement you have not checked stays reported, however confident it sounds.',
    'Report credibility = 100 − 12 for each item called verified that is not (an over-claim) − 6 for each contradiction you missed − 3 for any other mismatch.',
    'The report counts as over-claimed when it has two or more over-claims. The steering group’s reaction depends on your verdict and on whether the report is honest or over-claimed.',
  ],
  assumptions: [
    'Each item has one right status. In practice a finding can be partly verified; then write which part.',
    'The steering group reads the report carefully. Real ones skim, which makes an over-claim survive longer and fall harder.',
  ],
  leftOut: [
    'Weighting the dimensions of readiness against each other: lesson 02.6 covers the full assessment.',
    'Findings you never collected. The interviews and exports in module 2 are how you get them.',
  ],
};

let shell;
let scenario;
let picks = {};
let verdict = null;
let view = {};
let radiosByItem = {};

function start(key) {
  scenario = PRESETS[key];
  picks = {};
  verdict = null;
  radiosByItem = {};
  build();
  renderStatus();
}

const tone = (s) => (s === 'verified' ? 'good' : s === 'contradicted' ? 'bad' : 'warn');

function build() {
  view.status = h('div', { class: 'stats' });
  const pile = panel('The evidence', { id: 'pile' });
  pile.body.append(
    h('ul', { class: 'legend small' }, Object.entries(STATUSES).map(([k, s]) => h('li', {}, h('span', { class: `tag tag-${tone(k)}` }, s.label), ` ${s.note}.`))),
    h('div', { class: 'cards' }, scenario.items.map((it) => buildItem(it))),
  );
  if (scenario.notes && scenario.notes.length) {
    pile.body.append(h('details', { class: 'notes' }, h('summary', {}, 'Where these facts come from'),
      h('ul', {}, scenario.notes.map((n) => h('li', {}, n)))));
  }
  const send = panel('Your verdict', { id: 'verdict', className: 'debrief' });
  view.sendHeading = send.heading;
  view.send = h('div');
  send.body.append(view.send);
  renderSend();
  replace(shell.main, view.status, pile.el, send.el);
}

function buildItem(it) {
  const headingId = `item-${it.id}`;
  const radios = Object.entries(STATUSES).map(([k, s]) => {
    const id = `st-${it.id}-${k}`;
    const r = h('input', { type: 'radio', name: `st-${it.id}`, id, value: k });
    r.addEventListener('change', () => { if (r.checked) { picks[it.id] = k; renderStatus(); } });
    return h('span', { class: 'status-opt' }, r, h('label', { for: id }, s.label));
  });
  radiosByItem[it.id] = radios.map((x) => x.firstChild);
  const result = h('div', { class: 'item-result', hidden: true });
  const el = h('article', { class: 'card evidence-item', 'aria-labelledby': headingId },
    h('p', { class: 'item-meta' }, h('span', { class: 'tag tag-neutral' }, KINDS[it.kind]), ' ', h('span', { class: 'date' }, it.date), ' · ', it.area),
    h('h3', { id: headingId }, it.source),
    h('p', {}, it.text),
    h('fieldset', { class: 'status-group' }, h('legend', { class: 'small' }, 'This evidence is…'), radios),
    result,
  );
  view[`res-${it.id}`] = result;
  return el;
}

function renderStatus() {
  const t = tally(scenario, picks);
  replace(view.status,
    stat('Sorted', `${num(scenario.items.length - t.unsorted)} of ${num(scenario.items.length)}`, null, t.unsorted ? '' : 'good'),
    stat('Verified', num(t.verified)),
    stat('Reported', num(t.reported)),
    stat('Contradicted', num(t.contradicted)),
  );
}

function renderSend() {
  const radios = scenario.verdicts.map((v) => {
    const r = h('input', { type: 'radio', name: 'verdict', id: `v-${v.id}`, value: v.id });
    r.addEventListener('change', () => { if (r.checked) verdict = v.id; });
    return r;
  });
  const err = h('p', { class: 'callout callout-warn', role: 'alert', hidden: true });
  replace(view.send,
    h('fieldset', { class: 'group choices' }, h('legend', {}, 'Your verdict for Thursday'),
      scenario.verdicts.map((v, i) => h('div', { class: 'choice' }, radios[i], h('label', { for: `v-${v.id}` }, h('strong', {}, `${v.label}. `), v.text)))),
    err,
    h('div', { class: 'btn-row' }, button('Send the report to the steering group', () => {
      const missing = scenario.items.filter((it) => !picks[it.id]).length;
      if (missing || !verdict) {
        err.textContent = missing ? `Sort every item first (${missing} left).` : 'Choose a verdict first.';
        err.hidden = false;
        return;
      }
      renderDebrief();
    })),
  );
}

function verdictLine(r) {
  const map = { right: ['good', 'right'], overclaim: ['bad', 'over-claimed'], missedContradiction: ['bad', 'missed the contradiction'], other: ['warn', 'not quite'] };
  return h('span', { class: `tag tag-${map[r.result][0]}` }, map[r.result][1]);
}

function renderDebrief() {
  const d = debrief(scenario, picks, verdict);
  for (const r of d.rows) {
    for (const x of radiosByItem[r.item.id]) x.disabled = true;
    const box = view[`res-${r.item.id}`];
    box.hidden = false;
    replace(box,
      h('p', {}, verdictLine(r), ' ', `You: ${STATUSES[r.pick].label.toLowerCase()}. True: `, h('span', { class: `tag tag-${tone(r.item.truth)}` }, STATUSES[r.item.truth].label.toLowerCase())),
      h('p', { class: 'small' }, r.item.why));
  }
  const headline = d.overclaimed
    ? `Over-claimed: ${num(d.overclaims)} findings were called verified that were not.`
    : d.overclaims ? 'Honest, with one over-claim.' : 'An honest report.';
  view.sendHeading.textContent = 'Debrief';
  const mineTone = d.mine.tone;
  replace(view.send,
    h('div', { class: `callout callout-${d.overclaimed ? 'bad' : d.credibility >= 80 ? 'good' : 'warn'}` },
      h('p', {}, h('strong', {}, headline)),
      h('p', {}, `Report credibility ${num(d.credibility)} / 100: ${num(d.right)} of ${num(scenario.items.length)} items sorted right, ` +
        `${num(d.overclaims)} over-claimed, ${num(d.missedContradictions)} ${d.missedContradictions === 1 ? 'contradiction' : 'contradictions'} missed.`)),
    h('h3', {}, `The steering group reacts to “${d.mine.verdict.label}”`),
    h('div', { class: `callout callout-${mineTone}` }, h('p', {}, d.mine.text)),
    d.challenges.length ? h('div', {},
      h('h3', {}, 'The questions your report could not answer'),
      h('ul', {}, d.challenges.map((r) => h('li', {}, r.item.challenge, h('span', { class: 'small muted' }, ` (${r.item.source}, ${r.item.date})`))))) : null,
    h('h3', {}, 'The same verdict, honest vs over-claimed'),
    h('div', { class: 'compare' },
      h('div', { class: `callout callout-${d.honest.tone}` }, h('p', {}, h('strong', {}, d.overclaimed ? 'If the report had been honest' : 'Your honest report')), h('p', {}, d.honest.text)),
      h('div', { class: `callout callout-${d.inflated.tone}` }, h('p', {}, h('strong', {}, d.overclaimed ? 'Your over-claimed report' : 'If it had called the reported items verified')), h('p', {}, d.inflated.text))),
    h('h3', {}, d.verdictRight ? 'Your verdict' : 'A stronger verdict'),
    h('p', {}, h('strong', {}, `${d.bestVerdict.label}: `), d.bestVerdict.text),
    h('p', { class: 'small' }, `What would change it: ${d.bestVerdict.changeIt}`),
    h('h3', {}, 'The point of this lesson'),
    h('p', { class: 'lesson-point' }, scenario.lessonPoint),
    h('div', { class: 'btn-row' }, button('Sort the evidence again', () => { start(shell.presetKey); focusEl(document.getElementById(`item-${scenario.items[0].id}`)); }, { variant: 'secondary' })),
  );
  focusEl(view.sendHeading);
  shell.announce(`${headline} ${d.mine.text}`);
}

shell = mountShell({
  title: 'Readiness evidence grader',
  tagline: 'Seventeen pieces of evidence: verified, reported or contradicted?',
  presets: PRESETS,
  defaultPreset: DEFAULT_PRESET,
  about: ABOUT,
  onPreset: start,
});
start(shell.presetKey);
