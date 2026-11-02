import { h, replace, focusEl } from '../common/dom.js';
import { mountShell, panel } from '../common/shell.js';
import { button, stat } from '../common/controls.js';
import { stackTable } from '../common/table.js';
import { num } from '../common/format.js';
import { createState, canGather, gather, rate, registerCounts, debrief, RATINGS, METHODS, VERDICTS } from './model.js';
import { PRESETS, DEFAULT_PRESET } from './presets.js';

const ABOUT = {
  intro: 'A register of risks, each with an owner’s rating and a control as the owner describes it. Every test result is written in advance; what you choose to test, and how you re-rate, is up to you.',
  equations: [
    'You have a testing budget. Asking the owner, sampling the evidence and running a test cost different amounts; each can be done once per risk.',
    'Some evidence is conclusive about whether the control works; some only suggests it. A green counts as earned only if you gathered conclusive evidence for that risk.',
    'Credibility of a register = the average over all risks of: 1 for a right rating (a green only if it was tested), 0.5 for a right but untested green, 0.5 for a rating one level too high, 0.25 for two levels too high, 0 for a rating too low, and 0 for an unearned green.',
    'The owners’ register is scored the same way, with nothing tested, so you can see what your testing changed.',
  ],
  assumptions: [
    'Each risk has one true rating. In practice ratings are judgements; what matters is that a green has evidence behind it.',
    'A test finds the truth when it is conclusive. Real tests can be badly designed; lesson 04.5 covers how to design one.',
  ],
  leftOut: [
    'Likelihood × impact scoring and risk appetite: here the rating already combines them.',
    'Risks nobody wrote down. The pre-mortem in lesson 04.5 is how you find them.',
  ],
};

let shell;
let scenario;
let state;
let refs = {};
let view = {};

function start(key) {
  scenario = PRESETS[key];
  state = createState(scenario);
  refs = {};
  build();
  renderStatus();
}

const tone = (r) => (r === 'green' ? 'good' : r === 'red' ? 'bad' : 'warn');

function build() {
  view.status = h('div', { class: 'stats' });
  const reg = panel('The register', { id: 'register' });
  view.cards = h('div', { class: 'cards' }, scenario.risks.map((r) => buildCard(r)));
  reg.body.append(
    h('p', { class: 'small muted' }, `Costs: ${Object.entries(METHODS).map(([k, m]) => `${m.label.toLowerCase()} ${scenario.costs[k]}`).join(', ')}.`),
    view.cards,
  );
  if (scenario.notes && scenario.notes.length) {
    reg.body.append(h('details', { class: 'notes' }, h('summary', {}, 'Where these facts come from'),
      h('ul', {}, scenario.notes.map((n) => h('li', {}, n)))));
  }

  const submit = panel('Submit the register', { id: 'submit', className: 'debrief' });
  view.submitHeading = submit.heading;
  view.submit = h('div');
  submit.body.append(view.submit);
  renderSubmit();

  replace(shell.main, view.status, reg.el, submit.el);
}

function buildCard(risk) {
  const r = {};
  const selId = `rate-${risk.id}`;
  r.evidence = h('div', { class: 'evidence' });
  r.buttons = h('div', { class: 'btn-row' });
  r.select = h('select', { id: selId },
    RATINGS.map((x) => h('option', { value: x, selected: x === state.ratings[risk.id] }, x)));
  r.select.addEventListener('change', () => {
    state = rate(state, risk.id, r.select.value);
    renderStatus();
    renderTag(risk);
  });
  r.tag = h('span', { class: 'tag' });
  const headingId = `risk-${risk.id}`;
  r.el = h('article', { class: 'card risk', 'aria-labelledby': headingId },
    h('h3', { id: headingId }, risk.title),
    h('p', { class: 'small muted' }, `Owner: ${risk.owner}`),
    h('p', {}, h('span', { class: `tag tag-${tone(risk.ownerRating)}` }, `owner: ${risk.ownerRating}`), ' ', risk.control),
    r.buttons,
    r.evidence,
    h('div', { class: 'rate-row' }, h('label', { for: selId }, 'Your rating'), r.select, r.tag),
  );
  refs[risk.id] = r;
  renderButtons(risk);
  renderEvidence(risk);
  renderTag(risk);
  return r.el;
}

function renderButtons(risk) {
  const r = refs[risk.id];
  replace(r.buttons, Object.entries(METHODS).map(([k, m]) => {
    const done = state.gathered[risk.id].includes(k);
    return button(`${m.label} (${scenario.costs[k]})`, () => onGather(risk, k), {
      variant: 'quiet', disabled: !canGather(state, scenario, risk.id, k),
      'aria-label': `${m.label} for “${risk.title}”, costs ${scenario.costs[k]}${done ? ', done' : ''}`,
    });
  }));
}

function renderEvidence(risk) {
  const r = refs[risk.id];
  const got = state.gathered[risk.id];
  replace(r.evidence, got.length
    ? h('ul', { class: 'evidence-list' }, got.map((k) => h('li', {}, h('strong', {}, `${METHODS[k].label}: `), risk.evidence[k].text)))
    : null);
}

function renderTag(risk) {
  const r = refs[risk.id];
  const rating = state.ratings[risk.id];
  const tested = state.gathered[risk.id].some((k) => risk.evidence[k].strength === 'strong');
  r.tag.setAttribute('class', `tag tag-${tone(rating)}`);
  r.tag.textContent = rating === 'green' && !tested ? 'green, untested' : rating;
}

function onGather(risk, method) {
  state = gather(state, scenario, risk.id, method);
  for (const x of scenario.risks) renderButtons(x);
  renderEvidence(risk);
  renderTag(risk);
  renderStatus();
  focusEl(refs[risk.id].evidence.lastChild && refs[risk.id].evidence.lastChild.lastChild);
  shell.announce(`${risk.evidence[method].text} ${num(state.budget)} testing points left.`);
}

function renderStatus() {
  const c = registerCounts(state, scenario);
  replace(view.status,
    stat('Testing points left', `${num(state.budget)} of ${num(scenario.budget)}`, null, state.budget <= 2 ? 'warn' : ''),
    stat('On the register', `${c.green} green · ${c.amber} amber · ${c.red} red`),
    stat('Greens without evidence', num(c.untestedGreens), 'each one is a claim, not a rating', c.untestedGreens ? 'warn' : 'good'),
    stat('Risks tested conclusively', `${num(c.tested)} of ${num(scenario.risks.length)}`),
  );
}

function renderSubmit() {
  replace(view.submit,
    h('p', {}, 'When you have spent what you want to spend and re-rated what the evidence says, submit. The register then goes to the steering group, and you see the truth behind each rating.'),
    h('div', { class: 'btn-row' }, button('Submit the register', onSubmit)));
}

function onSubmit() {
  state = { ...state, submitted: true };
  for (const x of scenario.risks) { renderButtons(x); refs[x.id].select.disabled = true; }
  const d = debrief(state, scenario);
  const better = d.after - d.before;
  const headline = d.unearnedLeft
    ? `${d.unearnedLeft} unearned ${d.unearnedLeft === 1 ? 'green is' : 'greens are'} still on the register.`
    : 'No unearned greens left on the register.';
  view.submitHeading.textContent = 'Debrief';
  replace(view.submit,
    h('div', { class: `callout callout-${d.unearnedLeft ? 'bad' : d.after >= 75 ? 'good' : 'warn'}` },
      h('p', {}, h('strong', {}, headline)),
      h('p', {}, `Credibility of the register: owners’ version ${num(d.before)} / 100, yours ${num(d.after)} / 100 (${better >= 0 ? '+' : ''}${num(better)}). ` +
        `You found ${num(d.unearnedFound)} of the ${num(d.unearnedTotal)} unearned greens and spent ${num(d.spent)} of ${num(scenario.budget)} testing points.`)),
    h('div', { class: 'stats' },
      stat('Earned greens', num(d.earned), 'tested and true', 'good'),
      stat('Greens on trust', num(d.untested), 'right, but untested', d.untested ? 'warn' : ''),
      stat('Overstated', num(d.overstatedLeft), 'reds and ambers that are lower', d.overstatedLeft ? 'warn' : ''),
      stat('Understated', num(d.understated), 'worse than you rated', d.understated ? 'bad' : ''),
    ),
    h('h3', {}, 'Each risk: the owner, you and the truth'),
    stackTable({
      caption: 'Ratings by the owner, by you and the true rating, with the evidence you gathered',
      head: ['Risk', 'Owner', 'You', 'True', 'What you did', 'Why'],
      rows: d.rows.map((x) => ({
        th: [x.risk.title, ' ', h('span', { class: `tag tag-${VERDICTS[x.verdict].tone}` }, VERDICTS[x.verdict].label)],
        cells: [
          h('span', { class: `tag tag-${tone(x.owner)}` }, x.owner),
          h('span', { class: `tag tag-${tone(x.yours)}` }, x.yours),
          h('span', { class: `tag tag-${tone(x.truth)}` }, x.truth),
          h('span', { class: 'small' }, x.gathered.length ? x.gathered.map((k) => METHODS[k].verb).join(', ') : 'nothing'),
          h('span', { class: 'small' }, `Control: ${x.risk.truth.control}. ${x.risk.truth.why}`),
        ],
      })),
    }),
    d.askOnly ? h('p', { class: 'small' }, `On ${num(d.askOnly)} ${d.askOnly === 1 ? 'risk' : 'risks'} you only asked the owner. Owners describe the control they believe in; that is what the register already says.`) : null,
    h('h3', {}, 'The control-credibility test'),
    h('ul', {},
      h('li', {}, 'Does the control exist outside a document?'),
      h('li', {}, 'Does it run, on a schedule, done by a named person?'),
      h('li', {}, 'Does it catch what it is meant to catch (try it)?'),
      h('li', {}, 'Is there evidence you could hand to someone else?')),
    h('h3', {}, 'The point of this lesson'),
    h('p', { class: 'lesson-point' }, scenario.lessonPoint),
    h('div', { class: 'btn-row' }, button('Test the register again', () => { start(shell.presetKey); focusEl(view.cards.firstChild && view.cards.firstChild.firstChild); }, { variant: 'secondary' })),
  );
  focusEl(view.submitHeading);
  shell.announce(`${headline} Credibility ${d.after} out of 100; the owners’ version scored ${d.before}.`);
}

shell = mountShell({
  title: 'Risk register tester',
  tagline: 'Twelve ratings, a small testing budget: earn the green.',
  presets: PRESETS,
  defaultPreset: DEFAULT_PRESET,
  about: ABOUT,
  onPreset: start,
});
start(shell.presetKey);
