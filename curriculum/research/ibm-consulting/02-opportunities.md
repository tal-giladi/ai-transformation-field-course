# IBM Consulting cert, Course 2 — Identify and Prioritize AI Opportunities (notes)

Read 2026-11-02: all video transcripts (4 modules, ~78k chars). This course has **no coach
role-plays** (plugins only). Opening a plugin redirected to the course landing page (Tal is not
enrolled in this course; the transcripts were still readable), so no plugin was inspected here.
Slug: `identify-and-prioritize-ai-opportunities`. Notes in our own words.

Learner seat: "enterprise AI transformation consultant" / management analyst / transformation lead.
Scenario: the same multinational manufacturer — a call for AI ideas across supply chain, quality,
plants, sales/service, finance, HR returns a spreadsheet of a few dozen rows in incompatible units.

## Module 1 — Finding AI Opportunities

- Scenario: dozens of submissions, each in its own unit (days of inventory, escapes per million,
  handle time, an unexplained currency figure); a drafting assistant already used by several hundred
  people never appears because "nobody proposes what they already use"; the queue worker is absorbing
  the checking colleagues skipped.
- Concepts:
  - **Workflow anchor / process literacy**: a candidate is a claim about one step of a named
    workflow; walkable on paper (steps, owner per step, volume, trigger) or it is "not yet a
    candidate" (mapping comes first). Automating an unwalkable process amplifies its errors.
  - **Value and effort as two separately argued measures** (never a blended score).
  - **The ledger**: for every "time saved", who now reviews, corrects, escalates or waits? Saved for
    whom? (work relocates downstream, often to the customer).
  - **Opportunity density**: functions whose output is judgment, writing, analysis, coordination are
    dense in candidates; physical-throughput functions are sparse — estimate the share before hunting.
  - **Descriptive → predictive → prescriptive** spectrum: report needs a review step, predict needs
    uncertainty communication, prescribe needs an approval gate (heaviest governance).
  - **Bottom-up vs top-down discovery** — use both as filters: bottom-up finds what is real,
    top-down finds what is fundable; keep only candidates that survive both conversations.
  - **Three feeds** for the candidate list: submissions, what people already use, top-down value.
  - "Build the ruler before the list": inventory → both estimates → compare; ledger line per entry.
- How-to: moderate (fixed order; ask the worker "what eats your hours", ask the budget holder "what
  process improvement matters"; restate each entry as workflow + owner + value + effort + ledger).
- Gaps: no interview guide or observation protocol; no worked inventory; no template; no method to
  find "what people already use" (logs, licences, browser tools); no measurement of volumes/times.

## Module 2 — Qualifying Candidate Use Cases

- Scenario: unscored backlog sorts itself by pitch and seniority; top candidate (flag incoming
  shipments that will be out of spec) leaves the room as "revisit after data check".
- Concepts:
  - **Decompose a candidate**: rule vs learned-pattern per step (invoice example: extraction =
    interpretation; sum check = arithmetic; routing above a threshold = a chosen rule). Don't pay for
    ML where a rule works; don't under-govern the judgment steps.
  - **Seven screening dimensions**, kept separate: business value, workflow fit, data readiness,
    technical/financial feasibility, risk, sponsorship (named owner after the project team leaves),
    measurement clarity. Each blank = a person you haven't asked.
  - **Accuracy vs actionability**: right prediction that arrives after the decision closed is
    worthless; actionability is fixed by timetables/approvals/training, not models. Ask: who receives
    it, which decision changes, what they do differently that day.
  - **Data-readiness gate** (pass/fail, not a trade-off): inputs reachable, trusted, lawful for the
    purpose; **the label question** — was the outcome recorded consistently? If not, "wait" and start
    an outcome-recording project with an owner and a start date.
  - **Blast radius**: who/what a wrong output touches and how widely; reversible or not; locates the
    human approval line. Swap test: exposure should change with use, not with technique.
  - Qualify against the **existing workflow** (baseline + promised improvement) for the fast screen;
    AI-redesigned workflows are later work.
  - Verdicts: **proceed / proceed with a stated condition / stop and reconsider**, naming the
    dimension the verdict turns on and who owns the next step.
  - Agree in writing before seeing candidates which classes always get real scrutiny (output reaches a
    customer/supplier, irreversible, data without clear right to use).
- How-to: yes — one sentence per dimension; three-question actionability test; label question;
  blast-radius two questions.
- Gaps: no screening sheet; no example of a full backlog screened; no data check procedure (how to
  confirm labels exist, sample the records); no legal "lawful for purpose" method (Israel/GDPR).

## Module 3 — Prioritizing with a Value-Effort Lens

- Scenario: 12 candidates, a 2-hour scoring session; the top pick comes back "not ready to sequence"
  because the inspection review team can't absorb its flags, the risk reviewer's "low effort" meant
  light paperwork, and strategy (learning value) wasn't in the room.
- Concepts:
  - **Locked scoring criteria**: written, weighted definitions of impact and effort agreed before the
    list is opened; test: scorers can state them with the list closed. Include risk, compliance,
    business-line and strategy voices in setting them.
  - **Effort decomposition**: data condition, integration surface, regulatory/compliance burden,
    adoption resistance — each scored separately with an owner; reveals the dominant friction and a
    "reshape" move (e.g. nightly export instead of live integration).
  - **Absorption capacity**: receiving team's throughput (items/period at a standard); surplus becomes
    headcount, speed (errors) or a queue — get the number from the team.
  - **Direction of expensive error**: false alarm vs miss — which costs more is business-specific;
    subtract the cost of errors from the claimed benefit before ranking.
  - Chain: locked criteria → error direction → decomposed effort → only then plot the grid; read a
    finished grid backward.
  - When the sponsor's item ranks 4th: criteria were locked, name the friction, give a reshaping
    condition.
- How-to: yes (sequence and tests), but no worked numbers beyond small examples.
- Gaps: no scoring workshop facilitation (agenda, independent scoring, calibration); no weighted
  criteria example; no worked expected-error-cost calculation; no spreadsheet.

## Module 4 — Building the Prioritized Opportunity Portfolio

- Scenario: 12 ideas, budget for 3; a supplier-correspondence assistant request overlaps tools
  already built at two plants (different data paths); a plant lead built his own tool 8 months ago.
- Concepts:
  - **Portfolio** = the whole population held together; rank only means something against it.
    Assemble the full set first (include what nobody submitted), restate every entry in one unit:
    a business process + expected benefit.
  - **Benefit and effort as separate axes**; fund a deliberate mix (quick returns + one larger bet);
    benefit evidence is stronger when the org already logs the measure.
  - **Regulatory exposure before value**: classify by what it decides, whom it affects, how much human
    review — oversight costs enter the effort axis before ranking (not as a late veto).
  - **Intake** = one tracked place recording every AI build and request (owner, where it runs, data
    touched) — visibility instrument to find overlaps. Early consolidation vs tolerated duplication:
    a question of when (grow → consolidate).
  - **Portfolio gate**: criteria bind only when a build asks to scale, get funded, or faces
    retirement; earlier gating starves experimentation; never gating pays twice.
  - A portfolio also decides what to **stop**; "fund nothing new this cycle" is a valid result.
  - Telling the losing sponsor: a position, an axis and a condition — not a verdict.
- How-to: moderate (start an intake this week with a shared document and five colleagues).
- Gaps: no intake form design; no consolidation playbook (merge two plant tools, keep the builder
  motivated); no stop/retire steps; no resourcing-decision document template.

## New vs first certificate

New:
- **Discovery as consulting method**: three feeds (submissions, already-in-use, top-down), bottom-up
  and top-down as two filters, opportunity density, workflow anchor / "not yet a candidate".
- **The ledger** (who absorbs checking downstream) and **absorption capacity** (receiving team
  throughput) as part of value/effort — the first cert only had the capacity screen in governance.
- **Screening**: decomposition rule-vs-learned per step, seven dimensions, data-readiness gate with
  the **label question**, accuracy vs actionability, blast radius, three-verdict screen.
- **Prioritization rigor**: locked criteria before opening the list, effort decomposition into four
  frictions, direction of expensive error netted from benefit.
- **Portfolio mechanics**: one unit (process + benefit), regulatory exposure before value, intake as a
  visibility instrument, portfolio gate timing, stopping things.

Repeated: value–effort grid and 2×2 (first cert course 2), "use AI is not a strategy", sponsor's pet
idea losing, readiness bottleneck, shadow AI. Still narrated, one manufacturer, no data to work on.

## Implications for our plan

1. **Extend 02.2/02.3**: process literacy as a pass/fail ("walk it on paper: steps, owner per step,
   volume, trigger" — else "not yet a candidate"); interview prompts "what do you repeat / what eats
   your hours" for workers and "what improvement would clearly matter" for budget holders.
2. **Extend 03.1** (opportunity map) with the **three feeds** (submissions + already-in-use + top-down),
   opportunity density per function, and the report/predict/prescribe placement with its oversight
   need. Template `use-case-scorecard.md` gets: workflow anchor, rule-vs-learned per step, seven
   dimensions, ledger line, error direction, blast radius, verdict.
3. **New 03.2b → renumber as needed: "The fast screen"** (or fold into 03.2): seven dimensions,
   data-readiness gate with the **label question** (hands-on: check the data room for whether the
   outcome was ever recorded), actionability test, proceed / proceed-with-condition / stop.
4. **Extend 03.3** (scoring workshop): lock weighted criteria before opening the list (with strategy,
   risk, compliance, business-line voices), independent scoring, effort decomposition into four
   frictions with owners, reshape moves. Add to the `portfolio-sorter` simulation: a "criteria lock"
   step, an absorption-capacity number that must be asked for, and expected-error cost netted from
   benefit.
5. **Extend 03.5** (ROI model): net the **cost of the expensive error direction** from benefit; add a
   ledger line (review/rework moved downstream) to the model.
6. **Extend 04.7** (governance that runs): an **intake register** for every AI build and request
   (owner, where it runs, data touched), overlap detection, and a **portfolio gate** applied only when
   a build asks to scale, be funded or retire. Template `ai-intake-register.md`.
7. **Extend 07.2** (scale/fix/stop) with "fund nothing new this cycle" and **consolidation of
   duplicate builds** (two plants' tools with different data paths; keep the builder's goodwill).
   Strongest fit: engagement 15 (bank, 40 pilots) — add duplicate builds and a merge decision to its
   data room.
8. **Persona types**: the queue worker who absorbs others' skipped checking; the receiving-team lead
   who knows the throughput nobody asked for; the plant lead who built his own tool; a BI analyst who
   sees two data paths where others see one; a head of strategy who values learning over payback.
9. **Data-room additions** (all engagements): a submissions spreadsheet in mixed units (learner must
   restate to process + benefit); an already-in-use tool absent from submissions; at least one
   candidate whose outcome label was never recorded (factory, module 13, is the natural home).
