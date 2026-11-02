# Discovery at Harbor & Pine

The module 2 practical: the full discovery pack for Harbor & Pine, from the stakeholder map to the findings memo, made consistent so that every number in the memo traces back through the readiness assessment, the data profiles and the baselines to a file or a person. Most pieces start as your answers to lessons 02.1–02.7; the practical asks you to finish them, make them agree, and hold them to the standard of a CFO who will test one number at random. Plan 5 hours if you completed the lessons' "Your turn" tasks, longer if you did not.

## The brief

It is Tuesday 1 December 2026, day 30 of your plan as Head of AI and Operations Improvement at Harbor & Pine Ltd. Michal Peretz, the COO, meets Yoav Ben-Ami, the CEO, on 10 December to decide what to have working by the board meeting on 28 January 2027. She asks you for "the findings memo, and everything behind it, so that when Ronit picks a number I can show her where it comes from."

You have the Harbor & Pine data room (including the agents' one-week WhatsApp tally), the persona pack and everything you wrote in this module.

## Deliverables

| # | Deliverable | Template | Built in |
|---|---|---|---|
| 1 | Stakeholder map with the interview plan, updated after the interviews | [stakeholder map](../templates/stakeholder-map.md) | 02.1 |
| 2 | Interview notes for at least three interviews (Samir, Olga, Tamar), each fact marked seen / said / hearsay | [interview guide](../templates/interview-guide.md) | 02.2 |
| 3 | Paper-versus-practice list and task inventory (at least eight tasks) | [task inventory](../templates/task-inventory.md) | 02.3 |
| 4 | Baseline sheet (at least eight baselines, each with a definition card) and the time-study design | — (lesson 02.4's sheet) | 02.4 |
| 5 | Data profiles for at least four datasets, with verdicts and the questions for counsel | [data profile](../templates/data-profile.md) | 02.5 |
| 6 | Readiness assessment: bars, at least 12 findings, a verdict per use case | [readiness assessment](../templates/readiness-assessment.md) | 02.6 |
| 7 | Findings memo (two pages) with the check log of the AI draft in the appendix | [findings memo](../templates/findings-memo.md) | 02.7 |

## Steps

1. **Collect** your lesson outputs for deliverables 1–7. Where you skipped a "Your turn", do it now; the lessons' reference answers show the standard but are not yours to copy.
2. **Trace every number in the memo.** For each number, follow it back: memo → readiness finding → baseline or profile → file (or interview). Any number that stops before a file or a named interview is either fixed or removed. Mark persona-only facts ("Samir said…") as reported.
3. **Make the documents agree.** The same definitions (first response, WISMO, follow-up), the same numbers, the same dates and the same use-case letters everywhere. List every inconsistency you fix.
4. **Check the statuses.** Nothing marked verified in the readiness assessment rests only on an interview, a policy or a vendor document.
5. **Check the protection you promised.** No names next to workarounds anywhere in the pack; Samir and Tamar get the memo before Michal does (write the covering note).
6. **Self-assess** with the rubric below, then run the [coach prompt](../labs/common/coach-prompt.md) on the memo with the rubric as the checklist.

## Rubric

| Criterion | Strong | Weak |
|---|---|---|
| Stakeholder map | Includes the receiving team, file keepers, the board and the customer; two sentences each or "to learn"; stances with evidence; updated after interviews | The org chart with columns; needs guessed; stances as personality |
| Interviews | Walk-throughs of real recent work; every number's definition asked; the same-word test run; the channel question asked; facts marked seen / said / hearsay | Opinions and wish lists; leading questions; numbers taken as given; names asked for |
| Task inventory | Every volume and time has a source or "not measured"; tally limits stated; walk-on-paper verdicts; at least one "not yet a candidate" | Volumes guessed; bucket hours divided by tickets; every task a candidate |
| Baselines | Definition cards; KPI reproduced and shown beside the customer's wait; WISMO as a triangulated range; the delivery promise measured; a time study designed | One number per metric with no definition; the KPI or the category field taken as truth |
| Data profiles | Fitness for a named use; label question answered; stale copies and failed joins found; permission questions routed, not answered | "The data is good/bad" without a use; legal conclusions stated as fact |
| Readiness assessment | Bars before evidence; observation → consequence; dated; three statuses used honestly; verdict per use case with what would change it | Everything "verified"; one verdict for the company; a score |
| Findings memo | Answer in three sentences with a decision; claim–evidence–consequence; what we don't know; decisions table; AI draft checked with a log | Background first; numbers without sources; the AI draft's errors repeated; people blamed |
| Consistency | Every memo number traces to a file or named interview; documents agree | Different numbers for the same thing in different documents |

<details><summary>Model answer</summary>

The reference answers in each lesson are the model for deliverables 1–7: [02.1](../lessons/module-02/lesson-01.md) (15-row map, interview order), [02.2](../lessons/module-02/lesson-02.md) (notes table, same-word test, transcript critique), [02.3](../lessons/module-02/lesson-03.md) (ten-task inventory, paper vs practice), [02.4](../lessons/module-02/lesson-04.md) (eleven baselines, time study), [02.5](../lessons/module-02/lesson-05.md) (five data profiles, four questions for counsel), [02.6](../lessons/module-02/lesson-06.md) (15 findings, five verdicts) and [02.7](../lessons/module-02/lesson-07.md) (13-line check log, the memo). What the integrated pack adds:

**Consistency fixes a strong pack makes.**

- One definition of "where is my order?" everywhere: "31–44% across five signals; about two in five". The task inventory's WISMO volume, the readiness finding R-01 and memo finding 1 all point to baseline B7.
- One definition of follow-up: "same customer, same order (normalised), new ticket within 14 days of resolution" — 335 of 1,430 = 23.4% in the profile, R-04 and the memo. The interview notes' "people write again" is marked said and points to it.
- First response always shown as a pair: KPI 1.97 h (working-hours mean, Q3 email, business days) and customer 6.1 h (wall-clock median, all helpdesk channels).
- The WhatsApp tally labelled the same way everywhere: "hand tally, one week (18–22 Oct), estimates; 630 conversations, ~124 hours" — never "measured volume".
- Use-case letters A–E identical in the profiles, the assessment and the memo's decisions table.

**Trace of one memo number, as Ronit would ask for it.** "Vietnam and China orders promised from June arrived a median 11 days late" → readiness R-01 (verified, 18 Nov) → baseline B9 (definition: actual − promised, VN/CN, promised ≥ 1 June, delivered; n = 1,106) → `orders/orders.csv`, reproduced by `labs/module-02/baseline.py` section 6.

**Covering note to Samir and Tamar (30 November).** "Attached is the findings memo I will send Michal tomorrow. Nothing in it is attributed to either of you by name; where I used what you told me it says 'the support team' or 'logistics'. If anything is wrong or unfair, tell me by Thursday and I will fix it before it goes further."

</details>
