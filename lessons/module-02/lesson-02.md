---
id: "02.2"
module: 2
minutes: 18
practice_minutes: 120
prerequisites: ["02.1"]
objectives:
  - "Run a 30-minute discovery interview that gets a walk-through of real recent work, the workarounds and how every number is measured."
  - "Apply the same-word test to the words that will become KPIs or decisions, and record the competing meanings."
  - "Make it safe to talk and keep it safe: an attribution rule you can keep, no names asked for, notes marked seen, said or hearsay."
  - "Score your own interview transcript against a checklist with the coach prompt and name what you missed."
volatility: concept
sources:
  - title: "Global Anticorruption Blog — Two Legal Changes Which Would Bolster Israel's Protection of Whistleblowers (on the 1997 Protection of Workers law)"
    url: https://globalanticorruptionblog.com/2020/07/13/two-legal-changes-which-would-bolster-israels-protection-of-whistleblowers/
  - title: "NIST AI Risk Management Framework 1.0 — Core (MAP 1.6, GOVERN 5.1)"
    url: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
last_verified: "2026-11-02"
---

# 02.2 · The discovery interview

People will tell you what they wish AI would do, what the official process says and what the KPI report shows, unless you ask differently. In this lesson you learn to ask for the last real piece of work instead of the usual one, to ask how every number was measured, to test the words everyone assumes they share, and to make it safe for people to tell you about the workaround that breaks the rules. You practise on three Harbor & Pine stakeholders — the support manager, the senior agent and the logistics manager — and get feedback from the coach prompt. At the end you have three sets of interview notes, each fact marked by how you know it, and a list of what you still have to find out.

## The situation

Week 2, Tuesday 10 to Thursday 12 November 2026. Your stakeholder map (02.1) put three people first: Samir Haddad, who runs the 14-person support team; Olga Petrenko, the senior agent who trains everyone; and Tamar Shalev, who keeps the container tracking sheet. Michal has sent the invitations. Everyone on the support floor has heard that the CEO promised the board a bot and 40% lower support cost, and that you are "the AI person".

That rumour is the context of every answer you will get. A guarded manager gives you the KPI report. A worried agent gives you "we cope". A logistics manager with a container in customs gives you twenty minutes and exactly what you ask for.

IBM's consulting certificate names the same-word test: ask each role what a comfortable shared word excludes. Here you run it, along with the rest of a discovery interview, with three people who each hold part of the answer.

## What to do

### Step 1 — Prepare one page per person (10 minutes each)

Use the [interview guide](../../templates/interview-guide.md). From the stakeholder map copy the person's need, risk and what they hold, then write:

- **At most three things to find out.** For Samir: what drives the volume; how the first-response KPI is measured; what "resolved" means. For Olga: how a reply is really written on a normal day; what tools she uses. For Tamar: where container ETA updates go after they reach her; where the website's date comes from.
- **The attribution rule** you will say at the start and can keep. "Nothing you tell me goes into a document with your name on it. If I use it, it's 'the support team said', and you see it first."
- **The data you can show.** People open up when they see you did the homework: the KPI report's footnote, the ticket counts per month (272 in May, 570 in October).

### Step 2 — Open in a way that makes it safe to answer

The first two minutes decide how much you hear. Say who you are, what you are doing and what you are not doing, give the attribution rule, and say they can skip any question. Then ask an easy, concrete question about their work — not about AI.

> "I'm trying to understand how the work really happens here, including the shortcuts and the
> annoying parts. I'm not assessing anyone. Nothing you tell me gets your name on it; you'll see
> what I write first. You can skip anything. Can you describe the team?"

What makes people *more* guarded: talking about headcount, "efficiency", benchmarks or the chatbot; asking for names; jargon; promises you obviously cannot keep ("nobody will lose their job").

### Step 3 — Ask about the last real case, not the usual one

"How do you handle where-is-my-order questions?" gets the handbook. "Walk me through last Tuesday morning, from when you opened the queue" gets the work. Even better: "Can you show me the last ten?" — you see the real items, and the person describes what they do instead of what they should do.

Six question types to use and one to avoid, and what each gets you:

| Type | Example | Gets you |
|---|---|---|
| Open | "What is the most annoying part of your day?" | Where the pain is, in their words |
| Workflow | "Walk me through the last one, step by step. Who else touches it?" | The real process, the waits, the hand-offs |
| Show me | "Can I see your screen while you do the next one?" | Workarounds nobody describes |
| Numbers | "How many a day? Where does that number come from?" | A volume and its source |
| Same-word | "When the report says 'resolved', what has happened?" | Competing definitions |
| Channel | "How do customers actually reach you? Which way, how many a day?" | Work that isn't in the system you were given |
| Leading (avoid) | "So a bot would take most of the load off you, right?" | Your own opinion, and less trust |

The channel question deserves its own line. You were given the helpdesk and the phone log; the work may also live somewhere no export covers. Ask every frontline person how customers really reach them, and how many messages they handle a day — then compare with the system's count.

### Step 4 — Ask how every number was measured

Every number you hear in an interview is a claim (01.5) until you know its definition and source. Ask three things: *what is counted, over which period, and who produces it*. "First response is two hours" becomes, once you ask: business hours only, Sunday to Thursday 08:00–17:00, email only, tickets that arrive on business days, an average — exactly footnote 1 of the KPI report. The same question to Olga ("how long does a customer really wait?") gives a different answer, and in 02.4 you measure both.

### Step 5 — Run the same-word test

Some words feel shared and are not. The test: for each word that will end up in a KPI, a target or a decision, ask each role what has happened when that word is true, and what it does **not** include. Record all the readings and agree which one the work will use.

At Harbor & Pine the words to test are:

| Word | Where it appears | Readings to look for |
|---|---|---|
| resolved | KPI report: "Resolution rate 100%" | Agent: the reply was sent. Customer: the sofa arrived. Report: status set. |
| first response | KPI report, handbook §3 | Business hours, email only vs. what the customer experiences on a clock |
| delivery date | Website, order confirmation, macro | The checkout promise vs. the container's latest ETA vs. the booked slot |
| on time | Company values: "on time" on every van | Before the promise? Before the original ETA? |
| reviewed | Handbook §8: "reviewed by QA within 48 hours" | Who reviews, against what, and whether the step exists |

Ask it plainly: "When a ticket is 'resolved' in Deskly, what has happened? Does it mean the customer's problem is solved?" Then stop talking.

### Step 6 — Find the workarounds without hunting people

Workarounds are the most valuable thing discovery finds: they show where the official process fails and what people have already invented to fix it. They are also where people break rules — pasting customer emails into a free AI tool, keeping customer lists in a private sheet. How you ask decides whether you hear about them, and whether you can use what you hear.

- **Ask about the work, then the speed.** "You said writing is quick for you. How do you write a careful Russian reply so fast?" not "Do you use ChatGPT?"
- **Never ask for names.** If someone says "others do it too", ask "roughly how widespread?" once; if they won't say, accept it and ask the team together later, under the amnesty of the interim AI rule (01.6). Pressing for names in a one-to-one ends honesty in the whole team.
- **Record the practice, not the person.** In your notes: "At least one senior agent drafts Russian replies in a free chatbot, pasting full customer emails; saves ~10 minutes a reply." Not her name.
- **Say what you will do with it.** "This is a reason for an approved tool, not a disciplinary matter."

Two limits. First, you may hear about something that could be an offence (fraud, a safety breach, a deliberate data leak). Do not promise to keep that between you; say you may have to pass it on, and route it to counsel or the sponsor. Israel's Protection of Workers (Exposure of Offences and of Harm to Integrity or to Proper Administration) Law, 1997 (חוק הגנה על עובדים (חשיפת עבירות ופגיעה בטוהר המידות או במינהל התקין), התשנ"ז-1997) forbids employers from retaliating against employees who expose wrongdoing; whether a given disclosure is covered is counsel's question, not yours. Second, your notes are themselves sensitive: no customer names, phone numbers or order details in them, and no colleague names next to a workaround.

### Step 7 — Close, and write the notes within 24 hours

Three closing questions, every time: "If you could change one thing that has nothing to do with AI, what would it be?", "What should I have asked and didn't?", "Who else should I talk to?" Then read back the three things you will use and repeat the attribution rule.

Within 24 hours, write the notes in the interview guide's table and mark each fact:

- **seen** — you watched it or saw the record (Olga's queue: seven of the first ten were "where is my order");
- **said** — the person told you (Samir: "about 15% hang up");
- **hearsay** — the person told you what someone else does or says.

Next to each, the file or person that would verify it. Only "seen" and checked facts can be called verified in 02.6.

### Step 8 — Practise with the personas and the coach

Each persona is a roleplay prompt you paste into a new LLM chat; the model plays that person (how: [persona format](../../labs/common/persona-format.md)). Then paste your transcript into a new chat with the [coach prompt](../../labs/common/coach-prompt.md) and the checklist at the bottom of the persona file. Run the hardest one twice, a day apart.

[Simulation: Discovery interview](../../simulations/discovery-interview/index.html?preset=harbor)

The simulation gives you twelve questions across five Harbor & Pine stakeholders and asks you to name the real problem at the end. It is a fast way to feel how question order and trust change what people tell you; the roleplays are where you practise the actual words.

## Watch out

- **Pitching AI.** The moment you explain what AI could do, people tell you what you want to hear. Ask about the work; you will get to AI in module 3.
- **Asking about the usual case.** "Normally we…" is the handbook. Ask for the last one, the last ten, last Tuesday.
- **Accepting a number without its definition.** Every number gets "what is counted, over which period, who produces it".
- **Leading questions.** "So the macro saves time, right?" Recovery: notice it, then ask the open version: "What happens when you send the macro?"
- **Pressing for names.** You get one name and lose the team. Ask for "how widespread", then ask the team together.
- **Talking more than they do.** If your transcript lines are longer than theirs, you are presenting, not interviewing.
- **Interviewing only managers.** Managers know the numbers and the official process; the frontline knows the work and the channels nobody reports.
- **Notes from memory a week later.** Write them within 24 hours, with seen/said/hearsay, or you will quote your own guesses as findings.

## Your turn

### Inputs

- Personas, in the module download: [Samir Haddad](../../labs/common/harbor-and-pine/personas/samir-cs-manager.md), [Olga Petrenko](../../labs/common/harbor-and-pine/personas/olga-support-agent.md), [Tamar Shalev](../../labs/common/harbor-and-pine/personas/tamar-logistics.md). Don't read the roleplay prompt before you interview: it says what each person hides.
- No roleplay? Read the pre-run transcripts instead: [Samir](../../labs/common/harbor-and-pine/personas/transcripts/samir-cs-manager.md), [Olga](../../labs/common/harbor-and-pine/personas/transcripts/olga-support-agent.md), [Tamar](../../labs/common/harbor-and-pine/personas/transcripts/tamar-logistics.md).
- [Coach prompt](../../labs/common/coach-prompt.md) and [persona format](../../labs/common/persona-format.md).
- Template: [interview guide](../../templates/interview-guide.md). Your stakeholder map from 02.1.
- Data to show: [`company/kpi-report-2026-q3.md`](../../labs/common/harbor-and-pine/company/kpi-report-2026-q3.md), [`company/customer-service-handbook.md`](../../labs/common/harbor-and-pine/company/customer-service-handbook.md).

### Steps

1. Write a one-page interview guide for each of the three, with three things to find out and your attribution rule.
2. Interview each persona for 20–30 minutes in a new chat. Type `[end interview]` to finish.
3. For each, paste the transcript into the coach with the persona's "After the interview" checklist. Write down the coach's "one thing to do differently".
4. Re-run the interview you did worst, with that one thing in mind.
5. Write the notes for all three in the interview guide's table: every fact marked seen / said / hearsay, with the file or person that would verify it.
6. List what you still don't know and where you will look (02.3–02.5).

**No-roleplay path.** Read the three transcripts as if you were sitting in. For each, list what the interviewer found out, the questions that worked, the moments they made a mistake, and at least two things they never asked.

### Time

120 minutes (three interviews and coaching, one re-run, notes). No-roleplay path: about 60 minutes.

### Done when

- [ ] Three guides, each with at most three things to find out and an attribution rule you can keep.
- [ ] In each interview you asked for a walk-through of real recent work and how at least one number is measured.
- [ ] You ran the same-word test on "resolved" and on at least one other word.
- [ ] You asked every frontline person how customers actually reach them.
- [ ] You asked for no colleague's name, and your notes contain no customer details.
- [ ] Every fact in your notes is marked seen / said / hearsay with a way to verify it.

<details><summary>Reference answer</summary>

**What a strong set of notes contains** (said facts become verified only when checked in 02.3–02.5):

| # | Fact | From | Status | Verify with |
|---|---|---|---|---|
| 1 | Volume doubled since spring: ~270 tickets in May, ~570 in October | Samir | said | `tickets.csv` per month: 272 → 570 |
| 2 | Most of the morning queue is "where is my order"; the order-status macro repeats the promised date, often already passed | Samir, Olga | said; seen in Olga's queue (7 of 10) | Tag `macro_order_status`; `emails.csv` replies |
| 3 | Best agents skip the macro, email logistics@ or check Tamar's sheet, then reply | Olga | seen | Logistics mailbox export |
| 4 | KPI "2 hours" = business hours, email only, business days, average; web form and weekends excluded; Samir set it in 2024 | Samir | said; matches footnote 1 | Re-measure in 02.4 |
| 5 | "Resolved" = reply sent; a customer who writes again opens a new ticket | Samir, Olga | said | Follow-ups by customer + order (02.5) |
| 6 | Claims are decided by Rina with Samir; "there is no QA" since 2023 | Olga | said (hearsay about QA) | Org chart; claims log (02.3) |
| 7 | At least one senior agent drafts Russian and Arabic replies in a free chatbot with the full customer email; ~15–20 min → ~5 min | senior agent (unattributed) | said | Census (01.6): proxy log, chatbot traces in `emails.csv` |
| 8 | ETA updates reach logistics and stop in the tracking sheet; the website date never changes | Tamar | said; sheet seen | `shipments.csv` vs `orders.csv` (02.4) |
| 9 | Since June, 40 of the last 41 Vietnam/China containers were late, 5–23 days | Tamar | said | `shipments.csv` |
| 10 | 187 emails from support to logistics, Jul–Sep | Tamar | said | Mailbox export |
| 11 | Customers reach support mostly through the four shared WhatsApp phones; Samir had the agents tally one week in October | Samir or Olga, if asked the channel question | said | `support/whatsapp-week-tally.csv` (02.4) |

**Same-word test, recorded.** "Resolved": agent = reply sent; report = status; customer = problem solved. The work will use "no new contact from the same customer about the same order within 14 days". "First response": KPI = working hours, email, business days, mean; the work will report wall-clock median for all channels alongside it.

**Reading the pre-run transcripts.** *Samir:* the interviewer made it safe (attribution rule first, "judge me by what I do"), asked for a normal day and got the WISMO story, and asked exactly how the 2 hours is measured. Missed: never asked what "resolved" means (asked only "what happens after the agent replies"), never asked how customers reach the team besides email and phone, and never asked who QA is. *Olga:* "work as normal and talk me through it" was the best move in all three transcripts; the safety statement before the hard question unlocked the chatbot use. Mistake: "I just need to know how many, roughly. It stays between us" — pressing for numbers after she refused names made her colder; the interviewer recovered by accepting her suggestion to ask the team together. Missed: whether others use other tools, and whether she ever asked IT for an approved one. *Tamar:* "where does that update go after it reaches you?" was the key question and got "into my sheet; that's it". Missed: where the website's promised date comes from and who owns it, and what she would build with a week of IT help — the plain-automation candidate.

**Still to find out.** The real first-response time on all channels (02.4); the share of WISMO across helpdesk, phone and WhatsApp (02.4); how many "resolved" tickets come back (02.5); who owns the promised-date setting (Noa, per the settings file — interview in week 3); whether claim outcomes are recorded (02.5).

</details>

## References

- Global Anticorruption Blog, [Two legal changes which would bolster Israel's protection of whistleblowers](https://globalanticorruptionblog.com/2020/07/13/two-legal-changes-which-would-bolster-israels-protection-of-whistleblowers/) — the 1997 Protection of Workers law forbids retaliation against whistleblowing employees (secondary source; route specific cases to counsel).
- NIST, [AI RMF 1.0 Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) — MAP 1.6 (requirements elicited from relevant AI actors), GOVERN 5.1 (feedback from those external to the team).
- Template: [interview guide](../../templates/interview-guide.md). Field kit: [persona format](../../labs/common/persona-format.md), [coach prompt](../../labs/common/coach-prompt.md).
- Previous: [02.1 · Stakeholder map before the first interview](lesson-01.md). Next: [02.3 · Process walk and task inventory](lesson-03.md). Related: [01.6 · The shadow-AI census](../module-01/lesson-06.md) (amnesty and interim rule).
