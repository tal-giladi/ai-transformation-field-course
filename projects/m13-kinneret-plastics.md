# Kinneret Plastics

Run the whole engagement at Kinneret Plastics, a fictional family-owned injection-moulding company in the Galilee with about 600 people, two plants, three shifts and a workforce that speaks Arabic, Hebrew, Russian and Amharic, as its operations-excellence manager: the internal lead with a day job, handed "predictive maintenance with AI" by the owner. Your job is to find out what really makes Kinneret late to its largest customer, judge whether the company is ready for predictive maintenance, say "not yet" if the evidence says so and get the foundation funded instead, build a repeatable data-readiness audit and a tested multilingual manual assistant, and bring one recommendation to the management meeting. This is module 13's practical: one integrated deliverable set, every document consistent with every other.

## The brief

Read [the engagement brief](../labs/module-13/brief.md) (in the module download). In short: the ask was made at the annual management meeting on Thursday 7 January 2027; the sponsor is Dalia Mizrahi, VP operations; the vendor, Predictiva, presents on 15 February; management decides on Tuesday 23 March; the customer Arava expects a corrective-action plan by 31 March. A ₪1.5M "AI and Industry 4.0" line is controlled by the CFO and the CEO. The data room is `labs/module-13/data-room/` (start with its [INDEX](../labs/module-13/data-room/INDEX.md)); the people are in `labs/module-13/personas/` ([the cast](../labs/module-13/personas/README.md)); the pilot files are in `labs/module-13/pilot/`.

## Deliverables

| # | Deliverable | Template | Lesson |
|---|---|---|---|
| 1 | **Mandate memo** for the sponsor (objective read back, the stated ask as a claim, done, scope, entry-role table, advisory boundary), first-read sheet, access request, first-week plan, note to the CEO | [engagement charter](../templates/engagement-charter.md), [scope boundary](../templates/scope-boundary.md), [data-room first read](../templates/data-room-first-read.md), [access request pack](../templates/access-request-pack.md) | [13.1](../lessons/module-13/lesson-01.md) |
| 2 | **Findings memo** with evidence labels: the loss split by reason and shift, the same-word test, the records profiled for prediction, PM, night calls, parts, AI already in use; the safety escalations with times | [findings memo](../templates/findings-memo.md), [data profile](../templates/data-profile.md), [interview guide](../templates/interview-guide.md), [shadow-AI survey](../templates/shadow-ai-survey.md) | [13.2](../lessons/module-13/lesson-02.md) |
| 3 | **Baseline sheet** with one definition and an owner per measure, **opportunity map and screen** with data gates, **one-page case** netted with the CFO's numbers | [opportunity map](../templates/opportunity-map.md), [use-case scorecard](../templates/use-case-scorecard.md), [ROI model](../templates/roi-model.md), [decision-ready case](../templates/decision-ready-case.md) | [13.3](../lessons/module-13/lesson-03.md) |
| 4 | **Readiness verdict and foundation paper**: the bar dated before the vendor's presentation, the graded evidence, "not yet" with criteria and a date, the foundation plan with owners, costs, gates and a stop rule, the vendor read-back, the constraints map, the draft protocol with the works committee | [readiness assessment](../templates/readiness-assessment.md), [claim read-back](../templates/claim-read-back.md), [regulatory map](../templates/regulatory-map.md), [risk register](../templates/risk-register.md) | [13.4](../lessons/module-13/lesson-04.md) |
| 5 | **Data-readiness audit report** (repeatable), **pilot charter with gates, test-set spec, eval report** of the manual assistant, the shadow-use decision, the corrected AI inventory | [data profile](../templates/data-profile.md), [pilot charter](../templates/pilot-charter.md), [test-set spec](../templates/test-set-spec.md), [eval report](../templates/eval-report.md), [AI inventory](../templates/ai-inventory.md) | [13.5](../lessons/module-13/lesson-05.md) |
| 6 | **Readout** (one recommendation, a recommend-against, the Arava plan), **integration check**, notes of the **rehearsal** with the CEO, **decision record** with the re-decision date and **handover** | [steering pack](../templates/steering-pack.md), [integration check](../templates/integration-check.md), [decision record](../templates/decision-record.md), [handover pack](../templates/handover-pack.md) | [13.6](../lessons/module-13/lesson-06.md) |

## Steps

1. Read the brief and the data room's INDEX; fill the entry-role table; meet Dalia and Amnon; write the mandate memo, first read and note (13.1).
2. Interview at least three of Vladi, Nizar, Tigist and Eli; split the downtime; run the same-word test; profile the records, clocks, sensors and parts; escalate safety items the same day; write the findings memo (13.2; Track B: `discovery.py`).
3. Build the baseline sheet; map and screen the options; meet Orit; net the vendor and your top options; write the one-page case (13.3).
4. Write the bar before the vendor presents; read the vendor back; grade the evidence; write the verdict and the foundation plan; build the constraints map; meet Khalil and draft the protocol (13.4).
5. Run the audit; curate the pack; write the charter and gates; run the search baselines and the assistant; score per language and behaviour; run the negative tests; decide shadow use (13.5; Track B: `readiness_audit.py`, `pilot/run_manual.py`, `pilot/score_manual.py`).
6. Write the readout; run the integration check; rehearse the hardest finding with Amnon twice; run the meeting; write the decision record and the handover (13.6).
7. Score your set with the rubric below **before** you open the hidden truth and the expert set in 13.6; then compare.

Time: about 4 hours beyond the lessons' own exercises, most of it in steps 6 and 7.

## Self-assessment rubric

| Criterion | What "strong" looks like | What "weak" looks like |
|---|---|---|
| Entry and mandate | The objective is the sponsor's, with the customer in it; the owner's ask recorded as the claim tested; your own data declared under audit; no promise to any supplier | A vendor rollout plan sent to the owner; your own reports excluded; the vendor met before the works committee |
| Discovery | The loss split by reason and shift before it is explained; the same-word test run and both plants measured on one definition; records profiled for a named use with numerators and denominators; people protected | The deck's headline quoted; "breakdowns" treated as one thing; technicians or the planner named and blamed |
| Safety | The overdue examination and the outdated lockout translations escalated to their owners the day they were found; the memo reports what was done | Safety items held for the readout, or judged by you instead of the safety officer |
| Netting | The CFO's cost of an hour; the vendor netted at its own best claim; freed hours labelled capacity; the foundation's payback not invented | Revenue per hour; savings from freed hours; the vendor dismissed without numbers |
| Readiness verdict | The bar dated before the demo and traced to the vendor's own prerequisites; each criterion graded; "not yet" with criteria, funded work and a re-decision date | "No" with no date; a bar written after the demo; the second plant's "ready" accepted as reported |
| Foundation | Each gap with work, owner, cost, date and closing evidence; a short failure-mode list written with technicians in their languages; a stop rule | "Improve data quality" as an action; forty codes again; the foundation left unfunded |
| Workforce | The works committee consulted before anything is fixed; a written protocol on how records are and are not used; no cameras; training in the workers' languages; legal readings routed to counsel and the safety officer | The committee informed after the decision; promises you cannot sign; monitoring by the back door |
| Audit and assistant | The audit repeatable with fixed definitions and a verdict per dataset and use; the pack curated to current, approved, owned documents; gates dated before results incl. 100% safety routes and negative tests; scores per language and behaviour against search baselines | The assistant pointed at the drive; one accuracy figure; gates fitted to results; LLM back-coding presented as labels |
| Recommendation | One recommendation; the recommend-against on the front page with measured evidence; a plan for the customer this quarter; the hardest finding rehearsed privately with the owner | A menu; "no AI" with nothing for the customer; the owner corrected in front of his team |
| Follow-through | Decision record with owners, gates, the stop rule, the January 2028 criteria and dissent; handover to business and technical owners and a successor to the maintenance manager's knowledge, with the date you stop | "Approved; details to follow"; you keep everything; the knowledge leaves with one person |

## Model answer

<details><summary>Model answer</summary>

The expert's deliverable set is in the module download, `labs/module-13/expert/` ([README](../labs/module-13/expert/README.md)):

- [01 · Mandate memo and first week](../labs/module-13/expert/01-charter-and-first-week.md)
- [02 · Findings memo](../labs/module-13/expert/02-findings-memo.md)
- [03 · Baselines, opportunity map and the one-page case](../labs/module-13/expert/03-baselines-and-case.md)
- [04 · Readiness verdict, foundation plan and constraints](../labs/module-13/expert/04-readiness-verdict-and-foundation.md)
- [05 · Data-readiness audit, pilot charter and eval report](../labs/module-13/expert/05-audit-and-eval-report.md)
- [06 · Readout, decision record and handover](../labs/module-13/expert/06-steering-readout.md)

Every number computed from the data room, the audit and the search baselines is real and reproducible; the LLM evaluation figures are an illustrative worked example and say so. Lesson 13.6 reveals what was really going on at Kinneret and three futures; read them only after scoring yourself.

</details>
