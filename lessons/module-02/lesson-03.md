---
id: "02.3"
module: 2
minutes: 18
practice_minutes: 90
prerequisites: ["02.2"]
objectives:
  - "Run a one-hour observation of real work with an agreed protocol: consent, a timed log, think-aloud, and no personal data in the notes."
  - "Compare the written process with the observed one and record every difference as a finding with its evidence."
  - "Build a task inventory with volume, time, error, variation and judgment per task, each number with its source."
  - "Decide for each task whether its process can be walked on paper, and mark the ones that cannot as not yet candidates."
volatility: concept
sources:
  - title: "law.co.il (Haim Ravia) — Monitoring employees' email severely restricted (Isakov Inbar, National Labour Court, 8 Feb 2011)"
    url: https://www.law.co.il/en/articles/2011/04/25/monitoring-employees-email-severely-restricted/
last_verified: "2026-11-02"
---

# 02.3 · Process walk and task inventory

Interviews tell you how people describe their work; watching it tells you what they do. In this lesson you sit with two support agents for an hour each, compare what you see with the handbook, and turn interviews, observation and exports into a task inventory: every task the team does, with its trigger, volume, time, error rate, variation and the judgment it needs. You also apply a hard test — can the process be walked on paper? — that decides which tasks are candidates at all. At the end you have observation notes, a paper-versus-practice list and a task inventory for Harbor & Pine's customer service.

## The situation

Week 3, Tuesday 17 November 2026. The interviews (02.2) gave you a story: most contacts are "where is my order", the macro repeats a date that has passed, the good agents chase logistics instead, and claims are decided without the QA step the handbook describes. Samir also mentioned, almost in passing, that most customers don't email at all: they write to the four shared WhatsApp phones on the desks, which no system counts. In October he had the twelve agents tally every WhatsApp conversation by hand for one week.

That is a story from three people. Before it becomes a finding you need to see the work, and before anything becomes an AI candidate you need to know which tasks are big, slow, error-prone and repeatable, and which need judgment. Samir agreed to one hour with Olga and one with Hila.

IBM's consulting certificate puts a pass/fail gate here: a process you cannot walk on paper — steps, an owner per step, trigger, volume — is not yet a candidate; automating it amplifies its errors. Here you build the inventory that applies that gate.

## What to do

### Step 1 — Draw the process as written

Before you watch, write down the official version so you can see the differences. At Harbor & Pine the handbook (`company/customer-service-handbook.md`, v3.2, March 2024) gives you:

1. Take the oldest ticket in your language view (§4.1).
2. Find the order in Priority (§4.2).
3. Set the category; "Other/כללי" if nothing fits (§4.3, §5).
4. Use a saved reply where one exists (§4.4); for "where is my order" the macro "confirms the estimated delivery date from the order" (§6).
5. Send and set the status to **Resolved**; a new message opens a new ticket (§4.5).
6. Damage: photos macro → Rina opens a claim → "**Every claim is reviewed by QA within 48 hours**" → Rina informs the customer (§8).
7. Channels: email, web form, phone, showrooms (§2). Logistics only through logistics@ (§9).

Note what the handbook does *not* mention. There is no WhatsApp in §2.

### Step 2 — Agree an observation protocol

Watching people work is a form of monitoring, and Israeli labour case law expects it to be transparent and proportionate. In *Isakov Inbar* (National Labour Court, 2011) the court required employers to bring their monitoring policy to employees' attention and to use less invasive means first; that case was about email, but the same habits keep an observation honest and acceptable. Your protocol, agreed with the manager and told to each agent the day before:

- **Purpose**: how the work flows, not how fast anyone is. Say it, and mean it: no individual productivity numbers in any report.
- **Consent**: the agent can say no, and can stop at any time. No screen recording, no photos of screens.
- **Method**: sit beside them for 60–90 minutes; ask them to think aloud ("say what you're looking for"); write a timed log — start, end, channel, language, what the customer wanted, what they did, systems and files touched, waits, anything surprising.
- **No personal data in your notes**: no customer names, phone numbers, addresses or order numbers.
- **Read-back**: the agent sees your notes the next day.

If the organization has a works committee, or the observation will be repeated or extended, ask HR and counsel first. Harbor & Pine has no works committee; labour law still applies.

### Step 3 — Observe, and look for five things

During the hour, watch for:

1. **Triggers**: what starts each piece of work (a message, a call, a timer, a colleague).
2. **Waits**: where the work stops for someone else (logistics@, Rina, a call back).
3. **Workarounds**: steps that aren't in the handbook (Tamar's sheet, calling the delivery coordinator).
4. **Rework**: work caused by earlier work (the customer who writes again because the macro gave a passed date).
5. **Channels and files** nobody listed (a WhatsApp phone, a sticky note with a phone number).

The sit-in notes from 17 November are in the module download (`labs/module-02/observation-notes.md`). Excerpt from Olga's hour:

| Start | End | Ch | What the customer wants | What she did | Note |
|---|---|---|---|---|---|
| 09:28 | 09:38 | WA | Where is my order — "you promised the 10th!" | Finds a Deskly ticket from the same customer marked Resolved on 9 Nov with the order-status macro (date already passed); looks up the container; gives 24–26 Nov | Same customer on two channels; the macro answer created this contact |
| 09:45 | 09:58 | WA | Long, angry message about a delay | Writes a careful Russian reply herself | 13 minutes. "Before the rule I did this in five." |

And from Hila's: she follows the handbook — macro, Resolved — and twice in one hour the date she sends will pass before the order arrives.

### Step 4 — List paper versus practice

Every difference between the written and the observed process is a finding. Write it with both sources:

| Handbook says | Practice (evidence) | Consequence |
|---|---|---|
| Channels: email, form, phone (§2) | Most written contacts arrive on four WhatsApp phones: 630 in the tallied week vs 94 helpdesk tickets the same five days (`support/whatsapp-week-tally.csv`, `support/tickets.csv`); observed | The main channel has no export, no metrics and no rules |
| WISMO: send the macro with the order's date (§6) | Olga skips it and checks Tamar's sheet; Hila sends it and the date passes (observed) | Repeat contacts; the agent who follows the handbook creates more work |
| Set Resolved on reply (§4.5) | Tickets resolved while waiting for logistics (observed); 81% of resolved tickets are resolved within 5 minutes of the first reply (`tickets.csv`, 02.5) | "Resolution rate 100%" measures replies, not outcomes |
| Logistics only through logistics@ (§9) | Also phone calls to delivery coordinators for booking changes (observed) | Unrecorded load on logistics |
| QA reviews every claim within 48 hours (§8) | No QA role in `org-chart.md` or `headcount.csv`; no QA column in the claims log; median 8 days from opening to decision, 5% within 2 days (`claims/damage-claims-log.csv`) | A control that exists only on paper |
| Customer details stay in Deskly and Priority (§10) | Damage photos and phone numbers on shared WhatsApp phones; a phone number on a sticky note (observed) | Personal data outside any system (02.5) |

### Step 5 — Build the task inventory

One row per task as the worker does it. For each, five measures and their sources:

- **Volume**: how many per month, from an export where one exists, a tally where it doesn't, and "said" as a last resort.
- **Time per item**: from observation or a time study. Don't divide bucket hours by ticket counts: the time sheets put 70.7% of logged hours in the "email" bucket (`people/timesheets.csv`), about 6,990 hours May–October, while the helpdesk had 2,529 tickets — that would be 2.8 hours per ticket, which is absurd. The division fails because the bucket holds WhatsApp, chasing logistics and re-contacts, not only tickets. The absurd number is itself the clue that the work lives somewhere the helpdesk doesn't see.
- **Error or rework**: the share of items that come back or go wrong.
- **Variation**: low (one script fits nearly all), medium, high (every case differs).
- **Judgment**: rule (a written rule decides), pattern (experience recognises it), judgment (weighing money, fairness or risk).

To get WhatsApp volumes by task, the tally's `topic` column is the agents' own words in four languages: 44 different labels for 630 conversations. Group them yourself (Track A: add a column, filter by each label, pivot). One grouping:

| Group | Labels (examples) | Week | Share |
|---|---|---|---|
| Where is my order | בירור מועד אספקה, עיכוב באספקה, where is my order, وين الطلبية, где заказ, איפה הספה | 276 | 43.8% |
| Delivery booking / reschedule | לשנות תאריך הובלה, תיאום הובלה, delivery booking | 93 | 14.8% |
| Damage | damage, повреждение, רגל שבורה, שריטה, תמונות נזק | 86 | 13.7% |
| Assembly | הרכבה, تركيب, assembly, сборка | 41 | 6.5% |
| Returns, cancellations, refunds | החזרה, return, возврат, ביטול הזמנה | 41 | 6.5% |
| Other, general, blank | אחר, שאלה כללית, (blank) | 35 | 5.6% |
| Product, promotions, stock | מבצע, שאלה על מוצר, מלאי | 26 | 4.1% |
| B2B | לקוח עסקי, מלון - הזמנה גדולה, הצעת מחיר | 23 | 3.7% |
| Invoices | חשבונית | 9 | 1.4% |

A hand tally is a sample with its own biases: one week, chosen by the manager; minutes estimated in multiples of 5; topics in the agent's words; conversations possibly under-counted on busy days. Write those limits next to every number that comes from it. Lesson 02.4 compares it with the other systems.

### Step 6 — Apply the walk-on-paper test

For each task ask four questions. Can you write: the **steps**, an **owner** for each step, the **trigger**, and the **volume**? All four yes: the task can be a candidate. Any no: it is "not yet a candidate" and the next action is to map it, not to automate it.

- **Answer "where is my order"**: trigger (customer asks), steps (order → container → sheet or logistics@ → reply), owners (agent, Tamar's team), volume (tally + exports). Walkable. And the walk shows the real fix sits upstream: the promised date.
- **Decide a damage claim**: trigger (photos), owner (Rina with Samir), volume (149 claims in six months) — but the decision step has no written criteria, the QA step is fictional and the outcome is missing on a third of claims. **Not walkable** — not yet a candidate for AI, whatever a vendor says.
- **Handle WhatsApp conversations**: trigger and owner per phone are clear; volume exists only as one week's tally. Walkable for the steps, not yet measurable: say so.

## Watch out

- **Observing without consent or with a stopwatch.** People change how they work, and you lose trust you need for the pilot. Agree the protocol, say what you will not report.
- **Treating the handbook as the process.** It is the process as someone wanted it in 2024. Record both.
- **One hour, one agent, one conclusion.** Olga and Hila work the same queue in opposite ways. Observe at least two people, and say which agent's way the numbers describe.
- **Dividing bucket hours by tickets.** It produces nonsense. Use observation and a time study for time per item.
- **Trusting a tally as an export.** It is a one-week sample with estimates. Use it, label it, and say what a proper measurement would need.
- **Skipping the walk-on-paper test because the vendor has a product.** An unwalkable process automated is the same mess, faster.
- **Writing names into the inventory.** Rows are tasks and roles. "Who" is "agents" or "claims coordinator", not a person's name, unless the person *is* the role (Rina).

## Your turn

### Inputs

- In the module download: [`company/customer-service-handbook.md`](../../labs/common/harbor-and-pine/company/customer-service-handbook.md), [`support/whatsapp-week-tally.csv`](../../labs/common/harbor-and-pine/support/whatsapp-week-tally.csv), [`support/tickets.csv`](../../labs/common/harbor-and-pine/support/tickets.csv), [`claims/damage-claims-log.csv`](../../labs/common/harbor-and-pine/claims/damage-claims-log.csv), [`people/timesheets.csv`](../../labs/common/harbor-and-pine/people/timesheets.csv), [`company/org-chart.md`](../../labs/common/harbor-and-pine/company/org-chart.md), [`documents/internal-emails-logistics-mailbox.md`](../../labs/common/harbor-and-pine/documents/internal-emails-logistics-mailbox.md).
- Sit-in notes: [`labs/module-02/observation-notes.md`](../../labs/module-02/observation-notes.md) (or your own observation of real work, with consent).
- Your interview notes from 02.2.
- Template: [task inventory](../../templates/task-inventory.md); spreadsheet version `labs/module-02/task-inventory.csv` in the module download.

### Steps

1. Write the handbook's process as numbered steps (Step 1).
2. Read the sit-in notes (or observe for an hour with the protocol in Step 2). Mark triggers, waits, workarounds, rework and unlisted channels.
3. Write the paper-versus-practice table: at least five rows, each with evidence and consequence.
4. Group the WhatsApp tally's topics into tasks and count them.
5. Build the task inventory: at least eight tasks, each with volume, time, error/rework, variation and judgment, each number with its source or "not measured".
6. Apply the walk-on-paper test to every task; list the "not yet a candidate" tasks and what mapping each needs.

### Time

90 minutes.

### Done when

- [ ] The paper process and the observed process are written side by side, with at least five differences, each with evidence.
- [ ] Every volume and time in the inventory names its source (export, tally, observation, said) or says "not measured".
- [ ] The WhatsApp tally's limits are written next to every number taken from it.
- [ ] Every task has a walk-on-paper verdict; at least one is "not yet a candidate", with the mapping it needs.
- [ ] No customer details and no individual productivity figures anywhere.

<details><summary>Reference answer</summary>

**Task inventory — Harbor & Pine Customer Service — 19 November 2026.** Volumes per month; WhatsApp = tally week × 52/12 (one week, estimates, agents' labels); helpdesk = six-month average of `tickets.csv`; phone = `phone-log.csv`.

| ID | Task | Who | Volume / month (source) | Time per item (source) | Error / rework (source) | Var. | Judgment | Walkable? |
|---|---|---|---|---|---|---|---|---|
| CS-01 | Answer "where is my order" | Agents | ~1,200 WhatsApp (tally 276) + ≥130 helpdesk (macro tag 791 ÷ 6, lower bound) + ~170 calls in hours (IVR option 1: 1,022 ÷ 6) | 2–13 min observed; up to 29+ min waiting for logistics; tally median 10 min | Repeat contacts: 59 tally notes "חוזר שוב" (9.4%); 23% of resolved tickets with an order come back (02.5) | Low | Rule | Yes |
| CS-02 | Chase the real ETA (logistics@, the sheet) | Agents → import coordinators | 187 emails Jul–Sep ≈ 62 (Tamar; mailbox) | Observed: 29 min wait | Sheet updated twice a week (stale between) | Low | Rule | Yes |
| CS-03 | Book or change a delivery day | Agents → delivery coordinators | ~400 WhatsApp (tally 93) | Tally median 10 min; observed calls 3–6 min | Not measured | Low | Rule | Yes, but owned by logistics |
| CS-04 | First answer to a damage report (photos) | Agents | ~370 WhatsApp (tally 86) + ~25 helpdesk (tag macro_damage_photos 150 ÷ 6) | Tally median 15 min | Photos stay on the WhatsApp phone (observed) | Medium | Rule | Yes |
| CS-05 | Decide a damage claim | Rina with Samir | ~25 (149 claims in 6 months, claims log) | Not measured; 8 days median to decision | Decision missing on 32% (claims log) | High | Judgment | **No**: no criteria, QA step on paper only, outcome not recorded |
| CS-06 | Returns, cancellations, refunds | Agents → Rina | ~180 WhatsApp (tally 41) + ~25 helpdesk ("Returns & refunds") | Tally median 12.5–20 min | Not measured | Medium | Rule + policy | Yes |
| CS-07 | Assembly and product questions | Agents | ~290 WhatsApp (tally 41 + 26) + ~50 helpdesk ("Product info" 298 ÷ 6) | 2–5 min observed | Not measured | Medium | Pattern | Yes |
| CS-08 | Route B2B quotes | Agents → account managers | ~100 WhatsApp (tally 23) + helpdesk B2B tag | 3 min observed | Not measured | Low | Rule | Yes |
| CS-09 | Write replies in Russian and Arabic | 6 agents who speak them | `language` column: ru 295 + ar 327 = 25% of helpdesk tickets (auto-detected, 02.5); tally 140 Russian + 83 Arabic | Olga: 13 min observed, "5 before the rule" | Not measured | Medium | Pattern | Yes |
| CS-10 | Merge or answer duplicates | Agents | ~26 helpdesk (157 ÷ 6, 02.5) + cross-channel repeats (observed, not countable) | Not measured | 113 of 157 answered twice, only 44 merged (02.5) | Low | Rule | Yes |

**Not yet candidates.** CS-05: map the decision (criteria, who decides what, within how long), record outcome and reason on every claim for eight weeks. WhatsApp as a whole: no export, so no baseline per task beyond one tally week; decide the channel (02.6) before designing anything on it.

**Paper vs practice, the three that matter most.** WhatsApp is the main written channel and absent from the handbook; the WISMO macro produces repeat contacts and the best agents bypass it; the 48-hour QA review does not exist.

</details>

## References

- law.co.il, [Monitoring employees' email severely restricted](https://www.law.co.il/en/articles/2011/04/25/monitoring-employees-email-severely-restricted/) — *Isakov Inbar*, National Labour Court, 8 February 2011: transparency of monitoring policy, less invasive means first (a secondary summary; the judgment is in Hebrew).
- Template: [task inventory](../../templates/task-inventory.md). Lab: [module 2 lab README](../../labs/module-02/README.md).
- Previous: [02.2 · The discovery interview](lesson-02.md). Next: [02.4 · Measuring a baseline from exports](lesson-04.md). Later, lesson 03.2 uses the judgment column to decide between plain automation, AI and an agent.
