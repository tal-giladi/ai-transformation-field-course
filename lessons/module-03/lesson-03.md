---
id: "03.3"
module: 3
minutes: 18
practice_minutes: 75
prerequisites: ["03.2", "02.5"]
objectives:
  - "Screen every candidate on seven questions, one sentence each, naming the person who answered or the file that shows it."
  - "Apply the data gate as pass or fail: reachable, trusted, lawful for the purpose, and the outcome label recorded."
  - "Give each candidate a verdict of go, go with a condition, or stop, naming the question it turns on and the owner of the next step."
  - "Decide which classes of candidate always get full scrutiny, in writing, before you screen."
volatility: implementation
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera) — course 2, Identify and Prioritize AI Opportunities (qualifying candidates)"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "IAPP — Israel marks a new era in privacy law: Amendment 13 ushers in sweeping reform (13 Aug 2025)"
    url: https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform
  - title: "Pearl Cohen — Israel: New Draft Guidelines on the Application of Privacy Law to AI (4 May 2025)"
    url: https://www.pearlcohen.com/israel-new-draft-guidelines-on-the-application-of-privacy-law-to-ai/
  - title: "IAPP — The new Israeli data security regulations: A tutorial"
    url: https://iapp.org/news/a/the-new-israeli-data-security-regulations-a-tutorial
  - title: "Moffatt v. Air Canada, 2024 BCCRT 149 — summary by Evans Hudson LLP"
    url: https://ehlaw.ca/?p=22062
last_verified: "2026-11-02"
---

# 03.3 · The fast screen

Scoring a candidate that should never have reached the scoring table wastes a workshop and lends it credibility. The fast screen is the step in between: seven questions per candidate, one sentence each, a data gate that is pass or fail, and one of three verdicts. In this lesson you screen Harbor & Pine's candidates in about an hour, and you leave with a short list that is worth scoring, a list of conditions with owners, and a clear "stop" for the ideas that fail a basic test, including one the CFO proposed.

## The situation

Monday 23 November 2026. You have the opportunity map ([03.1](lesson-01.md)) and frames for the two biggest candidates ([03.2](lesson-02.md)). The scoring workshop is on Thursday. If all fifteen candidates go into it, the room will spend an hour on smart reorder and the copy tool, and the CEO's chatbot will be scored next to things that have not been checked at all.

IBM's consulting certificate calls this qualifying candidates: seven separate dimensions, a data-readiness gate with the label question, and proceed / proceed with a condition / stop. Here you run it on Harbor & Pine's files, with the Israeli legal questions it raises.

## What to do

### Step 1 — Before you screen, write what always gets full scrutiny

Agree this with Michal in writing before you look at any candidate, so it cannot bend to fit a favourite. At Harbor & Pine:

> Any candidate whose output reaches a customer without a person checking it, that decides about a
> person (a customer's claim, an applicant), that cannot be undone, or that uses personal data
> without a clear right to use it for this purpose, gets the full screen and a legal or privacy
> question routed to counsel or the DPO before it can pass. Michal, 23 Nov 2026.

### Step 2 — Ask the seven questions, one sentence each

Keep them separate. A blank is not a "medium": it is a person you have not asked yet.

| # | Question | What a good answer contains |
|---|---|---|
| 1 | **Value:** what changes, how much, for whom, against which goal? | A number from the opportunity map with its status, tied to the sponsor's objective |
| 2 | **Workflow fit:** can you walk it on paper, and is it actionable? | Who receives the output, which decision changes, what they do differently that day |
| 3 | **Data (the gate):** see Step 3 | Pass or fail, with the reason |
| 4 | **Feasibility:** can it be built and paid for? | Builder, connections, a cost band and the approval line it falls under |
| 5 | **Risk:** what does a wrong output touch? | Who is affected, how widely, whether it can be undone, which law or policy applies |
| 6 | **Sponsorship:** who owns it after you leave? | A named person who will run it and answer for it |
| 7 | **Measurement:** how will you know it worked? | An indicator someone already reviews, a baseline, and its source |

The actionability part of question 2 catches candidates that are right but useless. A forecast that arrives after the containers are booked changes nothing. A delay notice sent the day the ETA moves changes what the customer does that day: they stop writing to support.

### Step 3 — Run the data gate as pass or fail

The data gate has four parts, and a candidate passes only if all four do:

1. **Reachable:** can you get the inputs, at the frequency the use needs?
2. **Trusted:** are they current and correct enough? (Your data profile from [02.5](../module-02/lesson-05.md) answers this.)
3. **Lawful for the purpose:** may you use this data for this use? In Israel the Privacy Protection Law, 5741-1981 (חוק הגנת הפרטיות, התשמ"א-1981) governs it. Its Amendment 13 has been in force since 14 August 2025 and gives the Privacy Protection Authority administrative fines and stronger enforcement powers (IAPP, 13 August 2025). The Authority's draft guidance on AI (April 2025) expects a legal basis for processing, telling people when they are talking to a bot, privacy by design and impact assessments for AI (Pearl Cohen summary, 4 May 2025). You do not decide these questions: you write them down and route them to counsel or the DPO, and the verdict waits for the answer where it matters.
4. **The label question:** if the use learns from or is tested against past outcomes, were those outcomes recorded, consistently? If not, the answer is "not yet", and the next step is a recording project with an owner and a start date.

Worked example, damage-claim decisions (Ronit's idea):

- Reachable: yes, `claims/damage-claims-log.csv` and the photos in the tickets.
- Trusted: one person keeps the log by hand.
- Lawful: the log holds customer names and phone numbers on a shared drive; a model that decides a customer's claim is a decision about a person (route to the DPO).
- **Label: fails.** The decision column "החלטה" is blank for 48 of 149 claims (32.2%), and still 31.4% for claims opened by 30 September, so it is not just recent claims waiting. You cannot train or even test a decision model on outcomes nobody recorded. And the handbook's "every claim is reviewed by QA within 48 hours" (`company/customer-service-handbook.md` §8) describes a step that does not exist: there is no QA role, and the median decision takes 8 days.

Verdict: **stop**, with the next step written: "Rina records every outcome, with date and reason, from 1 December; Samir checks completeness monthly; re-screen in March 2027 with three months of complete labels."

### Step 4 — Give one of three verdicts, and say what it turns on

- **Go:** all seven answered, gate passed.
- **Go with a condition:** a named condition, an owner and a date. The candidate moves to scoring, but it cannot start until the condition is met.
- **Stop:** name the question it fails on and what would reopen it. "Stop" is not "never".

Worked example, the CEO's chatbot, screened on the vendor's own documents and your data:

| # | Answer |
|---|---|
| 1 Value | Vendor claims 70% resolved and −45% cost; the footnote says the 70% was measured on US and Canadian English-language retail with live order tracking, and −45% is from a survey of 22 customers (`vendors/chatnest-sales-deck.md`). At Harbor & Pine 38% of contacts are WISMO. Status: claimed |
| 2 Fit | Walkable, but for WISMO the bot would answer "the date shown in your order confirmation" (slide 4, footnote 3): the wrong date. Actionable only after the date fix |
| 3 Data gate | **Fails "trusted":** the demo was built on the 2023 catalogue copy from the shared drive (Oslo sofa quoted at ₪4,290, current ₪4,990; Bergen table discontinued since August 2025). Order tracking is "quoted separately". Lawful: customers must be told they are talking to a bot (PPA draft); data hosted in the United States (slide 7): route to the DPO |
| 4 Feasibility | ₪85,000 implementation + US$1,450 a month + US$0.45 per resolved conversation above 1,000; ERP integration not priced; at the finance planning rate of ₪3.70 per US$ (finance summary, October 2026) the platform fee alone is about ₪64,400 a year. Over three years well above ₪150,000: board approval |
| 5 Risk | Answers customers directly, without a person, about prices, dates and claims. A company answers for what its chatbot tells customers: in *Moffatt v. Air Canada* (2024 BCCRT 149) a Canadian tribunal held the airline liable for its chatbot's wrong statement about a fare policy and awarded damages. Wrong prices from the stale catalogue would reach customers |
| 6 Sponsor | Yoav (sponsor), but Samir would run it, and Samir has not been asked |
| 7 Measurement | "Resolved" is the vendor's definition (conversation ended without a transfer), not "the customer's problem was solved"; your follow-up baseline (about 23%) shows why that matters |

Verdict: **stop for now**, turning on question 3 (trusted data) and question 2 (it would answer WISMO with the wrong date). Reopen when the date fix is live, WhatsApp is routed into the helpdesk, and the vendor runs a proof of concept on Harbor & Pine's own current catalogue and order data (module 4, lesson 04.8). Owner of the next step: you, with Yoav.

### Step 5 — Write the screen as one table and send it before the workshop

One line per candidate: verdict, the question it turns on, the condition or next step, the owner. Send it to Michal and Ronit two days before the workshop, so nobody hears a "stop" for the first time in a room full of colleagues. The proposer of every stopped idea gets a short note from you first, in person if possible: what it failed on, what would reopen it.

## Watch out

- **Averaging the seven questions.** A candidate that is brilliant on value and fails the data gate is a "stop", not a "medium". The gate is not a trade-off.
- **Screening on the vendor's description.** Read the footnotes. "70%" measured on someone else's customers, language and integration is a claim about them.
- **Deciding the law yourself.** "It's probably fine under the privacy law" is not a screen answer. Write the question, route it to counsel or the DPO, and record that the verdict depends on the answer.
- **"Stop" with no way back.** A stop without a reopening condition reads as a personal rejection, and the proposer will route around you. Give the condition and the owner.
- **Ignoring tools already running.** PeopleWise Candidate Match is already ranking applicants. It is not a candidate to screen but a live system to review; put it straight into the AI inventory and risk work (module 4) and say so in the screen.
- **Letting the screen become the scoring.** The screen decides what is worth scoring. Do not rank the "go" candidates here; that needs the locked criteria of 03.4.

## Your turn

### Inputs

- Your opportunity map ([03.1](lesson-01.md)) and frames ([03.2](lesson-02.md)); your data profile ([02.5](../module-02/lesson-05.md)) and readiness assessment ([02.6](../module-02/lesson-06.md)).
- Data room (module download, `labs/common/harbor-and-pine/`): `vendors/chatnest-sales-deck.md`, `claims/damage-claims-log.csv`, `company/customer-service-handbook.md`, `catalog/products.csv`, `catalog/products-2023-shared-drive-copy.csv`, `it/smartstock-reorder-config.md`, `it/peoplewise-release-notes-2026-03.md`, `company/finance-summary.md`.
- Template: [use-case scorecard](../../templates/use-case-scorecard.md), part A (the screen); spreadsheet version `labs/module-03/use-case-scorecard.csv` in the module download.

### Steps

1. Write the scrutiny rule (Step 1) and get your sponsor's agreement (in the exercise, write the email).
2. Screen every candidate on your map: seven sentences, each naming a file or a person.
3. Run the data gate for each candidate that uses data; record each part as pass or fail.
4. Give each a verdict, the question it turns on, the condition or next step, the owner and a date.
5. List the legal and privacy questions you are routing, and to whom.
6. Write the short note you will send to one proposer whose idea stopped.

### Time

75 minutes: 10 for the rule, 50 for the screen, 15 for the routing list and the note.

### Done when

- [ ] The scrutiny rule is written and dated before the first verdict.
- [ ] Every candidate has seven one-sentence answers or a named person still to ask.
- [ ] The data gate is pass or fail on four parts; at least one candidate fails the label question with a number.
- [ ] Every "go with a condition" has the condition, an owner and a date; every "stop" says what would reopen it.
- [ ] Legal and privacy questions are routed to a named person, not answered by you.
- [ ] Tools already running are sent to the inventory and risk work, not screened as new ideas.

<details><summary>Reference answer</summary>

**Harbor & Pine fast screen, 24 November 2026** (sent to Michal and Ronit; proposers told first)

| # | Candidate | Verdict | Turns on | Condition or next step | Owner, date |
|---|---|---|---|---|---|
| 1 | Promised-date fix + proactive delay emails (no AI) | Go with a condition | 4 Feasibility, 6 Sponsorship | Noa and Yoav agree to change the StoreHub lead-time table and the notice texts; Tamar agrees the sheet format | You with Noa, by 3 Dec |
| 2 | WhatsApp routed into the helpdesk | Go with a condition | 3 Lawful, 4 Feasibility | Business account approved by Meta; the four numbers moved off the phones; DPO view on the chat history on the phones | Avi and Samir, by 14 Jan |
| 3 | Reply drafts for written contact, human sends | Go with a condition | 3 Lawful, 5 Risk | #2 done first; an approved tool with a data boundary replaces free ChatGPT (module 4); no send permission | Samir, start Feb 2027 |
| 4 | ChatNest chatbot | Stop for now | 3 Trusted, 2 Fit | Reopen after #1 and #2, with a proof of concept on current catalogue and order data | You with Yoav, re-screen Oct 2027 |
| 5 | B2B quote drafts | Go with a condition | 3 Trusted, 5 Risk | Prices and agreed discounts read from Priority, never written by the model; price agreements moved into Priority | Yaniv, by Apr 2027 |
| 6 | Assembly answers from manuals | Go with a condition | 3 Trusted, 4 Feasibility | Manuals cleaned (many are scans with poor translations); after #3 has a review routine | Olga and Samir, re-screen Jun 2027 |
| 7 | Damage-claim decisions | Stop | 3 Label (48 of 149 decisions blank) | Record every outcome from 1 Dec; re-screen Mar 2027 | Rina and Samir |
| 8 | Marketing copy tool | Not a project | — | Tool approval and data boundary (module 4); fact check against `catalog/products.csv` | Noa, module 4 |
| 9 | LinguaFlow translation extension | Not a project | 3 Lawful | Free plan keeps texts up to 18 months and uses them for training; replace or license (module 4) | Avi, module 4 |
| 10 | PeopleWise Candidate Match | Live system, not a candidate | 5 Risk | Switch off pending review; inventory and risk (module 4); route the ranking of applicants to counsel | Dana, now |
| 11 | SmartStock "AI" reorder | Stop | 1 Value, not AI | Min/max rules; the case study was a grocery distributor; re-open only with a forecast use case that names a decision | Purchasing |
| 12 | Demand forecasting | Stop | 2 Fit | Not yet a candidate: no decision named | Purchasing, if they bring one |
| 13 | Duplicate merge and category suggestion | Go (inside #3) | — | Part of #3's triage | Samir |
| 14 | Claim-outcome recording | Go (no AI) | — | The foundation for #7 | Rina, from 1 Dec |
| 15 | Contact-driver view | Go later | 3 Reachable | After #2 makes WhatsApp data exist | Samir, Q2 2027 |

**Routed questions:** to counsel or the DPO (Harbor & Pine has no DPO yet: Michal decides who) — (a) customer chat history on four shared phones and its retention; (b) disclosure that a customer is talking to a bot, if #4 is ever reopened, and US hosting; (c) PeopleWise ranking of applicants; (d) claims log with names and phones on the shared drive; (e) whether past customer messages may be used to build and test the drafting tool (to counsel through Ronit). To IT: LinguaFlow free-plan terms.

**Note to Ronit (stopped idea):**

> Ronit, about the damage-claim decisions: I screened it today and it stops on one thing. The
> decision is missing for 48 of the 149 claims since May, so there is nothing to teach or test a
> model on, and a wrong rejection lands on a customer. If Rina records every outcome from 1 December,
> we will have three clean months by March and I will screen it again then. In the meantime the
> drafts pilot will quote the claims policy correctly, which is where most of the write-off
> discussion starts.

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting), course 2, module "Qualifying candidate use cases" (seven dimensions, data-readiness gate, label question; named, not re-taught).
- IAPP, [Amendment 13 to the Privacy Protection Law](https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform) (in force 14 Aug 2025).
- Pearl Cohen, [PPA draft guidelines on privacy law and AI](https://www.pearlcohen.com/israel-new-draft-guidelines-on-the-application-of-privacy-law-to-ai/) (draft; check its status before relying on it).
- IAPP, [Israeli data security regulations tutorial](https://iapp.org/news/a/the-new-israeli-data-security-regulations-a-tutorial) (Privacy Protection (Data Security) Regulations, 5777-2017, in force 8 May 2018; relevant to the claims log and the WhatsApp phones).
- *Moffatt v. Air Canada*, 2024 BCCRT 149, [summary](https://ehlaw.ca/?p=22062).
- The course's [laws and guidance page](../../references/laws-and-guidance.md). This lesson is not legal advice: route legal questions to counsel or the DPO.
- Template: [use-case scorecard](../../templates/use-case-scorecard.md).
- Next: [03.4 · Scoring with evidence](lesson-04.md). Vendor proof of concept: lesson 04.8.
