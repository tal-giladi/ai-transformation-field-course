# 04 · Operating model: how AI goes to production at Crescent

*Paper for the Model Committee, Thursday 18 February 2027, agreed beforehand with Dr. Irina Kogan (CRO) and Adv. Lina Nassar (CCO); then to the Management Committee on 15 March. Regulatory readings in this paper are the CRO's and the CCO's, not the CoE's.*

## 1. The choice

| | Central CoE (the board's design) | Federated (units decide) | **Hub-and-spoke (proposed)** |
|---|---|---|---|
| Who builds | 16 central people | Each unit | Units (spokes), IT's data team for units without builders |
| Who decides go-live | The Model Committee, for everything | The unit head | **By risk tier** (§3) |
| Review | Full validation for all | Light or none | **By tier**; full for high |
| Duplicates | Visible, slow to fix | Multiply | Caught in the catalogue at intake |
| Shadow builds | Grow while units wait | Fewer, but weak models go live | Brought in through a fast route |
| In the simulation (crescent preset, 4 quarters / 12 quarters) | today's set-up: 2 / 7 in production, 23 shadow tools by year 3 | 40 live after a year, 10 weak live, 23 incidents by year 3 | 26 / 36 in production, 2 incidents, 0 shadow |

The bank already has an operating model it never chose (IBM's "operating-model drift"): central on paper, federated in practice, with the shadow estate as the result. The proposal centralises the constants and delegates the variables.

## 2. Hub and spokes

**Hub (AI CoE, 10 people, ₪3.2M a year):** head of the CoE (proposed as the bank's AI officer, reporting to the COO, with a standing item at the Board Risk Management Committee); portfolio and intake (2); evaluation and standards (2: the evaluation kit, templates, standard reviews of medium-tier builds); catalogue and reporting (1); platform product owner (1, seated with IT); change and training (1); risk and compliance liaison (1); one open position for a second evaluator from Q4.

**Spokes:** an AI lead and a named model owner per build in each unit. Six units already have builders (Cards, Digital, Contact Centre, Operations, Credit Risk, Treasury). Units without builders (Retail, Mortgages, SME, Corporate, Private, Compliance & AML, HR, Finance) are served by IT's Data & Analytics team as a shared spoke, prioritised by the monthly portfolio review.

| Item | Hub or spoke | Why |
|---|---|---|
| Shared platform: hosting, identity, logging, monitoring, the stop switch | Hub (built and run by IT) | Built once; what makes a paved road paved |
| Standards, templates and the evaluation kit | Hub | The same test everywhere lets units decide low and medium go-lives safely |
| The catalogue of every model and AI tool, with one owner | Hub | Duplicates, shadow builds and the supervisor's question are answered from it |
| Independent validation of high-risk models | MRM (outside the hub) | The same bar for every unit, by people who did not build it |
| Go-live of low-risk tools on the paved road | Spoke | Centralising it fills the queue with work that needs no central eye |
| Building: discovery, domain knowledge, the users | Spoke | Units know the work |
| Adoption and training in the unit | Spoke, with the hub's material | Only the unit can change how its people work |

## 3. Decision rights by tier

**Tier rule (owned by MRM, written into AI policy v2):**

- **High:** the output informs or makes a decision on credit, fraud, AML, hiring, investment advice, valuation, market abuse or liquidity. Examples: SME pre-approval, early-warning signals, credit memo drafting, fraud triage.
- **Medium:** not high, and it processes personal or confidential data where a person does not check every output, or it informs or decides something about a customer or employee, or it answers customers. Examples: complaint summaries, call summaries into the CRM, KYC checks.
- **Low:** staff aid on internal or public data, or a draft for one case that a person checks before it is used, or customer-facing content that only shows approved pages verbatim. Examples: Branch FAQ, procedure assistant, dispute letter drafts, in-app search.

| Decision | Low | Medium | High |
|---|---|---|---|
| Register in the catalogue (before any real data) | Spoke, within 5 days | Spoke | Spoke |
| Evidence | Evaluation kit: test set, threshold set before the run | Kit + monitoring spec + DPIA where personal data (DPO) | Full development documentation |
| Review | Hub checks the kit result (10 working days) | Standard review by the hub's evaluators, MRM critical review of the method (30 days) | Full independent validation by MRM (2 slots) |
| Go-live decided by | Unit head (the model owner's line) | Unit head, after the hub's sign-off | Model Committee |
| After go-live | MRM samples 10% a year; owner re-runs the kit on every content or model change | Quarterly monitoring report | Annual review (Directive 369) |
| Stop | Anyone in the chain, immediately; recorded within 24 hours | Same | Same |

The CRO's reading (recorded): Directive 369 applies its requirements proportionately to a model's type, complexity and risk; it allows part of the validation work to be done by others when an independent party critically reviews it; whether a generative drafting tool is a "model" under the bank's policy is the bank's definition, and policy v2 lists every AI tool in the catalogue whether or not it is a model. The CCO's note: the inter-ministerial report of December 2025 recommends board approval of AI use within risk appetite, an AI officer, validation before and during use and a stop capability; recommendations, not rules.

## 4. The review queue

- **Slots:** 3 AI slots a quarter stay; only high-tier builds use them. A validation contractor for six months (₪350,000) takes the Directive 369 phase-in backlog so MRM's own validators are not pulled away (the people risk in MRM is real and is the CRO's to manage).
- **Order:** the monthly portfolio review ranks high-tier submissions by value with a measured baseline × readiness (documentation complete, owner named); a submission without documentation does not enter the queue.
- **Service levels:** low 10 working days, medium 30 days, high a slot date within two quarters.
- **The three numbers to the board every quarter:** reached production; median days to decision with the slowest named; declined and why.

## 5. Paved roads

1. **Platform** (IT, on the approved ₪1.1M AI landing zone plus ₪2.4M from the programme): hosting, identity, logging, monitoring, a tested stop switch; the Tzofen tenant and the Ananim API moved to production terms. Live for low and medium builds by September.
2. **Templates and evaluation kit** (hub): test-set spec, eval report, monitoring spec, DPIA, catalogue card; pattern templates for the five patterns in the portfolio (Q&A over documents, drafting, summarisation, extraction and matching, scoring).
3. **Catalogue** (hub, first, by 31 May): every model and AI tool in use, in development or recently stopped, with the fields Directive 369 §32 lists for the model inventory (purpose and use, inputs and outputs, approval date, status, the people responsible at each stage incl. one owner, last and next validation, planned lifespan, internal or supplier) plus tier, data class, vendor contract and renewal date, dependencies, and the evidence. MRM's model inventory and the catalogue are one list with two views.

## 6. Bringing things in

- **Shadow builds:** a written route in until 31 March, not an amnesty from controls: register, move onto the platform or an approved tool, keep running while that happens only with the interim controls the DPO and the CISO set. Dispute letters (Cards) moved onto the approved sandbox under CRD-03 by 31 January; Digital's writers moved to Tzofen seats; branch letters in Arabic and Russian get a Tzofen template and training in April.
- **Perma-pilots:** the Branch FAQ, call summaries and the chatbot A/B are registered as in use now; each gets one owner and its tier route with a date; the chatbot A/B is switched off (it fails its own threshold).
- **AI in vendor products:** every vendor release note with AI features goes into intake; the Kesher renewal (notice by 2 March) asks for the generative features off by default until each passes its tier route.

## 7. AI policy v2 (outline)

1 Scope and definitions (AI tool, model, the catalogue) · 2 The tier rule (MRM) · 3 Decision rights per tier (§3 table) · 4 The evaluation kit and paved roads · 5 Public tools and data · 6 Vendors and AI in vendor products (with Directives 359A, 362, 364) · 7 Stop and incidents · 8 The AI officer and reporting to the board · 9 Exceptions (CRO, written, dated, with compensating controls) · 10 Review yearly.

## 8. Operating rhythm

Weekly intake triage (hub, 30 minutes). Monthly AI portfolio review (hub + spoke leads + MRM + IT, 60 minutes: the queue, the catalogue changes, incidents, the three numbers). Monthly Model Committee for high-tier items only. Quarterly report to the Board Risk Management Committee. Yearly policy review. RACI and triggers as in the [operating rhythm](../../../templates/operating-rhythm.md) template.
