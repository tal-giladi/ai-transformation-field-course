// Discovery interview: pure engine (no DOM). The scenario (cast, questions, facts, diagnosis options)
// lives in presets.js; this file only applies the rules.

/** Question types, their quality points and what the debrief calls them. */
export const TYPES = {
  rapport: { label: 'Making it safe to talk', quality: 2 },
  open: { label: 'Open question', quality: 2 },
  workflow: { label: 'Workflow walk-through', quality: 3 },
  numbers: { label: 'Asking for numbers', quality: 2 },
  showme: { label: '“Show me” request', quality: 3 },
  sameword: { label: 'Same-word check', quality: 3 },
  leading: { label: 'Leading question', quality: -2 },
};

export const MAX_TRUST = 4;

export function createState(scenario) {
  const trust = {};
  for (const p of scenario.cast) trust[p.id] = p.trust;
  return {
    budget: scenario.budget,
    asked: [],
    trust,
    flags: [],
    facts: [],
    log: [],
    done: false,
  };
}

const has = (list, x) => list.includes(x);

/** Is this question visible now (not asked yet, prerequisites met)? */
export function isAvailable(state, q) {
  if (has(state.asked, q.id)) return false;
  if (q.requires && !q.requires.every((f) => has(state.flags, f))) return false;
  if (q.requiresAny && !q.requiresAny.some((f) => has(state.flags, f))) return false;
  return true;
}

/** Questions the learner can ask this person now. */
export function availableQuestions(state, scenario, personId) {
  return scenario.questions.filter((q) => q.who === personId && isAvailable(state, q));
}

/** Count of questions still hidden for this person (prerequisite not met yet). */
export function hiddenCount(state, scenario, personId) {
  return scenario.questions.filter((q) => q.who === personId && !has(state.asked, q.id) && !isAvailable(state, q)).length;
}

/** Mood label from trust. */
export function mood(trust) {
  if (trust >= 3) return 'open';
  if (trust >= 2) return 'neutral';
  return 'guarded';
}

/**
 * Ask a question. Returns a NEW state and the entry added to the log.
 * A question asked while trust is below q.needTrust gets the guarded answer and reveals nothing.
 */
export function ask(state, scenario, qid) {
  if (state.done || state.budget <= 0) throw new Error('No questions left');
  const q = scenario.questions.find((x) => x.id === qid);
  if (!q) throw new Error(`Unknown question ${qid}`);
  if (!isAvailable(state, q)) throw new Error(`Question ${qid} is not available`);

  const trustBefore = state.trust[q.who];
  const guarded = q.needTrust !== undefined && trustBefore < q.needTrust;
  const answer = guarded ? q.guarded : q.answer;
  const newFacts = guarded ? [] : (q.reveals || []).filter((f) => !has(state.facts, f));
  const newFlags = guarded ? [] : (q.sets || []).filter((f) => !has(state.flags, f));
  const delta = q.trust || 0;
  const trustAfter = Math.max(0, Math.min(MAX_TRUST, trustBefore + delta));

  const entry = {
    qid: q.id, who: q.who, type: q.type, text: q.text, answer, guarded,
    newFacts, trustBefore, trustAfter,
  };
  const next = {
    ...state,
    budget: state.budget - 1,
    asked: [...state.asked, q.id],
    trust: { ...state.trust, [q.who]: trustAfter },
    flags: [...state.flags, ...newFlags],
    facts: [...state.facts, ...newFacts],
    log: [...state.log, entry],
  };
  return { state: next, entry };
}

/** Which question (and prerequisite) would have revealed a fact. */
export function routeTo(scenario, factId) {
  const qs = scenario.questions.filter((q) => (q.reveals || []).includes(factId));
  return qs.map((q) => {
    const person = scenario.cast.find((p) => p.id === q.who);
    const pre = [...(q.requires || []), ...(q.requiresAny || [])]
      .map((f) => scenario.questions.find((x) => (x.sets || []).includes(f)))
      .filter(Boolean);
    return {
      person: person.name, question: q.text, needTrust: q.needTrust,
      after: pre.map((x) => `${scenario.cast.find((p) => p.id === x.who).name}: “${x.text}”`),
      afterMode: q.requiresAny ? 'or' : 'and',
    };
  });
}

/** Debrief for a finished interview and the learner's chosen diagnosis. */
export function debrief(state, scenario, diagnosisId) {
  const option = scenario.diagnoses.find((d) => d.id === diagnosisId);
  const correct = Boolean(option && option.correct);
  const facts = scenario.facts.map((f) => ({ ...f, found: has(state.facts, f.id) }));
  const key = facts.filter((f) => f.key);
  const keyFound = key.filter((f) => f.found).length;

  const qualityPoints = state.log.reduce((a, e) => a + (e.guarded ? 0 : TYPES[e.type].quality), 0);
  const maxPoints = state.log.length * 3 || 1;
  const quality = Math.max(0, Math.round((qualityPoints / maxPoints) * 100));

  const leading = state.log.filter((e) => e.type === 'leading').map((e) => ({
    who: scenario.cast.find((p) => p.id === e.who).name,
    text: e.text,
    trustCost: e.trustBefore - e.trustAfter,
  }));
  const guardedAnswers = state.log.filter((e) => e.guarded).map((e) => ({
    who: scenario.cast.find((p) => p.id === e.who).name,
    text: e.text,
  }));
  const byType = {};
  for (const e of state.log) byType[e.type] = (byType[e.type] || 0) + 1;

  let verdict;
  if (correct && keyFound >= key.length - 1) verdict = 'strong';
  else if (correct) verdict = 'thin';
  else verdict = 'missed';

  return {
    option, correct, verdict, facts, keyFound, keyTotal: key.length,
    quality, qualityPoints, asked: state.log.length, budgetLeft: state.budget,
    leading, guardedAnswers, byType,
    missedKey: key.filter((f) => !f.found).map((f) => ({ ...f, routes: routeTo(scenario, f.id) })),
  };
}
