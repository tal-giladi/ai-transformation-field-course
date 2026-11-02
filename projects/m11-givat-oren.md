# Givat Oren municipality

Run the whole engagement at Givat Oren, a fictional Israeli city of about 221,000 residents who speak Hebrew, Arabic, Russian, Amharic and English, as the municipality's Head of Digital Services: the accidental owner handed "a citizen chatbot like other cities have" by the mayor's office, with no budget, no authority over the content and every purchase public. Your job is to find out why residents don't get correct answers about permits and fees, test whether any change — including an AI assistant — fixes it in four languages, and bring one recommendation to the management forum two days before the mayor's speech. This is module 11's practical: one integrated deliverable set, every document consistent with every other.

## The brief

Read [the engagement brief](../labs/module-11/brief.md) (in the module download). In short: the ask arrived by email on Thursday 26 November 2026; the director-general's mandate comes on 30 November; the management forum meets on 17 December (case) and 2 February 2027 (decision); the council votes the budget, with a ₪600,000 "smart chatbot" line, on 22 December; the mayor speaks at the residents' conference on 4 February. You report formally to the CIO and, for this work, to the director-general. The data room is `labs/module-11/data-room/` (start with its [INDEX](../labs/module-11/data-room/INDEX.md)); the people are in `labs/module-11/personas/` ([the cast](../labs/module-11/personas/README.md)); the pilot files are in `labs/module-11/pilot/`.

## Deliverables

| # | Deliverable | Template | Lesson |
|---|---|---|---|
| 1 | **Mandate memo** for the director-general (objective read back, the stated ask as a claim, done, scope, entry-role table, advisory boundary), a reply to the chief of staff, the first-read sheet, the access request and the first-week plan | [engagement charter](../templates/engagement-charter.md), [scope boundary](../templates/scope-boundary.md), [data-room first read](../templates/data-room-first-read.md), [access request pack](../templates/access-request-pack.md) | [11.1](../lessons/module-11/lesson-01.md) |
| 2 | **Findings memo** with evidence labels: repeat contacts, callbacks made, service language, pages against the council decision, decision letters, AI already in use; notes of at least two interviews | [findings memo](../templates/findings-memo.md), [stakeholder map](../templates/stakeholder-map.md), [shadow-AI survey](../templates/shadow-ai-survey.md) | [11.2](../lessons/module-11/lesson-02.md) |
| 3 | **Baseline sheet with future owners, opportunity map and screen, one-page case** for the 17 December forum, including the budget line and the mayor's sentence | [opportunity map](../templates/opportunity-map.md), [use-case scorecard](../templates/use-case-scorecard.md), [ROI model](../templates/roi-model.md), [decision-ready case](../templates/decision-ready-case.md) | [11.3](../lessons/module-11/lesson-03.md) |
| 4 | **Constraints paper**: the constraints map with sources and design rules, the MyCity read, the questions to the legal adviser and his preliminary views, the vendor read-back, the procurement route, the works-committee letter | [regulatory map](../templates/regulatory-map.md), [risk register](../templates/risk-register.md), [claim read-back](../templates/claim-read-back.md), [comms plan](../templates/comms-plan.md) | [11.4](../lessons/module-11/lesson-04.md) |
| 5 | **Pilot charter, test-set spec, eval report and AI-register entry**: gates dated before results; site search, pack search and the LLM design(s) against today; per language and per behaviour; negative tests; blind ratings; cost labelled; the corrected AI inventory | [pilot charter](../templates/pilot-charter.md), [test-set spec](../templates/test-set-spec.md), [eval report](../templates/eval-report.md), [AI inventory](../templates/ai-inventory.md) | [11.5](../lessons/module-11/lesson-05.md) |
| 6 | **Forum readout** (one recommendation, a recommend-against, the mayor's sentence), **integration check**, notes of the **rehearsal** with the chief of staff, **decision record** and **handover** outline | [steering pack](../templates/steering-pack.md), [integration check](../templates/integration-check.md), [decision record](../templates/decision-record.md), [handover pack](../templates/handover-pack.md) | [11.6](../lessons/module-11/lesson-06.md) |

## Steps

1. Read the brief and the data room's INDEX; reply to the chief of staff; write the mandate memo and the first-read sheet; meet the director-general (11.1).
2. Interview at least two of Larisa, Tsega, Amal and Dmitri; measure repeats, callbacks, service language; check every permits page; read the letters; list the AI in use; write the findings memo (11.2; Track B: `discovery.py`).
3. Build the baseline sheet, map and screen the candidates, net the case, write the one-page case (11.3; Track B: `case_model.py`).
4. Meet the legal adviser, the works committee chair and the vendor; write the constraints paper (11.4).
5. Write the charter; run the search baselines; build and run the assistant; run the negative tests; rate answers blind; write the eval report and the register entry (11.5; Track B: `pilot/run_faq.py`, `pilot/score_faq.py`).
6. Write the readout; run the integration check; rehearse the hardest finding with the chief of staff twice; run the forum; write the decision record and the handover (11.6).
7. Score your set with the rubric below **before** you open the hidden truth and the expert set in 11.6; then compare.

Time: about 4 hours beyond the lessons' own exercises, most of it in steps 6 and 7.

## Self-assessment rubric

| Criterion | What "strong" looks like | What "weak" looks like |
|---|---|---|
| Mandate and entry | The mandate comes from the director-general, objective read back; the chatbot recorded as the claim tested; no money or promise to anyone; the mayor's office informed on a rhythm | A chatbot plan sent to the mayor's office; the vendor met before the legal adviser; division heads asked for work without a mandate |
| Discovery | Front line watched, people protected, hidden tools found by asking about the work; repeat contacts, callbacks made and service language measured with definitions; every permits page checked against the council decision | Opinions about chatbots; the report's FCR quoted; one average for all languages; the clerk who built Ruti named and blamed |
| The real problem | One correct answer in the resident's language and a usable reason identified as the problem, with outdated pages, letters, callbacks and language shown | The chatbot treated as the problem or the solution; content called "a translation issue" |
| Netting | Hours labelled capacity and not the reason; the value stated as correct answers in four languages; the budget line re-labelled, not claimed | Savings in ₪ from freed hours; staff cuts implied; the ₪600,000 requested for the project |
| Public-sector constraints | Each constraint with its source, a design rule and an owner; legal readings attributed to the legal adviser; open questions listed; the free pilot read as a commitment; a procurement route chosen before any data is shared | "Legal is blocking us"; a disclaimer as the wrong-advice control; the tender threshold quoted from memory; the free pilot accepted |
| Languages and fairness | Arabic held to the Hebrew standard with a gate and counts; Amharic routed to a person; no machine-translated page passed off as service | Hebrew first, other languages "later"; one accuracy figure |
| Pilot design and eval | Gates dated before results; answers only from the owned pack with sources; route and clarify scored separately; compared with today and with search over both corpora; negative tests pass/fail; blind native ratings; a register entry written for residents | Thresholds fitted to results; the model judged on answers alone; search baselines skipped; public launch on an offline score |
| Workers | The works committee consulted before a proposal was fixed; commitments on positions in the director-general's letter; the test measures answers, not people | The committee informed after the decision; promises the project lead cannot keep |
| Recommendation | One recommendation; a recommend-against on the front page with evidence; a true sentence for the mayor with an owner and date behind each clause | A menu; "no chatbot" with nothing to announce; the recommend-against in an annex |
| Follow-through | Decision record with content owners and an update rule, stop rules, the 1 June decision and dissent; a handover to a business and a technical owner, with the date you stop | "Approved; content to follow"; the project lead keeps everything |

## Model answer

<details><summary>Model answer</summary>

The expert's deliverable set is in the module download, `labs/module-11/expert/` ([README](../labs/module-11/expert/README.md)):

- [01 · Mandate memo and first week](../labs/module-11/expert/01-mandate-and-first-week.md)
- [02 · Findings memo](../labs/module-11/expert/02-findings-memo.md)
- [03 · Baselines, opportunity map and the one-page case](../labs/module-11/expert/03-baselines-and-case.md)
- [04 · Public-sector constraints](../labs/module-11/expert/04-public-sector-constraints.md)
- [05 · Pilot charter, eval report and AI-register entry](../labs/module-11/expert/05-eval-report-and-register-entry.md)
- [06 · Forum readout, decision record and handover](../labs/module-11/expert/06-forum-readout.md)

Every number computed from the data room and the search baselines is real and reproducible; the LLM evaluation figures are an illustrative worked example and say so. Lesson 11.6 reveals what was really going on in Givat Oren and three futures; read them only after scoring yourself.

</details>
