---
id: "17.3"
module: 17
minutes: 16
practice_minutes: 100
prerequisites: ["17.2", "02.4", "03.7", "03.9"]
objectives:
  - "Give every AI system one measure, one definition and one owner, and measure each against a comparison rather than the vendor's baseline."
  - "Restate a booked savings figure line by line into measured, directional and claimed value, separating cash from capacity."
  - "Decompose a cost overrun into what was never budgeted, what ran too long and what the incident added."
  - "Write a one-page case for two principals that names the binding constraint and puts the non-AI fixes first."
volatility: concept
sources:
  - title: "IBM Lead AI Transformation: Strategy, Governance & Execution Professional Certificate (Coursera): net the claim, capacity vs cash, credible counterfactual"
    url: https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): AI Business Cases and ROI Models; the decision-ready case"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
last_verified: "2026-11-03"
---

# 17.3 · Diagnosis

The board was told ₪6.2M a year; the CEO wants it "back on track"; the external auditor will ask about it in August. In this lesson you give every system one measure and one owner, measure each against a fair comparison instead of the vendor's baseline, restate the savings line by line, take the overrun apart, find the binding constraint, and write the one-page case you walk through with the CEO first and the chair second. At the end you have a baseline table, a restated money table, a short list of fixes that need no AI, and the case.

## The situation

Sunday 20 June 2027. The findings memo went to both principals on Thursday ([17.2](lesson-02.md)); the incident is reopened and counsel has the facts. Svetlana, the CFO, sent the GL lines behind the four savings lines. Ofer read the memo and asked for "the upside: what the North could do across all regions". Ilana asked one question: "Which of these numbers would survive our auditor?"

IBM's value course has the vocabulary: net the claim, separate capacity from cash, demand a credible counterfactual, start with the conservative case. Its exercises hand you a measured number. Here you produce the number from Vantage's exports, and you produce it for two readers who want different things from it.

## What to do

### Step 1 — One measure, one definition, one owner per system

Use [02.4](../module-02/lesson-04.md). Every system gets the measure its budget owner already reviews, defined so it can be recomputed next quarter, and an owner who works at Vantage:

| System | Measure | Comparison | Owner |
|---|---|---|---|
| Route, North | Telematics km per stop | Same months a year earlier | Fleet (transport safety officer) |
| Route, any region | Late stops / stops | Before, with and after the tool | Regional manager |
| Docs | Material error per declaration, re-checked sample | Monthly QA, 5% | Head of customs brokerage |
| Docs | Seconds on the approval screen (median) | Weekly | Head of customs brokerage |
| Assist | Customer-service contacts a week | Before and after launch | VP Customers |
| Forecast | Overtime and agency cost at Modi'in | Ashdod DC, which still plans by spreadsheet | Head of warehousing |
| Kotev | Active users in 30 days | Seats billed | CFO |

The vendor's dashboard is not on the list: a measure the vendor computes for its own renewal cannot be the owner's.

### Step 2 — Measure against a comparison, not against the vendor's baseline

The dashboard says ₪2.56M a year (`vendor/tzir-value-dashboard-2027-05.md`). Its method: kilometres of a "naive shortest-path sequence of the same stops" minus the plan's kilometres, times ₪4.10, scaled to all licensed regions. Three problems, each checkable: the naive sequence is not what Vantage's dispatchers ever drove; the actual kilometres in `operations/route-daily-by-depot.csv` (`km_actual`) are never used; and three of the four regions do not use the tool.

The fair comparison: `operations/fleet-km-fuel-monthly.csv`, km per stop, December–May against November–April a year earlier. North −4.0%; Centre −0.2%; South −0.1%; Europe +0.8%. North's fuel is about ₪3.33M a year, so the effect is about **₪134,000** a year of fuel. Label it *directional*: there is no control region that kept a year without the tool, and fuel price moved.

The warehouse forecast has the comparison IBM asks for. Modi'in DC planned with the model from 3 January; Ashdod DC kept the spreadsheet. Average weekly overtime, before and after: Modi'in 713 → 609 hours, Ashdod 581 → 584. The difference in differences is **−15.1%**; with `overtime_cost_ils` and `agency_cost_ils`, about **₪624,000** a year. Label it *measured*.

### Step 3 — Restate the savings, line by line, cash and capacity apart

Use the [ROI model](../../templates/roi-model.md) and [03.7](../module-03/lesson-07.md):

| Line | Booked | What Vantage's data shows | Cash | Capacity | Label |
|---|---|---|---|---|---|
| Fuel and km | ₪3,100,000 | North km per stop −4.0%; other regions flat | ≈ ₪134,000 | — | Directional |
| Customs productivity | ₪1,600,000 ("8 FTE freed") | 31 agents before and after; output 9.2 a day; overtime up in May; 2 posts frozen since January | 0 | 2 frozen posts at most | Measured: no cash |
| CS deflection | ₪900,000 | Contacts a week 1,970 before, 1,995 after; 49% of sessions handed to a person | 0 | 0 | Measured: none |
| Warehouse overtime | ₪600,000 | −15.1% against Ashdod | ≈ ₪624,000 | — | Measured |
| **Total** | **₪6,200,000** | | **≈ ₪760,000** | | |

The customs line deserves one sentence of its own: the target rose from 9 to 12 declarations a day, volume did not, nobody moved. "Freed" capacity that is not used for anything is not a saving, and here the time it came from was the review.

[Simulation: ROI defender](../../simulations/roi-defender/index.html?preset=harbor)

The simulation is Harbor & Pine's, not Vantage's: practise netting a sponsor's claims across four ledgers there, then apply the same moves to the four lines above.

### Step 4 — Take the overrun apart

`finance/ai-programme-cost-2027.csv`, budget against actual plus forecast: ₪5.2M against ₪7.51M, +₪2.31M (+44%). By cause:

| Cause | ₪ 2027 |
|---|---|
| Never budgeted: Tzir Assist subscription and implementation ("funded from AI savings") | 2,090,000 |
| Ran longer than budgeted: Ayin (+₪116,000), Nezek (+₪88,000), quote add-in (+₪28,500) | 232,500 |
| The incident and you | 216,000 |
| Lower: the AI team after the head of AI left (−₪229,000) and other lines | −227,632 |

Read the first line twice. The budget funded part of the programme from savings that did not exist; the overrun is that circle closing. Behind it sits a commitment larger than any annual budget: three order forms of ₪4.86M, ₪4.68M and ₪4.87M, ₪14.41M over 36 months. That goes to the audit committee as a fact (protocol line 2); in your case it is the reason that "stop the vendor" is not a free option.

### Step 5 — Find the binding constraint

IBM asks for the one constraint that, if lifted, frees the rest. It is tempting to say the vendor, or the money. The evidence says something else: **nothing on the list had an owner who measured it.** The register recorded claims; the vendor computed the savings; the review was assumed; the regions were reported from licences; the feed broke and nobody owned it; the incident was closed on the vendor's word. Replace the vendor and the next one fills the same gap; cut the money and the forecast goes with the cameras.

### Step 6 — The fixes that need no AI come first

| Fix | Effect | Cost |
|---|---|---|
| Update the telematics credentials in the vendor's feed | The route model can adapt to Vantage's roads | IT, a day |
| Enter the closed roads in the North's console | Fewer overrides at Kiryat Shmona | Planners, about three days |
| Customs KPI back to 9–10 a day; supplier invoice beside the pre-fill | The review becomes possible | No cash |
| One business owner per system and per contract | Someone stops the invoices for unused tools | A list and a signature |

### Step 7 — The one-page case, walked through in protocol order

Use the [decision-ready case](../../templates/decision-ready-case.md) and [03.9](../module-03/lesson-09.md): the ask in one sentence, why now, what it costs, what it does not do, labels on every number. Walk it through with Ofer first (roleplay: [Ofer Lavi](../../labs/module-17/personas/ofer-ceo.md)), then Ilana ([Dr. Ilana Shaked](../../labs/module-17/personas/ilana-audit-chair.md)) the same afternoon.

Ofer will ask you to annualise the North across all regions. Answer with a date, not an argument: "The other regions don't use it. Fix the feed and the roads, measure the North again in September, and Centre decides then on that number." Ilana will ask which numbers survive the auditor. Answer with the labels.

> [!TIP]
> "About an eighth of the booked savings can be evidenced" is a finding. "The savings were fabricated" is an accusation nobody can prove and nobody needs. Say the first.

## Watch out

- **Arguing with the dashboard's arithmetic.** Its sums are right; its baseline is the problem. Replace the baseline, don't audit the multiplication.
- **Annualising the one region that works.** The North's −4% says nothing about regions that don't use the tool. Give the CEO a date to measure again, not a bigger number.
- **Counting capacity as cash.** "8 FTE freed" with 31 agents on the payroll is not a saving; at most it is a reason two posts stayed frozen.
- **Throwing out the measured with the claimed.** The forecast's ₪0.62M is the best-evidenced number in the company. Lead with it.
- **Hiding the overrun inside the restatement.** The board must see both: savings were overstated *and* costs were understated, and the second followed from the first.
- **Making the order forms your finding.** They are a fact for the committee; in your case they only explain why exiting the vendor is expensive.
- **Showing the chair first.** The protocol says the CEO sees findings about his decisions first, the same day.

## Your turn

### Inputs

- Your findings memo from 17.2.
- The [data room](../../labs/module-17/data-room/INDEX.md) (module download): `operations/fleet-km-fuel-monthly.csv`, `operations/warehouse-overtime-weekly.csv`, `operations/route-daily-by-depot.csv`, `vendor/tzir-value-dashboard-2027-05.md`, `customs/brokerage-staffing-monthly.csv`, `portal/cs-contacts-weekly-2027.csv`, `portal/assist-sessions-2027.csv`, `finance/ai-programme-cost-2027.csv`, `company/budget-2027-ai-and-savings.md`, `ai/forecast-backtest-2027-04.md`.
- Personas: [Ofer Lavi](../../labs/module-17/personas/ofer-ceo.md) and [Dr. Ilana Shaked](../../labs/module-17/personas/ilana-audit-chair.md) (or their transcripts), [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [ROI model](../../templates/roi-model.md), [decision-ready case](../../templates/decision-ready-case.md), [opportunity map](../../templates/opportunity-map.md) (for the non-AI options).
- Track B: `discovery.py`, section 6.

### Steps

1. Write the baseline table: one measure, its definition, its comparison and its owner for each system.
2. Compute the fuel effect from telematics (km per stop, a year earlier) and the warehouse effect as a difference in differences against Ashdod, in hours and ₪.
3. Restate the four savings lines: booked, evidence, cash, capacity, label.
4. Decompose the overrun by cause; note the 36-month commitment as context.
5. Name the binding constraint in one sentence and list the fixes that need no AI.
6. Write the one-page case. Walk it through with Ofer, then Ilana (roleplay or written notes of what each would ask), and record each one's reaction.

**Track B (Python).** `python discovery.py` section 6 computes the km-per-stop change by region, the North's fuel effect, the warehouse difference in differences and the contact volumes; section 7 the cost table. Python earns its place here because the restatement must be recomputed identically for the half-year accounts in August and every quarter after; the scripts are the definition.

### Time

100 minutes: 15 for the baseline table, 25 for the two effects, 15 for the restatement, 10 for the overrun, 10 for the constraint and fixes, 25 for the case and the two conversations.

### Done when

- [ ] Every system has one measure with a definition, a comparison and an owner who works at Vantage; the vendor's dashboard is not a measure.
- [ ] The fuel and warehouse effects are computed from Vantage's own data with a stated comparison, and labelled.
- [ ] The restatement separates cash from capacity and totals the evidenced value.
- [ ] The overrun is explained by cause and the unbudgeted line is named.
- [ ] The case names the binding constraint, puts the non-AI fixes first, and labels every number.
- [ ] The CEO saw the case before the chair, the same day.

<details><summary>Reference answer</summary>

The full version is `labs/module-17/expert/03-baseline-and-case.md` (module download).

**Effects (M unless marked):** km per stop North −4.0% (6.12 → 5.88), Centre −0.2%, South −0.1%, Europe +0.8%; North fuel ≈ ₪3.33M a year, so ≈ ₪134,000 (directional). Warehouse: Modi'in overtime 712.8 → 608.9 hours a week, Ashdod 580.6 → 583.9; difference in differences −15.1%, ≈ ₪624,000 a year with agency cost.

**Restatement:** booked ₪6,200,000; evidenced ≈ ₪760,000 (warehouse ₪624,000 measured, North fuel ₪134,000 directional); customs 0 cash (31 agents, output 9.2 a day, 2 posts frozen); CS 0 (1,970 → 1,995 contacts a week; 49% of sessions handed to a person).

**Overrun:** ₪5,200,000 budget vs ₪7,510,868: Assist never budgeted ₪2,090,000; pilots longer ₪232,500; incident and interim lead ₪216,000; AI team lower −₪228,998 and cloud +₪1,366. Context: order forms ₪14.41M over 36 months.

**Constraint:** nothing on the list had an owner who measured it.

**Case (ask):** "Agree on 24 June a turnaround plan that closes the incident on facts before 1 July, stops seven things, reduces two, keeps three with owners, brings three in from outside the register, and gives the board on 5 July numbers it can test." Why now: post-fix mismatches, 2,462 records, nine overdue customs queries, the 1 July notice date, the auditor in August. Cost: nothing new; ₪340,620 saved inside 2027.

**Reactions:** Ofer objected to "an eighth" and asked to annualise the North; accepted the restatement "if the plan shows what the North can become" — answered with the September re-measurement. Ilana asked how the ₪624,000 was measured, accepted the Ashdod comparison, and asked that the case say plainly the ₪6.2M was never measured.

</details>

## References

- IBM, [Lead AI Transformation certificate](https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution): net the claim, capacity vs cash, credible counterfactual, conservative case first (named, not re-taught).
- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting): the business case and the decision-ready case.
- [Simulation: ROI defender](../../simulations/roi-defender/index.html?preset=harbor) (Harbor & Pine's preset; educational model).
- Field kit: [02.4 · Measuring a baseline from exports](../module-02/lesson-04.md), [03.7 · The ROI model that survives finance](../module-03/lesson-07.md), [03.9 · The decision-ready case](../module-03/lesson-09.md).
- Templates: [ROI model](../../templates/roi-model.md), [decision-ready case](../../templates/decision-ready-case.md), [opportunity map](../../templates/opportunity-map.md).
- Earlier: [17.2 · Discovery](lesson-02.md). Next: [17.4 · The hard part: a turnaround](lesson-04.md).
