import { h, replace, focusEl } from '../common/dom.js';
import { mountShell, panel } from '../common/shell.js';
import { button, stat, selectField } from '../common/controls.js';
import { stackTable } from '../common/table.js';
import { num } from '../common/format.js';
import {
  STAGES, HOLDS, SCORE_MIN, SCORE_MAX, createState, setScore, advance, setDecision, weighted, ranking, pocBest, evaluate,
  truthScores, demoScores,
} from './model.js';
import { PRESETS, DEFAULT_PRESET } from './presets.js';

const ABOUT = {
  intro: 'A vendor selection in four steps: demos, how the numbers were measured, a proof of concept on your own data, and the decision with contract terms. Your scores carry from step to step; the debrief compares them with the evidence.',
  equations: [
    'Weighted score of a vendor = Σ (criterion weight × your score from 1 to 5) ÷ Σ weights. The weights are set in the scenario, as a steering group would agree them before the demos.',
    'Distance from the evidence = the average gap, in points, between your scores and the scores the evidence supports, over every vendor and criterion (0 = you scored exactly what the evidence shows).',
    'The demo impression is what a reasonable person would score after the demo alone; the evidence scores are what the conditions, the documents and the proof of concept support.',
    'Contract: each term you require is accepted or refused by the vendor you choose; the debrief compares your terms with the expert’s must-haves.',
  ],
  assumptions: [
    'The proof of concept is run fairly for every vendor, on synthetic recordings that look like the real work.',
    'Vendors answer the contract terms as stated; real negotiation moves some of them.',
    'The model never states a legal requirement: privacy and data-location questions go to the DPO and counsel.',
  ],
  leftOut: [
    'Price negotiation, procurement rules and tender law.',
    'Clinician adoption beyond the pilot step, and the integration project itself.',
  ],
};

const STAGE_TEXT = {
  demo: {
    title: 'Step 1 of 4: the demos',
    intro: 'Each vendor demoed and sent documents. Score every vendor on the six criteria from what you have seen (every score starts at 3).',
    next: 'Ask how the headline numbers were measured',
  },
  conditions: {
    title: 'Step 2 of 4: how the numbers were measured',
    intro: 'You asked every vendor for the conditions behind each headline number. Under each claim you now see where it was measured and whether that holds for this organization. Change any score.',
    next: 'Run the proof of concept on our own recordings',
  },
  poc: {
    title: 'Step 3 of 4: the proof of concept',
    intro: '',
    next: 'Choose the vendor and the contract terms',
  },
  decide: {
    title: 'Step 4 of 4: the decision',
    intro: 'Choose one vendor, the terms you will require in the contract, and what must happen before anyone signs.',
    next: 'Send the recommendation to the steering group',
  },
};

let shell;
let scenario;
let state;
const view = {};

function start(key) {
  scenario = PRESETS[key];
  state = createState(scenario);
  build();
  renderAll();
}

function build() {
  view.status = h('div', { class: 'stats' });
  const stage = panel('Step', { id: 'stage' });
  view.stageHeading = stage.heading;
  view.stage = h('div');
  stage.body.append(view.stage);

  const rank = panel('Your ranking', { id: 'ranking' });
  view.rank = h('div');
  rank.body.append(view.rank);
  if (scenario.notes && scenario.notes.length) {
    rank.body.append(h('details', { class: 'notes' }, h('summary', {}, 'Where these numbers come from'),
      h('ul', {}, scenario.notes.map((n) => h('li', {}, n)))));
  }

  const result = panel('Debrief', { id: 'result', className: 'debrief' });
  view.resultPanel = result.el;
  view.resultHeading = result.heading;
  view.result = h('div');
  result.body.append(view.result);
  view.resultPanel.hidden = true;

  replace(shell.main, view.status,
    h('div', { class: 'layout layout-2 rfp-layout' },
      h('div', { class: 'stack' }, rank.el),
      h('div', { class: 'stack' }, stage.el)),
    result.el);
}

function renderAll() {
  renderStatus();
  renderStage();
  renderRanking();
}

function renderStatus() {
  const r = ranking(state.scores, scenario);
  const i = STAGES.indexOf(state.stage);
  replace(view.status,
    stat('Step', state.stage === 'done' ? 'done' : `${num(i + 1)} of 4`, STAGE_TEXT[state.stage] ? STAGE_TEXT[state.stage].title.replace(/^Step \d of 4: /, '') : 'debrief below'),
    stat('Your top vendor', r[0].name, `${num(r[0].total, 2)} of 5`),
    stat('Runner-up', r[1].name, `${num(r[1].total, 2)} of 5`),
  );
}

function renderRanking() {
  const r = ranking(state.scores, scenario);
  replace(view.rank,
    h('ol', { class: 'rank-list' }, r.map((x) => h('li', {}, h('strong', {}, x.name), ` ${num(x.total, 2)}`))),
    h('p', { class: 'small muted' }, 'Weights: ', scenario.criteria.map((c) => `${c.label} ×${c.weight}`).join(', '), '.'),
  );
}

const scoringOpen = () => ['demo', 'conditions', 'poc'].includes(state.stage);
const shows = (stage) => STAGES.indexOf(state.stage) >= STAGES.indexOf(stage);

function vendorCard(v) {
  const total = h('p', { class: 'vendor-total' });
  const showTotal = () => { total.textContent = `Your weighted score: ${num(weighted(state.scores[v.id], scenario.criteria), 2)} of 5`; };
  showTotal();
  const scores = scoringOpen() ? h('fieldset', { class: 'group scores' },
    h('legend', {}, `Your scores for ${v.name}`),
    scenario.criteria.map((c) => selectField({
      label: c.label,
      options: [1, 2, 3, 4, 5].map((n) => ({ value: String(n), label: `${n}${n === SCORE_MIN ? ' (poor)' : n === SCORE_MAX ? ' (strong)' : ''}` })),
      value: String(state.scores[v.id][c.id]),
      onChange: (val) => {
        state = setScore(state, v.id, c.id, val);
        showTotal();
        renderRanking();
        renderStatus();
      },
    }).el)) : null;
  return h('article', { class: 'card vendor', 'aria-labelledby': `vendor-${v.id}` },
    h('h3', { id: `vendor-${v.id}` }, v.name),
    h('p', { class: 'muted small' }, v.tagline),
    h('p', {}, h('strong', {}, 'Demo: '), v.demo),
    h('h4', {}, 'Headline claims'),
    h('ul', { class: 'claims' }, v.claims.map((c) => h('li', {},
      h('strong', {}, c.text),
      shows('conditions') ? h('div', { class: 'small conditions' },
        h('span', { class: 'muted' }, 'Measured: '), c.conditions, ' ',
        h('span', { class: `tag tag-${HOLDS[c.holds].tone}` }, HOLDS[c.holds].label), ' ', c.why) : null))),
    h('details', { class: 'docs' }, h('summary', {}, `Documents (${v.docs.length})`),
      h('ul', {}, v.docs.map((d) => h('li', {}, h('strong', {}, `${d.title}: `), d.says)))),
    shows('poc') ? h('p', { class: 'small poc-note' }, h('strong', {}, 'Proof of concept: '), v.pocNote) : null,
    h('p', { class: 'small muted' }, v.price),
    scores,
    total,
  );
}

function pocTable() {
  const best = pocBest(scenario);
  return stackTable({
    caption: 'Proof-of-concept results by vendor',
    head: ['Measure', ...scenario.vendors.map((v) => v.name)],
    rows: scenario.pocMetrics.map((m) => ({
      th: m.label,
      cells: scenario.vendors.map((v) => {
        const x = v.poc[m.id];
        if (x === null || x === undefined) return h('span', { class: 'tag tag-bad' }, 'not available');
        const txt = `${num(x, Number.isInteger(x) ? 0 : 1)}${m.unit === '%' ? '%' : m.unit ? ` ${m.unit}` : ''}`;
        return x === best[m.id] ? h('span', {}, txt, ' ', h('span', { class: 'tag tag-good' }, 'best')) : txt;
      }),
    })),
  });
}

function renderStage() {
  if (state.stage === 'done') {
    view.stageHeading.textContent = 'Recommendation sent';
    replace(view.stage, h('p', {}, 'The debrief is below.'), h('div', { class: 'cards' }, scenario.vendors.map(vendorCard)));
    return;
  }
  const s = STAGE_TEXT[state.stage];
  view.stageHeading.textContent = s.title;
  const err = h('p', { class: 'callout callout-warn', role: 'alert', hidden: true }, 'Choose a vendor first.');
  replace(view.stage,
    h('p', {}, state.stage === 'poc' ? `${scenario.pocIntro} Change any score.` : s.intro),
    state.stage === 'demo' ? h('details', { class: 'notes' }, h('summary', {}, 'What the six criteria mean'),
      h('ul', {}, scenario.criteria.map((c) => h('li', {}, h('strong', {}, `${c.label} (×${c.weight}): `), c.help)))) : null,
    shows('poc') ? h('div', {}, h('h3', {}, 'Proof of concept on our own recordings'), pocTable()) : null,
    state.stage === 'decide' ? decisionForm() : null,
    h('div', { class: 'cards' }, scenario.vendors.map(vendorCard)),
    err,
    h('div', { class: 'btn-row' }, button(s.next, () => {
      if (state.stage === 'decide' && !state.decision.pick) { err.hidden = false; focusEl(err); return; }
      onNext();
    })),
  );
}

function checkList(name, items, selected, onToggle) {
  return items.map((it) => {
    const id = `${name}-${it.id}`;
    const box = h('input', { type: 'checkbox', id, checked: selected.includes(it.id) });
    box.addEventListener('change', () => onToggle(it.id, box.checked));
    return h('div', { class: 'choice' }, box, h('label', { for: id }, it.label));
  });
}

function decisionForm() {
  const d = state.decision;
  const toggle = (key) => (id, on) => {
    const set = new Set(state.decision[key]);
    if (on) set.add(id); else set.delete(id);
    state = setDecision(state, { [key]: [...set] });
  };
  return h('div', { class: 'decision' },
    h('fieldset', { class: 'group choices' },
      h('legend', {}, 'The vendor you recommend'),
      scenario.vendors.map((v) => {
        const id = `pick-${v.id}`;
        const r = h('input', { type: 'radio', name: 'pick', id, value: v.id, checked: d.pick === v.id });
        r.addEventListener('change', () => { if (r.checked) state = setDecision(state, { pick: v.id }); });
        return h('div', { class: 'choice' }, r, h('label', { for: id }, `${v.name} (your score ${num(weighted(state.scores[v.id], scenario.criteria), 2)})`));
      })),
    h('fieldset', { class: 'group choices' },
      h('legend', {}, 'Contract terms you will require'),
      checkList('term', scenario.terms, d.terms, toggle('terms'))),
    h('fieldset', { class: 'group choices' },
      h('legend', {}, 'Before anyone signs'),
      checkList('step', scenario.beforeSigning, d.steps, toggle('steps'))),
  );
}

function onNext() {
  state = advance(state);
  renderAll();
  if (state.stage === 'done') {
    renderDebrief();
    return;
  }
  focusEl(view.stageHeading);
  shell.announce(`${view.stageHeading.textContent}.`);
}

const VERDICT = {
  strong: ['An evidence-led choice with a contract that protects the data.', 'good'],
  rightVendorWeakTerms: ['The right vendor, with gaps in the contract or the steps before signing.', 'warn'],
  defensible: ['A defensible choice, not the strongest one.', 'warn'],
  demoLed: ['A demo-led choice.', 'bad'],
};

function renderDebrief() {
  const e = evaluate(state, scenario);
  const [headline, tone] = VERDICT[e.verdict];
  const expertVendor = scenario.vendors.find((v) => v.id === scenario.expert.pick);
  const truth = truthScores(scenario);
  const demo = demoScores(scenario);
  view.resultPanel.hidden = false;
  replace(view.result,
    h('div', { class: `callout callout-${tone}` },
      h('p', {}, h('strong', {}, headline)),
      h('p', {}, `You recommended ${e.vendor.name}. The expert chose ${expertVendor.name}. ${scenario.expert.why}`)),
    h('h3', {}, 'How your scores moved'),
    stackTable({
      caption: 'Your distance from the evidence and your ranking after each step',
      head: ['Step', 'Distance from the evidence', 'Your ranking'],
      rows: e.stages.map((s) => ({ th: s.label, cells: [`${num(s.error, 2)} points`, s.ranking.map((x) => x.name).join(' › ')] })),
    }),
    h('p', { class: 'small' }, `The demos alone rank them ${e.demo.map((x) => x.name).join(' › ')}; the evidence ranks them ${e.evidence.map((x) => x.name).join(' › ')}.`),
    stackTable({
      caption: 'Weighted score per vendor: what the demo suggested, your final score and the evidence',
      head: ['Vendor', 'The demo suggested', 'Your final score', 'The evidence'],
      rows: scenario.vendors.map((v) => ({
        th: v.name,
        cells: [num(weighted(demo[v.id], scenario.criteria), 2), num(weighted(state.scores[v.id], scenario.criteria), 2), num(weighted(truth[v.id], scenario.criteria), 2)],
      })),
    }),
    h('h3', {}, 'The headline numbers and where they were measured'),
    stackTable({
      caption: 'Every headline claim, its measurement conditions and whether it holds here',
      head: ['Claim', 'Measured', 'Here'],
      rows: scenario.vendors.flatMap((v) => v.claims.map((c) => ({
        th: `${v.name}: ${c.text}`,
        cells: [h('span', { class: 'small' }, c.conditions), h('span', { class: `tag tag-${HOLDS[c.holds].tone}` }, HOLDS[c.holds].label)],
      }))),
    }),
    h('h3', {}, 'The contract'),
    stackTable({
      caption: 'Each term: must-have or not, whether you required it, and the chosen vendor’s answer',
      head: ['Term', 'Expert', 'You', `${e.vendor.name}’s answer`],
      rows: scenario.terms.map((t) => {
        const mine = state.decision.terms.includes(t.id);
        const ans = e.vendor.terms[t.id];
        return {
          th: t.label,
          cells: [
            t.mustHave ? 'must-have' : 'nice to have',
            h('span', { class: `tag tag-${mine ? 'good' : t.mustHave ? 'bad' : 'neutral'}` }, mine ? 'required' : 'not asked'),
            h('span', {}, h('span', { class: `tag tag-${ans.reply === 'accepts' ? 'good' : 'bad'}` }, ans.reply), ' ', h('span', { class: 'small' }, ans.note)),
          ],
        };
      }),
    }),
    e.missingMust.length ? h('p', { class: 'callout callout-warn' }, `Must-haves you did not ask for: ${e.missingMust.map((id) => scenario.terms.find((t) => t.id === id).label.toLowerCase()).join('; ')}.`) : null,
    e.refused.length ? h('p', { class: 'callout callout-bad' }, `${e.vendor.name} refuses ${e.refused.map((a) => a.term.label.toLowerCase()).join('; ')}. Either you walk away, or the DPO and counsel accept that risk in writing.`) : null,
    h('h3', {}, 'Before anyone signs'),
    h('ul', {}, scenario.beforeSigning.map((s) => {
      const chose = state.decision.steps.includes(s.id);
      const ok = chose === s.right;
      return h('li', {}, h('span', { class: `tag tag-${ok ? 'good' : 'bad'}` }, chose ? 'you chose it' : 'you left it out'), ' ', h('strong', {}, s.label), '. ', s.why);
    })),
    h('h3', {}, 'Twelve months later'),
    h('p', {}, e.vendor.later),
    e.pickRight ? null : h('p', { class: 'small muted' }, `With ${expertVendor.name}: ${expertVendor.later}`),
    h('h3', {}, 'The point of this lesson'),
    h('p', { class: 'lesson-point' }, scenario.lessonPoint),
    h('div', { class: 'btn-row' }, button('Run the selection again', () => { start(shell.presetKey); focusEl(view.stageHeading); }, { variant: 'secondary' })),
  );
  focusEl(view.resultHeading);
  shell.announce(headline);
}

shell = mountShell({
  title: 'Vendor RFP',
  tagline: 'Score vendors on evidence, not demos; then put the protections in the contract.',
  presets: PRESETS,
  defaultPreset: DEFAULT_PRESET,
  about: ABOUT,
  onPreset: start,
});
start(shell.presetKey);
