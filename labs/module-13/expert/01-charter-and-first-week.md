# 01 · Mandate memo and first week

To: Dalia Mizrahi, VP operations. From: operations-excellence manager. Sunday 10 January 2027; agreed Monday 11 January (Dalia's corrections in italics).

## The entry-role table (internal lead with a day job)

| | What it means here | What goes into the mandate |
|---|---|---|
| Who gave the ask | The owner and CEO, in front of the management team | The mandate is Dalia's (sponsor); Amnon gets a one-page note every two weeks, copy Dalia |
| Budget | None of mine. ₪1.5M line 7400-210, released by the CFO and the CEO | "No commitment and no promise to any supplier by the project lead"; anything above ₪50,000 to Orit and Amnon |
| My history | I designed the ProdTrack reason codes and ran the 2025 tablets project the works committee objected to | My own data is audited like everyone else's; I say so in the findings; Lina re-checks my numbers |
| The floor knows me | Access and trust, but also old grievances | Workers' committee met before any vendor visit; nothing with personal identifiers leaves the plant |
| Day job continues | OEE reporting (Lina until March) and the Arava plan (mine) | The Arava corrective-action plan is part of the deliverable, not a parallel project |
| I stay | Whatever is set up, I or my team maintain | Every part has a named owner who is not me by the end of June |

## Objective (read back and corrected)

"By 23 March, find out what causes the unplanned downtime that makes Kinneret late to Arava, and test whether predictive maintenance, or something else, would reduce it; bring management one recommendation with costs and dates, *and give Dalia something for the Arava plan by 31 March whatever happens with AI*."

**The stated ask, recorded as the claim this work tests:** "Predictive maintenance with AI, starting with Predictiva's platform on all 40 machines."

## Done means

- A decision in the minutes of the 23 March management meeting, with an owner and a date for each part.
- Every number labelled measured, directional or assumed; downtime baselines from ProdTrack with definitions written down.
- Predictive maintenance judged against criteria written **before** looking at the vendor's evidence.
- Nothing installed, no data sent outside Kinneret, nothing on the floor that changes work without the works committee consulted first (local agreement clause 14).
- Any safety finding escalated the same day to the safety officer, not held for the readout.

## Scope

In: unplanned downtime at both plants (machines, moulds, material, waiting), maintenance records and how they are made, sensors, parts availability, the Arava plan. Out: ERP replacement, capex on new machines (Orit's line 8200), quality systems beyond the scrap data (Rotem), anything with cameras. Revisit after 23 March.

## Advisory boundary

I answer: what the data says, what it would take, options and costs. I route: safety and statutory examinations → Yaakov Dahan (safety officer); workers' consultation and anything on monitoring → Michal Aharon (HR) and the works committee, legal readings to the company's labour lawyer; contracts and money → Orit; employee personal data → HR; Plant G decisions → Eli Peretz.

## First read (excerpt)

| Statement | Where | Sort | Why |
|---|---|---|---|
| "Plant G repairs 1.6× faster" (3.5 h vs 5.7 h) | `company/kpi-deck-2026-12-extract.md` | **Claim to test** | Footnotes 1–2: two different definitions (restart vs "ready") |
| "Breakdowns are the number one loss — and they can be predicted" | Same deck, slide 5 | **Claim to test** | Breakdowns = machine + mould (footnote 4); split them |
| PM compliance 97% | `maintenance/pm-compliance-report-2026.md` | **Claim to test** | Counts closed work orders; "all PMs closed by end of September" |
| OTIF 81% vs 95%; 14 of 22 notices "machine breakdown" | `company/arava-letter-2026-12-14.md` | **Verified** (as the customer's view) | The reasons are Kinneret's own notices: check them |
| "Plant G data: ready" | `vendor/predictiva-questionnaire-plant-g.md` | **Claim to test** | Same word as the deck; what does "ready" mean at Galil? |
| "Up to 50% less downtime, 94% accuracy, ROI in 9 months" | `vendor/predictiva-proposal.md` | **Claim to test** | Case study is a wind farm (`predictiva-case-study.md`) |
| The vendor needs 12 months and ≥ 30 failures per mode | `vendor/predictiva-onboarding-guide-extract.md` | **Verified** (as their requirement) | Compare with our records in week 2 |
| Failure codes exist in MaintPro | `maintenance/failure-codes.csv` | **Verified** (the list exists) | Whether they are used: unverifiable until profiled |
| Condition monitoring on 3 of 26 Plant K machines | Deck slide 4, `assets/asset-register-plant-k.csv` | **Verified** | 0 of 14 at Plant G |
| No monitoring without agreement (clause 15) | `hr/local-agreement-2021-extract.md` | **Verified** | The vendor offers cameras |

Missing → access request: Danny's 22 late-shipment notices; Plant G's Excel original and Shlomi's machine numbering; the supervisors' night-call log; the historian for K21–K23; the tooling department's mould list; the ERP stores extract; IT's listing of the maintenance drive; the safety officer's periodic-examination register for both plants; HR's languages table.

## First week

Sun 10: first read, this memo. Mon 11: Dalia (mandate), access requests. Tue 12: Amnon, 15 minutes. Wed 13: ProdTrack and MaintPro exports, first profile. Thu 14: Rotem (scrap data, the October 8D reports), Danny (notices), first note to Amnon. Next week: Vladi (Sun 17), night shift (Tue 19), Plant G (Wed 20), Khalil informally (Thu 21).

Risks to the work: Amnon signs a letter of intent at the 15 February presentation (mitigation: note to Amnon before it, the vendor read-back); my own codes are part of the problem (mitigation: say so first).

## Note to Amnon (Thursday 14 January)

"Amnon, the work is aimed at what you said on Tuesday: Arava back to 95%. By 23 March you'll have one page: what we do, what it costs, what it gives Arava, with dates. We're evaluating Predictiva properly, on our own data, including at their presentation on 15 February. Nothing is signed or promised to any supplier until that meeting. Next note: 28 January."
