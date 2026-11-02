---
id: "03.1"
module: 3
minutes: 16
practice_minutes: 75
prerequisites: ["02.7"]
objectives:
  - "Build a candidate list from three feeds: what people ask for, what they already use, and the goals leadership has stated."
  - "Restate every candidate as one workflow step with an owner, a monthly volume and a benefit in one unit, each figure with its source."
  - "Place each candidate as automate, assist, augment or leave alone, with a one-line reason."
  - "Write the ledger line for each candidate: who will check, correct or absorb the work it moves."
volatility: concept
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera) — course 2, Identify and Prioritize AI Opportunities"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
last_verified: "2026-11-02"
---

# 03.1 · The opportunity map

An opportunity map is the full list of places where the work could change, written in one format so that a chatbot, a spreadsheet macro and a tool someone already pays for on a personal card can sit side by side and be compared. In this lesson you collect candidates from three feeds, restate each one as a workflow step with a volume and a benefit unit, and decide for each whether the change would automate, assist, augment or leave the work alone. At the end you have the Harbor & Pine opportunity map that the next three lessons screen, score and fund.

## The situation

It is Monday 16 November 2026, your third week at Harbor & Pine. Discovery is done, and the findings memo ([02.7](../module-02/lesson-07.md)) goes to Michal on 1 December. Your findings say that about 38% of written contacts are "where is my order?" (WISMO), that customers write mostly on WhatsApp, which the helpdesk never sees, that the promised delivery date comes from a fixed table that nobody updates, and that agents drafted Russian and Arabic replies in free ChatGPT with customer data until the interim rule of 12 November stopped it. Your baselines ([02.4](../module-02/lesson-04.md)) and data profile ([02.5](../module-02/lesson-05.md)) say which numbers you can trust.

Meanwhile ideas keep arriving. The CEO wants the ChatNest chatbot. Noa wants a copy tool. Ronit asked whether "AI could just decide the damage claims". The ERP reseller sent purchasing a brochure for an "AI smart reorder" module. Michal wants something she can show the board on 28 January. If you rank these as they arrive, you rank them by who shouted loudest and most recently.

IBM's consulting certificate calls this "build the ruler before the list" and names three feeds; here you build the list itself, from Harbor & Pine's data, so that every later decision is about the same kind of thing.

## What to do

### Step 1 — Open three feeds, not one

Each feed finds candidates the others miss. Use all three, and write down where each candidate came from.

| Feed | Where to look | What it finds | What it misses |
|---|---|---|---|
| **Requests** | Emails to you, the board minutes, ideas in interviews, vendor proposals forwarded by managers | What people think they want, often already shaped as a solution ("a chatbot") | Anything nobody thought to ask for, and anything people already do quietly |
| **Already in use** | Your shadow-AI census and AI inventory from [01.6](../module-01/lesson-06.md) and [01.7](../module-01/lesson-07.md) | Real demand, proven by people paying or risking something to get it | Work where nobody has found a tool yet |
| **Top-down goals** | The sponsor's objective, board commitments, the finance summary, the company's stated values | What is fundable and what leadership will defend | What it costs the people doing the work |

At Harbor & Pine the three feeds give you:

- **Requests:** the CEO's chatbot (`company/ceo-board-update-2026-09.md`); Samir and Olga's "help us write replies faster"; Yaniv Carmi's (B2B sales) "draft the hotel quotes"; Olga's "answer assembly questions from the manuals"; Ronit's "decide damage claims automatically"; Noa's copy tool; the reseller's smart-reorder module; the previous consultant's demand forecasting and "AI recruiting" (`documents/roadmap-previous-consultant.md`).
- **Already in use:** free ChatGPT for Russian and Arabic replies in Customer Service, with customer data pasted in until the interim rule of 12 November (`it/proxy-log.csv`, `support/emails.csv`); the LinguaFlow translation extension on 9 machines (`it/browser-extensions.csv`); CopyGenie Pro in marketing on a personal card (`it/expenses.csv`); PeopleWise AI Candidate Match, switched on by an update (`it/peoplewise-release-notes-2026-03.md`).
- **Top-down goals:** the board's "bot, strategy, −40% support cost"; Michal's "fewer angry customers, and a support cost that doesn't keep rising"; Ronit's "numbers I can audit"; the company value painted on every van, "on time" (`company/company-profile.md`).

And one more source that is not a feed but beats all three: **your own discovery findings**. Nobody requested "fix the promised delivery date", nobody uses a tool for it, and no goal names it. It came from the data (findings 1, 2 and 16 in your memo) and from Tamar and Michal's hidden worries. Add discovery as a fourth column value and expect it to produce the best candidate on the list, as it does here.

### Step 2 — Estimate where the candidates are dense

Before you chase every idea, look at where the work is. Functions whose output is writing, answering, coordinating or judging are dense in candidates; functions that move physical goods are sparse. At Harbor & Pine, per `company/org-chart.md`: Customer Service (14 people) and B2B sales (7) write all day; logistics (about 30 people, most in the warehouse) mostly lifts and drives, except the import and delivery coordinators who chase information. That tells you to spend your mapping time in support, sales and the coordinator desks, and not to promise "AI for every department", which is what the board slide says.

### Step 3 — Restate every candidate in one format

A request like "a chatbot" or "AI for quotes" cannot be compared with anything. Restate each one as:

> **[Workflow step]** done by **[owner]**, **[volume] a month** ([source]), **[minutes] each** ([source]); the change would **[what changes]**; benefit measured in **[one unit]**.

If you cannot fill the workflow step and the owner, the candidate is "not yet a candidate": write it down with the question that would make it one. A process nobody can walk on paper ([02.3](../module-02/lesson-03.md)) cannot be improved by AI; automating it amplifies whatever is broken.

Worked example, the chatbot:

> "A chatbot that replaces half of support" becomes: **answering customer questions in written channels**, done by **14 support agents**, about **3,200 written contacts a month in peak season** (about 2,700 on WhatsApp from Samir's one-week tally, `support/whatsapp-week-tally.csv`, scaled to a month, plus about 500–570 helpdesk tickets, `support/tickets.csv`); **about 10 minutes each** on WhatsApp (median of the tally) and 8 minutes for a timed helpdesk ticket (median `time_spent_min`); the change would **let a bot answer some contacts without an agent**; benefit in **agent hours a month**.

Writing it this way exposes the question the request hid: which contacts could a bot answer correctly? 38% are WISMO, and the only date the bot can see is the wrong promised date.

### Step 4 — Get the volumes from the data, not from the proposer

Every volume and time needs a source and a status: measured (you counted it), reported (someone told you) or claimed (a proposer's or vendor's figure). The numbers you need for Harbor & Pine, October 2026 (peak is starting):

| What | Volume a month | Minutes each | Source | Status |
|---|---|---|---|---|
| Helpdesk tickets (email + web form) | 570 (October) | 8 median, where timed | `support/tickets.csv` | measured |
| WhatsApp conversations | about 2,700 (630 in one week × 4.3) | 10 median (agents' estimate) | `support/whatsapp-week-tally.csv` | measured for one week, estimated minutes |
| Phone calls in opening hours | 501 (October; 201 chose "order status") | 4.3 median talk for order status | `support/phone-log.csv` | measured |
| WISMO share of written contact | about 44–47% (Jul–Oct tickets; 43.8% of the WhatsApp week) | — | 02.4 and 02.5 | measured |
| Customer orders | about 420 (May–Oct average) | — | `orders/orders.csv` | measured |
| Orders on a container that slipped 7+ days | about 210 | — | `orders.csv` joined to `shipments.csv` | measured |
| B2B quotes | about 140 (Yaniv's estimate); 88 B2B tickets in six months reach the helpdesk, 23 minutes median | — | Yaniv; `support/tickets.csv` | reported |
| Damage claims | about 25 (149 in six months) | — | `claims/damage-claims-log.csv` | measured |

Note what this does to the WISMO cost. In October about 1,650 contacts were WISMO: roughly 270 tickets, 1,180 WhatsApp conversations and 200 calls. At 8, 10 and 4.3 minutes that is about **247 agent-hours a month, about 1.4 people**, and almost none of it reaches the KPI report.

### Step 5 — Place each candidate: automate, assist, augment or leave alone

Four modes, decided by who does the work after the change:

- **Automate** — the system does the step end to end, no person per item. Use it for rules that are known and checkable (compare two dates, send a notice), or for AI only where a wrong output is cheap and caught later.
- **Assist** — the system drafts or suggests, a person decides and sends every item. The default for anything that reaches a customer in writing.
- **Augment** — the system gives a person something they could not produce at all before (a language they do not write, a view across 3,000 orders), and the person still owns the decision.
- **Leave alone** — no change, or not with AI: not worth it, not ready, not AI at all, or a governance decision rather than a project.

Then add two columns that the next lessons depend on. **Oversight need:** a step that only reports needs a review; a step that predicts needs its uncertainty shown; a step that decides or acts on a customer needs an approval gate. **Ledger line:** for every hour the candidate saves, who now checks, corrects, escalates or waits? IBM calls this "the ledger"; write one line per candidate and do not leave it blank.

### Step 6 — Keep the list whole, including what you expect to drop

Put everything on the map, including the PeopleWise feature and the smart-reorder module. A portfolio decision only means something against the whole population: if the smart-reorder module is missing from the map, nobody can see that you looked at it and said no, and the reseller will be back in March.

## Watch out

- **Ranking while you list.** The moment you write "high value" next to the chatbot you have started scoring without criteria. Lesson 03.4 locks the criteria first. Here you only collect, restate and place.
- **The proposer's unit.** "70% deflection", "15% less inventory" and "20 hours a month" are three incomparable claims. Restate each in the work's own unit (contacts, orders, hours) before it goes on the map.
- **Missing the tools already in use.** Nobody submits what they already do. If your map has no row for the free ChatGPT use in support, your portfolio will propose a "new" drafting tool to people who have used one daily for a year, and you will not know why adoption looks instant or why it is risky.
- **Treating an AI label as AI.** SmartStock "AI" reorder is min/max rules (`it/smartstock-reorder-config.md`). Put it on the map with mode "leave alone — not AI" so the question is closed in writing.
- **A blank ledger line.** "Saves 8 minutes per reply" without "and Olga spends 2 minutes checking it" is the claim that finance will cut first (03.7).
- **Losing the discovery candidate.** The best candidate here was requested by nobody. If your map has only the three feeds, add discovery.

## Your turn

### Inputs

- Your findings memo, baselines and data profile from module 2 ([02.4](../module-02/lesson-04.md), [02.5](../module-02/lesson-05.md), [02.7](../module-02/lesson-07.md)); your shadow-AI census and AI inventory from [01.6](../module-01/lesson-06.md) and [01.7](../module-01/lesson-07.md).
- Data room (in the module download, `labs/common/harbor-and-pine/`): `company/ceo-board-update-2026-09.md`, `company/org-chart.md`, `support/tickets.csv`, `support/whatsapp-week-tally.csv`, `support/phone-log.csv`, `orders/orders.csv`, `orders/shipments.csv`, `claims/damage-claims-log.csv`, `documents/roadmap-previous-consultant.md`, `vendors/chatnest-sales-deck.md`.
- Template: [opportunity map](../../templates/opportunity-map.md), spreadsheet version `labs/module-03/opportunity-map.csv` in the module download.

### Steps

1. List every candidate from the three feeds and from discovery, with its source document or person. Aim for 12–15 rows.
2. Restate each as workflow step, owner, monthly volume, minutes each and benefit unit. Mark every figure measured, reported or claimed, with its source.
3. Compute the WISMO workload across the three channels for October (Step 4) and write it in hours and people.
4. Place each candidate as automate, assist, augment or leave alone, with a one-line reason and the oversight need.
5. Write the ledger line for each row.
6. Mark the rows that are "not yet a candidate" and the question that would make them one.

### Time

75 minutes: 20 to collect, 35 to restate and source the figures, 20 to place and write the ledger lines.

### Done when

- [ ] At least 12 candidates, each with its feed (request, in use, top-down, discovery).
- [ ] Every row has a workflow step and an owner, or is marked "not yet a candidate" with its question.
- [ ] Every volume and time has a source and a status; no vendor figure is marked measured.
- [ ] Each row has a mode with a reason, and a non-blank ledger line.
- [ ] The tools already in use and the systems that only claim to be AI are on the map.
- [ ] The WISMO workload is stated across all three channels, in hours a month.

<details><summary>Reference answer</summary>

**Harbor & Pine opportunity map, 19 November 2026** (volumes for October 2026 unless stated; M = measured, R = reported, C = claimed).

| # | Candidate, restated | Feed | Owner | Volume a month | Mode | Oversight | Ledger line |
|---|---|---|---|---|---|---|---|
| 1 | Tell customers before the promised date passes: compare each open order's promised date with the container's latest ETA daily, email a new date, and correct the web store's lead-time table | Discovery (findings 1, 2) + top-down ("on time") | Tamar (ETA data), Noa (StoreHub table) | about 210 orders on slipped containers (M); about 1,650 WISMO contacts across channels (M) | Automate — rules, no AI | Report: Tamar reviews a daily exceptions list | Logistics keeps the ETA sheet clean, about 1 hour a week (R, Tamar) |
| 2 | Route the four WhatsApp phones into the helpdesk so every written contact is a ticket | Discovery (finding 16) | Samir; Avi for the setup | about 2,700 conversations (M, one week × 4.3) | Automate — integration, no AI | None per item | Agents learn one screen instead of two phones; customers' numbers move to the helpdesk |
| 3 | Draft replies to written contacts in the customer's language from the message, the order and the latest ETA; an agent edits and sends every reply | Requests (Samir, Olga) + in use (free ChatGPT) | Samir | about 3,200 contacts once #2 is done (M+R) | Assist | Approval gate: a human sends every reply | Agents spend about 2 minutes checking each draft; a native speaker spot-checks Arabic and Russian |
| 4 | Answer customer questions with a web and WhatsApp bot, handing over when it cannot | Request (CEO) | Samir | 3,200 contacts; vendor says 70% resolved (C, US English, with order tracking) | Automate — customer-facing AI | Decides what the customer is told: needs a gate per answer type | Agents absorb hand-overs and repeat contacts from wrong answers; customers absorb wrong dates |
| 5 | Draft B2B quotes from the customer's request email with prices read from Priority; an account manager checks and sends | Request (Yaniv) | Yaniv | about 140 quotes (R); 88 B2B tickets in six months, 23 min median (M) | Assist | Approval gate: the account manager sends | Account managers check every price line |
| 6 | Answer "how do I assemble this?" from supplier manuals, for an agent to check | Request (Olga) | Samir | about 25–30 assembly tickets (M) plus WhatsApp assembly topics (M, small) | Assist | Approval gate | Someone must clean and keep the manuals current |
| 7 | Approve or reject damage claims from photos and the order | Request (Ronit) | Rina, Samir | about 25 claims (M) | Leave alone for now — not yet a candidate: the decision is blank for 32% of claims, so there is nothing to learn from or test against | Would decide on a customer: heaviest gate | Rina records every outcome first |
| 8 | Product descriptions and newsletter copy in four languages | Request + in use (CopyGenie, personal card) | Noa | about 300 texts (C, Noa) | Leave alone as a project — a tool and data-boundary decision (module 4) | Review: fact check against the product master | Marketing checks dimensions and materials |
| 9 | Translate replies and supplier messages | In use (LinguaFlow free extension, 9 machines) | Samir, purchasing | not measured | Leave alone as a project — approve or replace the tool (module 4); folds into #3 for support | — | — |
| 10 | Rank job applicants by fit | In use (PeopleWise, on by default) | Dana | about 120 applicants (C) | Leave alone — switch off pending review; inventory and risk (module 4) | Decides on people: would need a gate and a legal review | HR re-reads every ranking |
| 11 | Suggest purchase orders automatically | Request (reseller) | Purchasing | about 1,800 SKU suggestions (C) | Leave alone — not AI (min/max rules) and the case study does not transfer | — | — |
| 12 | Forecast demand per SKU | Top-down (previous consultant's roadmap) | Purchasing | — | Not yet a candidate: who decides what from the forecast, and with which history? | Predict: show uncertainty | — |
| 13 | Merge duplicate tickets and suggest the category on arrival | Discovery (findings 5, 6) | Samir | about 6% duplicates; 28.5% "Other" (M) | Assist — part of #3's triage | Review | Agents confirm the category |
| 14 | Record every damage-claim outcome in one place | Discovery (finding 7) | Rina | about 25 claims (M) | Leave alone for AI — a data foundation, no AI | — | Rina, a few minutes per claim |
| 15 | A weekly view of contact drivers by channel for Samir and Michal | Discovery | Samir | — | Augment — later, once #2 makes the data exist | Report | — |

**WISMO workload, October 2026:** about 268 tickets × 8 min + 1,180 WhatsApp × 10 min + 201 calls × 4.3 min ≈ 14,800 minutes ≈ **247 agent-hours a month, about 1.4 people** at 182 hours a month. Most of it is on WhatsApp, which neither the helpdesk nor the KPI report counts.

**What the map already shows.** The two candidates with the most volume behind them (#1 and #2) need no AI. The CEO's request (#4) depends on both: without #1 a bot repeats the wrong date, and without #2 it sees a sixth of the contacts. Four rows (#8–#11) are decisions about tools and governance, not projects. One request (#7) fails the label question before anyone scores it.

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting), course 2 "Identify and Prioritize AI Opportunities" (three feeds, opportunity density, the ledger; named, not re-taught).
- Template: [opportunity map](../../templates/opportunity-map.md).
- Earlier: [01.6 · The shadow-AI census](../module-01/lesson-06.md), [01.7 · The AI inventory from zero](../module-01/lesson-07.md), [02.3 · Process walk and task inventory](../module-02/lesson-03.md), [02.4 · Measuring a baseline](../module-02/lesson-04.md), [02.7 · The findings memo](../module-02/lesson-07.md).
- Next: [03.2 · Agent or not](lesson-02.md).
