# Baselines, shortlist and one-page case — Northwind Outfitters

Expert deliverable for lesson 08.3, presented at the phase-1 readout on Thursday 26 November 2026.
Templates: [opportunity map](../../../templates/opportunity-map.md), [use-case
scorecard](../../../templates/use-case-scorecard.md), [ROI model](../../../templates/roi-model.md),
[decision-ready case](../../../templates/decision-ready-case.md). Company figures = extract × 100.
Exchange rate ₪3.136 per US$ (Bank of Israel representative rate, 2 November 2026). Fully loaded agent
₪13,800 a month ≈ ₪88 an hour (157 paid hours).

## 1. Baseline sheet (Q3 2026 unless stated)

| Measure | Value | Label | Definition |
|---|---|---|---|
| Agent contacts a month | ≈ 39,500 | measured | Rows in `contacts.csv`, Jul–Sep ÷ 3 × 100 |
| Orders delivered a month | ≈ 67,300 | measured | KPI report, Q3 average |
| Contacts per 100 orders (agents only) | 58.7 (Q2 50.7) | measured | The report's own definition |
| Repeat-contact rate | 32.1% (1 May – 14 Jun: 17.2%) | measured | Same customer, same order (normalised) or blank, within 7 days |
| AHT like for like | 8.9 min (before 15 Jun: 7.9) | measured | Handling + after-contact work, mean |
| Returns-family share of agent contacts | ≈ 45% (38–54%) | directional | Tag 37.5%; written-ticket labels 53.5% |
| Refund-status share | ≈ 12% | directional | Written-ticket labels (241 of 2,000); the helpdesk category cannot say |
| Card refund, request → paid | median 17 days | measured | `returns.csv`, card refunds |
| Chatbot "resolved" followed by an agent contact in 7 days | 64.1% | measured (logged-in only) | `bot-sessions.csv` joined to `contacts.csv` |
| Cost of a truly resolved chatbot chat | ≈ ₪14 | directional | October bill US$9,900 ÷ (6,000 × 36%) × 3.136 |
| Cost of an agent chat | ≈ ₪13 | directional | 8.9 min × ₪88/h |
| Returns tickets answered consistently with the terms | 55.6% | measured | Test set, labelling team's coding |

## 2. Opportunity map and fast screen (summary)

| # | Candidate | Type | Screen | Why |
|---|---|---|---|---|
| A | One lawful returns policy, everywhere (page, terms, club, SOP, macros, bot) | Policy, no AI | **Go** | Root cause of about half the contact; legal exposure |
| B | Refund clock: inspection in 2 days, daily refund run, refund-status SMS | Process + plain automation | **Go** | ~10% of contacts are "where is my refund" |
| C | Chatbot restricted to order status, hand-over for returns and money | Configuration | **Go** | Stops wrong policy statements; lowers billed resolutions |
| D | Agent-assist drafts for written contact (rules decide, LLM drafts, agent sends) | Generation | **Go with a condition**: only after A is drafted with counsel | Consistency in four languages; modest hours |
| E | Extend the chatbot to returns, refunds and WhatsApp (the stated ask) | Customer-facing generation | **Stop** | Would state a policy that is being rewritten; 64% of "resolved" chats come back; cost per true resolution above an agent's |
| F | Arabic and Russian in the chatbot | Vendor feature | Not now | Vendor date Q3 2027 at the earliest |
| G | Repeat-contact KPI and definition owners | BI, no AI | **Go** | Without it, no claim can be checked |

## 3. Directional effect of A + B (assumptions labelled)

| Contact type (share in the 2,000 written tickets) | A month (× 39,500) | Assumed reduction | Avoided a month |
|---|---|---|---|
| Refund status (12.1%) | 4,780 | 70% (refund clock + SMS) | 3,350 |
| Fee or credit dispute (5.6%) | 2,190 | 70% (lawful fee, money back) | 1,530 |
| Returns-policy question (7.7%) | 3,020 | 50% (one clear page) | 1,510 |
| Complaints and legal threats (2.1%) | 810 | 50% | 405 |
| **Total** | | | **≈ 6,800 (17% of agent contacts)** |

At 8.9 minutes: ≈ 1,000 agent-hours a month, about 6 agents' paid time, worth ≈ ₪89,000 a month **as
capacity, not cash** (Boris's rule: a saving needs a named plan). Shares come from the labelling team's reading of the 2,000 written tickets, applied to all agent
contacts (directional: phone may differ); the reductions are assumptions to be measured after launch.

**The other side of the ledger (for Boris, labelled).** Measured in the extract: 252 of 380 non-defect
refunds carried a 10% handling fee, each above the 5%/₪100 cap (≈ ₪1.4M a year company-wide); 62 of
137 defect-coded refunds had a deduction (≈ ₪0.4M); ₪39 shipping deductions ≈ ₪2.3M a year (a question
for counsel and a business choice). If store credit becomes the customer's option, part of the ≈ ₪2.6M
a year breakage goes (assumed: half). Whether these deductions are lawful is counsel's call; the case
shows them so nobody discovers them later.

## 4. One-page case (front page)

**Decision asked of the steering group on 3 December:** approve phase 2 on the basis that Northwind
fixes the returns policy (A) and the refund clock (B) first, restricts the chatbot (C), and tests
agent-assist offline (D); stop work on extending the chatbot to returns (E).

**Why now:** the Verbalo renewal notice is due 1 April; the board approves a 2027 budget in late January
that assumes 21 agents from April on evidence that does not hold; Black Friday is in 24 hours.

**What it costs:** A: counsel's time and marketing; B: two returns clerks back (≈ ₪21,000 a month) and an
SMS job (≈ ₪40,000 one-off); C: nothing; D: within the ₪60,000 tooling budget for the offline test.

**What it does not do:** it does not halve support by Q2. The honest range for 2027 is fewer contacts
per order and a smaller team through attrition, measured monthly, with the gate in April.

**Labels:** measured: repeat rate, AHT, refund time, bot recontact, consistency today. Directional:
returns share, cost per true chatbot resolution. Assumed: every reduction percentage.
