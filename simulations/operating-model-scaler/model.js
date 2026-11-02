// Operating-model scaler: pure engine (no DOM). Units, pilots, events and money live in presets.js as
// data; this file runs the quarters. Everything is deterministic: the same design and the same answers
// give the same three years.
//
// Each quarter: road funding is updated, the quarter's event (if any) is applied, pilots are built,
// finished pilots are routed by the decision rights (central review queue, unit sign-off, hub standards,
// paved road), the review queue is worked with the quarter's slots, units that wait too long start
// shadow builds, incidents accumulate from what runs in production, and the quarter's cost is booked.

export const ARCHETYPES = {
  central: { label: 'Central CoE: a central team builds everything', short: 'central CoE' },
  federated: { label: 'Federated: each unit builds its own', short: 'federated' },
  hub: { label: 'Hub-and-spoke: the hub owns platform, standards and high-risk review; units build', short: 'hub-and-spoke' },
};
export const RIGHTS = {
  central: { label: 'Every production decision goes through the central review queue', short: 'all to the central queue' },
  unit: { label: 'Unit heads decide for their own unit', short: 'unit heads decide' },
  tiered: { label: 'By risk: high to the central queue, medium with hub standards, low on the paved road', short: 'by risk tier' },
};
export const MRM = {
  full: { label: 'Full validation for every model', short: 'full for all', effort: { low: 2, med: 2, high: 2 } },
  tiered: { label: 'Validation by risk tier', short: 'by risk tier', effort: { low: 0.5, med: 1, high: 2 } },
  light: { label: 'A light check for every model', short: 'light for all', effort: { low: 0.5, med: 0.5, high: 0.5 } },
};
export const ROADS = {
  platform: { label: 'Shared AI platform (hosting, access control, logging, monitoring)', short: 'platform' },
  templates: { label: 'Templates and an evaluation kit units must use', short: 'templates and evaluation kit' },
  catalogue: { label: 'A catalogue of every model and AI tool in use, with an owner', short: 'catalogue' },
};
export const RISKS = { low: 'low', med: 'medium', high: 'high' };
const LIVE = new Set(['building', 'queue', 'prod']);

const clone = (x) => JSON.parse(JSON.stringify(x));

export function quarterLabel(preset, q) {
  return `Q${(q % 4) + 1} ${preset.startYear + Math.floor(q / 4)}`;
}

export function eventAt(preset, q) {
  return preset.events.find((e) => e.q === q) || null;
}

export function normalizeConfig(c = {}) {
  return {
    archetype: ARCHETYPES[c.archetype] ? c.archetype : 'central',
    rights: RIGHTS[c.rights] ? c.rights : 'central',
    slots: Number.isFinite(c.slots) ? Math.max(0, Math.round(c.slots)) : 3,
    mrm: MRM[c.mrm] ? c.mrm : 'full',
    roads: { platform: Boolean(c.roads && c.roads.platform), templates: Boolean(c.roads && c.roads.templates), catalogue: Boolean(c.roads && c.roads.catalogue) },
  };
}

export function createState(preset) {
  const pilots = [];
  let n = 0;
  for (const u of preset.units) {
    for (const p of u.pilots) {
      n += 1;
      pilots.push({
        id: `p${n}`, unit: u.id, t: p.t, name: p.name, r: p.r, weak: Boolean(p.weak), dependsOn: p.dependsOn || null,
        status: 'building', progress: 0, idle: 0, waited: 0, decidedWait: null, vf: 1, validation: null, shadow: false, dup: false,
      });
    }
  }
  const shadowAcc = Object.fromEntries(preset.units.map((u) => [u.id, 0]));
  return {
    q: 0, pilots, nextId: n + 1, shadowAcc, appetiteDelta: 0,
    roadSince: { platform: null, templates: null, catalogue: null }, forced: {},
    platformPausedUntil: -1, slotMods: [], freezeUntil: -1, buildPauseUntil: -1,
    budgetCut: null, lastArchetype: null,
    incidentAcc: 0, incidents: 0, incidentLog: [], duplicates: 0, merged: 0,
    cost: 0, history: [], log: [], answers: {}, done: false,
  };
}

function funded(s, cfg, key) {
  return s.forced[key] !== undefined || cfg.roads[key];
}

export function roadReady(s, preset, key, q) {
  const since = s.forced[key] !== undefined ? s.forced[key] : s.roadSince[key];
  if (since === null || since === undefined) return false;
  if (key === 'platform' && q < s.platformPausedUntil) return false;
  return q - since >= preset.money.roads[key].lead;
}

export function effectiveSlots(s, cfg, q) {
  let x = cfg.slots;
  for (const m of s.slotMods) if (q >= m.from && q < m.until) x += m.delta;
  return Math.max(0, x);
}

export function budgetForQuarter(s, preset, q) {
  const base = preset.money.budgetPerYear / 4;
  return s.budgetCut && q >= s.budgetCut.from ? base * (1 - s.budgetCut.cut) : base;
}

const unitOf = (preset, id) => preset.units.find((u) => u.id === id);

function addPilot(s, fields) {
  const p = {
    id: `p${s.nextId}`, status: 'building', progress: 0, idle: 0, waited: 0, decidedWait: null, vf: 1, validation: null,
    shadow: false, dup: false, weak: false, dependsOn: null, ...fields,
  };
  if (p.shadow) p.everShadow = true;
  s.nextId += 1;
  s.pilots.push(p);
  return p;
}

/** Validation factor on incident risk, by how the pilot reached production. */
function validationFactor(preset, how, risk, mrm) {
  const v = preset.risk.validation;
  if (how === 'review') {
    const effort = MRM[mrm].effort[risk];
    return effort >= 2 ? v.full : effort >= 1 ? v.standard : v.light;
  }
  if (how === 'standards' || how === 'paved') return v.standards;
  return 1;
}

/** Apply one quarter. pick: the option id for this quarter's event (required when there is one). */
export function playQuarter(state, config, preset, pick) {
  if (state.done) throw new Error('The three years are over');
  const cfg = normalizeConfig(config);
  const s = clone(state);
  const q = s.q;
  const notes = [];
  let extraCost = 0;
  const m = preset.money;

  // 1. Paved roads: funding starts the lead time; stopping funding loses the progress.
  for (const key of Object.keys(ROADS)) {
    if (s.forced[key] !== undefined) continue;
    if (cfg.roads[key]) { if (s.roadSince[key] === null) s.roadSince[key] = q; } else s.roadSince[key] = null;
  }
  const reorg = s.lastArchetype !== null && s.lastArchetype !== cfg.archetype;
  if (reorg) { extraCost += m.reorg; notes.push(`Reorganisation to ${ARCHETYPES[cfg.archetype].short}: no build progress this quarter.`); }
  s.lastArchetype = cfg.archetype;

  // 2. The quarter's event.
  const toRoute = [];
  const ev = eventAt(preset, q);
  let eventResult = null;
  if (ev) {
    const opt = ev.options.find((o) => o.id === pick);
    if (!opt) throw new Error(`Choose an answer for “${ev.title}”`);
    const ready = { platform: roadReady(s, preset, 'platform', q), templates: roadReady(s, preset, 'templates', q), catalogue: roadReady(s, preset, 'catalogue', q) };
    eventResult = applyEvent(s, cfg, preset, ev, opt, q, ready, toRoute);
    extraCost += eventResult.cost;
    s.answers[ev.id] = opt.id;
  }

  const ready = { platform: roadReady(s, preset, 'platform', q), templates: roadReady(s, preset, 'templates', q), catalogue: roadReady(s, preset, 'catalogue', q) };
  const frozen = (p) => q < s.freezeUntil && p.r !== 'low';

  const toProd = (p, how) => {
    const twin = s.pilots.find((x) => x !== p && x.t === p.t && x.status === 'prod' && x.unit !== p.unit && !x.shadow);
    if (twin && (cfg.archetype === 'central' || (cfg.archetype === 'hub' && ready.catalogue))) {
      p.status = 'merged';
      s.merged += 1;
      notes.push(`${p.name} (${unitOf(preset, p.unit).name}) merged into ${unitOf(preset, twin.unit).name}’s build: the ${cfg.archetype === 'central' ? 'central team' : 'catalogue'} saw the twin.`);
      return;
    }
    if (twin) { p.dup = true; s.duplicates += 1; notes.push(`${p.name} went live in ${unitOf(preset, p.unit).name} while ${unitOf(preset, twin.unit).name} runs the same thing.`); }
    p.status = 'prod';
    p.validation = how;
    p.vf = validationFactor(preset, how, p.r, cfg.mrm);
    p.prodAt = q;
    p.decidedWait = p.waited;
  };

  const route = (p) => {
    let how;
    if (cfg.rights === 'central') how = 'queue';
    else if (cfg.rights === 'unit') how = 'unit';
    else if (p.r === 'high') how = 'queue';
    else if (p.r === 'med') how = ready.templates ? 'standards' : 'queue';
    else how = ready.platform ? 'paved' : ready.templates ? 'standards' : 'queue';
    if (how !== 'queue' && frozen(p)) how = 'queue';
    if (how === 'queue') {
      p.status = 'queue';
      p.enteredQueue = q;
      p.waited = 0;
      return;
    }
    if (ready.templates && p.weak) {
      p.status = 'stopped';
      p.stoppedBy = 'the unit’s own test with the hub’s evaluation kit';
      p.decidedWait = 0;
      return;
    }
    toProd(p, how === 'unit' ? (ready.templates ? 'standards' : null) : how);
  };

  // 3. Arrivals.
  for (const a of preset.arrivals || []) if (a.q === q) addPilot(s, { unit: a.unit, t: a.t, name: a.name, r: a.r, weak: Boolean(a.weak) });

  // 4. Build.
  const buildPaused = reorg || q < s.buildPauseUntil;
  const cap = cfg.archetype === 'central' ? preset.build.centralCapacity : Infinity;
  let used = 0;
  for (const p of s.pilots.filter((x) => x.status === 'building')) {
    if (p.dependsOn) {
      const dep = s.pilots.find((x) => x.t === p.dependsOn && !x.shadow);
      if (!dep || ['killed', 'stopped', 'stalled', 'merged'].includes(dep.status)) {
        p.status = 'stalled';
        notes.push(`${p.name} (${unitOf(preset, p.unit).name}) stalled: it depends on ${dep ? dep.name : p.dependsOn}, which is gone.`);
        continue;
      }
    }
    if (buildPaused || used >= cap) { p.idle += 1; continue; }
    used += 1;
    const u = unitOf(preset, p.unit);
    let need = cfg.archetype === 'central' ? preset.build.central : preset.build.byMaturity[u.maturity];
    if (ready.platform && p.r !== 'high') need -= preset.build.platformSaves;
    need = Math.max(1, need);
    p.progress = Math.min(need, p.progress + 1);
    if (p.progress >= need) {
      if (p.dependsOn) {
        const dep = s.pilots.find((x) => x.t === p.dependsOn && !x.shadow);
        if (dep.status !== 'prod') continue;
      }
      route(p);
    }
  }
  for (const p of toRoute) route(p);

  // 5. Review queue.
  let capacity = effectiveSlots(s, cfg, q) * (ready.templates ? preset.review.templatesFactor : 1);
  const queue = s.pilots.filter((x) => x.status === 'queue').sort((a, b) => a.enteredQueue - b.enteredQueue || Number(a.id.slice(1)) - Number(b.id.slice(1)));
  let reviewed = 0;
  for (const p of queue) {
    if (frozen(p)) continue;
    const e = MRM[cfg.mrm].effort[p.r];
    if (e > capacity + 1e-9) break;
    capacity -= e;
    reviewed += 1;
    if (p.weak && cfg.mrm !== 'light') {
      p.status = 'stopped';
      p.stoppedBy = 'central review';
      p.decidedWait = p.waited;
    } else toProd(p, 'review');
  }
  for (const p of s.pilots.filter((x) => x.status === 'queue')) p.waited += 1;

  // 6. Shadow builds from units that wait.
  const W = preset.shadow.waitQuarters;
  for (const u of preset.units) {
    // A unit with any pilot waiting W+ quarters (for review, or for the central builders) builds around the queue.
    const waits = s.pilots.some((x) => x.unit === u.id && ((x.status === 'queue' && x.waited >= W) || (cfg.archetype === 'central' && x.status === 'building' && x.idle >= W)));
    const pressure = waits ? 1 : 0;
    const appetite = Math.max(0, Math.min(1, u.appetite + s.appetiteDelta));
    s.shadowAcc[u.id] += appetite * preset.shadow.rate * pressure;
    while (s.shadowAcc[u.id] >= 1) {
      s.shadowAcc[u.id] -= 1;
      addPilot(s, { unit: u.id, t: `shadow-${u.id}-${s.nextId}`, name: `A tool ${u.name} built outside the process`, r: 'med', status: 'prod', shadow: true, prodAt: q });
      notes.push(`${u.name} put a tool into use outside the process: its pilots have waited ${W} quarters or more.`);
    }
  }

  // 7. Incidents.
  const k = preset.risk;
  let expected = 0;
  let top = null;
  for (const p of s.pilots.filter((x) => x.status === 'prod')) {
    let x = k.base[p.r] * (p.weak ? k.weakFactor : 1) * p.vf * (p.shadow ? k.shadowFactor : 1);
    if (ready.platform && !p.shadow) x *= k.platformFactor;
    expected += x;
    if (!top || x > top.x) top = { p, x };
  }
  s.incidentAcc += expected;
  while (s.incidentAcc >= 1) {
    s.incidentAcc -= 1;
    s.incidents += 1;
    const who = top.p;
    s.incidentLog.push({ q, text: `${who.name} (${unitOf(preset, who.unit).name})` });
    notes.push(`Risk incident in ${unitOf(preset, who.unit).name}: ${who.name}${who.shadow ? ' (never reviewed)' : who.weak ? ' (a weak model that reached production)' : ''}.`);
  }

  // 8. Cost.
  let roadCost = 0;
  for (const key of Object.keys(ROADS)) {
    if (!funded(s, cfg, key)) continue;
    if (key === 'platform' && q < s.platformPausedUntil) continue;
    const r = m.roads[key];
    roadCost += roadReady(s, preset, key, q) ? r.run : r.build / r.lead;
  }
  const live = s.pilots.filter((x) => x.status === 'prod' && !x.shadow);
  const runCost = live.length * (ready.platform ? m.runOnPlatform : m.runOffPlatform);
  const slots = effectiveSlots(s, cfg, q);
  const cost = m.coe[cfg.archetype] + slots * m.slotCost + roadCost + runCost + extraCost;
  s.cost += cost;

  const queueNow = s.pilots.filter((x) => x.status === 'queue');
  s.history.push({
    q, label: quarterLabel(preset, q), cfg,
    prod: live.length, queue: queueNow.length, reviewed, slots,
    shadow: s.pilots.filter((x) => x.shadow && x.status === 'prod').length,
    incidents: s.incidents, duplicates: s.duplicates, cost, cumulative: s.cost,
    budget: budgetForQuarter(s, preset, q), ready, event: ev ? { id: ev.id, title: ev.title, answer: eventResult.answer, result: eventResult.text } : null,
    notes,
  });
  s.q = q + 1;
  s.done = s.q >= preset.quarters;
  return s;
}

function applyEvent(s, cfg, preset, ev, opt, q, ready, toRoute) {
  const e = opt.effects || {};
  let text = opt.result;
  let cost = e.cost || 0;
  for (const x of ev.inject || []) addPilot(s, { unit: x.unit, t: x.t, name: x.name, r: x.r || 'med', status: 'prod', shadow: true, prodAt: q });
  if (e.appetite) s.appetiteDelta += e.appetite;
  if (e.shadow === 'kill') for (const p of s.pilots) if (p.shadow && p.status === 'prod') p.status = 'killed';
  if (e.shadow === 'adopt') {
    for (const p of s.pilots) {
      if (p.shadow && p.status === 'prod') {
        p.shadow = false;
        p.adopted = true;
        p.status = 'queue';
        p.enteredQueue = q;
        p.waited = 0;
      }
    }
  }
  if (e.merge) {
    const twins = s.pilots.filter((p) => p.t === e.merge && LIVE.has(p.status) && !p.shadow)
      .sort((a, b) => unitOf(preset, b.unit).maturity - unitOf(preset, a.unit).maturity);
    for (const p of twins.slice(1)) { p.status = 'merged'; s.merged += 1; }
  }
  if (e.killTheme) {
    for (const p of s.pilots) if (p.t === e.killTheme && LIVE.has(p.status)) p.status = 'killed';
    // Whatever was built on top of it loses its foundation, even if it is already live.
    const lost = s.pilots.filter((p) => p.dependsOn === e.killTheme && LIVE.has(p.status));
    for (const p of lost) p.status = 'stalled';
    if (lost.length) text = `${text} ${lost.length === 1 ? 'One initiative was' : `${lost.length} initiatives were`} built on it and stalled: ${lost.map((p) => `${p.name} (${unitOf(preset, p.unit).name})`).join(', ')}.`;
  }
  if (e.regulator) {
    const clean = ready.catalogue && cfg.mrm !== 'light' && cfg.rights !== 'unit';
    if (e.regulator === 'answer') {
      if (clean) text = opt.resultClean;
      else { text = opt.resultFinding; s.freezeUntil = Math.max(s.freezeUntil, q + preset.regulator.findingQuarters); }
    } else if (e.regulator === 'delay') {
      s.forced.catalogue = q + 1 - preset.money.roads.catalogue.lead;
      s.roadSince.catalogue = null;
      s.freezeUntil = Math.max(s.freezeUntil, q + 1);
    } else {
      s.freezeUntil = Math.max(s.freezeUntil, q + preset.regulator.badAnswerQuarters);
    }
  }
  if (e.keyPerson) {
    const base = ready.templates ? preset.keyPerson.documented : preset.keyPerson.undocumented;
    let share = base.share;
    if (e.keyPerson === 'contractor') share /= 2;
    if (e.keyPerson === 'second') { share = 0; s.buildPauseUntil = Math.max(s.buildPauseUntil, q + 1); }
    const delta = -Math.round(cfg.slots * share);
    if (delta) s.slotMods.push({ delta, from: q, until: q + base.quarters });
    text = `${text} ${ready.templates ? 'The validation method was written down in the templates, so the gap was smaller.' : 'Nothing about the validation method was written down, so the gap was larger.'}`;
  }
  if (e.budgetCut) s.budgetCut = { from: q + 1, cut: e.budgetCut };
  if (e.slotsCut) s.slotMods.push({ delta: -e.slotsCut, from: q + 1, until: Infinity });
  if (e.pausePlatform) s.platformPausedUntil = Math.max(s.platformPausedUntil, q + 1 + e.pausePlatform);
  if (e.drift) {
    const p = s.pilots.find((x) => x.t === preset.driftTheme && !x.shadow);
    if (!p || p.status !== 'prod') {
      text = ev.resultNotLive;
      cost = 0;
    } else if (e.drift === 'retire') p.status = 'killed';
    else if (e.drift === 'retrain') { p.vf = Math.min(p.vf, preset.risk.validation.full); p.validation = 'review'; }
    else if (p.vf > preset.risk.validation.standard) {
      s.incidents += 1;
      s.incidentLog.push({ q, text: `${p.name} (${unitOf(preset, p.unit).name}) kept running after drifting` });
      text = opt.resultBad;
    }
  }
  if (e.wave) {
    for (const x of ev.wave || []) {
      if (e.wave === 'route') toRoute.push(addPilot(s, { unit: x.unit, t: x.t, name: x.name, r: x.r, status: 'building', progress: 99 }));
      else if (e.wave === 'ignore') addPilot(s, { unit: x.unit, t: x.t, name: x.name, r: x.r, status: 'prod', shadow: true, prodAt: q });
    }
  }
  return { cost, text, answer: opt.text };
}

/** Play every remaining quarter with one design and fixed event answers. */
export function runAll(config, preset, answers) {
  let s = createState(preset);
  while (!s.done) {
    const ev = eventAt(preset, s.q);
    s = playQuarter(s, config, preset, ev ? answers[ev.id] : undefined);
  }
  return s;
}

/** Key numbers. */
export function summary(s, preset) {
  const official = s.pilots.filter((p) => !p.shadow);
  const prod = official.filter((p) => p.status === 'prod');
  const decided = official.filter((p) => p.decidedWait !== null);
  const waiting = official.filter((p) => p.status === 'queue');
  const waits = [...decided.map((p) => p.decidedWait), ...waiting.map((p) => p.waited)];
  const quarters = s.history.length;
  const budget = s.history.reduce((a, x) => a + x.budget, 0);
  return {
    quarters,
    prod: prod.length,
    total: official.length,
    stopped: official.filter((p) => p.status === 'stopped').length,
    weakInProd: prod.filter((p) => p.weak).length,
    merged: s.merged,
    stalled: official.filter((p) => p.status === 'stalled').length,
    building: official.filter((p) => p.status === 'building').length,
    backlog: waiting.length,
    avgWait: waits.length ? waits.reduce((a, b) => a + b, 0) / waits.length : 0,
    duplicates: s.duplicates,
    incidents: s.incidents,
    shadow: s.pilots.filter((p) => p.shadow && p.status === 'prod').length,
    shadowEver: s.pilots.filter((p) => p.everShadow).length,
    cost: s.cost,
    budget,
    costPerProd: prod.length ? s.cost / prod.length : Infinity,
  };
}

/** Per unit: counts by status. */
export function unitTable(s, preset) {
  return preset.units.map((u) => {
    const mine = s.pilots.filter((p) => p.unit === u.id);
    const c = (f) => mine.filter(f).length;
    return {
      unit: u,
      building: c((p) => p.status === 'building'),
      queue: c((p) => p.status === 'queue'),
      prod: c((p) => p.status === 'prod' && !p.shadow),
      shadow: c((p) => p.status === 'prod' && p.shadow),
      stopped: c((p) => p.status === 'stopped'),
      other: c((p) => ['merged', 'killed', 'stalled'].includes(p.status)),
    };
  });
}

/** Hub constants vs spoke variables, read from a design. */
export function hubSpoke(cfg, preset) {
  return preset.hubSpoke.map((item) => {
    let mine;
    if (item.road) mine = cfg.roads[item.road] ? 'hub' : 'nobody';
    else if (item.id === 'lowRisk') mine = cfg.rights === 'central' ? 'hub' : 'spoke';
    else if (item.id === 'highRisk') mine = cfg.rights === 'unit' ? 'spoke' : 'hub';
    else if (item.id === 'build' || item.id === 'adoption') mine = cfg.archetype === 'central' ? 'hub' : 'spoke';
    else mine = item.default || 'spoke';
    return { ...item, mine, match: mine === item.expert };
  });
}

/** The debrief: your run against the expert's design and two baselines. */
export function debrief(s, finalCfg, preset) {
  const mine = summary(s, preset);
  const expert = summary(runAll(preset.expert.config, preset, preset.expert.answers), preset);
  const asIs = summary(runAll(preset.startConfig, preset, preset.naiveAnswers), preset);
  const fed = summary(runAll(preset.federatedConfig, preset, preset.naiveAnswers), preset);
  const scale = mine.prod >= expert.prod * 0.8;
  const safe = mine.incidents <= expert.incidents + preset.verdict.incidentSlack && mine.shadow <= preset.verdict.maxShadow;
  const verdict = scale && safe ? 'scaled' : scale ? 'scaledUnsafe' : safe ? 'stuck' : 'neither';
  return { verdict, mine, expert, asIs, fed, hubSpoke: hubSpoke(normalizeConfig(finalCfg), preset) };
}

/** Check a preset's data; returns a list of problems. */
export function validateScenario(p) {
  const problems = [];
  const units = new Set();
  for (const u of p.units) {
    if (units.has(u.id)) problems.push(`unit ${u.id} twice`);
    units.add(u.id);
    if (!p.build.byMaturity[u.maturity]) problems.push(`${u.id}: maturity ${u.maturity} has no build time`);
    if (!(u.appetite >= 0 && u.appetite <= 1)) problems.push(`${u.id}: appetite must be 0–1`);
    for (const x of u.pilots) {
      if (!RISKS[x.r]) problems.push(`${u.id}/${x.t}: unknown risk ${x.r}`);
      if (!x.name) problems.push(`${u.id}/${x.t}: missing name`);
      if (x.dependsOn && !p.units.some((v) => v.pilots.some((y) => y.t === x.dependsOn))) problems.push(`${u.id}/${x.t}: depends on unknown ${x.dependsOn}`);
    }
  }
  for (const a of p.arrivals || []) if (!units.has(a.unit)) problems.push(`arrival ${a.t}: unknown unit`);
  const qs = new Set();
  for (const e of p.events) {
    if (qs.has(e.q)) problems.push(`two events in quarter ${e.q}`);
    qs.add(e.q);
    if (!(e.q >= 0 && e.q < p.quarters)) problems.push(`${e.id}: quarter out of range`);
    if (!e.options || e.options.length < 2) problems.push(`${e.id}: needs two options`);
    for (const o of e.options || []) {
      if (!o.text || (!o.result && !o.resultClean)) problems.push(`${e.id}/${o.id}: needs text and result`);
      const ef = o.effects || {};
      if (ef.regulator === 'answer' && (!o.resultClean || !o.resultFinding)) problems.push(`${e.id}/${o.id}: needs resultClean and resultFinding`);
      if (ef.drift === 'keep' && !o.resultBad) problems.push(`${e.id}/${o.id}: needs resultBad`);
      if (ef.drift && !e.resultNotLive) problems.push(`${e.id}: needs resultNotLive`);
      if (ef.merge && !p.units.some((u) => u.pilots.filter((x) => x.t === ef.merge).length) ) problems.push(`${e.id}/${o.id}: merge theme not found`);
    }
    for (const x of [...(e.inject || []), ...(e.wave || [])]) if (!units.has(x.unit)) problems.push(`${e.id}: unknown unit ${x.unit}`);
    for (const key of ['expert', 'naive']) {
      const ans = key === 'expert' ? p.expert.answers : p.naiveAnswers;
      if (!ans[e.id] || !e.options.some((o) => o.id === ans[e.id])) problems.push(`${key} answers miss ${e.id}`);
    }
  }
  if (p.driftTheme && !p.units.some((u) => u.pilots.some((x) => x.t === p.driftTheme))) problems.push('driftTheme not found');
  const ex = summary(runAll(p.expert.config, p, p.expert.answers), p);
  const asIs = summary(runAll(p.startConfig, p, p.naiveAnswers), p);
  const fed = summary(runAll(p.federatedConfig, p, p.naiveAnswers), p);
  if (!(ex.prod > asIs.prod)) problems.push(`expert design should put more in production than the starting design (${ex.prod} vs ${asIs.prod})`);
  if (!(ex.incidents < fed.incidents)) problems.push(`expert design should have fewer incidents than federated (${ex.incidents} vs ${fed.incidents})`);
  if (!(fed.duplicates > ex.duplicates)) problems.push('federated should have more duplicates than the expert design');
  if (!p.lessonPoint) problems.push('missing lessonPoint');
  return problems;
}
