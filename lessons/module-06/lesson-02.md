---
id: "06.2"
module: 6
minutes: 16
practice_minutes: 120
prerequisites: ["06.1"]
objectives:
  - "Write a 60-minute role-based session plan on the team's real work: goal, run sheet, groups, cover and the exit check."
  - "Build exercises from real messages in the team's languages, each with a planted error that one specific check catches."
  - "Decide who is trained, when and in which group, and say what happens to the people who are not."
  - "Measure the session at the level of behaviour, not attendance: an exit check now and the first weeks of use later."
volatility: concept
sources:
  - title: "IBM Lead AI Transformation: Strategy, Governance & Execution Professional Certificate (Coursera) — course 5, Lead AI Change: train → transfer → sustain, untrainable moments, risk-informed delivery, Kirkpatrick levels"
    url: https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution
last_verified: "2026-11-02"
---

# 06.2 · Training that transfers: a 60-minute role-based session

Most AI training is a features tour: what the buttons do, a few clever prompts, a survey with good scores, and on Monday the same people work the same way. In this lesson you design and run the session that Harbor & Pine's support team actually needs: 60 minutes, in groups by language, on last year's real customer messages, where each exercise hides one error that one of four checks catches. You decide who is trained and when, during the tail of the peak season, and what happens to the people who are not. At the end you have a session plan, a run sheet, eight exercise cards with a trainer key, a one-page job aid and an exit check, ready for 7–11 February.

## The situation

Monday 25 January 2027. The workflow redesign is signed ([06.1](lesson-01.md)), the drafts go live on demand for email and the web form on 1 February after a 15-minute walkthrough on 28 January ([05.6](../module-05/lesson-06.md)), WhatsApp drafts follow no earlier than 15 February after two weeks in shadow mode, and the training is booked for 7–11 February. The ROI model counted three hours per person for training ([03.7](../module-03/lesson-07.md): 14 people × 3 hours × ₪130 = ₪5,460), and the risk register's control for "training slips into peak season" is two 60-minute slots per person in that week, with cover arranged ([04.5](../module-04/lesson-05.md)). Dana warned you in November: February or March, not December ([01.7](../module-01/lesson-07.md)). February is still the tail of the peak: the team cannot lose a morning.

Two people need a decision. The two seasonal temps worked until 31 January; their agency contracts end before the training week. And Hila Dahan goes on maternity leave on 21 February, two weeks after the session.

IBM's change course names the frame: train → transfer → sustain; completion is not learning, and learning is not changed behaviour; some situations are "untrainable moments" that only workflow, tools or managers can fix; deliver in proportion to the risk. Here you build the session that gets from train to transfer.

## What to do

### Step 1 — Write the goal as something people will do tomorrow

A session goal is a behaviour on the real work, observable in the first week:

> By the end, you can open any written contact, check the AI draft in under three minutes, decide used / edited / discarded, and raise the right flag — on our real messages, in your languages.

That one sentence decides the rest: no time on how language models work, no prompt tricks (agents do not write prompts; the panel does), all the time on the checking skill, because the risk in this pilot is a wrong reply reaching a customer, and the business case dies if review takes more than 4.4 minutes ([05.4](../module-05/lesson-04.md)).

### Step 2 — Decide who, when, and in which group

Write the roster decision down, with reasons:

| Who | Decision | Reason |
|---|---|---|
| 11 support agents + Olga | Session 1 and session 2 in language groups, 8–11 February | They draft every day |
| Olga, Lina, Shani | Champions: do all eight cards in a dry run on Sunday 7 February; co-train their language group | Trainees ask colleagues before they ask you ([06.3](lesson-03.md)) |
| Samir | Role version with Rina, Thursday 11 February | Manager: the switch, the flags, team numbers, his own visible use |
| Rina | Role version: claims and inbound translation | She decides claims; the draft never does |
| Hila | Trained with her group | Two weeks of use before her leave; on return she redoes session 2 with a champion |
| The two seasonal temps | **Not trained in February** | Their contracts ended 31 January. If temps are hired for the next peak, session 1 plus the job aid is their first-week onboarding; the cost goes into the temps decision at gate 2 |

Groups by language, two to four people, so that every card is in the trainees' own languages and nobody hides at the back. At most four people off the queue at once; Samir signs the cover.

### Step 3 — Build the exercises from the team's real messages

Generic examples teach generic skills. Take real messages from the helpdesk export (`support/emails.csv`) in each language and category, show the facts the panel will show beside them, and write a draft **with one planted error** that one specific check catches. Include one draft that is right, so people learn not to rewrite good drafts. At Harbor & Pine the eight cards (`labs/module-06/training/exercise-cards.md`) are:

| Card | Message (real) | What the draft gets wrong | The check |
|---|---|---|---|
| 1 Hebrew, WISMO | EM-32160, family event on 31/5 | Nothing: date matches the ETA field | Don't rewrite a good draft |
| 2 Russian, WISMO | EM-32768, "please answer in Russian" | ETA blank, so the draft repeats the passed checkout date | Dates |
| 3 Arabic, damage | EM-33631, broken glass (last year answered in Hebrew) | Promises a replacement in 3 days | Promises |
| 4 Arabic, return | EM-31849, garden set | Pickup fee ₪150; the policy says ₪250 | Numbers |
| 5 Russian, assembly | EM-32882, technician did not come | Sends assembly instructions | Does it answer the question? |
| 6 English, hotel quote | EM-32680, 24 chairs and 20 tables | Invented prices and total, a placeholder | Numbers, promises, scope |
| 7 Hebrew, child hurt + lawyer | Written for the session | Offers 20% and "no need for lawyers"; no flags | Flags |
| 8 WhatsApp, Russian | Written for the session | "Order not found" for a web-store number; letter-style | Missing information; channel register |

Card 5 is worth noticing: last year an agent made exactly the same mistake. The drafts make the team's own error patterns visible; say so in the room, it lowers the temperature.

> [!NOTE]
> The cards use last year's real customer messages, which already sit in the company's helpdesk; the trainees see nothing they could not open in Deskly. Keep the printed cards inside the office and shred them after the session, as you would any customer data (handbook §10).

### Step 4 — Write the run sheet: one third show, two thirds do

The 60 minutes, in blocks ([`session-script.md`](../../labs/module-06/training/session-script.md) has the full text):

| Minutes | Block |
|---|---|
| 0–5 | Why, what changes, what does not, what is logged and how it is reported; "what worries you?" on the board |
| 5–12 | Live demo on cards 1 and 2: think aloud through the four checks |
| 12–37 | Hands-on: four cards each, at their own screen, in the training copy of Deskly |
| 37–47 | Debrief: each card, which check caught it |
| 47–53 | Flags and the stop button: who clears what, what Samir can switch off |
| 53–57 | Job aid, champions, office hours, session 2 |
| 57–60 | Exit check (one fresh card, observed) and two questions |

Three rules for the trainer. Do not answer "is this right?"; ask "what on the screen tells you?". Answer "will this replace me?" with the approved FAQ wording only ([06.5](lesson-05.md)). Write every complaint about the drafts down as an issue, never argue it in the room.

**Session 2** (practice clinic, same week) is not a second lecture: 50 minutes on the trainee's own live queue with the champion beside them, every discard with its reason, then ten minutes naming one thing the drafts get wrong in their language. That list is the first agenda of the champions' huddle.

### Step 5 — Make the job aid the thing they keep

One page beside the screen, in their language: the rule ("you send every reply; you may discard any draft"), the four checks (names, dates, numbers, promises), the three marks, the four flags that stop the line, the WhatsApp differences, where to get help (`labs/module-06/training/job-aid.md`). If the session is forgotten by March, the job aid is what remains; it is also what an onboarding temp gets next winter.

### Step 6 — Measure behaviour, not attendance

Kirkpatrick's four levels, used honestly:

1. **Reaction** — two questions at the end ("how useful for your real work, 1–5?", "what will you do differently tomorrow?"). Useful for the next session, not evidence of anything else.
2. **Learning** — the exit check: one fresh card, observed; four checks applied, correct mark, flag raised if needed, reply ready to send (`proficiency-check.csv`). Those who miss it do the card again with the champion in session 2. The results stay with the trainer and the champion; they never go to the manager.
3. **Behaviour** — weeks 2–8 of real use: the qualified-use rate and the discard reasons, by team and week ([06.4](lesson-04.md)).
4. **Results** — gate 1 on 1 April: acceptance, review minutes, wrong replies reaching customers ([05.1](../module-05/lesson-01.md)).

Write in advance which number at which level would make you change the session, for example: "if fewer than 8 of 12 pass the exit check, session 2 becomes a second hands-on on the cards, not the live queue".

## Watch out

- **The features tour.** If more than 15 minutes are you talking, you are teaching the tool, not the work. Cut slides until the hands-on block is at least 25 minutes.
- **Invented examples.** "Customer X asks about product Y" teaches nothing about Harbor & Pine's blank ETA field or web-store order numbers. Use the export.
- **Training before the workflow is fixed.** If the macro is still there and the WhatsApp phones are still on the desk, the session teaches a workflow that does not exist. 06.1 comes first.
- **Training everyone the same way.** The manager and the claims coordinator need different exercises; the session for Samir is about the switch, the flags and his own visible use.
- **A test with consequences.** If the exit check goes to the manager, people will practise passing it, not checking drafts. Say who sees the results before the check.
- **Treating untrainable problems as training gaps.** A draft that is slow to load or too formal for WhatsApp is a design problem. Log it; no session fixes it.

## Your turn

### Inputs

- In the module download: [`support/emails.csv`](../../labs/common/harbor-and-pine/support/emails.csv), [`people/timesheets.csv`](../../labs/common/harbor-and-pine/people/timesheets.csv), [`usage/hr-roster.csv`](../../labs/common/harbor-and-pine/usage/hr-roster.csv), [`company/customer-service-handbook.md`](../../labs/common/harbor-and-pine/company/customer-service-handbook.md); the training folder `labs/module-06/training/` (session script, exercise cards, trainer key, job aid, run sheet, exit check; [lab README](../../labs/module-06/README.md)).
- The workflow redesign from 06.1; the categories and flags from module 5 (`labs/module-05/categories.md`).
- Template: [training session plan](../../templates/training-session-plan.md).

### Steps

1. Write the session goal as a behaviour on the real work.
2. Decide the roster: groups, the role versions, Hila, the temps; reasons for each.
3. Pick six to eight real messages from `emails.csv` across the four languages (one per check, one correct draft) and write a draft with one planted error for each. Add one WhatsApp card. If you prefer, critique and improve the eight cards in the lab instead of writing new ones.
4. Write the 60-minute run sheet and session 2.
5. Adapt the job aid to your checks.
6. Write the exit check and the rule that would change the session.
7. Run it: with two colleagues or friends playing agents, or alone with an LLM chat playing a sceptical agent on two cards. Note where people hesitated.

### Time

120 minutes: 30 for roster and goal, 45 for the cards, 20 for the run sheet and job aid, 25 to run a dry run.

### Done when

- [ ] The goal names a behaviour you could observe in week 2.
- [ ] Every person on the roster has a group or a reason why not, including the temps.
- [ ] Every exercise uses a real message (or says why it is written for the session), and each planted error maps to one check.
- [ ] At least 25 of the 60 minutes are hands-on.
- [ ] The exit check, who sees its results, and the rule that would change the session are written down.
- [ ] You ran the session once and changed at least one thing because of what happened.

<details><summary>Reference answer</summary>

**Training session plan — "Your drafts, your call" — v1.1, 26 January 2027** (owner: pilot lead; approved: Samir Haddad; cover: Samir, overtime cover up to 6 hours approved by Michal)

*Goal:* as in Step 1.

*Roster and groups* (`run-sheet.csv`): champions' dry run Sun 7 Feb 13:00 (Olga, Lina, Shani; all eight cards). Session 1: G1 Russian (Yana, Sergei; co-trainer Olga) Mon 8 Feb 08:30; G2 Arabic (Rami, Ahmad; Lina) Mon 14:00; G3 Hebrew A (Hila, Moran, Adi; Shani) Tue 9 Feb 08:30; G4 Hebrew and English (Tigist, Daniel; Shani) Tue 14:00. Session 2 for each group two days later, on the live queue with the champion. Role session (Samir, Rina) Thu 11 Feb 11:00. Temps: not trained (contracts ended 31 January); onboarding version for any future temp = session 1 + job aid in week 1. Hila trained; refresher on return. Total: 14 people × 3 hours (two sessions + one hour with a champion in weeks 2–4) = 42 hours ≈ ₪5,460, as in the ROI model.

*Exercises:* the eight cards in Step 3; groups get two cards in their language, one Hebrew, card 8 (see the run sheet).

*Run sheet:* as in Step 4. Hands-on 25 minutes + debrief 10 = 35 of 60 minutes with the trainees working.

*Measures:* reaction (two questions); learning (exit check, results to trainer and champion only); behaviour (06.4, team-level, weeks 2–8; discard reasons by language); results (gate 1). Change rule: fewer than 8 of 12 pass → session 2 repeats the cards; any language with fewer than half its trainees passing → that champion runs a third hour in week 3.

*What the dry run changed (Sunday 7 February):* (1) card 8 took 9 minutes, because nobody knew where the web-store number field was → the trainer shows it in the demo; (2) Lina said the Arabic drafts use formal Arabic (fusha) where customers write in spoken Arabic, and the drafts are too long for WhatsApp → logged as issue I-03 for the WhatsApp style check before 15 February, not argued in the session; (3) Olga asked that the "what is logged" sentence be read word for word from the comms pack, because "the team will ask exactly that" → done.

*How it went* (from the exit sheet and the two questions): 11 of 12 agents passed the exit check at the first attempt; the twelfth (card 5, sent the instructions) passed in session 2. Usefulness 4.3 of 5. The most common "what will you do differently": "check the ETA date before sending" (7 of 12). The most common worry on the board: "will they count how many drafts I use?" — answered from the FAQ: team and week only, never in performance reviews.

**What this plan cannot fix, written to Samir the same day:** WhatsApp drafts are not switched on until 15 February, after training; the Russian and Arabic WhatsApp register is untested. The session teaches the checks; whether WhatsApp drafts are usable is a design question for shadow mode, and the first weeks of use will show it.

</details>

## References

- IBM, [Lead AI Transformation certificate](https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution), course 5 (train → transfer → sustain; untrainable moments; Kirkpatrick levels; risk-informed delivery). Named, not re-taught.
- Template: [training session plan](../../templates/training-session-plan.md).
- Lab: `labs/module-06/training/` in the module download ([README](../../labs/module-06/README.md)).
- Earlier: [06.1 · Workflow redesign](lesson-01.md), [05.1 · The pilot charter](../module-05/lesson-01.md), [03.7 · The ROI model](../module-03/lesson-07.md). Next: [06.3 · Champions network and office hours](lesson-03.md).
