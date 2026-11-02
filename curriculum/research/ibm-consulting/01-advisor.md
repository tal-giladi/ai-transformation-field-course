# IBM Consulting cert, Course 1 — The AI Transformation Advisor (notes)

Read 2026-11-02 from the logged-in course: all video transcripts (5 modules, ~93k chars), one coach
role-play ("Interview the VP of Customer Experience") and one plugin ("Assemble the process") opened.
Slug: `the-ai-transformation-advisor`. Certificate: IBM Enterprise AI Transformation and Consulting
(7 courses; this is course 1). Notes in our own words.

## How the course is built

- Same shell as the first certificate: overview → "Problem" story → "four accountable readings"
  (four roles describe one situation) → 4–6 short concept videos, each followed by a 1-question
  plugin ("Skill practice") → "Win the role" video → coach role-plays → AI-graded written
  assignment (staffGraded, not opened).
- **Seat changes:** the learner is now an **outside advisor/consultant** (not the C-suite owner).
  The videos explicitly target experienced consultants and frame every skill as an interview answer
  and a "first three months in the job" story (career/job-market framing throughout).
- **Scenario:** one fictional multinational manufacturer, re-used across all modules (forecasting
  assistant at one plant; 11 "AI systems"; a folder of documents before steering; a sponsor who has
  already promised the board a figure; a vendor demo + a widely quoted study + a headcount cut in the
  plan). No data, no documents to open — everything is narrated.
- **Plugins** are hosted at `ianmelchinger-lang.github.io/EntAITranConsult/` (single-screen
  sort/sequence/classify activities with instant feedback). Good model for our offline sims, but
  shallow (one decision each).
- **Coach role-plays are now inside a client** (unlike the first certificate's job-interview
  framing): e.g. voice role-play with a VP of Customer Experience at a regional retailer — capture the
  goal in the VP's own words, run a "same-word test" on "handled/resolved", propose an
  inclusion/exclusion boundary the VP acknowledges. Five coaches in this course (engage the sponsor,
  reconcile a sales-enablement lead, convince/redirect the sponsoring executive, refinement or
  expansion). Voice only, Coursera Plus.

## Module 1 — What AI Transformation Advisory Is

- Scenario/role: advisor to an operations sponsor; a forecasting assistant "works" at one plant for
  five months, sponsor promised a second plant; planners quietly abandoned the output in week 6 and
  keep a spreadsheet; root cause is a part-numbering change that never reached the data feed.
- Concepts:
  - Advisory judgment (which problem, for whom, under what rules) vs technical build (how to build it)
    — sort every request by its verb: decide-verbs vs build-verbs.
  - Demonstration (can it work under chosen conditions) vs deployment (does it keep working under
    everything real).
  - "Structural uncertainty": scope of effect unclear, outcomes not foreseeable, tech moving — more
    research doesn't shrink it, so decide with the uncertainty named.
  - Three separable foundations: governed data, a **rule of use** (what the output may decide, who may
    override, how the override is recorded), organizational readiness (roles/habits rebuilt).
  - "Follow the decision, not the deployment": trace a change through data → decision → rule →
    who absorbs verification/rework.
- How-to: small. Separate stated ask from underlying problem; list decisions vs build work; name a
  decision owner for each; order them. "Ask which question a demo answers; ask what changes in the
  messiest real version."
- Produces: plugin sorts (clean the ask, demo or deployment, reducible or structural, sequence the
  foundations); coach "Engage the sponsor", "The ask underneath the ask"; written assignment.
- Gaps: no method for actually finding the abandoned output (usage logs, comparing spreadsheet vs
  model figures, interview script for the planner who quietly stopped); no template for a "rule of
  use"; no data reconciliation work; no engagement-letter/SOW content.

## Module 2 — Mapping the Enterprise AI Capability Landscape

- Scenario/role: before a board AI-investment session, the platform owner says "11 AI systems";
  reality is shadow adoption, 2 stalled pilots, an intake queue. Compliance strikes a team-adopted
  briefing assistant off the "register".
- Concepts:
  - Three different instruments, keep them separate: **capability inventory** (value — what can we do
    and how well), **maturity assessment** (org readiness, aggregate), **regulatory register of AI
    systems** (risk/legal duty). Merging corrupts the legal one.
  - **Counting rule first**: write what counts as one capability before counting.
  - **Gate question**: learned from data vs hand-written rules — rules engines are not AI (don't
    govern them for drift).
  - Four nested zones (ML ⊃ DL ⊃ generative/agentic); outer rings differ by **authority**, not smarts.
  - **Three strata of use**: thought partner (turn-taking) → configured agent/workflow end-to-end →
    workflow redesigned around AI. Licences overstate capability; most people are at stratum 1.
  - **Gap condition**: absent (build/buy) / exists but underperforms (improve model/data/process, not
    add review) / exists and performs but ungoverned (add oversight, don't replace).
  - **Ranking a shortfall**: value vs effort + foundational reuse + current exposure + what closing it
    commits you to maintain. Drop-one-input test. Adopt by default for common needs; build only for
    specific, recurring, deeply integrated needs; every build carries a deprecation plan.
  - Map the problem before choosing a tool (spot the "tool-first posture").
  - **Validated only in its domain**: moving a model to a new input type = revalidate, not redeploy.
    Ask "how is it checked, how often wrong, where weakest?"
  - "Governance" has two referents (external conformity vs internal approver path) → two columns.
- How-to: moderate — the five-step map (define counting rule → catalogue past sanctioned rows →
  score on independent axes → classify gap condition → rank on multiple inputs). Ask 3–4 users which
  stratum they actually work at.
- Produces: plugins (match the instrument, pass the gate/find the zone, find the stratum, name the
  condition, rank the gaps, spot tool-first, redeploy or revalidate); coaches "Reconcile the sales
  enablement lead", "Write the rule before you count".
- Gaps: still no discovery mechanics for the shadow footprint (SaaS logs, expense data, survey),
  no inventory template with fields, no worked map of a whole company, no "durable layers"
  (managed service / build environment / governed GenAI infra) worksheet beyond a sentence.

## Module 3 — The Advisory Toolkit

- Scenario/role: sponsor wants to know what happens next and what the org holds after phase 1;
  folder of competent documents (use-case spreadsheet, data-access memo, supplier trial summary, an
  unrouted plant quality concern) that close nothing.
- Concepts:
  - **Artifact vs report**: an artifact has a named person waiting to say go / no-go / revise against
    criteria set *before* the document arrives (a **decision gate**); a report moves nothing.
  - **Delivery artifacts** (opportunity assessment, roadmap, business case, trial report) vs
    **governance artifacts** (system inventory, ownership assignment, oversight spec, operational log)
    — different questions; the org owes governance records regardless of advisor.
  - **Commercial form of the engagement**: bounded exitable phases (client sizes exposure per phase;
    "done" = approved at boundary) vs continuous value-priced partnership (documents never close).
    Ask on day one which the client thinks it bought.
  - "The decision behind the document": for each document name the decision, who holds it (who can
    stop it, not who the org chart says), and what a "no" means and what the org keeps.
- How-to: small but useful: per document write one sentence "who reads it and what they will say
  yes/no/revise to"; sort a document list into "what to build" vs "who is accountable" columns.
- Produces: plugins (artifact or report, delivery or governance, fits or friction); coaches
  "Convince the sponsoring executive", "The folder that closes nothing".
- Gaps: no actual engagement structure (phase plan, deliverable list per phase with acceptance
  criteria), no SOW/proposal/pricing content (fixed-fee vs T&M vs retainer vs value-based — only the
  two forms named), no steering-meeting pack, no example of a phase-exit memo.

## Module 4 — Framing and Scoping the Engagement

- Scenario/role: advisor arrives after the sponsor promised the board a return for "three workflows
  at two plants"; in week 9 a fourth workflow is requested; is it refinement or expansion?
- Concepts:
  - **Objective → scope → boundary**, in that order. Capture the objective in the **sponsor's own
    words** (court reporter, not consultant); read it back.
  - **Scope boundary** written as inclusions + exclusions, each exclusion with a reason that comes
    from a finding (not opinion), acknowledged in writing; changes become visible decisions.
  - **Stakeholder map** = identification + for each role what they need to call it a win and what
    they risk ("two-sentence test").
  - **Advisory boundary**: answer framing/structure questions yourself; route legal, security,
    vendor-contract, regulatory and technical-configuration questions to the named specialist.
  - **Same-word test**: ask each role what a comfortable shared word ("scope", "ready", "proven",
    "value") excludes; record competing readings and the one the work will use.
  - A route for later additions (who weighs an addition against what it displaces).
- How-to: yes, a real 5-step sequence (objective in sponsor's words → roles with needs/risks →
  same-word test → boundary with reasoned exclusions acknowledged in writing → advisory boundary).
- Produces: plugins (whose words are these, decision or gap, whose need/whose fear, which response
  gets the boundary right, assemble the process); coaches: voice role-play with a VP of CX at a
  regional retailer (capture goal, same-word test on "handled/resolved", propose boundary);
  "Refinement or expansion?".
- Gaps: no scoping document/charter template, no change-request form or change-control process, no
  how to get the "written acknowledgement" (email? signature? steering minute?), no handling of a
  sponsor who refuses to narrow, no guidance on how many interviews in two weeks.

## Module 5 — Due Diligence on Claims, Vendors, and Signals

- Scenario/role: advisor to a group service function; vendor demo recording, a slide quoting a
  widely reported enterprise-AI study, and next year's plan already cuts service headcount against
  the capability.
- Concepts:
  - **Measurement conditions** behind every claim: sample, definition of success, volume and task
    mix, oversight level, time window. Unproven (tested, fell short) ≠ untestable (no test defined).
  - **Interested party**: who gains if the claim is accepted usually chose the conditions; apply the
    test symmetrically (also to dismissals). Ten quotes of one study = circulation, not evidence;
    trace a figure hop by hop to its methodology.
  - **Fit between two sets of conditions**: the study's vs the client's (data volume, task
    variability, oversight capacity). Benchmarks perish; re-check at point of use.
  - **Counterparty risk**: multi-year AI provider commitments depend on the provider's balance sheet
    (debt-financed infrastructure); name who answers in year 3 and the hedge (second supplier warm,
    shorter term, exit clause, check provider's dependencies).
  - **Inspectable demonstration**: the system running on records the client supplied, intermediate
    steps visible; if that takes weeks to arrange, that is a finding.
  - Rate each claim: enough to act on / worth testing further / not yet supportable, plus what
    evidence would raise confidence; deliver as a decision, not a caveat ("the readback": claim,
    conditions, counterparty).
- How-to: yes — the five-heading condition sheet, hop-tracing, client-conditions-first reading,
  one-sentence counterparty + hedge, request an inspectable demo.
- Produces: plugins (locate the conditions, name the interest, compare and rate, name the hedge,
  trace to inspectable); coaches "Redirect the sponsoring executive", "Proven, under what conditions?".
- Gaps: no vendor due-diligence pack (questionnaire, reference-call script, PoC/bake-off protocol
  with the client's data, scoring sheet), no contract clauses beyond "exit provision", no financial
  check method for a provider, nothing on undoing a headcount cut already in the plan.

## New vs first certificate

New (worth having):
- **The outside-advisor seat** and consulting craft: sponsor's-own-words objective, written scope
  boundary with reasoned exclusions, refinement vs expansion, advisory boundary (what to route to
  legal/security/procurement), commercial form of the engagement (exitable phases vs partnership).
- **Artifact vs report / decision gate / delivery vs governance artifacts** — a way to design the
  deliverable set of an engagement.
- **Claim due diligence** as a method: measurement conditions, interested party, hop-tracing of
  statistics, fit of conditions, inspectable demo, counterparty (provider balance-sheet) risk.
- **Capability mapping mechanics**: counting rule, gate question (rules engines are not AI), three
  instruments kept separate (inventory / maturity / legal register), three strata of use, three gap
  conditions with different fixes, multi-input ranking, deprecation plan for every build.
- **Rule of use** as one of three foundations.
- Coach role-plays set inside the client (VP of CX, sponsor), not job interviews.

Repeated from the first certificate (vocabulary only): demo ≠ deployment ≈ "pilot isn't scale";
nested AI family and predict/generate/act ≈ course 1 literacy; licence ≠ adoption; designed vs
effective governance; same "four accountable readings" format; one manufacturer scenario; narrated
evidence, nothing to open or build.

## Implications for our plan

1. **Extend 01.1** (three ways in): add the commercial form of a consulting engagement — exitable
   phases vs continuous partnership, fixed-fee/T&M/retainer, what "done" means in each; ask on day one.
2. **Extend 01.2** (mandate): capture the objective in the sponsor's own words and read it back;
   **new 01.7 "Scope boundary and change control"**: written inclusions/exclusions with reasons from
   findings, acknowledged in writing; refinement-vs-expansion test; a change-request route.
   New templates: `scope-boundary.md`, `change-request.md`; add an engagement-letter/SOW outline to
   the engagement charter template.
3. **Extend 02.1** (stakeholder map) with the two-sentence need/risk test, and **02.2** with the
   **same-word test** ("ready", "done", "resolved", "proven") — add to the interview guide and the
   coach prompt.
4. **Extend 01.6** (AI inventory from zero) with the counting rule, the gate question (rules engines
   ≠ AI), three separate instruments (capability inventory / maturity / legal register), strata of
   use and the three gap conditions. Inventory template gets "stratum", "gap condition", "governance
   (external)" and "governance (internal approver)" columns.
5. **New 04.8 (or extend 04.3) "Vendor and claim due diligence"**: the five-heading condition sheet,
   tracing a statistic to its method, inspectable demo / bake-off on the client's own data,
   counterparty risk and hedges (term length, exit, second supplier). New template
   `claim-readback.md` and `vendor-poc-protocol.md`; reuse in engagement 10 (clinic RFP) and in
   `vendor-rfp` simulation (add a "demo conditions" reveal step).
6. **Extend 07.1** (steering pack): artifact vs report — every document names the decision, the
   holder who can stop it, and what a "no" means; add a "deliverable map" (delivery vs governance
   artifacts per phase) to the handover pack (07.7).
7. **Add a "rule of use" section** to the pilot charter (05.1): what the output may decide, who may
   override, how overrides are logged.
8. **Advisory boundary**: add a short section to 01.1 or 04.6 on what an advisor answers vs routes to
   legal/DPO/security/procurement — important for Israel-first legal content (not legal advice).
9. **Persona types to add** to engagement packs: a supplier account executive defending a demo; a
   data steward who knows exactly why numbers diverge but is asked only for reassurance; a process
   owner who keeps adding scope; an engineer at a second site whose "ready" differs.
10. **New engagement idea (optional)**: a "headcount already cut against an untested capability"
    scenario fits engagement 8 (retailer: CEO wants half of support replaced) — make the plan's
    headcount cut part of that data room; and the demo-vs-deployment second-site extension fits
    engagement 13 (factory).
