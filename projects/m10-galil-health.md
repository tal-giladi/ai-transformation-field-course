# Galil Health

Run the whole engagement at Galil Health, a network of 14 community clinics in northern Israel, as an outside consultant to its CIO: from the first call to the steering decision and the handover. The CEO has promised the board "an ambient scribe for every doctor by Q2" and likes the vendor whose demo impressed everyone; your job is to find out what Galil's documentation problem really is, run a vendor selection on evidence from Galil's own conditions, and bring one recommendation, with contract terms and a clinician pilot, to the steering committee. This is module 10's practical: one integrated deliverable set, every document consistent with every other.

## The brief

Read [the engagement brief](../labs/module-10/brief.md) (in the module download). In short: 10 weeks, 15 November 2026 – 21 January 2027; ₪198,000 + VAT in three phases with exits on 3 December and 31 December; a proof-of-concept budget of up to ₪75,000; you report to Igor Shapiro (CIO); the steering group is the CEO, CIO, CMO, CFO, counsel and DPO, and the Head of Nursing. The data room is `labs/module-10/data-room/` (start with its [INDEX](../labs/module-10/data-room/INDEX.md)); the people are in `labs/module-10/personas/` ([the cast](../labs/module-10/personas/README.md)); the proof-of-concept results arrive in `labs/module-10/poc/` in lesson 10.4.

The fixed points: phase-1 readout Thursday 3 December; RFP sent Sunday 6 December, answers by 20 December; PoC recordings 8–10 December, results and exit point 2 on Thursday 31 December, the day ScribeWave's quoted discount expires; scoring, terms and pilot plan 3–14 January; steering committee Tuesday 19 January 2027; handover Thursday 21 January.

## Deliverables

| # | Deliverable | Template | Lesson |
|---|---|---|---|
| 1 | **Engagement charter** with decision rights (clinical safety, patients' information, money, vendor, integration), SOW with exits, scope, first-read sheet and access request | [engagement charter](../templates/engagement-charter.md), [scope boundary](../templates/scope-boundary.md), [data-room first read](../templates/data-room-first-read.md), [access request pack](../templates/access-request-pack.md) | [10.1](../lessons/module-10/lesson-01.md) |
| 2 | **Findings memo** with measured, reported and inferred labels: the language field tested, the documentation-time baseline, where the burden sits, the shadow-AI census, the earlier trial | [findings memo](../templates/findings-memo.md), [stakeholder map](../templates/stakeholder-map.md), [interview guide](../templates/interview-guide.md), [data profile](../templates/data-profile.md) | [10.2](../lessons/module-10/lesson-02.md) |
| 3 | **Baseline sheet, opportunity map with plain fixes, requirements, netted claim and one-page case** | [opportunity map](../templates/opportunity-map.md), [use-case scorecard](../templates/use-case-scorecard.md), [ROI model](../templates/roi-model.md), [decision-ready case](../templates/decision-ready-case.md) | [10.3](../lessons/module-10/lesson-03.md) |
| 4 | **RFP, claim read-backs, regulatory map for counsel, PoC protocol and results, the 31 December note** | [RFP for AI vendors](../templates/rfp-for-ai-vendors.md), [claim read-back](../templates/claim-read-back.md), [vendor PoC protocol](../templates/vendor-poc-protocol.md), [regulatory map](../templates/regulatory-map.md) | [10.4](../lessons/module-10/lesson-04.md) |
| 5 | **Decision paper**: evidence scores with reasons beside demo scores, sensitivity, must-have gate, three-year cost, contract terms, steps before signing, clinician pilot plan with stop rules and consent | [pilot charter](../templates/pilot-charter.md), [value measurement plan](../templates/value-measurement-plan.md), [human-review design](../templates/human-review-design.md), [decision-ready case](../templates/decision-ready-case.md) | [10.5](../lessons/module-10/lesson-05.md) |
| 6 | **Steering pack** (one recommendation, a recommend-against), **integration check**, notes of the **hardest-finding rehearsal**, **decision record** and **handover pack** outline | [steering pack](../templates/steering-pack.md), [integration check](../templates/integration-check.md), [decision record](../templates/decision-record.md), [handover pack](../templates/handover-pack.md) | [10.6](../lessons/module-10/lesson-06.md) |

The scoring sheet is `labs/module-10/rfp-scoring-sheet.csv` (module download).

## Steps

1. Read the brief and the data room's INDEX; write the charter with decision rights and the first-read sheet; interview Igor (10.1).
2. Interview at least two of Wasim, Elena, Suha and Fatma; test the language field; measure documentation time and where it sits; run the shadow-AI census; write the findings memo (10.2; Track B: `discovery.py`).
3. Build the baseline sheet; map the candidates including the plain fixes; write requirements; net "two hours a day" with Eyal; write the case; see Shlomit privately (10.3).
4. Lock the criteria; write the RFP; read back every claim; interview Yoni and Hagit; write the regulatory map; write the PoC protocol; score the PoC; run the `vendor-rfp` simulation once; write the 31 December note (10.4; Track B: `poc_score.py`).
5. Score the vendors with reasons and test the weights; apply the must-haves; cost three years; write the contract terms and the steps before signing; write the pilot plan with Wasim's stop rules and consent wording; write the decision paper (10.5).
6. Write the steering pack; run the integration check; rehearse the hardest finding with Shlomit twice; run the meeting; write the decision record and the handover outline (10.6).
7. Score your set with the rubric below **before** you open the hidden truth and the expert set in 10.6; then compare.

Time: about 4 hours beyond the lessons' own exercises, most of it in steps 6 and 7.

## Self-assessment rubric

| Criterion | What "strong" looks like | What "weak" looks like |
|---|---|---|
| Mandate and role | The CIO's objective read back; the CEO's ask written as the claim tested; decision rights name the CMO, the DPO and counsel, and the steering group; the consultant designs and scores, never selects or negotiates | The consultant "selects the vendor"; the CEO's ask adopted as the objective; legal and clinical questions answered by the consultant |
| Discovery | The language field tested against a second source; documentation time measured from the audit log with a definition card; the burden cut by language and clinic; people protected; shadow use found from three sources and reported without names | KPI and survey figures repeated; a network average; a doctor named; vendor numbers used as the baseline |
| The real problem | Languages and relatives identified as where the burden and the risk sit; the plain fixes (the language field, matched booking, the recording instruction) in the case | The scribe treated as the whole answer; Hebrew performance treated as the main criterion |
| Netting | "Two hours" set against 112 measured minutes; capacity on its own line; the retention condition for cash stated as an assumption; the cost of the expensive error named | Minutes converted to shekels; the vendor's claim accepted or ridiculed without Galil's numbers |
| The RFP and claims | Criteria locked and dated; the RFP asks for measurement conditions, makes the PoC part of the bid, lists must-haves with reasons and asks for intended purpose in writing; every claim read back under its conditions | "Accuracy %", "languages supported", "confirm you comply"; the demo scored again |
| Law and regulation | Health information, data security, the Patient's Rights Law, the Ministry's cloud circular, the funds' agreements and the medical-device question mapped with sources and routed to counsel and the DPO; open questions kept open | "It's legal" or "it's a medical device" in the consultant's voice; a vendor's compliance statement accepted; the health funds missed |
| Proof of concept | Synthetic visits only; hard cases by design; two runs; thresholds dated before results; every rate with its count and interval; a pass read as "fit to pilot" | Real patient audio; thresholds after results; one accuracy figure; a pass read as "safe" |
| Decision | Evidence scores with reasons beside demo scores; a sensitivity check; must-haves as a gate; three-year cost for the right number of seats; contract terms tied to Galil's obligations | A score without reasons; a must-have traded for price; 120 seats because the quote said so |
| Pilot plan | Two clinics including an Arabic-speaking one; a comparison; a weekly audit; gate thresholds; the CMO's stop rules; consent shaped by patients' conditions; the staff committee consulted; a date for the shadow users | A pilot with no comparison; stop rules written by the consultant; the vendor's consent text; nurses forgotten |
| Recommendation and follow-through | One recommendation; the recommend-against on the front page with evidence; a sentence for the CEO's board; a decision record with owners and dates for every condition; a handover tested by the owner | A menu; the evidence in an annex; "approved, subject to approvals"; a binder and a phone number |
| Integration | Dates traced to their dependencies (Fund A before the pilot); controls traced to hours and budget; numbers identical across all six deliverables | A pilot that starts before its approval; an audit nobody pays for; three different omission rates |

## Model answer

<details><summary>Model answer</summary>

The expert's deliverable set is in the module download, `labs/module-10/expert/` ([README](../labs/module-10/expert/README.md)):

- [01 · Engagement charter](../labs/module-10/expert/01-engagement-charter.md)
- [02 · Findings memo](../labs/module-10/expert/02-findings-memo.md)
- [03 · Baselines, requirements and the one-page case](../labs/module-10/expert/03-baselines-and-case.md)
- [04 · RFP, claim read-backs and the proof of concept](../labs/module-10/expert/04-rfp-claims-and-poc.md)
- [05 · Vendor scoring, contract terms and the clinician pilot plan](../labs/module-10/expert/05-vendor-decision-and-pilot-plan.md)
- [06 · Steering readout, decision record and handover](../labs/module-10/expert/06-steering-readout.md)

Every number computed from the data room and the PoC files is real and reproducible with `discovery.py` and `poc_score.py`. Vendors, prices and the PoC are fictional. Lesson 10.6 reveals what was really going on at Galil and three futures; read them only after scoring yourself.

</details>
