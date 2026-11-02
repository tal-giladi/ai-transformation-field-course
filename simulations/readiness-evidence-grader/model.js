// Readiness evidence grader: pure engine (no DOM). The evidence items, their true status, the verdict
// options and the steering group's reactions live in presets.js.
//
// The learner sorts each item: verified (checked against data you hold or seen yourself), reported
// (someone says so; not checked) or contradicted (data you hold says otherwise). Then picks a verdict.

export const STATUSES = {
  verified: { label: 'Verified', rank: 2, note: 'checked against data you hold, or seen yourself' },
  reported: { label: 'Reported', rank: 1, note: 'someone says so; not checked yet' },
  contradicted: { label: 'Contradicted', rank: 0, note: 'data you hold says otherwise' },
};

export const KINDS = {
  interview: 'Interview note',
  dashboard: 'Dashboard or report',
  policy: 'Policy or handbook',
  export: 'Data export profile',
  vendor: 'Vendor statement',
  email: 'Email',
  screen: 'Screen you checked',
};

/** How one sorting compares with the truth. */
export function classify(pick, truth) {
  if (pick === truth) return 'right';
  if (pick === 'verified') return 'overclaim';
  if (truth === 'contradicted') return 'missedContradiction';
  return 'other';
}

export const PENALTY = { right: 0, overclaim: 12, missedContradiction: 6, other: 3 };

/** The learner's report: per-item results, credibility and whether it counts as over-claimed. */
export function grade(scenario, picks) {
  const rows = scenario.items.map((it) => {
    const pick = picks[it.id] || null;
    const result = pick ? classify(pick, it.truth) : 'unsorted';
    return { item: it, pick, result };
  });
  const sorted = rows.filter((r) => r.pick);
  const count = (k) => rows.filter((r) => r.result === k).length;
  const penalty = sorted.reduce((a, r) => a + PENALTY[r.result], 0);
  const overclaims = count('overclaim');
  return {
    rows,
    right: count('right'),
    overclaims,
    missedContradictions: count('missedContradiction'),
    other: count('other'),
    unsorted: count('unsorted'),
    credibility: Math.max(0, 100 - penalty),
    overclaimed: overclaims >= scenario.overclaimThreshold,
    challenges: rows.filter((r) => r.result === 'overclaim' || r.result === 'missedContradiction'),
  };
}

/** Counts of the learner's picks, for the status bar. */
export function tally(scenario, picks) {
  const t = { verified: 0, reported: 0, contradicted: 0, unsorted: 0 };
  for (const it of scenario.items) t[picks[it.id] || 'unsorted'] += 1;
  return t;
}

/** The steering group's reaction to a verdict given an honest or an over-claimed report. */
export function reaction(scenario, verdictId, overclaimed) {
  const v = scenario.verdicts.find((x) => x.id === verdictId);
  if (!v) throw new Error(`Unknown verdict ${verdictId}`);
  return { verdict: v, text: overclaimed ? v.reactions.overclaimed : v.reactions.honest, tone: overclaimed ? v.tones.overclaimed : v.tones.honest };
}

export function debrief(scenario, picks, verdictId) {
  const g = grade(scenario, picks);
  return {
    ...g,
    mine: reaction(scenario, verdictId, g.overclaimed),
    honest: reaction(scenario, verdictId, false),
    inflated: reaction(scenario, verdictId, true),
    bestVerdict: scenario.verdicts.find((v) => v.best),
    verdictRight: scenario.verdicts.find((v) => v.id === verdictId).best === true,
  };
}

/** Check a scenario's data; returns a list of problems. */
export function validateScenario(s) {
  const problems = [];
  const ids = new Set(s.items.map((i) => i.id));
  if (ids.size !== s.items.length) problems.push('duplicate item ids');
  if (s.items.length < 14 || s.items.length > 18) problems.push(`${s.items.length} items; aim for 14–18`);
  for (const it of s.items) {
    if (!STATUSES[it.truth]) problems.push(`${it.id}: bad truth`);
    if (!KINDS[it.kind]) problems.push(`${it.id}: bad kind`);
    if (!it.date || !it.source || !it.text || !it.why) problems.push(`${it.id}: needs date, source, text and why`);
    if (it.truth !== 'verified' && !it.challenge) problems.push(`${it.id}: needs a challenge (what the steering group asks if it is over-claimed)`);
    for (const b of it.by || []) if (!ids.has(b)) problems.push(`${it.id}: unknown cross-check ${b}`);
    if (it.truth === 'contradicted' && !(it.by && it.by.some((b) => s.items.find((x) => x.id === b).truth === 'verified'))) {
      problems.push(`${it.id}: a contradiction needs a verified item that shows it`);
    }
  }
  for (const st of Object.keys(STATUSES)) if (!s.items.some((i) => i.truth === st)) problems.push(`no item is ${st}`);
  if (s.verdicts.filter((v) => v.best).length !== 1) problems.push('exactly one verdict must be best');
  for (const v of s.verdicts) if (!v.reactions || !v.reactions.honest || !v.reactions.overclaimed || !v.tones) problems.push(`${v.id}: needs both reactions and tones`);
  if (!(s.overclaimThreshold >= 1)) problems.push('overclaimThreshold missing');
  if (!s.lessonPoint) problems.push('missing lessonPoint');
  return problems;
}
