# ROI model

The business-case model that finance will review: costs and benefits by year in the finance team's own structure, every claimed benefit netted across four ledgers and labelled, three scenarios, NPV at the organization's hurdle rate, payback, the approval level, a sensitivity table and staged gates. Build it after the leadership has agreed the bets and before the decision-ready case, with the CFO's template and rules in hand. Lesson [03.7](../lessons/module-03/lesson-07.md) shows how. The spreadsheet version is `labs/module-03/roi-model.csv` in the module 3 download ([open](../labs/module-03/roi-model.csv)); the Python track computes scenarios and sensitivity with `labs/module-03/roi_model.py`.

## How to fill it

- Ask finance first: the template, the hurdle rate, payback preference, approval bands, how headcount savings count, the planning exchange rate, cash-timing constraints. Build in that structure.
- Start from hours: volume × share handled × accuracy × minutes saved, minus review minutes on every handled item and rework on the wrong ones. Hours are capacity.
- Costs include what is not on the invoice: integration days, test set and evaluation, internal hours, training, contingency, running cost (licences, hosting, monitoring, change control) and tokens with the model, price and date.
- Net every claim on four ledgers: the sponsor's team (double counts, rework), the receiving team (work moved to it), control capacity (review labour), the customer's share (money the customer keeps or no longer gets). Ask what happens without the project.
- Label every net benefit **measured / directional / assumed** and **cash / capacity**, and name the budget line it lands in. Capacity becomes cash only with a named plan, owner and date.
- Price the expensive error as the change from today's error rate.
- Scenarios: low = measured cash; expected = + directional; high = + assumed. NPV = −build + Σ (cash − running) ÷ (1 + rate)^t. In a spreadsheet: `=NPV(rate, year1:year3) + year0`.
- Sensitivity: change one input at a time; show the change in expected NPV. The lines that move it most become gate conditions.
- Stages: the first stage within the lowest approval band that buys the evidence; every gate a yes/no condition with a date.

## Template

```markdown
# ROI model — [project] — [organization] — v[n], [date]

Finance rules (from [CFO], [date]): template [ ] · hurdle [ ]% · payback preferred ≤ [ ] months ·
approval bands [ ] · headcount savings only with [ ] · planning rate ₪[ ] per US$ ([date]) ·
cash timing [ ] · indicator finance already reviews: [ ]

## 1. Hours (a typical / peak month)
| Line | Calculation | Hours |
|---|---|---|
| Items in scope | [ ] | — |
| Handled ([ ]%) | [ ] | — |
| Saved on right outputs ([accuracy] × [minutes]) | | + |
| Review of every handled item ([minutes]) | | − |
| Rework of wrong outputs ([minutes]) | | − |
| **Net hours (capacity)** | | |

## 2. Costs (₪)
| Item | Year 0 | Year 1 | Year 2 | Year 3 | Basis (quote / estimate / guess) |
|---|---|---|---|---|---|
| Integration ([days] × ₪[rate]) | | | | | |
| Test set, evaluation | | | | | |
| Internal hours (labelling, training) | | | | | |
| Contingency | | | | | |
| Licences, hosting, monitoring, change control | | | | | |
| Tokens ([model], US$[in]/[out] per million, [date], ₪[rate]) | | | | | |
| **Total** | | | | | Three-year total ₪[ ] → approver: [ ] |

## 3. Benefits netted (₪ a year)
| # | Claim | Claimed | Sponsor's team | Receiving team | Control capacity | Customer's share | Net | Measured / directional / assumed | Cash / capacity | Lands in (budget line, owner) | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|

Counterfactual check: [what happens without the project, per claim]
Expensive error: [drafts a year] × [percentage points above today] × ₪[cost per error] = ₪[ ] a year per point

## 4. Scenarios at [rate]% over [n] years
| Scenario | Cash a year | Capacity a year (not cash) | NPV | Payback |
|---|---|---|---|---|
| Low (measured) | | | | |
| Expected (+ directional) | | | | |
| High (+ assumed) | | | | |

## 5. Sensitivity of the expected NPV
| What changes | NPV | vs base |
|---|---|---|

## 6. Stages and gates
| Stage | When | ₪ | Buys | Gate at the end (all yes/no) | Date |
|---|---|---|---|---|---|
```

## Example

Harbor & Pine, reply-drafts pilot (January 2027): net 108.8 hours a month at peak (1,920 drafts; +204.8 saved, −64 review, −32 rework). Build ₪120,000, running ₪49,000 a year, three-year total ₪267,000 → board. Claimed ₪1,360,000 a year; after netting, expected cash ₪113,000 a year (translation ₪17,000 measured; no temps next peak ₪96,000 directional, signed by Samir and Michal) plus ₪73,740 of capacity. NPV at 12% over three years: low −₪196,859, expected ₪33,717 (payback 22.5 months), high ₪195,000. Most sensitive: only one temp released (−₪115,288) and 1.5 points more wrong replies reaching customers (−₪99,609). Stage 1 ₪48,000 (February–March), gate 1 on 1 April 2027.
