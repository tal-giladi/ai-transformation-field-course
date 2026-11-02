// Vendor RFP: pure engine (no DOM). Vendors, claims, documents, proof-of-concept results, contract
// terms and the expert's choice live in presets.js as data; this file scores and compares.
//
// Stages: demo → conditions (how each headline number was measured) → poc (the organization's own
// synthetic notes) → decide (vendor, contract terms, steps before signing) → done. The learner's scores
// (1–5 per vendor and criterion) carry from stage to stage and are snapshotted when a stage ends.

export const STAGES = ['demo', 'conditions', 'poc', 'decide', 'done'];
export const STAGE_LABELS = {
  demo: 'After the demos',
  conditions: 'After the demo conditions',
  poc: 'After the proof of concept',
};
export const HOLDS = {
  yes: { label: 'holds here', tone: 'good' },
  partly: { label: 'partly holds here', tone: 'warn' },
  no: { label: 'does not hold here', tone: 'bad' },
};
export const SCORE_MIN = 1;
export const SCORE_MAX = 5;
export const START_SCORE = 3;

export function createState(preset) {
  const scores = {};
  for (const v of preset.vendors) {
    scores[v.id] = {};
    for (const c of preset.criteria) scores[v.id][c.id] = START_SCORE;
  }
  return { stage: 'demo', scores, snapshots: {}, decision: { pick: null, terms: [], steps: [] } };
}

const copyScores = (s) => JSON.parse(JSON.stringify(s));

/** Set one score (returns a NEW state). */
export function setScore(state, vendorId, criterionId, value) {
  const v = Math.max(SCORE_MIN, Math.min(SCORE_MAX, Math.round(Number(value))));
  if (!Number.isFinite(v)) return state;
  const scores = copyScores(state.scores);
  scores[vendorId][criterionId] = v;
  return { ...state, scores };
}

/** Finish the current stage: snapshot the scores and move on. */
export function advance(state) {
  const i = STAGES.indexOf(state.stage);
  if (i < 0 || i >= STAGES.length - 1) throw new Error('No next stage');
  const snapshots = { ...state.snapshots };
  if (STAGE_LABELS[state.stage]) snapshots[state.stage] = copyScores(state.scores);
  return { ...state, stage: STAGES[i + 1], snapshots };
}

export function setDecision(state, patch) {
  return { ...state, decision: { ...state.decision, ...patch } };
}

/** Weighted score of one vendor (1–5). */
export function weighted(vendorScores, criteria) {
  let sum = 0;
  let w = 0;
  for (const c of criteria) {
    sum += c.weight * vendorScores[c.id];
    w += c.weight;
  }
  return w ? sum / w : 0;
}

/** Vendors sorted by weighted score, highest first (ties keep the preset's order). */
export function ranking(scores, preset) {
  return preset.vendors
    .map((v, i) => ({ id: v.id, name: v.name, total: weighted(scores[v.id], preset.criteria), i }))
    .sort((a, b) => b.total - a.total || a.i - b.i);
}

export const truthScores = (preset) => Object.fromEntries(preset.vendors.map((v) => [v.id, v.truth]));
export const demoScores = (preset) => Object.fromEntries(preset.vendors.map((v) => [v.id, v.demoImpression]));

/** Mean absolute difference between scores and the evidence (0 = matches the evidence). */
export function scoreError(scores, preset) {
  let d = 0;
  let n = 0;
  for (const v of preset.vendors) {
    for (const c of preset.criteria) {
      d += Math.abs(scores[v.id][c.id] - v.truth[c.id]);
      n += 1;
    }
  }
  return n ? d / n : 0;
}

/** The best and worst vendor for each proof-of-concept metric (null values are "not available"). */
export function pocBest(preset) {
  const out = {};
  for (const m of preset.pocMetrics) {
    const vals = preset.vendors.map((v) => v.poc[m.id]).filter((x) => x !== null && x !== undefined);
    if (!vals.length) continue;
    out[m.id] = m.better === 'lower' ? Math.min(...vals) : Math.max(...vals);
  }
  return out;
}

/** The debrief. */
export function evaluate(state, preset) {
  const d = state.decision;
  const vendor = preset.vendors.find((v) => v.id === d.pick) || null;
  const must = preset.terms.filter((t) => t.mustHave).map((t) => t.id);
  const missingMust = must.filter((id) => !d.terms.includes(id));
  const answers = vendor ? d.terms.map((id) => ({ term: preset.terms.find((t) => t.id === id), answer: vendor.terms[id] })) : [];
  const refused = answers.filter((a) => a.answer.reply === 'refuses');
  const rightSteps = preset.beforeSigning.filter((s) => s.right).map((s) => s.id);
  const missingSteps = rightSteps.filter((id) => !d.steps.includes(id));
  const wrongSteps = d.steps.filter((id) => !rightSteps.includes(id));
  const stages = Object.keys(STAGE_LABELS).filter((k) => state.snapshots[k]).map((k) => ({
    stage: k,
    label: STAGE_LABELS[k],
    error: scoreError(state.snapshots[k], preset),
    ranking: ranking(state.snapshots[k], preset),
  }));
  const pickRight = d.pick === preset.expert.pick;
  let verdict;
  if (pickRight && missingMust.length === 0 && missingSteps.length === 0 && wrongSteps.length === 0) verdict = 'strong';
  else if (pickRight) verdict = 'rightVendorWeakTerms';
  else if (vendor && preset.expert.acceptable && preset.expert.acceptable.includes(d.pick)) verdict = 'defensible';
  else verdict = 'demoLed';
  return {
    verdict, vendor, pickRight, missingMust, refused, answers, missingSteps, wrongSteps, stages,
    evidence: ranking(truthScores(preset), preset),
    demo: ranking(demoScores(preset), preset),
  };
}

/** Check a preset's data; returns a list of problems. */
export function validateScenario(p) {
  const problems = [];
  const crit = new Set(p.criteria.map((c) => c.id));
  for (const c of p.criteria) if (!(c.weight > 0)) problems.push(`criterion ${c.id}: weight must be positive`);
  const terms = new Set(p.terms.map((t) => t.id));
  const vids = new Set();
  for (const v of p.vendors) {
    if (vids.has(v.id)) problems.push(`vendor ${v.id} twice`);
    vids.add(v.id);
    for (const key of ['truth', 'demoImpression']) {
      for (const c of crit) {
        const x = v[key] && v[key][c];
        if (!(Number.isInteger(x) && x >= SCORE_MIN && x <= SCORE_MAX)) problems.push(`${v.id}.${key}.${c} must be 1–5`);
      }
    }
    if (!v.claims || !v.claims.length) problems.push(`${v.id}: no claims`);
    for (const cl of v.claims || []) {
      if (!cl.text || !cl.conditions || !HOLDS[cl.holds] || !cl.why) problems.push(`${v.id}/${cl.id}: claim needs text, conditions, holds and why`);
    }
    for (const m of p.pocMetrics) if (!(m.id in v.poc)) problems.push(`${v.id}: poc misses ${m.id}`);
    for (const t of terms) {
      const a = v.terms[t];
      if (!a || !['accepts', 'refuses'].includes(a.reply) || !a.note) problems.push(`${v.id}: term ${t} needs reply (accepts | refuses) and note`);
    }
    if (!v.later) problems.push(`${v.id}: missing later`);
  }
  if (!vids.has(p.expert.pick)) problems.push('expert pick is not a vendor');
  const ev = ranking(truthScores(p), p);
  if (ev[0].id !== p.expert.pick) problems.push('the evidence ranking does not put the expert pick first');
  const demo = ranking(demoScores(p), p);
  if (demo[0].id === p.expert.pick) problems.push('the demo ranking already puts the expert pick first: nothing to learn');
  const pick = p.vendors.find((v) => v.id === p.expert.pick);
  if (pick) for (const t of p.terms.filter((x) => x.mustHave)) if (pick.terms[t.id].reply !== 'accepts') problems.push(`expert pick refuses must-have term ${t.id}`);
  if (!p.beforeSigning.some((s) => s.right) || !p.beforeSigning.some((s) => !s.right)) problems.push('beforeSigning needs right and wrong steps');
  if (!p.lessonPoint) problems.push('missing lessonPoint');
  return problems;
}
