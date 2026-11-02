# IBM Consulting cert, Course 3 — Assess AI Readiness (notes)

Read 2026-11-02: all video transcripts (4 modules, ~75k chars). This course has **no coach
role-plays**, only plugins; plugins were not opened (Tal is not enrolled in this course, the widget
page redirects to the course landing page; transcripts were still readable). Slug:
`assess-ai-readiness`. Notes in our own words.

Learner seat: enterprise AI transformation consultant / management analyst writing a readiness
opinion. Scenario: the same multinational manufacturer, a different incident per module.

## Module 1 — The Dimensions of Readiness

- Scenario: a warranty-claims assistant that worked in one region was extended to four and pulled
  back after six weeks; rollback note, growing support queue, a data-protection review scheduled twice
  and never held, an all-green dashboard. The process analyst counts three AI systems in the workflow
  (the assistant, an unprocured drafting feature in spreadsheet software, a summarization feature a
  vendor added in a release); the procedure was never rewritten for a region with a different claim
  mix; the claims desk re-keyed a category by hand and stopped escalating.
- Concepts:
  - **AI readiness** = the condition of the organization around a model; seven dimensions: data,
    workflows, ownership, adoption, governance, measurement, trust. Pilots test capability only, so a
    year of pilots can mature none of them.
  - **Organization-level risk vs model-level risk** — different instruments: testing establishes
    model risk; structural inventory and governance review (who owns each output, who checks it,
    where exceptions go, which records it reads/writes, who was trained) establish org risk.
  - **System in context**: trustworthiness belongs to model + data pipeline + people acting on output
    + oversight; change any part = new arrangement to re-establish.
  - **Dated readiness finding**: a comparison against a stated standard on a stated date; two clocks
    (the organization changes, and the bar itself moves); reassess by rebasing the bar first.
  - "The organization is the system under test"; audit a self-assessment's instrument (whose boundary
    produced the item list; columns follow procurement or the work; what averaged two risks).
  - Purchasable dimensions (platform, data lake, training) vs non-purchasable ones (redesigned work,
    output owners, exception routes, records a reviewer can be shown).
- How-to: moderate — "for this to create value here, the following would have to be true" list; ask
  which instrument produced any evidence; record standard and date on every finding.
- Gaps: no readiness instrument/questionnaire; no interview set per dimension; no rubric levels; no
  worked assessment.

## Module 2 — Data and Technology Readiness

- Scenario: a maintenance-planning assistant recommended a part that had been superseded; the
  platform held a stale replica of the parts master; the steward's conditions lost her name in copying.
- Concepts:
  - **Fidelity** (origin, currency, completeness, representativeness — always for a named use) vs
    **access** (reachable) vs **permission** (law/contract/policy allows this use) — and **where each
    boundary is enforced** (ideally in the data layer).
  - **Governed data**: traceable origin, documented preparation and labelling, checked for gaps and
    skews, matches operating context (EU AI Act high-risk data requirements and ISO/IEC 42001 data
    controls agree).
  - **Single source of truth ≠ centralization**: one agreed, current, access-controlled copy per
    domain; centralised platforms can hold three divergent copies. Test: publish cadence vs read
    cadence.
  - **Tiered control**: control strength by the cost of getting that data category wrong; uniform
    policy over-controls cheap data and under-controls expensive data.
  - **Govern in place vs foundations first**: bounded, lower-stakes use cases proceed on data governed
    in place; core, regulated, cross-domain, at-scale use cases need foundations first. The finding
    states which regime applies and why.
  - **Self-report vs finding**: a platform owner's "it can support it" is a self-report to test; a
    data steward's lineage work is close to a finding — collect it rather than audit the steward.
  - **Chain-of-custody read** per data asset: origin → collected-for purpose → permission covering this
    use → enforcement point → accountable person today. A chain that ends at a system is broken.
    Ending: "clean yes with evidence" or "not yet, and here is the sequence".
- How-to: yes — the five-link read in fixed order (what it predicts → what record proves the outcome
  → map only needed assets → test origin/completeness/representativeness → where permission is
  enforced → who owns the running system).
- Gaps: no hands-on data profiling; no permission/legal-basis worksheet; no example data dictionary;
  no check of label existence on real records.

## Module 3 — Organizational Readiness

- Scenario: a documentation assistant ran 90 days in three plants; a quality sample found 19 supplier
  non-conformance write-ups revised after issue and nobody could tell which were AI-assisted (no
  marker in the workflow). Two unprovisioned tools appeared; the policy said "no sensitive
  information" and nobody would say if supplier records counted; the named reviewer was never told.
- Concepts:
  - **Organizational readiness** as an externally checkable condition: workflow redesigned, reviewer
    authority, skill demonstrated (not enthusiasm), reinforcement after launch week — four decisions
    (redesign the work, train, define handoffs, place human judgment). Saved hours refill by default
    unless someone decides where they go.
  - **Oversight design**: a specific person with information, authority and time before output
    becomes organizational fact, plus competence to judge it; otherwise "blame exposure", not control.
  - **Resistance as evidence**: points at unmet awareness/support/ability or an operational defect;
    concentrates in the middle (experts whose standing rests on today's work) — ask what they expect to
    break and record it as a finding.
  - **The altitude problem**: access, training and encouragement concentrate with seniority, so
    adoption looks better the higher you ask; a senior account is a hypothesis.
  - **Frontline manager sampling**: does the manager expect and reward use, show own recent use, and
    raise it in performance conversations?
  - Provisioning records vs actual use; more people using tools weekly than are sanctioned → work
    flows through unprovisioned channels.
  - **Absorption test**: can the receiving structure take, verify, correct and redeploy the output?
    Findings: proceed / phase / not yet, with remediation named and sequenced.
- How-to: moderate — turn each sponsor claim ("aligned", "licensed", "trained") into an observable
  and say where to observe it; ask frontline managers the three questions.
- Gaps: no observation protocol or survey; no way to get provisioning vs usage data; no AI-assisted
  marker design; no policy clarification process (what counts as sensitive).

## Module 4 — Reporting Readiness

- Scenario: an AI visual-inspection pilot; the report said "ready to proceed, subject to conditions";
  the sponsor slide carried 2 conditions, the risk register 5; two of three shifts had quietly stopped
  using it; funding went out the same week.
- Concepts:
  - **Provenance**: how you came to know something (check run, process watched, document read, or
    account given) — not confidence or seniority.
  - **Verified finding vs asserted claim**: label every claim; one mislabelled claim destroys trust in
    every label. Verified gap → risk-register entry with owner/date; asserted gap → verification task.
  - **Observation vs finding**: a finding adds the consequence for the decision (timeline, cost, risk).
  - **Resistance (quiet non-adoption) as evidence**: who stopped, when, back to what.
  - **Translating twice**: once into an obligation (governance reader), once into time/cost/operating
    consequence (sponsor). Keep statistics out of sentences that carry the argument.
  - Recommendation must allow **not yet** (else the report is justifying investment); approve / defer /
    fund-with-sequence; same interest commissioning and advocating = disclose provenance.
  - **Upstream read**: where else does the same gap live (shared upstream system blocks adjacent
    initiatives)?
  - Using an AI assistant to draft the report: compare against the source record and restore anything
    it collapsed, omitted or misweighted.
- How-to: yes — sort observations by provenance, write no claim stronger than its source, attach
  consequence, translate twice, close with yes / not yet + sequence, verify AI drafts.
- Gaps: no report template or worked example; no evidence log format; no guidance on handling the
  sponsor conversation when the answer is "not yet" (beyond wording).

## New vs first certificate

New:
- **Readiness as a formal assessment deliverable** with seven dimensions, org-level vs model-level
  risk (different instruments), system-in-context, **dated findings against a stated bar**.
- **Data readiness vocabulary**: fidelity / access / permission and where each is enforced, governed
  data (four tests), single source of truth vs centralization (publish vs read cadence), tiered
  control, govern-in-place vs foundations-first, **chain-of-custody read**, self-report vs finding.
- **Org readiness tests**: oversight = information + authority + time + competence; altitude
  problem; frontline-manager three-question sample; resistance as evidence; the absorption test;
  provisioning-vs-use and unsanctioned use as evidence.
- **Evidence-graded reporting**: provenance labels (verified vs stated/asserted), observation →
  finding (consequence), translate twice (obligation vs time/cost), not-yet as legitimate, upstream
  read, checking AI-drafted reports against sources.

Repeated: six-dimension readiness / one bottleneck (first cert course 1 module 3), "AI-ready ≠
BI-ready", effective vs designed oversight and the capacity screen (governance course), licence ≠
adoption, resistance as information (change course), pilot isn't scale. Still one manufacturer,
narrated incidents, no data to inspect.

## Implications for our plan

1. **New lesson 02.7 (or extend 02.6) "Readiness assessment as a deliverable"**: seven dimensions,
   org-level vs model-level evidence, every finding dated and measured against a stated bar, proceed /
   phase / not yet with a sequence. New template `readiness-assessment.md` (dimension × evidence ×
   provenance × consequence × owner × date).
2. **Extend 02.5** (profiling the data) with the **chain-of-custody read** and fidelity / access /
   permission / enforcement point per asset — permission written Israel-first (Privacy Protection Law
   purpose limitation, Amendment 13, database registration/obligations — verify when writing). Add a
   hands-on: in the data room, find the stale replica (publish cadence vs read cadence) and a dataset
   the org can reach but may not use for this purpose.
3. **Extend 02.6** (findings memo) with **provenance labels** (verified vs asserted), observation →
   finding with consequence, translating twice (obligation vs time/cost), the **upstream read**, and
   checking an AI-drafted memo against the sources (hands-on: give learners a flawed AI-drafted memo
   that drops a condition).
4. **Extend 06.4 / 06.6** with the **altitude problem**, the **frontline-manager three questions**,
   provisioning-vs-actual-use exports, and quiet non-adoption (who stopped, when, back to what) as
   evidence; add these to the `adoption-dynamics` simulation as hidden signals.
5. **Extend 05.5** (human-in-the-loop) with oversight = information + authority + time + competence,
   and an **AI-assisted marker** in the workflow (so you can tell which outputs were AI-drafted).
6. **Extend 04.2** (approved tools and data classes) with **tiered control** and a worked "does a
   supplier record count as sensitive?" clarification — the policy must answer the question staff
   will actually ask.
7. **Extend 07.3/07.1** (steering): report "not yet" honestly when the commissioning sponsor is also
   the advocate; the 2-conditions-vs-5-conditions failure as a `steering-committee` sim branch.
8. **Engagement data rooms**: add a rollback story (engagement 17 rescue already fits — the
   "extended to four regions and pulled back" pattern), a superseded-part stale-replica case (factory,
   module 13), and AI features that arrived inside vendor releases (bank or insurer) for the inventory.
9. **Persona types**: data governance analyst who could not finish a review (doesn't know which
   records the tool touches); claims-desk/queue lead who stopped escalating; platform owner whose
   "ready" is true but irrelevant; L&D lead whose training didn't cover what licences unlock;
   documentation lead named reviewer without being told.
10. **New simulation idea (optional)**: `readiness-evidence-grader` — sort a folder of interview notes,
    dashboard screenshots and documents into verified/asserted, attach consequences, and see how a
    steering group reacts to over-claimed vs honestly labelled reports.
