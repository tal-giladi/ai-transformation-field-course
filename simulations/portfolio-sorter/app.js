import { h, replace, focusEl } from '../common/dom.js';
import { mountShell, panel } from '../common/shell.js';
import { rangeField, toggleField, button } from '../common/controls.js';
import { ils, pct, num } from '../common/format.js';
import {
  RULES, MAX_PICKS, CEO_BONUS, normaliseWeights, errorCost, netBenefit, valueDiscounted,
  cardScore, ranking, absorption, commitProblems, evaluate,
} from './model.js';
import { PRESETS, DEFAULT_PRESET } from './presets.js';

const ABOUT = {
  intro: 'A scoring exercise with a hidden answer. Every card has a hidden truth and an expert rating, revealed only after you commit.',
  equations: [
    'Weights are turned into shares that add up to 100%.',
    'Score = (value share × value + feasibility share × feasibility + risk share × (6 − risk)) ÷ 5 × 100. Ratings are 1–5; risk 5 is the worst, so it counts as 1.',
    'With the “half value for claims” rule, a card whose evidence is only a claim has its value rating halved.',
    `With the CEO-bonus rule, the CEO’s card gets +${CEO_BONUS} points.`,
    'Expected cost of errors = items a month × error rate × cost per error. Net benefit = claimed benefit − expected cost of errors.',
    'Absorption: the hours a month each receiving team must give (training, checking, new steps) are added up per team and compared with what the team says it can absorb.',
    'The expert scores the same cards with weights 40/30/30 and the three non-trap rules.',
  ],
  assumptions: [
    'Benefits are claimed monthly figures; the hidden truths show how far some were from reality.',
    'The expert is not always right; the point is to compare reasons, not to match numbers.',
  ],
  leftOut: [
    'Discounting, build time and dependencies between cards (lesson 03.8 does the roadmap).',
    'The scoring workshop with real stakeholders (lesson 03.5): here you score alone.',
  ],
};

const SCALES = {
  value: ['very low', 'low', 'medium', 'high', 'very high'],
  feasibility: ['very hard', 'hard', 'medium', 'fairly easy', 'easy'],
  risk: ['low', 'moderate', 'medium', 'high', 'severe'],
};
const DIM_LABEL = { value: 'Value', feasibility: 'Feasibility', risk: 'Risk if wrong' };
const EVIDENCE = {
  measured: { label: 'measured', tone: 'good' },
  mixed: { label: 'partly measured', tone: 'warn' },
  claim: { label: 'claim only', tone: 'bad' },
};

let shell;
let scenario;
let st;
let view = {};
let refs = {};

function start(key) {
  scenario = PRESETS[key];
  st = {
    criteria: { weights: { value: 50, feasibility: 50, risk: 50 }, rules: Object.fromEntries(Object.keys(RULES).map((k) => [k, false])) },
    locked: false, ratings: {}, picks: [], asked: [], netted: [], committed: false,
  };
  refs = {};
  build();
}

const teamOf = (card) => scenario.teams.find((t) => t.id === card.team);

function build() {
  const crit = panel('Step 1 — Lock your criteria', { id: 'criteria' });
  view.critHeading = crit.heading;
  view.crit = crit.body;
  const cards = panel('Step 2 — Score the use cases', { id: 'cards' });
  view.cardsHeading = cards.heading;
  view.cards = cards.body;
  const port = panel('Step 3 — Your portfolio', { id: 'portfolio' });
  view.port = h('div');
  view.problems = h('div', { role: 'status' });
  view.commit = button('Commit my portfolio', onCommit, { disabled: true });
  port.body.append(view.port, view.problems, h('div', { class: 'btn-row' }, view.commit));
  const deb = panel('Debrief', { id: 'debrief', className: 'debrief' });
  view.debHeading = deb.heading;
  view.debrief = deb.body;
  view.debriefEl = deb.el;
  deb.el.hidden = true;

  replace(shell.main, crit.el, cards.el, port.el, deb.el);
  renderCriteria();
  replace(view.cards, h('p', { class: 'muted' }, 'The list opens once your criteria are locked.'));
  renderPortfolio();
}

function renderCriteria() {
  if (st.locked) {
    const w = normaliseWeights(st.criteria.weights);
    const rules = Object.entries(RULES).filter(([k]) => st.criteria.rules[k]);
    replace(view.crit,
      h('p', {}, h('span', { class: 'tag tag-neutral' }, 'locked'), ` Value ${pct(w.value)}, feasibility ${pct(w.feasibility)}, risk ${pct(w.risk)}.`),
      rules.length ? h('ul', {}, rules.map(([, r]) => h('li', {}, r.label))) : h('p', {}, 'No extra rules.'),
      h('p', { class: 'small muted' }, 'Locked criteria cannot be changed after you have seen the list. That is the point.'));
    return;
  }
  const shares = h('p', { class: 'small', 'aria-live': 'polite' });
  const showShares = () => {
    const w = normaliseWeights(st.criteria.weights);
    shares.textContent = `As shares: value ${pct(w.value)}, feasibility ${pct(w.feasibility)}, risk ${pct(w.risk)}.`;
  };
  const weight = (key, label, help) => rangeField({
    label, min: 0, max: 100, step: 5, value: st.criteria.weights[key], help, format: (v) => num(v),
    onInput: (v) => { st.criteria.weights[key] = v; showShares(); },
  }).el;
  showShares();
  replace(view.crit,
    h('p', {}, 'Decide how you will judge every card before you see any of them. You cannot change this later.'),
    h('fieldset', { class: 'group' }, h('legend', {}, 'Weights'),
      weight('value', 'Value (net benefit)', 'How much the organization gains.'),
      weight('feasibility', 'Feasibility', 'Data ready, integration simple, people available.'),
      weight('risk', 'Risk if wrong (lower is better)', 'The consequence when the output is wrong.'),
      shares),
    h('fieldset', { class: 'group' }, h('legend', {}, 'Rules'),
      Object.entries(RULES).map(([k, r]) => toggleField({
        label: r.label, help: r.help, checked: st.criteria.rules[k],
        onChange: (v) => { st.criteria.rules[k] = v; },
      }).el)),
    h('div', { class: 'btn-row' }, button('Lock criteria and open the list', onLock)),
  );
}

function onLock() {
  st.locked = true;
  renderCriteria();
  renderCards();
  renderPortfolio();
  focusEl(view.cardsHeading);
  shell.announce('Criteria locked. The list of use cases is open.');
}

function ratingSelect(card, dim) {
  const id = `r-${card.id}-${dim}`;
  const sel = h('select', { id },
    h('option', { value: '' }, '– choose –'),
    SCALES[dim].map((lab, i) => h('option', { value: String(i + 1) }, `${i + 1} (${lab})`)));
  sel.addEventListener('change', () => {
    st.ratings[card.id] = { ...(st.ratings[card.id] || {}), [dim]: Number(sel.value) || 0 };
    updateScore(card);
    renderPortfolio();
  });
  return { el: h('div', { class: 'rating' }, h('label', { for: id }, DIM_LABEL[dim]), sel), sel };
}

function renderCards() {
  const list = h('div', { class: 'cards' });
  for (const card of scenario.cards) list.appendChild(buildCard(card));
  replace(view.cards,
    h('p', {}, `Rate every card 1–5 on value, feasibility and risk, using only what the card shows. Then choose up to ${MAX_PICKS} for your portfolio.`),
    list);
}

function buildCard(card) {
  const r = {};
  const ev = EVIDENCE[card.evidence];
  const team = teamOf(card);

  r.net = h('div', { class: 'net' });
  r.ask = h('div', { class: 'ask' });
  r.score = h('p', { class: 'score', 'aria-live': 'polite' });
  r.value = ratingSelect(card, 'value');
  r.feas = ratingSelect(card, 'feasibility');
  r.risk = ratingSelect(card, 'risk');
  r.pickNote = h('p', { class: 'small', role: 'status' });
  r.pick = h('input', { type: 'checkbox', id: `pick-${card.id}` });
  r.pick.addEventListener('change', () => onPick(card, r.pick.checked));
  r.truth = h('div', { class: 'truth', hidden: true });

  const headingId = `card-${card.id}`;
  r.el = h('article', { class: 'card usecase', 'aria-labelledby': headingId },
    h('h3', { id: headingId }, card.title),
    h('p', { class: 'small muted' }, card.proposer),
    h('p', {}, card.summary),
    h('dl', { class: 'facts-list' },
      h('dt', {}, 'Claimed benefit'), h('dd', {}, `${ils(card.claimedBenefit)} a month`, h('span', { class: 'small muted' }, ` — ${card.benefitBasis}`)),
      h('dt', {}, 'Evidence'), h('dd', {}, h('span', { class: `tag tag-${ev.tone}` }, ev.label), ' ', card.evidenceText),
      h('dt', {}, 'Errors'), h('dd', {}, `${num(card.volume)} ${card.volumeUnit}; about ${pct(card.errorRate, card.errorRate < 0.05 ? 1 : 0)} go wrong (${card.errorText}); about ${ils(card.costPerError)} each.`),
      h('dt', {}, 'Build cost'), h('dd', {}, card.buildCost ? ils(card.buildCost) : 'none (already running)'),
      h('dt', {}, 'Receiving team'), h('dd', {}, `${team.name}: needs about ${num(card.absorbHours)} hours a month to absorb it.`),
    ),
    r.net, r.ask,
    h('div', { class: 'ratings' }, r.value.el, r.feas.el, r.risk.el),
    r.score,
    h('div', { class: 'toggle-row pick-row' }, r.pick, h('label', { for: `pick-${card.id}` }, 'Put in my portfolio')),
    r.pickNote,
    r.truth,
  );
  refs[card.id] = r;
  renderNet(card);
  renderAsk(card);
  updateScore(card);
  return r.el;
}

function renderNet(card) {
  const r = refs[card.id];
  const needNet = st.criteria.rules.netErrors && !st.netted.includes(card.id);
  r.value.sel.disabled = needNet || st.committed;
  if (st.netted.includes(card.id)) {
    const net = netBenefit(card);
    replace(r.net, h('p', { class: `callout ${net < 0 ? 'callout-bad' : net < card.claimedBenefit * 0.6 ? 'callout-warn' : 'callout-good'}` },
      `Expected cost of errors: ${ils(errorCost(card))} a month. Net benefit: ${ils(net)} a month.`));
  } else {
    replace(r.net,
      button('Net the expected cost of errors', () => {
        st.netted.push(card.id);
        renderNet(card);
        renderPortfolio();
        shell.announce(`${card.title}: net benefit ${ils(netBenefit(card))} a month.`);
      }, { variant: 'quiet', disabled: st.committed }),
      needNet ? h('p', { class: 'small muted' }, 'Your rule: net the error cost before you score value.') : null);
  }
}

function renderAsk(card) {
  const r = refs[card.id];
  const team = teamOf(card);
  if (st.asked.includes(team.id)) {
    const over = card.absorbHours > team.capacity;
    replace(r.ask, h('p', { class: `callout ${over ? 'callout-bad' : ''}` },
      h('strong', {}, `${team.contact}: `), `“${team.answer}”`,
      h('br'), `${team.name} can absorb ${num(team.capacity)} hours a month in total.`));
  } else {
    replace(r.ask, button(`Ask ${team.contact} what ${team.name} can absorb`, () => {
      st.asked.push(team.id);
      for (const c of scenario.cards) if (c.team === team.id) renderAsk(c);
      renderPortfolio();
      shell.announce(`${team.name} can absorb ${team.capacity} hours a month.`);
    }, { variant: 'quiet', disabled: st.committed }));
  }
}

function updateScore(card) {
  const r = refs[card.id];
  const s = cardScore(card, st.ratings[card.id], st.criteria);
  if (s === null) {
    r.score.textContent = 'Score: rate all three to see it.';
    return;
  }
  const notes = [];
  if (valueDiscounted(card, st.criteria)) notes.push('value halved: claim only');
  if (st.criteria.rules.ceoBonus && card.ceoPriority) notes.push(`+${CEO_BONUS} CEO bonus`);
  r.score.textContent = `Your score: ${num(s)}${notes.length ? ` (${notes.join('; ')})` : ''}`;
}

function onPick(card, checked) {
  const r = refs[card.id];
  if (checked && st.picks.length >= MAX_PICKS) {
    r.pick.checked = false;
    r.pickNote.textContent = `Your portfolio is full (${MAX_PICKS}). Remove one first.`;
    return;
  }
  r.pickNote.textContent = '';
  st.picks = checked ? [...st.picks, card.id] : st.picks.filter((x) => x !== card.id);
  renderPortfolio();
}

function renderPortfolio() {
  if (!st.locked) {
    replace(view.port, h('p', { class: 'muted' }, 'Lock your criteria first.'));
    view.commit.disabled = true;
    return;
  }
  const rank = ranking(scenario, st.ratings, st.criteria);
  const absorb = absorption(scenario, st.picks, st.asked);
  replace(view.port,
    h('h3', {}, 'Your ranking'),
    h('div', { class: 'table-wrap' }, h('table', {},
      h('caption', { class: 'sr-only' }, 'Use cases ranked by your score'),
      h('thead', {}, h('tr', {}, ['#', 'Use case', 'Your score', 'In portfolio'].map((c) => h('th', { scope: 'col' }, c)))),
      h('tbody', {}, rank.map((x, i) => h('tr', {},
        h('td', {}, x.score === null ? '–' : num(i + 1)),
        h('th', { scope: 'row' }, x.card.title),
        h('td', {}, x.score === null ? 'not rated' : num(x.score)),
        h('td', {}, st.picks.includes(x.card.id) ? 'yes' : '')))))),
    h('h3', {}, `Absorption check (${st.picks.length} of ${MAX_PICKS} picked)`),
    absorb.length
      ? h('ul', {}, absorb.map((a) => h('li', {},
        `${a.team.name}: your picks need ${num(a.demand)} hours a month; `,
        a.asked
          ? (a.demand > a.capacity ? h('strong', { class: 'bad-text' }, `the team can absorb ${num(a.capacity)}. Over capacity.`) : `the team can absorb ${num(a.capacity)}.`)
          : 'you have not asked what they can absorb.')))
      : h('p', { class: 'muted' }, 'No cards picked yet.'),
  );
  view.commit.disabled = st.committed;
}

function onCommit() {
  const problems = commitProblems(scenario, st.criteria, st.ratings, st.picks, st.asked, st.netted);
  if (problems.length) {
    replace(view.problems, h('div', { class: 'callout callout-warn' },
      h('p', {}, h('strong', {}, 'Not yet:')), h('ul', {}, problems.map((p) => h('li', {}, p)))));
    shell.announce(`Not yet. ${problems.join(' ')}`);
    return;
  }
  replace(view.problems);
  st.committed = true;
  view.commit.disabled = true;
  for (const card of scenario.cards) {
    const r = refs[card.id];
    r.value.sel.disabled = true;
    r.feas.sel.disabled = true;
    r.risk.sel.disabled = true;
    r.pick.disabled = true;
    renderNet(card);
    renderAsk(card);
    revealTruth(card);
  }
  renderDebrief();
  view.debriefEl.hidden = false;
  focusEl(view.debHeading);
}

function revealTruth(card) {
  const r = refs[card.id];
  const exp = card.expertRating;
  r.truth.hidden = false;
  replace(r.truth, h('div', { class: 'callout' },
    h('p', {}, h('strong', {}, 'What was really true: '), card.truth),
    h('p', { class: 'small' }, `Expert: value ${exp.value}, feasibility ${exp.feasibility}, risk ${exp.risk}. ${card.expertNote}`),
    h('p', { class: 'small' }, `Net of expected errors: ${ils(netBenefit(card))} a month.`)));
}

function renderDebrief() {
  const ev = evaluate(scenario, st.criteria, st.ratings, st.picks, st.asked, st.netted);
  const ex = scenario.expert;
  const title = (id) => scenario.cards.find((c) => c.id === id).title;
  const pts = [];
  if (!ev.mustHavePicked) pts.push(`You left out “${title(ex.mustHave)}”. It needs no AI, it is measured, cheap and it removes the cause of the biggest contact type. The best first move is often not an AI project.`);
  else pts.push(`You picked “${title(ex.mustHave)}”: plain automation, measured, cheap. Good: the best first move is often not an AI project.`);
  for (const x of ev.trapsPicked) pts.push(`“${x.card.title}”: ${x.card.truth}`);
  for (const a of ev.overCapacity) {
    pts.push(`${a.team.name} would have to absorb ${num(a.demand)} hours a month; it can take ${num(a.team.capacity)}. ${a.asked ? 'You asked, and committed anyway.' : 'You never asked.'} A portfolio the receiving team cannot absorb fails in the rollout, not in the business case.`);
  }
  if (ev.pickedNegativeNet.length) pts.push(`Once errors are netted, ${ev.pickedNegativeNet.map((x) => `“${x.card.title}”`).join(' and ')} lose${ev.pickedNegativeNet.length === 1 ? 's' : ''} money every month.`);
  if (ev.pickedNotNetted.length) pts.push(`You did not net the error cost of ${ev.pickedNotNetted.map((x) => `“${x.card.title}”`).join(', ')} before picking it.`);
  for (const k of ev.trapRules) pts.push(k === 'ceoBonus'
    ? 'Your criteria gave the CEO’s idea a bonus. Who proposed a use case is not evidence; it belongs in the conversation with the sponsor, not in the score.'
    : 'Your criteria counted a vendor case study as measured evidence. A number measured on someone else’s customers, language and data is a claim until you test it on yours.');
  for (const k of ev.missedRules) pts.push(`You did not lock the rule “${RULES[k].label.toLowerCase()}”.`);
  if (ev.weightDistance > 0.2) {
    const w = normaliseWeights(ex.criteria.weights);
    pts.push(`Your weights are far from the expert’s (value ${pct(w.value)}, feasibility ${pct(w.feasibility)}, risk ${pct(w.risk)}). Neither is right by definition; what matters is that you set them before you saw the list.`);
  }
  if (ev.biggestGaps.length) pts.push(`Your ratings differed most from the expert’s on ${ev.biggestGaps.map((x) => `“${x.card.title}”`).join(', ')}. Read their hidden truths on the cards above.`);

  const tone = ev.overlap.length === ex.picks.length && ev.mustHavePicked ? 'good' : ev.mustHavePicked ? 'warn' : 'bad';
  replace(view.debrief,
    h('div', { class: `callout callout-${tone}` },
      h('p', {}, h('strong', {}, `Your portfolio shares ${ev.overlap.length} of ${ex.picks.length} cards with the expert’s.`)),
      h('p', {}, `Expert portfolio: ${ex.picks.map(title).join('; ')}. ${ex.summary}`)),
    h('div', { class: 'table-wrap' }, h('table', {},
      h('caption', { class: 'sr-only' }, 'Your scores and picks compared with the expert’s'),
      h('thead', {}, h('tr', {}, ['Use case', 'Your score', 'Expert score', 'You', 'Expert', 'Net a month'].map((c) => h('th', { scope: 'col' }, c)))),
      h('tbody', {}, ev.cards.slice().sort((a, b) => b.expertScore - a.expertScore).map((x) => h('tr', {},
        h('th', { scope: 'row' }, x.card.title),
        h('td', {}, x.yourScore === null ? '–' : num(x.yourScore)),
        h('td', {}, num(x.expertScore)),
        h('td', {}, x.picked ? 'picked' : ''),
        h('td', {}, x.expertPicked ? 'picked' : ''),
        h('td', {}, ils(x.net))))))),
    h('h3', {}, 'What to take from your choices'),
    h('ul', {}, pts.map((p) => h('li', {}, p))),
    h('p', { class: 'small muted' }, `Build cost of your portfolio: ${ils(ev.totalBuild)} (expert: ${ils(ev.expertBuild)}). Projects above ₪150,000 need board approval at Harbor & Pine.`),
    h('h3', {}, 'The point of this lesson'),
    h('p', { class: 'lesson-point' }, scenario.lessonPoint),
    h('div', { class: 'btn-row' }, button('Start again', () => { start(shell.presetKey); focusEl(view.critHeading); }, { variant: 'secondary' })),
  );
  shell.announce(`Committed. Your portfolio shares ${ev.overlap.length} of ${ex.picks.length} cards with the expert.`);
}

shell = mountShell({
  title: 'Portfolio sorter',
  tagline: 'Lock the criteria, score on evidence, ask what the team can absorb, then see what was really true.',
  presets: PRESETS,
  defaultPreset: DEFAULT_PRESET,
  about: ABOUT,
  onPreset: start,
});
start(shell.presetKey);
