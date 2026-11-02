---
id: "08.2"
module: 8
minutes: 20
practice_minutes: 180
prerequisites: ["08.1", "02.2", "02.4", "02.7"]
objectives:
  - "Interview the head of customer service, a frontline agent, the BI owner and an affected customer, and get the facts each of them would not volunteer."
  - "Measure a repeat-contact rate and a like-for-like handling time from a helpdesk export where neither was ever reported."
  - "Join chatbot sessions to helpdesk contacts to test a vendor's containment figure against what customers did next."
  - "Write a findings memo whose every finding is labelled measured, reported or inferred and names its consequence."
volatility: implementation
sources:
  - title: "Kol Zchut, ביטול עסקת מכר מרחוק (cancelling a distance sale): 14 days, fee 5% or ₪100, refund within 14 days, 4 months for 65+ etc. (page updated 6 September 2026)"
    url: https://www.kolzchut.org.il/he/ביטול_עסקת_מכר_מרחוק
  - title: "Consumer Protection Law, 5741-1981, full text (Hebrew Wikisource): sections 2, 14C, 14C1, 14E"
    url: https://he.wikisource.org/wiki/חוק_הגנת_הצרכן
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): the same-word test, verified vs reported findings"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
last_verified: "2026-11-02"
---

# 08.2 · Discovery

Two weeks before Black Friday you have a CEO's slide, a vendor's dashboard and a floor that is drowning, and they do not agree. In this lesson you interview four people at Northwind (the head of customer service, a senior agent, the head of BI and a customer who tried to return a tent) and you measure the three numbers nobody has: repeat contacts, handling time like for like, and what customers did after the chatbot "resolved" them. At the end you have a findings memo, each finding labelled and traced to its evidence, ready for the 26 November readout.

## The situation

Monday 9 to Thursday 19 November 2026. Your charter is signed (08.1). Orly booked Meseret Tadesse (Head of Customer Service) and Alexei Morozov (Head of IT and BI) for Monday and two hours on the WhatsApp desk with Nadia Khoury for Tuesday. Hila Rosen (counsel) agreed that you may speak to Valentina Orlova, a customer with an open complaint to the Consumer Protection Authority, on 18 November, on the condition that the complaint itself is not discussed.

This is the discovery method of module 2, run on a bigger, angrier organization: the [stakeholder map](../module-02/lesson-01.md) first, then [interviews](../module-02/lesson-02.md) that ask for the work and test the same words, then [baselines from exports](../module-02/lesson-04.md), then a [findings memo](../module-02/lesson-07.md). IBM's consulting certificate calls the distinction you keep throughout *verified versus reported*; here every finding carries one of three labels: **measured** (computed from Northwind's data), **reported** (someone told you) or **inferred** (your reading of both).

## What to do

### Step 1 — Map who knows what before you ask

Four people, four kinds of knowledge. Put them on the [stakeholder map](../../templates/stakeholder-map.md) with what each needs from the engagement and what each risks by talking to you:

| Person | Knows | Needs | Risks by talking |
|---|---|---|---|
| Meseret (head of CS) | How the KPIs are built; what the floor feels | No more cuts; someone to see the strain | Being blamed for the numbers |
| Nadia (senior agent) | What agents really say about returns | One policy she can say out loud | Being named for "giving away money" |
| Alexei (IT and BI) | Why every number moved | KPI definitions with owners | Nothing, if asked the right question |
| Valentina (customer, 68) | What the journey is like from outside | Her money and an apology | Being "handled" again |

### Step 2 — Interview for the work, and test the same words

Use the [interview guide](../../templates/interview-guide.md). Three Northwind words mean different things to different people, and each hides a finding:

- **"AHT."** To the CEO's slide, handling time per contact. To BI since 14 June, the agent's handling time without the after-contact work (return forms, notes). Ask Meseret: "How is AHT measured now, compared with May?"
- **"Contained" / "resolved".** To Verbalo, a chat that ended without a hand-over, including customers who closed the window. To a customer, a problem that went away. Ask: "When the report says a chat was contained, what does that mean to you? How would you know?"
- **"Returns policy".** There are four. Ask Nadia not what the policy is, but: "A customer opened a tent, didn't use it, it's day ten and they want their money back. What do you actually tell them?"

Protect the people who answer. Meseret will only tell you about the AHT change if you have promised not to attribute it to her; Nadia will only show you the agents' unofficial exceptions document if nobody's name goes in your memo. Write the promise down and keep it: the memo says "the definition changed on 14 June at the customer-service department's request", not who asked.

Run each interview as a roleplay ([Meseret](../../labs/module-08/personas/meseret-cs-head.md), [Nadia](../../labs/module-08/personas/nadia-senior-agent.md), [Alexei](../../labs/module-08/personas/alexei-it-bi.md), [Valentina](../../labs/module-08/personas/valentina-customer.md)) and score it with the [coach prompt](../../labs/common/coach-prompt.md), or read the [transcripts](../../labs/module-08/personas/transcripts/) and mark what each interviewer found and missed.

**The customer is different.** Valentina is not a data source; she is the person the system affected. Let her tell the sequence in order, write down each contact and each answer, do not explain the policy to her, and do not promise an outcome you cannot authorise. Her four contacts (chat in Russian answered in Hebrew; phone, refused at day 25 although she is in the 65+ club; a credit note minus 10% and ₪39 she never asked for; two unanswered WhatsApps) are the whole system in one journey.

### Step 3 — Measure the repeat-contact rate nobody reports

Both KPI reports say "repeat-contact rate: not tracked", so there is no baseline unless you build one. Write the definition card first (the method in [02.4](../module-02/lesson-04.md)):

> **Repeat contact:** an agent contact from a customer who had an agent contact about the same order in the previous 7 days, on any channel. Order numbers normalised first (agents type `NW-4…`, `nw4…`, `4…`, `#NW-…`); if either contact has no order number, count it as the same order. Source: `support/contacts.csv`.

In a spreadsheet: sort by `customer_id`, then `created_at`; add a normalised order column (`=IFERROR("NW-"&TEXTJOIN("",TRUE,IFERROR(MID(E2,SEQUENCE(LEN(E2)),1)*1,"")),"")` or a find-and-replace pass); in each row compare with the row above (same customer, within 7 days, same or blank order). The result on Northwind's extract:

| Period | Repeat-contact rate | Label |
|---|---|---|
| 1 May – 14 June (before the bot and the cuts) | **17.2%** (379 contacts) | measured: the only baseline there is |
| Q3 (July–September) | **32.1%** | measured |
| By month May → Oct | 14.2 / 28.2 / 30.4 / 33.2 / 32.7 / 34.4% | measured |
| From 15 June, by language field | Hebrew 29.0%, English 32.5%, Arabic 38.6%, Russian 40.8% | measured |

Say what this is not: it does not prove the bot caused it. The bot launch, the definition change, the cuts and the summer peak all fall in June and July. It does prove that the sentence "no drop in service" is not true.

### Step 4 — Rebuild handling time like for like

`contacts.csv` has both `handle_time_sec` and `after_contact_work_sec`. The Q2 report's AHT used both; the Q3 report's uses the first only. Compute both for both periods:

| | Before 15 June | From 15 June |
|---|---|---|
| As Q3 defines it (handling only) | 4.6 min | 5.6 min |
| As Q2 defines it (handling + after-contact work) | **7.9 min** | **8.9 min** |

The "30% reduction" (8.0 in Q2 against 5.6 in Q3) compares the right column of one row with the left of the other. Like for like, handling time went *up* by about 14%: the bot took the easy order-status chats, and what reaches agents is harder.

### Step 5 — Test "containment" against what customers did next

The vendor counts a chat as resolved when it ends without a hand-over. Check it: for every "resolved" session with a `customer_id` (only logged-in customers have one, about 60%), look in `contacts.csv` for an agent contact from the same customer in the next 7 days. In a spreadsheet: `COUNTIFS(contacts!D:D, customer_id, contacts!B:B, ">"&started_at, contacts!B:B, "<="&started_at+7)`.

Result: **64.1% of 170 logged-in "resolved" sessions** were followed by an agent contact within a week; 78% for returns-policy questions, 48% for order status. Two cautions to write next to it: logged-out customers may behave differently, and some later contacts are about something else. Even halved, it is not "containment".

While you are in `bot-sessions.csv`, read `last_bot_reply` for the 151 sessions with `bot_intent = returns_policy`. Of the 69 that gave a policy answer (not a hand-over or "I didn't understand"), 26 promise "30 days, full cash refund", 24 say "store credit only, minus 10%", 19 give the terms of sale. And 121 of 439 sessions are in a language the bot does not speak.

### Step 6 — Measure the returns process the SOP describes

`orders/returns.csv` against `policies/warehouse-returns-sop.md`:

- **Inspection "within 2 business days"**: median 3 business days before 1 August, **8** after; none within 2 after August. Orly told you (reported) that two of four returns clerks moved to the warehouse floor in July.
- **Refund "within 14 days"**: card refunds a median **17 days** after the request, 66% over 14 days, and every single one paid on a Thursday.
- **Fees**: 252 of 380 non-defect refunds (66.3%) carry a 10% handling fee; the terms of sale say 5% or ₪100, whichever is lower. 62 of 137 refunds coded as defects still had a deduction. 199 of 517 refunds were store credit.

These are facts about Northwind's practice set against Northwind's own terms of sale. The terms of sale restate the Consumer Protection Law's rules on cancelling a distance sale (sections 14C and 14E: 14 days from receipt, refund within 14 days of the notice, fee at most 5% or ₪100). Whether the practice breaches the law is counsel's question, not yours; your memo says "conflicts with section 9 of the terms of sale" and routes the rest to Hila.

**Track B (Python).** `python discovery.py` in `labs/module-08/` (module download) prints every number in steps 3–6 from the data room. Python is worth it here because the repeat-contact rule and the bot-to-helpdesk join are fiddly in a spreadsheet (sorting, normalising order numbers, a 7-day window per customer), and you will re-run them every month after the engagement: BI will need exactly this script to own the new KPI.

### Step 7 — Write the findings memo

Follow [02.7](../module-02/lesson-07.md) and the [findings memo](../../templates/findings-memo.md) template: the answer first, then each finding with its evidence, label and consequence, then what you did not find. Three Northwind-specific rules:

1. **Every number names its sample.** "32.1% of agent contacts in the 1% extract", not "a third of customers".
2. **Reported findings stay reported** until the data confirms them. The exceptions document is reported (Nadia showed it; you did not get a copy).
3. **Nobody is named for what they told you.** Findings describe systems, not people.

Before you send it, have each person who appears in a finding read their part (Meseret the floor, Alexei the definitions). People who see themselves described fairly in private defend the memo in public.

## Watch out

- **Measuring before defining.** "Repeat contact" with no window, no order rule and no channel rule gives any number you like. Write the card first.
- **Treating the sample as noise.** 2,075 rows are a lot of evidence for a rate and very little for a rare event. Report the counts with every rate (13 Amharic contacts do not support a percentage).
- **Taking the bot's word for its own success.** Containment is Verbalo's number about Verbalo's product. Join it to Northwind's own records before anyone repeats it.
- **The customer as a case study.** Valentina's story will be the most powerful page of your memo. Use it only with her consent and Orly's, without her name, and never to argue her complaint.
- **Saying "illegal".** You found practice that conflicts with Northwind's own terms. The legal reading belongs to counsel; writing it yourself makes the memo easier to dismiss.
- **Burning the agent.** If the exceptions document becomes "Nadia's document" in a steering meeting, the floor stops talking to you for the rest of the engagement.

## Your turn

### Inputs

- Data room (module download): `support/contacts.csv`, `support/bot-sessions.csv`, `support/bot-transcripts-sample.md`, `orders/returns.csv`, `support/macros.csv`, the four files in `policies/`, both KPI reports, `people/cs-headcount-2026.csv`, `legal/regulator-and-claims-log.csv`.
- Personas: [Meseret](../../labs/module-08/personas/meseret-cs-head.md), [Nadia](../../labs/module-08/personas/nadia-senior-agent.md), [Alexei](../../labs/module-08/personas/alexei-it-bi.md), [Valentina](../../labs/module-08/personas/valentina-customer.md), or their [transcripts](../../labs/module-08/personas/transcripts/); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [stakeholder map](../../templates/stakeholder-map.md), [interview guide](../../templates/interview-guide.md), [data profile](../../templates/data-profile.md), [findings memo](../../templates/findings-memo.md).
- Track B: `labs/module-08/discovery.py`.

### Steps

1. Fill the stakeholder map for the four people.
2. Interview at least two of them by roleplay (one must be Meseret or Nadia) and read the other transcripts; for each, write the hidden fact you got and one you did not.
3. Write the definition card for repeat contacts and compute the rate before 15 June and in Q3.
4. Compute AHT both ways for both periods.
5. Join "resolved" bot sessions to agent contacts within 7 days; classify the bot's returns answers.
6. Measure inspection time, refund time and fees against the SOP and the terms of sale.
7. Write the findings memo (answer first; 6–9 findings; labels; consequences; what you did not find) and list who reads which part before it goes out.

**Track B (Python).** Run `python discovery.py`, check its numbers against two you computed by hand, then use it for the memo's figures.

### Time

180 minutes: 60 for interviews, 70 for the measurements (40 with Track B), 50 for the memo.

### Done when

- [ ] The repeat-contact rate has a written definition, a pre-June baseline and a Q3 value, with counts.
- [ ] AHT is shown both ways for both periods, and the memo says which comparison the board saw.
- [ ] Containment is tested against agent contacts within 7 days, with the limits of the test stated.
- [ ] At least one hidden fact each from Meseret and Nadia is in the memo, labelled reported, unattributed.
- [ ] Every finding has a label (measured, reported, inferred), its evidence and a consequence.
- [ ] No finding says "illegal"; the conflict with the terms of sale is routed to counsel.

<details><summary>Reference answer</summary>

The full memo is `labs/module-08/expert/02-findings-memo.md` in the module download. The opening and three findings:

**Answer first.** The chatbot is not what drives cost and pressure in customer service. Returns are. About 45% of agent contacts concern returns, refunds and fees; they repeat because Northwind gives customers four different answers and pays card refunds a median 17 days after the request. Since mid-June the team has shrunk from 42 to 30 agents while repeat contacts almost doubled; "AHT down 30%" is a change of definition.

**Finding 1 (measured).** Repeat contacts: 17.2% of agent contacts from 1 May to 14 June (n = 379 in the 1% extract), 32.1% in Q3. Definition: same customer, same order (normalised) or blank, within 7 days, any channel. Never reported before; this is the only baseline. *Consequence:* any saving claimed from the bot must be netted against extra contacts.

**Finding 2 (measured + reported).** AHT like for like rose from 7.9 to 8.9 minutes; the reported 5.6 excludes after-contact work since 14 June (Q2 vs Q3 footnotes; BI's change log, requested by the customer-service department). *Consequence:* the board slide's −30% should be withdrawn or footnoted.

**Finding 7 (measured).** Of 170 logged-in chats Verbalo counts as resolved, 64.1% were followed by an agent contact within 7 days (78% for returns-policy questions). Limits: logged-in customers only; some later contacts may be about another matter. *Consequence:* "containment" is not resolution, and each is billed at US$0.85.

**Interviews, what the transcripts got and missed:**

| Person | Found | Missed |
|---|---|---|
| Meseret | AHT definition changed at her department's request; repeats "every day"; returns answered differently | Real floor capacity: about 26 agents on a normal day, not 30 |
| Nadia | The exceptions document (14 rules); Arabic customers bounced by the bot; Thursday refunds | Two agents paste Arabic messages into a free online translator |
| Alexei | Both definition changes on 14 June; the change log | Containment never checked against the helpdesk; a repeat measure takes him a day |
| Valentina | The four contacts in order; would have accepted money minus a small fee | Where she would accept an automatic answer (tracking yes, money no) |

**Valentina's journey (with consent, unnamed in the memo):** bought a ₪1,290 tent in a chat with an agent (14 Sep), delivered 17 Sep; 11 Oct the bot answered her Russian in Hebrew, then "store credit, unopened, 14 days"; 12 Oct the phone agent refused (day 25; she is in the 65+ club, which has 30 days); credit note of ₪1,122 (minus ₪129 and ₪39) on 23 Oct; two WhatsApps unanswered; complaint to the Authority on 26 Oct. Under Northwind's own club terms she was inside the window; whether other rights apply is counsel's question.

</details>

## References

- Kol Zchut, [cancelling a distance sale](https://www.kolzchut.org.il/he/ביטול_עסקת_מכר_מרחוק) (updated 6 September 2026) and the [Consumer Protection Law, 5741-1981](https://he.wikisource.org/wiki/חוק_הגנת_הצרכן) (חוק הגנת הצרכן), sections 14C, 14C1 and 14E: what Northwind's terms of sale restate. Route any reading of Northwind's practice to counsel.
- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting): the same-word test and verified vs reported findings (named, not re-taught).
- Field kit: [02.1 · Stakeholder map](../module-02/lesson-01.md), [02.2 · The discovery interview](../module-02/lesson-02.md), [02.4 · Measuring a baseline from exports](../module-02/lesson-04.md), [02.5 · Profiling the data](../module-02/lesson-05.md), [02.7 · Writing a findings memo people believe](../module-02/lesson-07.md).
- Templates: [stakeholder map](../../templates/stakeholder-map.md), [interview guide](../../templates/interview-guide.md), [data profile](../../templates/data-profile.md), [findings memo](../../templates/findings-memo.md).
- Earlier: [08.1 · The call](lesson-01.md). Next: [08.3 · Diagnosis](lesson-03.md).
