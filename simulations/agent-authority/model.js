// Agent authority: pure engine (no DOM). The organization, its tools, the scripted days and the
// must-refuse probes live in presets.js as data; this file applies the rules.
//
// A configuration gives each tool a rung on the authority ladder (not granted / one approver / two
// approvers / executes alone) and limits (amount caps, daily totals, per-customer rate, customer
// tiers, verification, address on file, soft delete), plus global controls: logging, the agent's own
// identity, a kill switch, a prompt rule and change control on knowledge sources.
//
// Each day, routine requests arrive evenly between 08:00 and 18:00 and scripted events arrive at their
// hour. For every request the agent tries one action; the checks below decide whether it happens.
// Requests the agent should complete and does not are handed to people through a ticket (or dropped
// when the agent cannot open tickets). Actions it should not take and does take are harm: money,
// records and trust, each with a recoverability window. Whether harm is recovered depends on when it
// is detected, which depends on logging.

export const RUNGS = {
  off: { label: 'Not granted (never delegate)', short: 'not granted', ladder: 'never delegate', approvals: 0 },
  approve: { label: 'Recommend: one person approves each action', short: 'one approver', ladder: 'recommend', approvals: 1 },
  two: { label: 'Recommend: two people approve (two-person rule)', short: 'two approvers', ladder: 'recommend', approvals: 2 },
  auto: { label: 'Execute alone within the limits', short: 'executes alone', ladder: 'execute', approvals: 0 },
};
export const RUNG_ORDER = ['off', 'approve', 'two', 'auto'];

export const LOGGING = {
  none: { label: 'No agent log (only what the product records anyway)', short: 'no agent log' },
  actions: { label: 'Log actions (tool, customer, amount); read in the weekly report', short: 'actions only' },
  full: { label: 'Full trace (message, documents read, tool calls, approvals) and a daily 20-minute review', short: 'full trace + daily review' },
};
export const LOGGING_ORDER = ['none', 'actions', 'full'];

export const BANDS = {
  easy: 'easy to reverse',
  bounded: 'reversible within a window',
  difficult: 'hard to reverse',
  none: 'cannot be undone',
};

export const LIMIT_KINDS = {
  cap: { label: 'Most per action', type: 'amount' },
  dailyTotal: { label: 'Most in total per day', type: 'amount' },
  perCustomerDay: { label: 'Most actions per customer per day', type: 'count' },
  tiers: { label: 'Customer tiers it may act for', type: 'tiers' },
  verify: { label: 'Only after verification on a channel already on file', type: 'flag' },
  ownAddressOnly: { label: 'Only to the address already on the account', type: 'flag' },
  softDelete: { label: 'Deletes are soft (recoverable for a while)', type: 'flag' },
};

export const RIGHTS = {
  do: 'the agent should complete it',
  handoff: 'a person should handle it',
  refuse: 'the agent must refuse',
};

const toolById = (preset, id) => preset.tools.find((t) => t.id === id);
const hasLimit = (tool, kind) => (tool.limits || []).some((l) => l.kind === kind);

/** A full configuration from a partial one: every tool, every limit, every global control. */
export function normalizeConfig(preset, partial = {}) {
  const tools = {};
  for (const t of preset.tools) {
    const p = (partial.tools && partial.tools[t.id]) || {};
    const c = { rung: RUNGS[p.rung] ? p.rung : 'off' };
    for (const l of t.limits || []) {
      const kind = LIMIT_KINDS[l.kind];
      if (kind.type === 'tiers') c.tiers = Array.isArray(p.tiers) ? preset.tiers.map((x) => x.id).filter((x) => p.tiers.includes(x)) : preset.tiers.map((x) => x.id);
      else if (kind.type === 'flag') c[l.kind] = Boolean(p[l.kind]);
      else c[l.kind] = p[l.kind] === undefined ? null : p[l.kind];
    }
    tools[t.id] = c;
  }
  return {
    tools,
    logging: LOGGING[partial.logging] ? partial.logging : 'actions',
    ownIdentity: Boolean(partial.ownIdentity),
    killSwitch: Boolean(partial.killSwitch),
    promptRule: Boolean(partial.promptRule),
    sourceControl: Boolean(partial.sourceControl),
  };
}

export const cloneConfig = (c) => JSON.parse(JSON.stringify(c));

/**
 * Would the agent take this action? ctx: { approvalsUsed, capacity, totalToday(toolId), countToday(toolId, customer) }
 * (omit ctx for an unloaded check). Returns { status, by, approvals, rubber }.
 * status: notGranted | blocked | promptRefused | caught | done.
 */
export function check(action, cfg, preset, ctx = null) {
  const tool = toolById(preset, action.tool);
  const tc = cfg.tools[action.tool];
  if (!tool || !tc || tc.rung === 'off') return { status: 'notGranted', by: `${tool ? tool.label : action.tool} is not granted`, approvals: 0 };
  for (const need of tool.needs || []) {
    if (cfg.tools[need].rung === 'off') return { status: 'notGranted', by: `${toolById(preset, need).label} is not granted, so it cannot see the account`, approvals: 0 };
  }
  if (action.sourceStoppable && cfg.sourceControl) {
    return { status: 'blocked', by: 'change control on knowledge sources: the replaced article never went live', approvals: 0 };
  }
  if (hasLimit(tool, 'tiers') && action.tier && !tc.tiers.includes(action.tier)) {
    const tier = preset.tiers.find((x) => x.id === action.tier);
    return { status: 'blocked', by: `the tier limit (${tier ? tier.label : action.tier} customers go to a person)`, approvals: 0 };
  }
  const amount = action.amount || 0;
  if (hasLimit(tool, 'cap') && tc.cap !== null && amount > tc.cap) return { status: 'blocked', by: `the cap of ${preset.currency}${tc.cap.toLocaleString('en-US')} per action`, approvals: 0 };
  if (hasLimit(tool, 'dailyTotal') && tc.dailyTotal !== null && ctx && ctx.totalToday(action.tool) + amount > tc.dailyTotal) {
    return { status: 'blocked', by: `the daily total of ${preset.currency}${tc.dailyTotal.toLocaleString('en-US')}`, approvals: 0 };
  }
  if (hasLimit(tool, 'perCustomerDay') && tc.perCustomerDay !== null && ctx && ctx.countToday(action.tool, action.customer) >= tc.perCustomerDay) {
    return { status: 'blocked', by: `the limit of ${tc.perCustomerDay} per customer per day`, approvals: 0 };
  }
  if (hasLimit(tool, 'verify') && tc.verify && !action.verified) return { status: 'blocked', by: 'the verification rule', approvals: 0 };
  if (hasLimit(tool, 'ownAddressOnly') && tc.ownAddressOnly && action.toOther) return { status: 'blocked', by: 'the address-on-file rule', approvals: 0 };
  if (action.injection && cfg.promptRule && action.promptRuleStops) {
    return { status: 'promptRefused', by: 'the prompt rule (this time: the injection was crude)', approvals: 0 };
  }
  const need = RUNGS[tc.rung].approvals;
  if (need) {
    const rubber = Boolean(ctx && ctx.capacity !== undefined && ctx.approvalsUsed + need > ctx.capacity);
    const catches = action.catchAt === 'approve' || (action.catchAt === 'two' && tc.rung === 'two');
    if (!rubber && catches) return { status: 'caught', by: tc.rung === 'two' && action.catchAt === 'two' ? 'the second approver' : 'the approver', approvals: need, rubber };
    return { status: 'done', by: rubber ? 'approved without a real check (the approvers were over capacity)' : 'approved', approvals: need, rubber };
  }
  return { status: 'done', by: 'executed alone', approvals: 0, rubber: false };
}

/** When would this harm be detected (hours since the start of day 1)? */
export function detectAt(abs, logging, preset, harm) {
  const d = preset.detection;
  let t;
  if (logging === 'full') {
    t = Math.floor(abs / 24) * 24 + d.reviewHour;
    if (abs >= t) t += 24;
  } else if (logging === 'actions') {
    t = d.weeklyReportAt;
    while (abs >= t) t += 168;
  } else {
    t = abs + d.noneHours;
  }
  if (harm && harm.complaintAfter !== undefined && harm.complaintAfter !== null) t = Math.min(t, abs + harm.complaintAfter);
  return t;
}

const WEEKDAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

/** Hours since the start of day 1 (a Sunday) → "Monday 14:30", "Sunday 09:00 a week later". */
export function clock(abs, preset) {
  const day = Math.floor(abs / 24);
  const hrs = abs - day * 24;
  const hh = Math.floor(hrs);
  const mm = Math.round((hrs - hh) * 60);
  const time = `${String(hh).padStart(2, '0')}:${String(mm).padStart(2, '0')}`;
  if (day < preset.days.length) return `${preset.days[day].label} ${time}`;
  if (day < 7) return `${WEEKDAYS[day]} ${time}`;
  const weeks = Math.floor(day / 7);
  return `${WEEKDAYS[day % 7]} ${time} (${weeks === 1 ? 'a week later' : `${weeks} weeks later`})`;
}

function emptyTotals() {
  return {
    shouldDo: 0, resolvedAlone: 0, resolvedApproved: 0, missedHandedOff: 0, missedDropped: 0,
    shouldHandoff: 0, handoffOk: 0, handoffDropped: 0,
    mustRefuse: 0, refused: 0,
    harms: 0, money: 0, moneyRecovered: 0, records: 0, recordsRecovered: 0, trust: 0,
    approvals: 0, rubber: 0, minutes: 0, auditRequired: 0, auditRecorded: 0,
  };
}

export function createRun(preset) {
  return { day: 0, totals: emptyTotals(), dayResults: [], harms: [], causeStops: {}, configs: [], done: false };
}

/** The day's requests in time order: routine units spread evenly from 08:00 to 18:00, then scripted events. */
function dayItems(preset, dayIndex) {
  const items = [];
  for (const g of preset.routine) {
    for (let i = 0; i < g.count; i += 1) {
      items.push({
        kind: 'routine', group: g.id, hour: 8 + (10 * (i + 0.5)) / g.count,
        action: { tool: g.tool, amount: g.amount || 0, tier: g.tier, verified: g.verified, customer: `${g.id}-${dayIndex}-${i}` },
        right: 'do', units: 1,
      });
    }
  }
  for (const e of preset.events.filter((x) => x.day === dayIndex + 1)) {
    items.push({ kind: 'event', event: e, hour: e.hour, action: { ...e.action, customer: e.customer.id }, right: e.right, units: e.count || 1 });
  }
  return items.sort((a, b) => a.hour - b.hour || (a.kind === 'event' ? 1 : -1));
}

function auditFields(cfg, approvals) {
  const logged = cfg.logging !== 'none';
  const req = 3 + (approvals ? 1 : 0);
  let rec = 0;
  if (logged && cfg.ownIdentity) rec += 1; // who acted
  if (logged) rec += 1; // what it did
  if (cfg.logging === 'full') rec += 1; // why: the message and documents it read
  if (approvals && logged) rec += 1; // who approved
  return { req, rec };
}

/** Run one day with this configuration. Returns a NEW run state. */
export function runDay(run, config, preset) {
  if (run.done) throw new Error('The run is over');
  const cfg = cloneConfig(config);
  const dayIndex = run.day;
  const base = dayIndex * 24;
  const t = { ...run.totals };
  const harms = [...run.harms];
  const causeStops = { ...run.causeStops };
  const k = preset.costs;
  const amounts = {};
  const counts = {};
  let approvalsUsed = 0;
  const routine = {};
  const events = [];
  const ctx = {
    capacity: preset.approvalCapacity,
    get approvalsUsed() { return approvalsUsed; },
    totalToday: (tool) => amounts[tool] || 0,
    countToday: (tool, customer) => counts[`${tool}|${customer}`] || 0,
  };

  const ticket = () => {
    const r = check({ tool: preset.ticketTool, tier: null, customer: 'ticket' }, cfg, preset, ctx);
    if (r.status === 'done') {
      approvalsUsed += r.approvals; t.approvals += r.approvals;
      return true;
    }
    return false;
  };

  for (const item of dayItems(preset, dayIndex)) {
    const abs = base + item.hour;
    const ev = item.event;
    const outcomes = [];
    for (let u = 0; u < item.units; u += 1) {
      const a = item.action;
      let r;
      const stop = ev && ev.cause ? causeStops[ev.cause] : undefined;
      if (stop !== undefined && stop <= abs) {
        r = { status: 'blocked', by: 'the cause had already been found and stopped', approvals: 0 };
      } else {
        r = check(a, cfg, preset, ctx);
      }
      if (r.approvals) {
        approvalsUsed += r.approvals;
        t.approvals += r.approvals;
        if (r.rubber) t.rubber += 1;
        t.minutes += r.rubber ? r.approvals * k.rubberMinutes : r.approvals * k.approvalMinutes;
      }
      const audit = auditFields(cfg, r.approvals);
      t.auditRequired += audit.req;
      t.auditRecorded += audit.rec;
      let result;
      if (r.status === 'done') {
        amounts[a.tool] = (amounts[a.tool] || 0) + (a.amount || 0);
        counts[`${a.tool}|${a.customer}`] = (counts[`${a.tool}|${a.customer}`] || 0) + 1;
      }
      if (item.right === 'do') {
        t.shouldDo += 1;
        if (r.status === 'done') {
          if (r.approvals) t.resolvedApproved += 1; else t.resolvedAlone += 1;
          result = r.approvals ? 'resolvedApproved' : 'resolvedAlone';
        } else if (ticket()) {
          t.missedHandedOff += 1; t.minutes += k.handoffMinutes; result = 'handedOff';
        } else {
          t.missedDropped += 1; t.trust += k.droppedTrust; result = 'dropped';
        }
      } else if (r.status !== 'done') {
        if (item.right === 'handoff') {
          t.shouldHandoff += 1;
          if (ticket()) { t.handoffOk += 1; t.minutes += k.handoffMinutes; result = 'handedOff'; } else { t.handoffDropped += 1; t.trust += k.droppedTrust; result = 'dropped'; }
        } else {
          t.mustRefuse += 1; t.refused += 1; result = 'refused';
        }
      } else {
        if (item.right === 'handoff') t.shouldHandoff += 1; else t.mustRefuse += 1;
        result = 'harm';
        const hm = ev.harm;
        const tool = toolById(preset, a.tool);
        const soft = a.tool === preset.deleteTool && cfg.tools[a.tool] && cfg.tools[a.tool].softDelete;
        let until;
        if (soft) until = abs + preset.softDeleteHours;
        else if (hm.window.untilAbs !== undefined) until = hm.window.untilAbs;
        else until = abs + hm.window.hours;
        const detected = detectAt(abs, cfg.logging, preset, hm);
        const recovered = detected <= until;
        const money = hm.money || 0;
        const records = hm.records || 0;
        t.harms += 1;
        t.money += money; t.records += records;
        if (recovered) { t.moneyRecovered += money; t.recordsRecovered += records; }
        t.trust += recovered ? (hm.trust || 0) / 2 : (hm.trust || 0);
        harms.push({
          event: ev.id, title: ev.title, at: abs, tool: tool.label, money, records, trust: hm.trust || 0,
          band: soft ? 'bounded' : hm.band, text: hm.text, lastReversible: soft ? `Within ${Math.round(preset.softDeleteHours / 24)} days, while the soft delete can be undone` : hm.lastReversible,
          until, detected, recovered, how: r.by,
        });
        if (ev.cause) {
          const stopAt = detected + (cfg.killSwitch ? preset.killSwitchHours : preset.noKillSwitchHours);
          causeStops[ev.cause] = Math.min(causeStops[ev.cause] ?? Infinity, stopAt);
        }
      }
      outcomes.push({ result, by: r.by, rubber: Boolean(r.rubber) });
    }
    if (item.kind === 'routine') {
      const g = routine[item.group] || (routine[item.group] = { resolvedAlone: 0, resolvedApproved: 0, handedOff: 0, dropped: 0, by: {} });
      for (const o of outcomes) {
        g[o.result] += 1;
        if (o.result === 'handedOff' || o.result === 'dropped') g.by[o.by] = (g.by[o.by] || 0) + 1;
      }
    } else {
      const summary = {};
      for (const o of outcomes) summary[o.result] = (summary[o.result] || 0) + 1;
      events.push({ event: ev, at: abs, outcomes, summary, by: [...new Set(outcomes.map((o) => o.by))], rubber: outcomes.some((o) => o.rubber) });
    }
  }
  if (cfg.logging === 'full') t.minutes += k.reviewMinutes;
  const dayResult = { day: dayIndex, label: preset.days[dayIndex].label, approvalsUsed, capacity: preset.approvalCapacity, routine, events };
  const next = dayIndex + 1;
  return {
    day: next,
    totals: t,
    dayResults: [...run.dayResults, dayResult],
    harms,
    causeStops,
    configs: [...run.configs, cfg],
    done: next >= preset.days.length,
  };
}

/** Run every day with one configuration. */
export function runAll(config, preset) {
  let run = createRun(preset);
  while (!run.done) run = runDay(run, config, preset);
  return run;
}

/** Key numbers of a run. */
export function summary(run) {
  const t = run.totals;
  const moneyLost = t.money - t.moneyRecovered;
  const recordsLost = t.records - t.recordsRecovered;
  return {
    resolvedShare: t.shouldDo ? (t.resolvedAlone + t.resolvedApproved) / t.shouldDo : 0,
    resolved: t.resolvedAlone + t.resolvedApproved,
    shouldDo: t.shouldDo,
    handedOff: t.missedHandedOff + t.handoffOk,
    dropped: t.missedDropped + t.handoffDropped,
    moneyLost, moneyRecovered: t.moneyRecovered, money: t.money,
    recordsLost, recordsRecovered: t.recordsRecovered, records: t.records,
    trustLost: Math.round(t.trust * 10) / 10,
    harms: t.harms,
    unrecovered: run.harms.filter((x) => !x.recovered).length,
    audit: t.auditRequired ? t.auditRecorded / t.auditRequired : 0,
    approvals: t.approvals, rubber: t.rubber,
    minutes: t.minutes,
    refused: t.refused, mustRefuse: t.mustRefuse,
  };
}

/**
 * Run each must-refuse probe once against a configuration (an approver with time; no load).
 * A probe's `prior: { count, total }` says what that customer and tool already did today.
 */
export function negativeTests(config, preset) {
  return preset.probes.map((p) => {
    const prior = p.prior || {};
    const ctx = { approvalsUsed: 0, totalToday: () => prior.total || 0, countToday: () => prior.count || 0 };
    const r = check({ ...p.action, customer: `probe-${p.id}` }, config, preset, ctx);
    return { id: p.id, text: p.text, refused: r.status !== 'done', by: r.by, status: r.status };
  });
}

/** How many settings differ between two configurations (for "you changed it after day N"). */
export function configChanges(a, b) {
  let n = 0;
  for (const key of ['logging', 'ownIdentity', 'killSwitch', 'promptRule', 'sourceControl']) if (a[key] !== b[key]) n += 1;
  for (const id of Object.keys(a.tools)) {
    if (JSON.stringify(a.tools[id]) !== JSON.stringify(b.tools[id])) n += 1;
  }
  return n;
}

/** The debrief: verdict, the expert's run on the same days, the ladder per tool and the harm table. */
export function debrief(run, preset) {
  const mine = summary(run);
  const expertRun = runAll(normalizeConfig(preset, preset.expert.config), preset);
  const expert = summary(expertRun);
  const startRun = runAll(normalizeConfig(preset, preset.startConfig), preset);
  const start = summary(startRun);
  const safe = mine.unrecovered === 0 && mine.moneyLost <= preset.verdict.maxMoneyLost;
  const useful = mine.resolvedShare >= expert.resolvedShare - preset.verdict.resolvedSlack;
  let verdict;
  if (safe && useful) verdict = 'safeUseful';
  else if (safe) verdict = 'safeNotUseful';
  else if (useful) verdict = 'usefulNotSafe';
  else verdict = 'neither';
  const finalCfg = run.configs[run.configs.length - 1];
  const ladder = preset.tools.map((tool) => ({
    tool, mine: finalCfg.tools[tool.id].rung, expert: preset.expert.config.tools[tool.id].rung, why: tool.expertWhy,
  }));
  let changedAfter = 0;
  for (let i = 1; i < run.configs.length; i += 1) if (configChanges(run.configs[i - 1], run.configs[i])) changedAfter += 1;
  return { verdict, mine, expert, start, ladder, harms: run.harms, negative: negativeTests(finalCfg, preset), changedAfter, finalCfg };
}

/** Check a preset's data; returns a list of problems. */
export function validateScenario(p) {
  const problems = [];
  const ids = new Set();
  for (const t of p.tools) {
    if (ids.has(t.id)) problems.push(`tool ${t.id} twice`);
    ids.add(t.id);
    for (const l of t.limits || []) {
      if (!LIMIT_KINDS[l.kind]) problems.push(`${t.id}: unknown limit ${l.kind}`);
      const type = LIMIT_KINDS[l.kind] && LIMIT_KINDS[l.kind].type;
      if ((type === 'amount' || type === 'count') && !(Array.isArray(l.options) && l.options.includes(null))) problems.push(`${t.id}/${l.kind}: options must include null (no limit)`);
    }
    if (!BANDS[t.band]) problems.push(`${t.id}: unknown band ${t.band}`);
    for (const n of t.needs || []) if (!p.tools.some((x) => x.id === n)) problems.push(`${t.id}: needs unknown tool ${n}`);
    if (!t.expertWhy) problems.push(`${t.id}: missing expertWhy`);
  }
  for (const key of ['ticketTool', 'deleteTool']) if (!ids.has(p[key])) problems.push(`${key} ${p[key]} is not a tool`);
  const tiers = new Set((p.tiers || []).map((x) => x.id));
  const checkAction = (where, a) => {
    if (!ids.has(a.tool)) problems.push(`${where}: unknown tool ${a.tool}`);
    if (a.tier && !tiers.has(a.tier)) problems.push(`${where}: unknown tier ${a.tier}`);
    if (a.catchAt && !['approve', 'two'].includes(a.catchAt)) problems.push(`${where}: catchAt must be approve or two`);
  };
  for (const g of p.routine) checkAction(`routine ${g.id}`, g);
  const evIds = new Set();
  for (const e of p.events) {
    if (evIds.has(e.id)) problems.push(`event ${e.id} twice`);
    evIds.add(e.id);
    if (!(e.day >= 1 && e.day <= p.days.length)) problems.push(`${e.id}: day out of range`);
    if (!(e.hour >= 0 && e.hour < 24)) problems.push(`${e.id}: hour out of range`);
    if (!RIGHTS[e.right]) problems.push(`${e.id}: unknown right ${e.right}`);
    checkAction(e.id, e.action);
    if (e.right !== 'do') {
      const hm = e.harm;
      if (!hm || !hm.text || !hm.lastReversible || !BANDS[hm.band] || !hm.window) problems.push(`${e.id}: harm needs text, lastReversible, band and window`);
    }
    if (!e.title || !e.says || !e.customer || !e.customer.name) problems.push(`${e.id}: needs title, says and customer`);
  }
  for (const pr of p.probes) checkAction(`probe ${pr.id}`, pr.action);
  for (const cfgKey of ['startConfig']) {
    for (const id of Object.keys(p[cfgKey].tools || {})) if (!ids.has(id)) problems.push(`${cfgKey}: unknown tool ${id}`);
  }
  for (const id of ids) if (!p.expert.config.tools[id]) problems.push(`expert config misses tool ${id}`);
  const ex = normalizeConfig(p, p.expert.config);
  const failing = negativeTests(ex, p).filter((x) => !x.refused);
  if (failing.length) problems.push(`expert config fails probes: ${failing.map((x) => x.id).join(', ')}`);
  const exRun = summary(runAll(ex, p));
  if (exRun.unrecovered) problems.push(`expert config leaves ${exRun.unrecovered} unrecovered harms`);
  if (!p.lessonPoint) problems.push('missing lessonPoint');
  return problems;
}
