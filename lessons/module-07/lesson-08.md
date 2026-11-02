---
id: "07.8"
module: 7
minutes: 18
practice_minutes: 100
prerequisites: ["07.4", "05.6", "06.3"]
objectives:
  - "Turn a board's yes into work within 72 hours: confirmed minute, money released, team told, every condition with an owner and a date."
  - "Write a week-by-week phase-1 plan with goals, deliverables, owners, people-hours, money committed and the gate or condition each week checks."
  - "Write a one-page weekly report from real usage data that separates learning-week signals from gate evidence and asks for decisions."
  - "Treat a stage date as the earliest date, not a deadline, and record any departure from an exit condition."
volatility: concept
sources:
  - title: "IBM Lead AI Transformation: Strategy, Governance & Execution Professional Certificate (Coursera) — course 5, Lead AI Change (go-live is not the goal; train, transfer, sustain); course 6, Measure AI Value and Scaling Transformation (pilot isn't scale)"
    url: https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution
last_verified: "2026-11-02"
---

# 07.8 · The board said yes — now what

The board's yes is the moment most programmes lose a month: everyone assumes someone else is sending the purchase order, telling the team and booking the reviewers' time. In this lesson you run Harbor & Pine's phase 1 from the day after the board to the eve of gate 1: the first 72 hours, the staffing and money release, a plan for nine weeks with a goal and a check for each, the first weekly report written from the real usage export, and the week-3 decision where the calendar and the evidence disagree. At the end you have a phase-1 plan and two reports.

## The situation

This lesson steps back from April to the end of January. It is Friday 29 January 2027. Yesterday the board approved the drafts pilot within a three-year envelope of ₪267,000 and confirmed the steering committee's staging: ₪48,000 released now, ₪72,000 at gate 1 on Thursday 1 April ([07.4](lesson-04.md)). The same day the team ran the go-live dry run and walked all twelve agents through drafts on demand ([05.6](../module-05/lesson-06.md)). Go-live is Monday 1 February: drafts on demand for email and the web form in four languages, WhatsApp moving into the helpdesk and running in shadow mode. Training is 7–11 February ([06.2](../module-06/lesson-02.md)). The two seasonal temps' contracts ended on Sunday 31 January.

IBM's change course says go-live is not the goal, and its value course that a pilot is not scale. The gap it leaves, and this lesson fills, is the nine weeks between the yes and the first gate: who does what each week, what money moves when, and what the weekly page says.

## What to do

### Step 1 — The first 72 hours

Within three working days of the yes, close every item that makes the yes executable. Each one is small; together they decide whether week 1 starts on Monday.

| Item | What exactly | Who | By |
|---|---|---|---|
| Confirm the decision in writing | The board resolution matches the steering minute: amounts, conditions, gate date, who releases stage 2 | Pilot lead to Michal and Ronit | Fri 29 Jan |
| Release the money | PO to the integrator against stage 1 (₪48,000); invoice milestones tied to deliverables, not dates | Ronit | Fri 29 Jan |
| Tell the team, from their manager | Samir, not you: what starts Monday, that no cuts are in the case, that override marks are never used in performance reviews | Samir, with Michal | Sun 31 Jan |
| Give every condition an owner and a date | Out-of-hours support line (Avi, before go-live); privacy notice update and WhatsApp DPIA addendum (Ronit with counsel, 29 Jan); Arabic re-measured on 100 production drafts (pilot lead, before 1 Mar) | Pilot lead | Fri 29 Jan |
| Book people's time | Reviewers' and champions' hours in the rota, agreed with Samir; Olga's protected two hours a week | Samir | Sun 31 Jan |
| Set the reporting calendar | Weekly page every Thursday; monthly to the steering committee (Thu 25 Feb, Thu 25 Mar); gate pack out Sun 28 Mar | Pilot lead | Fri 29 Jan |
| Tell the board what happens next | One paragraph from Yoav to the board: start date, first measured numbers in April | Yoav (you draft) | Sun 31 Jan |

### Step 2 — Staff it, in hours, with the managers' agreement

A plan that says "Olga will check Russian drafts" without hours is a wish. Write each person's hours per week, from whose budget, agreed with their manager, and check the total against the team's capacity in the same weeks. February is off-peak, but the temps are gone and the volume is about double last May's.

| Person | Weeks 1–2 | Weeks 3–9 | What | Agreed with |
|---|---|---|---|---|
| Pilot lead | full time | full time | Release, reports, monitoring, shadow analysis | Michal |
| Olga Petrenko | 6 h | 4 h | Russian and Hebrew shadow ratings and spot audit; champion (2 h protected) | Samir |
| Lina Khoury | 5 h | 3 h | Arabic ratings and spot audit; champion | Samir |
| Shani Ohayon | 2 h | 2 h | Hebrew champion | Samir |
| Avi Mizrahi | 6 h | 2 h | Integration, switches, alerts, console rights | Michal |
| Integrator | 3 days in week 1, then on call | 2 days (WhatsApp, logging) | Connection, holdout, switch, logging, web-store lookup | PO |
| Training | — | 42 h total (14 × 3 h) in week 2 | Sessions and clinics (module 6) | Samir, Dana |

### Step 3 — Release the money against deliverables

Stage 1 is ₪48,000, and the case already tells you what it buys ([03.7](../module-03/lesson-07.md)). Tie each payment to a deliverable you can check, and track the burn weekly:

| Milestone | Payment | Checked by |
|---|---|---|
| Stage 1 live: drafts on demand, holdout, switch per channel and language, timeout to "no draft" | ₪16,000 | Samir: switch test passed in week 1 |
| WhatsApp shadow running; web-store order lookup for `HP-1…` numbers | ₪8,000 | Pilot lead: lookup returns an order for at least 90% |
| Logging and monitoring complete (05.7), cost alert live | ₪8,000 | Avi |
| Training and internal hours (agents, reviewers, labelling) | about ₪14,000 internal | Ronit (project code) |
| Contingency | about ₪2,000 | Ronit |

### Step 4 — Plan the nine weeks, one goal and one check each

Every week gets one goal, its deliverables, an owner, its hours and money, the condition or gate it checks, and the decision someone must take. The plan lives in the [phase-1 plan](../../templates/phase-1-plan.md) template (spreadsheet `labs/module-07/phase-1-plan.csv`, two example rows).

| Week | Dates | Goal | The check that week |
|---|---|---|---|
| 0 | 29–31 Jan | The yes becomes work | Board resolution = steering minute |
| 1 | 1–7 Feb | Stage 1 live; WhatsApp in shadow | Production-readiness lines closed; switch tested |
| 2 | 8–14 Feb | Training; shadow ratings; Arabic re-measure starts | Shadow exit condition on Sun 14 Feb (05.6) |
| 3 | 15–21 Feb | Stage 2 for WhatsApp *only if the exit is met*; gate measurement starts | Exit met per language and lookup ≥ 90% |
| 4 | 22–28 Feb | Monthly steering report (Thu 25 Feb) | Arabic condition due before 1 Mar |
| 5 | 1–7 Mar | Arabic result; first full month of gate readings | Acceptance per channel × language |
| 6 | 8–14 Mar | Change control running | Every change in the log with its tests |
| 7 | 15–21 Mar | (The incident: 07.5) | Runbook |
| 8 | 22–28 Mar | Steering adopts the incident review (22 Mar); adoption pre-read; gate pack out Sun 28 Mar | Gate (a)–(d) and the adoption gate, per segment |
| 9 | 29 Mar – 1 Apr | Gate 1 on Thu 1 Apr | 07.2 |

Learning weeks 1–2 are excluded from the gate readings by the value measurement plan ([05.1](../module-05/lesson-01.md)). Say so on every report, or someone will quote week 1 as a result.

### Step 5 — The weekly report: one page, every Thursday

Five blocks, always in the same order, so a reader sees at once what changed:

1. **Status in one line** (on track / at risk / off track) and why.
2. **Signals** this week, labelled: usage (qualified events, people using it, by queue), quality (spot audit), issues opened and closed. In learning weeks, signals only; no gate numbers.
3. **Decisions needed**, from whom, by when.
4. **Risks and conditions**: each condition from the minute with its status.
5. **Money**: committed and spent against stage 1; next week's plan.

Write the first one from the real data. In the usage export (`usage/ai-usage-export.csv`), week 1 (1–7 February) has 306 drafts inserted by 12 people, 440 drafts generated and 1,421 panel openings. The panel opens by itself when a ticket opens ([06.4](../module-06/lesson-04.md)), so it is not use; inserted drafts are. The champions' issues log has two issues by Thursday: drafts signed without the agent's name (I-01, fixed in configuration on 3 February) and a blank ETA field that makes the draft repeat the passed checkout date in about 1 in 12 WISMO drafts (I-02, a prompt change to test).

### Step 6 — When the calendar and the evidence disagree

Stage dates are the earliest dates, not deadlines. The release plan said WhatsApp drafts could go on "no earlier than 15 February", if the shadow exit condition was met ([05.6](../module-05/lesson-06.md)): at least 75% acceptance in each of Hebrew, Arabic and Russian with at least 50 rated per language, and the web-store lookup returning an order for at least 90% of `HP-1…` numbers. On Sunday 14 February the shadow results (the course story's, illustrative) were: Hebrew 78% (50 rated), Russian 76% (48), Arabic 71% (41), lookup 62%. Not met, on three counts.

The queue was two days behind, the temps were gone and "WhatsApp drafts 15 Feb" was in everyone's calendar. Samir, who owns the switch, wanted it on. The week-2 report must put the choice in front of him plainly, with the consequence of each option:

- **Stay in shadow two weeks** for Arabic and the lookup (the condition as written).
- **Partial:** Hebrew and Russian drafts on, Arabic in shadow; WhatsApp WISMO drafts off until the lookup works.
- **All on** (a departure from the exit condition, recorded with the reason and a re-check date).

In the course story WhatsApp drafts went on for everything on 15 February, without a recorded departure; the champions' log shows the result within days (drafts too long for WhatsApp, I-05, 16 February; "order not found" on one in three WhatsApp WISMO messages, I-06, 18 February), and gate 1 shows it in April ([07.2](lesson-02.md)). The lesson is not that Samir was wrong to decide; he owns the switch. It is that the plan did not say who decides a partly-met exit or how a departure is recorded, so nobody saw that a condition had been skipped.

## Watch out

- **The yes as the finish line.** Nobody sends the PO, the team hears about go-live from the rota. Run the 72-hour list.
- **Hours nobody agreed.** Reviewers' time taken from the queue without the manager's agreement disappears in the first busy week.
- **Paying by date instead of deliverable.** A milestone that pays on 15 February whether or not the lookup works buys nothing.
- **Learning-week numbers quoted as results.** Label them; exclude them from the gate.
- **Panel openings as use.** Count the qualified event, by queue.
- **A stage date treated as a deadline.** If the exit condition is not met, the date moves, or the departure is decided and written down by the person who owns the switch.

## Your turn

### Inputs

- The steering minute and follow-up ([07.4](lesson-04.md) reference answer); the release plan and readiness checklist ([05.6](../module-05/lesson-06.md)); the value measurement plan ([05.1](../module-05/lesson-01.md)); the training plan ([06.2](../module-06/lesson-02.md)).
- Data room (module download): `usage/ai-usage-export.csv`, `usage/hr-roster.csv`.
- Module 6 download: `labs/module-06/champions-issues-log.csv`, `labs/module-06/queue-rota-2027.csv`.
- Template: [phase-1 plan](../../templates/phase-1-plan.md); spreadsheet `labs/module-07/phase-1-plan.csv` (module download).

### Steps

1. Write the 72-hour list with owners and dates.
2. Write the staffing table in hours per week, with whose agreement.
3. Write the stage-1 payment schedule against deliverables.
4. Fill the phase-1 plan for weeks 0–9: goal, deliverables, owner, hours, money, check, decision, report.
5. Write the weekly report for Thursday 4 February from the usage export (week 1) and the issues log.
6. Write the week-2 report for Sunday 14 February with the shadow results in Step 6, the three options and your recommendation.

### Time

100 minutes: 15 for the 72 hours, 15 for staffing, 10 for money, 25 for the plan, 15 for the first report, 20 for the week-2 report.

### Done when

- [ ] Every item that makes the yes executable has an owner and a date within three working days.
- [ ] Every person's hours are written per week and agreed with their manager.
- [ ] Payments are tied to deliverables someone checks.
- [ ] Each week has one goal and one check; learning weeks are labelled and excluded from the gate.
- [ ] The first report uses qualified events by queue, not panel openings or names.
- [ ] The week-2 report puts the partly-met exit in front of the switch owner with options and consequences, and says how a departure is recorded.

<details><summary>Reference answer</summary>

**72 hours, staffing, money, nine weeks:** as in Steps 1–4.

**Weekly report — reply drafts — Thursday 4 February 2027 (week 1, a learning week: no gate numbers)**

> **Status: on track.** Stage 1 live since Monday on email and the web form in four languages; WhatsApp tickets arriving in the helpdesk and drafted in shadow.
>
> **Signals (learning week, not gate evidence).** Drafts inserted: 306 by 12 people (all twelve agents walked through on 28 January); drafts generated: 440; inbound translations: 134. Panel openings are not counted (the panel opens with every ticket). Shadow: 64 WhatsApp drafts rated so far. Switch tested on Monday 09:00: per channel and language, under a minute.
>
> **Issues.** I-01 drafts signed without the agent's name: fixed in configuration 3 February. I-02 blank ETA (container not yet in the forwarder export) makes the draft repeat the passed checkout date, about 1 in 12 WISMO drafts: prompt change drafted, test set re-run planned for 9 February; until then agents are told to check every WISMO date.
>
> **Decisions needed.** None this week. On Sunday 14 February: WhatsApp stage 2 (Samir), against the exit condition.
>
> **Conditions.** Out-of-hours support line: live 31 January (Avi). Privacy notice update: published 29 January (Ronit). WhatsApp DPIA addendum: signed 28 January. Arabic re-measure: starts week 2, due before 1 March.
>
> **Money.** Committed ₪48,000 (PO 20 January); paid ₪0; first milestone (₪16,000) on the switch test, passed.

**Week-2 report — Sunday 14 February (excerpt)**

> **Decision needed today from Samir: WhatsApp drafts from Monday 15 February.** The shadow exit condition is **not met**: Hebrew 78% (50 rated), Russian 76% (48), Arabic 71% (41, below both the 75% and the 50 rated); web-store lookup finds the order for 62% of `HP-1…` numbers (target 90%; StoreHub export access arrived on 11 February).
>
> **Options.** (1) Stay in shadow until Sunday 28 February: the condition as written; the queue stays two days behind for two more weeks. (2) **Recommended:** Hebrew and Russian WhatsApp drafts on from Monday, except WISMO; Arabic and WISMO drafts in shadow until the lookup reaches 90% and Arabic 75% on 50 rated; re-check Sunday 28 February. (3) Everything on from Monday: a departure from the exit condition, which the gate-1 report will have to explain.
>
> **However you decide,** the decision, its reason and its re-check date go in the change log as a recorded departure (if 2 or 3), so the gate-1 report can read the WhatsApp numbers against what was actually switched on.

*What happened in the course story:* option 3 without a recorded departure. Gate 1 read WhatsApp at 58% acceptance and 9–30% use ([07.2](lesson-02.md)).

</details>

## References

- IBM, [Lead AI Transformation certificate](https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution), course 5 (go-live is not the goal) and course 6 (pilot isn't scale); named, not re-taught.
- Template: [phase-1 plan](../../templates/phase-1-plan.md); earlier: [production-readiness checklist](../../templates/production-readiness-checklist.md), [value measurement plan](../../templates/value-measurement-plan.md), [champions playbook](../../templates/champions-playbook.md).
- Earlier: [05.6 · Shadow mode, staged release and rollback](../module-05/lesson-06.md), [06.2 · Training that transfers: a 60-minute role-based session](../module-06/lesson-02.md), [06.3 · Champions network and office hours](../module-06/lesson-03.md), [06.4 · The honest adoption dashboard](../module-06/lesson-04.md). Next: [07.9 · Handover](lesson-09.md).
