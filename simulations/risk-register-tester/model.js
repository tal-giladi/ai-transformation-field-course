// Risk register tester: pure engine (no DOM). The register (risks, owners' ratings, the evidence each
// test would find, the true rating) lives in presets.js.

export const RATINGS = ['green', 'amber', 'red'];
const LEVEL = { green: 0, amber: 1, red: 2 };

export const METHODS = {
  ask: { label: 'Ask the owner', verb: 'asked the owner' },
  sample: { label: 'Sample the evidence', verb: 'sampled the evidence' },
  test: { label: 'Run a test', verb: 'ran a test' },
};

/** What a rating means, in the words the debrief uses. */
export const VERDICTS = {
  earned: { label: 'earned green', tone: 'good', score: 1 },
  right: { label: 'right', tone: 'good', score: 1 },
  untested: { label: 'green, untested', tone: 'warn', score: 0.5 },
  overstated: { label: 'overstated', tone: 'warn', score: 0.5 },
  overstated2: { label: 'overstated by two levels', tone: 'warn', score: 0.25 },
  understated: { label: 'understated', tone: 'bad', score: 0 },
  unearned: { label: 'unearned green', tone: 'bad', score: 0 },
};

export function createState(scenario) {
  const ratings = {};
  const gathered = {};
  for (const r of scenario.risks) { ratings[r.id] = r.ownerRating; gathered[r.id] = []; }
  return { budget: scenario.budget, ratings, gathered, submitted: false };
}

export function canGather(state, scenario, riskId, method) {
  return !state.submitted && !state.gathered[riskId].includes(method) && scenario.costs[method] <= state.budget;
}

/** Spend budget on one test of one risk. Returns a NEW state. */
export function gather(state, scenario, riskId, method) {
  if (!METHODS[method]) throw new Error(`Unknown method ${method}`);
  if (!canGather(state, scenario, riskId, method)) throw new Error(`Cannot ${method} ${riskId} now`);
  return {
    ...state,
    budget: state.budget - scenario.costs[method],
    gathered: { ...state.gathered, [riskId]: [...state.gathered[riskId], method] },
  };
}

export function rate(state, riskId, rating) {
  if (!RATINGS.includes(rating)) throw new Error(`Unknown rating ${rating}`);
  if (state.submitted) throw new Error('Already submitted');
  return { ...state, ratings: { ...state.ratings, [riskId]: rating } };
}

/** Did the learner gather conclusive evidence about this risk's control? */
export function hasStrongEvidence(state, risk) {
  return state.gathered[risk.id].some((m) => risk.evidence[m].strength === 'strong');
}

/** Classify one rating against the truth. `tested` = conclusive evidence was gathered. */
export function verdict(rating, truth, tested) {
  if (rating === truth) {
    if (rating === 'green') return tested ? 'earned' : 'untested';
    return 'right';
  }
  if (rating === 'green') return 'unearned';
  const diff = LEVEL[rating] - LEVEL[truth];
  if (diff >= 2) return 'overstated2';
  if (diff === 1) return 'overstated';
  return 'understated';
}

/** Credibility of a register (0–100) given ratings and which risks were tested. */
export function credibility(scenario, ratings, testedIds) {
  let sum = 0;
  const rows = scenario.risks.map((r) => {
    const v = verdict(ratings[r.id], r.truth.rating, testedIds.includes(r.id));
    sum += VERDICTS[v].score;
    return { id: r.id, verdict: v };
  });
  return { score: Math.round((sum / scenario.risks.length) * 100), rows };
}

const count = (rows, v) => rows.filter((x) => x.verdict === v).length;

/** Counts shown in the status bar while the learner works. */
export function registerCounts(state, scenario) {
  const greens = scenario.risks.filter((r) => state.ratings[r.id] === 'green');
  return {
    green: greens.length,
    amber: scenario.risks.filter((r) => state.ratings[r.id] === 'amber').length,
    red: scenario.risks.filter((r) => state.ratings[r.id] === 'red').length,
    untestedGreens: greens.filter((r) => !hasStrongEvidence(state, r)).length,
    tested: scenario.risks.filter((r) => hasStrongEvidence(state, r)).length,
  };
}

export function debrief(state, scenario) {
  const tested = scenario.risks.filter((r) => hasStrongEvidence(state, r)).map((r) => r.id);
  const owners = {};
  for (const r of scenario.risks) owners[r.id] = r.ownerRating;
  const before = credibility(scenario, owners, []);
  const after = credibility(scenario, state.ratings, tested);
  const rows = scenario.risks.map((r, i) => ({
    risk: r,
    owner: r.ownerRating,
    yours: state.ratings[r.id],
    truth: r.truth.rating,
    gathered: state.gathered[r.id],
    tested: tested.includes(r.id),
    ownerVerdict: before.rows[i].verdict,
    verdict: after.rows[i].verdict,
  }));
  const ownerUnearned = rows.filter((x) => x.ownerVerdict === 'unearned');
  return {
    before: before.score,
    after: after.score,
    rows,
    spent: scenario.budget - state.budget,
    unearnedLeft: count(after.rows, 'unearned'),
    unearnedFound: ownerUnearned.filter((x) => x.verdict !== 'unearned').length,
    unearnedTotal: ownerUnearned.length,
    earned: count(after.rows, 'earned'),
    untested: count(after.rows, 'untested'),
    overstatedLeft: count(after.rows, 'overstated') + count(after.rows, 'overstated2'),
    understated: count(after.rows, 'understated'),
    askOnly: rows.filter((x) => x.gathered.length && x.gathered.every((m) => m === 'ask')).length,
  };
}

/** Check a scenario's data; returns a list of problems. */
export function validateScenario(s) {
  const problems = [];
  const ids = new Set();
  for (const r of s.risks) {
    if (ids.has(r.id)) problems.push(`duplicate risk ${r.id}`);
    ids.add(r.id);
    if (!RATINGS.includes(r.ownerRating)) problems.push(`${r.id}: bad owner rating`);
    if (!RATINGS.includes(r.truth.rating)) problems.push(`${r.id}: bad true rating`);
    for (const m of Object.keys(METHODS)) {
      const e = r.evidence[m];
      if (!e || !e.text) problems.push(`${r.id}: missing ${m} evidence`);
      else if (!['none', 'weak', 'strong'].includes(e.strength)) problems.push(`${r.id}/${m}: bad strength`);
    }
    if (!['sample', 'test'].some((m) => r.evidence[m] && r.evidence[m].strength === 'strong')) problems.push(`${r.id}: no conclusive way to test it`);
  }
  for (const m of Object.keys(METHODS)) if (!(s.costs[m] > 0)) problems.push(`cost of ${m} missing`);
  if (!s.lessonPoint) problems.push('missing lessonPoint');
  return problems;
}
