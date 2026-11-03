# Open Hands

Run the whole engagement at Open Hands, a 30-person Israeli amuta that accompanies families raising children with disabilities, as an unpaid volunteer consultant: from the first meeting with the executive director to the board's decision and the handover to the person who does IT on Tuesdays. The board said "help us use AI, we have no budget"; your job is to find out, in four weeks and 40 hours, what using AI safely means for an organization that holds children's medical and welfare information, build what is justified on the tools it already has, and leave it running. This is module 16's practical: one integrated deliverable set, sized for a small organization, every document consistent with every other.

## The brief

Read [the engagement brief](../labs/module-16/brief.md) (in the module download). In short: four weeks, Sunday 15 November – Thursday 10 December 2026; 40 hours pro bono through Mahut Pro Bono; no fee and no budget (the director may spend up to ₪3,000 a year on software, any recurring charge needs the treasurer); you report to Dr. Ronit Azoulay, executive director; the readout is a 20-minute item at the board's Zoom meeting on Wednesday 9 December; the handover is to Ronit and Yossi Mizrahi (operations, IT on Tuesdays). The data room is `labs/module-16/data-room/` (start with its [INDEX](../labs/module-16/data-room/INDEX.md)); the people are in `labs/module-16/personas/` ([the cast](../labs/module-16/personas/README.md)); the build files are in `labs/module-16/build/`.

The fixed points: staff meeting Monday 16 November; Tuesdays with Yossi (17 and 24 November); the volunteer lawyer's two hours by 26 November; Giving Tuesday 1 December; Hanukkah from the evening of 4 December, families' party and staff training Monday 7 December; board Wednesday 9 December; handover Thursday 10 December. The largest funder's Q4 report is due 15 January 2027 and its renewal proposal 31 January.

## Deliverables

Every deliverable is a Stage 1 template shrunk to the size a 30-person organization will read. The size is part of the assessment.

| # | Deliverable | Template | Lesson |
|---|---|---|---|
| 1 | **One-page charter**: objective read back, the stated ask as a claim, done (five checkable items), out of scope with owners, the urgent-finding rule, non-attribution; the **40-hour budget**; the **first-read sheet** (at least eight claims sorted); the first week | [engagement charter](../templates/engagement-charter.md), [scope boundary](../templates/scope-boundary.md), [data-room first read](../templates/data-room-first-read.md) | [16.1](../lessons/module-16/lesson-01.md) |
| 2 | **Findings memo** (two pages) with measured, reported and inferred labels; the **access count** for the family drive, the respite folder and the donor sheet; the **same-day note**; notes from at least four interviews including the parent | [findings memo](../templates/findings-memo.md), [interview guide](../templates/interview-guide.md), [stakeholder map](../templates/stakeholder-map.md) | [16.2](../lessons/module-16/lesson-02.md) |
| 3 | **Baseline in hours** with labels and an annual range; **money already spent** with sources and the exchange rate; **one-table map and screen** (including a "no AI" and a "plain automation" verdict); **one-page case in hours**; **the funder proposal page** | [task inventory](../templates/task-inventory.md), [opportunity map](../templates/opportunity-map.md), [use-case scorecard](../templates/use-case-scorecard.md), [decision-ready case](../templates/decision-ready-case.md) | [16.3](../lessons/module-16/lesson-03.md) |
| 4 | **Compression table** (what shrinks, what cannot); **one-page legal map** with five questions for counsel; **verified offers table** with dates; **data boundary**; **Yossi's afternoon checklist** and the same-day alternative | [data boundary](../templates/data-boundary.md), [tools and data classes](../templates/tools-and-data-classes.md), [regulatory map](../templates/regulatory-map.md) | [16.4](../lessons/module-16/lesson-04.md) |
| 5 | **Two workflows** (grant drafter; case notes and letters) with dated thresholds, a rated test sheet with negative tests and traps, an eval summary with versions; the **de-identification check** result; **the policy pack on one page** mapped to the Stage 1 templates | [pilot charter](../templates/pilot-charter.md), [test-set spec](../templates/test-set-spec.md), [eval report](../templates/eval-report.md), [human-review design](../templates/human-review-design.md), [acceptable-use policy](../templates/acceptable-use-policy.md) | [16.5](../lessons/module-16/lesson-05.md) |
| 6 | **One-page board pre-read**, **integration check**, notes of the **hardest-finding rehearsal**, **decision record**, **handover** with the 15-minute monthly check | [steering pack](../templates/steering-pack.md), [integration check](../templates/integration-check.md), [decision record](../templates/decision-record.md), [handover pack](../templates/handover-pack.md), [operating rhythm](../templates/operating-rhythm.md) | [16.6](../lessons/module-16/lesson-06.md) |

## Steps

1. Read the brief and the data room's INDEX; write the charter, the hour budget and the first read; interview Ronit (16.1).
2. Write the staff-meeting script; interview at least four people including Lina; count access; follow the money; send the same-day note; write the findings memo (16.2; optional Track B: `discovery.py`).
3. Build the baseline with labels; list the money; screen the candidates; write the case in hours; prepare and run the funder call with Ronit leading; call Vova (16.3).
4. Write the compression table and the legal map with questions for counsel; verify the offers yourself on today's date; write the boundary; run the afternoon fix with Yossi (16.4).
5. Date the thresholds; build and test both workflows; measure what the de-identification check misses; write the one-page policy (16.5; optional Track B: `build/deid_check.py`).
6. Write the pre-read; run the integration check; rehearse the hardest finding with Ronit twice; run the board item; write the decision record and the handover (16.6).
7. Score your set with the rubric below **before** you open the hidden truth and the expert set in 16.6; then compare.

Time: about 3 hours beyond the lessons' own exercises, most of it in steps 6 and 7. The point of this engagement is that the whole set fits in 40 real hours; if yours took far more, find which documents grew past what a 30-person organization reads.

## Self-assessment rubric

| Criterion | What "strong" looks like | What "weak" looks like |
|---|---|---|
| Entry and scope | One page signed by email; "safely" where the director put it; an urgent-finding rule written before the data was opened; 40 hours budgeted with people and access first | No charter "because it's pro bono"; the board's "use AI" adopted as the objective; hours spent on documents |
| Discovery | People shown, not asked about tools; non-attribution kept; volunteers and a parent included; access counted against roles; the money traced | A second survey; names in the memo; the parent treated as a data source or skipped; "46 accounts" without what to do |
| The real problem | The funder's template identified as the writing bottleneck and changed by a conversation; the access exposure and personal-account use found and ranked above "adoption" | AI proposed to write 120 narratives faster; the exposure listed as a footnote |
| Compression | Documents shrunk to tables and pages; every step touching people, access, the boundary and the tests kept at full weight, and the table says which | The method skipped wholesale "because it's small", or run at full size until the hours ran out |
| Law and counsel | Applies / does not apply / open, each with a source; security level and DPO duty routed to counsel as specific questions; nothing stated as legal advice | "Small nonprofits are exempt"; "we are now at basic level" announced; no lawyer asked |
| Tools and money | Offers verified on the vendors' pages with dates and exclusions; the free tool already owned used first; money found before money asked; hours and shekels kept apart | A paid tool bought on a blog post; a "free for nonprofits" tool that trains on uploads; freed hours shown as cash |
| Build and eval | Thresholds dated first; zero invented numbers enforced; traps run three times; each language judged by a reader; failures fixed in a versioned change; the person as the control | Thresholds after results; one run per trap; "the Amharic looks fine"; the tool's STOP treated as the control |
| Policy | One page, readable in five minutes, owner and review date, each rule mapped to a Stage 1 document, read aloud with staff | Ten documents for 30 people, or a template copied without the boundary |
| Recommendation and follow-through | One decision first; recommend-againsts on the page; the sponsor's own mistake delivered privately and told by her; a named 15-minute monthly check and a second administrator | A demo; the chair's ambition answered with a purchase; "IT will monitor" |
| Integration | Counts, money, dates and owners agree across all six deliverables; at least three contradictions found and fixed | The same number three ways; a control nobody runs |

## Model answer

<details><summary>Model answer</summary>

The expert's deliverable set is in the module download, `labs/module-16/expert/` ([README](../labs/module-16/expert/README.md)):

- [01 · Charter and first week](../labs/module-16/expert/01-charter-and-first-week.md)
- [02 · Findings memo](../labs/module-16/expert/02-findings-memo.md)
- [03 · Baselines, shortlist and the call with the funder](../labs/module-16/expert/03-baselines-and-shortlist.md)
- [04 · The compressed plan, the law for a small amuta and the data boundary](../labs/module-16/expert/04-compressed-plan-and-boundary.md)
- [05 · Two workflows, their test, and the policy pack on one page](../labs/module-16/expert/05-workflows-and-policy-pack.md)
- [06 · Board readout, decision record and handover](../labs/module-16/expert/06-board-readout-and-handover.md)

Every number computed from the data room is real and reproducible (`discovery.py`, `build/deid_check.py`); the AI test results are an illustrative worked example and say so. Lesson 16.6 reveals what was really going on at Open Hands and three futures; read them only after scoring yourself.

</details>
