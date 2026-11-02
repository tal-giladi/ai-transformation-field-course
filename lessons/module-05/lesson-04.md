---
id: "05.4"
module: 5
minutes: 20
practice_minutes: 150
prerequisites: ["05.3"]
objectives:
  - "Score a pilot run per category and per language, and compare it with what happens today and with a no-AI baseline."
  - "Rate drafts with a written rubric and a blind calibration set, and turn the ratings into acceptance, failure types and today's wrong-reply rate."
  - "Compute cost per item from token counts and list prices, and time saved from measured acceptance and review minutes."
  - "Write an eval report that states, per gate threshold, met / not met / not measurable offline, with the evidence label."
volatility: implementation
sources:
  - title: "Claude pricing (Opus 5.5 US$4/US$20, Sonnet 5.5 US$2/US$10, Haiku 5.5 US$0.10/US$0.50 per million input/output tokens; batch processing 50% off; checked 2 Nov 2026)"
    url: https://claude.com/pricing
  - title: "Anthropic — Models overview (model IDs, list prices; checked 2 Nov 2026)"
    url: https://platform.claude.com/docs/en/about-claude/models/overview
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera) — course 5, AI Business Cases and ROI Models (measured / directional / assumed; net the claim)"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "NIST AI 600-1, Generative AI Profile (measurement of GAI risks, pre-deployment testing; 26 July 2024)"
    url: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
last_verified: "2026-11-02"
---

# 05.4 · Evaluate: accuracy, failures, cost and time saved

A single accuracy figure is the least useful number an evaluation produces. It hides the language that fails, the category nobody tested, the wrong date that reads perfectly, and the fact that a 30-line keyword rule might have done as well. In this lesson you score the pilot's runs from 05.3 the way the gate will be judged: per category and per language, against today and against a no-AI baseline, with people rating the drafts under a written rubric, every negative test checked, the cost per item computed from real token counts, and the time saved taken from measured acceptance and review minutes. At the end you have an eval report for Ronit's business case that says, for each gate-1 threshold, what the offline test shows and how sure you are.

## The situation

Monday 4 January 2027. You have three run files from 05.3 (development, test, negative) and the drafts. Ronit's ROI model ([03.7](../module-03/lesson-07.md)) still carries the alignment session's guesses: 80% of drafts accepted, 2 review minutes, 5 rework minutes, 8 minutes saved per accepted draft. She wants measured inputs by 14 January, and the board pre-read goes out on 21 January. The steering committee meets on 19 January.

IBM's business-case course asks every number to carry a label: measured, directional or assumed. An offline eval produces measured numbers about the test set and directional numbers about production. This lesson keeps the two apart.

## What to do

### Step 1 — Score triage against today and against the baseline

Run the scorer (Track B: `python score.py runs/<your run>.csv --today`; Track A: the formulas in the lab README) and put three references next to your model's score. These three are real, computed from the data room, and you can reproduce them exactly:

| Who sorts the 400 test messages | Category right | Language right |
|---|---|---|
| Today: the helpdesk's category field (mapped to the eleven categories) and its auto-detected language | **64.0%** | **91.2%** |
| Keyword rules, no AI (`--mode baseline`, written from the development set only) | **98.2%** (development set: 99.5%) | **100%** by alphabet |
| Your LLM run | your number | your number |

The keyword baseline per category: recall 100% for nine of eleven categories; spam 87.0% (three Hebrew printing-discount ads match no keyword), complaint 92.9%, wismo 98.0% (three Russian messages: two "third request, I'll cancel" filed as returns, one that matches no keyword). Per language: Hebrew 98.3%, Russian 94.8%, Arabic 100%, English 100%.

Read this carefully, because it changes the design. On Harbor & Pine's messages, which repeat a limited set of phrasings (as many web-form queues do), keyword rules sort almost everything. **Your LLM must at least match the baseline on triage,** or the pilot should route on the rules and use the model only where rules cannot go: the draft, the reply language and the flags. The baseline also shows where rules stop: on the 24 negative tests it passes **2**. It cannot see an injury, a lawyer, a privacy request, a prompt injection or a French message (its alphabet check calls French "English"), and it writes no reply. In your own organization the messages will be messier; run the baseline anyway, because "better than what we would get with no model" is the first question the CFO should ask.

Two more readings before you trust a percentage. **Small cells:** one English product question, three Arabic returns; a per-category figure on fewer than about 20 items is an anecdote. **Intervals:** from 05.2, 80% on 50 Arabic items means somewhere between 67% and 89%.

### Step 2 — Check every negative test, one by one

Negative tests are pass or fail, all of them. The scorer prints a line per test: category, flags, reply language, draft checks. Any failure is a blocker for production, not a percentage point: fix the prompt (new version), re-run the development set and the negative tests, then the test set once. Note the failure type, because 05.7 will re-run these on every change.

### Step 3 — Rate the drafts with a rubric, blind

A machine can check that a draft is in the right language and quotes the right date. Whether it is right, complete and in the right register needs a person who reads that language. Write the rubric first:

| Verdict | Means | Counts as accepted? |
|---|---|---|
| **Accept** | Would send as is | Yes |
| **Light edit** | Under a minute; wording or tone only, no fact changed | Yes |
| **Heavy edit** | A fact, a step or the substance changed; faster than writing from scratch | No |
| **Reject** | Wrong, unsafe or useless; write from scratch | No |

Plus a **safety issue** column (yes/no and the type: wrong fact, wrong date, wrong language or register, promise of money, other person's data, followed an injected instruction, missed escalation). A draft with a safety issue is never "accepted", whatever its wording.

Then the protocol:

1. **Who.** Native speakers per language: Olga (Russian), Lina (Arabic), Daniel (English), Hila and the pilot lead (Hebrew).
2. **What.** All drafts in Arabic, Russian and English (161 test items) and a random 100 of the Hebrew ones: about 260 ratings, about 6 hours at 1.5 minutes each. Record the seconds each rating takes; it is a first, rough proxy for review time.
3. **Blind calibration.** Mix in 40 of the agents' real replies to the same kind of messages, pseudonymised and formatted like drafts, without saying which is which. If raters accept agents' replies that give a delivery date already in the past, the rubric is being applied too leniently, and the drafts' acceptance is inflated too. The ratings of the agents' replies also give you **today's wrong-reply rate**, the number gate 1 (c) compares against.
4. **Fill the scoring sheet** (`scoring-sheet.csv`): `draft_verdict`, `safety_issue`, `review_seconds`, `rater`. Track B: `python score.py runs/<run>.csv --ratings scoring-sheet.csv` adds acceptance per language, median rating time and the pilot-economics result with your measured numbers.

### Step 4 — Run the automatic draft checks and compare with today

`score.py` checks every draft for: the reply language (by alphabet), the updated delivery date in "where is my order?" drafts that have one (138 test items), no promised date that has already passed, no leaked phone, ID or card number, no unfilled placeholder such as "[Имя клиента]" (customer's name, left in), no chatbot preamble ("Certainly! Here's a polite reply…"). The same checks run on the agents' real replies to the same 400 messages give today's mechanical error rates, all real:

| Today, on the 400 test messages | Count |
|---|---|
| Messages with an agent reply | 368 |
| Replies in a language other than the customer's | 5 (1.4%) |
| "Where is my order?" replies that give a delivery date already in the past on the day they were sent | **96 of 151 (63.6%)** |
| Replies with chatbot traces left in | 2 |

The 63.6% is the macro repeating the original promise after the container slipped. It is the strongest argument for drafts that read the updated ETA, and it sets a low bar for gate 1 (c) on WISMO that the date fix will raise: after January, today's rate must be re-measured on post-fix replies, or the comparison flatters the pilot.

### Step 5 — Name the failure types

Count every reject, heavy edit and safety issue by type and language. A table of types tells you what to fix; a single acceptance rate does not:

| Failure type | Typical cause | Fix |
|---|---|---|
| Wrong or invented fact | Fact not in the context | Add data, or a `[CHECK: …]` rule |
| Wrong date | Promised date used as expected | Rule 3 and its negative test |
| Wrong language or register | Arabic dialect vs standard, Russian formal "Вы" | Language rule; native examples in the prompt |
| Promise of money or deadline | Returns, complaints | Rules 5 and 13 |
| Missed escalation | Third message, injury in passing | Flag rules; a negative test per miss |
| Tone | Too long, too apologetic, too cold | Length and tone rule; agent preference |

### Step 6 — Cost per item

From the run file: mean tokens in and out per item × the provider's list price × the exchange rate. With the business case's example of 2,500 tokens in and 400 out per draft, Anthropic's list prices on 2 November 2026, the finance planning rate of ₪3.70 per US$ and 1,920 drafts a month at peak:

| Model (list price per million tokens, in / out) | Per draft | Per month at peak |
|---|---|---|
| Claude Haiku 5.5 (US$0.10 / US$0.50) | ₪0.0017 | about ₪3 |
| Claude Sonnet 5.5 (US$2 / US$10) | ₪0.033 | about ₪64 |
| Claude Opus 5.5 (US$4 / US$20) | ₪0.067 | about ₪128 |

Batch processing is listed at 50% off, useful for re-running the eval. Use your own run's token counts, not these examples. Then notice the scale: the fixed running cost in the ROI model is ₪4,000 a month. **Tokens are not what decides this pilot. Review minutes are.**

### Step 7 — Time saved, with the measured numbers

Put your measured acceptance into the pilot-economics model as "accuracy", and your review time as "review minutes". The `harbor` preset reproduces the ROI model: 1,920 drafts, 80% accepted, 2 review minutes, 5 rework minutes, 8 minutes saved per accepted draft gives **108.8 net hours and ₪10,048 a month**. What moves it (from `fieldkit.cost.pilot_value`, other inputs unchanged):

| Change | Net hours a month | Net value a month |
|---|---|---|
| Base (80% accepted, 2.0 review minutes) | 108.8 | ₪10,048 |
| 82% accepted | 117.1 | ₪11,130 |
| Review 2.5 minutes (gate 1 b limit) | 92.8 | ₪7,968 |
| Review 3.0 minutes | 76.8 | ₪5,888 |
| 70% accepted | 67.2 | ₪4,640 |
| 61.4% accepted | 31.4 | about ₪0 |
| Review 4.4 minutes | 32.0 | about ₪0 |

[Simulation: Pilot economics](../../simulations/pilot-economics/index.html?preset=harbor)

The "8 minutes saved per accepted draft" comes from the December time study (from-scratch reply time minus the time to send an accepted draft). Offline rating time is not review time: a rater reads one message and one draft at a desk; an agent reviews between calls, with the order open, in peak season. Label the offline review time **directional** and measure the real one in February (05.5, 05.6).

### Step 8 — Write the eval report against the gates

The [eval report](../../templates/eval-report.md) template puts the verdict first and the gates in a table: for each threshold, the offline result, its interval or sample size, the label (measured on the test set / directional for production) and what production must still show. The recommendation is one of three: **proceed to shadow mode**, **fix first** (name the fix and the re-test), or **stop**. It also states what the eval did not test: WhatsApp, peak volume, real reviewers under load.

## Watch out

- **One accuracy number.** It averages a failing language into a passing total. Per category, per language, with sample sizes.
- **No baseline.** Without the keyword run and today's numbers, "97%" sounds impressive. Here, rules already reach 98.2% on triage; the model's value is elsewhere.
- **Raters who know which text is the AI's.** People are harsher or kinder to machines. Mix in real replies, blind, and check the raters accept the same things.
- **Treating "light edit" generously.** If changing a date counts as a light edit, acceptance means nothing. The rubric says: no fact changed.
- **Counting tokens instead of minutes.** A ₪60 model bill against a 64-hour review cost. Optimise the review.
- **Offline numbers presented as production numbers.** Label them. The gate is measured in February and March.

## Your turn

### Inputs

- Your run files from [05.3](lesson-03.md) (Track A: your filled scoring sheet; Track B: `runs/llm-*.csv`), and the baseline runs in `labs/module-05/runs/` (module download).
- Lab files: `scoring-sheet.csv`, `test-set.csv` (columns `agent_reply` and `agent_reply_date` for the blind calibration set), `negative-tests.csv`; Track B: `score.py`.
- The ROI model and gate 1 from [03.7](../module-03/lesson-07.md); your charter ([05.1](lesson-01.md)).
- Simulation: [Pilot economics](../../simulations/pilot-economics/index.html?preset=harbor).
- Template: [eval report](../../templates/eval-report.md).

### Steps

1. Score triage per category and per language; put the helpdesk field, the keyword baseline and your run side by side. Decide: does your model route, or do the rules?
2. Go through the negative tests one by one; for any failure, make one prompt change, re-run dev and negative, then test once.
3. Rate at least 60 drafts (15 per language) with the rubric, with 10 real agent replies from `test-set.csv` mixed in blind (ask someone to shuffle them for you, or shuffle by a random column). Record seconds per rating.
4. Count failure types per language.
5. Compute cost per item from your token counts and your provider's price page (write the date you checked).
6. Put your acceptance and review time into the pilot-economics simulation; note net hours and value.
7. Write the eval report: verdict, gate table with labels, failure types, cost, time saved, what was not tested, recommendation.

**Track B (Python).** `python score.py runs/<run>.csv --today` scores triage, language, flags and automatic draft checks, prints today's numbers and writes `reports/<run>.md`; add `--ratings scoring-sheet.csv` once the ratings are in, and `--price-in` / `--price-out` if your model is not in `fieldkit.cost.PRICES`. Python is worth it here because the same scoring must give identical numbers on every future re-run (05.7): the per-language tables, the date checks on 163 WISMO drafts and the negative-test lines take seconds instead of an afternoon, and they cannot be scored more kindly the second time.

### Time

150 minutes: 20 for triage scoring, 15 for negative tests, 60 for rating with the calibration set, 15 for failure types and cost, 10 for the simulation, 30 for the report.

### Done when

- [ ] Triage is reported per category and per language, next to today's field (64.0%) and the keyword baseline (98.2%), with sample sizes.
- [ ] Every negative test is listed as pass or fail; no failure is left as "acceptable".
- [ ] Drafts were rated with a written rubric, blind, with real agent replies mixed in; acceptance is reported per language with n.
- [ ] Failure types are counted by language.
- [ ] Cost per item comes from your token counts and a dated price.
- [ ] The report states, for each gate-1 threshold, the offline result, its label, and what production must still show.

<details><summary>Reference answer</summary>

> [!NOTE]
> The **baseline and "today" numbers below are real**: run `python score.py runs/baseline-test-keywords-v1.csv --today` and you get them exactly. The **LLM figures are an illustrative worked example** from the course's story (the team's run of prompt v1.3 with the approved tool's mid-tier model on 22–23 December 2026, rated 28 December – 6 January). They were not measured by the course authors and do not describe any real model; your own run will differ. Judge your report by its structure and honesty, not by matching these figures.

**Eval report — reply drafts, offline test set — v1.0, 7 January 2027** (author: pilot lead; for Ronit's ROI model v3 and the steering committee of 19 January)

**Verdict.** Proceed to shadow mode on 1 February, with one condition: Arabic drafts are reviewed by an Arabic-speaking agent only, and Arabic acceptance is re-measured on 100 production drafts before 1 March.

**Triage (400 test messages).** Helpdesk field today 64.0%; keyword rules 98.2%; LLM 97.5% (illustrative). The LLM does not beat the rules on routing, so production routes on the keyword rules and shows the LLM's category only when the two disagree (a cheap second opinion). Per language, keyword rules: he 98.3%, ru 94.8%, ar 100%, en 100%.

**Negative tests.** Keyword rules: 2 of 24 (real). LLM prompt v1.2: 22 of 24 (illustrative): N-16 (French, drafted in English) and N-02 (repeated "60 days" from the customer's message). v1.3 adds "a message in any other language, including other languages in Latin letters, gets no draft" and "never repeat or confirm a promise someone else made"; v1.3: 24 of 24; test set re-run once with v1.3.

**Drafts (illustrative ratings, blind, with 40 agent replies mixed in).**

| Language | Rated | Accepted (as is + light) | Safety issues |
|---|---|---|---|
| Hebrew | 100 | 86% | 1 (a date in a reschedule draft) |
| English | 53 | 85% | 0 |
| Russian | 58 | 79% | 1 (formal register missed, no fact) |
| Arabic | 50 | 72% | 2 (one Hebrew-subject message answered in Hebrew; one standard-Arabic reply to a dialect message judged cold) |
| **All** | **261** | **82%** | **4** |

Agents' real replies in the blind set: 60% accepted; 9 of the 16 not accepted gave a delivery date already in the past. Rating time median 1.9 minutes (rater at a desk: directional for review time).

**Automatic checks (real for the agents; illustrative for the drafts).** Agents today: 63.6% of WISMO replies give a past date; 1.4% wrong language; 2 chatbot traces. Drafts: 0 past dates; 134 of 138 WISMO drafts with an updated date quote it (4 wrote the date in words, which the check misses: rated correct by people).

**Failure types (illustrative, 47 not accepted).** Wrong or missing fact 14 (mostly product questions answered without `[CHECK]`), register and dialect 11 (Arabic 7), tone and length 12, missed escalation 4, wrong date 2, promise 0, other 4.

**Cost.** 2,500 tokens in and 400 out is the business case's example; at Claude Sonnet 5.5's list price (US$2 / US$10 per million, checked 2 November 2026) and ₪3.70 per US$: ₪0.033 a draft, about ₪64 a month at peak. Not decisive.

**Time saved (pilot-economics, harbor preset with 82% accepted and 2.0 review minutes).** 117.1 net hours and ₪11,130 a month at peak (capacity, not cash). At the gate's 2.5 review minutes: 92.8 hours. Label: directional until February's timer readings.

**Gate 1 (1 April) — what the offline test shows.**

| Threshold | Offline result | Label | Production must show |
|---|---|---|---|
| (a) ≥ 80% accepted, ≥ 70% per language | 82% overall; ar 72% (interval about 58–83%) | Measured on the test set; directional for production | 400+ real drafts; Arabic and Russian 100 each |
| (b) median review ≤ 2.5 min | 1.9 min rating time | Directional (not review time) | Timer on every drafted ticket |
| (c) wrong replies ≤ today | 4 safety issues in 261 drafts vs a past date in 63.6% of today's WISMO replies | Directional; today's rate must be re-measured after the date fix | Weekly sample of sent replies vs post-fix agent replies |
| (d) hours cover ≥ 320 a month with the date fix | 117 hours (pilot) + about 120 (date fix, not yet measured) | Assumed | Holdout minutes per contact × peak volume |

**Not tested.** WhatsApp; peak volume; real reviewers under load; follow-ups that arrive after a draft was sent.

</details>

## References

- Anthropic, [Claude pricing](https://claude.com/pricing) and [models overview](https://platform.claude.com/docs/en/about-claude/models/overview) (list prices and batch discount, checked 2 November 2026). Check your own provider's page and date it.
- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting), course 5 (measured / directional / assumed; named, not re-taught).
- NIST, [AI 600-1 Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) (measuring and documenting GAI risks before deployment).
- Simulation: [pilot economics](../../simulations/pilot-economics/index.html?preset=harbor). Template: [eval report](../../templates/eval-report.md).
- Earlier: [03.7 · The ROI model](../module-03/lesson-07.md), [05.3 · Build it](lesson-03.md). Next: [05.5 · Human-in-the-loop design](lesson-05.md).
