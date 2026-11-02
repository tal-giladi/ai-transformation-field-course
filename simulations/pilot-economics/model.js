// Pilot economics: pure model (no DOM). Every number is per month unless the name says otherwise.

export { steps } from '../common/math.js';

/** Working hours of one full-time person per month (42-hour week x 4.33). */
export const FTE_HOURS_PER_MONTH = 182;

/**
 * p: {
 *   volume            items per month in scope
 *   automationRate    share of items the AI handles (0..1)
 *   accuracy          share of AI outputs that are right (0..1)
 *   minutesSaved      minutes saved on an item when the AI output is right
 *   reviewMinutes     human review minutes on every AI-handled item
 *   reworkMinutes     extra minutes to fix an AI output that is wrong
 *   hourlyCost        fully loaded cost of one hour of the people doing the work (ILS)
 *   tokensIn, tokensOut   tokens per AI-handled item
 *   priceIn, priceOut     US$ per million tokens
 *   fx                ILS per US$
 *   fixedMonthly      fixed monthly cost (ILS): licences, hosting, monitoring, sampled QA
 *   buildCost         one-off build cost (ILS)
 * }
 */
export function compute(p) {
  const handled = p.volume * p.automationRate;
  const correct = handled * p.accuracy;
  const wrong = handled - correct;

  const grossMinutes = correct * p.minutesSaved;
  const reviewMinutesTotal = handled * p.reviewMinutes;
  const reworkMinutesTotal = wrong * p.reworkMinutes;
  const netMinutes = grossMinutes - reviewMinutesTotal - reworkMinutesTotal;

  const grossHours = grossMinutes / 60;
  const reviewHours = reviewMinutesTotal / 60;
  const reworkHours = reworkMinutesTotal / 60;
  const netHours = netMinutes / 60;

  const capacityValue = netHours * p.hourlyCost;
  const tokenUsd = (handled * (p.tokensIn * p.priceIn + p.tokensOut * p.priceOut)) / 1e6;
  const tokenIls = tokenUsd * p.fx;
  const runCost = tokenIls + p.fixedMonthly;
  const monthlyNet = capacityValue - runCost;
  const breakevenMonths = monthlyNet > 0 ? p.buildCost / monthlyNet : Infinity;
  const firstYearNet = monthlyNet * 12 - p.buildCost;

  const checkingShare = grossMinutes > 0 ? (reviewMinutesTotal + reworkMinutesTotal) / grossMinutes : Infinity;
  const reviewEatsSaving = reviewMinutesTotal + reworkMinutesTotal >= grossMinutes;

  // Review minutes per item at which monthly net value is exactly zero (everything else fixed).
  const runCostMinutes = p.hourlyCost > 0 ? (runCost * 60) / p.hourlyCost : Infinity;
  const maxReviewMinutes = handled > 0 ? (grossMinutes - reworkMinutesTotal - runCostMinutes) / handled : NaN;

  // Accuracy at which monthly net value is exactly zero (net value is linear in accuracy).
  const perItemSwing = p.minutesSaved + p.reworkMinutes;
  const breakevenAccuracy = handled > 0 && perItemSwing > 0
    ? (handled * p.reviewMinutes + handled * p.reworkMinutes + runCostMinutes) / (handled * perItemSwing)
    : NaN;

  return {
    handled, correct, wrong,
    grossMinutes, reviewMinutesTotal, reworkMinutesTotal, netMinutes,
    grossHours, reviewHours, reworkHours, netHours,
    fte: netHours / FTE_HOURS_PER_MONTH,
    capacityValue, tokenUsd, tokenIls, runCost, monthlyNet,
    breakevenMonths, firstYearNet,
    checkingShare, reviewEatsSaving,
    maxReviewMinutes, breakevenAccuracy,
    costPerItem: handled > 0 ? runCost / handled : NaN,
  };
}

/** Monthly net value while one parameter moves over values (everything else as in p). */
export function sweep(p, key, values) {
  return values.map((x) => ({ x, y: compute({ ...p, [key]: x }).monthlyNet }));
}

