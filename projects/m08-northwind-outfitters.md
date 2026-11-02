# Northwind Outfitters

Run the whole engagement at Northwind Outfitters, a 450-person Israeli online retailer of outdoor gear, as an outside consultant: from the call with the COO to the steering decision and the handover. The CEO wants "a chatbot that replaces half of support by Q2"; your job is to find out, with Northwind's own data and people, what AI should do in its customer service in 2027, test a pilot if one is justified, and bring one recommendation to the steering committee. This is module 8's practical: one integrated deliverable set, every document consistent with every other.

## The brief

Read [the engagement brief](../labs/module-08/brief.md) (in the module download). In short: 10 weeks, 8 November 2026 – 14 January 2027; ₪222,000 + VAT in three phases with exits on 26 November and 3 December; pilot tooling up to ₪60,000; you report to Orly Ben-David (COO); the steering group is the CEO, COO, CFO, head of customer service, counsel and the head of IT and BI. The data room is `labs/module-08/data-room/` (start with its [INDEX](../labs/module-08/data-room/INDEX.md)); the people are in `labs/module-08/personas/` ([the cast](../labs/module-08/personas/README.md)); the pilot files are in `labs/module-08/pilot/`.

The fixed points: phase-1 readout Thursday 26 November; Black Friday 27 November; decision paper Thursday 3 December; policy draft to counsel 7 December, marked up 17 December; offline eval report Thursday 7 January; steering committee Tuesday 12 January 2027; handover Thursday 14 January. The Verbalo renewal notice is due 1 April 2027; the board approves a 2027 budget in late January that assumes 21 agents from April.

## Deliverables

| # | Deliverable | Template | Lesson |
|---|---|---|---|
| 1 | **Engagement charter** with SOW outline (phases, exits, change control), entry-role table, advisory boundary, first-week plan, first-read sheet and access request | [engagement charter](../templates/engagement-charter.md), [scope boundary](../templates/scope-boundary.md), [data-room first read](../templates/data-room-first-read.md), [access request pack](../templates/access-request-pack.md) | [08.1](../lessons/module-08/lesson-01.md) |
| 2 | **Findings memo** with measured, reported and inferred labels; the repeat-contact baseline, like-for-like AHT and the containment test; interview notes for at least two people | [findings memo](../templates/findings-memo.md), [stakeholder map](../templates/stakeholder-map.md), [interview guide](../templates/interview-guide.md) | [08.2](../lessons/module-08/lesson-02.md) |
| 3 | **Baseline sheet, opportunity map and screen, one-page case**, netting the CEO's claim and your own | [opportunity map](../templates/opportunity-map.md), [use-case scorecard](../templates/use-case-scorecard.md), [ROI model](../templates/roi-model.md), [decision-ready case](../templates/decision-ready-case.md) | [08.3](../lessons/module-08/lesson-03.md) |
| 4 | **Decision paper**: who answers each contact type, the liability read (attributed to counsel), the returns-policy outline with business choices marked, the vendor claim read-back and contract actions | [decision-ready case](../templates/decision-ready-case.md), [regulatory map](../templates/regulatory-map.md), [risk register](../templates/risk-register.md), [claim read-back](../templates/claim-read-back.md) | [08.4](../lessons/module-08/lesson-04.md) |
| 5 | **Pilot charter, test-set spec and eval report** for agent-assist on the 2,000 tickets: thresholds dated before results; rules, LLM and hybrid compared with today; negative tests; blind ratings; cost and time labelled | [pilot charter](../templates/pilot-charter.md), [test-set spec](../templates/test-set-spec.md), [eval report](../templates/eval-report.md), [human-review design](../templates/human-review-design.md) | [08.5](../lessons/module-08/lesson-05.md) |
| 6 | **Steering pack** (one recommendation, a recommend-against), **integration check**, notes of the **hardest-finding rehearsal**, **decision record** and **handover pack** outline | [steering pack](../templates/steering-pack.md), [integration check](../templates/integration-check.md), [decision record](../templates/decision-record.md), [handover pack](../templates/handover-pack.md) | [08.6](../lessons/module-08/lesson-06.md) |

## Steps

1. Read the brief and the data room's INDEX; write the charter and the first-read sheet; interview Orly (08.1).
2. Interview at least two of Meseret, Nadia, Alexei and Valentina; measure repeats, AHT and containment; write the findings memo (08.2; Track B: `discovery.py`).
3. Build the baseline sheet, map and screen the candidates, net both claims, write the one-page case; talk to Boris (08.3; Track B: `case_model.py`).
4. Interview Hila and Daniel; write the decision paper (08.4).
5. Write the pilot charter; run the rules baseline; build and run the LLM and hybrid designs; run the negative tests; rate drafts blind; write the eval report (08.5; Track B: `pilot/run_assist.py`, `pilot/score.py`).
6. Write the steering pack; run the integration check; rehearse the hardest finding with Gil twice; run the meeting; write the decision record and the handover outline (08.6).
7. Score your set with the rubric below **before** you open the hidden truth and the expert set in 08.6; then compare.

Time: about 4 hours beyond the lessons' own exercises, most of it in steps 6 and 7.

## Self-assessment rubric

| Criterion | What "strong" looks like | What "weak" looks like |
|---|---|---|
| Mandate and entry | The sponsor's objective read back; the CEO's ask written as the claim tested; exits real and spoken; the CEO reached privately before any readout | The CEO's ask adopted as the objective; exits on paper; the CEO first meets the findings in a room |
| Discovery | People protected and their hidden facts found by asking for the work; every number with a definition, a sample and a label; containment tested against what customers did next | Opinions about the bot; a single "returns share"; vendor and KPI figures repeated |
| The real problem | Returns policy and the refund clock identified as the driver, with three readings of the share and the conflicting texts shown | The chatbot treated as the problem or the solution; returns mentioned as "noise" |
| Netting | The CEO's claim netted across ledgers with Northwind's numbers; capacity never shown as cash; the income the fix gives up on the front page | "Half of support" accepted or ridiculed; ₪ savings from freed hours; breakage discovered by the CFO in the room |
| The line between bot and agent | Decided per contact type by the cost of a wrong answer; the bot kept where it works | "Bot" or "no bot" for everything |
| Liability and law | Sources cited; every legal reading attributed to counsel; open questions listed; Air Canada used for its question, not as precedent | "Illegal" in the consultant's voice; foreign cases as Israeli law; no counsel |
| Pilot design and eval | Thresholds dated before results; rules decide, the model reads and writes; scored per language and per decision with counts, against today and rules; negative tests pass/fail; blind native ratings; time labelled assumed | Thresholds fitted to results; the model doing arithmetic; one accuracy figure; offline time presented as production |
| Recommendation | One recommendation; a recommend-against on the front page with evidence; a sentence for the CEO's board | A menu; the recommend-against in an annex; nothing for the CEO to say |
| Follow-through | Decision record with owners, dates, stop rules, next decision, dissent; a handover tested by the owner doing the work | "Approved; policy to follow"; a binder and a phone number |
| Integration | Numbers, dates and controls agree across all six deliverables; at least three contradictions found and resolved | The same measure with three values; a control nobody pays for |

## Model answer

<details><summary>Model answer</summary>

The expert's deliverable set is in the module download, `labs/module-08/expert/` ([README](../labs/module-08/expert/README.md)):

- [01 · Engagement charter and first-week plan](../labs/module-08/expert/01-engagement-charter.md)
- [02 · Findings memo](../labs/module-08/expert/02-findings-memo.md)
- [03 · Baselines, shortlist and one-page case](../labs/module-08/expert/03-baselines-and-shortlist.md)
- [04 · Decision paper: chatbot or agent-assist, and the returns policy first](../labs/module-08/expert/04-decision-paper.md)
- [05 · Pilot charter and offline eval report](../labs/module-08/expert/05-pilot-charter-and-eval-report.md)
- [06 · Steering readout, decision record and handover](../labs/module-08/expert/06-steering-readout.md)

Every number computed from the data room is real and reproducible; the LLM evaluation figures are an illustrative worked example and say so. Lesson 08.6 reveals what was really going on at Northwind and three futures; read them only after scoring yourself.

</details>
