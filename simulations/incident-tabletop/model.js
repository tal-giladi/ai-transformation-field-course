// Incident tabletop: pure engine (no DOM). The incident (injects, decisions, options, runbook) lives
// in presets.js as data; this file applies the rules.
//
// State: which injects are done, whether the AI feature is running ('all' | 'partial' | 'off'), flags,
// customers harmed, trust (customers, staff, leaders: 0–100), documentation points, cost, and when the
// harm was contained.

export const QUALITY = {
  best: { label: 'matches the runbook', tone: 'good' },
  ok: { label: 'partly', tone: 'warn' },
  poor: { label: 'differs from the runbook', tone: 'bad' },
};

const clamp = (x) => Math.max(0, Math.min(100, x));

export function createState(scenario) {
  return {
    index: 0,
    running: scenario.start.running,
    flags: [],
    harmed: scenario.start.harmed,
    newlyHarmed: 0,
    trust: { ...scenario.start.trust },
    docs: 0,
    cost: 0,
    containedAt: null,
    log: [],
    done: false,
  };
}

const cond = (c, state) => {
  if (!c) return true;
  if (c.ifFlag && !state.flags.includes(c.ifFlag)) return false;
  if (c.ifNotFlag && state.flags.includes(c.ifNotFlag)) return false;
  return true;
};

/** Is the harm still happening? The feature is fully on and the cause is not fixed. */
export function exposed(state, scenario) {
  return state.running === 'all' && !state.flags.includes(scenario.fixedFlag);
}

export function currentInject(state, scenario) {
  return state.done ? null : scenario.injects[state.index];
}

/** The decisions shown at this inject (some only appear in some states). */
export function activeDecisions(state, inject) {
  return inject.decisions.filter((d) => cond(d.when, state));
}

/** Extra lines of information that depend on earlier choices. */
export function injectInfo(state, inject) {
  return [inject.info, ...(inject.extra || []).filter((x) => cond(x, state)).map((x) => x.text)];
}

/**
 * Apply one option per active decision (picks: { decisionId: optionId }), then let time run to the next
 * inject. Returns a NEW state and the log entries.
 */
export function decide(state, scenario, picks) {
  if (state.done) throw new Error('The tabletop is over');
  const inject = currentInject(state, scenario);
  const decisions = activeDecisions(state, inject);
  let s = { ...state, trust: { ...state.trust }, flags: [...state.flags] };
  const entries = [];
  let delay = 0;
  for (const d of decisions) {
    const opt = d.options.find((o) => o.id === picks[d.id]);
    if (!opt) throw new Error(`Choose an option for ${d.id}`);
    const e = opt.effects || {};
    if (e.running) s.running = e.running;
    for (const f of e.sets || []) if (!s.flags.includes(f)) s.flags.push(f);
    for (const [k, v] of Object.entries(e.trust || {})) s.trust[k] = clamp(s.trust[k] + v);
    s.docs += e.docs || 0;
    s.cost += e.cost || 0;
    delay = Math.max(delay, e.delay ?? 0.25);
    entries.push({
      inject: inject.id, when: inject.when, decision: d.id, label: d.label, option: opt.id, text: opt.text,
      result: opt.result, quality: opt.quality, step: opt.step,
    });
  }
  // Containment: the first moment the harm stops for good.
  if (exposed(s, scenario)) s.containedAt = null;
  else if (s.containedAt === null) s.containedAt = inject.t + delay;

  // Time runs to the next inject.
  const next = scenario.injects[state.index + 1];
  let added = 0;
  if (next && exposed(s, scenario)) added = inject.exposure || 0;
  s.harmed += added;
  s.newlyHarmed += added;
  s.log = [...s.log, ...entries.map((x) => ({ ...x, harmedAfter: added }))];
  s.index = state.index + 1;
  s.done = !next;
  return { state: s, entries, added };
}

/** Scores from 0 to 100, and the raw numbers behind them. */
export function scores(state, scenario) {
  const k = scenario.scoring;
  const harm = clamp(100 - k.harmPerCustomer * state.newlyHarmed);
  const ct = state.containedAt;
  let contain = 0;
  if (ct !== null) {
    const band = k.containBands.find((b) => ct <= b.hours);
    contain = band ? band.score : 0;
  }
  const trustVals = Object.values(state.trust);
  const trust = Math.round(trustVals.reduce((a, b) => a + b, 0) / trustVals.length);
  const docsMax = maxDocs(scenario);
  const docs = Math.round(clamp((state.docs / docsMax) * 100));
  return { harm, contain, trust, docs, containedAt: ct, docsMax, overall: Math.round((harm + contain + trust + docs) / 4) };
}

/** Best possible documentation points (decisions that always appear). */
export function maxDocs(scenario) {
  let m = 0;
  for (const inj of scenario.injects) {
    for (const d of inj.decisions) {
      if (d.when) continue;
      m += Math.max(0, ...d.options.map((o) => (o.effects && o.effects.docs) || 0));
    }
  }
  return m || 1;
}

/** The runbook, step by step, with what the learner did at each step. */
export function runbookComparison(state, scenario) {
  return scenario.runbook.map((step) => {
    const did = state.log.filter((e) => e.step === step.id);
    let status;
    if (!did.length) status = 'skipped';
    else if (did.every((e) => e.quality === 'best')) status = 'best';
    else if (did.some((e) => e.quality === 'poor')) status = 'poor';
    else status = 'ok';
    return { ...step, did, status };
  });
}

export function debrief(state, scenario) {
  const sc = scores(state, scenario);
  const rb = runbookComparison(state, scenario);
  const notes = scenario.flagNotes.filter((n) => state.flags.includes(n.flag));
  let verdict;
  if (sc.overall >= 80) verdict = 'strong';
  else if (sc.overall >= 55) verdict = 'mixed';
  else verdict = 'weak';
  return { scores: sc, runbook: rb, notes, verdict, harmedTotal: state.harmed, newlyHarmed: state.newlyHarmed, cost: state.cost };
}

/** Check a scenario's data; returns a list of problems. */
export function validateScenario(s) {
  const problems = [];
  const steps = new Set(s.runbook.map((r) => r.id));
  const sets = new Set();
  const used = new Set([s.fixedFlag]);
  let lastT = -1;
  for (const inj of s.injects) {
    if (!(inj.t > lastT)) problems.push(`${inj.id}: times must increase`);
    lastT = inj.t;
    for (const x of inj.extra || []) { if (x.ifFlag) used.add(x.ifFlag); if (x.ifNotFlag) used.add(x.ifNotFlag); }
    for (const d of inj.decisions) {
      if (d.when) { if (d.when.ifFlag) used.add(d.when.ifFlag); if (d.when.ifNotFlag) used.add(d.when.ifNotFlag); }
      if (d.options.length < 2) problems.push(`${inj.id}/${d.id}: needs at least two options`);
      if (!d.options.some((o) => o.quality === 'best')) problems.push(`${inj.id}/${d.id}: no best option`);
      for (const o of d.options) {
        if (!steps.has(o.step)) problems.push(`${inj.id}/${d.id}/${o.id}: unknown runbook step ${o.step}`);
        if (!QUALITY[o.quality]) problems.push(`${inj.id}/${d.id}/${o.id}: unknown quality ${o.quality}`);
        if (!o.text || !o.result) problems.push(`${inj.id}/${d.id}/${o.id}: needs text and result`);
        for (const f of (o.effects && o.effects.sets) || []) sets.add(f);
      }
    }
  }
  for (const f of s.flagNotes.map((n) => n.flag)) used.add(f);
  for (const f of used) if (!sets.has(f)) problems.push(`flag "${f}" is used but never set`);
  for (const st of steps) {
    if (!s.injects.some((i) => i.decisions.some((d) => d.options.some((o) => o.step === st && o.quality === 'best')))) {
      problems.push(`runbook step ${st} has no best option anywhere`);
    }
  }
  if (!s.lessonPoint) problems.push('missing lessonPoint');
  return problems;
}
