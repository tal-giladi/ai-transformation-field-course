---
id: "14.3"
module: 14
minutes: 18
practice_minutes: 120
prerequisites: ["14.2", "02.4", "03.2", "03.3", "03.9"]
objectives:
  - "Measure an agent's resolution rate under two definitions and put a quality check beside the stricter one."
  - "Restate a board target as a measured baseline, a dated target and a gate."
  - "Size the people an agent's controls need (approvals, reviews, handoffs) against the people who have the time."
  - "Write a shortlist and a one-page case in which the real bottleneck, not the stated ask, sets the order."
volatility: concept
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): opportunity identification, readiness, decision-ready case"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "IBM Lead AI Transformation Professional Certificate (Coursera): measuring AI value"
    url: https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution
last_verified: "2026-11-03"
---

# 14.3 · Diagnosis

The board was told "50% resolved". The dashboard says 63%. The customer whose credit was promised and then taken back would say her issue was never resolved at all. In this lesson you pick one definition of "resolved", measure it on the beta, put a quality check beside it, size the people that any safe version of the agent will need, and decide what the real bottleneck is. At the end you have a baseline sheet, a shortlist with verdicts and a one-page case for Revital and the CEO.

## The situation

Sunday 13 to Thursday 17 December 2026. Your findings memo went to Revital on 10 December. She asked for two things before Christmas: a number for "resolved" she can defend, and something short she can show Yaron, who has given you 20 minutes on Thursday at 08:30 before a board-prep call. The account manager for Tavor Engineering has also agreed that you can call Tavor's office manager, Svetlana Mor, whose credit was reversed on 23 November.

IBM's value course asks you to measure an indicator the budget owner already reviews, beside a quality measure, against a baseline. Here the indicator exists, and its definition is the problem. You measure it the way [02.4](../module-02/lesson-04.md) taught (three systems, three numbers), then screen the candidates with [03.2](../module-03/lesson-02.md) and [03.3](../module-03/lesson-03.md), and write the case with [03.9](../module-03/lesson-09.md).

## What to do

### Step 1 — Measure "resolved" two ways

The dashboard counts a conversation as resolved when it ends without the customer pressing "Talk to a person". That includes customers who simply leave, and bug reports the agent passed to engineering. Write a stricter definition that a support person would accept:

> **7-day resolution:** the conversation ended closed or abandoned, and the same customer opened no ticket and no new conversation on the same intent within 7 days.

Join `assist-beta/sessions.csv` to itself and to `support/tickets.csv` on customer and intent. The worked example:

| Definition | Beta, 11 Oct – 26 Nov, 1,599 sessions |
|---|---|
| Dashboard ("no handoff") | 63.2% |
| 7-day resolution | **35.5%** |

By intent, 7-day: invoice questions 50.2% (448 sessions), credits 46.5% (187), notification questions 40.0% (60), payroll 32.3% (164), how-to 31.6% (354), plan changes 22.5% (142), bugs 9.8% (153, rightly handed to engineering), 2FA 4.3% (70: the agent cannot reset). By language the spread is small: Hebrew 37.3%, Russian 35.4%, English 33.7%, Arabic 33.3%.

### Step 2 — Put a quality check beside it

Look for the best number in the table, and distrust it. Downgrade questions show 81.0% 7-day resolution: customers who were wrongly credited did not come back. A resolution rate measures whether people stopped asking, not whether the answer was right. Pair it with a quality measure you can afford: **a weekly sample of 20 resolved conversations read against policy by a shift lead** (about 20 minutes), counting wrong actions and wrong answers. That pairing is the rule from [05.1](../module-05/lesson-01.md): every efficiency metric gets a quality metric.

### Step 3 — Hear "resolved" from the person affected

Call Svetlana (roleplay: [Svetlana Mor](../../labs/module-14/personas/svetlana-customer-admin.md); no-roleplay path: [the transcript](../../labs/module-14/personas/transcripts/svetlana-customer-admin.md)). Her conversation of 22 November is "resolved" on the dashboard. Find out what happened in her words, whether her issue was resolved in her terms, what she shared in the chat, what would have made it right, and one thing the transcript's interviewer never asked: in which language she uses Lumen, and whether she knew she was talking to an AI. Promise only what you can deliver, with a date.

### Step 4 — Restate the target

"50% of support contacts resolved without a person by end of Q2 2027" has three problems: no definition, no baseline, and a denominator ("all support contacts") that includes phone and email the agent never sees. Restate it in the form a gate can check:

> **7-day resolution of Lumen Assist conversations from 35.5% (beta) to 45% by 30 June 2027, with no rise in wrong actions found in the weekly sample.**

Label the 45% honestly: it is **assumed**. It is roughly what you would get if credits and Starter plan changes (now mostly handed off) and the weakest how-to articles started to behave like invoice questions. The monthly review replaces the assumption with the measured curve.

### Step 5 — Size the people the controls need

An agent with approvals, reviews and handoffs is a workload for people. Before you design a single control (14.4), measure the capacity it will draw on:

| Item | Per working day | Label |
|---|---|---|
| Beta sessions | 42 | measured |
| Beta handoffs to people | 15.7 | measured |
| GA requests, Starter and Growth (Product's projection) | ~80: 50 look-ups, 11 credits, 6 plan changes, 3 2FA resets, 10 bug tickets | directional |
| Approval capacity: two shift leads × 30 minutes for approvals (`people/support-shifts.csv`) | ~60 min ≈ 30 approvals at 2 min | measured |
| Credits and plan changes on one approver | ~17 a day ≈ 34 min | directional |
| Credits, plan changes and 2FA resets on approval, with Enterprise | ~40 a day | directional: over capacity |
| Daily review of the agent's full trace | 20 min | assumed |

The last two rows decide a lot of 14.4. An approval nobody has time to read is a rubber stamp, and you met the reasons in [05.5](../module-05/lesson-05.md). Approvals have to be spent where they buy safety, for as long as they are needed, and no longer.

### Step 6 — Name the real bottleneck

Line up what you know. The model gave the right downgrade answer whenever its source was right. The wrong credits came from an unapproved document, a limit that lived in the prompt, a stop that did not stop and nobody reading the log. Eleven agents act on or near customers under identities nobody can attribute, three of them under tokens whose creators have left. The bottleneck is **authority and visibility**, not model quality: who may do what, enforced where, as whom, seen by whom, stopped how. Everything on the shortlist depends on fixing that first.

### Step 7 — Screen and shortlist

Use the [agentic opportunity frame](../../templates/agentic-opportunity-frame.md) for each candidate, step by step, and the [use-case scorecard](../../templates/use-case-scorecard.md) for the verdict. One candidate is not AI at all; one is "never".

| Candidate | Verdict | Condition |
|---|---|---|
| A. Lumen Assist GA for Starter and Growth, with a permission map and staged autonomy | Go with conditions | Own identity; limits enforced in the tool layer; a tested stop; approved sources in every language; disclosure in every language; must-refuse tests passing |
| B. The fleet register and one identity per agent (a register, a token rule, offboarding) | Go | No AI involved: this is plain governance, and A depends on it |
| C. Renewal Rescue, the nightly CS automation | Go with guardrails | Own identity; Growth by plan; a cap; address on file; a weekly sample; a stop someone else can use |
| D. Assist for Enterprise | Not yet | Opt-in per customer after Shaked's questionnaire is answered; read-only first |
| E. The agent deleting data, or resetting 2FA without verification on file | Never delegate | Deletion stays the DPO's process; resets only through a channel already on file |

### Step 8 — Write the one-page case and test it on the CEO

Use the [decision-ready case](../../templates/decision-ready-case.md): a one-sentence ask, the evidence labelled measured, directional or assumed, the cost, the cost of waiting, and what a "no" means. Then take it to Yaron for 20 minutes (roleplay: [Yaron Ben-David](../../labs/module-14/personas/yaron-ceo.md); no-roleplay path: [the transcript](../../labs/module-14/personas/transcripts/yaron-ceo.md)). Lead with what the board needs, give him one sentence, deliver the 22 November facts in two sentences with the fix, and ask what he would accept instead of "everything on 9 February". Ask one thing the transcript's interviewer did not: when the next investor update goes out and what number it needs.

**Track B (Python).** Section 6 of `discovery.py` computes both resolution rates and the outcome mix; extend it to group by intent and language as in the table above (a dozen lines). Python is worth it because the 7-day rule is a self-join on timestamps that a spreadsheet does slowly, and you will re-run it every month as the gate measure.

## Watch out

- **Arguing about the number instead of the definition.** 63% and 35.5% are both correct. Agree the definition first; the number follows.
- **A resolution rate with no quality check.** The best-looking intent (downgrades, 81%) was the one where the agent was wrong. Always pair it with a sample read against policy.
- **Promising the board's target.** 45% by June is an assumption with a monthly gate, not a commitment. Say so on the page.
- **Designing controls before counting people.** If the approvals in your design exceed 30 a day, the design fails on Tuesday, not in an audit.
- **Shortlisting only AI.** The highest-value item on Lumen's list (B, the register and identities) has no model in it.
- **Defending the company to the customer.** Svetlana needs an apology and a dated answer about her data, not an explanation of the architecture.

## Your turn

### Inputs

- Data room (module download): `assist-beta/sessions.csv`, `support/tickets.csv`, `people/support-shifts.csv`, `product/assist-ga-design.md`, `company/board-update-2026-10.md`, `company/assist-beta-dashboard-2026-11.md`; your inventory and memo from 14.2.
- Personas: [Svetlana Mor](../../labs/module-14/personas/svetlana-customer-admin.md) and [Yaron Ben-David](../../labs/module-14/personas/yaron-ceo.md), or their [transcripts](../../labs/module-14/personas/README.md); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [agentic opportunity frame](../../templates/agentic-opportunity-frame.md), [use-case scorecard](../../templates/use-case-scorecard.md), [decision-ready case](../../templates/decision-ready-case.md), [value measurement plan](../../templates/value-measurement-plan.md).
- Track B: `discovery.py`.

### Steps

1. Measure resolution under both definitions, by intent and by language (Track A: a pivot table with a helper column for "repeat within 7 days"; Track B: extend `discovery.py`).
2. Define the weekly quality sample.
3. Interview Svetlana; write down what "resolved" meant for her.
4. Restate the target with a baseline, a date and a gate.
5. Fill the capacity table and mark each row measured, directional or assumed.
6. Write the bottleneck in three sentences; screen five candidates; write the shortlist.
7. Write the one-page case; test it on Yaron (roleplay or transcript).

### Time

120 minutes: 35 for the measurement, 20 for the interview, 20 for the capacity table, 20 for the shortlist, 25 for the case and the CEO.

### Done when

- [ ] Both resolution rates are computed on the 1,599 sessions, with the 7-day definition written out.
- [ ] A quality check sits beside the resolution rate, with who reads what and how often.
- [ ] The target has a baseline, a date, a gate, and the label "assumed".
- [ ] The capacity table compares approvals needed with approvals available.
- [ ] The shortlist includes one non-AI item and one "never delegate".
- [ ] The one-page case says what a "no" means, and you know what the CEO needs by March.

<details><summary>Reference answer</summary>

The expert's version is `labs/module-14/expert/03-baselines-and-shortlist.md`. The parts that carry the weight:

**Baseline.** Dashboard 63.2%; 7-day resolution 35.5% (1,599 sessions). By intent: invoices 50.2%, credits 46.5%, notifications 40.0%, payroll 32.3%, how-to 31.6%, plans 22.5%, bugs 9.8%, 2FA 4.3%. Downgrades 81.0%, the trap: the wrong credits made customers stop asking. Quality check: 20 resolved conversations a week read against policy by a shift lead.

**Target restated.** 7-day resolution from 35.5% to 45% by 30 June 2027, with no rise in wrong actions in the weekly sample; 45% assumed; monthly gate.

**Capacity.** ~17 approvals a day for credits and plan changes (34 minutes) against ~30 available; ~40 a day if 2FA and Enterprise were also on approval: over capacity. Daily trace review 20 minutes.

**Bottleneck.** Authority and visibility: the model answered correctly whenever its source was correct; the harm came from an unapproved source, a prompt-only limit, a stop that did not stop, no daily review and an identity nobody could attribute.

**Shortlist.** A go with conditions; B go (no AI); C go with guardrails; D not yet; E never delegate.

**One-page case (ask).** Launch Lumen Assist at Lumen Live for Starter and Growth under a permission map, money on approval for two weeks, then wider on evidence; Enterprise later by opt-in. Cost: about six of the engineer's twelve budgeted weeks, about an hour a day of shift-lead time in weeks 1–2. What a "no" means: Lumen Live shows a demo and the beta continues with today's weaker controls.

**What the interviews add.** Svetlana: her "resolved" conversation cost her two days and an apology nobody sent; she did not know the assistant was an AI because the disclosure line is empty in Russian. Yaron: Enterprise out is acceptable if Shaked is protected; the transcript's interviewer did not ask about the March investor update, which wants a measured number from real customers: a reason stage 2's gate must be dated before March.

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting) and [Lead AI Transformation certificate](https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution) (value measures, decision-ready case): named, not re-taught.
- Field kit: [02.4 · Measuring a baseline](../module-02/lesson-04.md), [03.2 · Agent or not](../module-03/lesson-02.md), [03.3 · The fast screen](../module-03/lesson-03.md), [03.9 · The decision-ready case](../module-03/lesson-09.md), [05.1 · The pilot charter](../module-05/lesson-01.md), [05.5 · Human-in-the-loop design](../module-05/lesson-05.md).
- Templates: [agentic opportunity frame](../../templates/agentic-opportunity-frame.md), [use-case scorecard](../../templates/use-case-scorecard.md), [decision-ready case](../../templates/decision-ready-case.md), [value measurement plan](../../templates/value-measurement-plan.md).
- Previous: [14.2 · Discovery](lesson-02.md). Next: [14.4 · The hard part: agent authority](lesson-04.md).
