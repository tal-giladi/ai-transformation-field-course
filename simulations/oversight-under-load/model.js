// Oversight under load: pure model (no DOM). Expected values, no randomness, so every number can be
// traced back to the equations in "About this model".

/** Arrivals by weekday (Sunday to Thursday): the queue is heaviest after the weekend. */
export const DAY_FACTORS = [1.25, 1.05, 0.95, 0.9, 0.85];
export const DAY_NAMES = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu'];

/** Fixed constants of the model (shown in "About this model"). */
export const K = {
  stampMinutes: 0.4,        // time to approve an item without checking it
  sourceSpeedup: 0.65,      // check time multiplier when the source is shown beside the draft
  catchChecked: 0.85,       // chance a real check catches a wrong item
  catchCheckedSource: 0.95, // ... when the source is shown beside the draft
  catchStamped: 0.15,       // chance a rubber stamp still catches a wrong item (the blatant ones)
  recovery: 0.5,            // flag feedback on: vigilance recovers half the gap to 1 each day
  decayNoFeedback: 0.06,    // flag feedback off: vigilance falls 6% a day (flags go nowhere)
  decayUsuallyRight: 0.04,  // extra daily fall when feedback is off and under 10% of items are wrong
  fatigue: 0.05,            // daily fall per unit of overload (load above 1)
  minVigilance: 0.3,
};

/** Minutes a real check takes with these settings. */
export function checkTime(p) {
  return p.checkMinutes * (p.sourceShown ? K.sourceSpeedup : 1);
}

/** The capacity screen: the most items per reviewer-hour that can still get a real check. */
export function capacityScreen(p) {
  return 60 / checkTime(p);
}

/**
 * p: { itemsPerDay, reviewers, hoursPerReviewer, errorRate, checkMinutes, sourceShown, flagFeedback, days }
 * Returns { days: [...per day], totals }.
 */
export function simulate(p) {
  const days = [];
  const c = checkTime(p);
  const sMin = K.stampMinutes;
  const pChecked = p.sourceShown ? K.catchCheckedSource : K.catchChecked;
  const capMin = p.reviewers * p.hoursPerReviewer * 60;
  let v = 1;

  for (let d = 0; d < p.days; d += 1) {
    const items = Math.round(p.itemsPerDay * DAY_FACTORS[d % DAY_FACTORS.length]);
    const load = capMin > 0 ? (items * c) / capMin : Infinity;
    // How many real checks fit in the day if every other item is at least stamped.
    let kTime;
    if (items === 0) kTime = 0;
    else if (c <= sMin) kTime = items;
    else kTime = Math.min(items, Math.max(0, (capMin - items * sMin) / (c - sMin)));
    const timeShare = items > 0 ? kTime / items : 1;
    const realShare = timeShare * v;
    const checked = items * realShare;
    const stamped = items - checked;
    const wrong = items * p.errorRate;
    const caught = wrong * (realShare * pChecked + (1 - realShare) * K.catchStamped);
    const escaped = wrong - caught;
    const used = checked * c + stamped * sMin;
    const utilisation = capMin > 0 ? used / capMin : Infinity;

    days.push({
      day: d + 1, name: DAY_NAMES[d % DAY_NAMES.length], items, load, timeShare, vigilance: v,
      realShare, checked, stamped, wrong, caught, escaped, utilisation,
      catchRate: wrong > 0 ? caught / wrong : 1,
    });

    // Vigilance for tomorrow.
    if (p.flagFeedback) v += K.recovery * (1 - v);
    else {
      v -= K.decayNoFeedback * v;
      if (p.errorRate < 0.1) v -= K.decayUsuallyRight * v;
    }
    if (load > 1) v -= K.fatigue * (load - 1) * v;
    v = Math.min(1, Math.max(K.minVigilance, v));
  }

  const sum = (k) => days.reduce((a, x) => a + x[k], 0);
  const items = sum('items');
  const wrong = sum('wrong');
  const caught = sum('caught');
  const escaped = sum('escaped');
  const checked = sum('checked');
  const reviewerHours = p.reviewers * p.hoursPerReviewer;
  return {
    days,
    totals: {
      items, wrong, caught, escaped, checked,
      stamped: items - checked,
      catchRate: wrong > 0 ? caught / wrong : 1,
      stampShare: items > 0 ? (items - checked) / items : 0,
      avgUtilisation: days.length ? sum('utilisation') / days.length : 0,
      maxUtilisation: Math.max(...days.map((x) => x.utilisation)),
      overloadedDays: days.filter((x) => x.load > 1).length,
      finalVigilance: days.length ? days[days.length - 1].vigilance : 1,
      reviewerHoursPerDay: reviewerHours,
      itemsPerReviewerHour: reviewerHours > 0 ? p.itemsPerDay / reviewerHours : Infinity,
      peakItemsPerReviewerHour: reviewerHours > 0 ? (p.itemsPerDay * Math.max(...DAY_FACTORS)) / reviewerHours : Infinity,
      screen: capacityScreen(p),
    },
  };
}

/** Did the learner's design meet the scenario's target? */
export function checkTarget(p, target) {
  const { totals } = simulate(p);
  const withinHours = totals.reviewerHoursPerDay <= target.maxReviewerHoursPerDay + 1e-9;
  const withinErrors = totals.escaped <= target.maxEscaped + 1e-9;
  return { totals, withinHours, withinErrors, met: withinHours && withinErrors };
}

/** Catch rate over the whole run while daily volume moves (for the load curve). */
export function loadCurve(p, volumes) {
  return volumes.map((x) => ({ x, y: simulate({ ...p, itemsPerDay: x }).totals.catchRate }));
}
