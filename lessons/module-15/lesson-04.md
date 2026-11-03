---
id: "15.4"
module: 15
minutes: 22
practice_minutes: 150
prerequisites: ["15.3", "04.4", "04.7", "05.5", "07.6"]
objectives:
  - "Name the operating model the organisation already runs, compare central, federated and hub-and-spoke on its own evidence, and draw the hub–spoke line item by item."
  - "Write decision rights by risk tier as checkable conditions, with validation depth, who decides go-live and who can stop, so the review queue carries only what needs a central eye."
  - "Specify the three paved roads — platform, templates and evaluation kit, catalogue — with owners, and the route that brings shadow builds, perma-pilots and vendor AI in."
  - "Pre-wire the design with the CRO and the CCO so the policy change is theirs to propose, and test it in the operating-model simulation."
volatility: implementation
sources:
  - title: "Bank of Israel, Proper Conduct of Banking Business Directive 369, Management of Model Risk (English, 8/24): AI models (§5), proportionality, effective challenge (§12), owner (§24), control team and temporary deviations (§25), inventory (§30–32), independence and critical review (§61), periodic review (§67), AI appendix"
    url: https://www.boi.org.il/media/ggpbdtqp/369_en.pdf
  - title: "Bank of Israel, Circular 2792-06 (21 August 2024): Directive 369, based mainly on US SR 11-7; AI definition left to the banks"
    url: https://www.boi.org.il/media/tq1e3rqh/h2792_en.pdf
  - title: "Inter-ministerial team, Artificial Intelligence in the Financial Sector, final report (December 2025, Hebrew): AI governance recommendations, pp. 120–127"
    url: https://www.boi.org.il/media/rh0bejl4/aireport.pdf
  - title: "Bank of Israel, Circular C-06-2799 (18 November 2024): Directive 364, IT, information security and cyber risk; third-party risk"
    url: https://boi.org.il/media/0gudtru2/h2799_en.pdf
  - title: "Bank of Israel, Circular 2849-06 (17 June 2026): update to Directive 362, Cloud Computing (Hebrew)"
    url: https://www.boi.org.il/media/bkrddust/h2849.pdf
  - title: "Bank of Israel, Circular C-06-2571 (8 October 2018): Directive 359A, Outsourcing"
    url: https://boi.org.il/media/w10dtldz/h2571_en.pdf
  - title: "Federal Reserve, SR 26-2, Revised Guidance on Model Risk Management (17 April 2026), superseding SR 11-7; generative and agentic AI outside its scope"
    url: https://www.federalreserve.gov/supervisionreg/srletters/sr2602.htm
  - title: "Federal Reserve, SR 26-2 attachment, Revised Guidance on Model Risk Management (footnote 3 on generative and agentic AI)"
    url: https://www.federalreserve.gov/supervisionreg/srletters/SR2602a1.pdf
  - title: "EU AI Act, Annex III (AI Act Explorer): point 5(b) creditworthiness of natural persons, point 4 employment"
    url: https://artificialintelligenceact.eu/annex/3/
  - title: "IBM Lead AI Transformation Professional Certificate (Coursera): archetypes, hub constants vs spoke variables, paved roads, delegation ladder"
    url: https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution
last_verified: "2026-11-03"
---

# 15.4 · The hard part: an operating model that scales

A bank with 40 builds, 46 people who build AI in its units and one gate that holds 1.5 AI systems a quarter does not need a bigger centre; it needs to decide differently. In this lesson you name the operating model Crescent already runs, choose the one it should run, draw the line between hub and spokes, write decision rights by risk tier, size the review queue, specify the paved roads, design the route that brings shadow builds in, and get the CRO and the CCO to own the policy change before it reaches the Model Committee. At the end you have an operating-model paper, a decision-rights table, the outline of AI policy v2 and a simulation run that tests it.

## The situation

Monday 8 February 2027. On 4 February Avner read the one-page case twice and said: "Bring Irina along, and bring me the design on the fifteenth of March." Dalit asked for the paper before the Model Committee on Thursday 18 February, where you have 30 minutes. Directive 369's phase-in for existing non-material models ends on 21 February. The CFO is waiting for the list (15.5). The board's risk committee wants its first quarterly AI report in Q2.

IBM's operating-models course gives you the vocabulary: three archetypes on a spectrum, *hub constants vs spoke variables*, *paved roads*, the *delegation ladder* and the *single accountable owner*. It stops at the one-sentence ownership line. Here you write the rules, the queue, the roads and the policy for one regulated bank, and then you test them.

## What to do

### Step 1 — Name the model you have

Before choosing a model, describe the one Crescent runs (*operating-model drift*). From your memo:

- **On paper, central:** one policy, one committee, full validation for everything; the board just approved a central build team.
- **In practice, federated:** 14 units built 40 things on 14 vendors and in-house; six units employ their own builders; nobody can see dependencies; four tasks were built twice.
- **The result:** a gate nobody passes and a shadow estate that grows while units wait (the Branch FAQ on a sandbox, call summaries in the CRM, dispute letters through a public API).

That sentence — "central on paper, federated in practice, with the shadow estate as the result" — is the opening of the paper.

### Step 2 — Compare the three archetypes on Crescent's evidence

| | Central CoE | Federated | Hub-and-spoke |
|---|---|---|---|
| Who builds | A central team | Each unit | Units; IT's data team for units without builders |
| Who decides go-live | One committee for everything | The unit head | By risk tier |
| Fits Crescent's talent location? | No: builders already sit in six units and IT | Yes | Yes |
| Fits its regulatory exposure? | Yes, slowly | No: high-risk models without independent validation | Yes: high risk keeps full validation |
| Duplicates | Visible, slow to fix | Multiply | Caught at intake by the catalogue |
| Shadow builds | Grow while units wait | Fewer, but weak models go live | Brought in through a fast route |

Test it in the simulation before you argue it. The `crescent` preset plays twelve quarters from Q1 2027 with Crescent's 14 units and 40 pilots:

[Simulation: Operating model scaler](../../simulations/operating-model-scaler/index.html?preset=crescent)

In this educational model, today's set-up ends 2027 with 2 pilots in production, 13 waiting and 2 shadow tools, and three years later with 7 in production, 29 waiting and 23 shadow tools; a central CoE with twice the review slots reaches 5 after a year and 18 after three, still with 19 shadow tools and more money; federated puts all 40 live in a year, including the 10 weak ones, with 4 duplicates and 23 incidents by year three; hub-and-spoke with decisions by tier and all three paved roads reaches 26 after a year and 36 after three, with 2 incidents and no shadow tools. The simulation is faster than a bank (no procurement, DPIAs or works committees); the ranking is the point, not the counts.

### Step 3 — Draw the hub–spoke line, item by item

Centralise the constants, delegate the variables:

| Item | Owner | Why |
|---|---|---|
| Shared platform: hosting, identity, logging, monitoring, a tested stop switch | Hub (built and run by IT) | Built once; it is what makes a paved road paved |
| Standards, templates and the evaluation kit | Hub | The same test everywhere lets units decide low and medium go-lives safely |
| The catalogue of every model and AI tool, one owner each | Hub | Duplicates, shadow builds and the supervisor's question are answered from it |
| Independent validation of high-risk models | MRM (outside the hub) | The same bar for every unit, by people who did not build it |
| Go-live of low-risk tools on the paved road | Spoke | Centralising it fills the queue with work that needs no central eye |
| Building: discovery, domain knowledge, users | Spoke | Units know the work |
| Adoption and training | Spoke, with the hub's material | Only the unit can change how its people work |

Then size it. The hub is not the board's 16 builders; it is roughly ten people who run the constants: portfolio and intake, evaluation and standards, the catalogue, a platform product owner seated with IT, change and training, risk liaison. Spokes are an AI lead per unit and one named model owner per build ([07.6](../module-07/lesson-06.md)); IBM's *fusion team* (business, data, build, change) is what a spoke looks like around one build.

### Step 4 — Decision rights by risk tier

Write the tier rule as checkable conditions ([04.4](../module-04/lesson-04.md)), owned by MRM, not by the CoE:

- **High:** the output informs or makes a decision on credit, fraud, AML, hiring, investment advice, valuation, market abuse or liquidity.
- **Medium:** not high, and it processes personal or confidential data where a person does not check every output, or it informs or decides something about a customer or employee, or it answers customers.
- **Low:** staff aid on internal or public data, or a draft for one case that a person checks before use, or customer-facing content that shows approved pages verbatim.

Test the rule on cases before you publish it. The Branch FAQ: internal procedures, a teller reads the answer → low. Dispute letter drafts: customer data, but one case and an agent reads every letter → low. Call summaries: customer data written into the CRM by a macro, unread → medium. Credit memo drafting: informs a credit decision → high, even though a banker edits it. If a case lands where your instinct disagrees, change the rule, not the case.

Then the decision table:

| Decision | Low | Medium | High |
|---|---|---|---|
| Register in the catalogue (before real data) | Spoke, 5 days | Spoke | Spoke |
| Evidence | Evaluation kit, threshold set before the run | Kit + monitoring spec + DPIA where personal data (DPO) | Full development documentation |
| Review | Hub checks the kit result (10 working days) | Hub's evaluators, MRM critical review of the method (30 days) | Full independent validation by MRM |
| Go-live decided by | Unit head | Unit head after the hub's sign-off | Model Committee |
| After go-live | MRM samples a share each year; kit re-run on every change | Quarterly monitoring | Annual review |
| Stop | Anyone in the chain, immediately, recorded | Same | Same |

Where the bank's rules come in (the CRO's and the CCO's readings, not yours):

- **Directive 369** applies to AI models and lets the bank apply its requirements in proportion to a model's type, complexity and risk; every model has one owner; validation should be independent of development and use, but where developers or others do part of it, an independent party must critically review that work (§61); the control function can allow temporary deviations from standard validation only with other controls such as deadlines and restrictions on use (§25). Its appendix asks, for AI in particular, for controls on outputs where human involvement is reduced, explainability and documentation of decision mechanisms. The medium tier's design — the hub's evaluators do the work, MRM reviews the method — is built on §61; ask Irina whether she reads it that way.
- **The inter-ministerial report (December 2025)** recommends board approval of AI use within risk appetite, an AI officer, validation before and during use, periodic retrospective review and the ability to stop a system. Recommendations, not rules; Lina decides how Crescent reflects them.
- **Don't import a US reading.** Directive 369 is "based mainly" on SR 11-7 (circular 2792-06). In April 2026 the Federal Reserve replaced SR 11-7 with SR 26-2, which leaves generative and agentic AI outside its scope. Crescent is supervised by the Bank of Israel, whose directive says it applies to AI models; read the Israeli text.
- **The EU AI Act** lists creditworthiness assessment of natural persons and recruitment among high-risk uses (Annex III, points 5(b) and 4). It reaches Crescent only where a system's output is used in the EU; the tier rule is the bank's, and the overlap is a note for counsel, not a design input.

The delegation ladder (assist → recommend → execute → never-delegate) sits inside each build, not in the tier rule; the human-review design of [05.5](../module-05/lesson-05.md) says where on the ladder each one really is.

### Step 5 — Size the review queue

- **Who uses the slots:** only high-tier builds. Six of the 26 kept builds (from the triage in 15.5) → 12 slots → 4 quarters at 3 slots, about 2.7 with templates.
- **The phase-in backlog:** a validation contractor for six months takes it, so MRM's own validators are not pulled away. The CRO, not you, decides how.
- **Order:** the monthly portfolio review ranks high-tier submissions by measured value × readiness; incomplete documentation does not enter the queue.
- **Service levels:** low 10 working days, medium 30 days, high a slot date within two quarters.
- **Reporting:** the three numbers to the board's risk committee every quarter ([04.7](../module-04/lesson-07.md)).

### Step 6 — Specify the paved roads

1. **Platform** (IT owns it): build on IT's approved, unstarted "AI landing zone" (₪1.1M of capex) plus ₪2.4M from the programme; move the Tzofen tenant and the sandbox API onto production terms; identity, logging, monitoring and a stop switch tested twice a year. Directive 362 (cloud, updated June 2026), 359A (outsourcing) and 364 (third parties) apply to what runs there; Nir and the CISO own those readings.
2. **Templates and evaluation kit** (hub): test-set spec, eval report, monitoring spec, DPIA, catalogue card, and one template per pattern found in the portfolio (Q&A over documents, drafting, summarisation, extraction and matching, scoring).
3. **Catalogue** (hub, first): every model and AI tool in use, in development or recently stopped, with the minimum fields Directive 369 §32 lists for a model inventory (purpose and use, inputs and outputs, approval date, status, the people at each stage including one owner, last and next validation, lifespan, internal or supplier) plus tier, data class, vendor contract and renewal date, dependencies and evidence. MRM's inventory and the catalogue become one list with two views. Build it by 31 May: the board's Q2 report and Lina's correction to the survey answer both depend on it.

### Step 7 — Design the route in

A route in is not an amnesty from controls; it is a faster way onto the controlled road:

- **Shadow builds:** register by a date; move onto the platform or an approved tool; keep running meanwhile only with the interim controls the DPO and the CISO set; no disciplinary route for people who come forward. The simulation shows the alternative: shutting shadow tools down raises every unit's appetite for the next one.
- **Perma-pilots:** register what is used today (Branch FAQ, call summaries, the chatbot A/B) with one owner and its tier route; switch off what fails its own threshold.
- **AI in vendor products:** every release note with AI features enters intake; the Kesher renewal (notice by 2 March) asks for generative features off by default until each passes its tier route.

### Step 8 — Get the policy change owned by the people who own the risk

Irina will not propose tiering ("it must not look like Risk lowering the bar"), but she will discuss a written proposal in which MRM owns the tier rule and high risk keeps full validation. Pre-wire it with her (roleplay: [Dr. Irina Kogan](../../labs/module-15/personas/irina-cro.md); [transcript](../../labs/module-15/personas/transcripts/irina-cro.md)) and with Lina ([Adv. Lina Nassar](../../labs/module-15/personas/lina-compliance.md)), who owns how the bank describes this to the supervisor and whether the head of the CoE is proposed as the AI officer. Show Nir the platform section first ([Nir Ashkenazi](../../labs/module-15/personas/nir-cio.md)). Tell Tsega what you are doing ([Tsega Alemu](../../labs/module-15/personas/tsega-internal-audit.md)); do not ask her to approve it.

Write AI policy v2's outline: scope and definitions; the tier rule; decision rights; the evaluation kit and paved roads; public tools and data; vendors and AI in vendor products; stop and incidents; the AI officer and reporting; exceptions; yearly review. Put the [governance charter](../../templates/governance-charter.md) and the [AI intake register](../../templates/ai-intake-register.md) underneath it.

## Watch out

- **Choosing an archetype as a midpoint.** Hub-and-spoke is a separation of concerns: constants in the hub, variables in the spokes. A "medium-sized centre" that still builds and still decides everything is the central model with fewer people.
- **A tier rule the CoE owns.** If the people who want things to go live write the rule, nobody will trust it. MRM owns it; the policy says so.
- **Tiering by the vendor's or the unit's label.** The register's `risk_self_assessed` says "Low" for CV screening. Tier by what the output decides, the data and the review.
- **Paved roads that are slides.** A platform nobody can deploy to, templates nobody must use and a catalogue nobody updates are the board design with new words. Each road has an owner, a date and a first user.
- **Shutting the shadow estate down.** It moves to phones and personal accounts. Bring it onto the road with interim controls.
- **Designing alone and presenting to the committee.** A committee that sees the paper first defends the old rule. Pre-wire with the people who will be asked to own it.
- **Reading Israeli rules through a US lens.** SR 11-7 was replaced and the replacement excludes generative AI; Directive 369 includes AI models. Ask the CRO.

## Your turn

### Inputs

- Your findings memo and case (15.2–15.3); data room (module download): `governance/` (all), `ai/architecture-notes.md`, `ai/intake-requests-2026.csv`, `people/ai-people-by-unit.csv`, `procurement/vendor-contracts-ai.csv`, `company/org-chart.md`.
- Personas: [Irina](../../labs/module-15/personas/irina-cro.md) (pre-wire), [Lina](../../labs/module-15/personas/lina-compliance.md), [Nir](../../labs/module-15/personas/nir-cio.md), [Tsega](../../labs/module-15/personas/tsega-internal-audit.md); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [governance charter](../../templates/governance-charter.md), [AI intake register](../../templates/ai-intake-register.md), [AI inventory](../../templates/ai-inventory.md), [regulatory map](../../templates/regulatory-map.md), [operating rhythm](../../templates/operating-rhythm.md), [risk register](../../templates/risk-register.md).
- [Simulation: Operating model scaler](../../simulations/operating-model-scaler/index.html?preset=crescent).

### Steps

1. Write the one-sentence description of the model Crescent runs today.
2. Compare the three archetypes on Crescent's evidence (at least five rows) and choose.
3. Draw the hub–spoke line (at least seven items) and size the hub.
4. Write the tier rule and test it on six of Crescent's builds, including the Branch FAQ, call summaries and credit memo drafting; then the decision table for low, medium and high.
5. Size the queue: which tiers use slots, the backlog, the order, the service levels.
6. Specify the three paved roads with owners, dates and the catalogue's fields.
7. Write the route in for shadow builds, perma-pilots and vendor AI.
8. Pre-wire with Irina (roleplay twice; coach after each) and write the policy v2 outline.
9. Run the simulation with today's set-up and the usual answers, then with your design; record production, waiting, incidents, shadow tools and cost after 4 and 12 quarters, and one thing you would change in your design because of it.

### Time

150 minutes: 15 for steps 1–2, 20 for the line, 30 for the tiers, 15 for the queue, 20 for the roads, 10 for the route in, 25 for the pre-wire and the outline, 15 for the simulation.

### Done when

- [ ] The paper opens with the model the bank runs today, in one sentence.
- [ ] The tier rule is checkable, owned by MRM, and tested on at least six real builds with no case left to instinct.
- [ ] Only high-tier builds use central review slots; low go-lives are decided in the unit on the paved road; anyone can stop a use.
- [ ] Each paved road has an owner, a date and a first user; the catalogue's fields include those of Directive 369 §32 and one owner per entry.
- [ ] Shadow builds have a route in with interim controls, not a shutdown or an amnesty.
- [ ] The CRO and the CCO saw the paper before the committee, and the policy change is proposed as theirs to own.
- [ ] Your simulation run is recorded with numbers and one lesson for the design.

<details><summary>Reference answer</summary>

The full paper is `labs/module-15/expert/04-operating-model.md` (module download). The parts that carry the weight:

**Today, in one sentence:** central on paper (one policy, one committee, full validation for all), federated in practice (14 units, 40 builds on 14 vendors and in-house, builders in six units), with a shadow estate as the result.

**Choice:** hub-and-spoke. Hub of 10 (₪3.2M): head of the CoE (proposed as AI officer, reporting to the COO with a standing item at the Board Risk Committee), portfolio and intake 2, evaluation and standards 2, catalogue 1, platform product owner 1 (with IT), change 1, risk liaison 1, one evaluator from Q4. Spokes: AI leads in Cards, Digital, Contact Centre, Operations, Credit Risk, Treasury; IT's data team as a shared spoke for the other eight units.

**Tier rule tested:** Branch FAQ low; dispute letters low; procedure assistant low; call summaries medium (macro writes unread into the CRM); complaint summaries medium (themes report at scale); credit memo high (informs credit); SME pre-approval high; CV screening high (hiring), whatever its self-assessed "Medium".

**Queue:** 3 AI slots a quarter for high only (6 builds, 12 slots); a validation contractor for six months for the 369 phase-in backlog (₪350,000); low 10 working days, medium 30 days, high a slot date within two quarters.

**Roads:** platform on IT's ₪1.1M landing zone + ₪2.4M, live September; kit and templates by June; catalogue by 31 May, MRM's inventory and the catalogue one list.

**Route in:** shadow route until 31 March with the DPO's and the CISO's interim controls; dispute letters onto CRD-03 by 31 January; Digital's writers onto Tzofen seats; branch letters in Arabic and Russian through a Tzofen template from April; chatbot A/B switched off; Kesher renewal with AI features off by default.

**Pre-wire with Irina (second rehearsal):** opened with her own capacity table, then "MRM owns the rule and the high tier keeps full validation; nothing changes until the catalogue is complete". She asked for the tier rule to be "MRM's document, referenced by the policy, not inside it", and for the contractor in writing. Both accepted. Lina asked that the AI-officer proposal go to the board as a separate item.

**Simulation (crescent, educational model):** today's set-up with the usual answers — after 4 quarters 2 in production, 13 waiting, 2 shadow tools; after 12, 7 in production, 29 waiting (5.3 quarters on average), 23 shadow tools, ₪21.4M. Hub-and-spoke, tiered rights and validation, 3 slots, all three roads, the expert's answers — after 4 quarters 26 in production, 7 waiting, 0 shadow; after 12, 36 in production, 0 waiting, 2 incidents, ₪29.8M of ₪30.9M. Lesson for the design: the catalogue is what makes the supervisor's question answerable in Q1 2028; without it the same design gets a finding and a pause.

</details>

## References

- Bank of Israel, [Directive 369](https://www.boi.org.il/media/ggpbdtqp/369_en.pdf) and [circular 2792-06](https://www.boi.org.il/media/tq1e3rqh/h2792_en.pdf): AI models (§5), effective challenge (§12), one owner (§24), control team and temporary deviations (§25), the inventory (§30–32), independence and critical review (§61), periodic review (§67), the AI appendix. The Hebrew text is binding; the CRO reads it for the bank.
- Inter-ministerial team, [AI in the financial sector, final report](https://www.boi.org.il/media/rh0bejl4/aireport.pdf) (December 2025, Hebrew), AI governance, pp. 120–127: board approval, AI officer, validation, stop capability. Recommendations.
- Bank of Israel, [circular C-06-2799](https://boi.org.il/media/0gudtru2/h2799_en.pdf) (Directive 364), [circular 2849-06](https://www.boi.org.il/media/bkrddust/h2849.pdf) (Directive 362 update, June 2026, Hebrew), [circular C-06-2571](https://boi.org.il/media/w10dtldz/h2571_en.pdf) (Directive 359A).
- Federal Reserve, [SR 26-2](https://www.federalreserve.gov/supervisionreg/srletters/sr2602.htm) (17 April 2026): supersedes SR 11-7; generative and agentic AI outside its scope.
- [EU AI Act, Annex III](https://artificialintelligenceact.eu/annex/3/), points 4 and 5(b); application dates as amended by Regulation (EU) 2026/1744 are in the course's [laws and guidance](../../references/laws-and-guidance.md).
- IBM, [Lead AI Transformation certificate](https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution): archetypes, hub constants vs spoke variables, paved roads, delegation ladder, fusion team (named, not re-taught).
- [Simulation: Operating model scaler](../../simulations/operating-model-scaler/index.html?preset=crescent) (educational model).
- Field kit: [04.4 · Inventory and risk tiering](../module-04/lesson-04.md), [04.7 · Governance that runs](../module-04/lesson-07.md), [05.5 · Human-in-the-loop design](../module-05/lesson-05.md), [07.6 · The operating rhythm](../module-07/lesson-06.md).
- Templates: [governance charter](../../templates/governance-charter.md), [AI intake register](../../templates/ai-intake-register.md), [AI inventory](../../templates/ai-inventory.md), [regulatory map](../../templates/regulatory-map.md), [operating rhythm](../../templates/operating-rhythm.md), [risk register](../../templates/risk-register.md).
- Earlier: [15.3 · Diagnosis](lesson-03.md). Next: [15.5 · Decide: triage, design and a 12-month plan](lesson-05.md).
