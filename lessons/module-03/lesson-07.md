---
id: "03.7"
module: 3
minutes: 20
practice_minutes: 120
prerequisites: ["03.6"]
objectives:
  - "Build an ROI model in the finance team's own template: costs by year (build, seats, tokens, integration days, review labour), benefits by year, three scenarios, NPV at the hurdle rate, payback and the approval level."
  - "Net every claimed benefit across four ledgers (the sponsor's team, the receiving team, review labour, the customer's share) and label it measured, directional or assumed, cash or capacity."
  - "Price the expensive error and the review minutes that follow from where the human check sits."
  - "Write staged gates as yes/no conditions and test the case's most fragile assumption with a sensitivity table."
volatility: implementation
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera) — course 5, AI Business Cases and ROI Models"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "Claude pricing (Anthropic) — API prices per million tokens, checked 2 Nov 2026"
    url: https://claude.com/pricing
  - title: "Klarna press release, 27 Feb 2024 — AI assistant handles two-thirds of customer service chats in its first month"
    url: https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/
  - title: "Entrepreneur, 9 May 2025 — Klarna is hiring customer service agents after AI couldn't cut it on calls, according to the company's CEO"
    url: https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396
last_verified: "2026-11-02"
---

# 03.7 · The ROI model that survives finance

The sponsor's deck says the drafts pilot is worth ₪1.36 million a year: the 40% the board was promised. Finance will find a much smaller number, and if finance finds it before you do, your case is dead. In this lesson you build the model Ronit will review, in her template: what the pilot really saves after the human check and the rework, which saving is cash and which is only hours, where work moves to other teams, what the customer keeps, what an error costs, and what the whole thing is worth at a 12% hurdle rate in three scenarios. At the end you have a case worth about ₪113,000 a year in cash, plus capacity that is not cash, that clears the hurdle in the expected case, and that you can defend line by line.

## The situation

Mid-December 2026. The alignment session ([03.6](lesson-06.md)) agreed three bets and asked for the drafts case in Ronit's template by 14 January. Michal's first draft of the deck, written with the CEO's 40% in mind, claims ₪1,360,000 a year from seven benefits; it is the same figure the previous consultant's roadmap used (`documents/roadmap-previous-consultant.md`). Ronit has told you how she judges a project (`company/finance-summary.md`; her persona transcript): her template, three scenarios, NPV at 12%, payback within 24 months preferred, the board above ₪150,000 over three years, headcount savings only with a named plan, money released in stages against conditions written in advance. In 2022 she approved a CRM case on the vendor's numbers and wrote off ₪860,000 a year later.

IBM's business-case course names the moves: net the claim, capacity versus cash, the customer's share, gate placement as a cost line, discounting, staged commitments. Here you build the spreadsheet.

## What to do

### Step 1 — Ask finance for its template and rules before you build anything

Build in the CFO's format, with her numbers, or rebuild it later. From Ronit: the template (costs and benefits by year, one-off and running, three scenarios, NPV, payback, the budget each benefit lands in); hurdle rate 12%; approval bands (₪50,000 department head and CFO; ₪150,000 CEO; above that over three years, the board); planning rate ₪3.70 per US$ (finance planning rate, October 2026); Q1 is the weakest cash quarter. Ask her one more question: "Which indicator do you already review that would show this working?" (Her answer: support cost, the KPI report, and the temp and overtime lines.)

### Step 2 — Hours first: what the pilot saves after the human check

The pilot drafts replies; an agent reads every draft and sends it. Model a peak month with the numbers from the alignment page and the pilot-economics model:

| Line | Calculation | Hours a month |
|---|---|---|
| Written contacts (WhatsApp routed into the helpdesk) | 3,200 | — |
| Drafted (60%) | 1,920 drafts | — |
| Saved on accepted drafts (80% × 8 minutes) | 1,536 × 8 min | 204.8 |
| Review of every draft (2 minutes) | 1,920 × 2 min | −64.0 |
| Rework of wrong drafts (20% × 5 minutes) | 384 × 5 min | −32.0 |
| **Net** | | **108.8 (about 0.6 of a person)** |

At ₪130 an hour (₪3.4 million ÷ 14 people ÷ about 1,870 paid hours each) that is ₪14,144 of capacity a month. Running cost is about ₪4,096 a month: ₪4,000 fixed (licences, hosting, monitoring and change control, an estimate) plus about ₪96 in tokens. Net about **₪10,048 a month, breakeven on the ₪120,000 build in 11.9 months**, but only in hours. Nobody's budget changes because agents have 109 hours.

Two things to notice. **The review is the biggest cost line**: 64 hours a month, more than three times the rework, and it is set by where the human check sits. Checking every draft before it is sent is the right gate for a pilot whose drafts reach customers; a check only on drafts that a risk signal flags would cost less but is not safe until the error rate is measured. **Tokens hardly matter**: 2,500 tokens in and 400 out per draft at the simulation's example prices (US$3 and US$15 per million) is about ₪96 a month; at Anthropic's listed API price for Claude Sonnet 5.5 (US$2 and US$10 per million, checked on claude.com/pricing on 2 November 2026) it is about ₪64. If review minutes rise from 2 to 4.4, the pilot is worth nothing; if token prices double, nobody notices.

[Simulation: Pilot economics](../../simulations/pilot-economics/index.html?preset=harbor)

### Step 3 — List every cost, including the ones that are not on the invoice

| Cost | Amount | Basis |
|---|---|---|
| Integration: helpdesk (draft only), Priority and ETA data (read) | ₪56,000 | 14 integrator days × ₪4,000 (estimate) |
| Prompts, test set and evaluation harness | ₪32,000 | 8 days × ₪4,000 (estimate) |
| Olga labels the test set | ₪5,200 | 40 hours × ₪130 |
| Training the agents | ₪5,460 | 14 people × 3 hours × ₪130 |
| Contingency | ₪21,340 | about 18% |
| **Build, one-off** | **₪120,000** | |
| Running | **₪49,000 a year** | ₪4,000 a month fixed + tokens, rounded to thousands as in the template |

Internal hours (Olga, training) are counted at ₪130 even though they are not cash either: finance counts them, and it keeps the case conservative. Three years: ₪120,000 + 3 × ₪49,000 = **₪267,000**, above the ₪150,000 line, so **the board decides**. Saying that yourself, before Ronit does, is part of the case.

### Step 4 — Net every claim across four ledgers

For each claimed benefit, ask four questions: does the **sponsor's own team** carry a cost or a double count; does a **receiving team** (logistics, marketing, the claims desk) get new work; does the **review labour** that keeps it safe eat part of it; does the **customer** keep part of the gain? Then label it **measured** (counted from data you can show), **directional** (the direction is evidenced, the size is an estimate) or **assumed** (a belief, a vendor figure, someone else's number), and **cash** (money that stops leaving or starts arriving in a named budget line) or **capacity** (hours, until someone owns a plan for them).

| # | Claim (₪ a year) | Adjustments | Net | Label | Class |
|---|---|---|---|---|---|
| 1 | Agents save 8 minutes per accepted draft, 319,500 | Rework −49,920 (sponsor); review −99,840 (control); −96,000 moves to claim 7 | 73,740 | measured on a sample of 400 real emails | capacity |
| 2 | Two fewer agents from April, 431,400 | The same hours as claim 1, counted twice: −431,400 | 0 | assumed | capacity |
| 3 | Fewer WISMO contacts, 300,000 | Caused by the date fix, not by this pilot: −300,000 (it belongs in the date-fix case) | 0 | directional | capacity |
| 4 | Translation service not needed, 42,000 | Marketing keeps a small plan −12,000 (receiving); native-speaker spot-check, about 100 hours, −13,000 (control) | 17,000 | measured (invoices) | cash |
| 5 | Fewer goodwill credits, 103,500 | Rina records every outcome −13,000 (control); half is money customers no longer get −51,750 (customer) | 38,750 | assumed | cash |
| 6 | Repeat purchases from faster replies, 67,600 | Gross margin (42%), not revenue: −39,200 (customer) | 28,400 | assumed | cash |
| 7 | No seasonal temps next peak, 96,000 | Samir and Michal sign that the next peak runs without the two temps if the pilot holds its numbers; the cost moves out of claim 1's capacity, not on top of it | 96,000 | directional | cash |

Notice three different mistakes in the deck. Claim 2 counts claim 1's hours a second time as salaries. Claim 3 is real but belongs to another project: ask what happens without the pilot (the credible counterfactual), and the WISMO drop is the same. Claims 5 and 6 are partly the customer's money: a "saving" on goodwill credits is a credit a customer no longer gets, and some of it comes back as complaints and lost sales.

Not every adjustment you can think of belongs in the netting. Taking a "customer's share" off claim 1 because customers get faster replies is a mistake: a faster reply does not reduce the hours agents save. The customer's share matters when the claim counts money the customer keeps or no longer receives.

[Simulation: ROI defender](../../simulations/roi-defender/index.html?preset=harbor)

### Step 5 — Price the expensive error

Some drafts will be wrong, and some wrong drafts will get past the agent. A wrong reply that reaches a customer costs a re-contact and sometimes a credit; the portfolio card priced it at about ₪120. Count only the change from today: agents already send wrong replies (the WISMO macro repeats a date that has passed). Every percentage point of drafts that reach customers wrong *on top of* today's rate costs 23,040 drafts a year × 1% × ₪120 = **about ₪27,600 a year**. That is why the error rate in shadow mode is a gate condition, not a footnote: at 1.5 points above today the expected case loses about ₪100,000 of NPV.

### Step 6 — Turn capacity into cash only through a named plan, and test it

Ronit's rule is right: freed hours are not cash until a budget line changes, with an owner and a date. In this case one line can change: Samir hires two temps every November to January, about ₪16,000 a month each, ₪96,000 a peak. Samir and Michal can sign, in advance, that the next peak runs without them if the pilot holds its numbers until September. That is claim 7: directional, because it depends on the pilot holding up, but cash, because it has an owner, a date and a budget line.

Now test it the way finance will. Two full-time temps give about 320 hours a month in the peak. The pilot frees about 109 net hours in a peak month. The date fix should take about half of the 247 WISMO hours a month away (about 120 hours) if it works as the portfolio expects. Together that is about 230 hours: enough to drop one temp, not yet two. Write it down as the case's most fragile assumption and test it at the first gate with measured numbers. If only one temp can go, the cash line is ₪48,000, not ₪96,000.

### Step 7 — Scenarios, discounting, payback and approval

Three scenarios, conservative first: **low** counts measured cash only; **expected** adds directional cash; **high** adds assumed cash. Discount each year's net cash at 12%: NPV = −build + Σ (cash − running) ÷ 1.12^t for years 1–3. In a spreadsheet: `=NPV(12%, C5:E5) + B5`, with year 0 in B and years 1–3 in C–E.

The Track B script `labs/module-03/roi_model.py` (module download) computes it; its output, run on 2 November 2026:

| Scenario | Cash a year | Capacity a year (not cash) | NPV at 12%, 3 years | Payback |
|---|---|---|---|---|
| Low (measured) | ₪17,000 | ₪73,740 | −₪196,859 | never |
| **Expected** (+ directional) | **₪113,000** | ₪73,740 | **₪33,717** | **22.5 months** |
| High (+ assumed) | ₪180,150 | ₪73,740 | ₪195,000 | 11.0 months |

Three-year cost ₪267,000: approval by the board.

The expected case clears the hurdle and pays back inside 24 months, by a small margin. Show the low case first: it tells the board that without the temps decision this pilot is a capacity investment, not a saving, and that is a legitimate thing to approve if they choose to.

### Step 8 — Show what breaks it

A sensitivity table is the answer to "what if you're wrong?" before anyone asks:

| What changes | Expected NPV | vs base |
|---|---|---|
| Base | ₪33,717 | — |
| Only one temp released (cash ₪65,000) | −₪81,571 | −₪115,288 |
| Translation contract kept in full | −₪7,114 | −₪40,831 |
| Running cost +25% | ₪4,295 | −₪29,422 |
| Build cost +25% | ₪3,717 | −₪30,000 |
| Token prices at US$2 / US$10 per million | ₪34,640 | +₪922 |
| 1.5% more wrong replies reach customers | −₪65,892 | −₪99,609 |
| Hurdle rate 15% | ₪26,126 | −₪7,591 |

Two assumptions carry the case: the temps and the error rate. Tokens do not. That tells you what the gates must test.

### Step 9 — Stage the money against yes/no conditions

Ronit releases money in stages. Split the ₪120,000 build so the first stage stays under ₪50,000 and buys the evidence for the rest:

- **Stage 1, February–March 2027, ₪48,000:** test set, evaluation harness, Olga's labelling, a read-only shadow-mode connection.
- **Gate 1, Thursday 1 April 2027 — all yes:** (a) on at least 400 real messages in Hebrew, Arabic, Russian and English, at least 80% of drafts accepted with no or light edits, and at least 70% in each language; (b) median review time measured at 2.5 minutes or less; (c) wrong replies reaching customers in the shadow sample no higher than today's measured rate; (d) the pilot's measured net hours at peak volume plus the date fix's measured WISMO reduction cover at least 320 hours a month. If (d) covers only 160, the case is re-presented with one temp before stage 2.
- **Stage 2, from April, ₪72,000:** full integration, training, contingency.
- **Gate 2, Thursday 30 September 2027:** the gate-1 numbers held from May to September; Samir and Michal confirm in writing that the November–January peak runs without temps.

### Step 10 — Have the conversation with finance before the paper

Walk Ronit through the model one to one before it goes anywhere. Start with the low case. Show the ₪1.36 million and where each shekel went. Say what you do not know ("the error rate is measured on a sample; gate 1 measures it properly"). Ask her to challenge the two lines that carry the case. A CFO who has found the weak points herself, and seen them turned into gates, signs; one who finds them in the board pack does not.

## Watch out

- **Hours presented as cash.** 109 hours a month is a real benefit and not a shekel of saving until a budget line changes. Label it capacity, every time.
- **Counting the same hours twice.** Time saved and salaries saved are the same hours. Count once, after netting.
- **Another project's benefit.** Ask what happens without your project. The WISMO drop happens anyway.
- **Revenue instead of margin, and the customer's money as your saving.** Count gross margin; count credits customers no longer receive at most at half until measured.
- **Forgetting the review.** The human check is what makes the pilot safe; it is paid in the same hours the claim counts.
- **A vendor's headline as an input.** Klarna announced in February 2024 that its AI assistant did the work of 700 full-time agents and would improve profit by US$40 million that year; by May 2025 its CEO was telling Bloomberg the company would hire human agents again because quality had suffered (as reported by Entrepreneur, 9 May 2025). A figure measured in someone else's business, at someone else's quality bar, is an assumption in yours.
- **Building outside finance's template.** A beautiful model in your own format will be re-typed by finance, and every assumption will be re-opened.

## Your turn

### Inputs

- The alignment page from [03.6](lesson-06.md); the portfolio cards from [03.4](lesson-04.md).
- Data room (module download, `labs/common/harbor-and-pine/`): `company/finance-summary.md`, `company/finance-summary.csv`, `people/headcount.csv`, `people/timesheets.csv`, `documents/roadmap-previous-consultant.md`.
- Persona: [Ronit Avraham, CFO](../../labs/common/harbor-and-pine/personas/ronit-cfo.md); no roleplay: her [pre-run transcript](../../labs/common/harbor-and-pine/personas/transcripts/ronit-cfo.md). Feedback: [coach prompt](../../labs/common/coach-prompt.md).
- Simulations: [pilot economics](../../simulations/pilot-economics/index.html?preset=harbor), then [ROI defender](../../simulations/roi-defender/index.html?preset=harbor).
- Template: [ROI model](../../templates/roi-model.md); spreadsheet `labs/module-03/roi-model.csv` (module download).
- Track B: `labs/module-03/roi_model.py`.

### Steps

1. Interview Ronit (or read her transcript) for the template, the rules and the indicator she already reviews.
2. Build the monthly hours model (Step 2) in your spreadsheet; check it against the pilot-economics simulation.
3. List the costs (Step 3) and the three-year total; name the approver.
4. Net the seven claims across four ledgers with labels and classes (Step 4). Then play ROI defender and compare.
5. Price the expensive error (Step 5) and test the temps line against peak-month hours (Step 6).
6. Compute the three scenarios, NPV and payback (Step 7) and a sensitivity table of at least five lines (Step 8).
7. Write the stages and gates (Step 9) as yes/no conditions.

**Track B (Python).** Run `python roi_model.py` from `labs/module-03/`. Python is worth it here because the sensitivity table is eight versions of the same model: change one input in `INPUTS` or `CLAIMS` and every scenario, NPV and sensitivity line is recomputed in a second, and `--csv` writes the filled model for your spreadsheet. Add two sensitivity lines of your own (for example volume 2,600 a month, or automation 50%).

### Time

120 minutes: 20 with Ronit, 30 for the hours and costs, 30 for the netting and ROI defender, 25 for scenarios and sensitivity, 15 for the gates.

### Done when

- [ ] The model is in finance's structure: costs and benefits by year, three scenarios, NPV at 12%, payback, the approver for the three-year total.
- [ ] Review minutes and rework are costs in the model; tokens are a separate line with their price, model and date.
- [ ] Every claim is netted on four ledgers and labelled measured / directional / assumed and cash / capacity, with its source.
- [ ] No hours are counted as cash without a named plan, owner and date; nothing is counted twice.
- [ ] The expensive error is priced, and the two assumptions that carry the case are in the sensitivity table.
- [ ] The first stage is under ₪50,000 and every gate is a yes/no condition with a date.

<details><summary>Reference answer</summary>

**Harbor & Pine — reply-drafts pilot, business case in the finance template (draft for Ronit, 7 January 2027)**

*Costs (₪):* year 0 build 120,000 (stage 1: 48,000; stage 2: 72,000); years 1–3 running 49,000 a year (fixed 48,000 + tokens about 1,150 at the example prices; Claude Sonnet 5.5 list price US$2/US$10 per million on 2 Nov 2026 would make tokens about 770). Three-year total 267,000: **board approval** (above ₪150,000).

*Benefits after netting (₪ a year):* translation 17,000 (measured, cash, lands in Customer Service licences); temps 96,000 (directional, cash, lands in the Customer Service temp budget; owner Samir; decision 30 Sep 2027); goodwill credits 38,750 and repeat purchases 28,400 (assumed, cash, upside only); agent time 73,740 (measured on a sample, **capacity**, not cash); "two fewer agents" and the WISMO drop: 0 (double count; another project).

*Scenarios at 12% over 3 years (from `roi_model.py`):* low −₪196,859 (never pays back); **expected ₪33,717, payback 22.5 months**; high ₪195,000, payback 11.0 months.

*Monthly economics at peak (pilot-economics):* 1,920 drafts, 204.8 hours saved, −64 review, −32 rework = 108.8 net hours (about 0.6 of a person); ₪10,048 a month of capacity value after ₪4,096 running cost; breakeven 11.9 months in capacity terms. Breakeven accuracy 61.4%; at most 4.4 review minutes per draft before the pilot is worth nothing.

*The two assumptions that carry the case:* (1) both temps released: one temp only → NPV −₪81,571; (2) the error rate: 1.5 points more wrong replies reaching customers → NPV −₪65,892. Tokens: +₪922 at the lower list price. Translation kept in full → −₪7,114.

*Peak-month test of the temps line:* two temps ≈ 320 hours a month; pilot ≈ 109; date fix ≈ 120 (half of 247 WISMO hours, to be measured from January). Together ≈ 230: one temp covered, the second not yet. Gate 1 (d) tests it with measured numbers.

*Stages and gates:* as in Step 9.

*The sentence for the case's front page:* "Expected value ₪113,000 a year in cash plus about 109 freed agent-hours a month at peak; NPV ₪33,700 at 12% and payback 22.5 months, resting on one decision Samir and Michal have signed (no temps next peak) and on an error rate that gate 1 measures before most of the money is spent."

**What Ronit is likely to push on, and your answer:** "Why is claim 1 measured?" — timed on 400 real emails, so measured on a sample; gate 1 measures it in shadow mode. "Where does the 109 hours go?" — nowhere in cash, except the temps; the rest is capacity for the volume that has doubled since May. "What if the date fix doesn't halve WISMO?" — then gate 1 (d) fails, and you come back with a one-temp case before stage 2 is spent.

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting), course 5 "AI Business Cases and ROI Models" (net the claim, the customer's share, gate placement as a cost line, discounting, staged investment; named, not re-taught).
- Anthropic, [Claude pricing](https://claude.com/pricing) (API prices checked 2 Nov 2026; check your own provider's page before you quote a cost).
- Klarna, [press release of 27 Feb 2024](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/); Entrepreneur, [Klarna is hiring customer service agents after AI couldn't cut it](https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396) (9 May 2025).
- Simulations: [pilot economics](../../simulations/pilot-economics/index.html?preset=harbor), [ROI defender](../../simulations/roi-defender/index.html?preset=harbor).
- Template: [ROI model](../../templates/roi-model.md). Persona: [Ronit Avraham](../../labs/common/harbor-and-pine/personas/ronit-cfo.md).
- Next: [03.8 · The roadmap](lesson-08.md). Later: measuring the value in the pilot (lesson 05.1) and evaluating it (05.4).
