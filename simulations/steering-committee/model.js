// Steering committee: pure engine (no DOM). The meeting (cast, agenda rounds, answers, outcomes) lives
// in presets.js as data; this file only applies the rules, so a new preset needs no code changes.
//
// Conditions (used by rounds' `when`, outcomes' `when` and `later[].when`) are plain data:
//   { flag: 'x' }  { notFlag: 'x' }  { support: { lt|lte|gt|gte: n } }
//   { mood: { who: 'ronit', lt|lte|gt|gte: n } }  { honesty: { lt|lte|gt|gte: n } }
//   { all: [cond, ...] }  { any: [cond, ...] }  { not: cond }
// A missing `when` is always true.

/** Kinds of response. The learner does not see these while playing; the debrief names them. */
export const TYPES = {
  answerFirst: { label: 'Answer first', good: true, note: 'The recommendation and the ask in the first minute; the reasons after. Busy people decide on what they hear first.' },
  background: { label: 'Background first', good: false, note: 'The story of how you got here before the ask. The room spends its attention waiting for the point.' },
  evidence: { label: 'Evidence vs inference', good: true, note: 'Says what was measured and what is inferred from it, separately. It lets a sceptic check you instead of trusting you.' },
  concede: { label: 'Concede a weakness', good: true, note: 'Names the weak point before someone else finds it, and ties it to a condition. It buys credibility for everything else.' },
  reframe: { label: 'Keep the paper honest, keep the person', good: true, note: 'Takes the point someone is making seriously, then puts the number in its right place (expected case vs an upside to test) without humiliating them.' },
  overclaim: { label: 'Overclaim', good: false, note: 'A bigger number or a firmer promise than the evidence supports. It pleases the room today and becomes your number in six months.' },
  inference: { label: 'Inference stated as fact', good: false, note: 'A guess delivered as if it were known. Often the guess the most anxious person in the room was afraid of.' },
  blunt: { label: 'Correct bluntly in public', good: false, note: 'Right on the facts, but it costs the person their face in front of their peers. You keep the number and lose the ally.' },
  defer: { label: 'Defer', good: false, note: 'Takes it offline or hands it back. Sometimes right for detail; wrong for the question the person actually needs answered in the room.' },
  askDecision: { label: 'Ask for the decision', good: true, note: 'Names the decision, the money, the conditions and who records it. A meeting that is not asked for a decision makes none.' },
};

export const MOODS = ['hostile', 'sceptical', 'neutral', 'supportive', 'champion'];
export const MAX_MOOD = 4;

export function moodLabel(m) {
  return MOODS[Math.max(0, Math.min(MAX_MOOD, Math.round(m)))];
}

export function honestyLabel(h) {
  if (h >= 0) return 'clean';
  if (h >= -2) return 'bent';
  return 'broken';
}

export function createState(scenario) {
  const moods = {};
  for (const p of scenario.cast) moods[p.id] = p.mood;
  const state = { moods, honesty: 0, flags: [], log: [], current: null, done: false };
  return { ...state, current: nextRoundId(state, scenario, -1) };
}

/** Weighted mean of the members' moods (0–4). */
export function support(state, scenario) {
  let w = 0;
  let s = 0;
  for (const p of scenario.cast) {
    const wt = p.weight ?? 1;
    w += wt;
    s += wt * state.moods[p.id];
  }
  return w ? s / w : 0;
}

function compare(x, c) {
  if (c.lt !== undefined && !(x < c.lt)) return false;
  if (c.lte !== undefined && !(x <= c.lte)) return false;
  if (c.gt !== undefined && !(x > c.gt)) return false;
  if (c.gte !== undefined && !(x >= c.gte)) return false;
  return true;
}

/** Evaluate a data condition against the state. */
export function test(cond, state, scenario) {
  if (!cond) return true;
  if (cond.all) return cond.all.every((c) => test(c, state, scenario));
  if (cond.any) return cond.any.some((c) => test(c, state, scenario));
  if (cond.not) return !test(cond.not, state, scenario);
  if (cond.flag !== undefined) return state.flags.includes(cond.flag);
  if (cond.notFlag !== undefined) return !state.flags.includes(cond.notFlag);
  if (cond.support) return compare(support(state, scenario), cond.support);
  if (cond.honesty) return compare(state.honesty, cond.honesty);
  if (cond.mood) return compare(state.moods[cond.mood.who], cond.mood);
  throw new Error(`Unknown condition ${JSON.stringify(cond)}`);
}

function nextRoundId(state, scenario, fromIndex) {
  for (let i = fromIndex + 1; i < scenario.rounds.length; i += 1) {
    const r = scenario.rounds[i];
    if (test(r.when, state, scenario)) return r.id;
  }
  return null;
}

export function currentRound(state, scenario) {
  return scenario.rounds.find((r) => r.id === state.current) || null;
}

/** Apply a response. Returns a NEW state and the log entry. */
export function choose(state, scenario, choiceId) {
  if (state.done) throw new Error('The meeting is over');
  const round = currentRound(state, scenario);
  const choice = round.choices.find((c) => c.id === choiceId);
  if (!choice) throw new Error(`Unknown choice ${choiceId} in round ${round.id}`);

  const moods = { ...state.moods };
  const moodChanges = [];
  for (const [who, d] of Object.entries(choice.moods || {})) {
    const before = moods[who];
    const after = Math.max(0, Math.min(MAX_MOOD, before + d));
    moods[who] = after;
    if (after !== before) moodChanges.push({ who, before, after });
  }
  const flags = [...state.flags, ...(choice.sets || []).filter((f) => !state.flags.includes(f))];
  const entry = {
    round: round.id, speaker: round.speaker, prompt: round.prompt, choice: choice.id, type: choice.type,
    text: choice.text, reply: choice.reply, moodChanges, honestyDelta: choice.honesty || 0, advocate: Boolean(round.advocate),
  };
  const next = {
    ...state, moods, flags, honesty: state.honesty + (choice.honesty || 0), log: [...state.log, entry],
  };
  const idx = scenario.rounds.findIndex((r) => r.id === round.id);
  next.current = nextRoundId(next, scenario, idx);
  next.done = next.current === null;
  return { state: next, entry };
}

/** The first outcome whose condition holds (the last outcome should have no `when`). */
export function outcome(state, scenario) {
  const o = scenario.outcomes.find((x) => test(x.when, state, scenario));
  if (!o) throw new Error('No outcome matched: give the last outcome no `when`.');
  const later = (o.later || []).find((l) => test(l.when, state, scenario));
  return { ...o, laterText: later ? later.text : '' };
}

/** Everything the debrief shows. */
export function debrief(state, scenario) {
  const o = outcome(state, scenario);
  const byType = {};
  for (const e of state.log) byType[e.type] = (byType[e.type] || 0) + 1;
  const members = scenario.cast.map((p) => ({
    ...p, start: p.mood, end: state.moods[p.id], change: state.moods[p.id] - p.mood,
  }));
  const advocate = state.log.filter((e) => e.advocate);
  return {
    outcome: o,
    support: support(state, scenario),
    honesty: state.honesty,
    honestyLabel: honestyLabel(state.honesty),
    members,
    byType,
    goodMoves: state.log.filter((e) => TYPES[e.type].good).length,
    weakMoves: state.log.filter((e) => !TYPES[e.type].good),
    advocate,
  };
}

/**
 * Check a scenario's data. Returns a list of problems (empty when fine). Used by the tests and by
 * writers adding a preset.
 */
export function validateScenario(s) {
  const problems = [];
  const ids = new Set(s.cast.map((p) => p.id));
  if (ids.size !== s.cast.length) problems.push('duplicate cast ids');
  for (const p of s.cast) {
    if (!(p.mood >= 0 && p.mood <= MAX_MOOD)) problems.push(`${p.id}: mood must be 0–4`);
    if (!p.concern) problems.push(`${p.id}: missing concern`);
  }
  const setFlags = new Set();
  const usedFlags = new Set();
  const walk = (cond, where) => {
    if (!cond) return;
    if (cond.all) cond.all.forEach((c) => walk(c, where));
    else if (cond.any) cond.any.forEach((c) => walk(c, where));
    else if (cond.not) walk(cond.not, where);
    else if (cond.flag !== undefined) usedFlags.add(cond.flag);
    else if (cond.notFlag !== undefined) usedFlags.add(cond.notFlag);
    else if (cond.mood) { if (!ids.has(cond.mood.who)) problems.push(`${where}: mood of unknown person ${cond.mood.who}`); }
    else if (!cond.support && cond.honesty === undefined) problems.push(`${where}: unknown condition ${JSON.stringify(cond)}`);
  };
  const roundIds = new Set();
  for (const r of s.rounds) {
    if (roundIds.has(r.id)) problems.push(`duplicate round ${r.id}`);
    roundIds.add(r.id);
    if (r.speaker && !ids.has(r.speaker)) problems.push(`${r.id}: unknown speaker ${r.speaker}`);
    if (!r.choices || r.choices.length < 2) problems.push(`${r.id}: needs at least two choices`);
    walk(r.when, r.id);
    for (const c of r.choices || []) {
      if (!TYPES[c.type]) problems.push(`${r.id}/${c.id}: unknown type ${c.type}`);
      if (!c.text || !c.reply) problems.push(`${r.id}/${c.id}: needs text and reply`);
      for (const who of Object.keys(c.moods || {})) if (!ids.has(who)) problems.push(`${r.id}/${c.id}: unknown person ${who}`);
      for (const f of c.sets || []) setFlags.add(f);
    }
  }
  if (!s.rounds.some((r) => r.advocate)) problems.push('no round is marked advocate (the sponsor-as-advocate moment)');
  const kinds = new Set(['approved', 'conditions', 'sentBack', 'killed']);
  for (const o of s.outcomes) {
    if (!kinds.has(o.kind)) problems.push(`outcome ${o.id}: kind must be one of ${[...kinds].join(', ')}`);
    walk(o.when, `outcome ${o.id}`);
    for (const l of o.later || []) walk(l.when, `outcome ${o.id} later`);
    if (!(o.later || []).some((l) => !l.when)) problems.push(`outcome ${o.id}: needs a default "later" text (one without when)`);
  }
  if (s.outcomes.length && s.outcomes[s.outcomes.length - 1].when) problems.push('the last outcome must have no `when` (fallback)');
  for (const f of usedFlags) if (!setFlags.has(f)) problems.push(`flag "${f}" is tested but never set`);
  if (!s.lessonPoint) problems.push('missing lessonPoint');
  return problems;
}
