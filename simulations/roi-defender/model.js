// ROI defender: pure engine (no DOM). The sponsor's claims, the candidate adjustments on each of the
// four ledgers and the truth live in presets.js; this file nets, labels, discounts and reviews.
//
// A learner's decisions: { [claimId]: { applied: [adjustmentId], label, cls } }.
// label: measured | directional | assumed. cls: cash | capacity.
// Scenarios: low counts measured claims; expected adds directional; high adds assumed.

export const LEDGERS = {
  sponsor: { label: 'Sponsor’s team', short: 'sponsor' },
  receiving: { label: 'Receiving team', short: 'receiving' },
  control: { label: 'Control capacity (review labour)', short: 'control' },
  customer: { label: 'Customer’s share of the gain', short: 'customer' },
};

export const LABELS = {
  measured: { label: 'Measured', rank: 2, note: 'counted from data you can show' },
  directional: { label: 'Directional', rank: 1, note: 'the direction is evidenced; the size is an estimate' },
  assumed: { label: 'Assumed', rank: 0, note: 'a belief, a vendor figure or someone else’s number' },
};

export const CLASSES = {
  cash: { label: 'Cash', note: 'money that stops leaving or starts arriving, in a named budget line' },
  capacity: { label: 'Capacity', note: 'hours freed; cash only with a named plan for them' },
};

const TIERS = { low: ['measured'], expected: ['measured', 'directional'], high: ['measured', 'directional', 'assumed'] };

/** The sponsor's own decisions: nothing netted, the deck's labels. */
export function sponsorDecisions(scenario) {
  const d = {};
  for (const c of scenario.claims) d[c.id] = { applied: [], label: c.deckLabel, cls: c.deckClass };
  return d;
}

/** The decisions a careful analyst would make (the truth in the data). */
export function truthDecisions(scenario) {
  const d = {};
  for (const c of scenario.claims) {
    d[c.id] = { applied: c.adjustments.filter((a) => a.real).map((a) => a.id), label: c.truth.label, cls: c.truth.cls };
  }
  return d;
}

/** Net value of each claim (₪ a year) after the applied adjustments; an adjustment may target another claim. */
export function nets(scenario, decisions) {
  const out = {};
  for (const c of scenario.claims) out[c.id] = c.claimed;
  for (const c of scenario.claims) {
    for (const a of c.adjustments) {
      if (decisions[c.id].applied.includes(a.id)) out[a.target || c.id] += a.amount;
    }
  }
  return out;
}

/** Cash and capacity (₪ a year) in each scenario. */
export function totals(scenario, decisions) {
  const n = nets(scenario, decisions);
  const res = {};
  for (const [tier, labels] of Object.entries(TIERS)) {
    let cash = 0;
    let capacity = 0;
    for (const c of scenario.claims) {
      const d = decisions[c.id];
      if (!labels.includes(d.label)) continue;
      if (d.cls === 'cash') cash += n[c.id];
      else capacity += n[c.id];
    }
    res[tier] = { cash, capacity, hours: capacity / scenario.hourlyCost };
  }
  return { ...res, nets: n };
}

/** Net present value of a yearly cash benefit against the case's costs, at the hurdle rate. */
export function npv(annualCash, costs, rate) {
  let v = -costs.build;
  for (let t = 1; t <= costs.years; t += 1) v += (annualCash - costs.runningPerYear) / (1 + rate) ** t;
  return v;
}

/** Months to pay back the build cost from the yearly net cash (Infinity if never). */
export function paybackMonths(annualCash, costs) {
  const net = annualCash - costs.runningPerYear;
  return net > 0 ? (costs.build / net) * 12 : Infinity;
}

/** Total cost over the case's years, and who must approve it. */
export function approval(scenario) {
  const total = scenario.costs.build + scenario.costs.years * scenario.costs.runningPerYear;
  const level = scenario.approval.find((a) => total <= a.max) || scenario.approval[scenario.approval.length - 1];
  return { total, level };
}

/** The finance review of each claim. */
export function review(scenario, decisions) {
  const truth = truthDecisions(scenario);
  const rows = scenario.claims.map((c) => {
    const d = decisions[c.id];
    const t = truth[c.id];
    const findings = [];
    for (const a of c.adjustments) {
      const applied = d.applied.includes(a.id);
      if (a.real && !applied) findings.push({ kind: 'missed', a });
      if (!a.real && applied) findings.push({ kind: 'invented', a });
    }
    const lr = LABELS[d.label].rank - LABELS[t.label].rank;
    if (lr > 0) findings.push({ kind: 'overLabel' });
    if (lr < 0) findings.push({ kind: 'underLabel' });
    if (d.cls === 'cash' && t.cls === 'capacity') findings.push({ kind: 'capacityAsCash' });
    if (d.cls === 'capacity' && t.cls === 'cash') findings.push({ kind: 'cashAsCapacity' });
    const has = (k) => findings.some((f) => f.kind === k);
    let status;
    if (has('overLabel') || has('capacityAsCash')) status = 'rejected';
    else if (has('missed')) status = 'reworked';
    else if (findings.length) status = 'understated';
    else status = 'survived';
    return { claim: c, decision: d, truth: t, findings, status };
  });
  const pen = { rejected: 15, reworked: 8, understated: 4, survived: 0 };
  const credibility = Math.max(0, 100 - rows.reduce((a, r) => a + pen[r.status], 0));
  return { rows, credibility };
}

/** Everything the debrief and the status bar show. */
export function summary(scenario, decisions, approvalPick) {
  const k = scenario.costs;
  const rate = scenario.hurdleRate;
  const claimedTotal = scenario.claims.reduce((a, c) => a + c.claimed, 0);
  const mine = totals(scenario, decisions);
  const right = totals(scenario, truthDecisions(scenario));
  const appr = approval(scenario);
  const rv = review(scenario, decisions);
  return {
    claimedTotal,
    claimedNpv: npv(claimedTotal, k, rate),
    mine,
    right,
    mineNpv: npv(mine.expected.cash, k, rate),
    rightNpv: npv(right.expected.cash, k, rate),
    minePayback: paybackMonths(mine.expected.cash, k),
    rightPayback: paybackMonths(right.expected.cash, k),
    approval: appr,
    approvalRight: approvalPick ? approvalPick === appr.level.id : null,
    review: rv,
    survived: rv.rows.filter((r) => r.status === 'survived' || r.status === 'understated').length,
  };
}

/** Check a scenario's data; returns a list of problems. */
export function validateScenario(s) {
  const problems = [];
  const ids = new Set(s.claims.map((c) => c.id));
  for (const c of s.claims) {
    if (!LABELS[c.truth.label] || !LABELS[c.deckLabel]) problems.push(`${c.id}: bad label`);
    if (!CLASSES[c.truth.cls] || !CLASSES[c.deckClass]) problems.push(`${c.id}: bad class`);
    const adjIds = new Set();
    for (const a of c.adjustments) {
      if (adjIds.has(a.id)) problems.push(`${c.id}: duplicate adjustment ${a.id}`);
      adjIds.add(a.id);
      if (!LEDGERS[a.ledger]) problems.push(`${c.id}/${a.id}: unknown ledger ${a.ledger}`);
      if (a.target && !ids.has(a.target)) problems.push(`${c.id}/${a.id}: unknown target ${a.target}`);
      if (!Number.isFinite(a.amount)) problems.push(`${c.id}/${a.id}: amount`);
      if (!a.text || !a.why) problems.push(`${c.id}/${a.id}: needs text and why`);
    }
  }
  for (const l of Object.keys(LEDGERS)) {
    if (!s.claims.some((c) => c.adjustments.some((a) => a.ledger === l && a.real))) problems.push(`no real adjustment on the ${l} ledger`);
  }
  if (!(s.hurdleRate > 0) || !(s.hourlyCost > 0)) problems.push('hurdleRate and hourlyCost needed');
  if (!s.approval.some((a) => a.max === Infinity || a.max === null)) problems.push('the last approval level needs max: Infinity');
  if (!s.lessonPoint) problems.push('missing lessonPoint');
  return problems;
}
