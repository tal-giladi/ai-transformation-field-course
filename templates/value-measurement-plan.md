# Value measurement plan

How you will know, at the gate, whether the pilot's benefit is real: the indicator the budget owner already reviews, a target that can be missed, a baseline taken with the same instrument as every later reading, a quality metric paired with every efficiency metric, a counterfactual with its fidelity label, an adoption gate, how long to run, and the second-order effects to watch. Write it with the pilot charter, before the pilot starts, and give it to the person who will judge the result (usually finance). Lesson [05.1](../lessons/module-05/lesson-01.md) shows how; engagements reuse it in every NN.3, and lesson 07.2 reads it at the scale, fix or stop decision.

## How to fill it

- Ask the budget owner which indicator they already review; the headline indicator should land in it.
- Baseline: same instrument, same definition, same population as the later readings. If there is no baseline, say so and name when and how it will be taken.
- Pair every efficiency metric with a quality metric that would move the wrong way if the gain were fake.
- Counterfactual, strongest first: random holdout, phased rollout, before-and-after per unit (never totals). Label the result **attributed** or **directional**.
- Adoption gate: the share of real use below which value numbers are not read.
- Duration: learning period excluded, measurement period long enough for the sample each threshold needs.

## Template

```markdown
# Value measurement plan — [pilot] — v[n], [date] (owner: [ ]; reader: [ ])

| Item | Entry |
|---|---|
| Indicator the budget owner reviews | [indicator] → [budget line or report] |
| Target (can be missed) | [number, date]; gate thresholds [link] |
| Baseline | [instrument, definition, population, period]; [value or "to be measured by …"] |
| Later readings | [same instrument, when] |
| Paired quality metrics | [efficiency metric] ↔ [quality metric]; … |
| Counterfactual | [holdout / phased / before-after per unit]; fidelity: [attributed / directional] |
| Adoption gate | [share of eligible items with real use, for how long] |
| Duration | [learning period excluded]; [measurement period]; [report date] |
| Second-order measures | [effects elsewhere: other teams, customers, shadow tools] |
| Fidelity label in the gate report | [per metric] |
```

## Example

Harbor & Pine, reply drafts, 8 December 2026: indicator = agent hours needed per month at peak volume, landing in the temp line Ronit already reviews; baseline = December time study (median minutes per written reply by category and language), with the Deskly timer meanwhile (median 9 minutes; Hebrew 8, Russian 10, Arabic 11; on 51% of tickets, self-selected); paired metrics = minutes per contact ↔ wrong replies reaching customers, acceptance ↔ repeat contact within 14 days (23.4% today), review time ↔ discard rate; counterfactual = random 10% holdout until gate 1 (attributed); adoption gate = drafts inserted on 60% of eligible tickets for two weeks; measured 15 February – 28 March, report 1 April.
