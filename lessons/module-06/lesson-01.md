---
id: "06.1"
module: 6
minutes: 17
practice_minutes: 75
prerequisites: ["05.1", "02.3"]
objectives:
  - "Map a team's real workflow step by step and mark every step keep, change, remove or new once the AI output is in place."
  - "Remove the old path for each step the tool replaces, with a date and an owner, so the new way is the easiest way."
  - "Write down where the freed hours go, who decides it and how it will be seen, before go-live."
  - "Write a change-impact table by role that includes the receiving teams outside the pilot."
volatility: concept
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera) — course 3, readiness: organizational readiness as redesigned workflow, reviewer authority, demonstrated skill and reinforcement; saved hours refill by default"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "IBM Lead AI Transformation: Strategy, Governance & Execution Professional Certificate (Coursera) — course 5, Lead AI Change (go-live is not the goal; untrainable moments)"
    url: https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution
last_verified: "2026-11-02"
---

# 06.1 · Workflow redesign: change the work, not just add a tool

A drafting panel added to an unchanged workflow becomes one more window agents may or may not open, next to the old macro, the old phone and the old habit. In this lesson you redesign the written-reply work of Harbor & Pine's support team around the drafts: every step of today's process marked keep, change, remove or new, the old paths switched off with a date and an owner, the decision rights and handoffs written down, and the freed hours given a destination before anyone can quietly absorb them. At the end you have workflow redesign v1.0, a change-impact table by role and a list of handbook changes, signed by Samir and Michal before go-live on 1 February.

## The situation

Tuesday 12 January 2027. The pilot charter is signed ([05.1](../module-05/lesson-01.md)): drafts for every written contact, an agent sends every reply, gate 1 on 1 April. The steering group meets on 19 January, and on 1 February three things happen at once: WhatsApp moves from the four shared phones into the helpdesk, the drafts panel goes live for email and the web form, and the date fix (live since mid-January) starts showing in fewer "where is my order?" contacts. Training is booked for 7–11 February ([06.2](lesson-02.md)).

So far everyone has talked about the tool. Nobody has written down what an agent does differently at 09:00 on 1 February. If you leave it there, the handbook will still tell agents to send the order-status macro that repeats a date that has passed, the WhatsApp phones will still sit on the desk, logistics will still get 60 chasers a month, and the 109 hours a month the business case counts on will disappear into the queue without anyone seeing them go.

The IBM certificates name the problem in two lines: go-live is not the goal, and organizational readiness means the workflow was redesigned, reviewer authority was placed, skill was shown and use is reinforced after launch week; saved hours refill by default unless someone decides where they go. Here you do the redesign.

## What to do

### Step 1 — Walk today's workflow, per channel, from evidence

Start from what people do, not from the handbook. You already have the evidence: the process walk and observation notes from [02.3](../module-02/lesson-03.md), the WhatsApp tally, the time sheets and the emails. Write one row per step, for each channel, with who does it, the tool and what it costs.

For a written "where is my order?" contact at Harbor & Pine, today:

| # | Step today | Who | Tool | Evidence |
|---|---|---|---|---|
| 1 | Message arrives: email or web form into Deskly; WhatsApp onto one of four shared phones | — | Deskly / phones | Tally week 18–22 Oct: 630 WhatsApp conversations, 94 Deskly tickets (`support/whatsapp-week-tally.csv`) |
| 2 | Pick the oldest ticket in your language view; WhatsApp: whoever holds the phone | Agent | Deskly / phone | Handbook §4.1, §7 |
| 3 | Find the order in Priority; on WhatsApp the customer quotes the web-store number (HP-1…), so look it up in StoreHub first | Agent | Priority, StoreHub | Handbook §4.2; finding 18 |
| 4 | Send the "Order status – delay apology" macro, which repeats the promised date from the order | Agent | Deskly macro | Handbook §6; the best agents skip it (Olga, 02.2) |
| 5 | Or: email logistics@ for the real date and wait, or open Tamar's sheet | Agent, logistics | Email, ETA sheet | 187 Customer Service emails to logistics@ in Jul–Sep (`documents/internal-emails-logistics-mailbox.md`) |
| 6 | Russian or Arabic reply: some agents paste the message into a free chatbot or translation extension | Agent | Personal tools | Census 01.6; the AUP and approved list replaced these in November (04.1, 04.2) |
| 7 | Send, set "Resolved"; on WhatsApp nothing is recorded | Agent | Deskly / phone | Handbook §4.5; tally |
| 8 | Log the time as "email" in the weekly time sheet | Agent | Time sheet | 70.7% of logged hours in the "email" bucket (`people/timesheets.csv`) |

Do the same for a damage report (photos request → Rina opens a claim → "QA within 48 hours", which does not exist → decision, median 8 days) and for a return. Three workflows cover most of the written work.

### Step 2 — Mark every step: keep, change, remove or new

Put the draft into the workflow and go through the steps one by one. Four marks, each with a reason:

- **Keep** — the step still adds something the draft cannot (Rina's claim decision).
- **Change** — the step stays but is done differently (finding the order: the draft shows the order and the ETA; the agent checks them instead of searching).
- **Remove** — the draft or the date fix makes the step pointless, *and you switch off the old way* (the delay-apology macro).
- **New** — a step the pilot adds (mark the draft used / edited / discarded; clear or escalate a flag).

The test of a good redesign: for every "change" and "remove", the new way must be the **easiest** way at that moment of the day. If the macro is still one click away and the draft is two, the macro wins at 16:20 on a Thursday in a queue of 80. That is why "remove" always comes with a date and an owner for switching the old path off, never "agents should prefer the draft".

### Step 3 — Put the draft where the work happens

Small design choices decide whether the tool is used. Agree them with Samir, Olga and the integrator, in writing:

1. **The draft lives inside the ticket, beside the customer's message**: the panel opens with the ticket, and one click on "Draft" produces it in about three seconds. Not a separate window, not a copy-paste into another tool. (Generating a draft on every ticket open was tried in the dry run and dropped: it drafted spam and duplicates and slowed the ticket view.)
2. **Insert, edit, send** in the normal reply box; the three marks (used as is / edited / discarded, with a reason for discarded) are one click each, as the rule of use says ([05.1](../module-05/lesson-01.md), Step 6).
3. **The facts shown next to the draft**: the order number in both systems (SO26… and HP-1…), the current ETA from the date fix with its last update date, and the source of any figure the draft quotes. A reviewer who sees the source checks; one who sees only fluent text approves ([05.5](../module-05/lesson-05.md)).
4. **Language**: the draft's language comes from the message text, not from Deskly's auto-detected field (85 wrong and 121 blank codes in May–October; [02.5](../module-02/lesson-05.md)).
5. **WhatsApp is not email.** Replies there are two or three lines, informal, often answering a photo or a voice note. Ask for a WhatsApp draft style (short, no letter-style greeting and signature) before WhatsApp drafts go live, and test it on real WhatsApp messages in shadow mode ([05.6](../module-05/lesson-06.md)). Write it down as a condition, because the test set has no WhatsApp ([05.2](../module-05/lesson-02.md)).

### Step 4 — Write the decision rights and the handoffs

A redesign that moves work also moves responsibility. For each handoff, name who decides and what the next person receives.

| Handoff | From → to | What changes | Who decides |
|---|---|---|---|
| ETA for a late order | Logistics → agent | The ETA field in Priority, updated by logistics every working day by 10:00, replaces emails to logistics@ | Tamar owns the field; agents email logistics@ only if the ETA is blank or older than 7 days |
| Flagged message (safety, legal threat, privacy request, refund exception) | Agent → Olga or Samir | Drafts for flagged messages are short acknowledgements; the senior clears the flag | Only Samir or Olga clear these flags (rule of use) |
| Damage claim | Agent → Rina | Draft asks for photos and the carton label, opens nothing; Rina opens the claim | Rina and Samir decide; the handbook's "QA within 48 hours" is removed and replaced by "decision within 5 business days of photos" (the service level already in §3) |
| A draft that keeps getting the same thing wrong | Agent → champion → pilot lead | One line in the issues log ([06.3](lesson-03.md)), not a private workaround | Pilot lead; prompt changes only through change control ([05.7](../module-05/lesson-07.md)) |

The first row is the one people forget: the pilot makes logistics a **receiving team**. Tamar's team gains a daily duty (keep the ETA field current) and loses about 60 chaser emails a month. Ask her what she can absorb before you write the row, and put it in her team's routine, not in a note.

### Step 5 — Remove the old paths, with dates

List every old path and say when and by whom it is switched off. At Harbor & Pine:

| Old path | Switched off | Owner | Why it must go |
|---|---|---|---|
| "Order status – delay apology" macro (4 languages) | 1 February, deleted from Deskly | Samir | Repeats a date that has passed; the draft quotes the updated ETA |
| The four shared WhatsApp phones | 1 February: numbers move to Deskly's WhatsApp channel; phones handed to Avi on 4 February after a three-day overlap | Samir, Avi | No log, no data boundary, customer data on shared devices (handbook §10 already forbids it) |
| The WhatsApp Business saved replies on those phones | Not migrated into Deskly | Avi, integrator | They contain the same old delivery-date line as the macro |
| Free chatbots and the free translation extension | Already removed in November (04.2) | Avi | The approved tools and the drafts cover the need |
| "QA within 48 hours" in the handbook | Handbook v4.0, 1 February | Samir | A control that exists only on paper (02.3) |

An old path you do not remove becomes the place people go back to when the new one is annoying. In module 6's adoption data you will see exactly that happen ([06.4](lesson-04.md)).

### Step 6 — Decide where the freed hours go

The business case expects about 109 net hours a month at peak volume ([03.7](../module-03/lesson-07.md)). If nobody decides where they go, they refill: slower replies, longer chats, more chasing. Write the destination down, in order, with an owner and the number that will show it:

1. **February–April:** first response on WhatsApp (never measured; the helpdesk will measure it from 1 February) and the wait for Russian and Arabic replies. Owner: Samir. Shown by: median first response per channel and language.
2. **May–October:** a working Friday rota and the backlog of open damage claims (median 8 days to a decision today). Owner: Samir with Rina.
3. **November 2027 – January 2028 (peak):** the hours replace the two seasonal temps, if gate 2 confirms them (₪96,000, the case's only cash line). Owner: Michal. Shown by: agent hours needed at peak vs hours available.

Say in the same paragraph what the hours are **not** for: they are not a headcount reduction of the permanent team. That sentence must be true and approved before you write it; lesson [06.5](lesson-05.md) gets it approved.

### Step 7 — Write the change-impact table and the handbook changes

One row per role, including the people outside the support team:

| Role | What changes on 1 February | What they need | Risk if ignored |
|---|---|---|---|
| Support agents (11) | Draft beside every written contact; three marks; WhatsApp in Deskly; no delay macro | 60-minute session on their own languages (06.2), job aid, a champion nearby | Use the draft unread, or ignore it and type as before |
| Olga (senior agent) | Clears flags; Russian spot checks; champion | Protected time (2 hours a week) | Becomes the bottleneck for every question |
| Rina (claims) | Damage drafts request photos only; she decides | Claims log fields for the decision (outcome recorded) | Drafts that promise replacements she has not approved |
| Samir (manager) | Owns the switch, the stop rules and the freed hours | Weekly team-level numbers, not individual ones | Reads the panel being open as use |
| Logistics (Tamar's team) | Keeps the ETA field current daily | Ten minutes a day, written into their routine | Drafts quote stale ETAs; WISMO comes back |
| IT (Avi) | WhatsApp channel, phones collected, logs | Integrator support for three days | Phones stay in drawers and come back into use |

Then list the handbook changes for v4.0 (§2 channels add WhatsApp, §4 working a ticket with a draft, §6 macros without the delay apology, §8 claims without the QA step, a new section on the three marks and the flags) and get Samir to own the rewrite, in the team's languages.

### Step 8 — Sign it, and test it before go-live

The redesign is signed by Samir (owner) and Michal (sponsor) and walked through in the dry run on 28 January: one agent per language works five real messages from start to finish in the new workflow while you watch where they hesitate. Every hesitation is either a fix to the design or an item for the training session.

## Watch out

- **Redesigning the tool, not the work.** A spec for the panel is not a workflow redesign. If no step was removed and no handoff changed, you added a tool.
- **"Remove" without a switch-off.** Leaving the old macro "for emergencies" keeps it as the default. Delete it, or set a date and a name.
- **Forgetting the receiving team.** Logistics now owns a field that customers' replies depend on. If that duty is not in Tamar's routine, the drafts will quote stale dates within a month.
- **Leaving the freed hours unassigned.** Unassigned capacity refills; then gate 1 shows "hours saved" that no budget ever sees, and the temps are hired again.
- **Copying email habits into WhatsApp.** A letter-style draft in a chat is slower to fix than typing two lines. Plan a WhatsApp style and test it on WhatsApp messages before switching it on.
- **Writing it alone.** The people who do the work find the steps you cannot see. Run the redesign with Samir, Olga and Rina, and Tamar for the ETA row.

## Your turn

### Inputs

- In the module download: [`company/customer-service-handbook.md`](../../labs/common/harbor-and-pine/company/customer-service-handbook.md), [`support/whatsapp-week-tally.csv`](../../labs/common/harbor-and-pine/support/whatsapp-week-tally.csv), [`support/emails.csv`](../../labs/common/harbor-and-pine/support/emails.csv), [`people/timesheets.csv`](../../labs/common/harbor-and-pine/people/timesheets.csv), [`documents/internal-emails-logistics-mailbox.md`](../../labs/common/harbor-and-pine/documents/internal-emails-logistics-mailbox.md).
- The pilot charter and rule of use ([05.1](../module-05/lesson-01.md)); your task inventory and observation notes ([02.3](../module-02/lesson-03.md)).
- Template: [workflow redesign](../../templates/workflow-redesign.md); spreadsheet version `labs/module-06/workflow-redesign.csv` ([lab README](../../labs/module-06/README.md)).

### Steps

1. Write today's steps for three workflows: a written WISMO contact, a damage report, a return request. Each step with who, tool and evidence.
2. Mark every step keep / change / remove / new with a reason.
3. Write the five design choices for where the draft appears (Step 3).
4. Fill the handoff table, including logistics as a receiving team.
5. List every old path with its switch-off date and owner.
6. Write where the freed hours go, in order, with owner and indicator, and what they are not for.
7. Fill the change-impact table by role and list the handbook changes.

### Time

75 minutes: 25 for today's steps, 20 for the marks and design choices, 15 for handoffs and old paths, 15 for hours and impact.

### Done when

- [ ] Every step of the three workflows has a mark and a reason.
- [ ] Every "remove" has a switch-off date and a named owner.
- [ ] The draft's placement says where it appears, what facts sit beside it and how WhatsApp differs.
- [ ] Logistics appears as a receiving team with its new duty and what it can absorb.
- [ ] The freed hours have a destination, an owner and an indicator, and the paragraph says what they are not for.
- [ ] The handbook changes are listed with an owner.

<details><summary>Reference answer</summary>

**Workflow redesign v1.0 — written replies with AI drafts — Harbor & Pine Customer Service — 18 January 2027** (owner: Samir Haddad; sponsor: Michal Peretz; written with Olga Petrenko, Rina Azoulay and, for the ETA row, Tamar Shalev)

**Written WISMO contact**

| # | Today | Mark | With drafts (from 1 February) | Reason |
|---|---|---|---|---|
| 1 | Email/form into Deskly; WhatsApp on 4 phones | Change | All three channels into Deskly; WhatsApp channel live 1 Feb | One queue, one log, one data boundary |
| 2 | Oldest ticket in language view; phone holder takes WhatsApp | Change | Language views include WhatsApp; WhatsApp tickets routed like email | No more "who has the phone" |
| 3 | Search Priority; StoreHub for HP-1… numbers | Change | Panel shows both order numbers and the ETA with its update date; agent checks, does not search | Removes the lookup; finding 18 needs the StoreHub mapping in the integration |
| 4 | Delay-apology macro with the passed date | **Remove** | Deleted from Deskly on 1 Feb (Samir) | It sends a wrong date |
| 5 | Email logistics@ and wait | Change | Only if the ETA is blank or older than 7 days | Tamar's team keeps the field current by 10:00 daily |
| 6 | Free chatbot for ru/ar | Removed in Nov 2026 | Draft in the customer's language | Approved path is easier |
| 7 | — | **New** | Insert the draft, edit, send; mark used / edited / discarded | Rule of use; the marks are gate-1 data |
| 8 | Send, set Resolved | Keep (for now) | Unchanged; "resolved on reply" logged as change request CR-11 for after gate 1 | Changing it now would break the repeat-contact baseline |

**Damage report:** photos-request macro → *change* (the draft asks for photos and the carton label in the customer's language, promises nothing); Rina opens the claim → *keep*; "QA within 48 hours" → *remove* from the handbook; decision → *keep* (Rina and Samir, within 5 business days of photos; outcome recorded in the claims log, every claim); customer informed → *change* (Rina's reply drafted, she edits and sends). **Return request:** returns-policy macro → *change* (draft quotes the policy and the pickup fee from the policy text, not from memory); refund → *keep* (finance, 14 business days).

**Draft placement:** panel opens with the ticket, one click to draft (about three seconds); beside the message; both order numbers, ETA and its date, and the source line under the draft; language from the text; WhatsApp drafts at most three lines, no greeting block or signature, switched on only after a WhatsApp check in shadow mode (target 15 February).

**Old paths:** delay macro (1 Feb, Samir); phones (numbers moved 1 Feb, handed to Avi 4 Feb); phones' saved replies (not migrated, Avi and the integrator; check on 4 Feb that Deskly's WhatsApp quick replies list is empty); "QA" line (handbook v4.0, Samir).

**Freed hours:** (1) Feb–Apr WhatsApp first response and ru/ar waits, Samir, median first response per channel and language; (2) May–Oct Friday rota and claim backlog, Samir and Rina; (3) peak 2027 replaces the two temps if gate 2 confirms it, Michal, hours needed vs available. Not a reduction of the permanent team (wording approved by Michal and Yoav in the comms pack, 06.5).

**Impact by role:** as in Step 7. Tamar agreed to ten minutes a day for the ETA field, done by her coordinator, on condition that agents stop emailing logistics@ about orders that have a current ETA.

**Handbook v4.0 (Samir, 1 February, Hebrew, Arabic, Russian, English):** §2 add WhatsApp; §4 rewrite for drafts; §6 remove the delay macro; §8 remove QA, add "decision within 5 business days, outcome recorded"; new §11 "The draft: three marks and four flags".

**Open after the dry run (28 January):** Ahmad and Moran asked who answers WhatsApp voice notes (answer: the agent listens, the draft answers the text only); Sergei found the Russian drafts "too polite for WhatsApp" — logged for the WhatsApp style check before 15 February.

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting), course 3 (organizational readiness; saved hours refill by default); IBM, [Lead AI Transformation certificate](https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution), course 5 (go-live is not the goal). Named, not re-taught.
- Template: [workflow redesign](../../templates/workflow-redesign.md); [task inventory](../../templates/task-inventory.md).
- Earlier: [02.3 · Process walk and task inventory](../module-02/lesson-03.md), [05.1 · The pilot charter](../module-05/lesson-01.md), [05.5 · Human-in-the-loop design](../module-05/lesson-05.md), [05.6 · Shadow mode and staged release](../module-05/lesson-06.md). Next: [06.2 · Training that transfers](lesson-02.md).
