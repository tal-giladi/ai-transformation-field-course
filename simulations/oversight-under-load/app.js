import { h, replace, focusEl } from '../common/dom.js';
import { mountShell, panel } from '../common/shell.js';
import { rangeField, toggleField, button, stat } from '../common/controls.js';
import { lineChart } from '../common/chart.js';
import { pct, num, minutes, plural } from '../common/format.js';
import { simulate, checkTarget, loadCurve, checkTime, capacityScreen, K } from './model.js';
import { steps } from '../common/math.js';
import { PRESETS, DEFAULT_PRESET } from './presets.js';

const ABOUT = {
  intro: 'A review queue over two working weeks (Sunday to Thursday). Every AI output must be approved by a person before it goes out. Expected values, no randomness.',
  equations: [
    'Items today = items per day × weekday factor (Sun 1.25, Mon 1.05, Tue 0.95, Wed 0.90, Thu 0.85).',
    `Real check time = minutes for a real check × ${K.sourceSpeedup} if the source is shown beside the draft, else × 1. Rubber stamp = ${K.stampMinutes} min.`,
    'Capacity = reviewers × review hours per reviewer × 60 minutes. Load = items × real check time ÷ capacity.',
    'Time allows k real checks where k × check time + (items − k) × stamp time = capacity (0 ≤ k ≤ items). The queue is always cleared: the rest are approved without a check.',
    'Share really checked = (k ÷ items) × vigilance. Vigilance starts at 1.',
    `A real check catches a wrong item with ${pct(K.catchChecked)} chance (${pct(K.catchCheckedSource)} with the source shown); a rubber stamp catches ${pct(K.catchStamped)} (the blatant ones).`,
    'Errors reaching customers = wrong items − caught.',
    `Vigilance tomorrow: flag feedback on → recovers ${pct(K.recovery)} of the gap to 1; off → falls ${pct(K.decayNoFeedback)} (and another ${pct(K.decayUsuallyRight)} if under 10% of items are wrong: the tool is "usually right"). Overload (load > 1) takes another ${pct(K.fatigue)} per unit of overload. Never below ${pct(K.minVigilance)}.`,
    'Capacity screen = 60 ÷ real check time: the most items one reviewer-hour can give a real check.',
    'Utilisation = (real checks × check time + stamps × stamp time) ÷ capacity. Above 100% means overtime.',
  ],
  assumptions: [
    'Reviewers are competent and have the authority to reject; this model is only about time, information and vigilance.',
    'Flag feedback on means every flag gets an answer within a day and the prompt or rule is fixed; off means flags go into a box nobody reads.',
    'Showing the source (the customer email, the order, the policy line) beside the draft makes a check faster and better.',
  ],
  leftOut: [
    'Day-to-day randomness, individual differences between reviewers, and learning over months.',
    'Errors that no reviewer could catch because the information is not on the screen at all.',
  ],
};

const FIELDS = [
  { key: 'itemsPerDay', label: 'Items per day (average)', min: 10, max: 1000, step: 5, unit: 'items', fmt: (v) => num(v) },
  { key: 'reviewers', label: 'Reviewers', min: 1, max: 20, step: 1, unit: 'people', fmt: (v) => num(v) },
  { key: 'hoursPerReviewer', label: 'Review hours per reviewer per day', min: 0.5, max: 8, step: 0.25, unit: 'h', fmt: (v) => `${num(v, 2)} h` },
  { key: 'errorRate', label: 'Share of AI outputs that are wrong', scale: 100, min: 1, max: 50, step: 1, unit: '%', fmt: (v) => `${num(v)}%` },
  { key: 'checkMinutes', label: 'Minutes for a real check', min: 0.5, max: 15, step: 0.25, unit: 'min', fmt: (v) => minutes(v, 2), help: 'Without the source beside the draft.' },
];

let shell;
let params;
let fields = {};
let view = {};
let debriefShown = false;

const preset = () => PRESETS[shell.presetKey];

function start(key) {
  params = { ...PRESETS[key].params };
  debriefShown = false;
  build();
  update();
}

function build() {
  fields = {};
  const p = preset();
  const inputs = panel('Your review design', { id: 'inputs' });
  const target = h('div', { class: 'callout' },
    h('p', {}, h('strong', {}, 'Target: '),
      `no more than ${plural(p.target.maxEscaped, `wrong ${p.item}`, `wrong ${p.items}`)} reach customers in two weeks, `,
      `with at most ${num(p.target.maxReviewerHoursPerDay)} reviewer-hours a day.`));
  const load = h('fieldset', { class: 'group' }, h('legend', {}, 'Queue and people'));
  for (const f of FIELDS) {
    const scale = f.scale || 1;
    const field = rangeField({
      label: f.label, min: f.min, max: f.max, step: f.step, unit: f.unit, help: f.help,
      value: Number((params[f.key] * scale).toFixed(4)), format: f.fmt,
      onInput: (v) => { params[f.key] = v / scale; update(); },
    });
    fields[f.key] = { field, scale };
    load.appendChild(field.el);
  }
  const design = h('fieldset', { class: 'group' }, h('legend', {}, 'How the check is designed'),
    toggleField({
      label: 'Source shown beside the draft',
      checked: params.sourceShown,
      help: 'The customer’s email, the order and the policy line sit next to the draft. Faster and better checks.',
      onChange: (v) => { params.sourceShown = v; update(); },
    }).el,
    toggleField({
      label: 'Flag feedback on',
      checked: params.flagFeedback,
      help: 'Every flag gets an answer and a fix within a day. Off: flags go into a box nobody reads.',
      onChange: (v) => { params.flagFeedback = v; update(); },
    }).el,
  );
  inputs.body.append(target, load, design,
    h('div', { class: 'btn-row' }, button('Reset to the scenario', () => start(shell.presetKey), { variant: 'secondary' })));
  if (p.notes && p.notes.length) {
    inputs.body.appendChild(h('details', { class: 'notes' }, h('summary', {}, 'Where these numbers come from'),
      h('ul', {}, p.notes.map((n) => h('li', {}, n)))));
  }

  view.stats = h('div', { class: 'stats' });
  view.screen = h('div', { role: 'status' });
  view.dayChart = lineChart({ title: '', series: [{ name: '', points: [{ x: 1, y: 0 }, { x: 2, y: 0 }] }] });
  view.dayTable = h('div', { class: 'table-wrap' });
  view.curve = lineChart({ title: '', series: [{ name: '', points: [{ x: 1, y: 0 }, { x: 2, y: 0 }] }] });

  const results = panel('Two working weeks', { id: 'results' });
  results.body.append(view.stats, view.screen, view.dayChart.el,
    h('details', { class: 'notes' }, h('summary', {}, 'Day by day, with errors reaching customers'), view.dayTable));
  const curve = panel('What happens as the queue grows', { id: 'curve' });
  curve.body.append(
    h('p', { class: 'muted small' }, 'Share of wrong items caught over the two weeks, while the daily volume moves and everything else stays as you set it.'),
    view.curve.el);

  const debrief = panel('Debrief', { id: 'debrief', className: 'debrief' });
  view.debrief = h('div');
  view.debriefButton = button('Check my design', () => {
    debriefShown = true;
    renderDebrief();
    focusEl(debrief.heading);
  });
  debrief.body.append(h('p', {}, 'When you think your design meets the target, check it. You can change it and check again.'), view.debriefButton, view.debrief);

  replace(shell.main,
    h('div', { class: 'layout layout-2' }, inputs.el, h('div', { class: 'stack' }, results.el, curve.el)),
    debrief.el);
}

function update() {
  const p = preset();
  const run = simulate(params);
  const t = run.totals;
  const ok = t.escaped <= p.target.maxEscaped;
  const hoursOk = t.reviewerHoursPerDay <= p.target.maxReviewerHoursPerDay;

  replace(view.stats,
    stat(`Wrong ${p.items} reaching customers`, num(t.escaped), `of ${num(t.wrong)} wrong, target ≤ ${num(p.target.maxEscaped)}`, ok ? 'good' : 'bad'),
    stat('Catch rate', pct(t.catchRate), 'wrong items caught'),
    stat('Approved without a check', pct(t.stampShare), 'rubber stamps', t.stampShare > 0.2 ? 'bad' : t.stampShare > 0.05 ? 'warn' : ''),
    stat('Reviewer utilisation', pct(t.avgUtilisation), `average; peak ${pct(t.maxUtilisation)}`, t.maxUtilisation > 1 ? 'warn' : ''),
    stat('Reviewer-hours a day', num(t.reviewerHoursPerDay, 2), `limit ${num(p.target.maxReviewerHoursPerDay)}`, hoursOk ? '' : 'bad'),
    stat('Vigilance on the last day', pct(t.finalVigilance), 'share of the time they really look', t.finalVigilance < 0.8 ? 'warn' : ''),
  );

  const screen = capacityScreen(params);
  const over = t.peakItemsPerReviewerHour > screen;
  replace(view.screen, h('div', { class: `callout ${over ? 'callout-bad' : 'callout-good'}` },
    h('p', {}, h('strong', {}, 'Capacity screen: '),
      `a real check takes ${minutes(checkTime(params), 2)}, so one reviewer-hour can give a real check to at most ${num(screen, 1)} ${p.items}. `,
      `You are asking for ${num(t.itemsPerReviewerHour, 1)} on an average day and ${num(t.peakItemsPerReviewerHour, 1)} on Sunday.`),
    over ? h('p', {}, 'Above the screen, the queue is still cleared on time and the dashboard still says “reviewed”. The difference is approved without a check.') : null,
    !over && !params.flagFeedback ? h('p', {}, 'There is time to check, yet vigilance is falling: flags go nowhere, so people stop looking. Watch the vigilance line.') : null,
  ));

  view.dayChart.update({
    title: 'Day by day',
    summary: `Over ten working days the share really checked goes from ${pct(run.days[0].realShare)} to ${pct(run.days[run.days.length - 1].realShare)}.`,
    xLabel: 'Working day', yLabel: 'Percent',
    xFormat: (v) => `${num(v)}`, tableX: (v) => `Day ${v} (${run.days[v - 1].name})`,
    yFormat: (v) => pct(v), zeroLine: true,
    series: [
      { name: 'Wrong items caught', points: run.days.map((d) => ({ x: d.day, y: d.catchRate })) },
      { name: 'Items really checked', points: run.days.map((d) => ({ x: d.day, y: d.realShare })) },
      { name: 'Vigilance', points: run.days.map((d) => ({ x: d.day, y: d.vigilance })) },
      { name: 'Utilisation', points: run.days.map((d) => ({ x: d.day, y: d.utilisation })) },
    ],
  });

  replace(view.dayTable, h('table', {},
    h('caption', { class: 'sr-only' }, 'Day by day results'),
    h('thead', {}, h('tr', {}, ['Day', 'Items', 'Load', 'Really checked', 'Vigilance', 'Wrong', 'Reached customers', 'Utilisation'].map((c) => h('th', { scope: 'col' }, c)))),
    h('tbody', {}, run.days.map((d) => h('tr', {},
      h('th', { scope: 'row' }, `${d.day} ${d.name}`),
      h('td', {}, num(d.items)), h('td', {}, pct(d.load)), h('td', {}, pct(d.realShare)), h('td', {}, pct(d.vigilance)),
      h('td', {}, num(d.wrong, 1)), h('td', {}, num(d.escaped, 1)), h('td', {}, pct(d.utilisation)))))));

  const maxVol = Math.max(60, Math.ceil((params.itemsPerDay * 3) / 10) * 10);
  const vols = steps(Math.max(5, Math.round(maxVol / 20)), maxVol, 20).map((v) => Math.round(v));
  const best = { ...params, sourceShown: true, flagFeedback: true };
  const screenVolume = capacityScreen(params) * params.reviewers * params.hoursPerReviewer;
  view.curve.update({
    title: 'Catch rate vs items per day',
    summary: `With your design the catch rate starts to fall at about ${num(screenVolume)} items a day, where the capacity screen is reached.`,
    xLabel: 'Items per day (average)', yLabel: 'Wrong items caught',
    xFormat: (v) => num(v), yFormat: (v) => pct(v), zeroLine: true,
    marker: { x: params.itemsPerDay, label: `you: ${num(params.itemsPerDay)} a day` },
    series: [
      { name: 'Your design', points: loadCurve(params, vols) },
      ...(params.sourceShown && params.flagFeedback ? [] : [{ name: 'Same people, source shown + flag feedback on', points: loadCurve(best, vols) }]),
    ],
  });

  if (debriefShown) renderDebrief();
}

function renderDebrief() {
  const p = preset();
  const res = checkTarget(params, p.target);
  const t = res.totals;
  const lines = [];
  if (res.met) lines.push(h('div', { class: 'callout callout-good' }, h('p', {}, `Target met: ${num(t.escaped, 1)} wrong ${p.items} reach customers with ${num(t.reviewerHoursPerDay, 2)} reviewer-hours a day.`)));
  else {
    const why = [];
    if (!res.withinErrors) why.push(`${num(t.escaped, 1)} wrong ${p.items} reach customers (target ≤ ${num(p.target.maxEscaped)})`);
    if (!res.withinHours) why.push(`the design needs ${num(t.reviewerHoursPerDay, 2)} reviewer-hours a day (limit ${num(p.target.maxReviewerHoursPerDay)})`);
    lines.push(h('div', { class: 'callout callout-bad' }, h('p', {}, `Not yet: ${why.join(', and ')}.`)));
  }
  const pts = [];
  if (!params.sourceShown) pts.push('The source is not beside the draft, so a real check is slow and misses more. This is usually the cheapest fix: it changes the screen, not the headcount.');
  if (!params.flagFeedback) pts.push(`Flags go nowhere, so vigilance fell to ${pct(t.finalVigilance)} by the last day, even on days with time to spare. People stop reporting what nobody fixes, and then stop looking.`);
  if (t.peakItemsPerReviewerHour > t.screen) pts.push(`On Sunday you ask for ${num(t.peakItemsPerReviewerHour, 1)} ${p.items} per reviewer-hour; the screen is ${num(t.screen, 1)}. Above the screen the queue is still cleared: the difference is rubber-stamped.`);
  if (params.errorRate < 0.1 && !params.flagFeedback) pts.push('The tool is usually right, which makes checking feel pointless. That is when vigilance drops fastest.');
  if (t.avgUtilisation < 0.85 && t.catchRate < 0.8) pts.push(`Utilisation looks comfortable (${pct(t.avgUtilisation)}) while only ${pct(t.catchRate)} of wrong items are caught. Utilisation does not tell you whether anyone checked.`);
  if (res.met) pts.push('Notice what did the work: the design of the check, not just more reviewers. Adding people without the source or the feedback loop buys little.');
  pts.push(`When a wrong ${p.item} reaches a customer, ask first whether the reviewer had the time and the information: on Sunday this design gives ${minutes(60 / t.peakItemsPerReviewerHour, 1)} per ${p.item} against ${minutes(checkTime(params), 1)} for a real check. Blaming a reviewer for a design failure teaches people to stop flagging.`);

  view.debriefButton.textContent = 'Check my design again';
  replace(view.debrief,
    ...lines,
    h('ul', {}, pts.map((x) => h('li', {}, x))),
    h('h3', {}, 'The point of this lesson'),
    h('p', { class: 'lesson-point' },
      'A human check only counts when the reviewer has the time, the information and a reason to keep looking. ' +
      'Size review with the capacity screen, put the source beside the draft and make every flag go somewhere. ' +
      'Otherwise rising load turns review into rubber-stamping while the dashboard still says “reviewed”.'),
  );
  shell.announce(res.met ? 'Target met.' : 'Target not met yet.');
}

shell = mountShell({
  title: 'Oversight under load',
  tagline: 'A review queue over two working weeks: load, rubber-stamping, and the capacity screen.',
  presets: PRESETS,
  defaultPreset: DEFAULT_PRESET,
  about: ABOUT,
  onPreset: start,
});
start(shell.presetKey);
