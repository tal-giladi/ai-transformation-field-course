---
id: "08.3"
module: 8
minutes: 18
practice_minutes: 150
prerequisites: ["08.2", "03.1", "03.3", "03.7", "03.9"]
objectives:
  - "Build a baseline sheet whose every number has a definition, a source and a label, including the ones the client never measured."
  - "Map and screen Northwind's candidates, including the CEO's, and name the one that is plain policy work, not AI."
  - "Net the case the way the CFO will: capacity vs cash, the cost per truly resolved chat, and the income a fix gives up."
  - "Write a one-page case with one decision asked, its cost, what a no means and what it does not promise."
volatility: implementation
sources:
  - title: "Bank of Israel, representative exchange rate API (US$ = ₪3.136, 2 November 2026)"
    url: https://boi.org.il/PublicApi/GetExchangeRate?key=USD
  - title: "Claude pricing: Sonnet 5.5 US$2 / US$10 per million input / output tokens (checked 2 November 2026)"
    url: https://claude.com/pricing
  - title: "Klarna press release, 27 February 2024: AI assistant handles two-thirds of customer service chats in its first month"
    url: https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/
  - title: "Fortune, 9 May 2025: Klarna CEO says cost was 'a too predominant evaluation factor', leading to 'lower quality'"
    url: https://fortune.com/2025/05/09/klarna-ai-humans-return-on-investment/
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): fast screen, net the claim, decision-ready case"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
last_verified: "2026-11-02"
---

# 08.3 · Diagnosis

The CEO wants the chatbot to take half of support; your memo says returns drive half the contact. Before the 26 November readout you have to turn that into something the CFO can put a number on and the CEO can tell a board. In this lesson you build the baseline sheet, map and screen the candidates (the CEO's included), net each claim the way finance will, and write the one-page case. At the end you have a shortlist with measured baselines and a case that asks for one decision.

## The situation

Monday 23 to Thursday 26 November 2026, the week of Black Friday. The findings memo is drafted (08.2). On 12 November Boris Kaplan, the CFO, told you how he judges cases: hurdle rate 14%, payback under 18 months preferred, the CEO approves up to ₪250,000 over a project's life and the board above that, headcount savings only with a named plan and date, "capacity freed is not a saving", exchange rate at the Bank of Israel representative rate on the day. And, once you had asked about credit notes: about 12% of credit-note value is never redeemed within two years, roughly ₪3M a year of income. Read [his transcript](../../labs/module-08/personas/transcripts/boris-cfo.md) or interview [Boris](../../labs/module-08/personas/boris-cfo.md).

The 2027 draft budget already assumes the CEO's plan: customer service ₪6.09M against ₪8.95M in 2025, 21 agents from April. If it does not happen, Boris needs about ₪1.3M from somewhere else.

This is module 3's method on a live, contested case: the [opportunity map](../module-03/lesson-01.md), [agent or not](../module-03/lesson-02.md), the [fast screen](../module-03/lesson-03.md), the [ROI model](../module-03/lesson-07.md) and the [decision-ready case](../module-03/lesson-09.md). IBM's consulting certificate calls the core move *net the claim*; at Northwind there are two claims to net, the CEO's and your own.

## What to do

### Step 1 — The baseline sheet: one row per number, with its label

Use the [data profile](../../templates/data-profile.md) and the baseline method of [02.4](../module-02/lesson-04.md). Every row: value, definition, source, label. Company figures are the extract × 100. Exchange rate ₪3.136 per US$; an agent costs ₪13,800 a month fully loaded, about ₪88 an hour (157 paid hours).

| Measure | Value | Label |
|---|---|---|
| Agent contacts a month (Q3) | ≈ 39,500 | measured |
| Contacts per 100 orders, agents only | 58.7 (Q2 50.7) | measured (narrow definition) |
| Repeat-contact rate | 32.1% Q3; 17.2% 1 May – 14 June | measured |
| AHT like for like | 8.9 min (7.9 before 15 June) | measured |
| Returns-family share of agent contacts | ≈ 45% (tag 37.5%; written tickets 53.5%) | directional |
| Card refund, request → paid | median 17 days | measured |
| Bot "resolved" followed by an agent contact in 7 days | 64.1% (logged-in) | measured, with limits |
| Today's returns replies consistent with the terms of sale | 55.6% (test tickets, n = 691) | measured (by the labelling team) |

The written-ticket share comes from 2,000 tickets two agents per language labelled for the pilot (08.5); it is the best reading of "what is this contact about?" Northwind has, because the helpdesk's category field puts 19% in "General" or blank.

### Step 2 — Map the candidates, including the one you were hired for

Three feeds ([03.1](../module-03/lesson-01.md)): the stated ask, what the data says, and what people asked for in interviews. Then decide per candidate, step by step ([03.2](../module-03/lesson-02.md)), whether it is plain policy or automation, generation, an agent, or a person:

| # | Candidate | Feed | Type |
|---|---|---|---|
| A | One lawful returns policy everywhere: page, terms, club terms, SOP, macros, bot | Data, Nadia, Meseret | **Policy, no AI** |
| B | Refund clock: inspection in 2 days, daily card-refund run, an SMS at inspection and at payment | Data, Orly | **Process + plain automation** |
| C | Bot limited to order status; hand-over for returns and money | Data | Configuration |
| D | Agent-assist: rules decide, an LLM drafts in the customer's language, an agent sends | Data, Nadia ("if it writes Arabic like a person") | Generation with a human sender |
| E | The bot on returns, refunds and WhatsApp (the stated ask) | Gil | Customer-facing generation |
| F | The bot in Arabic and Russian | Meseret | Vendor feature |
| G | A repeat-contact KPI with owners for every definition | Data, Alexei | BI, no AI |

Candidate A is the Harbor & Pine lesson again in a different costume: the most valuable item on the list contains no AI. Say so on the map.

### Step 3 — Screen each one, with the data gate

Run the seven questions of [03.3](../module-03/lesson-03.md) and write go, go with a condition, or stop. The ones that need care:

- **E, the bot on returns: stop.** It fails the data gate (the "data" it would answer from is four contradicting policies), the error-cost question (each wrong answer is a statement to a consumer about cancellation rights, and the claims log already has an Authority inquiry about one), and the evidence question (64% of its resolved chats come back; no evaluation exists).
- **D, agent-assist: go with a condition.** The condition is A: a draft that faithfully repeats the old policy is worse than no draft. Write the condition into the screen, with a date.
- **F, Arabic and Russian in the bot: not now.** The vendor's date (Q3 2027 at the earliest) is the gate.

### Step 4 — Net the CEO's claim

The claim: "half of support by Q2". Put it through the four ledgers of [03.7](../module-03/lesson-07.md) with Northwind's numbers:

- **The vendor's ledger.** Containment 63% sounds like 63% fewer chats. October: 6,000 billed resolutions, US$4,800 + 6,000 × US$0.85 = US$9,900 = ₪31,046. If 64.1% come back, about 2,150 chats were truly resolved: **≈ ₪14.4 per truly resolved chat, against ≈ ₪13.0 for an agent chat** (8.9 minutes at ₪88 an hour). Directional, because the recontact rate is measured on logged-in customers only.
- **The receiving team's ledger.** The contacts the bot did not resolve come to agents later, often angrier: repeat contacts 17% → 32%.
- **The control ledger.** Nobody reviews what the bot says about refunds; making it safe for returns would need review capacity nobody has budgeted.
- **The customer's ledger.** 121 of 439 sessions in a language the bot does not speak.

Then the public record, which the CEO will have read. In February 2024 Klarna announced that its AI assistant handled two-thirds of its customer-service chats in its first month, the equivalent work of 700 full-time agents, with repeat inquiries down 25%. In May 2025 its CEO told Bloomberg (reported by Fortune) that cost had been "a too predominant evaluation factor" and that the result was lower quality, and Klarna began recruiting so customers could always reach a human. Use it carefully: it shows that a bold containment claim can be followed by a quality correction, not that Northwind's bot will fail. Your case rests on Northwind's own numbers.

### Step 5 — Net your own claim, including what the fix gives up

The policy-first package (A + B) has a value and a cost, and the CFO knows part of the cost better than you do.

**Value, as capacity** (`case_model.py`; shares directional, reductions assumed):

| Contact type (share of written tickets) | A month | Assumed reduction | Avoided |
|---|---|---|---|
| Refund status (12.1%) | 4,780 | 70% | 3,346 |
| Fee or credit dispute (5.6%) | 2,212 | 70% | 1,548 |
| Returns-policy question (7.7%) | 3,042 | 50% | 1,521 |
| Complaint or legal threat (2.1%) | 830 | 50% | 415 |
| **Total** | | | **≈ 6,830 (17%)** |

≈ 1,013 agent-hours a month, ≈ ₪89,000 of capacity: about six agents' paid time. Capacity, not cash, until someone decides what it is for (Boris's rule).

**Cost, including the income Northwind gives up** (measured in the extract, scaled to a year): handling fees above the 5%/₪100 cap ≈ ₪1.4M; deductions on defect returns ≈ ₪0.4M; ₪39 shipping deductions ≈ ₪2.3M (a business choice once counsel has spoken); part of ≈ ₪2.6M credit-note breakage if store credit becomes the customer's choice. Plus two returns clerks (≈ ₪252,000 a year) and an SMS job (≈ ₪40,000 once).

This is the honest shape of the case: the fix costs Northwind income it has been collecting under a policy that contradicts its own terms. The case does not call that income unlawful (counsel decides); it shows it, so that nobody discovers it in April.

**Track B (Python).** `python case_model.py` in `labs/module-08/` prints the three calculations above from one block of inputs. Python is worth it here because the CFO will change every assumption in the meeting ("what if refund status falls by only 40%?"), and you want the answer in seconds, from the same model, with the labels intact.

### Step 6 — Write the one-page case

Use the [decision-ready case](../../templates/decision-ready-case.md) from [03.9](../module-03/lesson-09.md). One decision, in words that can be minuted; why now; what it costs; what a "no" means; what it does **not** promise; the labels. The sentence the CEO will look for is the last one: what replaces "half by Q2". Give him one he can say to the fund: fewer contacts per order and a smaller team through attrition, measured monthly, gated in April.

Before the readout, take the case to Gil privately (the [Gil persona](../../labs/module-08/personas/gil-ceo.md); the conversation that finally happened on 1 December is in [his transcript](../../labs/module-08/personas/transcripts/gil-ceo.md)). Start with his own question from the fund's director, "how is containment measured, and do customers come back?", because you now have the answer.

## Watch out

- **One returns share.** 33%, 38% and 54% are three readings of the same thing. Show the range and say which you trust and why.
- **Capacity in the cash column.** Six agents' time is not ₪1.07M a year saved unless someone decides to hire six fewer people. Boris will strike it out, and he will be right.
- **Hiding the income the fix gives up.** If the steering group learns about breakage and fees from the CFO in the room, your case dies. Put it on the page.
- **Fighting the stated ask with an anecdote.** Klarna is context; the ₪14.4 versus ₪13.0 is evidence. Lead with Northwind's numbers.
- **Killing the AI for the sake of it.** Agent-assist survives the screen, with a condition. A case that says "no AI" when the evidence says "AI after the policy" is as biased as the CEO's.
- **No sentence for the CEO.** A case that only says what not to do leaves him with nothing to tell the board, and he will go back to the vendor's.

## Your turn

### Inputs

- Your findings memo (08.2) and the data room (module download).
- Persona: [Boris Kaplan](../../labs/module-08/personas/boris-cfo.md) or [his transcript](../../labs/module-08/personas/transcripts/boris-cfo.md); [Gil Shachar](../../labs/module-08/personas/gil-ceo.md) or [his transcript](../../labs/module-08/personas/transcripts/gil-ceo.md).
- Templates: [opportunity map](../../templates/opportunity-map.md), [use-case scorecard](../../templates/use-case-scorecard.md), [ROI model](../../templates/roi-model.md), [decision-ready case](../../templates/decision-ready-case.md).
- Track B: `labs/module-08/case_model.py`.


### Steps

1. Build the baseline sheet: at least eight rows, each with definition, source and label.
2. Map at least six candidates with their feed and type; mark the one that contains no AI.
3. Screen each candidate; give a reason and, for any "go with a condition", the condition and its date.
4. Net the CEO's claim across the four ledgers with Northwind's numbers.
5. Net your own: capacity avoided (with your own assumed reductions) and the income the fix gives up.
6. Write the one-page case and the sentence the CEO can say to the board.
7. Interview Boris (or read the transcript) and change one thing in your case because of what he said.

**Track B (Python).** Change the assumed reductions and the agent-assist inputs in `case_model.py` to your own and keep the printout as the case's appendix.

### Time

150 minutes: 30 for the baseline sheet, 30 for the map and the screen, 45 for netting, 30 for the case, 15 for Boris.

### Done when

- [ ] Every baseline number has a definition, a source and a label; the returns share is a range with a reason.
- [ ] The map has a candidate with no AI in it, marked as such.
- [ ] The CEO's ask is screened with reasons from Northwind's data, and the screen says what would change the verdict.
- [ ] Capacity and cash are in different columns; the income the fix gives up is on the page.
- [ ] The one-page case asks one minutable decision, says what a "no" means and what it does not promise.
- [ ] There is a sentence for the CEO to say to the board.

<details><summary>Reference answer</summary>

The full set is `labs/module-08/expert/03-baselines-and-shortlist.md` in the module download.

**Screen.** A one returns policy: go. B refund clock: go. C bot to order status only: go. D agent-assist: go with a condition (policy v2 drafted with counsel by 17 December). E bot on returns, refunds, WhatsApp: **stop** (fails the data gate: four contradicting policies; error cost: statements on cancellation rights; evidence: 64.1% of resolved chats come back, no evaluation). F Arabic/Russian bot: not now (vendor date). G repeat-contact KPI: go.

**Netting the CEO's claim:** ≈ ₪14.4 per truly resolved chat vs ≈ ₪13.0 for an agent chat (directional); repeats 17.2% → 32.1% (measured); 121 of 439 chats in a language the bot does not speak (measured).

**Our claim:** ≈ 6,830 contacts a month avoided (assumed reductions on directional shares) ≈ 1,013 agent-hours ≈ ₪89,000 a month of capacity, not cash. Income given up, measured in the extract and scaled: fees above the cap ≈ ₪1.4M a year, defect deductions ≈ ₪0.4M, shipping ≈ ₪2.3M (business choice), part of ≈ ₪2.6M breakage. Costs: two returns clerks ≈ ₪252,000 a year, SMS job ≈ ₪40,000 once.

**One-page case, front:** *Decision asked on 3 December:* approve phase 2 on the basis that Northwind fixes the returns policy and the refund clock first, limits the chatbot to order status, and tests agent-assist offline; stop work on extending the chatbot to returns. *Why now:* Verbalo renewal notice 1 April; the January board approves a budget built on 21 agents from April. *What a no means:* the bot keeps stating returns rules Northwind's terms contradict. *What it does not do:* halve support by Q2. *For the board:* "Our returns policy, not the bot, drives about half our contacts. We are fixing it, measuring cost per order monthly, and the team will get smaller through attrition, gated in April."

**What changed after Boris:** cost per order became the headline measure, and the breakage line moved from the appendix to the front page.

</details>

## References

- Bank of Israel, [representative exchange rate](https://boi.org.il/PublicApi/GetExchangeRate?key=USD), ₪3.136 per US$ on 2 November 2026; Anthropic, [Claude pricing](https://claude.com/pricing) (checked 2 November 2026).
- Klarna, [press release of 27 February 2024](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/) and Fortune, [9 May 2025](https://fortune.com/2025/05/09/klarna-ai-humans-return-on-investment/): a public containment claim and its later quality correction.
- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting): fast screen, net the claim, decision-ready case (named, not re-taught).
- Field kit: [03.1 · The opportunity map](../module-03/lesson-01.md), [03.2 · Agent or not](../module-03/lesson-02.md), [03.3 · The fast screen](../module-03/lesson-03.md), [03.7 · The ROI model that survives finance](../module-03/lesson-07.md), [03.9 · The decision-ready case](../module-03/lesson-09.md).
- Templates: [data profile](../../templates/data-profile.md), [opportunity map](../../templates/opportunity-map.md), [use-case scorecard](../../templates/use-case-scorecard.md), [ROI model](../../templates/roi-model.md), [decision-ready case](../../templates/decision-ready-case.md).
- Earlier: [08.2 · Discovery](lesson-02.md). Next: [08.4 · The hard part](lesson-04.md).
