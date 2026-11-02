import { h, replace, focusEl } from '../common/dom.js';
import { mountShell, panel } from '../common/shell.js';
import { button, stat } from '../common/controls.js';
import { pct, num, plural } from '../common/format.js';
import { createState, availableQuestions, hiddenCount, ask, mood, debrief, TYPES } from './model.js';
import { PRESETS, DEFAULT_PRESET } from './presets.js';

const ABOUT = {
  intro: 'A branching interview with a fixed question budget. Every answer is written in advance; the rules below decide which answer you get.',
  equations: [
    'Each person starts with a trust level from 0 to 4 (guarded below 2, neutral at 2, open at 3 or more).',
    'Some questions only appear after another question has been asked (often to someone else).',
    'Some answers need trust: asked too early, the person gives a guarded answer, nothing is revealed, and the question is used up.',
    'Making it safe to talk (no attribution, not hunting people) raises that person’s trust by 2. A leading question lowers it by 1.',
    `Question quality = points ÷ (3 × questions asked). Points: ${Object.values(TYPES).map((t) => `${t.label.toLowerCase()} ${t.quality > 0 ? '+' : ''}${t.quality}`).join(', ')}; a guarded answer scores 0.`,
    'The debrief checks whether you found the four facts that make the case for the real problem.',
  ],
  assumptions: [
    'People answer honestly from their own seat; they only hold back when it is not safe or the question does not reach the fact.',
    'A real interview has follow-ups and silences; here every question is a single exchange.',
  ],
  leftOut: [
    'Your tone of voice and body language, which matter at least as much as the words.',
    'The data room: in the course you check every claim here against the exports (lesson 02.4).',
  ],
};

let shell;
let scenario;
let state;
let selected;
let finished = false;
let view = {};

function start(key) {
  scenario = PRESETS[key];
  state = createState(scenario);
  selected = scenario.cast[0].id;
  finished = false;
  build();
  renderAll();
}

function person(id) {
  return scenario.cast.find((p) => p.id === id);
}

function build() {
  view.status = h('div', { class: 'stats' });
  const people = panel('People', { id: 'people' });
  view.people = h('div', { class: 'people', role: 'group', 'aria-label': 'Choose who to ask' });
  people.body.appendChild(view.people);
  const qs = panel('Questions', { id: 'questions' });
  view.qHeading = qs.heading;
  view.questions = h('div');
  qs.body.appendChild(view.questions);

  const transcript = panel('Transcript', { id: 'transcript' });
  view.transcript = h('ol', { class: 'transcript' });
  transcript.body.appendChild(view.transcript);
  const notebook = panel('Your notebook', { id: 'notebook' });
  view.notebook = h('div');
  notebook.body.appendChild(view.notebook);

  const finish = panel('What is the real problem?', { id: 'finish', className: 'debrief' });
  view.finishHeading = finish.heading;
  view.finish = h('div');
  finish.body.appendChild(view.finish);

  replace(shell.main,
    view.status,
    h('div', { class: 'layout layout-2' },
      h('div', { class: 'stack' }, people.el, qs.el),
      h('div', { class: 'stack' }, transcript.el, notebook.el)),
    finish.el);
}

function renderAll() {
  renderStatus();
  renderPeople();
  renderQuestions();
  renderTranscript();
  renderNotebook();
  renderFinish();
}

function renderStatus() {
  replace(view.status,
    stat('Questions left', `${num(state.budget)} of ${num(scenario.budget)}`, null, state.budget <= 2 ? 'warn' : ''),
    stat('Facts in your notebook', num(state.facts.length)),
  );
}

function renderPeople() {
  replace(view.people, scenario.cast.map((p) => {
    const m = mood(state.trust[p.id]);
    return h('button', {
      type: 'button', class: `person ${p.id === selected ? 'is-selected' : ''}`,
      'aria-pressed': p.id === selected ? 'true' : 'false',
      onClick: () => { selected = p.id; renderPeople(); renderQuestions(); },
    },
    h('span', { class: 'person-name' }, p.name),
    h('span', { class: 'person-role' }, p.role),
    h('span', { class: `tag tag-${m === 'open' ? 'good' : m === 'guarded' ? 'bad' : 'neutral'}` }, m));
  }));
}

function renderQuestions() {
  const p = person(selected);
  view.qHeading.textContent = `Ask ${p.name}`;
  if (finished) {
    replace(view.questions, h('p', { class: 'muted' }, 'The interviews are over.'));
    return;
  }
  if (state.budget <= 0) {
    replace(view.questions, h('p', {}, 'You have used all your questions. Name the real problem below.'));
    return;
  }
  const qs = availableQuestions(state, scenario, selected);
  const hidden = hiddenCount(state, scenario, selected);
  replace(view.questions,
    h('p', { class: 'muted small' }, `${p.role}. Currently ${mood(state.trust[selected])}.`),
    qs.length
      ? h('ul', { class: 'question-list' }, qs.map((q) => h('li', {},
        h('button', { type: 'button', class: 'question', onClick: () => onAsk(q.id) }, q.text))))
      : h('p', {}, `Nothing more to ask ${p.name.split(' ')[0]} right now.`),
    hidden ? h('p', { class: 'muted small' }, `${plural(hidden, 'more question')} may open up once you know more.`) : null,
  );
}

function onAsk(qid) {
  const res = ask(state, scenario, qid);
  state = res.state;
  renderAll();
  focusEl(view.transcript.lastChild);
  const e = res.entry;
  shell.announce(`${person(e.who).name}: ${e.answer}${e.newFacts.length ? ` Added ${plural(e.newFacts.length, 'fact')} to your notebook.` : ''}`);
}

function trustNote(e) {
  const first = person(e.who).name.split(' ')[0];
  if (e.trustAfter > e.trustBefore) return `${first} relaxes.`;
  if (e.trustAfter < e.trustBefore) return `${first} closes up a little.`;
  return null;
}

function renderTranscript() {
  if (!state.log.length) {
    replace(view.transcript, h('li', { class: 'muted empty' }, 'No questions asked yet.'));
    return;
  }
  replace(view.transcript, state.log.map((e) => {
    const note = trustNote(e);
    return h('li', { class: 'exchange' },
      h('p', { class: 'q' }, h('span', { class: 'who' }, 'You → ', person(e.who).name, ': '), e.text),
      h('p', { class: 'a' }, h('span', { class: 'who' }, person(e.who).name.split(' ')[0], ': '), e.answer,
        e.guarded ? h('span', { class: 'tag tag-warn' }, ' guarded answer') : null),
      note ? h('p', { class: 'muted small' }, note) : null,
      e.newFacts.length
        ? h('p', { class: 'small new-fact' }, 'Added to your notebook: ',
          e.newFacts.map((f) => scenario.facts.find((x) => x.id === f).text).join(' '))
        : null,
    );
  }));
}

function renderNotebook() {
  if (!state.facts.length) {
    replace(view.notebook, h('p', { class: 'muted' }, 'Facts you learn appear here.'));
    return;
  }
  replace(view.notebook, h('ul', {}, state.facts.map((f) => h('li', {}, scenario.facts.find((x) => x.id === f).text))));
}

function renderFinish() {
  if (finished) return;
  const name = 'diagnosis';
  const radios = scenario.diagnoses.map((d, i) => h('input', { type: 'radio', name, id: `dx-${i}`, value: d.id }));
  const options = scenario.diagnoses.map((d, i) => h('div', { class: 'choice' }, radios[i], h('label', { for: `dx-${i}` }, d.text)));
  const err = h('p', { class: 'callout callout-warn', role: 'alert', hidden: true }, 'Choose one answer first.');
  const submit = button('Submit my diagnosis', () => {
    const chosen = radios.find((r) => r.checked);
    if (!chosen) {
      err.hidden = false;
      return;
    }
    finished = true;
    renderQuestions();
    renderDebrief(chosen.value);
  });
  replace(view.finish,
    h('p', {}, state.budget > 0
      ? `You can answer now or keep interviewing (${plural(state.budget, 'question')} left). Once you answer, the interviews end.`
      : 'Your questions are used up. Based on your notebook, what is the real problem?'),
    h('fieldset', { class: 'group choices' }, h('legend', {}, 'The real problem at Harbor & Pine is…'), options),
    err,
    h('div', { class: 'btn-row' }, submit),
  );
}

function renderDebrief(choiceId) {
  const d = debrief(state, scenario, choiceId);
  const tone = d.verdict === 'strong' ? 'good' : d.verdict === 'thin' ? 'warn' : 'bad';
  const headline = d.verdict === 'strong'
    ? 'Right answer, and you have the evidence to defend it.'
    : d.verdict === 'thin'
      ? `Right answer, thin evidence: you found ${d.keyFound} of the ${d.keyTotal} key facts. The CFO would ask how you know.`
      : 'Not the real problem.';

  view.finishHeading.textContent = 'Debrief';
  replace(view.finish,
    h('div', { class: `callout callout-${tone}` },
      h('p', {}, h('strong', {}, headline)),
      h('p', {}, `You chose: “${d.option.text}”`),
      h('p', {}, d.option.feedback)),

    h('h3', {}, `The evidence chain: ${d.keyFound} of ${d.keyTotal} key facts found`),
    h('ul', { class: 'facts' }, d.facts.map((f) => h('li', {},
      h('span', { class: `tag ${f.found ? 'tag-good' : 'tag-bad'}` }, f.found ? 'found' : 'missed'),
      f.key ? h('span', { class: 'tag tag-neutral' }, 'key') : null, ' ', f.text))),
    d.missedKey.length ? h('div', {},
      h('h3', {}, 'How you could have found the key facts you missed'),
      h('ul', {}, d.missedKey.map((f) => h('li', {}, f.text, h('ul', {}, f.routes.map((r) => h('li', {},
        `Ask ${r.person}: “${r.question}”`,
        r.after.length ? ` — it only opens after ${r.after.join(r.afterMode === 'or' ? ' or ' : ' and ')}` : '',
        r.needTrust ? `; ${r.person.split(' ')[0]} answers only once it is safe to talk` : '',
        '.'))))))) : null,

    h('h3', {}, `Question quality: ${pct(d.quality / 100)}`),
    h('div', { class: 'table-wrap' }, h('table', {},
      h('caption', { class: 'sr-only' }, 'Questions you asked by type'),
      h('thead', {}, h('tr', {}, h('th', { scope: 'col' }, 'Type'), h('th', { scope: 'col' }, 'Asked'), h('th', { scope: 'col' }, 'Points each'))),
      h('tbody', {}, Object.entries(TYPES).map(([k, t]) => h('tr', {},
        h('th', { scope: 'row' }, t.label), h('td', {}, num(d.byType[k] || 0)), h('td', {}, `${t.quality > 0 ? '+' : ''}${t.quality}`)))))),
    d.leading.length
      ? h('div', {}, h('p', {}, h('strong', {}, 'Leading questions that cost trust:')),
        h('ul', {}, d.leading.map((l) => h('li', {}, `${l.who}: “${l.text}”`, l.trustCost ? ` (trust −${l.trustCost})` : ' (no trust lost, nothing learned)'))),
        h('p', { class: 'small' }, 'A leading question tells the person which answer you want. You get your own opinion back and lose the facts they would have offered.'))
      : h('p', {}, 'You asked no leading questions.'),
    d.guardedAnswers.length
      ? h('div', {}, h('p', {}, h('strong', {}, 'Asked before it was safe to answer:')),
        h('ul', {}, d.guardedAnswers.map((g) => h('li', {}, `${g.who}: “${g.text}”`))),
        h('p', { class: 'small' }, 'Say why you are there and that nothing is attributed before you ask people to show you their numbers or their workarounds.'))
      : null,
    d.budgetLeft > 0 ? h('p', { class: 'small muted' }, `You finished with ${plural(d.budgetLeft, 'question')} unused.`) : null,

    h('h3', {}, 'The point of this lesson'),
    h('p', { class: 'lesson-point' }, scenario.lessonPoint),
    h('div', { class: 'btn-row' }, button('Interview again', () => { start(shell.presetKey); focusEl(view.qHeading); }, { variant: 'secondary' })),
  );
  focusEl(view.finishHeading);
  shell.announce(headline);
}

shell = mountShell({
  title: 'Discovery interview',
  tagline: 'Twelve questions, five people, one real problem.',
  presets: PRESETS,
  defaultPreset: DEFAULT_PRESET,
  about: ABOUT,
  onPreset: start,
});
start(shell.presetKey);
