# 02 · Findings memo

*To: Dalit Ben-Ami, COO. Thursday 21 January 2027. Labels: **M** measured from the data room, **R** reported by a person, **I** inference. Names of staff who spoke in confidence are not given.*

## The answer first

"Forty pilots and nothing in production" is wrong in both directions. There are fewer real pilots than 40, and more AI in real use than none. The pilots do not reach production because the route to production has room for one and a half AI systems a quarter, not because the units are slow; while they wait, some of them went live anyway, outside any inventory, and so did tools nobody registered. Two decisions are due before the diagnosis on 4 February: the Mishov notice (30 January) and our comments on the CFO's cut (31 January).

## Findings

**1. The register is 40 builds, not 43 rows, and fewer than 40 are worth taking forward.** (M) Three pairs of rows share an environment, a test set and identical eval results: MTG-01/OPS-04, TRS-01/PRV-03, FIN-02/OPS-05; each is budgeted in both units (₪420,000 counted twice in 2027). Four pairs are two units building the same task on different vendors: complaint summaries (Retail on Mishov, Cards on Bahir), credit-memo drafting (SME, Corporate), KYC document checks (SME, Compliance & AML), conversation summaries (Contact Centre, Digital); Retail has asked for a fifth (branch call summaries). Ten pilots fail their own thresholds or have no users, no owner or an open compliance question (details in 03). Sixteen rows have no measured baseline.

**2. The gate holds one and a half AI systems a quarter.** (M) AI policy §2: full validation for every AI system. MRM: a head and two validators, 12 slots a quarter, 3 for AI, 2 slots per full validation. The queue: 19 submissions, 2 in validation, 0 approved, 0 declined; median wait 193 days, longest 437 (the Branch FAQ). The committee met 5 times in 2026, not monthly (§5). After 21 February the phase-in slots move to annual reviews, not to AI (R, Irina). At this rate the 40 builds need 80 slots: 27 quarters.

**3. AI is in real use without validation.** (M) The Branch FAQ: 31 branches, a median of 2,072 questions a week, on a sandbox whose contract says "pilots only, no production use"; it quoted an outdated fee in November (thumbs-down 9.0% in the fee weeks against 4.9% over the quarter). Contact Centre call summaries are written into customers' CRM notes by a Kesher macro since August; the pilot has two owners (Revital Cohen / Tom Erez). The customer chatbot is live for 2% of web visitors since 3 November although the committee returned it in November; its last eval was 0.76 against 0.90. (I) Internal audit would count a pilot used every day as a model in use (R, Tsega: "whether it is called a pilot doesn't change that").

**4. AI outside the register.** (M) A public LLM API ("LLMHUB *API USAGE") on a Cards team lead's corporate card every month since April: ₪13,741 in nine lines; the proxy shows the Cards disputes subnet sending 127 MB to api.llmhub.io in Q4, "allowed (uncategorised)". Three people in Digital marketing claim a writing tool on personal accounts every month (₪2,144 in 2026). Contact Centre agents use a free translator (2,342 requests in Q4). Branch PCs tried a public chat site 924 times in Q4 (blocked). (R) Branch staff draft letters to customers in Arabic and Russian; how, I could not establish. **None of these is in the register or the model inventory.**

**5. What the bank told the supervisor does not match.** (M) The 2026 survey answer 3.1 says a central inventory lists every AI application with its owner; the register has no owner for PRV-02 (owner left in September), two for CC-01, and none of finding 4. Answer 3.4 says no AI is in production with customers (finding 3). Answer 4.2 says public generative AI is blocked (finding 4). (I) This needs Lina and Irina this month, not at the readout.

**6. The CFO's cut would cut the base of two of the best pilots.** (M) The memo: cancel the assistant, ₪2.4M, "16% of seats". December: 250 weekly active users of 1,600 seats (16%) — but of 380 onboarded users (66%); in October–November the two pilot teams were at 74% (Operations) and 68% (Contact Centre). The Operations procedure assistant (0.91, threshold 0.85) and the Contact Centre knowledge assistant (0.88, threshold 0.85) run inside the assistant's agent studio, on indexes that are deleted 30 days after the subscription ends. The register's dependency column is empty for all 43 rows.

**7. Contracts decide dates for us.** (M) Mishov (Retail complaints): 24-month auto-renewal unless notice by 30 January. Katvan AI (two stop candidates): notice by 15 March. Kesher CRM: notice by 2 March; release 27.1 in October switches on generative features for every user by default (R, Nir). Kishron Rank (CV screening) renewed itself on 15 December with no DPA.

**8. The builders already sit in the units.** (M) 46 people work on AI: six units have their own (Cards 5, Digital 6, Treasury 3, Credit Risk 4, Contact Centre 3, Operations 3), IT's data-science team (8) built a third of the pilots for units without builders. A central build team of 16 would hire a second copy of people the bank already has.

## What I need decided before 4 February

1. Give Mishov notice by 30 January (Dalit, with Hagit informed): it keeps the complaint-tool decision open; we can renew for 12 months later if Retail's build wins.
2. Our reply to the CFO by 31 January: the 15% can be met without cancelling the assistant; the list comes on 4 February.
3. Lina and Irina briefed on finding 5 this week.

## Escalated the same day

- 13 January, to the CISO's office, the DPO and Nir: customer data going to an uncategorised public API from the Cards disputes subnet (finding 4). Their decision: the host is blocked from 1 February; from 14 January Cards removes names and card digits from what it sends; the letters move to the dispute-letter pilot on the approved sandbox with the DPO's approval by 31 January, so the team is not pushed onto phones. Karim agreed and was told this is a route in, not a disciplinary matter.
- 20 January, to Lina: finding 5.
