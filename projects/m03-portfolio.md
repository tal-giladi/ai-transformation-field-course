# From findings to a funded portfolio — Harbor & Pine

The module 3 practical: the full set of documents that takes Harbor & Pine from a findings memo to a board decision. Most pieces start as your answers to lessons 03.1–03.9; the practical asks you to finish them, make them agree with each other, and hold them to the standard a CFO and a board would apply. Plan 6 hours if you completed the lessons' "Your turn" tasks, longer if you did not.

## The brief

It is Thursday 21 January 2027. The board pre-read is due today; the board meets on 28 January. Michal Peretz, the COO and your sponsor, asks for "the whole pack, in one place: what we're doing, why those three things, what it costs, what we get, and the page the board will read". Ronit Avraham, the CFO, will read every number. Yoav Ben-Ami, the CEO, has agreed the story privately and needs a page he can present without being contradicted by the appendix.

You have the Harbor & Pine data room, the persona pack, your module 2 findings, and everything you wrote in this module.

## Deliverables

| # | Deliverable | Template | Built in |
|---|---|---|---|
| 1 | Opportunity map (at least 12 candidates, three feeds plus discovery) | [opportunity map](../templates/opportunity-map.md); `labs/module-03/opportunity-map.csv` | 03.1 |
| 2 | Two agentic opportunity frames: the date fix and the reply drafts | [agentic opportunity frame](../templates/agentic-opportunity-frame.md) | 03.2 |
| 3 | Fast screen of every candidate, with the scrutiny rule and the routed questions | [use-case scorecard](../templates/use-case-scorecard.md) part A | 03.3 |
| 4 | Scored portfolio of three: locked criteria, scores, error costs, four-part effort, absorption | [use-case scorecard](../templates/use-case-scorecard.md) part B | 03.4 |
| 5 | Workshop pack: scoring-workshop script and read-back; alignment-session agenda, pre-read and the one-page output | [scoring workshop script](../templates/scoring-workshop-script.md), [alignment session agenda](../templates/alignment-session-agenda.md) | 03.5, 03.6 |
| 6 | ROI model with scenarios, sensitivity and staged gates | [ROI model](../templates/roi-model.md); `labs/module-03/roi-model.csv` or `roi_model.py` | 03.7 |
| 7 | Roadmap, one page, with the quarterly check | [roadmap](../templates/roadmap.md) | 03.8 |
| 8 | Decision-ready case: front page and appendix list | [decision-ready case](../templates/decision-ready-case.md) | 03.9 |
| 9 | A consistency note to Michal: what you checked across 1–8 and what you fixed | — | this project |

## Steps

1. **Collect** your lesson outputs for deliverables 1–8. Where you skipped a "Your turn", do it now; the reference answers show the standard but are not yours to copy.
2. **Trace the three bets end to end.** For each of the date fix, the reply drafts and the quote drafts, follow it from its row on the opportunity map, through its frame, screen verdict, score, alignment-page sentence, ROI lines and roadmap gates, to the front page. Every step should say the same thing about scope, owner, condition and date.
3. **Make the numbers agree.** The same figures must appear everywhere: WISMO share and October volume, the 3,200 written contacts, 108.8 net hours, ₪120,000 build and ₪49,000 a year to run, ₪267,000 over three years, ₪113,000 expected cash, NPV ₪33,717, payback 22.5 months, the gate dates. List every inconsistency you fix.
4. **Check every label and every source.** Each number on the front page is measured, directional or assumed and names its source. Persona-only facts ("Ronit said…", "Yaniv's study") are marked as reported. No vendor figure is marked measured.
5. **Check the parked list.** Every idea that did not make the portfolio is on it, with its reason and a dated reopening condition, and the CEO's chatbot is worded as agreed ("re-screen", not "rejected").
6. **Check capacity.** No quarter in the roadmap asks a team for more than it said it can absorb, no support go-live falls in the November–January peak, and the central review queue holds at most two new evaluations a quarter.
7. **Write the consistency note** (half a page): what you traced, what was inconsistent, what you changed, and the one assumption that carries the case.
8. **Self-assess** with the rubric, then run the [coach prompt](../labs/common/coach-prompt.md) on the front page with the rubric as the checklist.

## Rubric

| Criterion | Strong | Weak |
|---|---|---|
| Opportunity map | Three feeds plus discovery; every candidate restated as a step with an owner and a sourced volume; tools already in use and false "AI" on the map; a ledger line on every row | A list of requests in the proposers' own words and units; no ledger lines |
| Agent or not | Workflows mapped from the data and simplified first; each step justified as automation, generation, agent or person; facts always from systems; the date fix ends as plain automation | "Use an agent" chosen before the workflow was mapped; a model producing prices or dates |
| Fast screen | Scrutiny rule written first; seven separate answers; a pass/fail data gate with the label question; every stop has a reopening condition; legal questions routed, not answered | Candidates averaged into "medium"; vendor figures accepted; legal conclusions stated as fact |
| Scoring and portfolio | Criteria locked and dated before scoring, with anchors; error costs netted; four-part effort with owners; absorption asked and respected; card volumes checked against the data | Weights changed after seeing the list; a CEO bonus; absorption assumed |
| Workshop pack | Independent scoring before discussion; divergence discussed, not averaged; one-page alignment output with goal, KPI, guardrail, owner and yes/no gate per bet; baselines measured or "to be confirmed"; read-backs sent the same day | Scores negotiated in the room; estimated baselines; no written output |
| ROI model | In finance's template; review, rework and tokens costed; claims netted on four ledgers and labelled; capacity never shown as cash; low scenario first; sensitivity shows what carries the case; first stage under ₪50,000 | Hours × rate as savings; double counts; one scenario; no gates |
| Roadmap | Horizons by evidence; foundations with owners; gates as conditions; what each phase proves for the next; quarterly check against absorption, review capacity and cash timing; ledger column | Everything in Q1; dates instead of gates; foundations missing |
| Decision-ready case | One-sentence ask with what, who, when and how much; conservative first; every claim labelled and tagged; cost of waiting in two columns; two-reader check done | A strategy essay ending in a total; two decisions in one ask; unlabelled numbers |
| Sponsor handling | The CEO heard the result privately first, chose among options, and has a true sentence for the board; his commitments to the board and the vendor are known | The CEO learns in a meeting or from the paper; the message softened until it disappears |
| Consistency | The same numbers, owners and dates in every document; inconsistencies listed and fixed | Different figures in the ROI model, roadmap and front page |

<details><summary>Model answer</summary>

The reference answers in each lesson are the model for deliverables 1–8: [03.1](../lessons/module-03/lesson-01.md) (fifteen-row map; WISMO about 247 agent-hours a month across channels), [03.2](../lessons/module-03/lesson-02.md) (frames for the date fix, reply drafts and quotes), [03.3](../lessons/module-03/lesson-03.md) (screen of fifteen; damage-claim decisions stop on the label question, 48 of 149 decisions blank), [03.4](../lessons/module-03/lesson-04.md) (criteria 40/30/30; scores 100, 80, 66 for the portfolio; absorption 25 of 30, 4 of 12, 10 of 20), [03.5](../lessons/module-03/lesson-05.md) and [03.6](../lessons/module-03/lesson-06.md) (workshop read-back; three bets with KPI, guardrail, owner and gate), [03.7](../lessons/module-03/lesson-07.md) (₪1.36 million claimed → ₪113,000 cash a year plus capacity; NPV ₪33,717; payback 22.5 months; ₪267,000 over three years → board), [03.8](../lessons/module-03/lesson-08.md) (roadmap v1.0) and [03.9](../lessons/module-03/lesson-09.md) (front page). Run `labs/module-03/roi_model.py` to reproduce the ROI numbers; `labs/module-03/roi-model-harbor-solution.csv` is the filled model.

**What the integrated pack adds.**

*Consistency fixes a strong pack makes.* The drafts are "for all written contact once WhatsApp is routed into the helpdesk" everywhere, not "support emails" in some documents. The B2B owner is Yaniv Carmi (Head of B2B Sales in `company/org-chart.md`) in every document. The date fix's live date is 14 January in the roadmap and the front page. The quote drafts' benefit is marked reported (Yaniv's time study), not measured. The card volumes for damage claims and assembly questions are corrected from the data room (about 25 claims and about 25 assembly tickets a month), even though neither is in the portfolio.

*Consistency note to Michal (excerpt).*

> I traced each of the three bets from the opportunity map to the front page and checked twelve
> numbers across the eight documents. I fixed four inconsistencies: the drafts' scope (all written
> contact, not email only), the B2B owner, the date fix's live date, and the label on the quote
> benefit (reported, not measured). Every number on the front page now names its source; the only
> vendor figure in the pack (ChatNest's 70%) appears once, as a claim, in the parked list. The case
> rests on one assumption more than any other: that the pilot and the date fix together free enough
> peak-season hours for the next peak to run without the two temps. On today's numbers they free
> about 230 of the 320 hours the temps give; gate 1 on 1 April tests it with measured numbers before
> most of the money is spent, and if it fails we come back with a one-temp case.

</details>
