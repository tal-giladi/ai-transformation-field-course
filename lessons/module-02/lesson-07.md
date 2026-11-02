---
id: "02.7"
module: 2
minutes: 18
practice_minutes: 90
prerequisites: ["02.6"]
objectives:
  - "Check an AI-drafted memo statement by statement against its sources and keep a check log: kept, corrected or removed."
  - "Write a two-page findings memo that answers the sponsor's question in its first three sentences, with every finding as claim, evidence and consequence."
  - "State what is not known yet and the decisions needed, without blaming or naming individuals."
volatility: implementation
sources:
  - title: "Mata v. Avianca, Inc., No. 22-cv-1461 (PKC), Opinion and Order on Sanctions (S.D.N.Y., 22 June 2023)"
    url: https://storage.courtlistener.com/recap/gov.uscourts.nysd.575368/gov.uscourts.nysd.575368.54.0.pdf
  - title: "NIST AI 600-1 — Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (July 2024)"
    url: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
last_verified: "2026-11-02"
---

# 02.7 · Writing a findings memo people believe

Discovery ends in a memo, and the memo is what people remember: the CEO will quote one sentence from it to the board, the CFO will test one number in it, the support manager will read it for what it says about his team. In this lesson you first check a findings memo someone drafted with an AI assistant — it reads well and is wrong in at least eight places — and then write your own: answer first, every finding with its evidence and consequence, what you don't know yet, and the decisions you need. At the end you have a check log of the AI draft and a two-page findings memo for Harbor & Pine that would survive the CFO's questions.

## The situation

Monday 30 November 2026. The readiness assessment went to the steering check-in this morning (02.6). Tomorrow, day 30 of your plan, the findings memo is due to Michal; on 10 December she and Yoav decide what to have working by the board meeting on 28 January.

In the data room there is already a memo: `documents/findings-memo-ai-draft.md`, "DRAFT v0.3", dated 19 October, sent to Yoav and Michal "from Operations", drafted with an AI assistant from the helpdesk export and the KPI report. It recommends a chatbot in Q1 2027 and a 40% cost reduction. Yoav has read it. If your memo disagrees with it, you need to show exactly where it is wrong and why, without making it about whoever wrote it.

IBM's readiness course ends on the same two moves: report every claim no stronger than its source, and when an AI assistant drafts the report, compare it against the source record and restore what it collapsed, omitted or misweighted. Here you do both on a real draft.

## What to do

### Step 1 — Check the AI draft statement by statement

Generative AI produces what NIST's Generative AI Profile calls confabulation: confidently stated but false content. It also does quieter damage: it collapses definitions ("average" becomes "median"), counts the population it was given rather than the one that matters, and reads a status field as a fact. The most public warning is *Mata v. Avianca* (S.D.N.Y., 22 June 2023): lawyers filed a brief citing judicial opinions that ChatGPT had invented and kept standing by them when the court asked; the court imposed a $5,000 penalty and reminded them that "existing rules impose a gatekeeping role on attorneys to ensure the accuracy of their filings." Whoever sends a memo owns every sentence in it, whoever drafted it.

The method:

1. Split the draft into **checkable statements**: every number, every citation, every definition, every causal claim.
2. For each, find the **source** it claims or implies, open it, and reproduce the statement.
3. Mark it **kept**, **corrected** (with the right statement) or **removed** (no source can support it).
4. Then read for what is **missing**: the finding the draft never mentions because its inputs never contained it.

Worked example on three statements:

| Statement in the draft | Source checked | Result |
|---|---|---|
| "The median first response time is 2 hours, meeting the target" | KPI report footnote 1: *average* of working hours, Q3, email only, received on business days (n = 718); `tickets.csv`: wall-clock median 6.1 h, all channels | **Corrected.** The 2.0 h is a mean under a narrow definition; the customer's median wait is 6.1 h, 10.0 h on the web form |
| "According to a Gartner 2025 study of 400 retailers, AI chatbots fully resolve 65–70% of enquiries" | No document attached; a search on 2 November 2026 found no such study | **Removed** unless the author produces the document. A citation nobody can open does not go into a memo |
| "Only 18% of tickets are delivery-status questions" | `tickets.csv`: "Delivery status" = 463 of 2,529 = 18.3% — but that category exists only from 1 July; before July the same questions were "Delivery"; 28.5% sit in "Other" | **Corrected.** The draft counted one category over six months. The five signals in 02.4 give 31–44% |

Watch the pattern in the third one: the arithmetic is right and the conclusion is wrong. That is the most common AI-draft error, and the one a reader can't catch without the data.

### Step 2 — Find what the draft left out

The draft was made from the helpdesk export and the KPI report, so it cannot know what those files don't contain. Nothing about the WhatsApp phones (about five times the helpdesk's weekly volume in the tallied week), nothing about the promised delivery date (the cause of the largest category), nothing about claim outcomes, nothing about the stale catalogue behind the ChatNest demo it recommends. An AI draft is bounded by its inputs; a findings memo must be bounded by the question.

### Step 3 — Answer first

Write the memo for the person who reads only the first paragraph. Three sentences: the answer to the question you were given, in the sponsor's words; the one number that carries it; what you recommend deciding. The question is the one your 30-60-90 set for days 1–30 (01.4): what is really happening in the work, the data and the AI already in use? Michal's objective (01.2) says where the answer has to lead: "The board sees one thing that already works." Background, method and caveats go after, or in the appendix.

### Step 4 — Each finding: claim, evidence, consequence

Three to six findings. Each one:

- **Claim** in one sentence a non-specialist can repeat.
- **Evidence**: file or interview, the number with its denominator and date, and its status — verified or reported (02.6).
- **Consequence**: what it means in time, money or risk, for whom, for the decision on 10 December.

Where governance is involved, translate twice: the obligation ("customer messages sit on shared phones outside any system, and nobody has checked our databases against the 2025 privacy amendment") and the operating consequence ("so the main channel has no baseline, and any AI tool on it would start without permission or data").

Keep statistics out of the sentence that carries the argument. "Two in five contacts ask where their order is" carries; "31.3%–43.8% depending on signal" goes in the evidence line.

### Step 5 — Say what you don't know, and what you looked for and didn't find

"We don't know handling time per task; the time study runs 6–17 December." "We found no evidence that QA reviews claims." "We could not join WhatsApp conversations to orders." These sentences make the rest believable: they show where your knowledge stops.

### Step 6 — Ask for decisions

End with a short table: decision, options, your recommendation, who decides by when. A findings memo that asks for nothing is a status report.

### Step 7 — Protect people, and check tone

No names next to workarounds. No team blamed for a system's design: "the promised date is never updated" not "logistics doesn't tell customers". Send the memo to the people it describes before it goes up — you promised Samir and Tamar they would see it first.

### Step 8 — If you used AI to draft, show your check

You may well use an assistant to tighten your own memo. Give it your verified findings table, not the raw data; tell it not to add sources or numbers; then check every sentence against your table as in Step 1, and keep the check log in the appendix. That log is what lets Ronit trust a memo she knows was AI-assisted.

## Watch out

- **Polish as proof.** The AI draft reads better than most human drafts. Fluency is not evidence.
- **Right arithmetic, wrong population.** 463 ÷ 2,529 is 18.3%; it answers the wrong question. Check what was counted, not only the division.
- **Citations nobody can open.** Ask for the document. No document, no citation.
- **Definitions that drift.** Mean becomes median, "resolved" becomes "solved", "every ticket" ignores 78 blanks. Re-read every definition against the source.
- **The memo as a story about people.** "Agents misuse ChatGPT" will be quoted, and you will lose the team that has to make the pilot work. Write about the work.
- **Burying the answer.** If the first paragraph is background, the CEO quotes the old draft.
- **Attacking the old draft's author.** Correct the statements, not the person; the draft was made from the files Operations had.

## Your turn

### Inputs

- In the module download: [`documents/findings-memo-ai-draft.md`](../../labs/common/harbor-and-pine/documents/findings-memo-ai-draft.md), [`company/kpi-report-2026-q3.md`](../../labs/common/harbor-and-pine/company/kpi-report-2026-q3.md), [`support/tickets.csv`](../../labs/common/harbor-and-pine/support/tickets.csv), [`company/finance-summary.md`](../../labs/common/harbor-and-pine/company/finance-summary.md), [`vendors/chatnest-sales-deck.md`](../../labs/common/harbor-and-pine/vendors/chatnest-sales-deck.md).
- Your outputs from 02.1–02.6: interview notes, task inventory, baseline sheet, data profiles, readiness assessment.
- Template: [findings memo](../../templates/findings-memo.md). Feedback: [coach prompt](../../labs/common/coach-prompt.md), with this lesson's "Done when" list as the checklist.

### Steps

1. Split the AI draft into checkable statements (at least ten) and check each against its source: kept, corrected or removed, with the source and the right statement.
2. List what the draft left out that a findings memo for Michal must contain.
3. Write your findings memo: answer in three sentences, three to six findings, what you don't know, what you looked for and didn't find, decisions needed. Two pages at most, plus an appendix with sources and, if you used AI, the check log.
4. Run the coach prompt on your memo with the "Done when" list as the checklist; fix what it finds.

### Time

90 minutes.

### Done when

- [ ] The check log covers at least ten statements from the draft, each with its source and a result.
- [ ] The first three sentences of your memo answer Michal's question and name a decision.
- [ ] Every finding has a claim, evidence with number, denominator, date and status, and a consequence.
- [ ] The memo names what you don't know and what you looked for and didn't find.
- [ ] A decisions table with options, recommendation, owner and date.
- [ ] No individual named next to a workaround; no team blamed for a design gap.

<details><summary>Reference answer</summary>

**Check log — "Findings memo DRAFT v0.3", 19 October 2026.**

| # | Statement in the draft | Source checked | Result |
|---|---|---|---|
| 1 | "Efficient but expensive" | No measure of efficiency in any source | Removed (opinion presented as finding) |
| 2 | "Median first response of 2 hours" (summary and finding 3) | KPI footnote 1; `tickets.csv` | Corrected: mean of working hours, Q3 email received Sun–Thu = 1.97 h; customer's wall-clock median 6.1 h (web form 10.0 h) |
| 3 | "Resolves 100% of tickets" | KPI footnote 2; `tickets.csv` | Corrected: status set on reply (81.2% within 5 min of the reply); 23.4% of resolved tickets with an order get a follow-up within 14 days |
| 4 | "2,529 tickets … plus phone calls" | `tickets.csv`, `phone-log.csv`, WhatsApp tally | Corrected: kept the 2,529; added 3,194 calls and WhatsApp (630 conversations in one tallied week, ~2,700 a month) |
| 5 | "Only 18% are delivery-status questions" | `tickets.csv` categories, handbook Addendum A | Corrected: one post-July category over six months; WISMO is 31–44% across five signals |
| 6 | "Spread across many smaller categories, typical for furniture retail" | No source for "typical" | Removed |
| 7 | "Speed is not the problem — cost is" | Contradicted by 2 and by CSAT 63% (KPI report: negative ratings mostly about delivery dates) | Removed |
| 8 | Languages 54% / 12% / 13% / 13% "based on the language field" | `tickets.csv` `language` | Corrected: the arithmetic matches the field (he 54.4%, ar 12.9%, en 12.9%, ru 11.7%), but the field is auto-detected with 121 blanks and 85 wrong codes, and excludes WhatsApp, where Russian is ~22% |
| 9 | "Gartner 2025 study of 400 retailers … 65–70% … up to 45%" | No document; search on 2 Nov 2026 found none | Removed unless the document is produced |
| 10 | "Every ticket has a category; 29% are 'Other'" | `tickets.csv` | Corrected: 78 blank (3.1%); "Other" 28.5% |
| 11 | "ChatNest has already given a demo built on our catalogue" | ChatNest deck slide 4; both catalogues | Corrected: built on the 2023 shared-drive copy (Oslo sofa ₪4,290 vs ERP ₪4,990; discontinued items recommended) |
| 12 | "Go live in Q1 2027 on the website and WhatsApp" | Finance summary (Q1 weakest cash quarter); timesheets (92% utilisation Nov–Jan); tally (no WhatsApp integration) | Removed as a recommendation; see readiness verdicts |
| 13 | "Target: 40% cost reduction in line with the CEO's commitment" | Board minutes (no basis given); finance summary (headcount savings only with a named plan) | Removed: a commitment is not a finding |

**Left out by the draft:** the promised-date cause and the delivery lateness; WhatsApp as the main channel; claim outcomes missing; the QA step that exists only on paper; customer data in free chatbots and on shared phones; the open privacy questions.

**Findings memo — what is really happening in customer service, and what to do first.** To Michal Peretz · Cc: Ronit Avraham · 1 December 2026 · Draft for Samir's and Tamar's comments by 3 December.

> **Answer.** Customers are angry mainly because the delivery date we promise at checkout is a fixed
> number of days that is never updated when a container is late, and our support team spends much of
> its day answering that one question by hand. About two in five contacts ask "where is my order?",
> and most of them come in on four WhatsApp phones that no system counts. I recommend deciding on
> 10 December to fix the promise first, with a daily delay notice that needs no AI, and to prepare a
> draft-reply pilot for the other questions from February; a customer-facing chatbot is not ready.
>
> **1. The promise causes the biggest share of contacts.** The web store promises 42 days for Vietnam
> and 38 for China, a table last changed in February 2023; Vietnam and China orders promised from June
> arrived a median 11 days late (n = 1,106; 95% late), and "where is my order" contacts arrive a median
> 12 days after a delayed container's original ETA (`orders.csv`, `shipments.csv`, `tickets.csv`;
> verified). *Consequence:* a chatbot would give the same wrong date faster; the fix is upstream and
> cheap.
>
> **2. Most written work is on WhatsApp, where we measure nothing.** In the week of 18–22 October agents
> tallied 630 WhatsApp conversations and about 124 hours, against 94 helpdesk tickets (hand tally,
> reported; helpdesk verified). Customer messages and photos stay on shared phones. *Consequence:* the
> main channel has no baseline, no test set and no access control; that is both a privacy question and
> the reason the time sheets show 70% "email".
>
> **3. Our reported numbers describe the process, not the customer.** "2.0 hours" is a working-hours
> mean for email on business days; the customer's median wait is 6.1 hours, 10 on the web form.
> "Resolution 100%" is a click on reply; 23% of resolved tickets with an order come back within 14 days
> (`tickets.csv`; verified). *Consequence:* any pilot judged on these KPIs will look good or bad for
> the wrong reasons; I propose reporting both definitions from December.
>
> **4. Two ideas are not ready, and why.** Claim decisions: the outcome is missing on 32% of claims and
> the 48-hour QA review in the handbook does not exist (claims log, org chart; verified). The ChatNest
> demo answered from a 2023 catalogue copy with old prices and discontinued items (verified).
>
> **5. The team has already found its own AI tools.** Customer emails were pasted into free chatbots to
> write Russian and Arabic replies faster; six sent replies still carry chatbot phrasing (`emails.csv`;
> verified); the interim rule of 12 November stopped it, and a careful Russian reply now takes about
> 13 minutes instead of 5 (observed once). *Consequence:* without an approved tool the workaround will
> return; with one, these agents are the pilot's best allies.
>
> **What we don't know yet.** Handling time per task (time study 6–17 December); whether past messages
> may be used to build and test a drafting tool (question with counsel through Ronit); what number
> agents type as "order number" on WhatsApp. **Looked for and not found:** any record of QA review; any
> export of WhatsApp conversations.
>
> | Decision (10 Dec) | Options | Recommendation | Who |
> |---|---|---|---|
> | First move for the board | Bot / delay notice / both | Delay notice, live by mid-January, measured | Michal, Yoav |
> | Owner of the promised date | Marketing / logistics / operations | Operations owns the rule; marketing the web store | Michal |
> | Approved drafting and translation tool | Decide now / after counsel | Decide now, conditional on counsel's answer | Michal, Ronit |
> | WhatsApp | Keep as is / business integration / move to the helpdesk | Scope a decision for January | Michal, Samir, Avi |

</details>

## References

- *Mata v. Avianca, Inc.*, [Opinion and Order on Sanctions](https://storage.courtlistener.com/recap/gov.uscourts.nysd.575368/gov.uscourts.nysd.575368.54.0.pdf), S.D.N.Y., 22 June 2023 — fabricated citations generated by ChatGPT; $5,000 penalty.
- NIST, [AI 600-1 Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) (July 2024) — confabulation as a generative-AI risk.
- Template: [findings memo](../../templates/findings-memo.md). Field kit: [coach prompt](../../labs/common/coach-prompt.md).
- Previous: [02.6 · The readiness assessment as a deliverable](lesson-06.md). Module practical: [Discovery at Harbor & Pine](../../projects/m02-discovery.md).
