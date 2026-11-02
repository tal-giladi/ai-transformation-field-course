import { h, replace, focusEl } from '../common/dom.js';
import { mountShell, panel } from '../common/shell.js';
import { button, stat } from '../common/controls.js';
import { stackTable } from '../common/table.js';
import { ils, num, pct, hours, monthsText } from '../common/format.js';
import { sponsorDecisions, totals, npv, paybackMonths, summary, truthDecisions, LEDGERS, LABELS, CLASSES } from './model.js';
import { PRESETS, DEFAULT_PRESET } from './presets.js';

const ABOUT = {
  intro: 'A finance review of one case. The claims, the possible adjustments and the right answers are written in advance; you decide how to net, label and classify each claim.',
  equations: [
    'Net value of a claim = the claimed ₪ a year + the adjustments you apply (most are negative). One adjustment moves value from one claim to another instead.',
    'Scenarios: low counts measured claims only; expected adds directional ones; high adds assumed ones. The case is judged on the expected scenario.',
    'Cash claims go into the NPV. Capacity claims are shown in hours (₪ ÷ the hourly cost) and are not cash.',
    'NPV = −build cost + the sum over three years of (expected cash − running cost) ÷ (1 + hurdle rate)^year. Payback = build cost ÷ (expected cash − running cost), in months.',
    'Approval is decided by the total cost over three years (build + three years of running cost), not by the build cost alone.',
    'The review: a claim labelled more certain than it is, or capacity called cash, is rejected; a missed adjustment means the CFO reworks it; adjustments that are not real or labels that are too cautious understate it. Credibility = 100 − 15 per rejection − 8 per rework − 4 per understatement.',
  ],
  assumptions: [
    'Benefits are flat from year one. Real benefits ramp up, and the temps saving only arrives at the next peak.',
    'Every adjustment is either right or wrong. Real netting is a range; the CFO wants your reasoning as much as your number.',
  ],
  leftOut: [
    'Tax, depreciation and the finance template’s other lines.',
    'The cost of the expensive error (a wrong refund, a privacy incident): incident-tabletop shows one.',
  ],
};

let shell;
let scenario;
let decisions;
let approvalPick = null;
let refs = {};
let view = {};

function start(key) {
  scenario = PRESETS[key];
  decisions = sponsorDecisions(scenario);
  approvalPick = null;
  refs = {};
  build();
  refresh();
}

const signed = (n) => (n > 0 ? `+${ils(n)}` : ils(n));
const nth = (i) => `Claim ${i + 1}`;

function build() {
  view.status = h('div', { class: 'stats' });
  const claims = panel('Michal’s claims', { id: 'claims' });
  claims.body.append(
    h('p', { class: 'small muted' }, 'Each card starts as Michal’s deck has it: nothing netted, labelled measured, counted as cash.'),
    h('div', { class: 'cards' }, scenario.claims.map((c, i) => buildCard(c, i))),
  );
  if (scenario.notes && scenario.notes.length) {
    claims.body.append(h('details', { class: 'notes' }, h('summary', {}, 'Where these numbers come from'),
      h('ul', {}, scenario.notes.map((n) => h('li', {}, n)))));
  }

  const send = panel('Before it goes to Ronit', { id: 'send', className: 'debrief' });
  view.sendHeading = send.heading;
  view.send = h('div');
  send.body.append(view.send);
  renderSend();

  replace(shell.main, view.status, claims.el, send.el);
}

function buildCard(c, i) {
  const r = { boxes: [] };
  const headingId = `claim-${c.id}`;
  const adjust = h('fieldset', { class: 'group ledgers' }, h('legend', {}, 'Net it across the ledgers'),
    c.adjustments.map((a) => {
      const id = `adj-${c.id}-${a.id}`;
      const box = h('input', { type: 'checkbox', id });
      box.addEventListener('change', () => {
        const d = decisions[c.id];
        d.applied = box.checked ? [...d.applied, a.id] : d.applied.filter((x) => x !== a.id);
        refresh();
      });
      r.boxes.push(box);
      return h('div', { class: 'adj' }, box, h('label', { for: id },
        h('span', { class: `tag ledger-${a.ledger}` }, LEDGERS[a.ledger].label), ' ', a.text,
        h('span', { class: 'amount' }, ` ${signed(a.amount)}${a.target ? ` (from ${nth(scenario.claims.findIndex((x) => x.id === a.target)).toLowerCase()})` : ''}`)));
    }));
  const lid = `label-${c.id}`;
  const cid = `class-${c.id}`;
  r.label = h('select', { id: lid }, Object.entries(LABELS).map(([k, l]) => h('option', { value: k, selected: k === c.deckLabel }, l.label)));
  r.cls = h('select', { id: cid }, Object.entries(CLASSES).map(([k, l]) => h('option', { value: k, selected: k === c.deckClass }, l.label)));
  r.label.addEventListener('change', () => { decisions[c.id].label = r.label.value; refresh(); });
  r.cls.addEventListener('change', () => { decisions[c.id].cls = r.cls.value; refresh(); });
  r.net = h('p', { class: 'net', 'aria-live': 'polite' });
  r.review = h('div', { class: 'review', hidden: true });
  r.el = h('article', { class: 'card claim', 'aria-labelledby': headingId },
    h('h3', { id: headingId }, `${nth(i)}. ${c.title}`),
    h('p', { class: 'claimed' }, `Claimed: ${ils(c.claimed)} a year`),
    h('p', { class: 'small' }, c.basis),
    adjust,
    h('div', { class: 'pickers' },
      h('div', { class: 'picker' }, h('label', { for: lid }, 'Evidence label'), r.label),
      h('div', { class: 'picker' }, h('label', { for: cid }, 'Cash or capacity'), r.cls)),
    r.net,
    r.review,
  );
  refs[c.id] = r;
  return r.el;
}

function refresh() {
  const t = totals(scenario, decisions);
  for (const c of scenario.claims) {
    const d = decisions[c.id];
    const n = t.nets[c.id];
    const counted = d.label !== 'assumed';
    refs[c.id].net.textContent = `Your net: ${ils(n)} a year, ${d.cls === 'cash' ? 'cash' : `capacity (${hours(n / scenario.hourlyCost, 0)})`}; ` +
      `${counted ? 'counts in the expected case' : 'upside only (assumed claims count only in the high case)'}.`;
  }
  const k = scenario.costs;
  const cash = t.expected.cash;
  const v = npv(cash, k, scenario.hurdleRate);
  const claimed = scenario.claims.reduce((a, c) => a + c.claimed, 0);
  replace(view.status,
    stat('Claimed in the deck', `${ils(claimed)} a year`, 'all counted as cash'),
    stat('Your expected cash', `${ils(cash)} a year`, `low ${ils(t.low.cash)} · high ${ils(t.high.cash)}`),
    stat('Your capacity', hours(t.expected.hours, 0), `${ils(t.expected.capacity)} a year, not cash`),
    stat(`NPV at ${pct(scenario.hurdleRate)}, ${k.years} years`, ils(v), `payback ${monthsText(paybackMonths(cash, k))}`, v >= 0 ? 'good' : 'bad'),
  );
}

function renderSend() {
  const name = 'approval';
  const radios = scenario.approval.map((a) => h('input', { type: 'radio', name, id: `appr-${a.id}`, value: a.id }));
  for (const r of radios) r.addEventListener('change', () => { if (r.checked) approvalPick = r.value; });
  const limits = (a, i) => {
    const lo = i ? scenario.approval[i - 1].max : 0;
    return a.max === Infinity ? `above ${ils(lo)}` : `${i ? `${ils(lo)} to ` : 'up to '}${ils(a.max)}`;
  };
  const err = h('p', { class: 'callout callout-warn', role: 'alert', hidden: true }, 'Say who must approve it first.');
  replace(view.send,
    h('p', {}, `Ronit’s rules: hurdle rate ${pct(scenario.hurdleRate)}, ${scenario.costs.years}-year view; the case costs ${ils(scenario.costs.build)} to build and about ${ils(scenario.costs.runningPerYear)} a year to run. Approval limits are for the total cost over ${scenario.costs.years} years.`),
    h('fieldset', { class: 'group choices' }, h('legend', {}, 'Who must approve this case?'),
      scenario.approval.map((a, i) => h('div', { class: 'choice' }, radios[i], h('label', { for: `appr-${a.id}` }, `${a.who} (${limits(a, i)})`)))),
    err,
    h('div', { class: 'btn-row' }, button('Send it to Ronit’s review', () => {
      if (!approvalPick) { err.hidden = false; return; }
      onReview();
    })),
  );
}

function statusTag(s) {
  const map = { survived: ['good', 'survived'], understated: ['warn', 'survived, understated'], reworked: ['warn', 'reworked by Ronit'], rejected: ['bad', 'rejected as stated'] };
  return h('span', { class: `tag tag-${map[s][0]}` }, map[s][1]);
}

function findingText(f) {
  switch (f.kind) {
    case 'missed': return `Ronit finds what you did not net (${LEDGERS[f.a.ledger].label.toLowerCase()}): ${f.a.text} ${f.a.why}`;
    case 'invented': return `You netted something that is not there: ${f.a.why}`;
    case 'overLabel': return 'Labelled more certain than the evidence allows. Ronit: “Measured by whom, on what?”';
    case 'underLabel': return 'Labelled less certain than the evidence allows: you left defensible value out of the expected case.';
    case 'capacityAsCash': return 'Counted as cash with no named plan for the hours. Ronit: “Whose budget line goes down, and from which month?”';
    case 'cashAsCapacity': return 'Counted as capacity although there is a named budget line: you understated the cash.';
    default: return '';
  }
}

function onReview() {
  const s = summary(scenario, decisions, approvalPick);
  const truth = truthDecisions(scenario);
  for (const row of s.review.rows) {
    const r = refs[row.claim.id];
    for (const b of r.boxes) b.disabled = true;
    r.label.disabled = true;
    r.cls.disabled = true;
    r.review.hidden = false;
    replace(r.review,
      h('p', {}, statusTag(row.status)),
      row.findings.length ? h('ul', { class: 'small' }, row.findings.map((f) => h('li', {}, findingText(f)))) : h('p', { class: 'small' }, 'Ronit has no questions on this one.'),
      h('p', { class: 'small muted' }, `The defensible version: net ${ils(s.right.nets[row.claim.id])}, ${LABELS[row.truth.label].label.toLowerCase()}, ${row.truth.cls}. ${row.claim.truth.note}`));
  }
  const apprOk = s.approvalRight;
  const level = s.approval.level;
  const headline = s.review.credibility >= 85 ? 'Your case survives finance.' : s.review.credibility >= 55 ? 'Your case survives, after Ronit’s corrections.' : 'Ronit sends the case back.';
  view.sendHeading.textContent = 'Debrief';
  replace(view.send,
    h('div', { class: `callout callout-${s.review.credibility >= 85 ? 'good' : s.review.credibility >= 55 ? 'warn' : 'bad'}` },
      h('p', {}, h('strong', {}, headline)),
      h('p', {}, `Claimed: ${ils(s.claimedTotal)} a year. Yours: ${ils(s.mine.expected.cash)} cash in the expected case. ` +
        `Defensible: ${ils(s.right.expected.cash)} cash plus ${hours(s.right.expected.hours, 0)} a year of capacity. ` +
        `${s.survived} of ${scenario.claims.length} claims survived the review as you stated them; credibility ${num(s.review.credibility)} / 100.`)),
    stackTable({
      caption: 'Claimed, your version and the defensible version',
      head: ['Measure', 'Claimed', 'Yours', 'Defensible'],
      rows: [
        { th: 'Cash a year, expected', cells: [ils(s.claimedTotal), ils(s.mine.expected.cash), ils(s.right.expected.cash)] },
        { th: 'Cash a year, low / high', cells: ['–', `${ils(s.mine.low.cash)} / ${ils(s.mine.high.cash)}`, `${ils(s.right.low.cash)} / ${ils(s.right.high.cash)}`] },
        { th: 'Capacity a year (not cash)', cells: ['–', hours(s.mine.expected.hours, 0), hours(s.right.expected.hours, 0)] },
        { th: `NPV at ${pct(scenario.hurdleRate)}`, cells: [ils(s.claimedNpv), ils(s.mineNpv), ils(s.rightNpv)] },
        { th: 'Payback', cells: [monthsText(paybackMonths(s.claimedTotal, scenario.costs)), monthsText(s.minePayback), monthsText(s.rightPayback)] },
      ],
    }),
    h('p', {}, s.rightNpv >= 0
      ? `The defensible case clears the ${pct(scenario.hurdleRate)} hurdle on cash alone (NPV ${ils(s.rightNpv)}, payback ${monthsText(s.rightPayback)}), with the capacity as a bonus that nobody is asked to bank.`
      : `The defensible case does not clear the ${pct(scenario.hurdleRate)} hurdle on cash: take it as a capacity case with a staged budget, or find the named plan that turns hours into money.`),
    h('div', { class: `callout callout-${apprOk ? 'good' : 'bad'}` },
      h('p', {}, apprOk ? `Right: ${level.who.toLowerCase()} must approve it.` : `Not quite: ${level.who.toLowerCase()} must approve it.`),
      h('p', { class: 'small' }, `Build ${ils(scenario.costs.build)} + ${scenario.costs.years} × ${ils(scenario.costs.runningPerYear)} running = ${ils(s.approval.total)} over ${scenario.costs.years} years. The limits apply to the total, not to the build cost alone.`)),
    h('h3', {}, 'Which claims survived'),
    h('ul', {}, s.review.rows.map((row, i) => h('li', {}, statusTag(row.status), ` ${nth(i)}. ${row.claim.title}: claimed ${ils(row.claim.claimed)}, defensible ${ils(s.right.nets[row.claim.id])} ${truth[row.claim.id].cls} (${LABELS[truth[row.claim.id].label].label.toLowerCase()}).`))),
    h('h3', {}, 'The point of this lesson'),
    h('p', { class: 'lesson-point' }, scenario.lessonPoint),
    h('div', { class: 'btn-row' }, button('Start the review again', () => { start(shell.presetKey); focusEl(refs[scenario.claims[0].id].el.firstChild); }, { variant: 'secondary' })),
  );
  focusEl(view.sendHeading);
  shell.announce(`${headline} Defensible: ${ils(s.right.expected.cash)} a year in cash. Yours: ${ils(s.mine.expected.cash)}.`);
}

shell = mountShell({
  title: 'ROI defender',
  tagline: 'Seven claims, four ledgers, one CFO: find the number that survives.',
  presets: PRESETS,
  defaultPreset: DEFAULT_PRESET,
  about: ABOUT,
  onPreset: start,
});
start(shell.presetKey);
