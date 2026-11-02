# IBM course 4 — AI Governance, Risk, and Responsible Deployment

Read 2026-11-02 from the logged-in course (all video transcripts and readings; one plugin and one
coach opened). Slug `ibm-ai-governance-risk-responsible-deployment`. 5 modules, ~8 h. The longest
and best course of the seven.

Course-wide format: each module = intro video, a "the problem" story video, a "perspectives" video
(5–6 roles each say what they own and what earns their attention), a "Terms you should know"
reading, a concepts video, an expert tutorial, an **exercise guide with downloadable LabBook files
(docx/xlsx/txt case packs)**, an expert demo screencast filling the template, a "portable skill /
interview answer" video, a Coursera Coach AI role-play (voice/text), a 15-min plugin and a
staff-graded assignment.

- **Plugins** are small external single-page HTML widgets (hosted on a github.io page, e.g.
  `C4M4_PriceHumanCheckpoint.html`): fill 3 numbers, check them, pick the one defensible reading of
  three, then move sliders (volume, exception rate, minutes, reviewers, "gateway enforces approval"
  toggle) and see a capacity vs enforcement verdict. Good model for our offline simulations.
- **Coach items** are Coursera's AI role-play: e.g. "AI Governance Hiring Manager" — you answer an
  interview question as a candidate about a hiring-ranking feature that arrived via a software
  update, then switch seats and grade another candidate's answer. Voice chat. Several coach items are
  framed as **job interviews**, not as conversations inside an organization.
- The scenario is a different small fictional case per exercise (marketplace moderation, Harborline
  Retail scheduling optimizer, customer-scoring service, invoice coding assistant, Northstar Talent
  Services candidate ranking, PayFlow supplier-payment agent, store-credit model). The learner is
  always "the AI and transformation lead" reading someone else's evidence.

## Module 1 — The AI Governance Imperative

- **Scenario/role.** Multi-BU enterprise where GenAI arrived bottom-up; the board/auditor asks how a
  consequential decision was shaped by AI and nobody can answer. Learner = AI transformation lead /
  newly named AI officer with accountability but no machinery.
- **Concepts.**
  - AI governance = an operating capability that wires together data governance, model risk,
    security, privacy, legal — not a document or ethics statement.
  - Values become governable only as responsibility + control + evidence (model card, test, log).
  - Four oversight postures: per-action approval, threshold approval, monitored operation with
    interruption, retrospective audit ("the ladder" — explicitly not a maturity scale).
  - Designed posture vs effective posture vs control effectiveness — three separate judgments.
  - Meaningful oversight needs: relevant evidence, time at real volume, competence, authority (and
    perceived authority), a working way to intervene.
  - "Read the rung, build the rail" — governance as a feedback loop (inventory → controls →
    monitoring → review of authority).
  - AI inventory as a shared object (system, use, owner, actions).
- **How-to given.** Yes, a real 6-step procedure: read the system record → name designed posture →
  test effective posture against operating evidence → judge control effectiveness (effective /
  partially evidenced / ineffective / cannot determine) → name the priority gap + evidence needed →
  recommend (strengthen / maintain / reduce / reconsider / pause authority). Sentence template for
  the recommendation. Evidence register with confidence levels (fact / inference / assumption).
- **Exercise.** Oversight Posture Readout (xlsx) on one of 4 fictional case cards
  (`synthetic-governance-case-pack.docx`); demo uses the scheduling optimizer (97% of schedules
  released within 20 min → "partially evidenced", recommend blocking publication while exceptions
  are open). Optional: ask a chatbot to challenge the readout. Plugin "What the log can prove".
  Coach: "On paper, or in practice?" and "Build a defensible AI oversight recommendation".
- **Gaps.**
  - Says "inventory the systems" but never how: no discovery method for finding AI in SaaS
    feature updates, browser extensions, expense reports, proxy logs; no inventory template fields
    beyond the four named; no "who do I email on day 1".
  - Minimum required oversight is *given on the case card*. In reality the learner must derive it
    (from law, policy, consequence) — not taught.
  - No log/telemetry work: the learner is told what the logs show, never pulls or reads real logs,
    never specifies what logging to switch on.
  - No governance charter, committee terms of reference, meeting cadence, or intake process for new
    AI uses.

## Module 2 — Manage AI Risk

- **Scenario/role.** A signed register where everything is green: customer-scoring service in
  production and a hiring screening assistant in pilot. Learner = AI transformation lead integrating
  evidence from reviewer, model owner, risk/compliance, business owner, finance/procurement.
- **Concepts.**
  - AI risk is socio-technical and use-specific (assess a use, not a technology).
  - Taxonomy for coverage (data/privacy, performance/safety, fairness/rights, security/misuse,
    operational/human factors, third-party/legal) + mechanism sentence for each row: "Because
    [condition], [party] may suffer [harm] through [decision/workflow]".
  - Inherent vs control status vs residual — three judgments; four control statuses (designed and
    evidenced / designed not validated / partially effective or deficient / not implemented).
  - "Unearned green"; control-credibility test (6 questions: mechanism fit, real conditions,
    detectable failure, performer authority, evidence, how you'd know it's failing).
  - Capacity screen: net review minutes ÷ minutes per case vs peak demand; watch denominators that
    drop unresolved cases.
  - Failure signal = indicator + threshold + owner + cadence + response.
  - Treatments reduce/avoid/transfer/accept; benefit-and-burden ledger (risk reduction vs control
    cost and workload moved to another team); risk acceptance = named person, exposure, date, trigger.
  - Preventive / detective / corrective controls.
- **How-to given.** Yes — 6 steps to re-test one Low row (restate → test match → classify status →
  capacity test → failure signal → revised readout), plus a short "applying it at work" checklist
  (use your org's taxonomy; rewrite one real row).
- **Exercise.** `customer-scoring-risk-register.xlsx` + operations brief; row R-03: 8,000 ÷ 2.5 =
  3,200 capacity vs 4,640 peak → residual back to High; capacity trigger and pause authority for the
  operations lead. Plugin "Test one green row — the capacity screen". Coaches: "Test the control
  behind the rating", "Defend the residual risk rating".
- **Gaps.**
  - Re-tests one row of a register someone else wrote. Never builds a register from zero: no
    risk-identification workshop, no pre-mortem, no list of typical risks per use-case type (chatbot,
    extraction, scoring, agent), no starter register.
  - No actual control testing: never samples outputs, runs a test set, measures error rates, or
    designs the negative test — the "evidence" is always pre-written in the brief.
  - Vendor/third-party risk only named (indemnity, audit rights); no vendor questionnaire, DPA
    review, model-change notification clause, exit plan.
  - No security-specific risks (prompt injection, data leakage) worked through.
  - No link to the organization's existing ERM/risk appetite process — "ask your risk function".

## Module 3 — Read the AI Regulatory Landscape

- **Scenario/role.** Board asks "are we compliant?"; a candidate-ranking assistant and a scheduling
  tool that emits performance signals both arrived as feature updates. Learner owns the board answer.
- **Concepts.**
  - "Compliance drift": confident claims with no source/version/date/actor behind them.
  - Two layers: slow deployment facts vs fast legal conclusions — refresh only the legal layer.
  - Classify the use, not the sophistication; check the AI-system definition first; one high-risk
    use doesn't make everything high-risk.
  - Scope follows legal actors (provider, importer, distributor, deployer, employer) and connections,
    not geography; buying usually makes you deployer until your changes make you provider
    ("substantial modification").
  - Voluntary frameworks (NIST AI RMF), management-system certificates (ISO/IEC 42001 — check
    scope, sites, exclusions, validity) and binding law do different jobs; none presumes the other.
  - Source ladder: enacted text → definitions/annexes → implementing acts → official guidance →
    case law/enforcement; commentary is only a search lead.
  - Legal dates are distinct: adoption, publication, entry into force, application, enforcement.
  - Regulatory exposure profile (per bounded use) + auditable claim card (conclusion, facts, actor,
    instrument version, provision, source, verification date, legal status, application date, open
    questions). "Actor–source–date check".
- **How-to given.** Yes — 6 steps on one claim: unit of analysis → facts vs inference vs missing
  evidence (with an evidence owner per gap) → search plan (chatbot allowed, as search plan only) →
  verify in the official text → resolve two conflicting secondary summaries → challenge.
- **Exercise.** EU AI Act on "Candidate Match" (Northstar Talent Services, Irish subsidiary):
  Art. 2, 3, 6(2)–(4), Annex III 4(a), Art. 113, the full two-part Art. 6(3) exception and the
  profiling rule. **Useful fact for our course (verify ourselves):** the course states that on its
  2026-08-02 check, EUR-Lex listed Regulation (EU) 2026/1744 as published 2026-07-24, in force
  2026-07-27, amending Art. 113 so Chapter III §§1–3 apply to Art. 6(2)/Annex III systems from
  2027-12-02. Plugin "Build the claim card: status vs application date". Coach "AI Governance Hiring
  Manager" (interview role-play, then grade another candidate).
- **Gaps.**
  - EU only, in depth, on one article. Nothing on GDPR/DPIA, national privacy law (e.g. Israel's
    Amendment 13), US state laws, sector regulators, employment/works-council consultation, or
    consumer-protection liability for chatbot answers.
  - Produces one claim card; never a full regulatory map for an organization's whole AI inventory,
    never a compliance work plan (who does what by when), never what documents a deployer must
    actually produce (FRIA, transparency notices, logs retention, AI literacy obligation).
  - No guidance on working with counsel: what to send, how to scope a legal question, budget.
  - No procurement clauses that make a vendor carry provider duties.

## Module 4 — Govern Agentic AI and Autonomy

- **Scenario/role.** An invoice-matching agent switched on inside licensed automation software
  cleared the backlog; operations wants it to release payments untouched; the board asks how much
  authority was granted. Learner = AI transformation lead reconciling ops, engineer, CRO, AP
  supervisor.
- **Concepts.**
  - Authority gap = what the agent can do vs what anyone authorized.
  - Behavioral instruction (prompt) ≠ authorization boundary (enforced outside the model: scoped
    credential, allowlist, transaction ceiling, dual approval). Test: what independent component
    refuses an out-of-scope action?
  - Detective control (5 pm report) ≠ preventive gate.
  - Autonomy mode ladder (assistant → proposes → approval-gated steps → supervised automation of
    standard cases → minimal intervention) — a label only; widening authority is a governed
    decision with validated permissions, tested recovery and review capacity, rollback trigger.
  - Agent as a separately attributable actor: own revocable identity, least privilege, trace of
    inputs/tool calls/approvals/state changes/timestamps (not hidden reasoning).
  - Recoverability bands: easy / bounded / difficult / uncertain. "Last reversible moment" = last
    practical prevention point. Preventive / detective / corrective / recovery-oriented controls.
  - Agent Authorization Summary + Action Register (one row per action: consequence,
    recoverability, prevention point, enforcer, human gate, identity, open questions).
- **How-to given.** Yes — 6 steps (inventory every tool → consequence & recoverability → prevention
  point & control type → human review capacity → rewrite the boundary as an enforceable condition +
  define one negative test → summary). Notices tools missing from the business narrative
  (`update_supplier_contact`).
- **Exercise.** PayFlow Agent, 11 tools, worktable xlsx + summary docx; 780 × 8% = 63 cases vs 480
  capacity → capacity fine but gateway doesn't require approval; shared `payflow-prod` credential →
  attribution gap. Plugin "Price the human checkpoint" (sliders; verdict "performable but
  bypassable"). Optional chatbot role-plays the over-confident engineer. Coaches: "Trace one action
  to the thing that can refuse it", "Govern authority before expanding agentic AI".
- **Gaps.**
  - The learner never configures or tests an agent: never writes the permission set, never runs the
    negative test, never sees a tool-call log, never runs an interruption drill ("you are not being
    asked to implement identity controls, design an audit system, run an interruption drill").
  - No agent-specific threats (prompt injection via supplier emails/invoices, data exfiltration),
    which is exactly how such an AP agent gets attacked.
  - No staged rollout plan (shadow → approve-each → threshold → supervised), no metrics for
    promoting a rung, no rollback runbook.
  - No vendor-feature governance: how to catch "a vendor update switched on agentic features"
    (release-note monitoring, admin-console settings review).

## Module 5 — Responsible Deployment in Practice

- **Scenario/role.** A finished customer-financing (store credit, US) model beats baseline in shadow
  evaluation; final validation shows approval 60% vs 48% (ratio 0.80); launch on the roadmap.
  Learner = issues the verdict with the credit executive as named authorizer.
- **Concepts.**
  - "Ungated launch": no criteria, no gate that can fail, no named person who can fail it.
  - Gate question = a principle rewritten as an evidence question that can be answered "no" / "not
    documented"; rate pass / flag / block; sort evidence into pre-authorization / continuing
    controls / post-launch-only.
  - Fix criteria before reading results.
  - Fairness metrics named (outcome-rate ratio, demographic parity, equalized odds, calibration,
    predictive parity) and the impossibility of satisfying all when base rates differ; metric choice
    is a documented judgment; 0.80 is an internal screen, not a legal safe harbor.
  - Verdicts: ship / ship with conditions / wait. A block rules out both ships. A condition binds
    only with metric, warning threshold, hard limit, cadence, owner, stop authority, escalation,
    response. "We'll monitor and improve" binds nothing.
  - Deployer duties remain when you buy; adverse-action reasons (ECOA) need feature-level logging.
  - Decision record incl. dissent; cost of delay must be stated honestly.
  - IBM's Pillars of Trustworthy AI referenced.
- **How-to given.** Yes — 6 steps (bound → rate 3 gates with citations → read the disparity measure
  with sample sizes/CIs → verdict → condition or N/A → challenge with opposite verdict, record
  dissent). Demo result: Wait (adverse-action explanation = block).
- **Exercise.** `store-credit-evaluation-brief.docx`, `deployment-decision-record.docx`,
  `assistant-instruction-block.txt` (chatbot restricted to the brief). Plugin "Gate rating and
  verdict". Coaches: "Ship, ship with conditions, or wait" and "The deployment verdict: interviewing
  for AI governance judgment".
- **Gaps.**
  - Only three gates, pre-populated. The learner never writes a full gate checklist for a use case
    type, never decides which gates are mandatory, never runs the launch review meeting.
  - Never computes a fairness metric or sees the data; never chooses a mitigation and re-tests.
  - No post-launch side: monitoring dashboards, drift checks, complaint/appeal handling, incident
    response, rollback.
  - Credit-model framing (classic ML); little on GenAI deployment gates (hallucination rate,
    groundedness, harmful-output tests, red-teaming, transparency notices to users).

## Course-level verdict

**Reuse as vocabulary (don't re-teach, point to it):** designed vs effective posture; the four
oversight postures; control-credibility test and "unearned green"; capacity screen; mechanism
sentence for risks; actor–source–date check and claim card; authority gap, behavioral instruction vs
authorization boundary, last reversible moment, recoverability bands; gate question, pass/flag/block,
ship / ship-with-conditions / wait, enforceable condition fields. The "perspectives" device (each
role says what it owns) is a good template for our persona packs.

**Fill:**
1. Building governance from zero in a real org: AI inventory discovery (shadow AI, SaaS feature
   updates), intake process, governance committee charter, acceptable-use policy, approved-tools list.
2. Producing the evidence instead of reading it: sampling outputs, building test sets, computing
   error and subgroup metrics, running negative tests and interruption drills, reading real logs.
3. Full regulatory map across the inventory and beyond the EU AI Act (GDPR/DPIA, Israel Amendment 13,
   US state laws, sector rules, works councils), plus the deployer's concrete document list and how
   to brief counsel.
4. Agent implementation governance: permission configuration, identity setup, prompt-injection
   threats, staged autonomy rollout with promotion metrics and rollback runbook.
5. Post-launch operations: monitoring, incidents, complaints/appeals, re-certification on vendor
   model changes; and vendor contracting (questionnaire, DPA, change-notification, exit).
6. Real conversations inside an org (the coaches are mostly job-interview role-plays), and running
   the meetings (risk workshop, launch review, governance committee).
