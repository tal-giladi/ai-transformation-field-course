# Use-case scorecard

One card per candidate in two parts. Part A is the fast screen: seven questions answered in one sentence each, a data gate that is pass or fail, and a verdict of go, go with a condition, or stop. Part B is the score, filled only for candidates that passed the screen and only after the scoring criteria have been locked: value, feasibility and risk ratings with their evidence, effort in four parts, the expected cost of errors, and what the receiving team can absorb. Lessons [03.3](../lessons/module-03/lesson-03.md) (part A) and [03.4](../lessons/module-03/lesson-04.md) (part B) show how; the spreadsheet version, one row per candidate, is `labs/module-03/use-case-scorecard.csv` in the module 3 download ([open](../labs/module-03/use-case-scorecard.csv)).

## How to fill it

- Write the scrutiny rule and lock the criteria (weights and rules) **before** opening any card, and date them.
- Every answer names a file or a person. A blank means "not asked yet", never "medium".
- The data gate is four separate passes or fails. One fail means the verdict cannot be "go".
- A "stop" says what would reopen it; a "go with a condition" has an owner and a date.
- Ratings are 1–5 with a one-line reason; risk 5 is the worst. Claimed benefits (not measured) count at half value if the locked rules say so.
- Expected error cost = items a month × error rate × cost per error. Net it from the benefit before you rate value.
- Absorption comes from the receiving team's lead, in hours a month, not from you.

## Template

```markdown
# Use-case scorecard — [candidate] — [organization]

Scrutiny rule (dated): [ ]   ·   Criteria locked on [date] by [who]: weights value [ ]% /
feasibility [ ]% / risk [ ]%; rules: [net errors · claims at half value · ask capacity · …]

## Part A — The fast screen ([date])
| # | Question | Answer (one sentence) | Source (file or person) |
|---|---|---|---|
| 1 | Value: what changes, how much, for whom, which goal? | | |
| 2 | Workflow fit: walkable? who receives it, which decision changes, what do they do differently that day? | | |
| 3 | Data gate (below) | | |
| 4 | Feasibility: builder, connections, cost band, approval line | | |
| 5 | Risk: who or what a wrong output touches, how widely, reversible?, which law or policy | | |
| 6 | Sponsorship: who owns and runs it after the project team leaves | | |
| 7 | Measurement: indicator already reviewed, baseline, source | | |

**Data gate:** reachable [pass/fail] · trusted [pass/fail] · lawful for the purpose [pass/fail/routed
to: ] · label recorded [pass/fail/not needed] — reason: [ ]

**Verdict:** [go / go with a condition / stop] — turns on question [ ] — condition or what would
reopen it: [ ] — owner: [ ] — date: [ ]

**Routed questions:** [question → counsel / DPO / security / procurement, date sent]

## Part B — The score ([date], only after Part A says go or go with a condition)
| | Rating 1–5 | Reason and evidence |
|---|---|---|
| Value (after netting errors; claimed = half if the rule says so) | | |
| Feasibility | | |
| Risk (5 = worst) | | |

Benefit claimed: ₪[ ] a month ([measured / mixed / claimed], source) · Expected error cost: [items] ×
[rate] × ₪[cost] = ₪[ ] a month · Net: ₪[ ] a month

Effort in four parts (each with an owner):
| Part | Rating (low / medium / high) | Why | Owner | Reshape move |
|---|---|---|---|---|
| Data condition | | | | |
| Integration surface | | | | |
| Regulatory and compliance burden | | | | |
| Adoption resistance | | | | |

Receiving team: [team] — needs [ ] hours a month — can absorb [ ] (asked [who], [date])
Weighted score: [ ] / 100
```

## Example

Harbor & Pine, B2B quote drafts (excerpt):

- Part A verdict: **go with a condition** — turns on question 3 (trusted) and 5 (risk): prices and agreed discounts read from Priority, never written by the model. Owner Yaniv Carmi, April 2027.
- Part B: value 3, feasibility 4, risk 3. Claimed ₪8,750 a month (140 quotes × 25 minutes × ₪150 an hour, Yaniv's two-week time study, reported). Expected error cost in the trial: 140 × 4% × ₪900 = ₪5,040, net ₪3,710; with prices read from Priority wrong prices fall below 1%. Effort: data medium (price agreements in personal spreadsheets), integration medium (Priority read), regulatory low, adoption low. Sales needs 10 hours a month and can absorb 20 (Yaniv). Score with weights 40/30/30: 66.
