---
id: "15.5"
module: 15
minutes: 21
practice_minutes: 180
prerequisites: ["15.4", "03.4", "03.8", "07.2", "07.8"]
objectives:
  - "Triage a portfolio of 40 builds with rules written before you look at the list: clean the copies, tier every build, stop what fails its own evidence, merge duplicates under one owner, and route the rest."
  - "Find the dependencies a cut would break, and decide a contested budget line on usage with the right denominator."
  - "Compute the review load and the money of the triaged portfolio under the new operating model, and meet a 15% budget cut without cutting the wrong thing."
  - "Write a 12-month scale plan with yes/no gates, review capacity per quarter, owners and dates, and test it against the simulation's events."
volatility: implementation
sources:
  - title: "Bank of Israel, Proper Conduct of Banking Business Directive 369, Management of Model Risk (English, 8/24): one owner per model (§24), inventory (§30–32), periodic review (§67)"
    url: https://www.boi.org.il/media/ggpbdtqp/369_en.pdf
  - title: "Bank of Israel, Circular C-06-2571 (8 October 2018): Directive 359A, Outsourcing — board and management duties for outsourced activities"
    url: https://boi.org.il/media/w10dtldz/h2571_en.pdf
  - title: "Inter-ministerial team, Artificial Intelligence in the Financial Sector, final report (December 2025, Hebrew): bias and discrimination, outcome testing (pp. 103–110)"
    url: https://www.boi.org.il/media/rh0bejl4/aireport.pdf
  - title: "IBM Lead AI Transformation Professional Certificate (Coursera): pilot isn't scale, scale / sustain / retire, sequence for absorption"
    url: https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution
last_verified: "2026-11-03"
---

# 15.5 · Decide: triage, design and a 12-month plan

Forty builds, fourteen unit heads who each think theirs is first, a CFO who wants ₪3.02M back and a review queue that will carry six high-risk builds a year. In this lesson you triage the whole portfolio with rules you write before you look at the list, find the dependencies a cut would break, decide the assistant, compute what the new design needs from the queue and the budget, and write the 12-month plan with gates. At the end you have a triage table for all 43 rows, a merge and stop list with owners and dates, the money, and the plan you take to the Management Committee on 15 March.

## The situation

Monday 22 February 2027. The Model Committee on the 18th agreed to take AI policy v2 to the Board Risk Committee on 20 April, with the tier rule as MRM's document; Irina asked for the triaged list "so we know what the rule will be applied to". The CFO wants the list he was promised. The Katvan AI notice (two stop candidates) is due 15 March. The Management Committee meets on Monday 15 March.

This is [03.4](../module-03/lesson-04.md) and [07.2](../module-07/lesson-02.md) at portfolio scale: lock the criteria before you open the list, score on evidence, decide scale, fix or stop, merge duplicates, decommission properly. The difference is volume and politics: 43 rows from 14 units, each line someone's project. IBM's *pilot isn't scale* and *sequence for absorption* frame it; the rules below make it repeatable every quarter.

## What to do

### Step 1 — Write the rules before you open the list

Write and date five rules. Read them to Irina and Dalit before you apply them, so nobody can say they were fitted to the answer:

1. **One build, one row.** Rows sharing an environment and a test set are one build; keep the row that went to the Model Committee.
2. **Tier** by the rule in 15.4 (what the output decides, the data, the review) — never by the unit's own label.
3. **Stop** a build if any of these holds: its latest evaluation is below its own threshold; it has no owner; it has had no users for three months (unless on hold for the committee or customer-facing on a test); a compliance question on it is open and unanswered; an existing non-AI tool already does the job; it has no test set and almost no users.
4. **Merge** two builds of the same task on the same kind of data in two units; the kept build is the one with the stronger evidence (a passed evaluation on the bank's own data, then a test set, then users); one owner serves both.
5. **Route** everything else by its tier; fix first where the owner is missing or shared, or the baseline or the evaluation is missing.

### Step 2 — Clean, tier and record the issues

Open `triage-sheet.csv` in the module folder (Track A: every register row with its latest evaluation, and empty columns for your decisions), or run `triage.py` (Track B). The result of rules 1–3 on Crescent's register:

- **Clean (3):** OPS-04 = MTG-01, PRV-03 = TRS-01, OPS-05 = FIN-02. 43 rows → 40 builds.
- **Tier of the 40:** low 15, medium 14, high 11. Check the ones the units mislabelled: CV screening self-assessed "Medium" is high (hiring); the chatbot self-assessed "Low" is medium (answers customers); credit memo drafting self-assessed "Medium" is high (informs credit).
- **Stop (10):**

| Build | Issue (the evidence) |
|---|---|
| RET-02 Next-best-offer | Open compliance question on purpose of use of transaction data; uplift never tested |
| MTG-02 Valuation sanity check | False-accept 0.18 against 0.05; a 2023 price-index snapshot |
| MTG-04 Broker email drafts | No users since August; no test set |
| CRD-04 Chargeback summaries | The rules engine already does it |
| PRV-01 Client letters | Two users, no test set |
| PRV-02 Portfolio commentary | 14% factual errors on holdings against 2%; owner left in September |
| CMP-02 AML alert triage | False negatives 9% against 1%; 11 true positives auto-closed |
| CC-03 Complaint routing | Accuracy 0.61 against 0.85 |
| DIG-01 Customer chatbot | 0.76 against 0.90; wrong on 2026 fees; Arabic answered in Hebrew; live on 2% |
| HR-01 CV screening | Selection-rate ratio by home town 0.62 against 0.80; home town and graduation year as features |

Two of the stops are not only weak but exposed. CV screening ranks applicants partly by where they live and an age proxy; the inter-ministerial report's chapter on bias names outcome testing and proxies as the issue, and equal opportunity in employment is counsel's question. AML triage auto-closed real alerts; the 11 go back to AML operations today. Stopping is the decision; what else follows is Lina's and counsel's.

### Step 3 — Merge the duplicates under one owner

| Task | Kept build, one owner | Retired | The evidence that decided |
|---|---|---|---|
| Complaint summaries | CRD-01 (Cards, Bahir), Maya Elkayam | RET-01 (Retail, Mishov) | 0.91 on 300 of the bank's own complaints vs the vendor's 90% on its own benchmark |
| Credit memo drafting | CORP-01 (Corporate, Pinkas), Daniel Friedman | SME-01 (contractor POC) | 0.97 on 120 memos vs no test set |
| KYC document checks | CMP-01 (Compliance & AML, Imut Docs), Samer Khoury | SME-02 (Mismach Check) | 0.96 on 250 vs 0.89 on 90; licence covers business customers |
| Conversation summaries | CC-01 (Contact Centre, Kolot), Revital Cohen | DIG-02 (chat summaries) | 0.89 on 200 vs a 50-item spot check; fix Arabic (0.81) first |

Merging Retail's complaint build into Cards' means telling Hagit her build lost. Do it with the evidence and with what she keeps: Retail's channels and the themes report for the public complaints officer, a two-month side-by-side so the themes do not get worse, and Retail's branch-call request served from CC-01 later. Merge in two moves ([07.2](../module-07/lesson-02.md)): the knowledge and the users now, the build when the kept one has served both for a quarter. Directive 369 §24 says one owner per model; a merged build with two owners is not merged. Rehearse it (roleplay: [Hagit Mor](../../labs/module-15/personas/hagit-retail.md)), and agree with Karim (roleplay: [Karim Haddad](../../labs/module-15/personas/karim-cards.md)) what serving Retail means for his team.

Do not merge the five question-and-answer assistants (Branch FAQ, Mortgage FAQ, procedure assistant, knowledge assistant, HR FAQ). They share a pattern, not a task: one template and one platform pattern, five content owners.

### Step 4 — Decommission the stops, with the contract dates

Use the decommissioning checklist from 07.2 for each stop: people told what replaces it, access removed, data returned or deleted with written confirmation, contract notice, records updated, a check after 30 days. The contract list sets the dates: Katvan AI (MTG-04 and PRV-01) notice by **15 March**; Kishron Rank (HR-01) renewed itself on 15 December without a DPA — termination is for counsel. Directive 359A puts outsourced activities under the board's policy and management's oversight; ending a vendor relationship goes through procurement, not an email from the CoE.

### Step 5 — Find the dependencies, then decide the assistant

The register's `depends_on` column is empty, so the triage cannot see that two kept builds — the procedure assistant (OPS-02, 0.91) and the knowledge assistant (CC-02, 0.88) — run inside the assistant (OPS-01): its agent studio, its indexes, its seats. Cancelling OPS-01 deletes them 30 days later.

Decide the assistant on the usage that answers the question (15.2: 66% of onboarded users weekly, 74% and 68% in the pilot teams), not the CFO's 16% of all seats. The decision: **keep, staged** — the 380 onboarded first; branches from April with training and an approved template for letters in Arabic and Russian (the request Olga's branch made); the rest by September — with a condition the CFO can hold you to: weekly active users at least half of assigned seats by 30 September, or the seat count is cut to use. Write the dependencies into the catalogue (`depends_on`) so the next budget review sees them.

### Step 6 — The review load and the money

**Track B (Python).** `triage.py` applies the five rules to the register, writes `out/triage.csv`, groups the kept builds by pattern, computes the central review load under four designs and the money released. `--llm` asks an LLM, through `fieldkit.llm`, whether each same-pattern pair in different units is the same task (about 70 short calls; `FIELDKIT_PROVIDER=mock` tests it for free). Python is worth it here because the triage must be re-run every quarter on the catalogue with identical rules, and because the duplicates hide across Hebrew and English descriptions that a filter misses; the LLM check is a second opinion on pairs, never the decision.

```bash
cd labs/module-15
python triage.py
python triage.py --llm
```

The load, in review slots (3 AI slots a quarter):

| Design | Builds | To the queue | Slots | Quarters |
|---|---:|---:|---:|---:|
| Today | 40 | 40 | 80 | 26.7 |
| Triaged, full validation | 26 | 26 | 52 | 17.3 |
| Triaged, validation by tier | 26 | 26 | 26 | 8.7 |
| Triaged, rights by tier, templates | 26 | 6 | 12 | 2.7 |

The money for 2027: the triage releases ₪1.56M (stop) + ₪0.76M (merge, less ₪0.18M of merge work) + ₪0.42M (double-booked) of unit lines; the hub of 10 instead of a central team of 16 brings the central programme from ₪11.0M to about ₪10.0M after funding the platform (₪2.4M + ₪0.6M run), the evaluation kit (₪0.32M), the catalogue (₪0.225M), the reorganisation (₪0.3M) and a validation contractor (₪0.35M). All AI spend: ₪20.13M → about ₪16.57M, a saving of about ₪3.57M against the CFO's ₪3.02M, **with the assistant kept**. Label it: unit lines measured; central lines directional.

### Step 7 — The 12-month plan

Use the [roadmap](../../templates/roadmap.md) of [03.8](../module-03/lesson-08.md) and the [phase-1 plan](../../templates/phase-1-plan.md) of [07.8](../module-07/lesson-08.md). Gates as yes/no conditions, not dates; review capacity per quarter; owners.

| Quarter | Operating model | Portfolio | In production (approved route, cumulative) |
|---|---|---|---|
| Q2 2027 | Policy v2 to the Board Risk Committee (20 April); hub hiring; catalogue v1 (31 May); contractor April–September; survey answer corrected (April) | Stops decommissioned (30 June); merges start; Kesher renewal with AI off by default | 2 (CRD-03 dispute letters, FIN-02 invoice matching) |
| Q3 2027 | Platform live (September); kit and templates v1 | Low-tier wave; CC-01's Arabic fixed | 5 (+ RET-03, OPS-02, CC-02) |
| Q4 2027 | Second evaluator; first full quarter of the three numbers | Medium-tier reviews | 10 (+ OPS-01 rollout, MTG-03, HR-02, FIN-01, CRK-01 validated) |
| Q1 2028 | Policy review; 2028 plan | High-tier queue ordered | 14 (+ CRD-01, CMP-01, CC-01, CORP-01) |

Gates: no low go-live without a catalogue entry and a passed kit; no medium without the hub's sign-off and, with personal data, the DPO's DPIA decision; no high without the Model Committee; no build with two owners. The other 12 kept builds have dates in Q2–Q4 2028.

Then play it. Run your design through the simulation's three years and answer its events as your plan would (shadow builds, the complaints duplicate, the supervisor's question, a resignation in MRM, a 15% cut, a drifting credit model, AI arriving in a vendor release):

[Simulation: Operating model scaler](../../simulations/operating-model-scaler/index.html?preset=crescent)

Try the budget event twice: once spreading the cut, once cutting the assistant. In the model, cutting it stalls its two dependents and ends with 33 builds in production after three years instead of 36. The simulation's expert run has 26 in production after four quarters; your plan commits to 14 by March 2028 because the simulation has no procurement, DPIA or works-committee time. Say so in the plan, and keep the plan's number.

## Watch out

- **Rules written after the list.** A stop list that matches your instincts too well will be read as politics. Date the rules and read them to Irina and Dalit first.
- **Stopping by vote.** Every stop has evidence the owner can check; nobody's build is stopped because a committee preferred another.
- **Merging into the louder unit.** The evidence picks the owner; the other unit keeps its channels, its report and a side-by-side.
- **Merging patterns.** Five Q&A assistants are five content owners. Share the road, not the build.
- **Cutting what something else stands on.** Fill `depends_on` before any cut; the register did not.
- **A plan with dates and no gates.** "Go-live in Q3" is a wish; "go-live when the kit passes and the catalogue entry exists" is a gate.
- **Quoting the simulation's numbers as the plan.** It is an educational model; the plan carries your commitment and your reasons.

## Your turn

### Inputs

- `triage-sheet.csv` (Track A) or `triage.py` (Track B) in the module download; the data room's `ai/`, `procurement/vendor-contracts-ai.csv`, `people/`, `company/cfo-budget-review-2027-01-12.md`.
- Your operating-model paper (15.4).
- Personas: [Hagit](../../labs/module-15/personas/hagit-retail.md) (the merge), [Karim](../../labs/module-15/personas/karim-cards.md), [Dalit](../../labs/module-15/personas/dalit-coo.md) (the assistant); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [use-case scorecard](../../templates/use-case-scorecard.md), [decision record](../../templates/decision-record.md), [roadmap](../../templates/roadmap.md), [phase-1 plan](../../templates/phase-1-plan.md), [AI intake register](../../templates/ai-intake-register.md).
- [Simulation: Operating model scaler](../../simulations/operating-model-scaler/index.html?preset=crescent).

### Steps

1. Write and date the five rules.
2. Fill the triage sheet for all 43 rows: copy, tier, issues, family, action, merge target.
3. Write the stop list with the evidence for each and the decommissioning dates the contracts set.
4. Write the merge list with the kept build, one owner and what the other unit keeps; rehearse the conversation with Hagit.
5. Fill the dependencies you can find and decide the assistant, with its condition.
6. Compute the review load under at least three designs and the 2027 money; check that it meets the CFO's ₪3.02M.
7. Write the 12-month plan by quarter with gates, capacity and owners; list the 12 builds that come after March 2028.
8. Play your design in the simulation for 12 quarters; record the numbers after 4 and 12 quarters and what you changed.

**Track B (Python):** run `triage.py`, compare its actions with your sheet, and explain every difference; run it with `--llm` (or `mock`) and note one pair where the model's view differs from yours and who is right.

### Time

180 minutes: 15 for the rules, 50 for the triage, 20 for stops and merges, 20 for the Hagit rehearsal, 15 for the assistant, 20 for load and money, 25 for the plan, 15 for the simulation.

### Done when

- [ ] The rules are dated and were read to the CRO and the sponsor before you applied them.
- [ ] All 43 rows have an action; 40 builds are counted; each stop has evidence an owner can check.
- [ ] Each merge has one owner chosen by evidence, and the other unit's needs are written down.
- [ ] The two dependents of the assistant are in the catalogue, and the assistant decision has a condition.
- [ ] The review load is shown under at least three designs, and the 2027 money meets the CFO's target without cutting the assistant.
- [ ] The plan has yes/no gates, a number per quarter, owners, and the builds that come after March 2028.
- [ ] Your simulation run is recorded with numbers, including the budget event played both ways.

<details><summary>Reference answer</summary>

The full set is `labs/module-15/expert/05-triage-and-scale-plan.md` (module download).

**Actions on 43 rows (`triage.py`):** clean 3, stop 10, merge 4, route 24, fix then route 2 (TRS-01: no baseline; CC-01: two owners). Kept 26: low 12 (RET-03, MTG-03, CRD-03, CORP-02, TRS-01, OPS-01, OPS-02, CC-02, DIG-03, HR-02, FIN-01, FIN-02), medium 8 (RET-04, MTG-01, CRD-01, CRK-02, CMP-01, OPS-03, CC-01, FIN-03), high 6 (CRD-02, SME-03, CORP-01, TRS-02, TRS-03, CRK-01). SME-03's backtest uses 2024 data from before the rate changes: re-test on 2026 data before validation (in the simulation, this is the model that drifts in 2029).

**Patterns among the 26:** Q&A over documents 5, drafting 5, extraction and matching 5, scoring 7, summarisation 3, search 1 — one template each.

**Conversation with Hagit (second rehearsal):** opened with Retail's complaint volume (10,011 in 2026) and the themes report she cares about, then Cards' 0.91 on 300 of the bank's own complaints against Mishov's figure on its own benchmark, then what Retail keeps (its channels, the themes report, a two-month side-by-side, branch call summaries later). She asked who owns the themes report: Retail does; the build is Cards'.

**Assistant:** kept, staged; condition 50% weekly use of assigned seats by 30 September; `depends_on` filled for OPS-02 and CC-02.

**Money:** all AI spend ₪20.13M → ₪16.57M; saving ₪3.57M vs ₪3.02M; central ₪9.995M; unit lines ₪6.57M.

**Plan:** 2 by 30 June, 5 by 30 September, 10 by 31 December, 14 by 31 March 2028; the other 12 dated in Q2–Q4 2028.

**Simulation (crescent, the expert's design and answers; educational model):** after 4 quarters 26 in production, 6 stopped, 4 merged, 7 waiting, 0 incidents, 0 shadow, ₪10.38M; after 12, 36 in production, 10 stopped, 0 waiting, 2 incidents, ₪29.78M of ₪30.94M. Same, but cutting the assistant: 2 builds stalled, 33 in production after 12 quarters. Kept in the plan: 14 by March 2028.

</details>

## References

- Bank of Israel, [Directive 369](https://www.boi.org.il/media/ggpbdtqp/369_en.pdf): one owner per model (§24), the inventory (§30–32), periodic review (§67).
- Bank of Israel, [circular C-06-2571](https://boi.org.il/media/w10dtldz/h2571_en.pdf), Directive 359A: the board's outsourcing policy and management's oversight of outsourced activities; contract changes go through procurement.
- Inter-ministerial team, [AI in the financial sector, final report](https://www.boi.org.il/media/rh0bejl4/aireport.pdf) (December 2025, Hebrew), bias and discrimination (pp. 103–110): proxies and outcome testing. Recommendations; employment questions go to counsel.
- IBM, [Lead AI Transformation certificate](https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution): pilot isn't scale, scale / sustain / retire, sequence for absorption (named, not re-taught).
- [Simulation: Operating model scaler](../../simulations/operating-model-scaler/index.html?preset=crescent) (educational model).
- Field kit: [03.4 · Scoring with evidence](../module-03/lesson-04.md), [03.8 · The roadmap](../module-03/lesson-08.md), [07.2 · Scale, fix or stop](../module-07/lesson-02.md), [07.8 · Running phase 1](../module-07/lesson-08.md).
- Templates: [use-case scorecard](../../templates/use-case-scorecard.md), [decision record](../../templates/decision-record.md), [roadmap](../../templates/roadmap.md), [phase-1 plan](../../templates/phase-1-plan.md), [AI intake register](../../templates/ai-intake-register.md).
- Earlier: [15.4 · The hard part](lesson-04.md). Next: [15.6 · Readout and debrief](lesson-06.md).
