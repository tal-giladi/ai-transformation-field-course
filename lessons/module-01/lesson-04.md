---
id: "01.4"
module: 1
minutes: 14
practice_minutes: 50
prerequisites: ["01.2", "01.3"]
objectives:
  - "Write a one-page 30-60-90 plan that names the question each 30 days answers, its deliverables, the decisions and who makes them."
  - "Plan the first week day by day so that every meeting and data request serves the 30-day question."
  - "Place decision points where the evidence will exist, instead of committing to a solution in week one."
volatility: concept
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera) — course 4, Design AI Transformation Roadmaps"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
last_verified: "2026-11-02"
---

# 01.4 · The first-week plan and the 30-60-90

Your sponsor asked for a one-page plan for the first 30 days by Thursday. The useful version covers 90 days, because that is where the board meeting is, and it is built from questions and decisions, not activities. In this lesson you fix the dates, list the constraints, give each 30 days one question to answer, and plan your first four working days hour by hour. At the end you have a filled 30-60-90 plan for Harbor & Pine that Michal can approve in five minutes.

## The situation

You start on 2 November 2026. Michal wants "a short written plan for the first 30 days by Thursday. One page. Who you'll see, what data you need, what you'll bring me at the end of the month." The board meets on 28 January 2027 and expects an AI strategy, a plan and a business case in the CFO's format. In between sits the busiest season of the year.

A 30-60-90 plan is usually written to impress. Yours is written to be checked: each block ends in something Michal, Ronit or the board decides. IBM's roadmap course sequences work across horizons and puts gates between them; this lesson is the same idea at the scale of your first quarter.

## What to do

### Step 1 — Fix the dates, counting from day one

Count days, not weeks, and write the actual dates. Israel's working week runs Sunday to Thursday; customer service also works Friday mornings (`company/customer-service-handbook.md`). Your first week is four working days, Monday 2 to Thursday 5 November.

| Marker | Date | What must exist |
|---|---|---|
| Day 1 | Mon 2 Nov 2026 | Entry note, confirmed objective (01.1, 01.2) |
| Day 4 | Thu 5 Nov | One-page plan to Michal (this lesson) |
| Day 30 | Tue 1 Dec | Diagnosis answered (see Step 3) |
| Day 60 | Thu 31 Dec | What to do first, and what it is worth |
| Steering pre-read | Thu 21 Jan 2027 | Board pack to Michal and Ronit, a week early |
| Day 88 | Thu 28 Jan 2027 | Board meeting |

The pre-read date matters more than the board date. If the CFO sees the business case for the first time two days before the board, she will not sign it, and "numbers Ronit has signed" is one of Michal's four conditions.

### Step 2 — Write down the constraints before the plan

A plan that ignores constraints fails in week three. Harbor & Pine's, each with its source:

- **Peak season November–January:** support and warehouse at full stretch; interviews short; no support-team workshops before February (Michal, `company/company-profile.md`).
- **Utilisation:** the support team ran at about 92% utilisation last winter (timesheets; Dana says the same). Every hour you take from an agent is an hour a customer waits.
- **No budget before January;** ₪120,000 from H1 2027; above ₪50,000 the CFO's business-case template; above ₪150,000 over three years the board (Michal, `company/finance-summary.md`).
- **Cash:** Q1 is the weakest quarter; large payments in February–March are hard (`finance-summary.md`).
- **Authority:** marketing and the web store by request only (charter, 01.2).
- **A public promise:** the CEO's bot, strategy and 40% (board minutes).

### Step 3 — Give each 30 days one question

Activities fill time; questions end. Name the question each block must answer, then list only the work that answers it.

| Block | The question | Ends in |
|---|---|---|
| Days 1–30 (2 Nov – 1 Dec) | What is really happening — in the work, the data, and the AI already in use? | A findings memo and a decision on interim guardrails |
| Days 31–60 (2 – 31 Dec) | What should we do first, and what is it worth? | A shortlist with baselines, one decision-ready case, a pilot charter |
| Days 61–90 (1 – 28 Jan) | Does the first thing work on our data, and will the board fund the next six months? | Pilot evidence, steering pack, board decision |

### Step 4 — Fill each block: outcomes, deliverables, decisions, people, risks

For each block write five short lists. Link each deliverable to the method you will use, so the plan doubles as your own checklist:

**Days 1–30.** *Deliverables:* charter and scope boundary (01.2, 01.3); access pack and data-room first read (01.5); shadow-AI census and AI inventory (01.6, 01.7); interviews with 8–10 people (module 2); baselines for contacts and response times (02.4); findings memo (02.7); interim AI rule and one approved tool proposal (module 4, by day 10 if the census shows customer data in free tools). *Decisions:* Michal approves the interim rule; Michal decides scope changes weekly. *People:* Samir, Olga, Rina, Tamar, Ronit, Avi, Noa, Dana. *Risks:* exports late (ask on day 2); agents fear the census (frame it as an amnesty). *Will not:* talk to vendors, promise savings, run workshops.

**Days 31–60.** *Deliverables:* opportunity map and scored shortlist (03.1–03.4); ROI model in Ronit's template (03.7); decision-ready case for one first move (03.9); policy pack draft (module 4); pilot charter with stop rules (05.1). *Decisions:* Michal and Yoav choose the first move at the monthly review (10 December); Ronit agrees the ROI method. *People:* Yoav, Michal, Ronit, Samir in a short scoring session. *Risks:* the CEO insists on the bot regardless of evidence (prepare the alignment session, 03.6); holiday absences late December.

**Days 61–90.** *Deliverables:* pilot built and evaluated on real data in shadow mode (module 5); eval report; steering pack and decision record (module 7); six-month plan; business case signed by Ronit. *Decisions:* steering pre-read 21 January; board 28 January (scale, fix or stop; budget above ₪150,000 if requested). *People:* Michal, Ronit, Yoav, Samir, the two or three agents who test the pilot. *Risks:* the pilot is not ready (the plan's fallback is "evidence of the cause plus a measured quick fix"); training slips into peak season (don't: training starts February).

### Step 5 — Put decision points where the evidence will exist

The strongest line in the plan is the one that refuses to name a solution too early:

> By 10 December, Michal and Yoav choose the one thing to have working by 28 January, from a
> shortlist with measured baselines.

Not "build the chatbot by January", and not "no chatbot". If you name the solution in week one, every finding that points elsewhere looks like a change of plan. If you name the decision and its date, the evidence arrives to an empty chair.

### Step 6 — Plan the first week by the hour

Four working days. Every slot serves the 30-day question; every data request goes out early because exports take days.

| Day | Morning | Afternoon |
|---|---|---|
| Mon 2 Nov | 09:05 Michal (objective, money, authority; 01.2). Entry note. | Read the board minutes, org chart, finance summary, KPI report. Send the read-back email. Access request to Avi (01.5). |
| Tue 3 Nov | 08:30–09:30 sit with a support agent (watch, don't ask). 10:00 Samir, 45 min. | 14:00 Ronit, 30 min: her template, hurdle rate, how the last big project was judged. Data-room first read (01.5). |
| Wed 4 Nov | 09:00 Avi, 40 min: proxy, extensions, SaaS list, what logs exist (01.6). | 13:00 Rina (claims), 30 min. 15:00 Tamar (logistics), 30 min — Michal didn't list her; the delivery questions in your notes say you need her. |
| Thu 5 Nov | 08:00 30-day plan to Michal. 11:00 Noa: scope for marketing (01.3). | 15:00 Michal, weekly check-in: plan approved or corrected; interview list for week 2. |

Two choices in that week are deliberate. The first hour on Tuesday is spent *watching* the work before anyone tells you about it (module 2 builds on this). And Tamar is on the list although nobody sent you to her: your sponsor's hint about delivery and the board slide's "on time" value both point at logistics.

### Step 7 — Fit it on one page and set the rhythm

One page: the dates line, the three blocks as a table, the week-one calendar, the decision points, and "what I will not do". Below it, the rhythm: a weekly 30-minute check-in with Michal (Thursday), a monthly review with Yoav and Michal (10 December), the steering pre-read (21 January). Fill the [30-60-90 plan template](../../templates/30-60-90-plan.md).

## Watch out

- **A plan of activities.** "Interview stakeholders, analyse data, build pilot" can never be late or wrong, so it can't be managed. Each block needs a question and a decision.
- **Naming the solution in week one.** "Chatbot by January" in your plan makes every contrary finding a failure. Name the decision and its date instead.
- **Ignoring the season.** A workshop with 14 agents in December costs the company customer replies it cannot afford, and the team will remember who asked.
- **No buffer before the board.** If finance first sees the numbers in the last week, they will not be signed. The pre-read is the real deadline.
- **Requests sent on Thursday.** Exports and access take days. Send every data request on day one or two.
- **A plan nobody approved.** Ask Michal to reply "approved" or to correct it. A plan she corrected is better than one she never read.
- **Forgetting to show what you won't do.** "No vendor meetings in November" protects you from the most common derailment.

## Your turn

### Inputs

- Your charter (01.2) and scope boundary (01.3).
- Data room: `company/company-profile.md` (seasons), `company/finance-summary.md` (approval rules, cash), `company/ceo-board-update-2026-09.md` (board date), `company/org-chart.md`.
- Template: [30-60-90 plan](../../templates/30-60-90-plan.md).

### Steps

1. Fill the dates line (Step 1) with real dates, including the steering pre-read.
2. List at least five constraints, each with its source.
3. Write the question for each block and the deliverables, decisions (with who and when), people, risks and "will not" lists.
4. Write at least two decision points as dated decisions, not solutions.
5. Plan the four days of week one by half-days, with the reason for each meeting.
6. Cut it to one page and write the two-line cover email to Michal.

### Time

50 minutes.

### Done when

- [ ] Every block has one question, and ends in a decision by a named person on a date.
- [ ] No block names a vendor or commits to a specific AI solution.
- [ ] Each constraint has a source.
- [ ] The steering pre-read is at least a week before the board.
- [ ] Week one sends every data request by day two and includes time watching the work.
- [ ] The plan fits on one page and says what you will not do.

<details><summary>Reference answer</summary>

**Harbor & Pine — 30-60-90 plan, v1.0, sent 5 November 2026**

*Dates:* Day 1 Mon 2 Nov · plan Thu 5 Nov · Day 30 Tue 1 Dec · monthly review with Yoav Thu 10 Dec · Day 60 Thu 31 Dec · steering pre-read Thu 21 Jan · board Thu 28 Jan 2027.

*Constraints:* peak season Nov–Jan, no support workshops before Feb (Michal); support ~92% utilised in peak (timesheets); no budget before Jan, ₪120k H1 2027, >₪150k board (Michal, finance summary); Q1 cash weakest (finance summary); marketing and web store by request (org chart); CEO's public commitment (board minutes).

| | Days 1–30 | Days 31–60 | Days 61–90 |
|---|---|---|---|
| Question | What is really happening in the work, the data and the AI already in use? | What first, and what is it worth? | Does it work on our data; will the board fund six months? |
| Deliverables | Charter, scope, access pack, data-room read, shadow-AI census, AI inventory, 8–10 interviews, baselines, findings memo; interim AI rule | Shortlist with baselines, ROI model in Ronit's template, decision-ready case, policy pack draft, pilot charter | Pilot evaluated in shadow mode, eval report, steering pack, six-month plan, signed business case |
| Decisions | Michal: interim AI rule (by 12 Nov); scope changes weekly | Michal + Yoav: the first move (10 Dec); Ronit: ROI method (by 20 Dec) | Steering pre-read (21 Jan); board: fund / fix / stop (28 Jan) |
| People | Samir, Olga, Rina, Tamar, Ronit, Avi, Noa, Dana | Yoav, Michal, Ronit, Samir | Michal, Ronit, Yoav, Samir, 2–3 agents |
| Risks | Late exports; fear of the census | CEO insists on the bot; late-December absences | Pilot not ready → fallback: cause + measured quick fix |
| Will not | Meet vendors; promise savings; run workshops | Sign contracts | Train the whole team before Feb |

*Week one:* as in Step 6.

*Cover email:* "Michal — the one-page plan, as asked. The key decision is yours and Yoav's on 10 December: what we have working by the board. Please approve or correct."

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting), course 4 "Design AI Transformation Roadmaps" (horizons and gates — named, not re-taught).
- Template: [30-60-90 plan](../../templates/30-60-90-plan.md).
- Previous: [01.3 · Scope boundary and change control](lesson-03.md). Next: [01.5 · Access and the first-day data-room read](lesson-05.md).
