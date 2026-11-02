import { h, replace, focusEl } from '../common/dom.js';
import { mountShell, panel } from '../common/shell.js';
import { button, stat } from '../common/controls.js';
import { stackTable } from '../common/table.js';
import { num } from '../common/format.js';
import { createState, currentRound, choose, support, moodLabel, honestyLabel, debrief, TYPES, MAX_MOOD } from './model.js';
import { PRESETS, DEFAULT_PRESET } from './presets.js';

const ABOUT = {
  intro: 'A branching meeting. Every line is written in advance; the rules below decide how the room reacts and what it decides.',
  equations: [
    'Each member has a mood from 0 (hostile) to 4 (champion). Each answer moves some moods up or down by 1 or 2.',
    'Support in the room = the weighted average of the moods. The CEO and CFO count 2, the sponsor 1.5, the others 1.',
    'Paper honesty starts at 0. Overclaiming, deferring a number into the minutes or stating a guess as fact lowers it; separating evidence from inference and conceding a weak point raise it. Clean at 0 or more, bent at −1 or −2, broken below.',
    'Some questions only come up because of an earlier answer (for example, the CFO asks which number goes to the board if the sponsor’s number was left standing).',
    'The outcome is the first rule that matches: killed if support is very low; sent back if nobody asked for a decision, if a blocking risk was left open or if the CFO no longer trusts the numbers; approved with conditions if you asked for a decision with conditions and support is at least 2.2; approved if you asked without conditions.',
    '“Six months later” depends on the outcome and on how honest the paper stayed.',
  ],
  assumptions: [
    'People react to what you say, not to how you say it; in a real room tone, timing and the meetings before the meeting matter as much.',
    'Each member has one main concern. Real members have several and trade them off.',
  ],
  leftOut: [
    'The one-to-one meetings before the steering group, where most decisions are really made (lesson 07.4 covers them).',
    'The written paper itself: lesson 07.1 builds it.',
  ],
};

let shell;
let scenario;
let state;
let view = {};

function start(key) {
  scenario = PRESETS[key];
  state = createState(scenario);
  build();
  renderAll();
}

const person = (id) => scenario.cast.find((p) => p.id === id);
const first = (id) => person(id).name.split(' ')[0];
const moodTone = (m) => (m >= 3 ? 'good' : m <= 1 ? 'bad' : 'neutral');

function build() {
  view.status = h('div', { class: 'stats' });

  const room = panel('Around the table', { id: 'room' });
  view.room = h('ul', { class: 'room' });
  room.body.append(view.room);
  if (scenario.paper && scenario.paper.length) {
    room.body.append(h('details', { class: 'notes' }, h('summary', {}, 'Your paper (sent on Sunday)'),
      h('ul', {}, scenario.paper.map((l) => h('li', {}, l)))));
  }
  if (scenario.notes && scenario.notes.length) {
    room.body.append(h('details', { class: 'notes' }, h('summary', {}, 'Where these numbers come from'),
      h('ul', {}, scenario.notes.map((n) => h('li', {}, n)))));
  }

  const now = panel('Now', { id: 'now' });
  view.nowHeading = now.heading;
  view.now = h('div');
  now.body.append(view.now);

  const transcript = panel('Minutes so far', { id: 'transcript' });
  view.transcript = h('ol', { class: 'transcript' });
  transcript.body.append(view.transcript);

  const result = panel('Debrief', { id: 'result', className: 'debrief' });
  view.resultPanel = result.el;
  view.resultHeading = result.heading;
  view.result = h('div');
  result.body.append(view.result);
  view.resultPanel.hidden = true;

  replace(shell.main,
    view.status,
    h('div', { class: 'layout layout-2' },
      h('div', { class: 'stack' }, room.el),
      h('div', { class: 'stack' }, now.el, transcript.el)),
    result.el);
}

function renderAll() {
  renderStatus();
  renderRoom();
  renderNow();
  renderTranscript();
}

function renderStatus() {
  const s = support(state, scenario);
  replace(view.status,
    stat('Support in the room', `${num(s, 1)} of ${MAX_MOOD}`, moodLabel(s), s >= 2.2 ? 'good' : s < 1.4 ? 'bad' : 'warn'),
    stat('Paper honesty', honestyLabel(state.honesty), state.honesty < 0 ? 'the paper says more than the evidence' : 'the paper matches the evidence',
      state.honesty >= 0 ? 'good' : state.honesty >= -2 ? 'warn' : 'bad'),
    stat('Questions answered', num(state.log.length)),
  );
}

function renderRoom() {
  replace(view.room, scenario.cast.map((p) => {
    const m = state.moods[p.id];
    return h('li', { class: 'member' },
      h('div', { class: 'member-head' },
        h('span', { class: 'member-name' }, p.name),
        h('span', { class: `tag tag-${moodTone(m)}` }, moodLabel(m))),
      h('div', { class: 'member-role' }, p.role, p.sponsor ? ' · sponsor' : ''),
      h('p', { class: 'small member-concern' }, p.concern));
  }));
}

function renderNow() {
  const round = currentRound(state, scenario);
  if (!round) {
    view.nowHeading.textContent = 'The meeting is over';
    replace(view.now, h('p', {}, 'The decision and what happened next are in the debrief below.'));
    return;
  }
  const who = person(round.speaker);
  view.nowHeading.textContent = `${who.name} asks`;
  replace(view.now,
    h('blockquote', { class: 'prompt' }, h('p', {}, `“${round.prompt}”`)),
    h('p', { class: 'small muted' }, 'How do you answer?'),
    h('ul', { class: 'choice-list' }, round.choices.map((c) => h('li', {},
      h('button', { type: 'button', class: 'choice-btn', onClick: () => onChoose(c.id) }, c.text)))),
  );
}

function moodNote(e) {
  if (!e.moodChanges.length) return null;
  return e.moodChanges.map((m) => `${first(m.who)}: ${moodLabel(m.before)} → ${moodLabel(m.after)}`).join(' · ');
}

function renderTranscript() {
  if (!state.log.length) {
    replace(view.transcript, h('li', { class: 'muted empty' }, 'Nothing said yet.'));
    return;
  }
  replace(view.transcript, state.log.map((e) => {
    const note = moodNote(e);
    return h('li', { class: 'exchange' },
      h('p', { class: 'q' }, h('span', { class: 'who' }, `${first(e.speaker)}: `), e.prompt),
      h('p', { class: 'a' }, h('span', { class: 'who' }, 'You: '), e.text),
      h('p', { class: 'small' }, e.reply),
      note ? h('p', { class: 'small muted' }, note) : null,
    );
  }));
}

function onChoose(id) {
  const res = choose(state, scenario, id);
  state = res.state;
  renderAll();
  const note = moodNote(res.entry);
  if (state.done) {
    renderDebrief();
  } else {
    focusEl(view.nowHeading);
    shell.announce(`${res.entry.reply}${note ? ` ${note}.` : ''} Next: ${view.nowHeading.textContent}.`);
  }
}

function renderDebrief() {
  const d = debrief(state, scenario);
  const o = d.outcome;
  const tone = o.kind === 'conditions' ? (d.honesty >= 0 ? 'good' : 'warn') : o.kind === 'approved' ? 'warn' : 'bad';
  view.resultPanel.hidden = false;

  const adv = d.advocate[0];
  const reframe = TYPES.reframe;

  replace(view.result,
    h('div', { class: `callout callout-${tone}` },
      h('p', {}, h('strong', {}, o.title)),
      h('p', {}, o.text)),
    h('h3', {}, 'Six months later'),
    h('p', {}, o.laterText),

    h('h3', {}, 'The room at the end'),
    stackTable({
      caption: 'Each member’s mood at the start and at the end',
      head: ['Member', 'Start', 'End', 'Their concern'],
      rows: d.members.map((m) => ({
        th: m.name,
        cells: [moodLabel(m.start), h('span', { class: `tag tag-${moodTone(m.end)}` }, moodLabel(m.end)), h('span', { class: 'small' }, m.concern)],
      })),
    }),
    h('p', {}, `Support in the room: ${num(d.support, 1)} of ${MAX_MOOD}. Paper honesty: ${d.honestyLabel} (${d.honesty > 0 ? '+' : ''}${num(d.honesty)}).`),

    h('h3', {}, 'Your answers, by kind'),
    h('ul', { class: 'type-list' }, Object.entries(TYPES).filter(([k]) => d.byType[k]).map(([k, t]) => h('li', {},
      h('span', { class: `tag tag-${t.good ? 'good' : 'bad'}` }, `${t.label} ×${d.byType[k]}`), ' ', t.note))),
    d.weakMoves.length
      ? h('div', {}, h('p', {}, h('strong', {}, 'Where a stronger answer was available:')),
        h('ul', {}, d.weakMoves.map((e) => {
          const r = scenario.rounds.find((x) => x.id === e.round);
          const better = r.choices.filter((c) => TYPES[c.type].good).map((c) => c.text);
          return h('li', {}, `${first(e.speaker)}: “${e.prompt}” You: ${TYPES[e.type].label.toLowerCase()}.`,
            better.length ? h('span', { class: 'small' }, ` A stronger answer: ${better[0]}`) : null);
        })))
      : h('p', {}, 'Every answer you gave was one of the strong kinds.'),

    adv ? h('div', {},
      h('h3', {}, 'When the sponsor is also the advocate'),
      h('p', {}, `${first(adv.speaker)} argued past the evidence. You chose: ${TYPES[adv.type].label.toLowerCase()}.`),
      h('p', { class: 'small' }, `${reframe.label}: ${reframe.note} Agreeing makes their number yours; correcting them bluntly keeps the number and costs you the sponsor; deferring lets the number into the minutes.`))
      : null,

    h('h3', {}, 'The point of this lesson'),
    h('p', { class: 'lesson-point' }, scenario.lessonPoint),
    h('div', { class: 'btn-row' }, button('Run the meeting again', () => { start(shell.presetKey); focusEl(view.nowHeading); }, { variant: 'secondary' })),
  );
  focusEl(view.resultHeading);
  shell.announce(`${o.title}. ${o.laterText}`);
}

shell = mountShell({
  title: 'Steering committee',
  tagline: 'Five members, one recommendation, one decision to leave with.',
  presets: PRESETS,
  defaultPreset: DEFAULT_PRESET,
  about: ABOUT,
  onPreset: start,
});
start(shell.presetKey);
