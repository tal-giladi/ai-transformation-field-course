---
id: "08.4"
module: 8
minutes: 22
practice_minutes: 150
prerequisites: ["08.3", "03.2", "04.6", "04.8"]
objectives:
  - "Decide, step by step, which parts of customer contact a bot may answer alone, which an agent answers with a draft, and which need a person, and defend the line with Northwind's evidence."
  - "Read a chatbot's liability the way counsel will: who is speaking, about what, under which rules, and what the Air Canada case does and does not show."
  - "Turn four contradicting returns texts into one policy outline with every business choice marked for its owner and every legal point routed to counsel."
  - "Read back a vendor's claims and contract terms under the conditions they were measured, and name what to change before renewal."
volatility: implementation
sources:
  - title: "Manatt, 'AI Gone Wild: Airline Has to Honor a Refund Policy Its Chatbot Fabricated' (Moffatt v. Air Canada, 2024 BCCRT 149; member Christopher Rivers; CA$650.88 plus interest and fees), 28 February 2024"
    url: https://manatt.com/insights/newsletters/advertising-law/ai-gone-wild-airline-has-to-honor-a-refund-policy
  - title: "CTV News, 'Air Canada's chatbot gave a B.C. man the wrong information. Now, the airline has to pay for the mistake', 14 February 2024"
    url: https://www.ctvnews.ca/vancouver/article/air-canadas-chatbot-gave-a-bc-man-the-wrong-information-now-the-airline-has-to-pay-for-the-mistake/
  - title: "Consumer Protection Law, 5741-1981 (Hebrew Wikisource): section 2(a) misleading, 14C and 14C1 cancellation of distance sales, 14E refund and fee, 31A punitive damages"
    url: https://he.wikisource.org/wiki/חוק_הגנת_הצרכן
  - title: "Kol Zchut, ביטול עסקת מכר מרחוק (cancelling a distance sale), updated 6 September 2026"
    url: https://www.kolzchut.org.il/he/ביטול_עסקת_מכר_מרחוק
  - title: "Class Actions Law, 5766-2006 (Hebrew Wikisource): second schedule, item 1 (claims against a dealer under the Consumer Protection Law)"
    url: https://he.wikisource.org/wiki/חוק_תובענות_ייצוגיות
  - title: "Intercom pricing: Fin AI Agent US$0.99 per outcome; Copilot US$29 per agent a month billed annually (checked 2 November 2026)"
    url: https://www.intercom.com/pricing
  - title: "Zendesk pricing: automated resolutions US$1.50 committed / US$2.00 pay-as-you-go; Copilot add-on US$50 per agent a month billed annually (checked 2 November 2026)"
    url: https://www.zendesk.com/pricing/
  - title: "IAPP, Amendment 13 to Israel's Privacy Protection Law (in force 14 August 2025)"
    url: https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform
last_verified: "2026-11-02"
---

# 08.4 · The hard part

Every organization in this course is about one hard thing; Northwind's is that the chatbot the CEO wants is not the problem and might be the liability. A bot that answers "can I get my money back?" can only repeat the policy it is given, and Northwind has four. In this lesson you draw the line between what a bot may say alone and what an agent should say with a draft, read the liability the way counsel will, outline the one returns policy that has to come first, and read back the vendor's claims before the renewal. At the end you have the decision paper for the steering group on 3 December.

## The situation

Monday 30 November to Thursday 3 December 2026. The phase-1 readout went to the steering group on 26 November; they agreed to continue to phase 2 but asked one question in Gil's words: "Bot or not?" Your answer is due at the second exit point, Thursday 3 December.

This week you see two people. Adv. Hila Rosen, Northwind's one-person legal department, on Monday (roleplay: [Hila](../../labs/module-08/personas/hila-legal-counsel.md); [transcript](../../labs/module-08/personas/transcripts/hila-legal-counsel.md)); and Daniel Brenner, Verbalo's account executive, on Wednesday, who asked for the meeting "to talk about phase two" (roleplay: [Daniel](../../labs/module-08/personas/daniel-verbalo-ae.md); [transcript](../../labs/module-08/personas/transcripts/daniel-verbalo-ae.md)).

The field kit has every move: [agent or not, step by step](../module-03/lesson-02.md), the [regulatory map](../module-04/lesson-06.md), the [risk register](../module-04/lesson-05.md), [vendor and claim due diligence](../module-04/lesson-08.md) and [human review that actually checks](../module-05/lesson-05.md). IBM's governance course would call the result a *pass / flag / block* gate per use; here you apply it to each kind of customer question, not to "the chatbot" as a whole.

## What to do

### Step 1 — Split the contact, not the technology

"Chatbot or agent-assist" is the wrong first question. Take the contact types from your baseline and decide, for each one, who may answer and how ([03.2](../module-03/lesson-02.md)). The rule that decides it: **what happens when the answer is wrong, and who could have caught it?**

| Contact type (share of written tickets) | Answer needs | If wrong | Who answers |
|---|---|---|---|
| Where is my order (≈ 21%) | Order-system lookup | A wrong date; the customer asks again | **Bot alone**, from the order system, with hand-over |
| Product questions (≈ 9%) | Catalogue facts | A wrong spec; a return later | Bot from the product page, or agent; low risk |
| Where is my refund (≈ 12%) | OMS status and the refund run | A false promise of a date | Agent with a draft that quotes the status; better still, an SMS before they ask (08.3, B) |
| Can I return this, how much do I get back, why was I charged, it arrived broken (≈ 30%, plus defects ≈ 8%) | Order facts, the policy, the fee arithmetic, sometimes the customer's age or how they bought | A statement to a consumer about cancellation rights | **Agent with a draft**: rules decide, the model writes, a person sends |
| Complaints, legal threats, injuries (≈ 2–3%) | Judgement | Escalation missed | **A person**, the same day; the draft only flags |

The middle row is the hard part and the biggest. It is also where the bot is today: of its 69 policy answers in the extract, 50 contradict Northwind's own terms of sale.

### Step 2 — Read the liability the way counsel will

You are not giving legal advice; you are preparing the questions so counsel can. Four points, each with its source, go into the paper:

**Who is speaking.** A chatbot on northwind.co.il answering a customer's refund question is Northwind speaking. The public case everyone will cite is **Moffatt v. Air Canada** (British Columbia Civil Resolution Tribunal, 2024 BCCRT 149, February 2024). A grieving customer asked Air Canada's website chatbot about bereavement fares; it told him he could buy a full-price ticket and claim the reduction within 90 days; the airline then refused. The tribunal member found Air Canada liable for negligent misrepresentation, rejected its argument that the chatbot was responsible for its own words, and ordered it to pay the difference, CA$650.88, plus interest and fees. It is a small-claims decision in Canada and binds no Israeli court. What it shows is the question any court or regulator will ask: if your bot says it, did you say it?

**What the rules are.** Northwind's terms of sale (§9) restate the Consumer Protection Law, 5741-1981 (חוק הגנת הצרכן) on cancelling a distance sale: 14 days from receiving the goods (section 14C); the price refunded within 14 days of the notice, less a cancellation fee of at most 5% or ₪100, whichever is lower, and no fee where the cancellation is for a defect, a mismatch or late delivery, in which case the business collects the goods (section 14E); four months from the transaction for senior citizens, people with disabilities and new immigrants when the transaction included a conversation, including one by electronic communication (section 14C1). The returns page, the club terms, the warehouse SOP and two of the bot's three answers say something else.

**What a wrong statement can cost.** The same law prohibits misleading a consumer on a material matter, and lists cancellation conditions among them (section 2(a)); it allows punitive damages without proof of damage, up to ₪10,000 (more for repeated breaches), where a consumer cancelled and the price was not refunded (section 31A); and claims against a dealer under it may be brought as a class action (Class Actions Law, 5766-2006, second schedule, item 1). Northwind already has the demand letter of 22 September.

**What is open.** Ask counsel, do not assume: does a chat with the bot count as a "conversation" for the four-month right? How should "opened" and "used" be worded? What about deductions already made? Hila's answer in the transcript is the right one for a consultant to hear: "Don't build anything that assumes either answer."

Put each point in the [regulatory map](../../templates/regulatory-map.md) with its owner (counsel) and in the [risk register](../../templates/risk-register.md) with its control. The privacy angle goes there too: the bot's conversations are stored by Verbalo in Ireland for 24 months and may be used to train its models unless Northwind opts out (order form §7); since Amendment 13 the Privacy Protection Authority's sanctions are far larger, and counsel has not reviewed the contract.

### Step 3 — Outline the one policy that has to come first

A draft that repeats four policies faithfully is worse than no draft. So the paper carries the outline of returns policy v2, written for counsel to mark up, with every **business choice** marked ★ for its owner:

1. Cancel within 14 days of delivery; ★ club members 30 days (keeps the club promise; COO/CFO).
2. Money back to the original means of payment within 14 days of the notice; ★ store credit only if the customer asks (CFO: breakage).
3. Fee 5% or ₪100, whichever is lower; ★ no handling fee; ★ Northwind pays the drop-off label (CFO).
4. Faulty, not as described or late: no fee; Northwind collects.
5. Senior citizens, disability, new immigrants, purchase in a conversation with an agent: four months from the purchase; proof requested. (Bot conversations: open with counsel.)
6. Personalised items excluded unless faulty; ★ size exchanges free within 30 days.
7. Escalate the same day: the Authority, a lawyer, a claim, a card dispute, any injury.

One text replaces the page, §9, club clause 5.2, SOP step 4 and all nine macros, and the agents' unofficial exceptions document is retired publicly on the day it is published. The version counsel marked up on 17 December is the pilot's reference in 08.5 (`labs/module-08/pilot/policy-for-pilot.md`).

### Step 4 — Read back the vendor's claims, then the contract

Use the [claim read-back](../../templates/claim-read-back.md) and [04.8](../module-04/lesson-08.md): each claim, the conditions it was measured under, the fit with Northwind, the read-back.

| Claim | Conditions (from Daniel and the documents) | Fit | Read-back |
|---|---|---|---|
| 62% containment | 40 questions chosen with e-commerce; English; sandbox; 12 May; 4 about returns, none with an exception | Poor | Not evidence for production |
| 95% accuracy | Rated by the vendor's own engineer | No independent rater | Not evidence |
| "Resolution" | Ended without a hand-over, including closed windows; billed at US$0.85 | 64.1% come back within 7 days | Change the definition before renewal |
| CSAT 4.6 | Thumbs on resolved chats; people who click | 95 down, 45 up in the extract | Not a satisfaction measure |
| Arabic, Russian | "Roadmap" | 28% of chats | Q3 2027 at the earliest, in writing |

Put the price in context: per-outcome pricing is normal in this market, and the definition is everything. On 2 November 2026 Intercom listed its Fin AI agent at US$0.99 per *outcome* and its Copilot (agent-assist) at US$29 per agent a month billed annually; Zendesk listed automated resolutions at US$1.50 committed or US$2.00 pay-as-you-go, and a Copilot add-on at US$50 per agent a month billed annually. Read each vendor's definition of what it bills before comparing prices; this course is tool-agnostic and these are reference points, not recommendations.

Then the contract actions before the notice date (1 April 2027): counsel reviews §5–§7; Northwind opts out of training in writing; the knowledge content is cut to delivery and order-status pages; the resolution definition changes to "no agent contact from the same customer within 72 hours". Daniel's transcript misses two things a better interviewer would have found: what content the bot answers returns questions from (the returns page, the club terms and the terms of sale, all loaded at go-live and never reviewed) and what Verbalo would accept to change the definition.

### Step 5 — Write the decision paper

Answer first, one decision, options side by side, the recommendation, what a "no" means. The [decision-ready case](../../templates/decision-ready-case.md) shape from [03.9](../module-03/lesson-09.md) works; add the liability read and the policy outline as sections, and the read-back as a table. The recommendation the evidence supports: **agent-assist after the policy, the bot narrowed to order status, and against extending the bot to returns in the first half of 2027.** Say plainly that this is a compliance decision with a cost (08.3), not an AI saving.

Rehearse the hardest paragraph with Hila first. Counsel who sees her own points stated accurately, as hers, will stand behind the paper in the room.

## Watch out

- **"Bot or not" for everything.** The bot is fine for order status. Drawing the line per contact type is what makes the answer credible to the CEO.
- **Using Air Canada as precedent.** It is a Canadian small-claims decision. Use it for the question it asks, not as Israeli law.
- **Writing the law yourself.** State what Northwind's terms and the cited sections say, attribute every reading to counsel, and list what is open. "Unlawful" is counsel's word.
- **Fixing the bot's prompt instead of the policy.** A better prompt picks one of four policies more consistently. It is still one of four.
- **Comparing prices without definitions.** US$0.85 per "resolution" and US$0.99 per "outcome" are different products until you read what each counts.
- **Letting the vendor set the agenda.** Daniel wants phase two and a 24-month renewal before March. Your read-back is what Northwind negotiates with; you do not negotiate.

## Your turn

### Inputs

- Data room (module download): `policies/` (all four), `support/macros.csv`, `support/bot-sessions.csv`, `support/bot-transcripts-sample.md`, `vendor/` (order form, demo deck, demo questions, invoices), `legal/` (both logs).
- Your findings memo (08.2) and one-page case (08.3).
- Personas: [Hila Rosen](../../labs/module-08/personas/hila-legal-counsel.md) and [Daniel Brenner](../../labs/module-08/personas/daniel-verbalo-ae.md), or their [transcripts](../../labs/module-08/personas/transcripts/); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [regulatory map](../../templates/regulatory-map.md), [risk register](../../templates/risk-register.md), [claim read-back](../../templates/claim-read-back.md), [vendor AI questionnaire](../../templates/vendor-ai-questionnaire.md), [decision-ready case](../../templates/decision-ready-case.md).

### Steps

1. Split Northwind's contact into five to seven types; for each, write what the answer needs, what a wrong answer costs, and who answers (bot alone, agent with draft, person).
2. Interview Hila (or read the transcript). Write the liability read: who speaks, the rules, what a wrong statement can cost, what is open, each attributed.
3. Outline returns policy v2 in at most ten lines, marking every business choice ★ with its owner.
4. Interview Daniel (or read the transcript). Write the claim read-back and the contract actions before 1 April.
5. Write the decision paper: decision asked, options table, recommendation, liability, policy outline, read-back, risks, what a "no" means.

### Time

150 minutes: 25 for the split, 40 for Hila and the liability read, 25 for the policy outline, 30 for Daniel and the read-back, 30 for the paper.

### Done when

- [ ] Every contact type has an owner (bot, agent with draft, person) with a reason tied to the cost of a wrong answer.
- [ ] The liability read cites its sources, attributes every legal reading to counsel and lists the open questions.
- [ ] The policy outline replaces all four texts and the macros, and every business choice is marked with an owner.
- [ ] Every vendor claim has its measurement conditions and a read-back; the contract actions have dates.
- [ ] The paper recommends against something, with the evidence, and says what a "no" means.

<details><summary>Reference answer</summary>

The full paper is `labs/module-08/expert/04-decision-paper.md` in the module download. Its spine:

**Decision asked (3 December):** approve (1) one returns policy drafted with counsel by 17 December and published after the COO, CFO and counsel sign; (2) the chatbot limited to order status and hand-over for returns, refunds and money from 10 December; (3) an offline agent-assist test on the 2,000 tickets, reported 7 January. Decline extending the chatbot to returns, refunds and WhatsApp in Q1 2027. *What a no means:* the bot keeps stating returns rules Northwind's terms contradict, about 3,400 returns-policy chats a month.

**Options:**

| | Extend the bot | Agent-assist | Nothing new |
|---|---|---|---|
| Who decides refund and fee | The bot, from whichever text it retrieves | Rules on order data; the agent confirms | The agent, from four policies |
| Measured today | 64.1% of "resolved" chats come back in 7 days; 50 of 69 policy answers contradict the terms | Tested in 08.5 | 55.6% of returns replies consistent; 32.7% give the customer less than the terms |
| Depends on the policy being fixed | Completely | For its value | — |

**Liability read (counsel's points, attributed):** the bot is Northwind speaking; Moffatt v. Air Canada (2024 BCCRT 149) is the question, not the precedent; Northwind's §9 restates sections 14C, 14C1, 14E of the Consumer Protection Law; section 2(a), section 31A and the Class Actions Law are why wrong statements are expensive; open: bot chats and the four-month right, "used" items, past deductions; privacy: Verbalo §7 training and EU storage, contract never reviewed.

**Policy v2 outline:** the seven lines in Step 3, with ★ on club 30 days, store credit as the customer's option, no handling fee, Northwind-paid label, free size exchanges.

**Read-back and contract actions:** as in the Step 4 table; before 1 April: counsel review of §5–§7, written training opt-out, knowledge content cut to delivery and order status, "resolution = no agent contact within 72 hours" (Daniel would offer it for a 24-month term; recommend 12).

**What the transcripts missed:** Hila's open question on bot chats and the four-month right was never asked (she raises it only if asked about older customers or chat purchases); Daniel was never asked what the bot was taught about returns, or what Verbalo would accept to change the definition.

</details>

## References

- Moffatt v. Air Canada, 2024 BCCRT 149: as reported by [Manatt](https://manatt.com/insights/newsletters/advertising-law/ai-gone-wild-airline-has-to-honor-a-refund-policy) (28 February 2024) and [CTV News](https://www.ctvnews.ca/vancouver/article/air-canadas-chatbot-gave-a-bc-man-the-wrong-information-now-the-airline-has-to-pay-for-the-mistake/) (14 February 2024). The tribunal's own decision page could not be opened by the course's tools; check it before quoting.
- [Consumer Protection Law, 5741-1981](https://he.wikisource.org/wiki/חוק_הגנת_הצרכן) (sections 2, 14C, 14C1, 14E, 31A); Kol Zchut, [cancelling a distance sale](https://www.kolzchut.org.il/he/ביטול_עסקת_מכר_מרחוק); [Class Actions Law, 5766-2006](https://he.wikisource.org/wiki/חוק_תובענות_ייצוגיות), second schedule. Not legal advice: route every reading to counsel.
- IAPP, [Amendment 13](https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform) (in force 14 August 2025).
- Market reference prices, checked 2 November 2026: [Intercom](https://www.intercom.com/pricing), [Zendesk](https://www.zendesk.com/pricing/).
- Field kit: [03.2 · Agent or not](../module-03/lesson-02.md), [04.5 · Risk register from zero](../module-04/lesson-05.md), [04.6 · Which law applies to you](../module-04/lesson-06.md), [04.8 · Vendor and claim due diligence](../module-04/lesson-08.md), [05.5 · Human-in-the-loop design](../module-05/lesson-05.md).
- Templates: [regulatory map](../../templates/regulatory-map.md), [risk register](../../templates/risk-register.md), [claim read-back](../../templates/claim-read-back.md), [vendor AI questionnaire](../../templates/vendor-ai-questionnaire.md), [decision-ready case](../../templates/decision-ready-case.md).
- Earlier: [08.3 · Diagnosis](lesson-03.md). Next: [08.5 · Build: agent-assist on 2,000 tickets](lesson-05.md).
