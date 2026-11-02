# IBM Consulting cert — Course 4: Design AI Transformation Roadmaps

Read 2026-11-02 from the full video transcripts (25 videos, ~71k chars). Tal is not enrolled in this
certificate, so the interactive items (≈28 "plugin"/dialogue widgets per course, e.g. "Gate or
date?", "Mind the queue", "Assemble the process") redirect to the landing page and could not be
opened. There are no readings in this course; the widgets are the only exercises.

Course shape: 4 modules (2h, 2h, 2h, 1h). Every module = overview → "the problem" → one use case
told by four role-holders who all tell the truth but disagree → 4–6 concept videos each followed by a
short widget → a "skill" video that frames the skill as a job-interview answer (weak vs strong) and a
"first months in the role" example → a dialogue activity. Learner role throughout: an outside
**AI transformation advisor** to a **multinational manufacturer**. Mentions IBM watsonx Orchestrate
as the agentic reference platform.

## Module 1 — Roadmap Fundamentals ("sequencing to the precondition")

- **Scenario/role.** Advisor to the manufacturer's transformation lead, 8 weeks before a funding
  review. A visible pilot, a long-waiting initiative, a vendor-backed assistant with executive
  attention, and several easy automations. Use case: a visual-inspection assistant whose approved
  expansion phase to three sites never started. Four readings: BU sponsor (owns the benefit), central
  platform/governance owner (owns the intake queue), site operations lead (solves locally if blocked),
  quality engineer (owns the verification load).
- **Concepts.**
  - Place by value *and* readiness; horizon buckets (near / mid / later).
  - Phase gate = a yes/no condition, not a date ("advance when the archive has an owner and legal
    approved", not "begin in October").
  - Dependency written as a checkable precondition.
  - The ledger question: where the benefit lands vs where the residue lands. Residue = verification,
    rework, absorbed expectation (e.g. suppliers now expect 1-hour bid answers). Benefit and residue in
    different places = a *transfer*, not a gain.
  - Centralize/federate allocation per initiative (standards, governance, reference architecture,
    platform stay central; implementation and local adaptation move out), bounded by the central
    team's review capacity per quarter.
  - Segment-by-segment scaling: a pilot's "it worked" describes its conditions; each new site/unit
    gets a small check of only what differs (data, workflow, risk); legacy estate sets how many checks.
- **How-to given.** Yes, a 7-move procedure: read value vs readiness → classify risk → place in a
  horizon → ledger question → each dependency as a gate → allocate central vs business against real
  capacity → scale by segment. Small "do this week" drills (rewrite a milestone as a yes/no sentence;
  count near-horizon reviews vs reviews the central team can finish).
- **Exercises.** One widget per concept ("Gate or date?", "Find the residue", "Mind the queue", "Test
  the segment") + "Assemble the process" dialogue. Not opened (not enrolled).
- **Gaps.** No roadmap is ever drawn: no template, no worked full roadmap, no Gantt/kanban, no intake
  tracker. "Ask the central team how many reviews it can do" — but no method to measure review
  capacity or build an intake queue. No conversation practice for telling the sponsor that the
  approved phase cannot start.

## Module 2 — Sequencing the Investment Portfolio Across Horizons ("reading the self-funding chain")

- **Scenario/role.** Same manufacturer: plants run inspection/maintenance pilots, corporate uses broad
  assistants, one technology budget line mostly locked into legacy, an AI CoE needing visible progress.
  Use case: the enterprise-wide assistant lost funding and a case-management deployment stalled 3
  weeks later because it relied on the familiarity the assistant was building. Four readings: plant
  leader, group finance lead, portfolio lead, CoE lead.
- **Concepts.**
  - Investment horizon = proof maturity + dependence on today's core business, not start date.
  - Acceptance dependency: a low-ROI broad assistant can be a precondition for a later system's
    adoption; cutting it deletes a dependency nobody wrote down.
  - Pilot-to-scale gate: four checkpoints (link to strategic goals, interoperable tech foundation,
    trained available team, compliant transparent operating practice) + a fixed measurement baseline.
  - Default allocation split (near-heavy reference split) adjusted by industry maturity and pace of
    disruption, with a stated review cadence.
  - Experiment discipline vs case discipline: cheap/reversible work on fast experiments tied to a
    named objective; expensive/irreversible/platform work needs a business case. Each lane states
    which discipline governs it.
  - Self-funding chain: each stage frees capacity or proves ground for the next.
- **How-to given.** Partly: re-sort an initiative list by evidence and dependency; write the
  acceptance dependency into the record before a cut is voted; run the four checkpoints in one
  sitting. No numbers worked end to end.
- **Exercises.** "Horizon by evidence", "Trace the dependency", "Run the gate", "Write the
  adjustment", "Set the boundary", "Assemble the process". Not opened.
- **Gaps.** No budget model (how capacity freed in H1 is actually redeployed and shown to finance), no
  portfolio register, no decision-record template, no worked example with money. No method to estimate
  the "acceptance" effect or prove it exists.

## Module 3 — AI-Enabled Workflow and Agent Opportunities ("controlling scope under uncertainty")

- **Scenario/role.** Roadmap has a line "agentic workflows" with labels only (supplier escalation,
  warranty triage, shift handover). A planner already built an unattended morning-briefing agent that
  reads mail and calendar. Use case: the briefing listed a customer commitment nobody recognised.
  Four readings: operations lead (decision boundary), central platform owner (layer and controls),
  business-based builder (deliverable), receiving planner (the residue — people changing how they
  write so the agent can read their work).
- **Concepts.**
  - Unit of work: chatbot = input→response, model = input→prediction, agent = goal pursued across
    steps; oversight must attach to the decisions along the way; every decision point needs a named
    owner — gaps get multiplied by autonomy.
  - Intervention fit: deterministic rules → ordinary automation; estimating from history →
    analytical model; drafts → generation; multi-step with judgment → agent. Sorted by recurrence and
    judgment.
  - Agentic surface: remove waste steps, leave rules to automation, put agents only at judgment steps
    (e.g. 2 of 40 month-end-close steps); several narrow agents beat one big one (versioning, blast
    radius).
  - Deployment layer (personal assistance / governed low-code by business builders / production
    agentic flows on core data with observability) and permission tier, set by reach and
    reversibility; the tier is the price tag.
  - Map first, then source (build/buy/partner); friction types: volume, judgment, coordination
    (coordination often needs no AI).
  - Residue/legibility work: people reformatting their work for the agent is real cost.
- **How-to given.** Yes, an 8-step framing procedure ("visible, small, real, checked"): map and find
  friction → simplify → match each step to an intervention → cut to the agentic surface → place in
  layer and name the builder → list system connections and upkeep → define verification before
  building → name the residue. Drills: write each decision point with an owner; mark steps rule vs
  judgment.
- **Exercises.** "Find the blank", "Match the step", "Cut to the surface", "Place it and price it",
  "Read the map", "Assemble the process". Not opened.
- **Gaps.** Never maps a real workflow from data (no process-mining, no event log, no swimlane
  template). No permission matrix, no connector/system inventory, no verification design (test set,
  negative tests), no cost estimate for an agent. Never builds even a read-only agent. Governance of
  citizen-built agents (intake, registry, kill switch) only named.

## Module 4 — Pressure-Testing the Roadmap ("the pre-failure reading")

- **Scenario/role.** Roadmap already approved; inspection pilot at one plant should prove benefit
  before others; dependency column says only "data availability, business readiness". Use case: a
  6-week slip at the second plant because records were kept in different forms. Four readings:
  transformation lead (owns dependencies), risk analyst (exposure, not delivery risk), gate reviewer
  (review load), plant operations lead (start date arrived before the promised demonstration).
- **Concepts.**
  - Planning ≠ pressure testing; approval is not a test; a "clean review" is worth only what the
    reviewer tried to find.
  - Wrong assumption (false today → correct it) vs fragile dependency (true today, may change →
    fallback, trigger, resequence, remove).
  - Reviewer independence (red team: someone who did not write the plan).
  - Delivery risk vs exposure; control load test (can the gate reviewer handle the volume).
  - Findings written as "what breaks, for whom, and when" + a disposition: correct, re-sequence, add
    fallback, de-scope, defer, remove.
- **How-to given.** Yes, 8 verbs: promise → fail (assume the key date was missed) → trace concrete
  causes → sort wrong vs fragile → load-test each control → trial (find what a small experiment can
  settle) → name the finding → route to an owner.
- **Exercises.** "Read the clean review", "Correct or answer", "Reopen the answer", "Assemble the
  process". Not opened.
- **Gaps.** No facilitation of a real pre-mortem with the plan's authors in the room; no finding
  log template; no example of a full pressure-test report; no handling of the political cost of
  challenging a plan the sponsor already showed the board.

## New vs first certificate

New (not in the first certificate):
- **Agentic opportunity framing** — intervention fit, agentic surface, deployment layers, permission
  tier as price, map-first sourcing, legibility residue. The first cert only governed agents
  (recoverability sweep); this one *designs* them.
- **Portfolio horizon logic** — proof maturity, acceptance dependency, self-funding chain, default
  split adjusted to industry, experiment vs case discipline.
- **Pressure-testing a plan** — pre-failure reading, wrong vs fragile, reviewer independence,
  dispositions.
- Central/federate as a per-initiative bundle bounded by review capacity, and segment-by-segment
  scaling with per-segment checks.
- The "four role-holders who all tell the truth" format — a good model for our persona packs.
- Advisor (consultant) seat instead of the C-suite seat; job-interview framing of each skill.

Repeated (first cert): "sequence for absorption" ≈ sequencing to the precondition; pilot isn't scale;
phase gates; centralize/federate/hub-and-spoke; capacity screen for reviewers.

## Implications for our plan

1. **New lesson 03.7 — "Agent or not: framing workflow opportunities"** (map → simplify → intervention
   fit by recurrence and judgment → agentic surface → layer and builder → connections and upkeep →
   verification → residue). Our 03.1 opportunity map has "automate/assist/augment/leave alone" but
   no step-level intervention fit. Practical: frame two Harbor & Pine candidates, one of which ends as
   "plain automation, no AI". Template: **agentic opportunity frame** (one page).
2. **Extend M14 (Lumen SaaS)** NN.3 with the deployment-layer/permission-tier pricing and the
   "several narrow agents" design; and add to the Lumen data room a **citizen-built unattended agent**
   (the morning-briefing pattern) that the learner must find, assess and either bless with
   guardrails or stop.
3. **New lesson 07.8 — "Pressure-test the roadmap before it hardens"** (pre-failure reading, wrong vs
   fragile, dispositions, independent reviewer). Our M7 has the steering meeting but no independent
   test of a plan. Practical: pressure-test a roadmap *written by someone else* (provided in labs) and
   produce a findings log. Template: **pressure-test findings log** (finding = what breaks, for
   whom, when; type wrong/fragile; disposition; owner).
4. **Extend 03.6 / 07.6** with horizon logic and the self-funding chain: each phase states what it
   frees or proves for the next; write acceptance dependencies into the decision record. Add an
   **acceptance-dependency** trap to M15 (Crescent Bank): the bank's broad Copilot rollout is on the
   cut list while two later initiatives depend on it.
5. **Roadmap template** (we listed none): gates written as yes/no conditions, horizon by evidence,
   central vs business allocation per initiative, review-capacity check, segment-by-segment scale
   plan, ledger column (benefit lands / residue lands). Add to `templates/`.
6. **Simulation tweak**: `operating-model-scaler` gets a central review queue with finite slots per
   quarter (near-horizon demand vs capacity) and per-segment checks.
7. **Persona packs**: adopt the "four truthful role-holders" pattern per incident/decision, and add
   two persona types we lack: the **business-based builder** (citizen developer shipping agents
   faster than intake) and the **receiving team** that absorbs residue (quality engineer / planner).
