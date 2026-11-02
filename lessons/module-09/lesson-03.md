---
id: "09.3"
module: 9
minutes: 18
practice_minutes: 120
prerequisites: ["09.2", "02.4", "03.1", "03.7", "03.9"]
objectives:
  - "Reconcile three conflicting cycle-time baselines and agree one definition with the people who will challenge it."
  - "Decompose the claimant's wait into segments and name the bottleneck and its cause from the data."
  - "Screen the candidates, including one that needs no AI, and net every benefit claim into measured, directional or assumed money."
  - "Write a one-page case that de-scopes the sponsor's favourite idea with evidence."
volatility: concept
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera) — course 5, AI Business Cases and ROI Models (net the claim; measured, directional, assumed)"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "Capital Market, Insurance and Savings Supervisor — circular 2016-9-9 (5 July 2016): s. 8(a)(6) further documents within 14 business days; s. 8(b) notice within 30 days of having all documents"
    url: https://www.gov.il/BlobFolder/dynamiccollectorresultitem/regulation-1101/he/regulation_h_2016-9-9.pdf
last_verified: "2026-11-02"
---

# 09.3 · Diagnosis

The proposal promises to cut a 10.5-day handling time by 30%. The claimant in 09.2 waited 44 days. In this lesson you find out which number is true for whom, where the days actually go, what a winter peak does to any plan, and which candidate deserves money. At the end you have measured baselines that the Chief Actuary signs, a shortlist in which the best first move needs no AI, and a one-page case that tells your sponsor her pilot is not the first thing to do.

## The situation

Sunday 22 – Thursday 26 November 2026. On Sunday Ilana signed the change request from your interim
memo: Fraud Insight's auto-referral is off, F08 and F09 are disabled, and the SIU sees the score only
as a review aid. She took it well and asked for "the positive plan" by Thursday.

Two things are now true at once: the sponsor trusts you a little more, and her proposal is weaker.
IBM's business-case course asks you to net every claim and label each number measured, directional
or assumed. Here you build the numbers those labels go on.

## What to do

### Step 1 — Put the three baselines side by side

[02.4](../module-02/lesson-04.md) warned that three systems give three baselines. At Meridian
(reproduce with `python baselines.py --section baselines`):

| Measure | Definition | Source | Value |
|---|---|---|---|
| Dashboard "handling time" | File complete → decision, SIU claims excluded | BI, whole company | 10.5 days mean year to date (on the sample: mean 10.6, median 8.1, n=743; 94.9% within 30 days) |
| Kalanit cycle | Registered → closed | Register sample | median 41.1 days (n=787) |
| **Claimant's wait** | **Reported date → last payment to the claimant or garage** | Register + ERP payments | **median 32 days**, p75 46, p90 64 (n=696 claims paid in 2026) |
| Direct-channel check | First CRM contact → last payment | CRM + ERP, May–October | median 25 days (n=165) |

None of them is wrong; they measure different things. The dashboard measures the Supervisor's
30-day clock, which runs from the day the insurer has all the documents it asked for (circular
2016-9-9, s. 8(b)); it is a compliance number and should stay, under an honest name. Kalanit's closure
is administration: nobody waits for it. The CRM check is lower because it misses agents' claims, the
slower half. The objective you read back in 09.1 is about the claimant, so the baseline is the
claimant's wait.

A baseline is only agreed when the person who will challenge it signs the definition. Take it to
[Natalia Gurevich](../../labs/module-09/personas/natalia-chief-actuary.md), the Chief Actuary: she uses
the same definition for reserving, and she will tell you which other numbers she will attack.

### Step 2 — Decompose the wait

Median segments, claims decided January–October 2026 (`--section segments`):

```mermaid
flowchart LR
  A[Reported] -->|2.5 d intake| B[Registered]
  B -->|1.1 d| C[First documents list]
  C -->|12.8 d document chase, mean 18.5| D[File complete]
  D -->|8.3 d| E[Decision]
  E -->|1.6 d| F[Paid]
```

Intake typing, the thing the proposal automates, sits inside the first 2.5 days. The document chase is
five times longer. The number of rounds explains it: median wait 24 days with one round of document
requests (n=380), 41 with two (n=219), 60 with three or more (n=97).

### Step 3 — Find the cause, not just the bottleneck

Why are there rounds? The data and the interviews give three causes (`--section documents`):

1. **The day-one list is late.** The complete list goes out on the day of the report for 5.6% of
   claims; median four days (manual 3.2 says the same day).
2. **The day-one list is incomplete in practice.** 45.4% of the documents asked for in round 2 or
   later were on the claim type's standard list. They should have been asked for on day one. For
   travel medical claims the list itself is wrong: it never asks for a medical report in Hebrew or
   English, so any non-English clinic means a second round (Marina, 09.2).
3. **Follow-ups are slow.** 13.7% of follow-up requests went out more than 14 working days after the
   previous documents arrived. Whether a given case breaches the circular's 14 business days "from
   when the need became clear" is not something an export can decide; it is a question for compliance.

A cause you can name is a cause you can fix. Two of the three need no technology at all.

### Step 4 — Put the peak on the calendar

`--section peak` multiplies the sample by 40:

| Month | Claims (company) | Home claims | Intake lag (median days) |
|---|---|---|---|
| Jan 2025 | 5,120 | 2,520 | 5.6 |
| Jan 2026 | 5,080 | 2,200 | 5.6 |
| May–Oct 2026 (typical month) | ≈ 2,550 | ≈ 520 | 1.5–1.6 |

The proposed pilot window (1 December – 28 February) is the busiest quarter of the year, with storm
weeks on top (home claims ×4–5 for a few days). Yusuf's team leads cannot review a pilot then. Any
change that needs handlers' attention starts in March; a change that removes work (a complete list on
day one) can start in January.

### Step 5 — Map and screen the candidates

Use the [opportunity map](../../templates/opportunity-map.md) ([03.1](../module-03/lesson-01.md)) with
three feeds: the request (Ilana's proposal), AI already in use (the 9.4 modules, shadow translation)
and the goal (claimants paid sooner). Then decide per step whether it needs AI at all
([03.2](../module-03/lesson-02.md)) and run the fast screen ([03.3](../module-03/lesson-03.md),
[use-case scorecard](../../templates/use-case-scorecard.md)):

| Candidate | Type | Screen |
|---|---|---|
| A. Complete documents list on day one: mandatory fields in the agents' portal, an intake checklist per claim type, the travel-medical list fixed, letters in the claimant's language | Process change and plain automation, **no AI** | Go, first |
| B. Extraction with a completeness check: read what arrived, pre-fill fields for the handler, list what is missing | AI assist, a person confirms | Go with conditions: offline pilot now, shadow mode after the peak |
| C. Smart Intake as it is | Vendor AI | Not as is: 3.5 + 3.3 minutes vs 6.7 without it (time study); compare with B in 09.5 |
| D. Fraud Insight on home claims; Fraud Insight Pro | Weighted rules sold as AI | Stop: proxies; labels are referrals; benefit unsourced (09.4) |
| E. A sanctioned translation tool for foreign documents | AI assist | Go, small, through the approved enterprise tool and the DPO |

### Step 6 — Net the money, and label it

[03.7](../module-03/lesson-07.md) built an ROI model that survives finance. The CFO's planning rate is
₪145 an hour for a handler; 2025 volume is 36,760 claims (sample × 40). From Claims QA's time study
(`--section money`):

| Line | Yearly | Label |
|---|---|---|
| Keying: 5.5 min a claim | ₪488k | Measured (time study n=120) |
| Finding missing documents: 6.8 min a claim | ₪606k | Measured |
| Smart Intake today: keying 3.5 + checking 3.3 vs 6.7 | ≈ ₪0 net | Measured |
| B: half the keying saved, 1.5 min of checking added | ≈ ₪110k | Directional |
| A + B: rounds from 1.62 to about 1.3, a third of the "finding" time | ≈ ₪200k | Assumed |

Then net the fraud claim. The SIU's "fraud prevented" (₪6.77M year to date) is claimed minus paid on
every closed SIU case, whatever the outcome (`python bias_test.py --outcomes`): confirmed fraud
₪2.34M, no finding ₪2.90M, claimant withdrew ₪1.54M. Samira's case shows why "no finding" is in it: her
claim was ₪16,480, she was paid ₪14,530, and the ₪1,950 difference, her deductible, is counted as fraud
prevented. Then read back the ₪20M ([04.8](../module-04/lesson-08.md),
[claim read-back](../../templates/claim-read-back.md)): "fraud is 10% of claims paid" × ₪281M × two
thirds, the 10% from "industry studies" nobody can name. Natalia's range for undetected leakage is
₪3–6M with wide uncertainty. Nothing shows a score that finds any of it. Count ₪0, and say it is a
decision, not an oversight.

Hours are capacity, not cash, until Yusuf decides what they buy (the six winter temps, overtime).

### Step 7 — Write the one-page case, and tell Ilana first

The [decision-ready case](../../templates/decision-ready-case.md) from [03.9](../module-03/lesson-09.md):
one ask, the evidence with labels, the cost of waiting, what a "no" means. Her favourite idea (the winter
pilot, Pro) is not in it. Tell her before the paper goes anywhere, in person, answer first: what you
recommend, the one number that decided it, what her proposal still gets (the extraction pilot is her
"automate intake", done in a way that will survive the committee).

## Watch out

- **Picking the baseline that flatters.** Ten days is easier to cut by 30% than 32 days is. The
  objective decides the baseline, not the target.
- **Throwing away the dashboard.** It measures the regulatory clock; keep it, renamed, next to the
  claimant's wait.
- **Automating the step that is not slow.** Intake typing is 2.5 days of 32. A pilot that only speeds
  it up cannot move the claimant's wait much.
- **Counting activity as savings.** "Fraud prevented" includes deductibles and people who gave up.
- **Planning through the peak.** A change that needs attention in January will get none.
- **Letting the sponsor read the de-scope in a paper.** Tell her first, with the alternative.

## Your turn

### Inputs

- Data room: `claims/claims_register_sample.csv`, `claims/doc_requests.csv`, `finance/claim_payments.csv`,
  `claims/crm_contacts.csv`, `ops/intake-time-study-2026-10.csv`, `siu/siu_case_log.csv`,
  `reports/claims-kpi-dashboard-2026-10.md`, `company/finance-summary.md`,
  `plans/pilot-proposal-2026-11.md`, `vendor/email-kalanit-fraud-insight-pro-2026-10-20.md` (module download).
- Persona: [Natalia Gurevich](../../labs/module-09/personas/natalia-chief-actuary.md) (transcript in the
  module download); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [opportunity map](../../templates/opportunity-map.md), [use-case scorecard](../../templates/use-case-scorecard.md),
  [ROI model](../../templates/roi-model.md), [claim read-back](../../templates/claim-read-back.md),
  [decision-ready case](../../templates/decision-ready-case.md).

[Simulation: Pilot economics](../../simulations/pilot-economics/index.html?preset=generic)

The `generic` preset is a document-processing queue; replace its inputs with Meridian's (volume ≈
3,060 claims a month, ₪145 an hour, your keying and checking minutes) and watch where checking time
eats the saving.

### Steps

1. Compute the three baselines (Track A: pivot tables on the register and the payments ledger, joined
   on `claim_id`; the claimant's wait is `paid_date` minus `reported_date`). Write each definition.
2. Interview Natalia: agree the definition; find out which numbers she will challenge.
3. Decompose the wait into the five segments; compute the wait by number of rounds.
4. Find the causes of rounds: same-day lists, standard-list share in later rounds, slow follow-ups.
5. Make the monthly volume table and mark the proposed pilot window.
6. Screen five candidates; at least one must end as "no AI".
7. Net the money with labels, including the fraud decomposition and the ₪20M read-back.
8. Write the one-page case; write the two sentences you will say to Ilana first.

**Track B (Python).** `python baselines.py` prints every table in this lesson (sections `baselines`,
`segments`, `documents`, `peak`, `money`) and `python bias_test.py --outcomes` the fraud decomposition.
Python is worth it here because the joins (register × payments × CRM, with FNOL rows matched on policy
when the claim number is missing) are easy to get subtly wrong in a spreadsheet, and the committee
will ask for the same numbers again in January.

### Time

120 minutes: 40 for the baselines and segments, 20 for Natalia, 20 for the screen, 25 for the money,
15 for the case.

### Done when

- [ ] Three baselines with definitions, sources and n; one chosen, with the reason and who agreed it.
- [ ] The wait is decomposed and the bottleneck has named causes from the data.
- [ ] The peak is on the plan, with a start date after it for anything that needs handlers' attention.
- [ ] At least one candidate is "no AI", and it is first.
- [ ] Every money line has a label; fraud is counted only when confirmed; the ₪20M has a read-back.
- [ ] The case has one ask, a cost of waiting and what a "no" means.

<details><summary>Reference answer</summary>

Full version: `labs/module-09/expert/03-baselines-and-case.md` (module download).

**Baseline agreed with Natalia (23 November).** The claimant's wait, reported → last indemnity payment:
**median 32 days**, p75 46, p90 64 (n=696, 1-in-40 sample, paid in 2026). The dashboard number stays,
renamed "time to decision after a complete file" (mean 10.5 days). This also answers internal audit's
open 2025 finding once BI adds it to the dashboard.

**Bottleneck and causes.** Document chase 12.8 days median (mean 18.5) of 32; one round 24 days, two
41, three or more 60. Causes: complete list sent the same day for 5.6% of claims; 45.4% of later
requests were on the standard list; the travel-medical list lacks a translated medical report; 13.7%
of follow-ups more than 14 working days after the previous documents.

**Shortlist.** A (documents list on day one, no AI) from 4 January; B (extraction with a completeness
check) offline now, shadow after the peak; E (sanctioned translation) small. Not as is: C. Stop: D.

**Money.** Keying ₪488k a year and finding missing documents ₪606k (measured); B ≈ ₪110k net
(directional); A + B ≈ ₪200k (assumed); fraud ₪0 counted (confirmed fraud ₪2.34M year to date exists;
no evidence a score adds to it; the ₪20M has no source).

**Front page.**

> **Ask.** Approve ₪155,000 of the ₪240,000 for (A) a day-one documents list from 4 January and (B) an
> extraction-and-completeness pilot, offline now, in shadow mode from mid-March, Hebrew, Russian and
> English first. Do **not** extend Fraud Insight or buy Pro; its auto-referral is off since 22 November.
>
> **Why.** Claimants wait a median 32 days, 12.8 of them chasing documents; 45% of later requests ask
> for things that should have been asked for on day one (*measured*).
>
> **Cost of waiting.** Each month about 1,380 claims (45% of ≈ 3,060) need a second round.
>
> **What a no means.** The winter runs as today; the documents list is fixed anyway (no AI needed).

**To Ilana first:** "I recommend we fix the documents list in January and test extraction properly after
the peak; the winter pilot would speed up the 2.5 days of intake, but the claimant's 32 days are mostly
documents. Your 'automate intake' is in the plan, as a pilot the committee can approve."

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting), course 5 (net the claim; measured, directional, assumed; named, not re-taught).
- Supervisor of the Capital Market, Insurance and Savings, [circular 2016-9-9](https://www.gov.il/BlobFolder/dynamiccollectorresultitem/regulation-1101/he/regulation_h_2016-9-9.pdf), s. 8(a)(6) and 8(b) (Hebrew). Compliance with the circular is for the compliance officer and counsel to judge.
- Field kit: [02.4 · Measuring a baseline from exports](../module-02/lesson-04.md), [03.1 · The opportunity map](../module-03/lesson-01.md), [03.2 · Agent or not](../module-03/lesson-02.md), [03.3 · The fast screen](../module-03/lesson-03.md), [03.7 · The ROI model that survives finance](../module-03/lesson-07.md), [03.9 · The decision-ready case](../module-03/lesson-09.md), [04.8 · Vendor and claim due diligence](../module-04/lesson-08.md).
- Templates: [opportunity map](../../templates/opportunity-map.md), [use-case scorecard](../../templates/use-case-scorecard.md), [ROI model](../../templates/roi-model.md), [claim read-back](../../templates/claim-read-back.md), [decision-ready case](../../templates/decision-ready-case.md).
- Simulation: [pilot economics](../../simulations/pilot-economics/index.html?preset=generic).
- Next: [09.4 · The hard part: a regulated deployment verdict](lesson-04.md).
