# Atlas & Rowe

Run the whole engagement at Atlas & Rowe, a 90-lawyer Israeli commercial law firm, as an outside consultant to its managing partner: from the first call to the partners' vote and the handover. Half the partners want a legal-AI platform before a vendor's discount expires; the other half think it will invent cases and cost them clients. Your job is to find out, with the firm's own data and people, how it should use AI in its legal work, test a precedent search and a citation-verification gate on its own documents, revise the business case with the customer's share in it, and bring one recommendation to the partners. This is module 12's practical: one integrated deliverable set, every document consistent with every other.

## The brief

Read [the engagement brief](../labs/module-12/brief.md) (in the module download). In short: 15 November 2026 – 14 January 2027; ₪180,000 + VAT in three phases with exits on 3 December and 17 December; pilot tooling up to ₪40,000; you report to Yoav Dagan (managing partner); the management committee is Yoav, Shmuel Atlas, Noa Friedman, Orit Levinson and Eli Ben-Hamo; the partners' meeting decides. The data room is `labs/module-12/data-room/` (start with its [INDEX](../labs/module-12/data-room/INDEX.md)); the people are in `labs/module-12/personas/` ([the cast](../labs/module-12/personas/README.md)); the pilot files are in `labs/module-12/pilot/`.

The fixed points: phase-1 readout Thursday 3 December; decision paper Thursday 17 December; the vendor's discount expires 31 December; offline eval report Thursday 7 January; management committee Tuesday 12 January 2027; partners' vote and handover Thursday 14 January; the insurer's questionnaire is due 15 January; Carmel's panel review closes 31 January.

You are not a lawyer, and this project is not legal advice: every legal or ethical reading in your deliverables is attributed to the firm's ethics partner or to the source she points to.

## Deliverables

| # | Deliverable | Template | Lesson |
|---|---|---|---|
| 1 | **Engagement charter** with SOW (phases, exits, change control), the partnership entry-role table, the advisory boundary for a non-lawyer, first-read sheet, access request, first-week plan | [engagement charter](../templates/engagement-charter.md), [scope boundary](../templates/scope-boundary.md), [data-room first read](../templates/data-room-first-read.md), [access request pack](../templates/access-request-pack.md) | [12.1](../lessons/module-12/lesson-01.md) |
| 2 | **Findings memo**: AI use from logs against the survey, research from narratives against codes, the memo's citations checked, the knowledge bank's state; every finding labelled; nobody identifiable | [findings memo](../templates/findings-memo.md), [stakeholder map](../templates/stakeholder-map.md), [interview guide](../templates/interview-guide.md) | [12.2](../lessons/module-12/lesson-02.md) |
| 3 | **Baseline sheet by billing type, the slide netted, opportunity map and screen, one-page case**, including the customer's share from the firm's own history | [ROI model](../templates/roi-model.md), [opportunity map](../templates/opportunity-map.md), [use-case scorecard](../templates/use-case-scorecard.md), [decision-ready case](../templates/decision-ready-case.md) | [12.3](../lessons/module-12/lesson-03.md) |
| 4 | **Decision paper**: the rule / opinion / view / decision table, the cases and the citation gate, pricing tested with the client, the vendor read-back and contract changes, an interim rule for counsel | [regulatory map](../templates/regulatory-map.md), [acceptable-use policy](../templates/acceptable-use-policy.md), [claim read-back](../templates/claim-read-back.md), [vendor AI questionnaire](../templates/vendor-ai-questionnaire.md), [decision-ready case](../templates/decision-ready-case.md) | [12.4](../lessons/module-12/lesson-04.md) |
| 5 | **Pilot charter, test-set spec, eval report and revised ROI**: search before and after curation, the gate's rules and reader step, negative tests, checking time and cost, the ROI with the customer's share | [pilot charter](../templates/pilot-charter.md), [test-set spec](../templates/test-set-spec.md), [eval report](../templates/eval-report.md), [human-review design](../templates/human-review-design.md), [ROI model](../templates/roi-model.md) | [12.5](../lessons/module-12/lesson-05.md) |
| 6 | **Partners' paper** (one recommendation in votable parts, a recommend-against), **integration check**, notes of the **hardest-finding rehearsal**, **decision record** and **handover** outline | [steering pack](../templates/steering-pack.md), [integration check](../templates/integration-check.md), [decision record](../templates/decision-record.md), [handover pack](../templates/handover-pack.md) | [12.6](../lessons/module-12/lesson-06.md) |

## Steps

1. Read the brief and the INDEX; write the charter and the first read; interview Yoav (12.1).
2. Interview at least three of Karim, Yana, Tamar and Noa; measure AI use and research time; check the memo; write the findings memo (12.2; Track B: `discovery.py`).
3. Build the baselines by billing type, net the slide, screen the candidates, write the one-page case; talk to Eli and Shmuel (12.3; Track B: `roi_model.py`).
4. Interview Orit and Sigal; write the decision paper and the interim rule (12.4).
5. Write the pilot charter; run the search uncurated and curated; run the gate; run your assistant and the negative tests; time and cost it; revise the ROI; write the eval report (12.5; Track B: `pilot/search.py`, `pilot/verify_citations.py`).
6. Write the partners' paper; run the integration check; rehearse the hardest finding with Shmuel twice; run the committee; write the decision record and the handover (12.6).
7. Score your set with the rubric below **before** you open the hidden truth and the expert set in 12.6; then compare.

Time: about 4 hours beyond the lessons' own exercises, most of it in steps 6 and 7.

## Self-assessment rubric

| Criterion | What "strong" looks like | What "weak" looks like |
|---|---|---|
| Mandate in a partnership | The managing partner's objective read back; the platform as the question answered; both camps met early; the vote as the decider | The platform as the objective; one camp first; the managing partner treated as a CEO |
| Advisory boundary | Every legal and ethical reading attributed; incidents routed to the ethics partner; no client files requested | "This breaches privilege" in the consultant's voice; client files requested; foreign cases as Israeli law |
| Discovery | AI use from logs and expenses against the survey, with limits; research from narratives against codes; associates protected; the memo checked citation by citation | The survey taken at face value; codes counted; a name in the memo; the near miss missed or attributed |
| The real problem | Rule, knowledge and pricing identified as the decisions, with the platform as a later choice | The platform debate accepted as the problem |
| Netting | By billing type; capacity in hours; fees lost on hourly work; the customer's share priced from the firm's own history; sensitivity shown | Hours × rate; one number; the client's renegotiation ignored |
| Citations | The five-check gate built from the cases; rules separated from judgement; stale authority treated as a failure | "Check your sources" as the whole control; existence only; a disclaimer |
| Pilot and eval | Thresholds dated before results; uncurated vs curated; per-language and per-failure-type counts; false alarms measured; time labelled directional | Thresholds after results; one accuracy figure; word matching as support; offline time as production |
| Pricing | Tested with the client; fixed prices for repeat work set before hours fall; billing-for-time-not-spent routed to ethics | A discount conceded or refused without a model; value billing adopted without counsel |
| Recommendation | One recommendation in votable parts; the recommend-against on the front page; the discount date answered | A menu; the recommend-against in an annex; the deadline decides |
| Integration and follow-through | Numbers, dates, owners and costs agree across all six deliverables; the hardest finding delivered privately; owners can run the gate and the model without you | The same measure with three values; a control nobody owns; a binder and a phone number |

## Model answer

<details><summary>Model answer</summary>

The expert's deliverable set is in the module download, `labs/module-12/expert/` ([README](../labs/module-12/expert/README.md)):

- [01 · Engagement charter](../labs/module-12/expert/01-engagement-charter.md)
- [02 · Findings memo](../labs/module-12/expert/02-findings-memo.md)
- [03 · Baselines, the slide netted, shortlist and one-page case](../labs/module-12/expert/03-baselines-and-shortlist.md)
- [04 · Decision paper: confidentiality, citations and the billable hour](../labs/module-12/expert/04-decision-paper.md)
- [05 · Pilot charter, eval report and revised ROI](../labs/module-12/expert/05-pilot-charter-and-eval-report.md)
- [06 · Partners' paper, readout, decision record and handover](../labs/module-12/expert/06-partners-paper-and-readout.md)

Every number computed from the data room, the search, the gate's rules and the ROI model is real and reproducible; the reader-step, assistant-answer and timing figures are an illustrative worked example and say so. Lesson 12.6 reveals what was really going on at Atlas & Rowe and three futures; read them only after scoring yourself.

</details>
