---
id: "04.8"
module: 4
minutes: 18
practice_minutes: 100
prerequisites: ["04.3"]
objectives:
  - "Read a vendor's headline claim under five measurement conditions (sample, definition of success, volume and task mix, oversight, time window) and name who chose them."
  - "Trace a statistic hop by hop to its source and judge whether its conditions fit the client's."
  - "Interview a vendor account executive and get the facts the deck leaves out, without letting the discount deadline set the timeline."
  - "Write a claim read-back and a proof-of-concept protocol on the client's own data, with success criteria fixed before results."
volatility: concept
sources:
  - title: "Bank of Israel — representative exchange rates (2 November 2026)"
    url: https://www.boi.org.il/en/economic-roles/financial-markets/exchange-rates/
  - title: "Regulation (EU) 2024/1689 (AI Act), Article 50(1): providers must ensure people are told they are interacting with an AI system — EUR-Lex"
    url: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689
  - title: "EBN Law — PPA draft AI guidance: explicit disclosure when people interact with a chatbot (draft)"
    url: https://www.ebnlaw.co.il/media-center/draft-guidance-from-the-israeli-privacy-protection-authority/
last_verified: "2026-11-02"
---

# 04.8 · Vendor and claim due diligence

A vendor's best number is usually true under conditions the vendor chose. Due diligence is finding those conditions and asking whether they are yours. In this lesson you read ChatNest's headline claims under five measurement conditions, trace each figure to its source, meet the account executive who sold the CEO the demo, and turn the result into a claim read-back and a proof of concept on Harbor & Pine's own data. At the end you have a decision the CEO can act on — test, under these conditions, before signing — instead of a list of doubts.

## The situation

It is Thursday 19 November 2026. Eitan Gross, ChatNest's account executive, has a video call with you this afternoon. Since the demo on 30 September, Yoav has told him he would "most likely sign in November"; the deck offers 15% off the platform fee if signed before 30 November. The previous consultant's roadmap (`documents/roadmap-previous-consultant.md`) already assumes the deck's 70% deflection.

You have read the deck as a vendor document in 04.3 (no DPA, US hosting, a customer-facing bot that is a restricted use). Now read it as a set of claims. You also know two things Eitan may not: about 38% of Harbor & Pine's written contacts are "where is my order?", caused by promised dates that are never updated (module 2), and most written contact arrives on WhatsApp, not the website (02.3).

IBM's consulting course teaches this as claim due diligence: measurement conditions, the interested party, hop-tracing, fit, an inspectable demonstration, and counterparty risk. It gives no read-back form or proof-of-concept protocol; this lesson adds both.

## What to do

### Step 1 — List the claims, one per line

Write down every claim that could move the decision, exactly as stated, with where it appears:

| # | Claim | Where |
|---|---|---|
| C1 | "70% of customer conversations fully resolved by ChatNest without an agent" | Slide 2, footnote 1 |
| C2 | "−45% customer service cost in the first year" | Slide 2, footnote 2 |
| C3 | "4.6 / 5 customer satisfaction with ChatNest conversations" | Slide 2, no footnote |
| C4 | "Tracks orders and tells customers when their delivery arrives" | Slide 3, footnote 3 |
| C5 | The demo "built on your own catalogue in 48 hours" | Slide 4, footnote 4 |
| C6 | "Go live in 4–6 weeks" | Slide 5 |
| C7 | "Answers in 30+ languages, including Hebrew, Arabic and Russian" | Slide 2 |

### Step 2 — Read each claim under five measurement conditions

For each claim, fill five headings. A blank heading is a finding, not a gap to fill with good will:

| Condition | C1: 70% resolved |
|---|---|
| **Sample** | ChatNest retail customers in the US and Canada |
| **Definition of success** | "Resolved" = the conversation ended **without a transfer to a human agent during the session** — not that the customer's problem was solved |
| **Volume and task mix** | English conversations; deployments **with live order-tracking integration** (Shopify or custom API) |
| **Oversight** | None in the session (that is the point of the metric) |
| **Time window** | January–June 2026 |

Then ask the **interested-party** question: who chose these conditions, and who gains if you accept them? The vendor chose the definition, the customers and the period. That does not make the number false; it makes it the vendor's number. Apply the same test to your own side: the CEO's "40% lower support cost" was also chosen by someone who gains if it is believed.

### Step 3 — Trace each number hop by hop

Follow every figure back until you reach a method or a dead end:

- **C1 (70%):** deck → footnote 1 → "measured across ChatNest retail customers…" → no report, no sample size, no repeat-contact measure. Dead end at the vendor's own analytics. Ask for the report.
- **C2 (−45%):** deck → footnote 2 → "customer-reported, based on a survey of 22 customers, 2025". It is a survey of what customers said, not a measurement — and of 22 customers out of "300+".
- **C3 (4.6/5):** deck → nothing. No source, no scale definition, no response rate. Not supportable until sourced.
- **C4 (order tracking):** footnote 3 — "Requires the order-tracking integration; without it, ChatNest answers order questions from the information in the order confirmation." At Harbor & Pine the order confirmation carries the promised date from the fixed lead-time table — the very date that is wrong for most delayed Vietnam and China orders (module 2). The demo's own answer shows it: "Estimated delivery: **the date shown in your order confirmation.**"
- **C5 (demo on your catalogue):** footnote 4 — file "received by email from Harbor & Pine marketing, 28 September 2026". Compare slide 4 with `catalog/products.csv`: the Oslo 3-seat sofa in grey is ₪4,990 today, not ₪4,290; the Bergen dining table 180 in oak (HP-DTB-1097) was discontinued on 1 August 2025. Both match the stale 2023 shared-drive copy. The demo was built on the wrong file, and nobody at either company checked.

The same discipline applies to circulated figures. The previous consultant's roadmap repeats "70% deflection" as an assumption; that is one hop further from the method, not a second source.

### Step 4 — Judge the fit between their conditions and yours

A claim can be true and still irrelevant. Put the two sets of conditions side by side:

| Condition | ChatNest's 70% | Harbor & Pine |
|---|---|---|
| Language | English | Hebrew about 60%, plus Arabic, English and Russian |
| Channel | Website chat | Mostly WhatsApp (630 conversations in the tallied week vs 94 helpdesk tickets) |
| Order tracking | Live integration | None; integration with Priority not quoted |
| Biggest contact reason | Not stated | "Where is my order?" ≈ 38%, caused by wrong promised dates |
| Success | No transfer in the session | Customer does not contact us again about the same order within 14 days (module 2's follow-up definition) |

Then rate each claim with one of three labels, and say what evidence would change it: **enough to act on**, **worth testing further**, or **not yet supportable**. For Harbor & Pine, C1 is *not yet supportable* here (different language, channel, integration and definition); C2 and C3 are *not yet supportable*; C4 is *contradicted* for delayed orders until the date fix and an integration exist; C5 is *contradicted* (stale data); C6 and C7 are *worth testing further*.

### Step 5 — Interview the account executive

The deck is the vendor's written case; the account executive knows the footnotes. Your goals for the call, in order:

1. The exact definition of the headline number and the conditions it was measured under.
2. What the bot would answer a customer whose container is ten days late, and what it would take to change that (integration, time, cost).
3. Results in Hebrew, Arabic and Russian, or the honest absence of them; a reference you can call.
4. Where the demo's data came from, and whether anyone checked it was current.
5. A proof of concept on Harbor & Pine's own data, with success criteria agreed before it starts.
6. Exit terms, and what happens if ChatNest is acquired or closes.
7. Do not let the discount set your timeline.

Two techniques make the difference with a confident salesperson: ask for the definition, not the number ("how exactly is 'resolved' counted?"); and ask for the behaviour in your case, not the capability ("what would it say to *this* customer, today?").

**Roleplay.** Paste [Eitan Gross's persona](../../labs/common/harbor-and-pine/personas/eitan-chatnest.md) into a new LLM chat and run the meeting (25–35 minutes). Afterwards, paste your transcript into the [coach prompt](../../labs/common/coach-prompt.md) with the persona's "After the interview" checklist. If you prefer not to roleplay, read the [pre-run transcript](../../labs/common/harbor-and-pine/personas/transcripts/eitan-chatnest.md) and list what the interviewer found and what they missed.

### Step 6 — Name the counterparty risk and the hedge

A twelve-month minimum term with a vendor founded in 2021 is a bet on that vendor being there and unchanged. Write it as one sentence and one hedge: "ChatNest is a five-year-old, venture-funded company; if it is acquired or fails during our term, our customer conversations and configuration depend on a 30-day JSON export and nothing else." Hedge: no signature before the proof of concept; if signed, a change-of-control exit right, a data export tested before go-live, no auto-renewal, and the drafts pilot (module 5) kept as the warm alternative.

### Step 7 — Write the claim read-back and the proof-of-concept protocol

The read-back is the deliverable: one page the CEO can read in two minutes, one row per claim, with the decision at the top ([claim read-back template](../../templates/claim-read-back.md)). The proof-of-concept protocol is the test that turns "not yet supportable" into evidence ([vendor proof-of-concept protocol](../../templates/vendor-poc-protocol.md)). Its rules:

- **The client's data, under the client's conditions:** a test set of Harbor & Pine's own past messages — all four languages, WhatsApp and email, including delayed-order cases — pseudonymised, under a signed DPA.
- **Success criteria fixed before results:** the definition of "resolved", the wrong-answer threshold, the per-language minimums, and the cost per resolved contact, signed by both sides before the vendor sees the data.
- **Inspectable:** the vendor shows intermediate steps (what it looked up, what it answered) on records you supplied, not a polished recording.
- **A fair comparison:** the same test set goes to the drafts pilot, so the decision compares two options on one yardstick.
- **Sequenced after the date fix:** testing "where is my order?" before customers receive real dates measures the wrong problem.

Israel first: if a bot ever answers customers directly, the Privacy Protection Authority's draft AI guidance (April 2025, still a draft) expects explicit disclosure that people are interacting with a bot (EBN Law's summary). For a provider whose bot reaches people in the EU, Article 50(1) of the AI Act puts that duty on the provider from 2 August 2026. Put both in the protocol's requirements and in any contract.

## Watch out

- **Arguing with the number.** "70% is impossible" loses the room. Ask for its conditions; the conditions do the arguing.
- **Accepting circulation as corroboration.** The roadmap repeating the deck's 70% is the same claim one hop further away.
- **Testing their demo instead of your data.** A demo answers "can it work under chosen conditions?"; you need "does it work under ours?".
- **Moving the goalposts after results.** Criteria written after the vendor's results are a negotiation, not a test.
- **Missing the question that matters most here.** At Harbor & Pine it is "what does it say to a customer whose order is late?" — the answer is the same wrong date.
- **Letting the discount deadline become your deadline.** It is the vendor's quarter end. Say so politely and keep your sequence.
- **Being unfair to the vendor.** Apply the same tests to internal claims (the CEO's 40%) and to your own pilot. Due diligence is symmetric.

## Your turn

### Inputs

- Data room (module download): `vendors/chatnest-sales-deck.md`, `catalog/products.csv`, `catalog/products-2023-shared-drive-copy.csv`, `documents/roadmap-previous-consultant.md`, `support/whatsapp-week-tally.csv`, `orders/orders.csv` ([INDEX](../../labs/common/harbor-and-pine/INDEX.md)).
- Persona: [Eitan Gross, ChatNest](../../labs/common/harbor-and-pine/personas/eitan-chatnest.md); [pre-run transcript](../../labs/common/harbor-and-pine/personas/transcripts/eitan-chatnest.md); [coach prompt](../../labs/common/coach-prompt.md).
- Your vendor review of ChatNest (04.3) and the drafts pilot's DPIA (04.4).
- Templates: [claim read-back](../../templates/claim-read-back.md), [vendor proof-of-concept protocol](../../templates/vendor-poc-protocol.md).

### Steps

1. List the deck's claims (Step 1) and fill the five conditions for each.
2. Trace each figure hop by hop. Check slide 4's prices and products against both catalogue files.
3. Fill the fit table against Harbor & Pine's conditions and rate each claim.
4. Prepare seven questions for Eitan, then run the roleplay (or read the transcript). Run the coach.
5. Write the counterparty sentence and the hedge.
6. Write the claim read-back (one page, decision first) and a proof-of-concept protocol with criteria fixed in advance.

### Time

100 minutes (35 for the roleplay and coach).

### Done when

- [ ] Every claim has its five conditions or a written "not stated".
- [ ] Each figure is traced to a method or to a dead end; the stale catalogue is shown with SKU and price.
- [ ] The fit table compares language, channel, order tracking, contact mix and the definition of success.
- [ ] You found out what the bot would answer to a delayed order and what changing that costs (or recorded that you did not ask).
- [ ] The read-back has a decision at the top and a rating per claim with the evidence that would change it.
- [ ] The proof of concept uses Harbor & Pine's data under a DPA, with criteria signed before results and the same test set for the drafts pilot.
- [ ] The discount deadline does not appear as a reason in your recommendation.

<details><summary>Reference answer</summary>

**What the pre-run transcript found and missed.** Found: the definition of "resolved" (no transfer in the session); the conditions (US and Canada, English, January–June 2026, order-tracking integration); two Israeli customers, both fashion, under six months, about 38% without transfer on the larger one (said by Eitan, unverified); the −45% is a 2025 survey of 22 customers; US hosting (EU only on Enterprise); JSON export within 30 days, no change-of-control clause; the demo built from the file marketing sent on 28 September. Missed: what the bot answers to a late order without the integration (the confirmation's original date) and what the Priority integration costs (Eitan would have said "typically 8–12 weeks and 60,000–120,000 shekels through a partner"); the paid proof of concept (four weeks, ₪25,000, credited if they sign — offered only if asked for one on their own data with criteria agreed in advance); that slide 4's prices are wrong (Eitan would have offered to rebuild it); any question on Arabic or Russian. Good moves: "I'm not here to negotiate today"; asking for the definition before the number; refusing to tie the decision to the 30 November discount.

**Claim read-back — ChatNest, 23 November 2026.**

*Decision:* do not sign by 30 November. Run a four-week proof of concept on our own data after the delivery-date fix is live and a DPA is signed, against the same test set as the drafts pilot; decide at the review group in February.

| Claim | Conditions | Fit to us | Rating | What would change it |
|---|---|---|---|---|
| 70% resolved without an agent | "No transfer in the session"; US/Canada; English; Jan–Jun 2026; with order-tracking integration | Language, channel, integration and definition all differ; their Israeli customer: about 38% (said, unverified) | Not yet supportable for us | Proof of concept: share of test conversations with no re-contact on the same order within 14 days and no wrong fact |
| −45% service cost | Survey of 22 customers, 2025, self-reported | Not a measurement | Not yet supportable | Measured cost per contact from a comparable deployment |
| 4.6/5 satisfaction | Not stated | — | Not yet supportable | Source, scale, response rate |
| Tracks orders | Only with integration; otherwise the confirmation date | For delayed orders it repeats the wrong date; Priority integration 8–12 weeks, ₪60–120k (said) | Contradicted for WISMO | Date fix live + integration quote after technical review |
| Demo on our catalogue | File from marketing, 28 Sep 2026 | Stale 2023 copy: Oslo sofa ₪4,290 vs ₪4,990; Bergen table discontinued Aug 2025 | Contradicted | Rebuild on `products.csv` |
| Live in 4–6 weeks | Catalogue and helpdesk only | Excludes order tracking and WhatsApp | Worth testing | Plan including WhatsApp and Priority |
| Hebrew, Arabic, Russian | "30+ languages" | No published results in our languages | Worth testing | Per-language results in the proof of concept |

*Counterparty:* founded 2021, Series B 2025, 12-month minimum, export in JSON within 30 days, no change-of-control clause. *Hedge:* proof of concept before any term; if signed, change-of-control exit, tested export, no auto-renewal; drafts pilot as the alternative. *Cost if signed:* ₪85,000 implementation + US$1,450 a month (₪64,380 a year at the finance planning rate of ₪3.70; ₪54,570 at the Bank of Israel rate of ₪3.136 on 2 November 2026) + US$0.45 per resolved conversation above 1,000 a month + integration — above ₪150,000 over three years, so a board decision.

**Proof-of-concept protocol (excerpt).** *Data:* 400 past written contacts from May–October 2026 (100 per language; at least 40% delayed-order cases; WhatsApp included once routed), pseudonymised, under a DPA with no training and deletion at the end. *Fixed before results, signed by both sides:* resolved = no re-contact on the same order within 14 days in a follow-up check, and no wrong fact (date, price, policy); hard limit: wrong-fact rate ≤ 2% overall and in every language; per-language resolution reported separately; bot discloses it is a bot in the first message. *Inspectable:* the vendor shows, for every test conversation, what it looked up and what it answered. *Comparison:* the same 400 contacts run through the drafts pilot (module 5). *Cost:* ₪25,000 for four weeks, credited if signed. *Start:* after the date fix is live and the DPA is signed.

</details>

## References

- Persona: [Eitan Gross](../../labs/common/harbor-and-pine/personas/eitan-chatnest.md) and the [pre-run transcript](../../labs/common/harbor-and-pine/personas/transcripts/eitan-chatnest.md); [coach prompt](../../labs/common/coach-prompt.md).
- EBN Law, [PPA draft guidance on AI systems](https://www.ebnlaw.co.il/media-center/draft-guidance-from-the-israeli-privacy-protection-authority/) — bot disclosure (draft); [AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689) Article 50(1).
- Bank of Israel, [representative exchange rates](https://www.boi.org.il/en/economic-roles/financial-markets/exchange-rates/) (₪3.136 per US$ on 2 November 2026); the company's planning rate of ₪3.70 is in `company/finance-summary.md`.
- Templates: [claim read-back](../../templates/claim-read-back.md), [vendor proof-of-concept protocol](../../templates/vendor-poc-protocol.md).
- Earlier: [03.3 · The fast screen](../module-03/lesson-03.md) (the chatbot's condition), [04.3 · Vendor and tool review](lesson-03.md). Module practical: [The policy pack](../../projects/m04-policy-pack.md). Later: engagement 10 (Galil Health) runs a full vendor selection.
