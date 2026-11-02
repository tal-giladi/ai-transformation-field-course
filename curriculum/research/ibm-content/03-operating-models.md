# IBM Course 3 — AI Operating Models and Organizational Design (notes)

Read 2026-11-02 from the logged-in course (all transcripts and readings; one plugin opened). No coach
items or written assignments in this course's item feed — plugins only. Slug:
`ibm-ai-operating-models-organizational-design`.

Same shape as courses 1–2, but modules 1–3 each have an expert tutorial and a 15-minute exercise guide
(browser AI assistant + starter sheet + one-page template). Narration partly AI-generated (stated).
Scenario: unnamed enterprise with pilots in several units; the tutorials add one concrete example —
a 30,000-person manufacturer with 3 BUs (industrial equipment, consumer products, services), no
central AI team.

## Module 1 — Choose Your AI Operating Model

- Concepts / IBM terms:
  - Operating model drift — the enterprise already has a model, it just never chose it.
  - AI operating model (how the business is organised to deliver AI) vs AI strategy (where).
  - Three archetypes on a spectrum: centralized (consistency, slow), federated (speed, duplication),
    hub-and-spoke (centre owns platform/standards/governance/observability = "paved roads"; units own
    discovery, adoption, domain products) — a separation of concerns, not a midpoint.
  - MIT CISR four maturity stages: experiment & prepare; build pilots & capabilities; develop AI
    ways of working; become AI future-ready.
  - Five decision factors: maturity, regulatory exposure, talent location, BU autonomy, use-case
    diversity — each tilts central or local.
  - Evolution signals: duplication → more centre; units routing around approval queue → more edge;
    governance straining → slow down. "Driver's licence" certification to let people build safely.
  - CoE-bottleneck test: centre adequately staffed? units literate? governance documented and not
    person-dependent? centre shipping production outcomes?
  - Cited: Gartner 2024 ~half of AI projects reach production, ~8 months; McKinsey — workflow
    redesign is the factor with the biggest effect; IBM IBV 2026 — 77% say adoption outpaces
    governance; IBM CEO study 2026 — 76% have a CAIO (verify before reuse).
  - "Match the Model to the Moment" skill.
- Concrete how-to: expert tutorial gives 6 steps — inventory current AI use and owners and name the
  current model honestly; locate on maturity curve; profile 5 factors; match archetype and state the
  trade-off; draw the centre/unit ownership line in one sentence each; sequence the evolution with
  signals. Good, but the inventory step ("write down how AI is really used") has no method.
- Exercise: one-page recommendation from a provided generic scenario with an AI assistant.
- Gaps: how to run the inventory (survey, SaaS/expense/SSO logs, interviews); who decides the model
  and how to get it approved; staffing the hub (roles, headcount, budget, hiring vs secondment);
  charter for a CoE/hub; what "paved roads" physically are (approved tools, templates, platform).

## Module 2 — Roles, Responsibilities, and Decision Rights

- Concepts / IBM terms:
  - Ownership drift — governed by tool, but exposure is in decisions nobody owns.
  - Decision right; RACI vs DACI vs RAPID (Bain); single-accountable rule (committees advise, never
    decide).
  - AI delegation ladder: assist → recommend → execute → never-delegate; the rung is what really
    happens (if reviewers approve ~everything, it's execute).
  - Never-delegate test is about legitimacy, not difficulty.
  - Layers: data governance vs AI ethics vs AI governance (operational machinery).
  - New seats: model owner, data/AI steward, responsible-AI lead, governance owner.
  - Authority check: owner can see the recommendation and basis, can overturn it without the
    builders, and has time to. Legitimate override = visible basis, substitute outcome without
    permission, recorded with reason, reviewable.
  - Decision-to-model inventory (including rules the AI reads).
  - "Map the Decision, Not the Tool" skill.
- Concrete how-to: exercise guide is detailed — one-decision map from a provided case (fraud-flag
  account hold, or a second option): name the decision, pick the rung and argue the neighbour rung,
  never-delegate test, framework, one owner, voice vs vote, AI's bounded role, skeptic prompt,
  override/escalation/record. Strong single-decision method.
- Gaps: building the full inventory of AI-shaped decisions across an organisation (where to find
  them, how to interview for them); getting the named owner to accept accountability; writing it into
  procedures, job descriptions and system permissions; testing that the override actually works at
  volume (touched in course 4).

## Module 3 — Data and Infrastructure Foundations for Leaders

- Concepts / IBM terms:
  - The unowned foundation; "own the foundation, not the plumbing".
  - Three-layer stack: infrastructure / platform / applications, data across all three.
  - Data fabric (Gartner, metadata-driven central integration) vs data mesh (Dehghani 2019, domain
    data products, federated governance) — complementary.
  - Placement per workload class (retrieval assistant, training run, agent acting in systems); six
    placement questions: steady-state cost, data movement, latency, jurisdiction, audit evidence,
    cost to move later.
  - Build / buy / partner on five factors: core competency, urgency, budget, talent, control needs;
    Prahalad & Hamel 1990 core-competency test; the call may split (buy commodity, build the narrow
    differentiating piece).
  - Four leader calls: data foundation, infrastructure posture, build/buy/partner, governance model;
    everything else delegated to a named team.
  - Cited: McKinsey ~8 in 10 use GenAI, about as many see no significant bottom-line impact.
- Concrete how-to: tutorial walks the 6 steps on predictive maintenance at the manufacturer
  (telemetry owned by one unit, service history by another, nobody owns the pair). Exercise: one
  foundation call on warranty-claim triage with AI assistant, five factors, core-competency test,
  own-vs-delegate line, argue against yourself twice.
- Plugin: "Make the Call: Build, Buy, or Partner".
- Gaps: actually checking data readiness (profiling a sample, lineage, consent/permission to use);
  vendor evaluation and contracting for "buy"; cost estimation for placement (tokens, GPU, egress);
  security/privacy review of a SaaS AI tool; nothing on running the decision with IT/procurement.

## Module 4 — Scale the Operating Model Across Units

- Concepts / IBM terms:
  - The un-extended model — clone vs free-for-all both fail; extend a hub, adapt spokes.
  - Hub owns constants (infra, standards, reusable-asset library, observability, attribution,
    security); spokes own variables (discovery, domain knowledge, adoption).
  - Maturity ladder per unit: experimentation → tool adoption → internal platforms → strategic
    integration → AI-native; plus factors (growth stage, workflow complexity, data foundation, AI
    fluency, risk tolerance).
  - Operationalized governance — approvals before production, role-based access for users, apps,
    integrations and agents, runtime logging, policy-as-code.
  - Fusion team (four seats: business, data, build, change) per unit, short cycles.
  - Usage can climb while impact stays flat.
  - Hub evolves from gatekeeper to advisor; "the platform is the constant, not the model".
  - "Extend the Hub, Adapt the Spoke" skill.
- Plugin (opened): support unit (messier data, warier staff) extending a marketing pilot; sort 9
  items into hub vs spoke; then an ungraded centralise↔federate dial showing seize vs fragment.
- Gaps: a unit-by-unit rollout plan; how to staff and run a fusion team; the inventory of what is
  running (shadow tools); concrete control-plane setup (access, logging) in common tools; extension
  health checks — how to measure them.

## Course-level verdict

- Reuse as vocabulary: operating model drift, paved roads, the 5 factors, maturity stages,
  ownership drift, delegation ladder (assist/recommend/execute/never-delegate), single-accountable,
  legitimate override (4 parts), own the foundation not the plumbing, placement questions,
  build/buy/partner + core-competency test, hub constants vs spoke variables, operationalized
  governance, fusion team.
- Fill: the inventory work (what AI and which AI-shaped decisions exist today — never taught how),
  getting decisions approved and staffed (hub charter, roles, budgets, hiring), vendor
  evaluation/contracting, real data-readiness checks, and a concrete rollout plan across units.
  This is the most method-rich IBM course so far (three guided single-decision exercises), but each
  exercise is one decision on a generic provided scenario, never a whole organisation.
