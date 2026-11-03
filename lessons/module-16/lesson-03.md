---
id: "16.3"
module: 16
minutes: 17
practice_minutes: 90
prerequisites: ["16.2", "02.4", "03.1", "03.3", "03.7", "03.9"]
objectives:
  - "Measure the writing burden from one logged week, say what that week is a sample of, and annualise it with its label."
  - "Find the money already being spent from a card statement and an accounts list, at a stated exchange rate."
  - "Map and screen the candidates in one table, including at least one that is not AI and one that is plain automation."
  - "Prepare a one-page proposal that lets the executive director ask the largest funder to change its report."
volatility: implementation
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): identify and prioritize opportunities; business cases"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "Microsoft, Technology and software grants and discounts for nonprofits (Business Basic free to 300 users; Business Premium US$5.50/user/month paid yearly)"
    url: https://www.microsoft.com/en-us/nonprofits/offers-for-nonprofits
  - title: "Bank of Israel, representative exchange rate API (US$ = ₪3.136, 2 November 2026)"
    url: https://boi.org.il/PublicApi/GetExchangeRate?key=USD
last_verified: "2026-11-03"
---

# 16.3 · Diagnosis

At Open Hands the biggest saving available in the whole engagement does not involve AI at all: it is a conversation with the funder whose report format takes most of the writing time. In this lesson you measure that burden from the one week anyone logged, find the money already being spent on software, screen every candidate in one table, and prepare the call in which the executive director asks the funder to change its report. At the end you have a baseline in hours with labels, a list of money already spent, a screened shortlist and a one-page proposal for the funder.

## The situation

Week 2, Sunday 22 November. Ronit has your findings memo; Yossi closed the respite link on Wednesday. The board hears you on 9 December; the Adler-Haddad Family Foundation's Q4 report is due on 15 January and its renewal proposal on 31 January. You have ten hours this week, four of them already promised to Yossi for Tuesday's access fix (16.4).

Stage 1 gave you the opportunity map ([03.1](../module-03/lesson-01.md)), the fast screen with its data gate ([03.3](../module-03/lesson-03.md)), baselines from exports ([02.4](../module-02/lesson-04.md)) and the ROI model that survives finance ([03.7](../module-03/lesson-07.md)). IBM's consulting certificate frames this as identifying and prioritising opportunities and building the business case. At 30 people, all of it fits in one table and one page — and the business case is in hours, because freed hours at a nonprofit go back to families; they do not come back as cash.

## What to do

### Step 1 — Say what the logged week is a sample of

Ronit asked ten people to log one week, 4–8 October, chosen "because that is when it hurts": the week before the Q3 Adler-Haddad report was due. Open [`people/time-log-2026-10.csv`](../../labs/module-16/data-room/people/time-log-2026-10.csv) and pivot hours by person and activity. Worked example:

| Measure (4–8 October) | Hours | Label |
|---|---|---|
| Adler-Haddad report, everyone | 57.8 | Measured |
| … the six coordinators | 37.8 (6.3 each; one 7.5) = 18.7% of their 201.8 hours | Measured |
| Coordinators' direct family time (contact and home visits) | 86.5 (42.9%) | Measured |
| Coordinators' case notes | 28.5 (4.8 each, 14.1%) | Measured |
| Coordinators' letters and translation | 6.5 | Measured |
| Head of development: funder writing | 21.5 of 42.0 (51.2%); reports only 12.0 | Measured |

Then the step everyone skips: **this is a peak, not a baseline.** Noa says a normal week is "maybe a third"; Samah says the narratives take two weeks a quarter, one drafting and one in corrections. So:

- Adler-Haddad a year ≈ 57.8 × 2 weeks × 4 quarters ≈ **462 hours** — *inferred*, ±25%. Development's own estimate in [`fundraising/funders.csv`](../../labs/module-16/data-room/fundraising/funders.csv) is 90 hours per report, 360 a year — *reported*.
- All funder reports ≈ 570 hours a year and proposals ≈ 223 (development's estimates, *reported*); Adler-Haddad alone is 63% of the report hours.
- "Half my week on reports" was the crunch week and included proposals: reports alone were 12 of 42 hours. The same-word test ([02.2](../module-02/lesson-02.md)) on "reports" turned a slogan into two numbers.

Ask for what is missing: one more logged week, a normal one, before the January crunch (Ronit agreed: 7–11 December). A baseline you cannot get today is one you schedule.

### Step 2 — Find the real bottleneck

Read the funder's template ([`grant-library/adler-haddad-quarterly-template.md`](../../labs/module-16/data-room/fundraising/grant-library/adler-haddad-quarterly-template.md)) next to the Q3 report extract and Open Hands' own [outcomes framework](../../labs/module-16/data-room/fundraising/grant-library/outcomes-framework-2024.md). The template asks for "a narrative for each family served under the grant" — 120 narratives every quarter, in English, written by coordinators who think in Arabic, Russian, Amharic or Hebrew. The framework, adopted by the board in 2024 and never used in a report, measures the same things in numbers, plus "up to six family stories a quarter told with the family's approval".

That is the bottleneck: not the speed of writing, but **what is asked to be written**. AI could make 120 narratives faster — and would do it by pasting more family details into more tools. Changing the format removes most of the work *and* most of the exposure. It is a conversation, not a tool.

### Step 3 — Find the money already being spent

From [`finance/card-statement-2026.csv`](../../labs/module-16/data-room/finance/card-statement-2026.csv) and [`it/accounts-and-licences.csv`](../../labs/module-16/data-room/it/accounts-and-licences.csv), at the Bank of Israel representative rate of ₪3.136 per US$ (2 November 2026):

| Item | Evidence | A year |
|---|---|---|
| Microsoft 365 Business Premium: 7 of 10 seats unused | 3 sign-ins since mid-August; nonprofit price US$5.50 per user per month, paid yearly (Microsoft's nonprofit offers page); renewal charge ₪2,072 on 14 October | 7 × 5.50 × 12 = US$462 = **₪1,449** |
| ChatGPT Plus on the second card since March, coded "Office supplies" | Card statement | US$240 = **₪753** |
| Dropbox Plus, unused since May 2024 | Accounts list, IT notes | US$144 = **₪451** |
| GrantGenie, converting to US$49 a month on 1 January | Its terms; accounts list | US$588 = **₪1,844** (avoidable) |
| **Total** | | **₪4,497 a year** (≈ ₪2,650 already being spent, ₪1,844 from January) |

"No budget" was true about new money and false about money. This list is the most persuasive page you will hand the treasurer, because it asks him to stop paying, not to start.

### Step 4 — Map and screen every candidate in one table

Combine the opportunity map and the seven-question screen into one table. The data gate does most of the work here: at Open Hands, the class of data a candidate touches decides more than its value.

| Candidate | Type | Data it touches | Verdict |
|---|---|---|---|
| Change the Adler-Haddad report format | **No AI** | Aggregated numbers, consented stories | **Go first** |
| Grant drafting from an approved content library | Assist | Organizational texts only | **Go** (16.5) |
| Case notes structured; letters to families in Arabic, Russian, Amharic | Assist | De-identified family text | **Go with conditions** (16.4 boundary, 16.5 test) |
| Funder narratives written by AI from raw notes | Generation | Identifiable family data | **Stop** (fails the data gate; removed by the format change) |
| Donor segmentation and personalised appeals | Generation | Donor personal data, ID numbers | **Plain automation, no AI**: a mail merge |
| Chatbot for families on the website | Bot | Families' rights questions | **Leave alone**: wrong-advice risk, nobody to maintain it |
| Volunteer scheduling | Automation | Volunteer contacts | **Leave alone**: a shared calendar |

Two lines matter for the board: the first ("the biggest win is not AI") and the fifth ("the thing someone already did with AI should have been a mail merge").

### Step 5 — Write the case in one page, in hours

Use the front page of the [decision-ready case](../../templates/decision-ready-case.md) ([03.9](../module-03/lesson-09.md)), shrunk:

- **Ask:** let the funder report shrink; give people a safe tool for writing; stop paying for what nobody uses.
- **Cost:** ₪0 now. Up to ₪602 a year from March (two nonprofit seats for development, if the free tools prove too limited), paid from the ₪4,497.
- **Freed (directional):** about 300–350 coordinator hours a year if the funder agrees to the short format; grant drafting 20–30% of ≈ 790 writing hours (assumed until tested in 16.5); case notes unknown until tested.
- **Not:** a cash saving, a smaller team, or reports that "write themselves".

Keep hours and shekels in separate columns all the way to the board. The treasurer's first question will be "how much, every year, and who approved it?" (persona: [Vova Gorelik](../../labs/module-16/personas/vova-treasurer.md); transcript: [here](../../labs/module-16/personas/transcripts/vova-treasurer.md)). His second will be about anything that turns hours into shekels. To practise the difference, the four-ledger simulation is optional:

[Simulation: ROI defender](../../simulations/roi-defender/index.html?preset=harbor)

### Step 6 — Prepare the call with the funder, and let Ronit lead it

You are a volunteer; the relationship is Ronit's. Your job is a one-page proposal she can send after the call, and three questions for the call itself. Worked example of the page:

> **Proposal for the Adler-Haddad quarterly report from Q4 2026.** (1) Outcomes for families under the grant against Open Hands' outcomes framework, with Q1–Q3 figures (rights obtained, appeals won, respite, parent rest score; split by language). (2) Up to six family stories a quarter, each told with the family's written consent and approval of the final text. (3) Outputs table and financial report unchanged. (4) Family names, towns, schools and diagnoses no longer appear in reports.

The three questions, in this order: *What does the foundation actually use the report for? Who reads which part? Would this format give you what you need?* (Persona: [Tamar Weiss-Levi](../../labs/module-16/personas/tamar-funder.md); transcript: [here](../../labs/module-16/personas/transcripts/tamar-funder.md).) In the worked example she reads the first ten narratives and skims the rest, uses the numbers and two or three stories for her board, and agrees to the short format for Q4. A good interviewer also learns that the foundation is drafting guidance asking grantees not to put identifiable family information into AI tools without safeguards — the transcript's interviewer never asked.

## Watch out

- **Annualising the crunch week.** 57.8 × 52 = 3,006 hours is wrong by a factor of six. Say what the week is a sample of, and schedule the normal week.
- **Solving the template with a tool.** Writing 120 narratives faster with AI multiplies the exposure. Ask first whether they need to be written.
- **Turning hours into shekels.** "350 hours × ₪100 = ₪35,000 saved" is a number the treasurer will (rightly) reject: nobody's salary changes.
- **Leading the funder call yourself.** The relationship and the renewal are Ronit's. Prepare, sit in, stay quiet unless asked.
- **Forgetting the "not AI" lines.** A shortlist where every candidate is AI tells the board you were looking for AI, not for the problem.

## Your turn

### Inputs

- Data room (module download): [`people/time-log-2026-10.csv`](../../labs/module-16/data-room/people/time-log-2026-10.csv), [`fundraising/funders.csv`](../../labs/module-16/data-room/fundraising/funders.csv), [`grant-library/`](../../labs/module-16/data-room/fundraising/grant-library/adler-haddad-quarterly-template.md) (template, Q3 extract, outcomes framework), [`finance/card-statement-2026.csv`](../../labs/module-16/data-room/finance/card-statement-2026.csv), [`it/accounts-and-licences.csv`](../../labs/module-16/data-room/it/accounts-and-licences.csv), [`company/budget-2026.md`](../../labs/module-16/data-room/company/budget-2026.md); `labs/module-16/build/content-library/numbers-2026-q1-q3.csv` (the numbers Shira compiled).
- Personas: [Vova](../../labs/module-16/personas/vova-treasurer.md), [Tamar](../../labs/module-16/personas/tamar-funder.md) (with Ronit); their transcripts; [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [task inventory](../../templates/task-inventory.md), [opportunity map](../../templates/opportunity-map.md), [use-case scorecard](../../templates/use-case-scorecard.md), [decision-ready case](../../templates/decision-ready-case.md).

### Steps

1. Pivot the time log; write the baseline table with labels and say what the week is a sample of.
2. Annualise Adler-Haddad two ways (log × weeks; development's estimate) and give the range.
3. List the money already spent, with sources and the exchange rate.
4. Write the one-table map and screen with at least six candidates, one "no AI" and one "plain automation".
5. Write the one-page case in hours.
6. Write the funder proposal page and the three questions; run the call with Tamar (roleplay, Ronit leading) or annotate the transcript.
7. Call Vova (roleplay or transcript) with the money list.

**Track B (Python).** Optional: `python discovery.py time funders money consent` (module download, `labs/module-16/`) prints the pivot, the funder hours, the money lines and the consent counts. Useful if you will re-run the baseline after the normal week is logged in December.

### Time

90 minutes: 25 for the baseline, 15 for the money, 20 for the map and case, 30 for the funder page and the two calls.

### Done when

- [ ] The baseline says it is a peak week and gives an annual range with a label, not a single number.
- [ ] The money list adds up, names its sources and states the exchange rate and date.
- [ ] The screen has a "no AI" candidate first and a "plain automation" candidate, and the data class decides at least one verdict.
- [ ] The case keeps hours and shekels in separate columns.
- [ ] The funder page proposes a concrete format and removes identifying details from reports; Ronit makes the ask.
- [ ] You learned what the funder uses the report for, and her foundation's view on grantees' AI use.

<details><summary>Reference answer</summary>

The full version is `labs/module-16/expert/03-baselines-and-shortlist.md`.

**Baseline (peak week, 4–8 Oct):** Adler-Haddad 57.8 h (coordinators 37.8, 6.3 each, 18.7% of their time); direct family time 42.9%; case notes 28.5 h (4.8 each); Noa 21.5 of 42 h funder writing, 12.0 h reports. **Annual Adler-Haddad:** 360 h (development's estimate, reported) to ≈ 462 h (log × 2 weeks × 4, inferred). **Asked for:** a normal week, 7–11 December.

**Money (₪3.136/US$, 2 Nov 2026):** Microsoft 7 unused seats ₪1,449; ChatGPT Plus ₪753; Dropbox ₪451; GrantGenie from January ₪1,844 → ₪4,497 a year.

**Screen:** format change (no AI) go first; grant drafting go; case notes and letters go with conditions; AI narratives from raw notes stop; donor segmentation → mail merge; family chatbot and volunteer scheduling leave alone.

**Case:** cost ₪0 now, ≤ ₪602 a year from March if needed, funded by the ₪4,497; freed ≈ 300–350 coordinator hours a year (directional) if the format changes.

**The call (25 Nov):** Tamar reads the first ten narratives, uses numbers and two or three stories for her board; agrees to the short format for Q4 and asks for the page in writing; the foundation is drafting AI guidance for grantees (no identifiable family data without safeguards).

**Vova:** approved cancelling Dropbox and reducing Microsoft on the call; would consider "up to ₪2,500 a year, one line, an owner, paid from what you cancel" — he says it only after seeing the money list.

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting): identifying and prioritising opportunities, business cases (named, not re-taught).
- Microsoft, [Technology and software grants and discounts for nonprofits](https://www.microsoft.com/en-us/nonprofits/offers-for-nonprofits) (checked 3 November 2026): Business Basic free to 300 users; Business Premium US$5.50 per user per month paid yearly.
- Bank of Israel, [representative exchange rate](https://boi.org.il/PublicApi/GetExchangeRate?key=USD) (₪3.136 per US$, 2 November 2026).
- Field kit: [02.4 · Measuring a baseline from exports](../module-02/lesson-04.md), [03.1 · The opportunity map](../module-03/lesson-01.md), [03.3 · The fast screen](../module-03/lesson-03.md), [03.7 · The ROI model that survives finance](../module-03/lesson-07.md), [03.9 · The decision-ready case](../module-03/lesson-09.md).
- Templates: [task inventory](../../templates/task-inventory.md), [opportunity map](../../templates/opportunity-map.md), [use-case scorecard](../../templates/use-case-scorecard.md), [decision-ready case](../../templates/decision-ready-case.md).
- Simulation (optional): [ROI defender](../../simulations/roi-defender/index.html?preset=harbor).
- Earlier: [16.2 · Discovery](lesson-02.md). Next: [16.4 · The hard part: four weeks, no budget, sensitive data](lesson-04.md).
