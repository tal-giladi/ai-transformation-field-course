---
id: "07.6"
module: 7
minutes: 18
practice_minutes: 90
prerequisites: ["07.2", "05.7", "04.7"]
objectives:
  - "Write a RACI for a running AI service with one accountable owner and a named person for every recurring task and every switch."
  - "Build the operating calendar (daily, weekly, monthly, quarterly, yearly) with the hours each item costs, and check the total against the business case."
  - "Turn monitoring signals into triggers that say who is told, who may act, how fast and with which response, and keep them separate from the review cadence."
  - "Write the retirement criteria for the service on the day it goes live."
volatility: concept
sources:
  - title: "IBM Lead AI Transformation: Strategy, Governance & Execution Professional Certificate (Coursera) — course 6, Measure AI Value and Scaling Transformation, module 4 'Build durable AI capability' (accountable owner; proportionate monitoring; escalation trigger vs review cadence)"
    url: https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution
  - title: "NIST AI Risk Management Framework (AI RMF 1.0, January 2023) and the Generative AI Profile (NIST AI 600-1, July 2024): Govern and Manage functions"
    url: https://www.nist.gov/itl/ai-risk-management-framework
last_verified: "2026-11-02"
---

# 07.6 · The operating rhythm

A pilot has a team watching it; a service has a calendar, or nobody watches it at all. In this lesson you turn Harbor & Pine's reply drafts, now a service on email and web form, into something that runs without you: one accountable owner, a RACI for every recurring task and every switch, a calendar with the hours each item costs, triggers that send a named person to act, a monthly review with a fixed agenda, and the conditions under which the service will be retired. At the end you have the operating rhythm Samir's team will run from April, and you know what it costs.

## The situation

Sunday 4 April 2027. Three days ago gate 1 turned the drafts on email and web form from a pilot into a service, with WhatsApp in a fix until 1 July ([07.2](lesson-02.md)). Samir asked you on Thursday evening: "What exactly do I have to do every week once you move on to the next thing?" In June you hand the service over ([07.9](lesson-09.md)); before that it needs a rhythm that does not depend on you remembering. The monitoring spec of January ([05.7](../module-05/lesson-07.md)) has the signals and a weekly routine; the incident review of 22 March ([07.5](lesson-05.md)) added a money flag, a targeted sample and change control that the console enforces; the AI review group meets every second Thursday ([04.7](../module-04/lesson-07.md)).

IBM's leadership course describes the failure this lesson prevents ("nobody is watching": the project team disperses and silence is read as satisfaction) and its cures: one accountable owner, proportionate monitoring, an escalation trigger that is not the same thing as a review cadence, and outcomes from continue to retire. NIST's AI RMF puts the same ideas in its Govern and Manage functions. Neither gives a RACI, a calendar or a cost. Here you write them.

## What to do

### Step 1 — Name one accountable owner, and the roles around them

One person is accountable for the service: they decide when it is switched off, they chair its review, and the board's question "does it still work?" is theirs to answer. Not a committee, and not the person who built it.

| Role | Who | What they own |
|---|---|---|
| Service owner (accountable) | Samir Haddad | The service, its switches, its monthly review, the decision to restrict or suspend |
| Service analyst | The pilot lead until 30 June; then Shani Ohayon, four protected hours a week (agreed in 07.9) | Weekly report, prompt and source releases, eval re-runs, change log |
| Technical owner | Avi Mizrahi with the integrator | Integration, console rights, alerts, model lifecycle, vendor settings |
| Quality reviewers | Olga Petrenko (Russian, Hebrew), Lina Khoury (Arabic), Daniel Shaw (English) | The weekly spot audit and the targeted sample |
| Value owner | Ronit Avraham | Monthly value numbers against the case |
| Privacy | Counsel or the DPO, through Ronit | DPIA review, any privacy incident |
| Governance | AI review group (chair Michal) | Restrictions, incidents, vendor changes, the three numbers for the board |
| Investment | Steering committee (chair Yoav) | Re-gates, scaling, retirement |

### Step 2 — Write the RACI for what actually happens

A RACI for a running AI service is a list of the things people will actually do, with one A per line. The lines that matter most are the ones nobody thinks about until they are needed: the switch, a source change, a model notice, retirement.

| Activity | Samir | Analyst | Avi | Reviewers | Ronit | Review group | Steering |
|---|---|---|---|---|---|---|---|
| Switch drafts off (category, channel, language, all) | A/R | R | R | C | I | I | I |
| Prompt change (standard) | A | R | C | C | — | I | — |
| Knowledge-source change | A | R | R (console) | C | — | I | — |
| Model or provider change; new channel; new stage of autonomy | C | R | R | C | C | A | I |
| Weekly spot audit and targeted sample | A | C | — | R | — | — | — |
| Monthly eval re-run and negative tests | A | R | C | C | — | I | — |
| Incident lead | A | R | R | C | C (counsel) | I | I |
| Value numbers against the case | C | R | — | — | A | I | I |
| Vendor settings and admin-rights audit | I | C | A/R | — | — | I | — |
| Licences: grant, reclaim, leavers | A | R | R | — | I | — | — |
| Training new joiners (job aid, champion hour) | A | C | — | R (champions) | — | — | — |
| Retirement decision | C | C | C | — | C | C | A |

Check each line: exactly one A; the A has the authority to do it (Samir can switch off without asking anyone, which is written into the charter); nobody is R on so many lines that the rhythm depends on them alone. Olga appears on the audit, the champions' work and Russian escalations; that is the line to watch.

### Step 3 — Put it on a calendar, with the hours

Monitoring that depends on someone remembering stops in the third week. Fix every recurring item to a day and a person, and cost it in hours:

| Cadence | When | What | Who | Hours a month |
|---|---|---|---|---|
| Daily | 08:30 | Alerts: cost, errors, safety flags not cleared | Avi | 2 |
| Weekly | Sunday | Automated report (acceptance, discard rate, review time, flags, cost, errors) read and one line sent to Samir | Analyst | 2 |
| Weekly | Tuesday | Spot audit: 20 random replies per language plus every money-flagged draft | Olga, Lina, Daniel | 7 |
| Weekly | Wednesday | Prompt and source review, 20 minutes: discard reasons, audit findings, proposed changes | Analyst, Samir, Olga | 4 |
| Weekly | Thursday | One line to the team: what changed because of their marks | Analyst | 1 |
| Monthly | First Thursday | Service review, 45 minutes (Step 5) | Samir chairs; analyst, Avi, Ronit, Olga | 4 |
| Monthly | Before the review | Full eval re-run on the 400-message test set and the negative tests | Analyst | 2 |
| Monthly | Before the review | Value numbers: minutes per contact (drafted vs holdout), repeat contacts, cost | Ronit, analyst | 2 |
| Monthly | — | Vendor settings and console rights audit; proxy-log check for free chatbots | Avi | 1 |
| Quarterly | With the steering committee | Value against the case; re-gates; roadmap | Steering | 1 |
| Yearly | January | DPIA review, contract renewals, full re-tiering, retirement review | Review group, counsel | 1 (averaged) |
| **Total** | | | | **about 27 hours a month** |

Now do the integration check ([07.1](lesson-01.md)): trace the rhythm's hours to the business case. ROI model v3 counted about 100 hours a year of native-speaker spot checks as the control cost; the rhythm needs about 27 hours a month, about 320 a year. The difference, about 220 hours a year (about ₪29,000 at ₪130 an hour), is not cash, but it comes straight out of the roughly 570 hours of capacity the case promised. Tell Ronit now and put it in the next re-forecast; a rhythm the case did not pay for is the first thing cut in November.

### Step 4 — Write triggers, separately from the cadence

A cadence is when you look; a trigger is what makes someone act, whenever it happens. Each trigger names the threshold, who is told, who may act, how fast, and the response. Harbor & Pine's, from the monitoring spec plus what gate 1 and the incident added:

| Trigger | Told | May act | How fast | Response |
|---|---|---|---|---|
| Any S1 incident (07.5) | Samir, Michal | Samir, analyst or Avi | Immediately | Runbook: narrowest switch, log, counsel if privacy |
| Spot audit above today's rate, two weeks, in one channel × language | Samir | Samir | Same day | That segment off; fix; re-test |
| Acceptance below 60% two weeks in one channel × language | Analyst, Samir | Samir | Same week | That segment off (the per-segment stop rule from 07.2) |
| Discard rate below 5% while acceptance is under 90% | Samir | Samir | Within a week | Audit 20 sends; check the load rule; a refresher |
| Money-flagged drafts above 1 in 8, or second-look time above 60 seconds | Analyst | Samir | Within a week | Review the flag rule and the source library |
| Negative test fails on any change | Analyst | Analyst | Before release | No release; if live, roll back |
| Model deprecation notice | Avi, analyst | Review group | At least 30 days before retirement | Migration test: eval and negative tests on the new model |
| Cost over twice the four-week daily average | Avi | Avi | Same day | Look for loops, retries, prompt growth |
| Holdout difference under half the planned saving for two months | Ronit | Steering | Next quarterly | Re-forecast; consider restrict or retire |

### Step 5 — Fix the monthly review's agenda

Forty-five minutes, the same agenda every month, so that a skipped item is visible:

1. Signals against thresholds, by channel and language (10 minutes; the analyst's one page).
2. Incidents and near misses since last month; actions from earlier reviews (5).
3. Changes released and proposed: prompt, sources, configuration; the change log (5).
4. Value: minutes per contact drafted vs holdout; repeat contacts; cost per draft (5).
5. Adoption by queue, never by person ([06.4](../module-06/lesson-04.md)) (5).
6. Vendor and model notices; contract dates (5).
7. Decisions: continue, adjust, restrict, roll back, suspend or propose retirement, each minuted with an owner (10).

The review's minutes go to the AI review group a week later, where the service is one line among the company's AI uses, and once a quarter to the steering committee. The board gets the three numbers from 04.7 (what reached production, how long decisions take, what was declined and why), not the service's dashboard.

### Step 6 — Write the retirement criteria now

A service is easiest to retire when the conditions were written on the day it went live, before anyone is attached to it. Write four or five, each checkable:

- Acceptance below 60% in every channel for three consecutive months, with a fix tried and re-tested.
- Minutes saved per contact against the holdout below 1 for two quarters (the service no longer pays for its own review time).
- A model retirement with no replacement that passes the eval and negative tests before the deadline.
- The work moves: a channel closes, or a different system (for example the helpdesk vendor's own feature) does the same job at lower total cost and passes the same eval.
- A change in law or in counsel's view that the processing cannot meet.

When one is met, the steering committee decides, and the retirement runs the decommissioning checklist from [07.2](lesson-02.md): people, access, data, contract, records, a check after 30 days.

## Watch out

- **A committee as the owner.** "The AI group owns it" means nobody does on a Tuesday. One accountable person, with the switch.
- **The rhythm in the spec and nowhere else.** If it is not in calendars with names, it stops when the builder leaves. Send the invitations before you write the document.
- **An uncosted rhythm.** About 27 hours a month nobody budgeted will be cut at the first peak. Put the hours in the case.
- **Cadence instead of triggers.** A monthly review finds a broken segment up to four weeks late. Triggers act the day the threshold is crossed.
- **Retirement criteria written at the end.** By then everyone is attached. Write them now.
- **Reporting adoption by person.** The review sees queues and segments; the AUP promised it.

## Your turn

### Inputs

- The decision record from [07.2](lesson-02.md), the incident review from [07.5](lesson-05.md), the monitoring spec and change control from [05.7](../module-05/lesson-07.md) (spreadsheet `labs/module-05/monitoring-signals.csv` in the module 5 download), the governance charter and review group's terms from [04.7](../module-04/lesson-07.md), the ROI model ([03.7](../module-03/lesson-07.md)).
- Module download: `labs/module-07/operating-rhythm.csv` (columns and three example rows).
- Template: [operating rhythm](../../templates/operating-rhythm.md).

### Steps

1. Name the accountable owner and the roles, with one line each on what they own.
2. Write the RACI for at least ten activities, including the switch, a source change, a model notice and retirement; check one A per line.
3. Build the calendar with times and hours per month; total it.
4. Trace the total to the business case and write the note to Ronit.
5. Write the triggers table, at least eight rows, with who is told, who may act, how fast and the response.
6. Write the monthly review agenda and the first review's date and invitees.
7. Write four or five retirement criteria.

### Time

90 minutes: 10 for roles, 20 for the RACI, 20 for the calendar and hours, 10 for the note to Ronit, 15 for the triggers, 5 for the agenda, 10 for retirement.

### Done when

- [ ] One person is accountable for the service and holds the switch.
- [ ] Every RACI line has exactly one A, and the switch, source changes, model notices and retirement are on it.
- [ ] Every recurring item has a day, a person and hours; the total is compared with the case.
- [ ] Triggers and cadence are separate tables, and every trigger names who may act and how fast.
- [ ] Retirement criteria are checkable and written before anyone needs them.

<details><summary>Reference answer</summary>

**Operating rhythm — reply drafts service — v1.0, Sunday 4 April 2027** (owner: Samir Haddad; analyst: pilot lead until 30 June, then Shani Ohayon)

*Roles, RACI, calendar, triggers, agenda:* as in Steps 1–5.

*Hours:* about 27 a month: daily alerts 2; Sunday report 2; Tuesday audit 7; Wednesday review 4; Thursday note 1; monthly review 4; eval re-run 2; value numbers 2; settings, rights and proxy 1; quarterly and yearly 2 (averaged). Not included: the champions' protected hours (module 6 budget).

*Note to Ronit (4 April):* "The service's operating rhythm needs about 27 hours a month (about 320 a year) of internal time. ROI model v3 counted about 100 hours a year of spot checks. The difference, about 220 hours (about ₪29,000 at ₪130 an hour), is capacity, not cash, but it reduces the case's roughly 570 hours of capacity to about 350. I propose we show it in the July re-forecast with the WhatsApp re-gate. Nothing in the cash line changes."

*First monthly service review:* Thursday 6 May 2027, 10:00–10:45; Samir (chair), analyst, Avi, Ronit, Olga. Calendar invitations sent on 4 April for the first Thursday of every month to December. The AI review group sees the minutes on Thursday 13 May, the same day as the WhatsApp checkpoint.

*Retirement criteria:* the five in Step 6, with the steering committee deciding and 07.2's decommissioning checklist executing.

*Two things the first draft got wrong and the review fixed:* Olga was R on six lines (audit, champions, Russian escalations, flag clearing, labelling, the WhatsApp test set); the audit's Hebrew share moved to Shani and the English to Daniel. And the switch was listed as "IT": Samir holds it, as the charter says, with the analyst and Avi as deputies.

</details>

## References

- IBM, [Lead AI Transformation certificate](https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution), course 6, module 4 (nobody is watching; accountable owner; proportionate monitoring; escalation trigger vs review cadence; continue to retire). Named, not re-taught.
- NIST, [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) (AI RMF 1.0, January 2023; Generative AI Profile NIST AI 600-1, July 2024): Govern and Manage.
- Templates: [operating rhythm](../../templates/operating-rhythm.md), [monitoring spec](../../templates/monitoring-spec.md), [governance charter](../../templates/governance-charter.md), [integration check](../../templates/integration-check.md).
- Earlier: [05.7 · Before launch](../module-05/lesson-07.md), [04.7 · Governance that runs](../module-04/lesson-07.md), [06.4 · The honest adoption dashboard](../module-06/lesson-04.md). Next: [07.7 · Pressure-test a roadmap](lesson-07.md); the handover, [07.9](lesson-09.md).
