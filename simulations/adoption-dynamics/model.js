// Adoption dynamics: pure model (no DOM). One simulated person per team member, 26 weeks, seeded
// randomness so the same plan and seed always give the same run.

import { makeRng } from '../common/random.js';
import { clamp } from '../common/math.js';

export const WEEKS = 26;

/** Constants of the model (shown in "About this model"). */
export const K = {
  tryChampions: 0.08,       // extra weekly chance to try the tool while champions are active
  tryTraining: { none: 0, generic: 0.35, role: 0.5 }, // one-off chance in the training week
  tryForced: 0.6,           // weekly chance to try while a mandate or "old path removed" is active
  skillTraining: { none: 0, generic: 0.08, role: 0.3 },
  skillChampions: 0.1,
  skillOfficeHoursPerWeek: 0.02,
  skillOfficeHoursMax: 0.15,
  skillRedesign: 0.25,
  habitStart: 0.7,
  habitUp: 0.12,
  habitDown: 0.12,
  habitIdle: 0.05,
  skillMax: 0.85,
  forcedActivity: 0.9,      // chance a person logs some use in a week under a mandate or with the old path gone
  mandateQualityFactor: 0.4, // use done to satisfy a mandate is rarely on the tasks that matter
  noOldPathQualityFactor: 0.8, // forced onto the tool without the skill: the work gets done, often badly
  stopAfterWeeksWithoutValue: 4,
  returnAlone: 0.02,        // weekly chance a stopped person tries again with no help
  returnWithSupport: 0.05,  // extra weekly chance while champions or office hours run
  returnOnRedesign: 0.3,    // one-off chance to come back in the week the workflow is redesigned
};

/** A plan: { training: 'none'|'generic'|'role', trainingWeek, champions, officeHours, redesign, mandate, removeOldPath } (weeks; 0 = off). */
export const EMPTY_PLAN = { training: 'none', trainingWeek: 0, champions: 0, officeHours: 0, redesign: 0, mandate: 0, removeOldPath: 0 };

const on = (startWeek, w) => startWeek > 0 && w >= startWeek;

function makeTeam(preset, rng) {
  const n = preset.teamSize;
  const withOpportunity = Math.round(n * preset.opportunityShare);
  const order = rng.shuffle([...Array(n).keys()]);
  const team = [];
  for (let i = 0; i < n; i += 1) {
    team.push({
      id: i,
      name: preset.names[i % preset.names.length] + (i >= preset.names.length ? ` ${Math.floor(i / preset.names.length) + 1}` : ''),
      propensity: rng.range(0.05, 0.3),
      baseSkill: rng.range(0.15, 0.5),
      hasOpportunity: order.indexOf(i) < withOpportunity,
      oldWay: rng.pick(preset.oldWays),
      tried: false,
      triedWeek: 0,
      habit: 0,
      status: 'never', // never | using | stopped
      noValueStreak: 0,
      stoppedWeek: 0,
      everStopped: false,
      returnedWeek: 0,
      lastActive: false,
      lastQualified: false,
      qualifiedWeeks: 0,
      activeWeeks: 0,
    });
  }
  return team;
}

function skillOf(person, plan, w) {
  let skill = person.baseSkill;
  if (on(plan.trainingWeek, w)) skill += K.skillTraining[plan.training] || 0;
  if (on(plan.champions, w)) skill += K.skillChampions;
  if (on(plan.officeHours, w)) skill += Math.min(K.skillOfficeHoursMax, K.skillOfficeHoursPerWeek * (w - plan.officeHours + 1));
  if (on(plan.redesign, w)) skill += K.skillRedesign;
  return clamp(skill, 0, K.skillMax);
}

/**
 * Run 26 weeks. preset: { teamSize, opportunityShare, names, oldWays, usesPerWeek, minutesPerUse, seed }.
 * Returns { weeks: [...], people: [...final state], summary }.
 */
export function simulate(preset, plan, seed = preset.seed) {
  const rng = makeRng(seed);
  const team = makeTeam(preset, rng);
  const oppPop = team.filter((p) => p.hasOpportunity).length;
  const weeks = [];

  for (let w = 1; w <= WEEKS; w += 1) {
    const mandate = on(plan.mandate, w);
    const noOldPath = on(plan.removeOldPath, w);
    const support = on(plan.champions, w) || on(plan.officeHours, w);
    let active = 0;
    let qualified = 0;
    let forced = 0;

    for (const p of team) {
      const skill = skillOf(p, plan, w);

      // 1. First try.
      if (!p.tried) {
        let tryP = p.propensity;
        if (on(plan.champions, w)) tryP += K.tryChampions;
        if (plan.trainingWeek === w) tryP += K.tryTraining[plan.training] || 0;
        if (mandate || noOldPath) tryP += K.tryForced;
        if (rng.chance(clamp(tryP, 0, 0.95))) {
          p.tried = true;
          p.triedWeek = w;
          p.habit = K.habitStart;
          p.status = 'using';
        }
      }

      // 2. People who stopped may come back.
      if (p.status === 'stopped') {
        let back = K.returnAlone;
        if (support) back += K.returnWithSupport;
        if (plan.redesign === w) back += K.returnOnRedesign;
        if (noOldPath) back = 1; // there is nothing to go back to
        if (back > 0 && rng.chance(back)) {
          p.status = 'using';
          p.habit = 0.6;
          p.noValueStreak = 0;
          p.returnedWeek = w;
        }
      }

      // 3. Activity this week.
      // A mandate or a removed old path forces some activity, whether or not it helps.
      let isActive = false;
      let byForce = false;
      if (p.status === 'using') {
        isActive = rng.chance(p.habit);
        if (!isActive && (mandate || noOldPath) && rng.chance(K.forcedActivity)) { isActive = true; byForce = true; }
      } else if (p.status === 'stopped' && mandate) {
        isActive = rng.chance(K.forcedActivity);
        byForce = isActive;
      }

      // 4. Qualified use: on the tasks that matter, done properly.
      let isQualified = false;
      if (isActive && p.hasOpportunity) {
        const factor = !byForce ? 1 : noOldPath ? K.noOldPathQualityFactor : K.mandateQualityFactor;
        isQualified = rng.chance(skill * factor);
      }

      // 5. Habit and quiet stopping.
      if (p.status === 'using') {
        if (isQualified) {
          p.habit = Math.min(0.97, p.habit + K.habitUp);
          p.noValueStreak = 0;
        } else {
          p.habit = Math.max(0.05, p.habit - (isActive ? K.habitDown : K.habitIdle));
          p.noValueStreak += 1;
        }
        if (p.noValueStreak >= K.stopAfterWeeksWithoutValue && w >= 3 && !noOldPath) {
          p.status = 'stopped';
          if (!p.everStopped) p.stoppedWeek = w;
          p.everStopped = true;
        }
      }

      p.lastActive = isActive;
      p.lastQualified = isQualified;
      if (isActive) { active += 1; p.activeWeeks += 1; }
      if (isQualified) { qualified += 1; p.qualifiedWeeks += 1; }
      if (byForce) forced += 1;
    }

    const stopped = team.filter((p) => p.status === 'stopped').length;
    weeks.push({
      week: w,
      licences: team.length,
      active,
      qualified,
      forced,
      stopped,
      activeRate: active / team.length,
      qualifiedRate: oppPop > 0 ? qualified / oppPop : 0,
      hoursSaved: (qualified * preset.usesPerWeek * preset.minutesPerUse) / 60,
    });
  }

  const last = weeks.slice(-4);
  const avg = (k) => last.reduce((a, x) => a + x[k], 0) / last.length;
  const peakActive = Math.max(...weeks.map((x) => x.activeRate));
  const quietStoppers = team.filter((p) => p.everStopped && p.stoppedWeek >= 3);
  return {
    weeks,
    people: team,
    summary: {
      teamSize: team.length,
      opportunityPopulation: oppPop,
      licences: team.length,
      activeRate: avg('activeRate'),
      qualifiedRate: avg('qualifiedRate'),
      peakActiveRate: peakActive,
      peakWeek: weeks.find((x) => x.activeRate === peakActive).week,
      hoursSavedPerWeek: avg('hoursSaved'),
      goodhartGap: avg('activeRate') - avg('qualifiedRate'),
      quietStoppers: quietStoppers.length,
      stillStopped: team.filter((p) => p.status === 'stopped').length,
      neverTried: team.filter((p) => !p.tried).length,
      forcedShare: avg('forced') / team.length,
    },
  };
}

/** The people who quietly stopped (tried, stopped in week 3 or later). */
export function whoStopped(result) {
  return result.people
    .filter((p) => p.everStopped && p.stoppedWeek >= 3)
    .map((p) => ({
      name: p.name, triedWeek: p.triedWeek, stoppedWeek: p.stoppedWeek, backTo: p.oldWay,
      cameBack: p.status === 'using', returnedWeek: p.returnedWeek,
      stillCountedActive: p.status === 'stopped' && p.lastActive,
      hasOpportunity: p.hasOpportunity,
    }))
    .sort((a, b) => a.stoppedWeek - b.stoppedWeek);
}
