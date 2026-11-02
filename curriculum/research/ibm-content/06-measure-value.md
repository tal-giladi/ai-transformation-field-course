# IBM course 6 — Measure AI Value and Scaling Transformation

Read 2026-11-02 (all transcripts and readings). Slug `ibm-measure-ai-value-scaling`. 4 modules, ~4 h.
Same thin format as course 5: intro, problem story, "perspectives" (4–6 roles), terms reading,
concepts video, "portable skill / interview answer" video, AI-graded assignment, 15-min plugin.
**No exercise guide, no LabBook files, no expert demo, no coach role-play.** Plugins are public at
`ianmelchinger-lang.github.io/LeadTrans/` (`C6M1_NetClaim.html`, `LeadTrans_C6_M2.html`,
`C6M3_GateVsReadiness_activity.html`, `C6M4_PrioritizeMaterialIssues.html`).

## Module 1 — ROI Frameworks for AI

- **Scenario/role.** A BU pilot reports "20 hours a week saved"; the board wants ROI; the finance
  business partner produces a round figure; the CFO won't carry it. Perspectives: finance business
  partner, CFO, BU ops leader, downstream operator (owns the rework), AI transformation leader.
- **Concepts.**
  - "Mystery benefit claim" — gross hours with no baseline, no counterfactual, rework not subtracted,
    capacity mistaken for cash.
  - Simple ROI, payback, NPV, IRR — each answers a different question; hurdle rate.
  - Baseline (cycle time, cost to serve, error rate, throughput) + credible counterfactual
    (comparison group, phased rollout, matched cohort, controlled test, adjusted forecast).
  - Full lifecycle cost: integration, data work, testing, security/compliance review, training,
    monitoring, human review, support, decommissioning.
  - Net capacity created = gross time removed − new review/correction/coordination/rework.
    Capacity → realized value only through redeployment with a measured outcome; → cashable saving
    only via observable avoided spend (hiring, overtime, contractors).
  - Value categories: financially quantified / non-financial outcomes (quality, workforce,
    customer, risk) / strategic option value (describe, don't monetize without a scenario). Evidence
    status separately: measured / estimated / forecast.
  - "Return on autonomy" read across the same categories; autonomy counts only if outcomes improve
    after oversight and risk costs.
  - Leading indicators (adoption, coverage, proficiency) ≠ realized operational outcome ≠ realized
    financial return.
  - Enterprise ledger: where each benefit lands and where verification, rework, delay, risk land;
    deduct only the shifted portion. If review can't be done at volume → control gap.
  - "Bank what you can defend"; "not yet demonstrated" is a professional result; overclaiming loop.
- **How-to given.** A sequence in the interview answer (baseline & counterfactual → net capacity →
  mechanism to outcome/cash → categorize → mark evidence status → lifecycle cost → horizon → allow
  "not yet"). No spreadsheet model, no worked numbers in the videos.
- **Exercise.** Plugin "Net the claim" (`C6M1_NetClaim.html`): 50 people × 3.0 h × 52 × $75 =
  $585k vs $150k → "290%"; learner files five slices into Banked (0.75 contract not renewed + 0.30
  temp staffing ended) / Capacity (0.90) / Rework (0.60) / Transfer (0.45 to payments team); sliders
  for loaded rate and TCO; "not yet is a finished answer".
- **Gaps.**
  - Never builds an ROI model: no template (inputs, scenarios, sensitivity), no worked NPV, no
    TCO checklist with real price points (seat licences, API tokens, platform fees, integration
    days), no token-cost estimation for a GenAI workload.
  - Never measures a baseline: how to pull cycle times/volumes from a ticketing or ERP export, time
    studies, sampling — all assumed.
  - Never designs the counterfactual: how to set up a phased rollout or matched teams in a real org,
    sample sizes, how long to run.
  - No conversation with finance on how they want it (their template, hurdle rate, how they treat
    capacity) and no example of a value case finance actually signed.

## Module 2 — Build the AI Measurement System

- **Scenario/role.** Usage curve climbs, outcome flat; a claims team's cycle time drifts 18 → 26
  days in one quarter and the monthly report catches it late. Perspectives: AI transformation lead
  (owns the chain), BU leader (owns the bottleneck), finance (owns attribution), executive sponsor
  (owns the decision view).
- **Concepts.**
  - "Missing chain": deployment → telemetry dashboard, skipping goal and drivers.
  - Goal–driver–indicator chain built backward (objective + success criterion + target + horizon →
    2–3 drivers → indicators + baseline). The chain is a hypothesis to test.
  - Indicator vs KPI; leading/lagging are relative to a goal and horizon; candidate leading signals
    (workload trajectory, processing-time variance, exception clustering) and three ways to find
    them (statistical input/output analysis, value-stream mapping, owner/customer role-play).
  - Guardrail measures (quality, error, safety, compliance, customer, workforce, cost); review
    cadence per measure.
  - Baseline vs credible comparator; movement ≠ attribution.
  - Stage-appropriate metrics (exploring → adoption/learning; optimizing → efficiency; enhancing →
    quality; transforming → new capability).
  - Imperfect proxies (rework %, time in review, escalations per sprint) with rationale, limits, how
    it could be gamed; or an explicit measurement gap.
  - "No KPI without an objective, no success claim without a target, no impact claim without a
    credible comparison." Every material signal → owner + response.
- **How-to given.** The backward chain order; principles. No template, no example chain.
- **Exercise.** Plugin "Build the AI measurement system" (`LeadTrans_C6_M2.html`). AI-graded
  assignment.
- **Gaps.** No data plumbing: where the numbers come from (CRM, ticketing, ERP, AI tool admin logs),
  how to instrument a workflow, how to build the dashboard, how to reconstruct a baseline from history,
  how to run the statistical/value-stream analysis it names. No example board view.

## Module 3 — Decide Which Pilots to Scale

- **Scenario/role.** A 10-week regional customer-ops pilot: accuracy held, handling time dropped,
  survey glowed; sponsor wants every market. Pilot ran on pre-cleaned data, 20 attentive users, a
  narrow slice, low volume, one integration with workarounds, engineer on call. Perspectives: AI
  program lead (owns verdict), BU leader, data/platform leader, risk/compliance, finance/value,
  change/people.
- **Concepts.**
  - "Pilot isn't scale"; PoC vs pilot vs productionization vs scaling; flattering pilot conditions.
  - Target operating envelope (users, use cases, volume, locations, integrations, autonomy, service
    expectations, consequence of failure) — "ready for what, exactly?"
  - Judge the whole AI-enabled system (pipelines, interfaces, prompts, human roles, rules, vendors,
    controls), not the model. GenAI output shifts when a vendor updates a model.
  - Non-compensable gates (legal permissibility, unacceptable safety/rights risk, security & privacy
    controls, minimum performance, accountable ownership, monitoring & response plan) rated pass /
    not passed / insufficient evidence — before readiness factors (value, operations, governance,
    change, sponsorship) rated ready / ready with conditions / not ready / insufficient evidence.
  - Oversight tested under representative load before expansion; rollback can't unsend decisions.
  - Verdicts: scale / sustain / retire ("not yet" = timing condition on sustain). A review that can
    only say yes is a sales document.
  - Sources cited: OECD lifecycle guidance, NIST AI RMF, GAO accountability framework.
- **How-to given.** The review sequence: envelope → gates → readiness → net value across workflow →
  verdict with decisive evidence, uncertainty, conditions, owner.
- **Exercise.** Plugin "Gate or readiness factor?" (`C6M3_GateVsReadiness_activity.html`).
- **Gaps.** No production-readiness checklist (load test, integration hardening, support model, SLA,
  runbook, on-call), no method to test transfer (shadow run on production data, staged rollout by
  market, canary), no portfolio triage of many pilots at once with a budget constraint, no
  decommissioning steps for "retire", no template for the review document.

## Module 4 — Build Durable AI Capability

- **Scenario/role.** A scaled customer-service AI tool; project closed, team dispersed; months later
  nobody can say if it still works; silence misread as satisfaction. Perspectives: AI program lead
  (owns rhythm), BU leader (lesson that travels), value owner (proportionate overhead), platform lead
  (triggers).
- **Concepts.**
  - "Nobody is watching"; launch = handoff into operational management, not end of responsibility.
  - Improvement cycle: collect signals → synthesize → controlled change → evaluate → communicate;
    outcomes continue / investigate / adjust / roll back / restrict / retrain / reinvest / suspend /
    retire.
  - Accountable owner (one named person, not a committee) + documented supporting roles.
  - Proportionate monitoring sized to impact, risk, volume, rate of change, dependencies, regulation,
    speed of harm; sample vs continuous; purpose-limited data collection.
  - Balanced signal set (outcomes, quality, reliability, safety, fairness, security, privacy, cost,
    usage, overrides, complaints, incidents, affected-people feedback) with a baseline at deployment.
  - Escalation trigger ≠ review cadence: threshold → who is notified, who may act, how fast, which
    response (investigate, override, rollback, restrict, suspend, incident response, escalate).
  - Smallest adequate intervention, tested, guardrails re-checked, rollback path kept.
  - Say "performance or context change" rather than "drift" until you know what changed.
  - Portfolio version: tier systems by impact/risk, set monitoring per tier, reuse existing forums
    where they have expertise and authority.
- **How-to given.** Four beats: own it, watch it, act, learn; the interview answer lists the steps.
- **Exercise.** Plugin "Prioritize material issues" (`C6M4_PrioritizeMaterialIssues.html`).
- **Gaps.** No operating-rhythm calendar, no RACI for a running AI service, no monitoring spec for a
  GenAI system (sampled output review, eval suite re-run on vendor model change, cost alerts), no
  incident runbook, no handover document from project to operations, no change-control process for
  prompts/models.

## Course-level verdict

**Reuse as vocabulary:** mystery benefit claim; gross vs net capacity; capacity vs cash (banked /
capacity / rework / transfer); credible counterfactual; measured/estimated/forecast; enterprise
ledger; bank what you can defend; goal–driver–indicator chain; leading/lagging relative to horizon;
guardrail metrics; target operating envelope; non-compensable gates vs readiness factors; scale /
sustain / retire; accountable owner; proportionate monitoring; escalation trigger vs review cadence.

**Fill:**
1. A real ROI/TCO model (spreadsheet) with GenAI cost lines (seats, tokens, platform, integration,
   review time), scenarios and sensitivity — built on data, signed off with finance.
2. Measuring baselines and running counterfactual designs in a live org (pull exports, time studies,
   phased rollouts, matched teams), then the dashboard itself.
3. Production-readiness and transfer testing for scale (shadow on production data, staged market
   rollout), portfolio triage with budget limits, decommissioning.
4. Operating the live system: monitoring spec, re-evaluation on vendor model updates, incident
   runbook, change control for prompts/models, project-to-operations handover.
