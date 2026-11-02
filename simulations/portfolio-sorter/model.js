// Portfolio sorter: pure model (no DOM). The scenario (cards, teams, expert view) lives in presets.js.

/** Scoring rules the learner may lock in with the weights. Two of them are traps. */
export const RULES = {
  netErrors: {
    label: 'Net the expected cost of errors from the benefit before scoring value',
    help: 'You must open each card’s error cost before you can score its value.',
  },
  halfClaims: {
    label: 'Benefits that are only claimed, not measured, count at half value',
    help: 'Applied to the value score of cards whose evidence is a claim.',
  },
  askCapacity: {
    label: 'Ask every receiving team what it can absorb before committing',
    help: 'You cannot commit until you have asked each team in your portfolio.',
  },
  ceoBonus: {
    label: 'Give the CEO’s announced priority a bonus of 20 points',
    help: 'Added to the score of the card the CEO announced.',
    trap: true,
  },
  vendorAsMeasured: {
    label: 'Count a vendor’s published case study as measured evidence',
    help: 'Vendor claims are then not halved by the rule above.',
    trap: true,
  },
};

export const MAX_PICKS = 3;
export const CEO_BONUS = 20;

/** Weights as shares that sum to 1 (equal if all are zero). */
export function normaliseWeights(w) {
  const total = w.value + w.feasibility + w.risk;
  if (total <= 0) return { value: 1 / 3, feasibility: 1 / 3, risk: 1 / 3 };
  return { value: w.value / total, feasibility: w.feasibility / total, risk: w.risk / total };
}

/** Expected monthly cost of errors: items x error rate x cost per error. */
export function errorCost(card) {
  return card.volume * card.errorRate * card.costPerError;
}

/** Claimed monthly benefit minus the expected cost of errors. */
export function netBenefit(card) {
  return card.claimedBenefit - errorCost(card);
}

/** Is this card's value halved under these criteria? */
export function valueDiscounted(card, criteria) {
  if (!criteria.rules.halfClaims || card.evidence !== 'claim') return false;
  return !(criteria.rules.vendorAsMeasured && card.source === 'vendor');
}

const complete = (r) => r && r.value > 0 && r.feasibility > 0 && r.risk > 0;

/**
 * Score 0-100 (more with the CEO bonus) from ratings 1-5: value high = good, feasibility high = easy,
 * risk high = bad (so risk counts as 6 - risk). Null until all three are rated.
 */
export function cardScore(card, rating, criteria) {
  if (!complete(rating)) return null;
  const w = normaliseWeights(criteria.weights);
  const v = valueDiscounted(card, criteria) ? rating.value * 0.5 : rating.value;
  let score = ((w.value * v + w.feasibility * rating.feasibility + w.risk * (6 - rating.risk)) / 5) * 100;
  if (criteria.rules.ceoBonus && card.ceoPriority) score += CEO_BONUS;
  return score;
}

/** Cards ranked by score (unrated last). */
export function ranking(scenario, ratings, criteria) {
  return scenario.cards
    .map((c) => ({ card: c, score: cardScore(c, ratings[c.id], criteria) }))
    .sort((a, b) => (b.score ?? -1) - (a.score ?? -1));
}

/** Absorption per receiving team for the picked cards. capacity is known only if asked. */
export function absorption(scenario, picks, asked) {
  const rows = [];
  for (const team of scenario.teams) {
    const cards = scenario.cards.filter((c) => picks.includes(c.id) && c.team === team.id);
    if (!cards.length) continue;
    const demand = cards.reduce((a, c) => a + c.absorbHours, 0);
    const isAsked = asked.includes(team.id);
    rows.push({
      team, cards: cards.map((c) => c.id), demand,
      asked: isAsked,
      capacity: isAsked ? team.capacity : null,
      over: demand > team.capacity,
    });
  }
  return rows;
}

/** What still blocks a commit. Empty list = ready. */
export function commitProblems(scenario, criteria, ratings, picks, asked, netted) {
  const problems = [];
  const unrated = scenario.cards.filter((c) => !complete(ratings[c.id]));
  if (unrated.length) problems.push(`Score every card first (${unrated.length} left).`);
  if (picks.length === 0) problems.push('Choose at least one card for your portfolio.');
  if (picks.length > MAX_PICKS) problems.push(`Your portfolio can hold at most ${MAX_PICKS} cards.`);
  if (criteria.rules.askCapacity) {
    const notAsked = absorption(scenario, picks, asked).filter((r) => !r.asked).map((r) => r.team.name);
    if (notAsked.length) problems.push(`Your own rule: ask what ${notAsked.join(' and ')} can absorb before you commit.`);
  }
  if (criteria.rules.netErrors) {
    const notNetted = scenario.cards.filter((c) => picks.includes(c.id) && !netted.includes(c.id)).map((c) => c.title);
    if (notNetted.length) problems.push(`Your own rule: net the error cost of ${notNetted.join(', ')}.`);
  }
  return problems;
}

/** The debrief after commit. */
export function evaluate(scenario, criteria, ratings, picks, asked, netted) {
  const expert = scenario.expert;
  const expertScores = {};
  for (const c of scenario.cards) expertScores[c.id] = cardScore(c, c.expertRating, expert.criteria);

  const cards = scenario.cards.map((c) => {
    const r = ratings[c.id];
    const diff = complete(r)
      ? (Math.abs(r.value - c.expertRating.value) + Math.abs(r.feasibility - c.expertRating.feasibility) + Math.abs(r.risk - c.expertRating.risk)) / 3
      : null;
    return {
      card: c,
      yourScore: cardScore(c, r, criteria),
      expertScore: expertScores[c.id],
      picked: picks.includes(c.id),
      expertPicked: expert.picks.includes(c.id),
      netted: netted.includes(c.id),
      ratingGap: diff,
      errorCost: errorCost(c),
      net: netBenefit(c),
    };
  });

  const overlap = picks.filter((id) => expert.picks.includes(id));
  const trapsPicked = cards.filter((x) => x.picked && x.card.trapPick);
  const absorb = absorption(scenario, picks, asked);
  const overCapacity = absorb.filter((r) => r.over);
  const pickedNotNetted = cards.filter((x) => x.picked && !x.netted);
  const pickedNegativeNet = cards.filter((x) => x.picked && x.net < 0);
  const ew = normaliseWeights(expert.criteria.weights);
  const yw = normaliseWeights(criteria.weights);
  const weightDistance = (Math.abs(ew.value - yw.value) + Math.abs(ew.feasibility - yw.feasibility) + Math.abs(ew.risk - yw.risk)) / 2;
  const trapRules = Object.keys(RULES).filter((k) => RULES[k].trap && criteria.rules[k]);
  const missedRules = Object.keys(RULES).filter((k) => !RULES[k].trap && !criteria.rules[k]);
  const gaps = cards.filter((x) => x.ratingGap !== null);
  const meanGap = gaps.length ? gaps.reduce((a, x) => a + x.ratingGap, 0) / gaps.length : null;
  const biggestGaps = gaps.slice().sort((a, b) => b.ratingGap - a.ratingGap).slice(0, 3).filter((x) => x.ratingGap >= 1);

  return {
    cards, overlap, trapsPicked, absorb, overCapacity, pickedNotNetted, pickedNegativeNet,
    weightDistance, trapRules, missedRules, meanGap, biggestGaps,
    mustHavePicked: picks.includes(expert.mustHave),
    askedTeams: asked.length,
    totalBuild: cards.filter((x) => x.picked).reduce((a, x) => a + x.card.buildCost, 0),
    expertBuild: cards.filter((x) => x.expertPicked).reduce((a, x) => a + x.card.buildCost, 0),
  };
}
