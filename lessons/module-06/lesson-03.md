---
id: "06.3"
module: 6
minutes: 15
practice_minutes: 60
prerequisites: ["06.2"]
objectives:
  - "Choose champions by language group and by the respect they have for the work, and give each protected time and a written limit on what they do."
  - "Run an issues log and a weekly huddle that turn champions' observations into decided changes, and tell the team what changed."
  - "Set up office hours that help on live work without tracking who attends."
  - "Spot a champion who has become a single point of failure and plan the back-up."
volatility: concept
sources:
  - title: "IBM Lead AI Transformation: Strategy, Governance & Execution Professional Certificate (Coursera) — course 5, Lead AI Change: resistance as information, capability support, reinforcement after launch"
    url: https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera) — course 3, readiness: reinforcement after launch week; resistance concentrates with experts"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
last_verified: "2026-11-02"
---

# 06.3 · Champions network and office hours

After the training week, people stop asking the trainer and start asking whoever sits next to them. Champions make sure that person knows the answer, and that what they hear on the floor reaches someone who can change the tool. In this lesson you choose Harbor & Pine's three champions, give them time and a written limit on their role, set up the issues log, the weekly huddle and the office hours, and run the first four weeks of the log. At the end you have the champions playbook v1.0 and a log in which every issue has a decision, an owner and a date the team was told.

## The situation

Thursday 28 January 2027, four days before go-live. The training plan names three co-trainers ([06.2](lesson-02.md)): Olga for Russian, Lina for Arabic, Shani for Hebrew. Samir assumed "champion" meant "the people who like the tool". He also assumed Olga would do it on top of everything else: senior agent, unofficial team lead, Russian spot checks, flag clearer, test-set labeller.

IBM's change course treats resistance and silence as information and asks for reinforcement after launch week; the consulting certificate adds that reinforcement is part of organizational readiness, not an extra. Neither says how to run a champions network on a team of fourteen. That is this lesson.

## What to do

### Step 1 — Write down what champions are for, and what they are not

Three jobs, nothing more:

1. **Help on real work.** Sit beside a colleague with a live ticket; answer "is this draft right?" with "what does the ETA field say?".
2. **Collect what goes wrong**, with an example ticket, in the issues log. Not opinions ("the Arabic is bad"), examples ("T-50391: formal Arabic to a customer who wrote in spoken Arabic").
3. **Carry decisions back** to the team: what changed this week and why.

And three things they never do, written in the playbook so nobody can ask them to: report who uses the drafts and who does not; change prompts or settings themselves (changes go through change control, with the test set re-run; [05.7](../module-05/lesson-07.md)); decide claims, refunds or flags that the rule of use reserves for Samir and Olga as seniors (Olga clears flags as senior agent, not as champion).

The first "never" is the one that keeps the network alive. A champion who is seen as the manager's eyes stops hearing anything useful within two weeks.

### Step 2 — Choose by language and by respect, not by enthusiasm

Criteria, in order:

1. **One per language group** that drafts: Russian, Arabic, Hebrew (English is one person, Daniel; Olga covers it).
2. **Respected for the work**, by colleagues, not only by the manager. Ask Samir and two agents separately: "who do you ask when a reply is tricky?"
3. **Willing**, asked privately, with the right to say no.
4. **Not only enthusiasts.** One champion who is openly sceptical but fair makes the network credible ("even Lina says the Arabic got better").

At Harbor & Pine: **Olga** (Russian; everyone already asks her), **Lina** (Arabic; careful, sceptical of the formal-Arabic drafts after the dry run), **Shani** (Hebrew; steady, sits in the middle of the room, not yet overloaded). Tigist, who started slowly, is a good candidate for the second round.

### Step 3 — Give them time, and make it real

Two hours a week each, protected in Samir's rota for eight weeks, then reviewed at gate 1. "Protected" means the rota shows it and the queue is covered: champion time that comes out of their own queue is overtime by another name. The hours come from the first destination of the freed hours ([06.1](lesson-01.md), Step 6), so the redesign pays for its own support. Over eight weeks: 3 × 2 × 8 = 48 hours, about ₪6,240 at ₪130 an hour. Tell Ronit: it is a running cost of the pilot, not part of training.

What champions get: early access to changes, a direct line to the pilot lead, their names in Michal's monthly note (with their consent), and a say in which issue is fixed first.

### Step 4 — Run the issues log and the weekly huddle

The issues log (`labs/module-06/champions-issues-log.csv`) has one row per problem, not per complaint:

| Field | Example (I-02) |
|---|---|
| Logged, by, language, channel, category | 3 Feb, Olga, all, email, WISMO |
| What went wrong, with an example ticket | ETA blank → draft repeats the passed checkout date; T-50240; about 1 in 12 WISMO drafts |
| Decision | Prompt change: if the ETA is blank or older than 7 days, the draft says "we are checking" and when we will write again |
| Change reference and owner | PC-02, test set re-run 9 Feb, released 10 Feb; pilot lead |
| Told the team | Huddle note 14 Feb; job aid v1.1 |

The **huddle** is 20 minutes every Sunday at 12:30: the three champions and the pilot lead (Samir joins every second week). Agenda: new issues, top three by how often they happen and how much harm they could do, a decision on each (fix in configuration, prompt change through change control, job-aid or training change, or "won't fix" with a reason), and the three lines that go to the team. Every issue gets a decision within two huddles, even if the decision is "not now, because".

The last column matters most. A team that reports problems and never hears back stops reporting and starts working around the tool. Michal's monthly note and a three-line message after each huddle ("this week we changed… because you told us…") close the loop.

### Step 5 — Set up office hours that people actually use

Weekly, 45 minutes, the same slot (Tuesday 13:00–13:45), at the desks, on live tickets, with the pilot lead and one champion. "Bring a stuck ticket" is the whole format. Record the topics, never the names: who attends is nobody's business, and if attendance looks like a register, the people who most need help stay away. In the first four weeks the topics are a second issues feed: three of the first ten were about the WhatsApp drafts.

### Step 6 — Watch the champions' own load

Olga now holds six roles. If she is sick in week 4, Russian spot checks, flag clearing, the Russian champion role and half the test-set labelling stop at once. Name a back-up for each role (Yana for Russian checks and as second Russian champion; Samir for flags) and check her hours in the rota every two weeks. A champion network that depends on one person is a single point of failure with a friendly name.

### Step 7 — Plan the end

Champions are a launch structure. At gate 1 decide: rotate (Tigist and Yana take over), shrink to one per language with one hour a week, or end, with office hours kept monthly. Say this in the playbook so that nobody's role quietly becomes permanent unpaid work.

## Watch out

- **Champions as monitors.** The moment a champion reports who is not using the drafts, the network dies. Put the limit in writing before anyone asks.
- **Time that does not exist.** Champion hours that are not in the rota come out of the champion's queue or her evenings. Cover them, or do not appoint champions.
- **A log that only collects.** Issues without decisions and without a message back to the team teach people that reporting is pointless.
- **Champions who change the tool themselves.** Fixing the Russian prompt directly feels efficient and skips the test set; the next change breaks something nobody can trace. All changes go through change control, and champions own the evidence, not the switch.
- **Choosing only fans.** If every champion loved the tool from day one, the sceptics will treat the network as marketing.
- **Forgetting the receiving teams.** Logistics and Rina get issues too (stale ETAs, claim drafts); they need a route into the log.

## Your turn

### Inputs

- In the module download: `labs/module-06/champions-issues-log.csv` (weeks 1–8 of the log), `labs/module-06/queue-rota-2027.csv` (Samir's rota with the champion hours), the training run sheet `labs/module-06/training/run-sheet.csv` ([lab README](../../labs/module-06/README.md)); [`usage/hr-roster.csv`](../../labs/common/harbor-and-pine/usage/hr-roster.csv).
- The workflow redesign (06.1) and the session plan (06.2).
- Template: [champions playbook](../../templates/champions-playbook.md).

### Steps

1. Write the three jobs and the three "never" lines for Harbor & Pine's champions.
2. Choose the champions with the four criteria; say why each, and who is next.
3. Put their time in the rota and price it.
4. Read entries I-01 to I-08 of the issues log as of 28 February: for each open issue write the decision you would take at the huddle on Sunday 28 February, with owner and date, and the three lines to the team.
5. Write the office-hours format and what is recorded.
6. Write the back-up for each of Olga's roles and the end-of-launch decision for gate 1.

### Time

60 minutes: 15 for jobs and choice, 10 for time and cost, 25 for the huddle on the log, 10 for back-ups and the end.

### Done when

- [ ] The playbook says what champions do, what they never do, and who they report issues to.
- [ ] Each champion's time is in the rota, priced, and covered.
- [ ] Every open issue as of 28 February has a decision, an owner and a date, and the team message is written.
- [ ] Office hours record topics, not names.
- [ ] Olga's roles each have a back-up; the end of the launch structure is dated.

<details><summary>Reference answer</summary>

**Champions playbook v1.0 — AI drafts pilot — Harbor & Pine — 31 January 2027** (owner: pilot lead; approved: Samir Haddad)

*Purpose:* help on real work; issues with examples; carry decisions back. *Never:* report individuals' use; change prompts or settings; decide claims, refunds or flags as champions. Olga and Samir are Deskly admins from before the pilot; agreed that settings and prompt changes go only through the pilot lead and change control.

*Champions:* Olga (Russian, also English), Lina (Arabic), Shani (Hebrew). Next round: Tigist (Hebrew), Yana (Russian). *Time:* 2 hours a week each in the rota from week 2 (8 Feb) to 1 April; 48 hours ≈ ₪6,240, running cost of the pilot, told to Ronit on 1 February. *Huddle:* Sundays 12:30, 20 minutes; Samir every second week. *Office hours:* Tuesdays 13:00–13:45, live tickets, topics recorded, names not. *Back-ups:* Russian checks and champion — Yana; flag clearing — Samir; test-set labelling — Lina for Arabic, Yana for Russian. *End:* decided at gate 1 (rotate, shrink or end).

**Huddle, Sunday 28 February — decisions on open issues**

| Issue | Decision | Owner | By |
|---|---|---|---|
| I-05 WhatsApp drafts too long | Build the WhatsApp test set first (100 messages from 1–14 Feb, Olga and Lina label 50 each), then release the WhatsApp style through change control; until then **switch WhatsApp drafts off** so the WhatsApp pod is not fighting a bad draft on every ticket | Pilot lead; Samir switches off | Test set 7 Mar; release 11 Mar |
| I-06 HP-1… numbers not found | StoreHub mapping already in test; keep | Avi | 2 Mar |
| I-07 Old quick replies with the date line | Delete all migrated quick replies today; two approved ones (greeting, "we are checking with logistics") | Avi, Samir | 1 Mar |

*Three lines to the team (28 February, in four languages):* "1. WhatsApp drafts are off until the short WhatsApp style is tested (about 11 March) — you told us they were slower than typing, and you were right. 2. The old WhatsApp quick replies are gone tomorrow: one of them still promised the date from the order. 3. Web-store numbers (HP-1…) will be found by the panel from Tuesday."

**What the log shows when you read it as a whole:** four of the ten issues are about WhatsApp, and two of them (I-05, I-07) were still open when Samir set up the WhatsApp pod on 22 February. The decision the huddle should have taken on 21 February, when I-05 was first discussed, is the one in the table above: switch WhatsApp drafts off until they are fixed, and tell the pod so. In the log you are reading, that never happened: the huddle left the drafts on "until the style is fixed", the WhatsApp test set slipped (I-10, 22 March: 52 of 100 labelled), and the quick replies were still there in March. Lesson 06.4 shows what that did to the three people working WhatsApp.

</details>

## References

- IBM, [Lead AI Transformation certificate](https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution), course 5 (resistance as information; reinforcement); IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting), course 3 (reinforcement after launch as part of readiness). Named, not re-taught.
- Template: [champions playbook](../../templates/champions-playbook.md).
- Earlier: [06.2 · Training that transfers](lesson-02.md), [05.7 · Before launch: change control](../module-05/lesson-07.md). Next: [06.4 · The honest adoption dashboard](lesson-04.md).
