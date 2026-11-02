# Northwind Outfitters — writer's notes for module 08 (never imported)

The first Stage 2 engagement. The learner runs the whole method once more, this time as an **outside
consultant** on a 10-week fixed-fee engagement, in an organization almost four times the size of Harbor
& Pine, where the decision they were hired to support (replace half of support with a chatbot) has
already been half-taken. The data room is in `labs/module-08/data-room/` (built by `generate.py`, seed
20261108); the pilot files are in `labs/module-08/pilot/`. Ground truth for the answer key is in
`curriculum/engagements/module-08-answer-key/` (`python generate.py --answer-key <dir>`); never link it
from lessons.

## The company

- **Northwind Outfitters Ltd.** (נורת'וינד אאוטפיטרס בע"מ), founded 2012, online retailer of outdoor and
  sports gear. Website and app; no shops. 450 employees (head office in Petah Tikva, fulfilment centre in
  Modi'in industrial zone). Revenue ₪548M (2025). About 60,000 orders a month, average basket ₪760;
  peaks before Passover, July–August, before Sukkot, Black Friday (27 November 2026). A private-equity
  fund (Galilee Growth Partners) holds 35% and two board seats.
- Customer languages (2,000-ticket labels): Hebrew 68%, Arabic 13%, Russian 10%, English 7%, Amharic 0.6%.
- Customer Service: in-house team in Petah Tikva. **42 agents in June 2026; 30 by September** (12 fewer:
  6 contracts not renewed in July "automation plan", 3 in August, 3 resignations not replaced). Six team
  leads, one head. Channels: phone, email, web form, WhatsApp (in the helpdesk since 2024), web chat
  (agents until 15 June; since then the bot first).
- Systems (fictional): helpdesk "Tikra"; the OMS; the chatbot "Verbalo AI" (Verbalo Ltd., Tel Aviv
  office of a UK company); BI; finance ERP that pays card refunds in a weekly Thursday run.
- Loyalty: Trail Club (free; 30-day "hassle-free returns" in the club terms) and Silver Trail (its 65+
  tier).

## Who the learner is, and what changes from Harbor & Pine

Orly Ben-David (COO) hired the learner as an **independent consultant**: 10 weeks, Sunday 8 November
2026 – Thursday 14 January 2027, fixed fee in three exitable phases (₪72,000 diagnose, weeks 1–3;
₪126,000 decide and build, weeks 4–9; ₪24,000 readout and handover, week 10; ₪222,000 + VAT), paid
from the COO's budget, pilot tooling up to ₪60,000. Reports to Orly; the steering group is the CEO,
COO, CFO, head of customer service, counsel and the head of IT & BI.

What changes for an outsider (08.1, pointing to 01.1): no line authority, influence only through the
sponsor; exit points written into the statement of work; access by agreement (NDA, data-processing
agreement, pseudonymised extracts, no live systems); independence is the product but the client can stop
at each gate; the sponsor is not the person with the ask (the CEO is) and the CEO may see the consultant
as the COO's weapon; the clock is the contract; the exit is a handover to a named internal owner.

## Stated ask vs hidden truth

- **Stated ask (CEO Gil Shachar):** "A chatbot that replaces half of support by Q2 2027." Board, 21 Sep:
  bot live, containment above 60%, handling time down 30%, headcount 42 → 30, ₪2.0M annualised saving,
  support cost halved by Q2 by putting the bot on returns, refunds and WhatsApp. 2027 draft budget
  ₪6.09M (21 agents from April) against ₪8.95M in 2025.
- **Hidden truth.** The biggest driver of contact is the **returns policy**: about 45% of agent contacts
  (truth 47%) are returns, refunds, fees and exchanges, and they repeat. Northwind has four written
  answers to "can I return this and get my money back?" (returns page, terms of sale, Trail Club terms,
  warehouse SOP) and nine macros. The page and the warehouse practice (store credit for opened items,
  10% + ₪39, inspection that rejects "used" items) conflict with the terms of sale and with the Consumer
  Protection Law's rules on cancelling a distance sale (14 days from receipt; fee at most 5% or ₪100;
  money back within 14 days of the notice; no fee for defects, collected by the business; 4 months for
  65+, disability, new immigrants when the sale included a conversation). Refunds take a median 17 days
  (inspection backlog after two of four returns clerks were moved in July; weekly Thursday run).
- The chatbot **states the policy** to customers, sometimes the store-credit rule, sometimes "30 days,
  full cash refund" from the club terms (the Air Canada pattern). Its billed "resolution" is any session
  without a hand-over; about 64% of logged-in "resolved" sessions are followed by an agent contact within
  7 days. It answers Arabic and Russian in Hebrew.
- **The headcount was cut against an untested bot**; the KPI that "proves" it (AHT −30%) is a definition
  change made on 14 June, the day before launch. Like for like, handling time went *up* (7.9 → 8.9 min).
  Repeat contacts rose from 17% to 33%. Load per agent doubled (≈ 600 → 1,220 contacts a month).
- **The honest answer:** fix the returns policy first (one lawful policy with counsel), fix the refund
  clock, restrict the bot to order status with hand-over for returns and money (renegotiate the
  resolution definition, opt out of training before renewal), pilot **agent-assist** for written contact
  (rules decide, the LLM reads and drafts, a person sends), stop further cuts until the gate, and restate
  "half of support" as cost per order and repeat-contact rate.

## Planted findings (each discoverable, never stated)

| # | Finding | Where |
|---|---|---|
| 1 | Headcount cut against an untested bot | `people/cs-headcount-2026.csv`, `company/board-update-2026-09.md`, `vendor/verbalo-demo-deck.md` |
| 2 | Handling time down while repeat contacts rise | `support/contacts.csv` |
| 3 | Report definition changed near rollout | `company/kpi-report-2026-q2.md` vs `kpi-report-2026-q3.md` footnotes |
| 4 | Returns drive ~45% of agent contacts; refund lag; fees above the cap; store credit | `support/contacts.csv`, `orders/returns.csv`, `support/written-tickets-2000.csv` |
| 5 | Four written policies, nine macros | `policies/*.md`, `support/macros.csv` |
| 6 | The bot states the policy wrongly (Air Canada pattern) | `support/bot-sessions.csv`, `support/bot-transcripts-sample.md` |
| 7 | Demo on 40 curated English questions; "resolution" = no hand-over; billing counts abandons; no Arabic/Russian | `vendor/*`, `support/bot-sessions.csv` |
| 8 | Training on conversation data unless opt-out; contract never went to counsel | `vendor/verbalo-order-form.md` §7, `legal/contract-review-log.csv` |
| 9 | Legal exposure: review pending since March; Authority inquiries; demand letter 22 Sep | `legal/*.csv` |
| 10 | Steps on paper only: inspect in 2 days, refund in 14 | `policies/warehouse-returns-sop.md` vs `orders/returns.csv` |
| 11 | Missing baseline: repeat contacts never reported | `support/contacts.csv`, both KPI reports |
| 12 | 4-month right ignored | `orders/orders-sample.csv`, `customers/customers-sample.csv`, `written-tickets-2000.csv` |
| 13 | Arabic and Russian customers repeat more; bot fallback | `support/contacts.csv`, `support/bot-sessions.csv` |
| 14 | Credit-note liability growing; breakage income | `company/finance-summary.md` |
| 15 | Agents' unofficial exceptions doc | Nadia persona only |
| 16 | Refunds paid once a week (Thursday) | `orders/returns.csv` |

## The cast (persona pack)

| Persona | Role | Type | Hidden / unlock |
|---|---|---|---|
| Gil Shachar | CEO, co-founder | owner of the ask | The fund's director asked how containment is measured; the January review looks at customer service first; demand letter "kept quiet"; contract not reviewed. Unlock: what exactly he committed and what the fund will check; legal risks |
| Orly Ben-David | COO, sponsor | sponsor | Moved two of four returns clerks in July; refunds take 2–3 weeks; sat on Hila's March memo. Unlock: what happens to a return / what she would fix without the bot |
| Boris Kaplan | CFO | sceptic | Likes store credit (breakage ≈ ₪3M a year, 12% never redeemed; liability ₪9.6M); didn't answer the memo; demand letter not provisioned. Unlock: credit notes; what is not in the budget |
| Meseret Tadesse | Head of Customer Service | middle manager | Asked BI to drop after-contact work from AHT (14 June); repeats up; ~26 agents actually on the floor. Unlock: non-attribution + how AHT is measured now vs May; floor vs payroll |
| Nadia Khoury | Senior agent, WhatsApp and Arabic desk | frontline | Exceptions doc (14 rules); two agents paste Arabic into a free translator. Unlock: the opened-tent question + no names; how non-Arabic speakers cope |
| Valentina Orlova | Customer, 68 | person affected | Sequence of 4 contacts; would accept money minus a small fee; robot fine for tracking, not for money. Unlock: let her tell it in order; ask what would have made it OK |
| Hila Rosen | Legal counsel | counsel | March memo; never saw Verbalo; demand letter view; open question whether a bot chat is a "conversation". Unlock: reviewed the page? reviewed the contract? |
| Daniel Brenner | Verbalo AE | vendor AE | Resolution definition; demo conditions; knowledge content contradictory and unreviewed; Arabic Q3 2027; would change the definition for 24 months. Unlock: exact measurement questions |
| Alexei Morozov | Head of IT and BI | data steward | Change log of 14 June; repeat measure in a day; Verbalo never joined to Tikra. Unlock: when did the formulas change |

Transcripts leave hidden: Orly's own view on the bot; Gil's demand letter and the unreviewed contract;
Boris's unprovisioned exposure; Meseret's real floor capacity; Nadia's translator use; Hila's open
question on bot chats and the four-month rule; Daniel's contradictory knowledge content and his
definition offer; Alexei's unchecked containment and the one-day repeat measure.

## Timeline

- Data: orders 15 Mar – 31 Oct 2026; contacts and returns 1 May – 31 Oct; bot sessions 15 Jun – 31 Oct;
  2,000 written tickets 1 Sep – 31 Oct.
- 12 May vendor demo; 19 May order form signed by Gil; 1 Jun term starts (notice by 1 Apr 2027); 14 Jun
  KPI definitions changed; 15 Jun bot live. July–September headcount 42 → 30. 21 Sep board. 22 Sep
  demand letter.
- Wed 4 Nov the call; Sun 8 Nov start (08.1); Mon 9 – Thu 19 Nov discovery (08.2; Valentina 18 Nov);
  Thu 26 Nov phase-1 readout (08.3; exit point 1); 27 Nov Black Friday; Mon 30 Nov Hila, Tue 1 Dec Gil,
  Wed 2 Dec Daniel; Thu 3 Dec decision paper (08.4; exit point 2); 7 Dec policy draft to Hila; 17 Dec
  counsel's mark-up = policy for the pilot; 18 Dec – 7 Jan pilot build and offline eval (08.5);
  Tue 12 Jan 2027 steering committee (08.6); Thu 14 Jan handover. Q2 2027 = Gil's deadline.
- Six months later: July 2027.

## The futures (08.6 debrief)

1. **Bot first.** Gil overrules; the bot gets returns and refunds by March. Billed resolutions rise,
   reported containment 70%, repeat contacts 38%. In May a customer posts a bot screenshot promising "30
   days, full cash refund"; the demand letter becomes a motion to certify a class action (June 2027); the
   Authority opens an inquiry. Northwind hires 8 temps for the summer at agency rates; two team leads
   resign. The bot is cut back to order status in July. Cost per order is higher than in 2025.
2. **Policy first, agent-assist (the expert path).** Policy v2 published 1 Feb after counsel; inspection
   in 2 days (two clerks back), daily refund run; bot limited to order status with hand-over; Verbalo
   renewed for 12 months with "resolution = no agent contact within 72 hours" and training opt-out.
   Agent-assist: shadow mode in February, live in Hebrew and English in March, Arabic and Russian in
   April after native review. By July: returns-family contacts −31%, repeat rate 19%, median refund 6
   days, no new hires (attrition covers the gap to 27 agents), cost per order −17% against 2025. Gil tells
   the board "half became a sixth, and it stuck". The demand letter settles with a refund programme for
   fees charged above the cap.
3. **Half-way.** Agent-assist approved, policy deferred "until after the peak". Drafts cite the old
   policies; acceptance looks good (agents accept what they would have written anyway); repeats don't
   move; the pilot is blamed and quietly stopped in June. The readout named the dependency; nobody owned it.

## Where each finding is planted (actual numbers)

Computed from the generated files (seed 20261108) with pandas; reproducible in a spreadsheet with
filters, pivots and lookups. "Sample" = BI's 1% customer extract; company figures = sample × 100.
*Truth* = answer key only. Paths relative to `labs/module-08/data-room/`.

**Volumes.** `customers/customers-sample.csv` 3,400 (regular 2,109, Trail Club 1,038, Silver Trail 253).
`orders/orders-sample.csv` 4,598 (web 3,254, app 1,059, phone 179, chat_assisted 106). `orders/returns.csv`
602. `support/contacts.csv` 2,075 (May 253, Jun 255, Jul 391, Aug 428, Sep 367, Oct 381).
`support/bot-sessions.csv` 439 (277 "resolved", 162 escalated; customer id present 60%).
`support/written-tickets-2000.csv` 2,000 (company-wide; he 1,367, ar 266, ru 208, en 147, am 12).

1. **Headcount.** 42 (Jan–Jun) → 36 (Jul, 6 not renewed) → 33 (Aug, 3) → 30 (Sep, 3 resignations not
   replaced). No test set or eval of the bot anywhere; only the vendor deck. Contacts per agent (× 100 ÷
   agents): ≈ 600 a month in May–June → 1,220 in Aug–Oct. Median first response, written: 2.6 h (May) →
   8.1 h (Sep); median phone wait 83 s (May) → 225 s (Oct).
2. **AHT down, repeats up.** Like-for-like AHT (handle + after-contact work) 7.9 min before 15 Jun → 8.9
   after; handle only after 15 Jun 5.6. Repeat contact (same customer, same order after normalising, or
   either blank, within 7 days of the previous contact): **17.2%** (1 May – 14 Jun, n = 379) → **32.1%** in
   Q3, 32.7% Jul–Oct; by month 14.2 / 28.2 / 30.4 / 33.2 / 32.7 / 34.4%. *Truth:* 9.2% → 28.0%.
3. **Definition change.** Q2 report AHT includes after-contact work, "customer contacts" = all; Q3 report
   AHT = handling only, "agent contacts", bot as containment. Q3: "AHT down 30%: 5.6 vs 8.0". Like for like
   Q3 = 8.9 (+12%). Contacts per 100 orders, narrow definition: 50.7 → 58.7; with bot conversations ≈ 75.
4. **Returns drive contact.** Category "Returns & refunds" 33.4% (+ "Damage / defect" 4.4%; "General"
   15.4%, blank 3.7%); tag `returns` 37.5%; *truth* 47.1%. In the 2,000 written tickets (labels): 53.5%.
   `returns.csv`: 318 card refunds, all on Thursdays; request → refund median **17 days** (p25 13, p75 22,
   p90 26), 66% over 14 days. Credit notes 199 of 517 refunds (38.5%). Deductions on 78.7% (handling fee
   48.7%, shipping 72.0%). Conservative reading (`reason_code` defect / not_as_described / late = defect):
   **252 of 380 non-defect refunds (66.3%) carried the 10% handling fee, every one above the 5%/₪100 cap**
   (median fee ₪54.90 vs cap ₪27.45); excess over the cap ₪9,004 in the sample; 62 of 137 defect-coded
   refunds (45%) had a deduction (₪2,418); shipping deductions ₪14,508 (counsel's question). Requests 15
   Mar – 31 Oct (7.5 months), so annualise × 160: excess fees ≈ ₪1.4M a year, defect deductions ≈ ₪0.4M,
   shipping ≈ ₪2.3M; credit notes issued ≈ ₪21.6M a year (12% breakage ≈ ₪2.6M). Finance: liability ₪9.6M (₪5.1M Dec 2025), 12% never
   redeemed; chargebacks 41 / 57 / 96.
5. **Policies and macros.** Page (14 days unopened, credit, 10% + ₪39); terms §9 (the law); club 5.2 (30
   days, refund); SOP (credit for opened, 10% + ₪39, 2 days, 14 days). Macros: MAC-031/032/052 credit;
   MAC-047/053 law; MAC-048 30 days full; MAC-060 "14 business days"; MAC-061 ship defects yourself.
6. **Bot states policy.** bot_intent `returns_policy` 151: hand-over 50, fallback 32, "30 days full cash" 26,
   store-credit 24, terms 19 → 50 of 69 policy answers (72%) contradict the terms of sale. Transcripts #1,
   #2 (30 days to a non-member; claims log 17 Aug), #3 (Valentina), #7 (personalised cap), #8 (68, phone).
7. **Vendor.** Deck: 62% on 40 English questions chosen with e-commerce (4 about returns/refunds, none
   with an exception). Resolutions billed: 2,500 / 6,600 / 6,000 / 6,600 / 6,000 (Jun–Oct), US$47,545 to
   October. Logged-in "resolved" sessions followed by an agent contact within 7 days: **64.1%** (n = 170;
   order status 48%, refund status 69%, returns policy 78%). Message language "other" 121 of 439 (28%).
   Thumbs down 95, up 45. Effective cost per truly resolved chat ≈ US$9,900 ÷ (6,000 × 0.36) ≈ US$4.6
   (₪14) vs an agent chat ≈ ₪13 (8.9 min at ₪88/h).
8. **Data use.** Order form §7; no Verbalo line in `contract-review-log.csv`.
9. **Legal.** LR-2026-011 "awaiting business decision" since 2 Apr (memo 24 Mar); claims log:
   inquiries (incl. Valentina, 29 Oct), 4 small claims (one ₪10,000), demand letter 22 Sep.
10. **On paper only.** Inspection median 3 business days before 1 Aug (35.8% within 2) → 8 after (0%).
11. **Missing baseline.** "Repeat-contact rate: not tracked"; only 1 May – 14 Jun in contacts.csv.
12. **4-month right.** Silver Trail orders: phone 54, chat_assisted 22 (of 344). 2,000 tickets: 17 with
    `refund_4m_verify` (13 in test). Today's agents never apply it.
13. **Languages.** Repeat rate after 15 Jun by detected language: he 29.0%, en 32.5%, ar 38.6%, ru 40.8%.
14. **Credit notes**: ₪9.6M; 12% never redeemed (≈ ₪3M a year at ≈ ₪27M issued).
16. **Thursday run**: every card refund date is a Thursday.

**The 2,000 tickets (08.5).** All 2,000: refund_minus_fee 379, refund_no_fee_pickup 211, outside_window
129, exchange_free 71, excluded_custom 22, refund_4m_verify 17, status_update 241, escalate_counsel 41,
n/a 889; escalate = y on 105. Split (`pilot/sets.py`, seed 20261218): dev 300, test 1,700, Track A 200
(he 100, ar 40, ru 35, en 25). **Rules baseline, test set** (real, `reports/rules-test-rules-today.md`):
intent 78.4% (ru 70.7, he 78.8, en 78.3, ar 81.7); decision, returns tickets (n = 691) **79.6%** (ru 72.6,
en 76.9, he 78.8, ar 91.3); all tickets 87.4%; right decision and fee 258 / 320 (80.6%); escalation recall
68.2% (58 / 85), precision 86.6%; draft language 88.8%; banned phrases 0. **Today:** 55.6% of returns
tickets match the policy; **32.7%** give the customer less than the law; 140 of 1,700 replies carry a
banned phrase. Dev rules: intent 80.3%, returns decision 81.2% (n = 138). Track A rules: intent 81.5%,
returns decision 80.0% (n = 80), today 61.3% / 26.2%. LLM and hybrid figures in 08.5 are an
illustrative worked example (no API key in the build).
