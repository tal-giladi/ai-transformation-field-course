import { h, replace, focusEl } from '../common/dom.js';
import { mountShell, panel } from '../common/shell.js';
import { button, stat, selectField, toggleField, rangeField } from '../common/controls.js';
import { stackTable } from '../common/table.js';
import { lineChart } from '../common/chart.js';
import { ilsShort, num, plural } from '../common/format.js';
import {
  ARCHETYPES, RIGHTS, MRM, ROADS, normalizeConfig, createState, playQuarter, eventAt, quarterLabel, summary, unitTable,
  debrief, effectiveSlots, roadReady,
} from './model.js';
import { PRESETS, DEFAULT_PRESET } from './presets.js';

const ABOUT = {
  intro: 'Twelve quarters of pilots moving (or not) from pilot to production under the design you choose. The model is deterministic: the same design and the same answers give the same three years.',
  equations: [
    'Build: a pilot needs 3 quarters of work in a less mature unit and 2 in a mature one, or 2 when the central team builds it, but the central team works on only a limited number at a time. A ready platform saves a quarter for low- and medium-risk pilots. Changing the operating model costs a quarter of build progress.',
    'Decision rights route each finished pilot: to the central review queue, to the unit head, to the unit with the hub’s standards (medium risk; needs the templates), or onto the paved road (low risk; needs the platform). With the evaluation kit, a unit’s own test stops weak pilots.',
    'Review: slots × 1.5 when templates exist, worked first come, first served. Each model takes 2 slots (full validation), 0.5 / 1 / 2 by risk tier, or 0.5 (light check). Every review except the light check stops weak pilots.',
    'Shadow builds: each quarter a unit has any pilot waiting two quarters or more, it adds 0.35 × its appetite towards a tool built outside the process; each whole one goes live unreviewed.',
    'Duplicates: a pilot that goes live while another unit runs the same thing is a duplicate, unless the central team (central CoE) or the catalogue (hub-and-spoke) spots the twin and merges it.',
    'Incidents: every pilot in production adds an expected number of incidents each quarter by risk tier, raised for weak models and shadow tools, lowered by validation and by the platform; each time the total passes a whole number, an incident happens.',
    'Cost per quarter: the central team + review slots + paved roads (build cost spread over the lead time, then a run cost) + a run cost per pilot in production (lower on the platform) + event costs.',
    'Time to decision: the average number of quarters pilots waited in the queue before their go-live decision; pilots still waiting count what they have waited so far.',
  ],
  assumptions: [
    'Every number is in the preset’s notes. Units differ only in maturity and in how readily they build outside the process.',
    'Events happen in the same quarter whatever you do; their effects depend on your design and your answers. The supervisor’s reaction is this model’s, not a statement about a real supervisor.',
  ],
  leftOut: [
    'The value each pilot creates once live, hiring, vendor management and change management in the units.',
    'Politics: in this model, everyone accepts the design you choose.',
  ],
};

let shell;
let scenario;
let config;
let state;
let pick = null;
const view = {};

function start(key) {
  scenario = PRESETS[key];
  config = normalizeConfig(scenario.startConfig);
  state = createState(scenario);
  pick = null;
  build();
  renderAll();
}

function build() {
  view.status = h('div', { class: 'stats' });
  const design = panel('Your design', { id: 'design' });
  view.design = h('div');
  view.designCost = h('p', { class: 'small muted' });
  design.body.append(
    h('p', { class: 'small muted' }, 'It starts as the bank works today. Change anything before any quarter.'),
    view.design, view.designCost);

  const now = panel('This quarter', { id: 'now' });
  view.nowHeading = now.heading;
  view.now = h('div');
  now.body.append(view.now);

  const units = panel('Units', { id: 'units' });
  view.units = h('div');
  units.body.append(view.units);

  const history = panel('Quarter by quarter', { id: 'history' });
  view.history = h('div');
  history.body.append(view.history);
  if (scenario.notes && scenario.notes.length) {
    history.body.append(h('details', { class: 'notes' }, h('summary', {}, 'Where these numbers come from'),
      h('ul', {}, scenario.notes.map((n) => h('li', {}, n)))));
  }

  const result = panel('Debrief', { id: 'result', className: 'debrief' });
  view.resultPanel = result.el;
  view.resultHeading = result.heading;
  view.result = h('div');
  result.body.append(view.result);
  view.resultPanel.hidden = true;

  replace(shell.main, view.status,
    h('div', { class: 'layout layout-2' },
      h('div', { class: 'stack' }, design.el),
      h('div', { class: 'stack' }, now.el, units.el, history.el)),
    result.el);
  renderDesign();
}

function quarterCostEstimate() {
  const m = scenario.money;
  let roads = 0;
  for (const key of Object.keys(ROADS)) {
    if (!config.roads[key] && state.forced[key] === undefined) continue;
    roads += roadReady(state, scenario, key, state.q) ? m.roads[key].run : m.roads[key].build / m.roads[key].lead;
  }
  return m.coe[config.archetype] + config.slots * m.slotCost + roads;
}

function designChanged() {
  replace(view.designCost, `Fixed cost of this design next quarter: about ${ilsShort(quarterCostEstimate())}, before run costs and events. Budget: ${ilsShort(scenario.money.budgetPerYear / 4)} a quarter.`);
}

function renderDesign() {
  const m = scenario.money;
  const roadHelp = (key) => {
    const r = m.roads[key];
    return `${ilsShort(r.build)} over ${plural(r.lead, 'quarter')}, then ${ilsShort(r.run)} a quarter.`;
  };
  replace(view.design,
    selectField({
      label: 'Operating model', value: config.archetype,
      options: Object.entries(ARCHETYPES).map(([k, v]) => ({ value: k, label: v.label })),
      help: `Central team cost a quarter: central ${ilsShort(m.coe.central)}, hub ${ilsShort(m.coe.hub)}, federated ${ilsShort(m.coe.federated)}.`,
      onChange: (v) => { config.archetype = v; designChanged(); },
    }).el,
    selectField({
      label: 'Who decides go-live', value: config.rights,
      options: Object.entries(RIGHTS).map(([k, v]) => ({ value: k, label: v.label })),
      onChange: (v) => { config.rights = v; designChanged(); },
    }).el,
    rangeField({
      label: 'Central review slots a quarter', min: 0, max: 10, step: 1, value: config.slots, unit: 'slots',
      help: `${ilsShort(m.slotCost)} per slot a quarter.`,
      onInput: (v) => { config.slots = v; designChanged(); },
    }).el,
    selectField({
      label: 'Model risk validation', value: config.mrm,
      options: Object.entries(MRM).map(([k, v]) => ({ value: k, label: v.label })),
      onChange: (v) => { config.mrm = v; designChanged(); },
    }).el,
    h('fieldset', { class: 'group' },
      h('legend', {}, 'Paved roads'),
      Object.entries(ROADS).map(([key, r]) => {
        const forced = state.forced[key] !== undefined;
        const ready = roadReady(state, scenario, key, state.q);
        const t = toggleField({
          label: `${r.label}${forced ? ' (funded after the supervisor’s question)' : ''}`,
          checked: config.roads[key] || forced,
          help: `${roadHelp(key)}${ready ? ' Ready.' : config.roads[key] || forced ? ' Being built.' : ''}`,
          onChange: (v) => { config.roads[key] = v; designChanged(); },
        });
        if (forced) t.input.disabled = true;
        return t.el;
      })),
  );
  designChanged();
}

function renderAll() {
  renderStatus();
  renderNow();
  renderUnits();
  renderHistory();
}

function renderStatus() {
  const s = summary(state, scenario);
  const started = state.q > 0;
  const overBudget = s.cost > s.budget;
  replace(view.status,
    stat('Quarter', state.done ? 'done' : quarterLabel(scenario, state.q), `${num(state.q)} of ${num(scenario.quarters)} played`),
    stat('In production', `${num(s.prod)}`, `of ${num(s.total)} pilots; ${num(s.stopped)} stopped as weak`, started && s.prod ? 'good' : ''),
    stat('Waiting for review', num(s.backlog), started ? `average wait ${num(s.avgWait, 1)} quarters` : null, s.backlog > 10 ? 'bad' : s.backlog > 4 ? 'warn' : ''),
    stat('Duplicates running', num(s.duplicates), s.merged ? `${num(s.merged)} merged` : null, s.duplicates ? 'warn' : ''),
    stat('Risk incidents', num(s.incidents), s.weakInProd ? `${plural(s.weakInProd, 'weak model')} in production` : null, s.incidents >= 5 ? 'bad' : s.incidents ? 'warn' : ''),
    stat('Shadow tools in use', num(s.shadow), 'built outside the process', s.shadow > 2 ? 'bad' : s.shadow ? 'warn' : ''),
    stat('Spent', ilsShort(s.cost), started ? `budget so far ${ilsShort(s.budget)}` : `budget ${ilsShort(scenario.money.budgetPerYear)} a year`, overBudget ? 'bad' : ''),
  );
}

function renderNow() {
  if (state.done) {
    view.nowHeading.textContent = 'Three years played';
    replace(view.now, h('p', {}, 'The debrief is below.'));
    return;
  }
  const label = quarterLabel(scenario, state.q);
  view.nowHeading.textContent = label;
  const ev = eventAt(scenario, state.q);
  const err = h('p', { class: 'callout callout-warn', role: 'alert', hidden: true }, 'Choose an answer first.');
  replace(view.now,
    ev ? h('fieldset', { class: 'group choices' },
      h('legend', {}, ev.title),
      h('p', {}, ev.text),
      ev.options.map((o) => {
        const id = `ev-${ev.id}-${o.id}`;
        const r = h('input', { type: 'radio', name: `ev-${ev.id}`, id, value: o.id, checked: pick === o.id });
        r.addEventListener('change', () => { if (r.checked) pick = o.id; });
        return h('div', { class: 'choice' }, r, h('label', { for: id }, o.text));
      })) : h('p', { class: 'muted' }, 'A quiet quarter: no event. Adjust the design if you want, then play it.'),
    err,
    h('div', { class: 'btn-row' }, button(`Play ${label}`, () => {
      if (ev && !pick) { err.hidden = false; focusEl(err); return; }
      onPlay();
    })),
  );
}

function onPlay() {
  state = playQuarter(state, config, scenario, pick || undefined);
  pick = null;
  for (const key of Object.keys(ROADS)) if (state.forced[key] !== undefined) config.roads[key] = true;
  renderDesign();
  renderAll();
  const last = state.history[state.history.length - 1];
  if (state.done) {
    renderDebrief();
    return;
  }
  focusEl(view.nowHeading);
  shell.announce(`${last.label}: ${num(last.prod)} in production, ${num(last.queue)} waiting for review. ${last.event ? last.event.result : ''} Now ${quarterLabel(scenario, state.q)}.`);
}

function renderUnits() {
  const rows = unitTable(state, scenario);
  replace(view.units, stackTable({
    caption: 'Pilots by unit and status',
    head: ['Unit', 'Building', 'Waiting', 'Live', 'Shadow', 'Stopped', 'Merged or gone'],
    rows: rows.map((r) => ({
      th: `${r.unit.name} (maturity ${r.unit.maturity})`,
      cells: [num(r.building), num(r.queue), num(r.prod), r.shadow ? h('span', { class: 'tag tag-bad' }, num(r.shadow)) : '0', num(r.stopped), num(r.other)],
    })),
  }));
}

function renderHistory() {
  if (!state.history.length) {
    replace(view.history, h('p', { class: 'muted' }, 'Nothing played yet.'));
    return;
  }
  const hs = state.history;
  const chart = hs.length >= 2 ? lineChart({
    title: 'Pilots in production, waiting for review and shadow tools',
    summary: `After ${hs[hs.length - 1].label}: ${num(hs[hs.length - 1].prod)} in production, ${num(hs[hs.length - 1].queue)} waiting, ${num(hs[hs.length - 1].shadow)} shadow tools.`,
    xLabel: 'Quarter', yLabel: 'Pilots',
    xFormat: (v) => `Q${num(v + 1)}`, tableX: (v) => quarterLabel(scenario, v), yFormat: (v) => num(v), zeroLine: true,
    series: [
      { name: 'In production', points: hs.map((x) => ({ x: x.q, y: x.prod })) },
      { name: 'Waiting for review', points: hs.map((x) => ({ x: x.q, y: x.queue })) },
      { name: 'Shadow tools', points: hs.map((x) => ({ x: x.q, y: x.shadow })) },
    ],
  }).el : null;
  replace(view.history,
    chart,
    h('ol', { class: 'qlog', reversed: true }, [...hs].reverse().map((x) => h('li', {},
      h('p', { class: 'q-head' }, h('strong', {}, x.label), ` · ${num(x.prod)} live · ${num(x.queue)} waiting · ${num(x.reviewed)} reviewed with ${num(x.slots)} slots · ${ilsShort(x.cost)}`),
      x.event ? h('p', { class: 'small' }, h('strong', {}, `${x.event.title}: `), x.event.answer, '. ', x.event.result) : null,
      x.notes.length ? h('ul', { class: 'small' }, x.notes.map((n) => h('li', {}, n))) : null))),
  );
}

const VERDICT = {
  scaled: ['Scaled, and safely.', 'good'],
  scaledUnsafe: ['Scaled, with incidents or a shadow estate to show for it.', 'warn'],
  stuck: ['Safe, but stuck: too little reached production.', 'warn'],
  neither: ['Stuck, and not safe either.', 'bad'],
};

function renderDebrief() {
  const d = debrief(state, config, scenario);
  const [headline, tone] = VERDICT[d.verdict];
  view.resultPanel.hidden = false;
  const row = (label, f) => ({ th: label, cells: [f(d.mine), f(d.expert), f(d.asIs), f(d.fed)] });
  replace(view.result,
    h('div', { class: `callout callout-${tone}` },
      h('p', {}, h('strong', {}, headline)),
      h('p', {}, `${num(d.mine.prod)} pilots in production after three years (the expert design: ${num(d.expert.prod)}), ${plural(d.mine.incidents, 'risk incident')}, ${plural(d.mine.shadow, 'shadow tool')} in use, ${plural(d.mine.duplicates, 'duplicate')}.`)),
    h('h3', {}, 'Your three years against three other designs'),
    h('p', { class: 'small muted' }, 'Same pilots, same events. “As the bank works today” and “Everyone for themselves” use the answers people usually give under pressure; the expert uses the expert’s answers.'),
    stackTable({
      caption: 'Results of your design, the expert design, the bank as it works today and a federated free-for-all',
      head: ['Result', 'You', 'Expert', 'As the bank works today', 'Everyone for themselves'],
      rows: [
        row('In production', (x) => num(x.prod)),
        row('Average wait for a decision', (x) => `${num(x.avgWait, 1)} quarters`),
        row('Waiting at the end', (x) => num(x.backlog)),
        row('Duplicates running', (x) => num(x.duplicates)),
        row('Risk incidents', (x) => num(x.incidents)),
        row('Weak models in production', (x) => num(x.weakInProd)),
        row('Shadow tools in use', (x) => num(x.shadow)),
        row('Cost over three years', (x) => ilsShort(x.cost)),
        row('Cost per pilot in production', (x) => (Number.isFinite(x.costPerProd) ? ilsShort(x.costPerProd) : '–')),
      ],
    }),
    h('h3', {}, 'Hub constants and spoke variables'),
    h('p', {}, 'What the centre should own is what must be the same everywhere; what the units should own is what differs by unit. Here is where your final design put each one.'),
    stackTable({
      caption: 'Who owns each part in your design and in the expert design',
      head: ['Part', 'Your design', 'Expert', 'Why'],
      rows: d.hubSpoke.map((x) => ({
        th: x.text,
        cells: [h('span', { class: `tag tag-${x.match ? 'good' : 'warn'}` }, x.mine === 'hub' ? 'the hub' : x.mine === 'spoke' ? 'the units' : 'nobody'),
          x.expert === 'hub' ? 'the hub' : 'the units', h('span', { class: 'small' }, x.why)],
      })),
    }),
    h('h3', {}, 'Your answers and the expert’s'),
    h('ul', {}, scenario.events.map((ev) => {
      const mineId = state.answers[ev.id];
      const mine = ev.options.find((o) => o.id === mineId);
      const ex = ev.options.find((o) => o.id === scenario.expert.answers[ev.id]);
      return h('li', {}, h('strong', {}, `${ev.title}: `), mine ? mine.text : 'not reached',
        mineId === ex.id ? h('span', {}, ' ', h('span', { class: 'tag tag-good' }, 'same as the expert')) : h('span', { class: 'small muted' }, ` (expert: ${ex.text.toLowerCase()})`));
    })),
    h('p', {}, h('strong', {}, 'The expert design: '), scenario.expert.why),
    h('h3', {}, 'The point of this lesson'),
    h('p', { class: 'lesson-point' }, scenario.lessonPoint),
    h('div', { class: 'btn-row' }, button('Play the three years again', () => { start(shell.presetKey); focusEl(view.nowHeading); }, { variant: 'secondary' })),
  );
  focusEl(view.resultHeading);
  shell.announce(`Three years played. ${headline}`);
}

shell = mountShell({
  title: 'Operating-model scaler',
  tagline: 'Design how AI pilots reach production across many units, then live with it for twelve quarters.',
  presets: PRESETS,
  defaultPreset: DEFAULT_PRESET,
  about: ABOUT,
  onPreset: start,
});
start(shell.presetKey);
