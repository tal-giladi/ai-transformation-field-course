---
id: "07.7"
module: 7
minutes: 18
practice_minutes: 90
prerequisites: ["03.8", "04.8", "02.7"]
objectives:
  - "Read a roadmap as if it has already failed: list its promises, write the failure stories, and trace each to a concrete cause in the evidence."
  - "Sort every finding into a wrong assumption (false today: correct it) or a fragile dependency (true today, may change: fallback, trigger, re-sequence or remove)."
  - "Load-test each control the plan relies on, and name what a small trial could settle before money is committed."
  - "Write a findings log (what breaks, for whom, when; type; disposition; owner) and deliver it without making the plan's sponsor defend it."
volatility: concept
sources:
  - title: "Gary Klein, 'Performing a Project Premortem', Harvard Business Review, September 2007"
    url: https://hbr.org/2007/09/performing-a-project-premortem
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera) — course 4, Design AI Transformation Roadmaps, module 4 'Pressure-testing the roadmap' (pre-failure reading; wrong vs fragile; reviewer independence; dispositions)"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
last_verified: "2026-11-02"
---

# 07.7 · Pressure-test a roadmap before it hardens

A roadmap hardens the moment someone signs a contract against it; after that, every flaw becomes a sunk cost someone must defend. In this lesson you pressure-test the AI roadmap a consultancy wrote for Harbor & Pine's CEO, while it is still a proposal: you imagine it has already failed, trace each failure to a cause you can show in the data room, sort wrong assumptions from fragile dependencies, test the controls it relies on, and write a findings log with a disposition and an owner for every line. At the end you have a log your sponsor can take into the scoring workshop, and a method you will turn on your own roadmap next.

## The situation

This lesson steps back in time, to before the steering pack and the pilot. It is Tuesday 24 November 2026, your fourth week. Yesterday Yoav forwarded the roadmap NextWave Digital Advisory wrote for him in October (`documents/roadmap-previous-consultant.md`, in the data room): "Board liked the direction. Can we just adopt this and sign ChatNest before the discount ends on the 30th?" Its next steps say: sign ChatNest before 30 November, announce the programme in December, start on 4 January. The scoring workshop is on Thursday 26 November ([03.5](../module-03/lesson-05.md)); your findings memo is due on 1 December ([02.7](../module-02/lesson-07.md)). Michal asked you for "something written about that roadmap that I can use on Thursday without starting a war".

It sits in module 7 because the method needs everything from modules 1 to 6, and because you will use it again in this module's future: in June, roadmap v2.0 for the second half of 2027 is written by you, so it needs someone else to pressure-test it ([07.9](lesson-09.md)).

IBM's roadmap course calls this the pre-failure reading: approval is not a test, a clean review is worth only what the reviewer tried to find, wrong assumptions are corrected and fragile dependencies get a fallback or a trigger, and the reviewer should not be the author. Gary Klein's premortem (HBR, 2007) is the same move as a team exercise: assume the project has failed and ask why, which lets people voice doubts they would otherwise keep. IBM gives no log template, no worked report and nothing on the politics of challenging a plan the CEO already showed the board. This lesson does.

## What to do

### Step 1 — List what the plan promises

Before judging anything, write down every promise the plan makes, in its own words, with its date. A pressure test tests promises, not prose.

| # | The plan promises | By |
|---|---|---|
| P1 | Chatbot on website, WhatsApp and email resolves 70% of conversations | Live 28 Feb 2027 |
| P2 | Customer service cost down 40% (₪1.36 million a year) | From month 4 |
| P3 | Deskly Autopilot sends AI replies for the remaining tickets | Live 15 Feb 2027 |
| P4 | AI product descriptions for all SKUs, ₪300,000 a year from traffic | 31 Jan 2027 |
| P5 | AI demand forecasting replaces SmartStock, ₪500,000 a year less stock | 31 Mar 2027 |
| P6 | PeopleWise AI recruiting switched on, ₪80,000 a year, cost 0 | 1 Jan 2027 |
| P7 | All 120 employees trained, one day each | 31 Mar 2027 |
| P8 | Total ₪520,000 plus licences; payback under four months; all live by March for the April board | Q1 2027 |

### Step 2 — Assume it failed, then write the stories

Set the date: "It is Thursday 29 April 2027. At the April board, Yoav had to explain why the AI programme failed." Then write, alone first (ten minutes, so nobody anchors on the loudest voice), the most likely stories of how it failed. Concrete stories, not risk categories: "the bot told customers their sofa would arrive on the date we had promised, which had passed" is a story; "data quality" is a category.

### Step 3 — Trace each story to a cause you can show

A failure story becomes a finding only when it points at evidence. For each, name the file, the number, the person:

- **The volume is wrong.** "About 9,000 contacts a year": the helpdesk alone had 2,529 tickets in six months, the phone system 3,194 calls, and the agents' WhatsApp tally 630 conversations in one week. With WhatsApp, written and phone contact is above 40,000 a year, so "₪380 per contact" is several times too high and every saving computed from it is fiction.
- **The 70% is someone else's.** The vendor's footnote and its account executive ([04.8](../module-04/lesson-08.md)): measured on US English retail with order tracking integrated. Here there is no integration, and 38% of contacts are "where is my order?" caused by a promised date that is wrong: the bot answers them from the order confirmation, with the wrong date.
- **The catalogue.** The demo was built on a 2023 copy of the catalogue (wrong prices, discontinued items); "the vendor will clean the catalogue" gives the job to someone who does not own the data.
- **The quarter.** Every initiative starts in Q1: the end of the November–January peak, and the weakest cash quarter of the year (finance summary). The support team is at 92% utilisation in those months.
- **The money.** ₪520,000 is above the ₪150,000 board line several times over, with no staging and no gates; the payback "under four months" rests on the ₪1.36 million.
- **The free item.** PeopleWise's candidate ranking is "already available" because it was switched on by default in a March release, and HR did not know. Ranking job applicants is the use module 4 sent to counsel; it is not a free benefit.
- **The rules engine.** SmartStock is a fixed min/max rules engine marketed as AI; "replacing it with AI forecasting" in two months, on 112 containers in six months, with no baseline, is a project nobody has scoped.
- **The people.** "Staff will adopt the tools once they see the benefit", in a team that heard "40% lower support cost" at the town hall and already uses free chatbots with customer data because nothing approved exists.

### Step 4 — Sort wrong from fragile

The disposition depends on the kind of finding:

- **Wrong:** false today. Correct it, or remove what rests on it. (The 9,000; the 70% for this business; ₪380; payback; PeopleWise as free; "the vendor cleans the catalogue"; "staff will adopt"; SmartStock as AI.)
- **Fragile:** true today, may change. Give it a fallback, a trigger to watch, a different sequence, or remove the dependency. (The ChatNest price and discount; the vendor's own model and terms, which it can change; the container delays, which drive WISMO and could end; one-person IT, which is enough until Avi is ill in January.)

The difference matters because the cures are opposite. You cannot "monitor" a wrong number into being right, and you cannot "correct" a dependency that is true today; you can only stop betting everything on it.

### Step 5 — Load-test the controls the plan relies on

Every plan says somewhere that someone will check something. Test whether they can, with arithmetic:

- **"Monthly steering meeting chaired by the CEO; the vendor provides performance reports."** Seven initiatives, one hour a month: about eight minutes each. The vendor grades its own work. No threshold, no stop rule, no independent sample.
- **"Communicate early; training" against staff resistance.** 120 people × one day = about 960 working hours in Q1, 112 of them for the support team in the last month of their peak.
- **IT capacity.** Chatbot, Autopilot, forecasting and PeopleWise all need Avi in January and February. Four integrations, one person, plus an outside service provider on a support contract.
- **Review capacity.** The roadmap you will write in January allows two evaluations a quarter ([03.8](../module-03/lesson-08.md)). This one starts seven things in one quarter with no evaluation at all.

### Step 6 — Find what a small trial can settle

Some findings can be argued forever and settled in two weeks. Name the cheapest test that would settle each one before money moves:

- The 70%: a proof of concept on Harbor & Pine's own contacts, with resolution defined in advance and checked against re-contacts ([04.8](../module-04/lesson-08.md)), after the date fix, not before.
- WISMO: a two-week dry run of a daily job that compares promised dates with container ETAs (no AI, about ₪35,000; the date fix).
- Volume: count it this week from the three exports and the WhatsApp tally.
- PeopleWise: switch it off until counsel answers; nothing to trial.

### Step 7 — Write the log, and deliver it without a war

Each finding is one row: what breaks, for whom, and when; the evidence; wrong or fragile; the load test or trial; the disposition (correct, re-sequence, add a fallback, de-scope, defer, remove); the owner and date ([pressure-test log](../../templates/pressure-test-log.md)). Sort it by consequence, not by page order.

Then the politics. Yoav paid for this roadmap and showed its direction to the board; NextWave is not in the room to defend it. So:

- **Give it to the sponsor first.** Michal decides how it is used on Thursday; you do not send it to Yoav or circulate it.
- **Attack the plan's assumptions, never its authors or its sponsor.** "The 70% was measured with order tracking integrated" is a finding; "NextWave did a poor job" is a fight.
- **Keep what is right.** The vision (fewer waiting customers), an AUP and governance document, and AI drafting of catalogue copy survive the test in some form. A log that finds nothing worth keeping reads as a rival's pitch.
- **Turn the next step into a decision with a date.** Here: do not sign ChatNest by 30 November; re-screen it after the date fix with a proof of concept on own data.
- **Ask for the same test on your own plan.** You are not independent of the roadmap you will write in January. Ask Ronit and Tamar to pressure-test it before it goes to the steering committee.

## Watch out

- **Reviewing instead of failing it.** "Looks ambitious but achievable" is what a review without a pre-failure reading says. Start from "it failed" and work back.
- **Categories instead of causes.** "Data quality risk" fixes nothing; "the demo quotes 2023 prices from a shared-drive copy" can be fixed by Friday.
- **Monitoring a wrong number.** If it is false today, correct it. Watch only what is true today and might change.
- **Testing the plan you wrote yourself.** You will find what you already believe. Get someone who did not write it.
- **A log that kills everything.** Keep what survives and say so; otherwise the log is a sales pitch for your own plan.
- **Going over the sponsor.** The CEO commissioned it. The log goes to Michal, who decides how it is used.

## Your turn

### Inputs

- The roadmap: `documents/roadmap-previous-consultant.md` in the data room (module download, `labs/common/harbor-and-pine/`).
- Evidence: `support/tickets.csv`, `support/phone-log.csv`, `support/whatsapp-week-tally.csv`, `orders/orders.csv`, `vendors/chatnest-sales-deck.md`, `catalog/products-2023-shared-drive-copy.csv`, `it/peoplewise-release-notes-2026-03.md`, `it/smartstock-reorder-config.md`, `company/finance-summary.md`, `people/timesheets.csv`; your findings from modules 1–4.
- Template: [pressure-test log](../../templates/pressure-test-log.md); spreadsheet version `labs/module-07/pressure-test-log.csv` (module download, one example row).

### Steps

1. List every promise in the roadmap with its date.
2. Set the failure date and write at least six failure stories, alone, in ten minutes.
3. Trace each story to evidence: file, number, person.
4. Sort each finding wrong or fragile.
5. Load-test at least three controls the plan relies on, with arithmetic.
6. Name the smallest trial that would settle each finding that is arguable.
7. Fill the log: what breaks, for whom, when; evidence; type; test; disposition; owner; date. Sort by consequence.
8. Write the three-paragraph cover note to Michal: what to decide by 30 November, what survives, and who should pressure-test your own roadmap in January.

### Time

90 minutes: 10 for the promises, 10 for the stories, 25 for the evidence, 10 for wrong vs fragile, 10 for the load tests and trials, 15 for the log and cover note, 10 to sort and read it as Yoav would.

### Done when

- [ ] Every finding points at a file, a number or a person, not a category.
- [ ] Every finding is typed wrong or fragile, and its disposition matches the type.
- [ ] At least three controls are load-tested with arithmetic.
- [ ] Each arguable finding has a named trial that would settle it.
- [ ] The log keeps what survives, and the cover note goes to the sponsor with one decision and a date.

<details><summary>Reference answer</summary>

**Pressure-test log — "Harbor & Pine AI Transformation Roadmap 2027" (NextWave, 15 October 2026) — 24 November 2026** (reviewer: Head of AI; for Michal Peretz). Sorted by consequence. The last column was added in July 2027, for this course, to show what happened.

| # | What breaks, for whom, when | Evidence | Type | Test or trial | Disposition | Owner | What actually happened |
|---|---|---|---|---|---|---|---|
| 1 | The chatbot answers "where is my order?" with the passed promised date; customers write again; from go-live (Feb 2027) | 38% of tickets are WISMO; Vietnam/China orders arrive a median 11 days after the promise; the deck's footnote: tracking needs integration | wrong (70% for this business) | Date-fix dry run (2 weeks); PoC on own data after it | Re-sequence: date fix first; chatbot to a re-screen with a PoC | Michal; you | Date fix live 14 Jan; WISMO share 44% → about 22% by March; chatbot parked to Oct 2027 |
| 2 | The board sees a ₪1.36M saving no budget line contains; Ronit cannot sign; at the first quarterly review (Apr 2027) | 2,529 tickets / 6 months, 3,194 calls, 630 WhatsApp conversations in one week: over 40,000 contacts a year, not 9,000 | wrong | Count from the exports (done) | Correct; recompute every benefit | You; Ronit | The measured case: ₪113,000 a year expected cash (Jan); re-forecast ₪65,000 after gate 1 |
| 3 | WhatsApp is listed as a chatbot channel; it lives on four shared phones with no system; the bot has nothing to connect to (Jan 2027) | WhatsApp tally; finding 16 | wrong (the channel does not exist as a system) | — | Add a prerequisite: WhatsApp into the helpdesk | Avi, Samir | Routed into Deskly 1 Feb; WhatsApp drafts failed gate 1 and went into a fix |
| 4 | Every Q1 start lands in the last peak month and the weakest cash quarter; the support team is at 92% utilisation (Jan 2027) | Timesheets; finance summary | wrong (capacity assumed) | — | Re-sequence: nothing new in the support team before February; no go-live Nov–Jan | You | Pilot went live 1 Feb; training 7–11 Feb |
| 5 | ₪520,000 committed in one quarter with no gates; the board approves above ₪150,000; nothing can stop a failing item | Finance summary thresholds | wrong (no staging) | — | Correct: stage money against yes/no gates | Ronit | ₪48,000 now, ₪72,000 at gate 1; gate 1 released only ₪30,000 |
| 6 | Deskly Autopilot sends AI replies with no person; trains on customer content unless opted out; any admin can switch it on (Feb 2027) | Deskly AI add-on terms §1.2, §3.2 | wrong (as a quick win) | — | Remove; keep Autopilot off and audited | Avi | Kept off; audited monthly |
| 7 | The demo's prices and products come from a 2023 copy; "the vendor cleans the catalogue" | Catalogue copy vs current: 29 discontinued, prices 15% lower | wrong | — | Correct: catalogue owned by Noa, one current source | Noa | The same pattern (a stale shared-drive file in an AI source) caused the 15 March incident |
| 8 | PeopleWise ranks applicants by default; counted as a free ₪80,000 benefit; HR did not know (already live) | Release notes, March 2026; SaaS list says "No" | wrong | — | Remove from the roadmap; switch off pending counsel | Dana | Off since 12 Nov 2026; counsel's view still open in March |
| 9 | Forecasting "replaces SmartStock" in two months: SmartStock is rules; 112 containers in six months; no baseline (Mar 2027) | SmartStock configuration; shipments | wrong (scoped as a swap) | Baseline of stock-outs first | Defer; re-screen with a baseline | Purchasing | Not started |
| 10 | Training 120 people one day each: about 960 hours in Q1, 112 of them in Customer Service at peak | Headcount; timesheets | wrong (cost ignored) | — | De-scope: a 60-minute role-based session for the people whose work changes | Dana, Samir | 14 people × 3 hours in February |
| 11 | "Staff will adopt once they see the benefit": a team that heard "40%" and uses free chatbots with customer data | Proxy log, interviews | wrong | — | Correct: AUP, an approved tool, a no-cuts message, champions | Michal | Adoption strong on email; quiet non-adoption in the WhatsApp pod |
| 12 | Governance: the vendor reports its own performance to a monthly CEO meeting of about eight minutes per initiative | The roadmap's governance section | wrong (control cannot carry the load) | Load test: 7 items × 1 hour | Correct: gates, stop rules, an independent sample | You | Charter stop rules; weekly spot audit; incident runbook |
| 13 | ChatNest's price and 15% discount end on 30 Nov; the CEO feels committed | Deck; Yoav's persona | fragile | — | Remove the deadline from the decision; re-screen in Oct 2027 | Yoav | Not signed |
| 14 | The container delays that drive WISMO could end; any WISMO saving would vanish with them | Shipments: 40 of 41 containers late since June | fragile | Watch the delay rate monthly | Trigger: re-forecast if delays stop | Tamar | Still delayed in Q1 2027 |

*What survives:* the goal of fewer waiting customers; an AI policy and governance document (as the AUP and governance charter of module 4); AI drafts for catalogue copy, within the tool and data rules (CopyGenie on business terms, P and I only).

**Cover note to Michal (24 November).** "The NextWave roadmap fails most likely on its first item: a chatbot would answer the biggest group of contacts with the date we promised, which has passed. Fourteen findings attached, each with evidence; twelve are wrong assumptions we can correct, two are dependencies to watch. What to decide before 30 November: do not sign ChatNest now; re-screen it after the date fix with a proof of concept on our own data. What survives: the goal, a policy and governance document, and AI help for catalogue copy. I am not independent of the roadmap I will write in January: I'd like Ronit and Tamar to pressure-test it before it goes to the steering committee."

</details>

## References

- Gary Klein, ["Performing a Project Premortem"](https://hbr.org/2007/09/performing-a-project-premortem), Harvard Business Review, September 2007.
- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting), course 4, module 4 (pre-failure reading; wrong vs fragile; reviewer independence; dispositions); named, not re-taught.
- Template: [pressure-test log](../../templates/pressure-test-log.md); [roadmap](../../templates/roadmap.md).
- Earlier: [03.8 · The roadmap](../module-03/lesson-08.md), [04.8 · Vendor and claim due diligence](../module-04/lesson-08.md), [02.7 · Writing a findings memo people believe](../module-02/lesson-07.md). Next: [07.8 · The board said yes](lesson-08.md).
