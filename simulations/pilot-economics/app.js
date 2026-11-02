import { h, replace, focusEl } from '../common/dom.js';
import { mountShell, panel } from '../common/shell.js';
import { rangeField, button, stat } from '../common/controls.js';
import { lineChart, barChart } from '../common/chart.js';
import { ils, ilsShort, pct, hours, num, usd, monthsText, minutes } from '../common/format.js';
import { compute, sweep, steps, FTE_HOURS_PER_MONTH } from './model.js';
import { PRESETS, DEFAULT_PRESET } from './presets.js';

// UI fields. scale: shown value = parameter x scale (percentages are shown as 0-100).
const GROUPS = [
  {
    title: 'Volume and quality',
    fields: [
      { key: 'volume', label: 'Items per month in scope', min: 100, max: 20000, step: 100, unit: 'items', fmt: (v) => num(v) },
      { key: 'automationRate', label: 'Automation rate', scale: 100, min: 0, max: 100, step: 5, unit: '%', fmt: (v) => `${num(v)}%`, help: 'Share of the items the AI handles at all.' },
      { key: 'accuracy', label: 'Accuracy', scale: 100, min: 50, max: 100, step: 1, unit: '%', fmt: (v) => `${num(v)}%`, help: 'Share of AI outputs a careful reviewer would send unchanged. Measure it on your own test set.' },
    ],
  },
  {
    title: 'Human minutes',
    fields: [
      { key: 'minutesSaved', label: 'Minutes saved per right output', min: 0, max: 30, step: 0.5, unit: 'min', fmt: (v) => minutes(v) },
      { key: 'reviewMinutes', label: 'Review minutes per item', min: 0, max: 15, step: 0.25, unit: 'min', fmt: (v) => minutes(v, 2), help: 'Every AI-handled item is checked by a person. This is where the human check sits.' },
      { key: 'reworkMinutes', label: 'Rework minutes per wrong output', min: 0, max: 30, step: 0.5, unit: 'min', fmt: (v) => minutes(v), help: 'Extra time to fix a wrong draft, on top of the review.' },
      { key: 'hourlyCost', label: 'Fully loaded hourly cost', min: 40, max: 400, step: 5, unit: '₪/h', fmt: (v) => ils(v) },
    ],
  },
  {
    title: 'Tokens',
    fields: [
      { key: 'tokensIn', label: 'Input tokens per item', min: 0, max: 20000, step: 100, unit: 'tokens', fmt: (v) => num(v) },
      { key: 'tokensOut', label: 'Output tokens per item', min: 0, max: 5000, step: 50, unit: 'tokens', fmt: (v) => num(v) },
      { key: 'priceIn', label: 'Price per million input tokens', min: 0, max: 30, step: 0.05, unit: 'US$', fmt: (v) => usd(v) },
      { key: 'priceOut', label: 'Price per million output tokens', min: 0, max: 100, step: 0.5, unit: 'US$', fmt: (v) => usd(v) },
      { key: 'fx', label: 'Exchange rate', min: 2.5, max: 5, step: 0.01, unit: '₪ per $', fmt: (v) => `₪${num(v, 2)} per $` },
    ],
  },
  {
    title: 'Fixed costs',
    fields: [
      { key: 'fixedMonthly', label: 'Fixed monthly costs', min: 0, max: 50000, step: 500, unit: '₪', fmt: (v) => ils(v), help: 'Licences, hosting, monitoring, the monthly sampled quality review.' },
      { key: 'buildCost', label: 'One-off build cost', min: 0, max: 1000000, step: 5000, unit: '₪', fmt: (v) => ils(v) },
    ],
  },
];

const ABOUT = {
  intro: 'A one-month ledger of minutes and shekels for an AI step with a person checking every output. It shows where the value comes from and where it goes.',
  equations: [
    'Handled = items per month × automation rate. Right = handled × accuracy. Wrong = handled − right.',
    'Minutes saved = right × minutes saved per right output.',
    'Checking minutes = handled × review minutes + wrong × rework minutes.',
    'Net hours = (minutes saved − checking minutes) ÷ 60. This is capacity: time freed, not cash.',
    'Value of freed time = net hours × fully loaded hourly cost.',
    'Token cost (₪) = handled × (input tokens × input price + output tokens × output price) ÷ 1,000,000 × exchange rate.',
    'Monthly net value = value of freed time − token cost − fixed monthly costs.',
    'Breakeven months = one-off build cost ÷ monthly net value (never, if the monthly net value is zero or less).',
    `FTE = net hours ÷ ${FTE_HOURS_PER_MONTH} (a 42-hour week).`,
  ],
  assumptions: [
    'Every AI-handled item is reviewed; every wrong output is caught and fixed (escaped errors are modelled in oversight-under-load).',
    'Items the AI does not handle are done the old way and change nothing.',
    'Freed hours are worth the hourly cost only if they are used: absorbed peak load, avoided hires or overtime, or work that was not getting done.',
    'Token prices and the exchange rate are examples; put in today’s numbers.',
  ],
  leftOut: [
    'Discounting and NPV (lesson 03.7 does this in the spreadsheet).',
    'Ramp-up: the first months run below these numbers while people learn the tool.',
    'The cost of an error that reaches a customer.',
  ],
};

let shell;
let params;
let fields = {};
let view = {};
let debriefShown = false;

function preset() {
  return PRESETS[shell.presetKey];
}

function start(key) {
  params = { ...PRESETS[key].params };
  debriefShown = false;
  build();
  update();
}

function build() {
  fields = {};
  const inputs = panel('Inputs', { id: 'inputs' });
  for (const g of GROUPS) {
    const group = h('fieldset', { class: 'group' }, h('legend', {}, g.title));
    for (const f of g.fields) {
      const scale = f.scale || 1;
      const field = rangeField({
        label: f.label, min: f.min, max: f.max, step: f.step, unit: f.unit, help: f.help,
        value: round(params[f.key] * scale),
        format: f.fmt,
        onInput: (v) => {
          params[f.key] = v / scale;
          update();
        },
      });
      fields[f.key] = { field, scale };
      group.appendChild(field.el);
    }
    inputs.body.appendChild(group);
  }
  inputs.body.appendChild(h('div', { class: 'btn-row' },
    button('Reset to the scenario’s numbers', () => {
      params = { ...preset().params };
      for (const [k, { field, scale }] of Object.entries(fields)) field.set(round(params[k] * scale));
      update();
      shell.announce('Inputs reset to the scenario’s numbers.');
    }, { variant: 'secondary' })));
  const notes = preset().notes || [];
  if (notes.length) {
    inputs.body.appendChild(h('details', { class: 'notes' },
      h('summary', {}, 'Where these numbers come from'),
      h('ul', {}, notes.map((n) => h('li', {}, n)))));
  }

  view.stats = h('div', { class: 'stats' });
  view.callout = h('div', { role: 'status' });
  view.ledger = barChart({ title: 'Hours per month', items: [] , format: hours });
  view.money = h('div', { class: 'table-wrap' });
  view.accChart = lineChart({ title: '', series: [{ name: '', points: [{ x: 0, y: 0 }, { x: 1, y: 0 }] }] });
  view.revChart = lineChart({ title: '', series: [{ name: '', points: [{ x: 0, y: 0 }, { x: 1, y: 0 }] }] });

  const results = panel('Results', { id: 'results' });
  results.body.append(view.stats, view.callout, view.ledger.el, h('h3', {}, 'Money per month'), view.money);
  const charts = panel('Where the value disappears', { id: 'charts' });
  charts.body.append(
    h('p', { class: 'muted small' }, 'Each line is the monthly net value while one input moves and the rest stay as you set them. Below the dark zero line the pilot loses money.'),
    view.accChart.el, view.revChart.el);

  view.debrief = h('div');
  const debrief = panel('Debrief', { id: 'debrief', className: 'debrief' });
  view.debriefButton = button('I have explored — show the debrief', () => {
    debriefShown = true;
    renderDebrief(compute(params));
    focusEl(debrief.heading);
  });
  debrief.body.append(
    h('p', {}, 'Before you open it, write down: the accuracy below which the pilot loses money, and the review minutes per item it can afford.'),
    view.debriefButton, view.debrief);

  replace(shell.main,
    h('div', { class: 'layout layout-2' }, inputs.el, h('div', { class: 'stack' }, results.el, charts.el)),
    debrief.el);
}

function round(v) {
  return Number(v.toFixed(4));
}

function update() {
  const r = compute(params);
  const p = preset();

  replace(view.stats,
    stat('Monthly net value', ils(r.monthlyNet), 'after checking, tokens and fixed costs', r.monthlyNet > 0 ? 'good' : 'bad'),
    stat('Net hours freed', hours(r.netHours), `capacity, not cash ≈ ${num(r.fte, 2)} FTE`, r.netHours > 0 ? '' : 'bad'),
    stat('Breakeven', monthsText(r.breakevenMonths), `on a ${ils(params.buildCost)} build`, Number.isFinite(r.breakevenMonths) && r.breakevenMonths <= 12 ? 'good' : 'warn'),
    stat('First-year net', ils(r.firstYearNet), '12 months minus the build', r.firstYearNet >= 0 ? '' : 'warn'),
    stat('Checking eats', Number.isFinite(r.checkingShare) ? pct(r.checkingShare) : '–', 'of the minutes saved', r.reviewEatsSaving ? 'bad' : r.checkingShare > 0.5 ? 'warn' : ''),
    stat('Run cost per item', ils(r.costPerItem, 2), `${p.item}: tokens + fixed costs`),
  );

  let tone;
  let msg;
  if (r.reviewEatsSaving) {
    tone = 'bad';
    msg = `Human review and rework eat the whole saving: ${hours(r.grossHours)} saved, ${hours(r.reviewHours + r.reworkHours)} spent checking and fixing. The AI makes this work slower.`;
  } else if (r.monthlyNet <= 0) {
    tone = 'bad';
    msg = `The checking leaves ${hours(r.netHours)} a month, worth ${ils(r.capacityValue)}, which does not cover ${ils(r.runCost)} of tokens and fixed costs.`;
  } else if (r.checkingShare > 0.5) {
    tone = 'warn';
    msg = `Checking eats ${pct(r.checkingShare)} of the time saved. A small change in review minutes moves this pilot a lot.`;
  } else {
    tone = 'good';
    msg = `Checking eats ${pct(r.checkingShare)} of the time saved. The pilot pays back in ${monthsText(r.breakevenMonths)}.`;
  }
  const limits = [];
  if (Number.isFinite(r.breakevenAccuracy) && r.breakevenAccuracy > 0 && r.breakevenAccuracy < 1) limits.push(`accuracy falls below ${pct(r.breakevenAccuracy, 1)}`);
  if (Number.isFinite(r.maxReviewMinutes) && r.maxReviewMinutes > 0) limits.push(`a review takes more than ${minutes(r.maxReviewMinutes, 2)} per ${p.item}`);
  replace(view.callout, h('div', { class: `callout callout-${tone}` },
    h('p', {}, msg),
    limits.length ? h('p', {}, `It loses money if ${limits.join(' or if ')}.`) : null));

  view.ledger.update({
    title: 'Hours per month',
    summary: `Saved ${hours(r.grossHours)}, review ${hours(r.reviewHours)}, rework ${hours(r.reworkHours)}, net ${hours(r.netHours)}.`,
    format: (v) => hours(v),
    items: [
      { label: 'Saved on right outputs', value: r.grossHours, tone: 'good' },
      { label: 'Review', value: -r.reviewHours, tone: 'bad' },
      { label: 'Rework on wrong outputs', value: -r.reworkHours, tone: 'bad' },
      { label: 'Net hours', value: r.netHours, tone: r.netHours >= 0 ? 'neutral' : 'bad' },
    ],
  });

  replace(view.money, h('table', {},
    h('caption', { class: 'sr-only' }, 'Money per month'),
    h('tbody', {},
      row(`Value of freed time (${hours(r.netHours)} × ${ils(params.hourlyCost)})`, ils(r.capacityValue)),
      row(`Tokens (${usd(r.tokenUsd)} at ₪${num(params.fx, 2)})`, ils(-r.tokenIls)),
      row('Fixed monthly costs', ils(-params.fixedMonthly)),
      row('Monthly net value', ils(r.monthlyNet), true),
    )));

  const accVals = steps(0.5, 1, 25);
  const halfReview = params.reviewMinutes / 2;
  view.accChart.update({
    title: 'Monthly net value vs accuracy',
    summary: `At your review minutes the pilot breaks even at about ${pct(r.breakevenAccuracy, 1)} accuracy.`,
    xLabel: 'Accuracy', yLabel: 'Net value per month',
    xFormat: (v) => pct(v), yFormat: ilsShort, tableY: (v) => ils(v),
    zeroLine: true,
    marker: { x: params.accuracy, label: `you: ${pct(params.accuracy)}` },
    series: [
      { name: `Review ${minutes(params.reviewMinutes, 2)} (yours)`, points: sweep(params, 'accuracy', accVals) },
      { name: `Review halved (${minutes(halfReview, 2)})`, points: sweep({ ...params, reviewMinutes: halfReview }, 'accuracy', accVals) },
    ],
  });

  const revMax = Math.max(6, Math.ceil(Math.max(params.minutesSaved * 1.25, params.reviewMinutes * 1.5)));
  const revVals = steps(0, revMax, 24);
  const accHigh = Math.max(params.accuracy, 0.95);
  view.revChart.update({
    title: 'Monthly net value vs review minutes per item',
    summary: `At your accuracy the pilot loses money once a review takes more than ${minutes(r.maxReviewMinutes, 2)}.`,
    xLabel: 'Review minutes per item', yLabel: 'Net value per month',
    xFormat: (v) => num(v, v % 1 ? 1 : 0), yFormat: ilsShort, tableX: (v) => minutes(v, 2), tableY: (v) => ils(v),
    zeroLine: true,
    marker: { x: params.reviewMinutes, label: `you: ${minutes(params.reviewMinutes, 2)}` },
    series: [
      { name: `Accuracy ${pct(params.accuracy)} (yours)`, points: sweep(params, 'reviewMinutes', revVals) },
      ...(accHigh > params.accuracy ? [{ name: `Accuracy ${pct(accHigh)}`, points: sweep({ ...params, accuracy: accHigh }, 'reviewMinutes', revVals) }] : []),
    ],
  });

  if (debriefShown) renderDebrief(r);
}

function row(label, value, strong = false) {
  return h('tr', {}, h('th', { scope: 'row' }, strong ? h('strong', {}, label) : label), h('td', {}, strong ? h('strong', {}, value) : value));
}

function renderDebrief(r) {
  view.debriefButton.hidden = true;
  const p = preset();
  const peak = shell.presetKey === 'harbor'
    ? ' At Harbor & Pine the hours are worth money because the team runs at about 92% in peak season: freed time replaces overtime and temporary staff, not salaries.'
    : ' Ask the budget owner which line the freed hours will show up in: avoided hires, overtime, or backlog. If none, the money is not real yet.';
  replace(view.debrief,
    h('h3', {}, 'What your numbers say'),
    h('ul', {},
      h('li', {}, `Checking (review + rework) is ${hours(r.reviewHours + r.reworkHours)} a month against ${hours(r.grossHours)} saved: ${Number.isFinite(r.checkingShare) ? pct(r.checkingShare) : 'all'} of the saving.`),
      h('li', {}, Number.isFinite(r.breakevenAccuracy) && r.breakevenAccuracy < 1
        ? `Breakeven accuracy: ${pct(r.breakevenAccuracy, 1)}. Breakeven review time: ${minutes(Math.max(0, r.maxReviewMinutes), 2)} per ${p.item}.`
        : 'At these settings no accuracy makes the pilot pay: the checking and fixed costs are larger than the best-case saving.'),
      h('li', {}, `Tokens cost ${ils(r.tokenIls)} a month. They are rarely the problem: the money is in people’s minutes.`),
      h('li', {}, `The ${hours(r.netHours)} freed is capacity (${num(r.fte, 2)} FTE), not cash.${peak}`),
    ),
    h('h3', {}, 'The point of this lesson'),
    h('p', { class: 'lesson-point' },
      'A pilot’s value is decided by where the human check sits and how many minutes a real check takes, not by the model’s accuracy alone. ' +
      'Put the review minutes from the check you will actually run into the model, show the breakeven accuracy next to the eval result, and call freed hours capacity until someone owns turning them into money.'),
    h('p', { class: 'muted small' }, 'Next: the 2 minutes in a spreadsheet is a guess. In oversight-under-load you see what a real check takes and what happens to it when the queue grows.'),
  );
}

shell = mountShell({
  title: 'Pilot economics',
  tagline: 'Volume × automation × accuracy × human review × tokens → net value and breakeven.',
  presets: PRESETS,
  defaultPreset: DEFAULT_PRESET,
  about: ABOUT,
  onPreset: start,
});
start(shell.presetKey);
