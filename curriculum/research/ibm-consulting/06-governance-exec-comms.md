# IBM Consulting cert — Course 6: AI Governance, Risk, and Executive Communication

Read 2026-11-02 from the full video transcripts (~69k chars). Interactive widgets (≈28, e.g. "Name
the question first", "Classify by condition", "Place the check", "Find the load", "One sentence test",
"Seam check", "Four question spec", "Control trace", "Assemble the account") could not be opened —
not enrolled. No readings. Same format: problem → four truthful role-holders → concept videos +
widget → skill as interview answer → dialogue activity. Learner = outside advisor to the
multinational manufacturer.

## Module 1 — AI Governance and Ethics ("reading the gap")

- **Scenario/role.** Risk and compliance lead hands over an approved responsible-AI policy and a
  one-page review form; nobody owns the live register, deviation triggers, restricted-use list or
  post-launch monitoring; service and plant teams use tools that never entered review; a quality
  engineer stopped using a tool because nobody could say if it was allowed. Use case: a warranty
  claim declined by an automated scorer/router using a replaced rule, with an assistant writing the
  customer letter. Four readings: compliance lead, counsel (two governed activities registered as
  one), named reviewer (wrong items look like right ones), **the claimant** (wants a usable reason).
- **Concepts.**
  - Three instrument types answer three questions: NIST AI RMF (how to think about risk), ISO/IEC
    42001 (a certifiable management system), EU AI Act (what the law requires of whom). Ask which
    question the client means first.
  - Governance across the life cycle; checklist organization vs infrastructure organization (settle
    criteria once, reuse them — governance that saves time).
  - Six-part governance anatomy: approved use cases (purpose, users, feasibility evidence, risk
    assessment, oversight model, security/access review, operating owner, monitoring and escalation
    commitments), restricted use cases, data boundary (what data, where it travels, who sees
    inputs/outputs/logs, vendor training, retention), model risk evidence, monitoring with thresholds
    and a named responder, escalation path (trigger, owner, response, authority).
  - Risk classification by checkable conditions, not by feel; settle it first.
  - Give the board three numbers: what reaches production, how long decisions take, what is declined
    and why.
- **How-to given.** Five verbs: classify (name the trigger) → scope obligations with owner or named gap
  → test every person-control for volume, cadence, detectability → ask the fairness question where
  outputs sort people → document reasoning and track review-process performance.
- **Gaps.** No register template, no restricted-use list example, no charter, no data-boundary
  document, no fairness test actually run; Israel and other jurisdictions absent (EU only).

## Module 2 — AI Risk Management ("risk before capability")

- **Scenario/role.** Agentic workflow on a customer-exception path retrieves terms from a document
  store, classifies, messages the customer and updates the record. "Works" (volume up, no
  escalations). The risk page lists categories, each with "a person will review the output". A
  replaced document went to a customer; 11 days until the customer's contract manager asked. Four
  readings: compliance lead, workflow engineer (got a goal and tools, never a boundary — no
  freshness check), named reviewer (flags go nowhere), operations owner of the agent fleet (can't
  enumerate agents; wants independent sampled audits).
- **Concepts.**
  - Authority grant: governance attaches to the permission to act, not to the model; one deployment
    = a judgment + a grant; applies to rules engines and scoring wired to dispatch too.
  - Classify twice: by regulation (intended purpose, consequence) and by authority (what it may do
    without a person). Legal determination goes to counsel with the facts.
  - Continuous risk management loop; supplier's governance travels with a supplied capability;
    record which obligations belong to which party.
  - Oversight failure (system as specified, person defers to wrong output) vs malfunction; in
    sequences, end-review is too late → halt conditions, approval gates, escalation at named steps.
  - Reviewer complacency: two causes — no consequence for flags (accountability) and load/reliability
    (attention drifts when the system is usually right); fix both.
  - Misattributed responsibility (moral crumple zone): a control is only real if the named person
    has time, the source beside the draft, and authority to halt.
  - Detectability: confidence ≠ accuracy; errors cluster in specific facts, recency, internal
    references → point verification there; arithmetic first (8 min × 200 drafts = 26+ h/day).
- **How-to given.** Six verbs: own it → classify it (twice) → name each failure at its step and where
  it travels → write controls a team could build from the sentence, draw data lines → set thresholds
  and load-test oversight → earn autonomy by evidence and close the loop. The "cannot list" (what the
  agent may never do, what forces handoff, what it logs) and evaluation evidence that it refuses.
- **Gaps.** No actual eval of refusals, no freshness-check implementation, no fleet inventory method,
  no sampled-audit procedure, no supplier contract clauses.

## Module 3 — Executive Communication ("the decidable sentence")

- **Scenario/role.** Executive committee pack decides whether to extend automated maintenance
  scheduling from 2 to 7 plants in 3 weeks. The pack says "outputs are reviewed"; the earlier draft's
  numbers (one reviewer, one shift, two sites, growing queue) were trimmed away on the way up
  (organizational silence: each relay has more to lose by delivering bad news). Use case: a work
  order passed review against the wrong equipment after expansion. Readings: CEO, compliance
  officer, named reviewer, **board member** ("I was told there was oversight").
- **Concepts.**
  - The four L's: lead with the decision and the date; land the hard finding once, unhedged; label
    evidence vs inference; leave two or three live options with costs.
  - Answer-first / bottom line up front; the one-sentence test (if it needs a subordinate clause the
    position isn't settled).
  - Evidence vs inference seam — keep it visible, especially for bad news.
  - Explainability as a requirement per audience (builder, executive, auditor later, affected
    person); four-question spec: what explanation, who receives it, what evidence, below what
    threshold it stops being explainable enough.
  - Frame risk in governance terms, not fear; frame it in each reader's sense of the word.
  - Every oversight claim carries volume, pace, detectability.
- **How-to given.** Six verbs: resolve, name, state, frame, attach, close.
- **Gaps.** No live delivery practice (presenting, handling interruptions, the sponsor who wants the
  finding softened), no slide/deck format, no rehearsal with hostile executives.

## Module 4 — Bringing the Advisory Story Together ("synthesis under contradiction")

- **Scenario/role.** After most of a year the advisory team delivered five documents (opportunity
  assessment, readiness report, governance and risk plan, roadmap, ROI case); each sound alone; the
  committee could not vote. The top use case's plant data isn't consolidated until wave 2; the
  governance plan commits a reviewer whose minutes neither the roadmap staffed nor the ROI case
  costed. Readings: committee chair/COO, CFO, CRO, data and technology lead.
- **Concepts.**
  - Cross-document contradiction: one document needs true what another denies or omits; lives only at
    the boundary.
  - Assembly order (evidence upward) vs delivery order (answer first; Minto's Pyramid Principle).
  - Narrative spine: what is true now → what changed → the question it raises → the single answer;
    two answers competing for the slot = unreconciled documents.
  - Integration = reasoning across documents by purpose ("question-first reading").
  - Disclose the tension to the sponsor early; a quiet fix takes the decision away from its owner.
- **How-to given.** Four verbs: find the contradiction, trace every human control to cost and
  staffing, map onto the spine, write answer-first and check what went quiet.
- **Gaps.** No integration checklist/template, no worked package, no practice with a real board pack.

## New vs first certificate

Repeated (first cert course 4): oversight that operates vs designed, capacity screen/load test,
control credibility, regulatory reading (actor–source–date), classification by conditions, agentic
authority, deployment verdict. New or sharper here:
- **Six-part governance anatomy** (approved uses, restricted uses, data boundary, model risk evidence,
  monitoring with responder, escalation path) and "infrastructure vs checklist" governance.
- **Three instrument types** as three different client questions.
- **Classify twice** (regulation and authority grant); supplier governance boundary.
- **Human-factors depth**: reviewer complacency (two causes), moral crumple zone, detectability and
  where errors cluster → point verification.
- **The affected person's view** (the claimant) and explainability as an audience-specific requirement.
- **Executive communication** as a skill: four L's, answer-first, evidence/inference seam,
  organizational silence (bad news softened on the way up).
- **Integration of five deliverables** and cross-document contradictions; narrative spine.

## Implications for our plan

1. **Extend 04.7 (governance that runs)** with the six-part anatomy as the governance charter's
   skeleton, the "three numbers for the board" metric (reached production, decision time, declined
   and why), and the three-instrument question for the client. Template: **approved/restricted use
   list** and **data boundary** sheet (add to the policy pack).
2. **Extend 05.5 (human-in-the-loop)** with detectability and point verification, the two causes of
   complacency (flags that go nowhere; load and reliability), and the crumple-zone test (time,
   source beside the draft, authority to halt). `oversight-under-load` gets a "flag feedback on/off"
   and "source shown/not shown" toggle.
3. **Extend M14 (Lumen SaaS)** with the authority-grant reading and the "cannot list", plus a planted
   **stale-source incident** (replaced document still retrieved, 11 days to discovery) and an agent
   fleet the operations owner cannot enumerate.
4. **New lesson 07.9 — "Delivering bad news upward"** (four L's, answer first, evidence vs inference,
   the finding stated once, live options; resisting the softening relay). Practical: rewrite a
   softened committee paper (provided) and deliver it in a roleplay to a sponsor who already told the
   board a number. Ties to the capstone's "hardest finding to the executive most likely to resist".
5. **New lesson 18.2a / extend 18.2 — "Integrate the package"**: cross-document contradiction check
   across our deliverables (charter, findings, portfolio + ROI, policy pack, pilot + eval, adoption
   plan, roadmap, decision-ready case), narrative spine, one recommendation. Template: **integration
   check** (each human control traced to its cost line and staffing quarter; each claim's timing
   traced to readiness and roadmap). Also apply it in every NN.6 debrief.
6. **Persona types to add**: the **affected person** (claimant/customer/citizen who wants a usable
   reason — M9 insurer, M11 municipality), **counsel** (identifies exposure, won't decide priority),
   **board member** (heard "there is oversight"), **agent fleet/operations owner** (M14, M15).
7. Israel-first note: the course is EU-only; our 04.6 must cover the Israeli instrument types
   (Privacy Protection Law and Amendment 13, PPA guidance, sector regulators) with the same "which
   question are you asking" framing.
