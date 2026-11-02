# Meridian Mutual — a regulated deployment verdict

Run the whole Meridian Mutual engagement as its new Head of AI Transformation: from the COO's call to the joint steering and risk committee, with every deliverable built on the data room and the people. This is module 9's practical and the full deliverable set of the engagement.

## The brief

Meridian Mutual, a mid-size Israeli insurer, hired you on 1 November 2026. The COO wants to "automate
claims intake and spot fraud" with two modules that arrived inside the claims system's September
release, in a pilot from 1 December 2026 to 28 February 2027, and to buy the vendor's premium fraud
module. The board's risk management committee meets on 15 December; the readout is on 26 January
2027. Everything you need is in the module download: the [engagement brief](../labs/module-09/brief.md),
the data room (`labs/module-09/data-room/`, start with `INDEX.md`), the [cast](../labs/module-09/personas/README.md)
and the Track B scripts ([labs README](../labs/module-09/README.md)).

You will have to decide what is really slowing claims, what the systems already running do and to
whom, what the committee can approve, and what to build. The stated ask is not necessarily the right
answer.

## Deliverables

| # | Deliverable | Template | Lesson |
|---|---|---|---|
| 1 | Engagement charter (internal lead) with first-day data-room read and first-week plan | [engagement charter](../templates/engagement-charter.md), [data-room first read](../templates/data-room-first-read.md), [30-60-90 plan](../templates/30-60-90-plan.md) | [09.1](../lessons/module-09/lesson-01.md) |
| 2 | Findings memo with evidence labels, and an interim recommendation on anything live | [findings memo](../templates/findings-memo.md), [data profile](../templates/data-profile.md) | [09.2](../lessons/module-09/lesson-02.md) |
| 3 | Measured baselines (three, reconciled), shortlist and one-page case | [opportunity map](../templates/opportunity-map.md), [use-case scorecard](../templates/use-case-scorecard.md), [ROI model](../templates/roi-model.md), [claim read-back](../templates/claim-read-back.md), [decision-ready case](../templates/decision-ready-case.md) | [09.3](../lessons/module-09/lesson-03.md) |
| 4 | **Deployment verdict** for the risk committee: classification, regulatory map, gate questions, outcome test, pass / flag / block per system, verdicts with conditions, correction to the record, dissent | [regulatory map](../templates/regulatory-map.md), [DPIA for AI](../templates/dpia-for-ai.md), [decision record](../templates/decision-record.md) | [09.4](../lessons/module-09/lesson-04.md) |
| 5 | **Extraction pilot**: prompt with version log, run files or the filled Track A sheet, eval report with the no-AI baseline and the vendor beside it, negative tests, fairness check, human-review design, and the pilot's deployment verdict | [pilot charter](../templates/pilot-charter.md), [test-set spec](../templates/test-set-spec.md), [eval report](../templates/eval-report.md), [human-review design](../templates/human-review-design.md) | [09.5](../lessons/module-09/lesson-05.md) |
| 6 | Readout pack, integration check, rehearsal transcript with coach feedback, decision record | [steering pack](../templates/steering-pack.md), [integration check](../templates/integration-check.md), [decision record](../templates/decision-record.md) | [09.6](../lessons/module-09/lesson-06.md) |

## Steps

1. Read the brief and the data room; interview the COO; write the charter (09.1).
2. Interview the VP Claims, a senior handler and the claimant; trace every claim into the data; write
   the findings memo and the interim recommendation (09.2).
3. Reconcile the baselines with the Chief Actuary; decompose the wait; screen the candidates; write the
   case and tell the COO first (09.3).
4. Classify the systems, map the law, write the gates, run the outcome test, interview the CRO, the DPO,
   internal audit and the vendor; write the verdict (09.4).
5. Build, score and fairness-check the extraction pilot; design the human check; write its verdict (09.5).
6. Build the readout pack, run the integration check, rehearse the hardest finding, write the decision
   record; then score yourself and only then open the hidden truth in 09.6.

Time: about 7 hours beyond the lessons' own exercises, most of it in steps 4 and 5.

## Self-assessment rubric

| Criterion | Strong | Weak |
|---|---|---|
| Charter | Objective in the sponsor's words as an outcome; live systems separated from the proposal; decision rights with sources; a line to the CRO; a bad-news rule | "Deliver the winter pilot"; vendor numbers as baselines; the live modules out of scope |
| Discovery | Interviews that made it safe to talk; the claimant's story contact by contact; every claim traced to a file with a label; data limits written | Leading questions; quotes from people who asked not to be quoted; sample and population mixed |
| Interim action | A live harm raised the week it was clear, with what to switch off, how, and who decides | Held for the committee four weeks later |
| Baselines | Three definitions side by side; the claimant's wait chosen and agreed with the actuary; the dashboard kept as the regulatory clock | The flattering number; or one number without its definition and n |
| Diagnosis and case | The wait decomposed; causes named from the data; the peak on the calendar; a no-AI move first; fraud counted only when confirmed; one ask | Automating the fast step; "fraud prevented" as savings; the ₪20M in the case |
| Classification and law | Systems classified by impact; Israel-first map with questions for counsel; a reasoned "EU AI Act not applicable" with a re-check trigger | "Not AI, so out of scope"; legal conclusions in your own voice; the EU AI Act assumed to apply |
| Outcome test | Recorded attributes only, nothing inferred, missing ones stated; rates with n and intervals; before/after; the mechanism found | Ethnicity inferred; a single ratio with no interval; a disparity with no cause |
| Gates and verdict | Gate questions dated before scoring; pass / flag / block with evidence; one verdict per system; conditions with limit, owner and stop authority; correction to the record; dissent | Gates written after the results; "we will monitor"; one verdict for everything |
| Pilot eval | Dev/test split; no-AI baseline and vendor beside the result; blanks and wrong values apart; all negative tests; minimisation as a gate | One accuracy figure; tuned on the test set; minimisation as a promise |
| Fairness check | Per group with intervals; stratified by capture channel; causes and fixes named; gaps in coverage stated | "Average looks fine"; a gap with no cause; groups too small read as findings |
| Human check | Source beside value; timers; an operating test; capacity checked against the peak | "A human reviews everything" with no minutes or evidence |
| Readout | One recommendation, a recommend-against and a de-scope; every number labelled and traced; the hardest finding rehearsed with the person who will resist it; decision record with dissent | Three recommendations; early good news unlabelled; the sponsor ambushed or the finding blurred |

<details><summary>Model answer</summary>

The expert's deliverable set is in the module download, `labs/module-09/expert/`:

- [01 · Charter and first week](../labs/module-09/expert/01-charter-and-first-week.md)
- [02 · Findings memo and interim memo](../labs/module-09/expert/02-findings-memo.md)
- [03 · Baselines, shortlist and one-page case](../labs/module-09/expert/03-baselines-and-case.md)
- [04 · Deployment verdict for the risk committee](../labs/module-09/expert/04-deployment-verdict.md)
- [05 · Extraction pilot: eval, fairness check and verdict](../labs/module-09/expert/05-pilot-eval-and-verdict.md)
- [06 · Readout pack and decision record](../labs/module-09/expert/06-readout-and-decision.md)

The data-room numbers in them are real and reproducible with the scripts in `labs/module-09/`
(`baselines.py`, `bias_test.py`, `extract_rules.py`, `score_extraction.py`): the claimant's median
wait of 32 days with a 12.8-day document chase; the 3.87× referral disparity after go-live (3.2% vs
3.4% before); Smart Intake 82.1% vs a no-AI rules script 86.7% on the 200 test documents. The expert's
own LLM pilot figures are an illustrative worked example; your run replaces them. Open the hidden truth
and the three futures in [09.6](../lessons/module-09/lesson-06.md) after you have written your readout.

</details>
