---
id: "18.2"
module: 18
minutes: 20
practice_minutes: 900
prerequisites: ["18.1", "03.7", "03.8", "05.1", "07.1", "07.9"]
objectives:
  - "Produce the full deliverable set for an unseen engagement — charter to handover — and score each piece against the capstone rubric before anyone else reads it."
  - "Keep one register of every number, date and owner the set relies on, so the same fact reads the same everywhere."
  - "Run the integration check: trace every claim's timing to the readiness assessment and the roadmap, and every human control to its cost line and the people who staff it."
  - "Decide for each contradiction whether it changes a decision, and disclose those that do instead of fixing them quietly."
volatility: concept
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): course 7, AI Transformation Advisory Package — integrate, document, present"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "IBM Lead AI Transformation: Strategy, Governance, and Execution Professional Certificate (Coursera)"
    url: https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution
last_verified: "2026-11-03"
---

# 18.2 · The full deliverable set and the integration check

Twelve documents that are each sound on their own can still tell a board two different stories. The ROI model counts a benefit from September that the roadmap cannot deliver before January; the pilot charter promises that a person checks every draft, and nobody's hours pay for it. In this lesson you build the whole Tzurim deliverable set, keep a single register of the facts it relies on, score each piece against the capstone rubric, and run the integration check across all of it. At the end you have a deliverable set you would sign, an integration check with its control and timing traces, and your own rubric score.

## The situation

You are in phases 2 and 3 of the Tzurim engagement: your charter is agreed, discovery is behind you or under way, and the board meets on 4 May. The [capstone project](../../projects/m18-capstone.md) lists the deliverables and the rubric; the [capstone checklist](../../labs/module-18/capstone-checklist.csv) in the module download tracks them with the template and the lesson that taught each one.

Every earlier engagement ended with an integration check in its NN.6 lesson. There it was one step of the readout. Here it is the main quality gate, because there is no lesson between your discovery and your board to tell you whether the pieces agree. IBM's consulting capstone has a stage called "integrate, document, present"; this lesson is that stage with real traces behind it.

The worked examples below come from Kinneret Plastics ([13.6](../module-13/lesson-06.md)) and Harbor & Pine ([07.1](../module-07/lesson-01.md)), not from Tzurim. Using Tzurim would reveal what you are meant to find yourself.

## What to do

### Step 1 — Assemble the set in the order the evidence was made

Write the deliverables in the order the method produces them, not the order the board will read them. Each later document stands on an earlier one, and a contradiction is easiest to fix where it starts.

| Deliverable | Template | Taught in | Stands on |
|---|---|---|---|
| Charter | [engagement charter](../../templates/engagement-charter.md), [scope boundary](../../templates/scope-boundary.md) | 01.2, 01.3 | The brief, the sponsor interview |
| Findings memo | [findings memo](../../templates/findings-memo.md), [data profile](../../templates/data-profile.md) | 02.2–02.7 | Interviews, profiling, baselines |
| Readiness assessment | [readiness assessment](../../templates/readiness-assessment.md) | 02.6 | Findings; the bar dated before vendor evidence |
| Portfolio and ROI | [opportunity map](../../templates/opportunity-map.md), [use-case scorecard](../../templates/use-case-scorecard.md), [ROI model](../../templates/roi-model.md) | 03.1–03.7 | Findings, readiness, finance's numbers |
| Roadmap | [roadmap](../../templates/roadmap.md) | 03.8 | Portfolio, readiness, capacity |
| Policy pack | [AI inventory](../../templates/ai-inventory.md), [acceptable-use policy](../../templates/acceptable-use-policy.md), [approved/restricted use list](../../templates/approved-restricted-use-list.md), [tools and data classes](../../templates/tools-and-data-classes.md), [claim read-back](../../templates/claim-read-back.md), [DPIA for AI](../../templates/dpia-for-ai.md), [risk register](../../templates/risk-register.md), [regulatory map](../../templates/regulatory-map.md), [governance charter](../../templates/governance-charter.md), [AI intake register](../../templates/ai-intake-register.md) | 04.1–04.8 | Findings (what is already in use), portfolio |
| Pilot and eval | [pilot charter](../../templates/pilot-charter.md), [value measurement plan](../../templates/value-measurement-plan.md), [test-set spec](../../templates/test-set-spec.md), [eval report](../../templates/eval-report.md) | 05.1–05.7 | Portfolio choice, policy pack, data |
| Adoption plan | [workflow redesign](../../templates/workflow-redesign.md), [training session plan](../../templates/training-session-plan.md), [champions playbook](../../templates/champions-playbook.md), [adoption dashboard spec](../../templates/adoption-dashboard-spec.md), [comms plan](../../templates/comms-plan.md) | 06.1–06.5 | Pilot design, people findings |
| Decision-ready case | [decision-ready case](../../templates/decision-ready-case.md), [steering pack](../../templates/steering-pack.md) | 03.9, 07.1 | Everything above |
| Decision record | [decision record](../../templates/decision-record.md) | 07.2 | The board meeting |
| Handover | [handover pack](../../templates/handover-pack.md), [operating rhythm](../../templates/operating-rhythm.md), [deliverable map](../../templates/deliverable-map.md) | 07.6, 07.9 | The decision |

Version every file and date it. "Findings memo v1.1, 4 March" is a fact you can trace; "findings memo (final)" is not.

### Step 2 — Keep one register of facts

Before the integration check, build a **register**: one row for every number, date and owner that appears in more than one document. It is the cheapest tool in this lesson and it catches most contradictions before they happen.

| Fact | Value | Label | Source (file, query, person, date) | Owner | Used in |
|---|---|---|---|---|---|

A Kinneret excerpt, written for this lesson from 13.6:

| Fact | Value | Label | Source | Owner | Used in |
|---|---|---|---|---|---|
| Unplanned downtime 2026 | 11,932 h | Measured | ProdTrack export, stop to restart | Ops excellence | Memo, case, readout |
| Moulds' share of lost hours | 46% | Measured (reasons as coded) | Same | Ops excellence | Memo, verdict, readout |
| Cost of an unplanned hour | ₪181 blended | Directional | CFO: ₪310 × 40% loaded + ₪95 assumed × 60% | CFO | Case, readout |
| Foundation budget | ₪730,000 in three stages | Assumed (quotes) | Case v2 | CFO, VP operations | Case, verdict, readout, decision record |
| Plant G recording start | 30 June 2027 | Plan | Protocol with the works committee | Plant G manager | Case, protocol, readout |

The register is also your defence in the meeting: when a director asks "where does ₪181 come from?", the answer is one row.

### Step 3 — Score each piece against the rubric before you integrate

Score every deliverable with the [capstone rubric](../../projects/m18-capstone.md) (0–3 per criterion) and write one sentence of evidence per score. Do this before the integration check, while you still remember what each document was meant to do. A piece that scores 1 on its own criterion will not be fixed by the integration check; rewrite it first.

Two rules make self-scoring honest:

- **Score the document, not your intention.** If the findings memo does not say how a number was measured, it does not get the evidence point, even if you know.
- **Quote the line that earns the score.** If you cannot quote it, the score is lower than you think.

### Step 4 — Run the integration check

Use the [integration check](../../templates/integration-check.md) template ([07.1](../module-07/lesson-01.md), [07.9](../module-07/lesson-09.md)). Start from what the decision-makers will rely on — numbers, dates, scope, controls — and read every document that mentions each item side by side, question first.

**The contradiction log.** For each pair that disagrees: which is right now, whether it changes a decision, the resolution, the owner. At Kinneret the check before the pre-read found three ([13.6](../module-13/lesson-06.md)):

| ID | What is relied on | A says | B says | Right now | Changes a decision? | Resolution |
|---|---|---|---|---|---|---|
| IC-01 | Plant G recording start | Case: 30 April | Protocol: nothing changes before the joint committee meets there on 6 April | Protocol | Yes | 30 June in every document, with the reason |
| IC-02 | Value of fewer night calls | Draft: "₪14,000 a year saved" | ROI rule: freed hours are capacity unless a cost line falls | ROI rule | No | Removed the shekels; reported as capacity |
| IC-03 | Assistant logs | Protocol: "anonymous" | Admin console stores logins | Console | Yes (a promise to workers) | "Stored without user id after export, 90 days"; settings request to IT before shadow use |

**The control trace.** Every human control in the set — a review step, a spot check, an approval, an on-call line — traced to a named person, the hours it takes and the cost line that pays for them. A control with no hours is a control that will be skipped under load ([05.5](../module-05/lesson-05.md)). From the template's Harbor & Pine example: the operating rhythm needed about 27 hours a month; ROI model v3 counted about 100 hours a year; the gap, about 220 hours a year, was netted from the capacity benefit in the July re-forecast.

| Human control | Person | Hours | Cost line in the model | Gap |
|---|---|---|---|---|

Ask for each control: who does it on the busiest day of the year, and what do they stop doing to make room?

**The timing trace.** Every claim of benefit traced to the date the case says it lands, the date readiness allows it, and the date the roadmap schedules it. A benefit that lands before the roadmap delivers its cause, or before readiness allows it, is the most common integration failure in a board pack.

| Claim | Lands when (case) | Readiness allows from | Roadmap schedules | Gap |
|---|---|---|---|---|

The Kinneret example: the Arava plan claimed on-time-in-full of 92% in Q3 2027 from night mould response, restored PMs and quality cover for first-article approval at night from 1 April. Readiness and the roadmap supported the first two; night quality cover was the quality manager's headcount decision and nobody owned it. The timing trace turned that into a line in the decision record with an owner, instead of a promise to the customer that rested on nobody.

Two more timing questions catch what the table misses:

- **When is the outcome measured, not only when is the change made?** A process change made in June may only show in a figure computed in October.
- **What external calendar does the claim cross?** Exam periods, holidays, budget cycles, a vendor's price expiry, a customer's deadline.

### Step 5 — Fix, flag or disclose

Each contradiction ends in one of three ways:

- **Fix** it everywhere when it changes no decision (a wording, a rounding, a version).
- **Flag** it in the pre-read when the right answer is not yet known, with who will know and when.
- **Disclose** it to the sponsor before the pre-read, and put it to the forum as its own line, when it changes a decision. Never fix those quietly ([07.3](../module-07/lesson-03.md)): a sponsor who learns in the meeting that the number moved stops trusting every other number.

### Step 6 — Close the set

Update the [capstone checklist](../../labs/module-18/capstone-checklist.csv) with versions, dates, scores and the integration-check IDs each document took part in. Re-score any piece you changed. Then write the [deliverable map](../../templates/deliverable-map.md): which document is the source of truth for which fact, who owns it after you leave, and when it is next reviewed.

## Watch out

- **Integrating at the end only.** A contradiction found the night before the pre-read becomes a quiet edit. Run the register from phase 1 and the full check at least a week before the pre-read.
- **Checking numbers but not promises.** The costliest contradictions are commitments to people (works councils, students, staff) that a later document quietly breaks.
- **A control trace that stops at the role.** "The service team reviews" is not a trace; a person, hours and a cost line is.
- **Counting a benefit from the day of the decision.** Trace it to the date the cause exists and the date the outcome is measured.
- **Self-scoring generously.** If you cannot quote the line that earns the score, lower it.
- **Fixing a decision-changing contradiction quietly.** Disclose it to the sponsor first and put it to the forum.

## Your turn

### Inputs

- Everything you produced in [18.1](lesson-01.md) and since: interviews, analyses, drafts.
- The [data room](../../labs/module-18/data-room/INDEX.md) and the [cast](../../labs/module-18/personas/README.md) (module download), as you need them.
- The [capstone project](../../projects/m18-capstone.md) (deliverables and rubric) — read the brief and the rubric only, not the reveal block.
- The [capstone checklist](../../labs/module-18/capstone-checklist.csv) and the [integration check](../../templates/integration-check.md) template (spreadsheet version in the module 7 download, `labs/module-07/integration-check.csv`).

### Steps

1. Complete the deliverable set from the charter to the adoption plan and the decision-ready case draft, versioned and dated.
2. Build the register of facts: every number, date and owner used in more than one document, with label and source.
3. Score each deliverable against the rubric, quoting the line that earns each score; rewrite any piece that scores 1 or 0.
4. Run the integration check: the contradiction log, the control trace (every human control) and the timing trace (every claim of benefit).
5. Fix, flag or disclose each contradiction; write the note to the sponsor for any that changes a decision.
6. Update the checklist and write the deliverable map.

### Time

About 15 hours across phases 2 and 3: 9 for the deliverables beyond what earlier lessons' exercises gave you, 1 for the register, 1.5 for scoring, 2.5 for the integration check and its traces, 1 for fixes, the disclosure note and the map.

### Done when

- [ ] Every deliverable in the project's list exists, versioned and dated, built on the template the checklist names.
- [ ] The register has every number, date and owner that appears twice, each with a label and a source.
- [ ] Every rubric score quotes the line that earns it; nothing scored below 2 is left unrevised.
- [ ] The contradiction log has at least four entries, each with "changes a decision?" answered and a resolution.
- [ ] Every human control appears in the control trace with a person, hours and a cost line, or a stated gap.
- [ ] Every claim of benefit appears in the timing trace with its case date, its readiness date and its roadmap date, and the date the outcome is measured.
- [ ] Any decision-changing contradiction was disclosed to the sponsor in writing before the pre-read.

<details><summary>Reference answer</summary>

This reference is built on Kinneret Plastics (module 13), so it reveals nothing about Tzurim. The expert's Tzurim integration check is in the project's reveal block, after you submit.

**Contradiction log (Kinneret, 17 March 2027, before the pre-read):** IC-01 Plant G recording 30 April (case) vs the protocol's joint-committee meeting on 6 April → 30 June everywhere, changes a decision, disclosed to Dalia and in the pre-read. IC-02 "₪14,000 a year saved" from night calls → removed; capacity, not cash; no decision changed. IC-03 assistant logs "anonymous" vs the console storing logins → "stored without user id after export, 90 days" and a settings request to IT before shadow use; changes a promise to workers, disclosed to the works committee chair. IC-04 Arava plan: OTIF 92% in Q3 depends on night quality cover, which no document assigns → a line in the decision record with the quality manager as owner and 1 April as the date; changes a decision.

**Control trace (excerpt):**

| Human control | Person | Hours | Cost line | Gap |
|---|---|---|---|---|
| Monthly re-run of the readiness audit | Half-time analyst | ≈ 4 h a month | Internal time, not in the ₪730,000 | None; named in the handover |
| Re-run of the assistant's test set after every pack change | Maintenance manager with the analyst | ≈ 3 h per change | Not in the case | Added to the operating rhythm; senior technician co-owns from June |
| Night quality cover for first-article approval | Quality manager | A night inspector's shift | None before the check | Gap → decision record (IC-04) |

**Timing trace (excerpt):**

| Claim | Lands when (case) | Readiness allows from | Roadmap schedules | Gap |
|---|---|---|---|---|
| Arava OTIF 92% | Q3 2027 | Night mould response from April; QA cover unowned | 1 April | Owner missing (IC-04) |
| Coded failures at Plant G | Case v1: from May | Protocol: after 6 April meeting, then training | 30 June | Fixed (IC-01) |
| Predictive-maintenance re-decision | January 2028 | Only on coded failures and sensor history, which start in 2027 | Re-decision with criteria and a proof-of-concept protocol | Decision is "whether to run a proof of concept", not "whether to buy"; written so in the decision record |

**Self-score note:** the strongest single habit is quoting the line. "Readiness: 3 — the bar is dated 'written on Sunday 14 February, before the vendor's presentation' and each criterion is graded with evidence" is a score you can defend.

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting): course 7's "integrate, document, present" (named, not re-taught); IBM, [Lead AI Transformation certificate](https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution).
- Field kit: [03.7 · The ROI model](../module-03/lesson-07.md), [03.8 · The roadmap](../module-03/lesson-08.md), [05.1 · The pilot charter](../module-05/lesson-01.md), [05.5 · Human-in-the-loop design](../module-05/lesson-05.md), [07.1 · The steering pack](../module-07/lesson-01.md), [07.3 · Delivering bad news upward](../module-07/lesson-03.md), [07.9 · Handover](../module-07/lesson-09.md); [13.6 · Readout and debrief](../module-13/lesson-06.md) (the Kinneret check).
- Templates: [integration check](../../templates/integration-check.md), [deliverable map](../../templates/deliverable-map.md), and every template in the table in Step 1.
- Capstone: [the project and rubric](../../projects/m18-capstone.md); [capstone checklist](../../labs/module-18/capstone-checklist.csv) (module download). Next: [18.3 · The executive presentation](lesson-03.md).
