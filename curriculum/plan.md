# AI Transformation in the Field — course plan

The hands-on companion to IBM's "Lead AI Transformation" certificate. IBM teaches how to judge AI
strategy, governance and value. This course makes you do the work: walk into an organization, find
the real work, write the documents, build and test the pilot, train the people, and stand in front
of the steering committee — ten times, in ten different organizations.

Written 2026-11-02. Status: plan only. No lessons written yet.
Research input: `research/ibm-gap-map.md` (what IBM teaches, what it leaves out, where we fill it —
built from the full IBM content), `research/ibm-content/01–07` (per-course notes),
`research/ibm-certificate.md` (public syllabus).

## 0. Binding build rules

> Read `C:\Users\TalGiladi\OneDrive\repos\tals-academy\docs\new-course-instructions.md` in full
> before writing anything. It wins over this plan.

Most important for this course:

- Work only in `course-creator\ai-transformation-field-course`. Plain markdown + YAML. English only.
- Every lesson ends in something the learner does; every module ends in a larger practical piece.
- Every quiz is multiple choice in `.quiz.yaml` (3–5 per lesson, 8–10 scenario questions per module).
- At most two agents running at once, across the whole tree. Sub-agents never spawn sub-agents.
- Verify every law, standard, date, price and tool feature against a primary source when writing the
  lesson; record `sources` and `last_verified`. Nothing in this plan is verified for publishing.
- `BUILD_PROGRESS.md` + `curriculum/status/module-NN.log`; commit after every module;
  `npm run check-course -- ../course-creator/ai-transformation-field-course` until `0 problems`.

## 1. Purpose

After the course the learner can enter an organization — as a new Head of AI, an outside consultant,
or "the person who was told to do AI" — and in the first 90 days:

1. Get a real mandate and a sponsor, and agree what success means.
2. Find out what people actually do and where AI is already used (shadow AI).
3. Turn that into a short, evidence-backed portfolio with measured baselines.
4. Put minimum guardrails in place in week 2: policy, approved tools, data rules, an AI inventory.
5. Build, evaluate and run one pilot on the organization's real data.
6. Train people so the pilot is used, and measure use honestly.
7. Bring a scale / fix / stop decision to the steering committee and defend it.
8. Hand over a running operating rhythm, not a slide deck.

**What it is not.** Not an AI engineering course (see `ai-engineer`, `llm-evals`), not the
engineering-team course (`ai-native-org` covers coding agents and the SDLC), not legal advice. It
re-uses IBM's judgment vocabulary and does not re-teach it.

**Relation to IBM.** IBM is a judgment course: one decision per pre-written case card, every number
already measured, one large multinational, seen from the C-suite, ending at board approval. This
course is everything around those decisions: producing the evidence, the documents, the pilot, the
conversations and the follow-through, in organizations of every size. When a lesson builds on an IBM
idea it names it in one line in `## The situation` (e.g. "IBM's capacity screen") and moves on; the
gap map says which lesson fills which gap.

## 2. Target learner

Someone who finished the IBM certificate (or knows the same ideas) and has to act now: an internal
transformation lead, a consultant, an IT/ops/product manager handed the AI mandate. Comfortable with
spreadsheets and AI chat tools. Coding is optional (two tracks, §5).

Needs: a computer, a spreadsheet tool, access to at least one LLM chat (free tier works; file upload
helps). Code track only: Python 3.12+ and an LLM API key (budget ~US$10 for the whole course).

## 3. Course design — "ten organizations"

The core of the course is **engagements**: full, realistic organizations the learner "joins", each
with its own data room, people, politics, constraints and a hidden truth. The learner runs the whole
engagement, from the first call to the steering-committee decision, and then sees how it played out.

Three stages:

1. **The field kit (modules 1–7).** The method, step by step, practised on one small warm-up org.
   Every lesson produces a real document or artifact the learner keeps and re-uses.
2. **Engagements (modules 8–17).** Ten organizations. Each one is a complete run of the method, but
   each stresses a different hard part, so the learner sees the same move work in one place and fail
   in another.
3. **Capstone (module 18).** An unseen engagement run end to end with no hints, or (optional) a real
   one in the learner's own workplace, with a full deliverable set.

### 3.1 What every engagement contains

Everything in `labs/module-NN/` (downloadable zip):

- **Engagement brief** — how you were brought in, by whom, the stated ask, budget, timeline.
- **Data room** — org chart, process maps, policies, contracts, financial summary, KPI reports, and
  real-shaped data exports (tickets, claims, time sheets, call logs, maintenance logs, proxy logs of
  AI tool use…). Synthetic, generated by a seeded script so it is reproducible, a few hundred rows to a
  few thousand. Each data room has planted findings (bad data, a missing baseline, shadow AI, a
  process step that only exists on paper).
- **Persona pack** — 6–9 stakeholders as roleplay prompts. The learner pastes one into any LLM chat
  and interviews that person: role, what they know, what they hide, what they want, their mood, what
  question unlocks what. The sponsor, the CFO, the CISO, legal/DPO, a middle manager, a frontline
  employee, a union/works-council rep or clinician lead, IT, a sceptic, a secret enthusiast. Each pack
  also has a pre-run interview transcript for learners who prefer not to roleplay.
- **Hidden truth** — what is really going on (the stated ask is often not the real problem). It is
  revealed only in the debrief lesson, inside `<details>`.
- **Deliverables list** and a **self-assessment rubric** for each deliverable.

### 3.2 Fixed lesson shape for engagement modules

| Lesson | What happens | Learner does |
|---|---|---|
| NN.1 The call | Brief, sponsor, mandate, data-room tour | Engagement charter + first-week plan |
| NN.2 Discovery | Persona interviews + data-room analysis | Findings memo with evidence |
| NN.3 Diagnosis | Opportunity map, baseline, the real bottleneck | Shortlist with measured baselines + one-page case |
| NN.4 The hard part | The thing this org is about (see §6) | The specific artifact (verdict, RFP, permissions map…) |
| NN.5 Build or decide | Pilot built and evaluated on the data room, or a decision under pressure | Working pilot + eval report, or decision record |
| NN.6 Readout and debrief | Steering-committee simulation, then "six months later" | Readout pack; compare to the expert path and the hidden truth; score with the rubric |

The debrief shows two or three futures ("what happened when the team chose X") and the expert's
deliverables for comparison.

### 3.3 Simulations

Two kinds:

1. **AI roleplay (markdown persona packs).** The real conversation practice. Works with any LLM chat.
   Every pack has a "coach" prompt too: paste your transcript, get feedback against the lesson's
   interview checklist.
2. **Interactive simulations (`simulations/`, offline HTML, labelled "educational model").** Re-used
   across engagements via presets (`?preset=insurance`).

| Simulation | What the learner practises |
|---|---|
| `discovery-interview` | Limited question budget, branching answers; finds the real problem or not |
| `portfolio-sorter` | Scores use cases on the evidence; hidden truths revealed after commit |
| `pilot-economics` | Volume × automation rate × accuracy × human review cost × tokens → net value, breakeven |
| `oversight-under-load` | Human reviewers in a queue; rubber-stamping, fatigue, the capacity screen |
| `adoption-dynamics` | 26 weeks; training, champions, workflow redesign, mandates; qualified-use rate vs licences |
| `steering-committee` | Branching meeting with CFO, CISO, GC, COO, sponsor; per-engagement presets |
| `incident-tabletop` | An AI incident unfolding hour by hour; contain, communicate, fix, report |
| `agent-authority` | Grant an agent tools and limits, run scripted days, see damage and recoverability |
| `vendor-rfp` | Score vendors on demos vs evidence; contract terms (data use, retention, exit) |
| `operating-model-scaler` | 12 business units over 3 years; CoE / federated / hub-and-spoke; bottlenecks and shadow builds |
| `risk-register-tester` | Ratings vs tested controls; earn the green |
| `roi-defender` | Sponsor claims under finance review; net each claim |

## 4. Content sources and accuracy

- **Israel first (Tal, 2026-11-02).** All organizations are Israel-based. Israeli law and regulators
  are the primary layer in every lesson: Privacy Protection Law incl. Amendment 13, the Privacy
  Protection (Data Security) Regulations, the Privacy Protection Authority's guidance on AI, the
  government AI policy principles, and sector regulators where an engagement needs them (Bank of
  Israel / Banking Supervision, Capital Market, Insurance and Savings Authority, Ministry of Health,
  public-procurement and freedom-of-information rules for the municipality, labour law and works
  committees for workforce change). Hebrew/Arabic/Russian/English workforce and customers are part of
  the data and the evals. The course stays in English; Israeli law titles get their Hebrew name once.
- **EU second**, as it reaches Israeli organizations: GDPR (adequacy, EU customers and staff) and the
  EU AI Act when an Israeli company is a provider or deployer for the EU market (check current
  application dates and the status of the "Digital Omnibus" changes when writing).
- **US and standards last:** NIST AI RMF 1.0 + Generative AI Profile (NIST AI 600-1), ISO/IEC 42001,
  and US rules only where an engagement sells there. All "verify at writing time".
- Public case files for teardowns (verify each against primary sources before use): Moffatt v. Air
  Canada (chatbot refund policy), Mata v. Avianca and later fake-citation sanctions, NYC MyCity
  chatbot, Klarna's AI customer-service claims and partial walk-back, the Dutch childcare-benefits
  scandal, Amazon's recruiting model, DPD's chatbot, Chevrolet dealer chatbot, Duolingo "AI-first"
  memo reaction, Morgan Stanley's adviser assistant, published adoption and pilot-failure surveys
  (read the method before quoting any "X% of pilots fail" figure).
- Tools: tool-agnostic core. Where a lab needs a tool, name current enterprise options (Microsoft 365
  Copilot / Copilot Studio, ChatGPT Enterprise, Claude for Work, Gemini for Workspace, n8n/Zapier/Make)
  without depending on one. Pin versions and dates in labs.
- Synthetic data only. No real company names for engagement orgs; fictional names, real-shaped
  numbers (sourced industry benchmarks where cited).

## 5. Two tracks for building

Every build lab has:

- **Track A — no-code:** LLM chat (projects / custom GPT / Claude project) + spreadsheet + a
  workflow tool. Eval done in a spreadsheet with a fixed test set.
- **Track B — code:** Python + an LLM API + a small eval harness in `labs/common/` (pinned versions).

Both tracks produce the same artifacts: the pilot, a test set, an eval report with numbers.

## 6. Modules and lessons

### Stage 1 — The field kit (warm-up org: "Harbor & Pine", a 120-person furniture importer)

**Module 1 — Walking in**
1. 01.1 Three ways in: internal lead, consultant, accidental owner — what changes for each
2. 01.2 Getting a real mandate: sponsor, scope, money, authority, what "done" means (sponsor conversation roleplay)
3. 01.3 The first-week plan and the 30-60-90 (template filled for Harbor & Pine)
4. 01.4 Access: data, systems, people — the access request pack and how to get it signed
5. 01.5 The shadow-AI census: survey, proxy/SaaS logs, expense reports, browser extensions, interviews (data room exercise)
6. 01.6 The AI inventory from zero: AI that arrived inside SaaS feature updates, the decisions AI already shapes, inventory fields and owners
- Module practical: engagement charter + 30-60-90 + access pack + shadow-AI census + first AI inventory for Harbor & Pine.

**Module 2 — Discovery that finds the real work**
1. 02.1 Stakeholder map before the first interview
2. 02.2 The discovery interview: questions that get workflows and workarounds, not wish lists; protecting people who speak up (roleplay ×3 + coach)
3. 02.3 Process walk and task inventory: observation protocol; volume, time, error, variation, judgment
4. 02.4 Measuring a baseline from exports: cycle times and volumes from a ticketing/ERP export, sampling, time studies
5. 02.5 Profiling the data: is it AI-ready? (completeness, labels, duplicates, access rights — on the data room)
6. 02.6 Writing a findings memo people believe
- Module practical: findings memo + task inventory + baselines + data profile.

**Module 3 — From findings to a funded portfolio**
1. 03.1 Opportunity map: automate, assist, augment, leave alone
2. 03.2 Scoring with evidence, not opinions (`portfolio-sorter`)
3. 03.3 Running the scoring workshop with the real stakeholders (facilitator script, roleplay)
4. 03.4 The leadership alignment session: 60–90 minutes from "use AI" to three bets (agenda, materials, roleplay)
5. 03.5 The ROI model that survives finance: hours → capacity → money; seats, tokens, integration days, review minutes; scenarios and NPV; the conversation with finance about their template and hurdle rate (spreadsheet in labs, `roi-defender`)
6. 03.6 The one-page business case, the cost of doing nothing, and telling the sponsor their favourite idea lost (roleplay)
- Module practical: portfolio of 3, ROI model, one-page case, workshop pack.

**Module 4 — Guardrails you can ship in week two**
1. 04.1 The AI acceptable-use policy (write it, 2 pages max)
2. 04.2 Approved tools and data classes: what data may go into which tool
3. 04.3 Vendor and tool review: data use for training, retention, location, sub-processors, certifications, exit (questionnaire + 3 real-shaped vendor documents)
4. 04.4 AI inventory and risk tiering; when you need a DPIA and how to write one
5. 04.5 Risk register from zero: pre-mortem workshop, starter risks per use-case type (chatbot, extraction, scoring, agent), security risks (prompt injection, data leakage), then test the controls (`risk-register-tester`)
6. 04.6 Which law applies to you: a one-page regulatory map (Israel first, then EU and US; actor and date)
7. 04.7 Governance that runs: governance charter, committee terms of reference, intake form for new AI uses, cadence, link to the existing risk process
- Module practical: the policy pack (AUP, tools list, vendor review, inventory, DPIA, risk register, regulatory map, governance charter + intake).

**Module 5 — Building and testing a pilot**
1. 05.1 The pilot charter: hypothesis, scope, thresholds, stop rules, owner, and the counterfactual (matched teams or phased rollout, how long to run)
2. 05.2 Building the test set from real data (and what to leave out)
3. 05.3 Build it — Track A and Track B (support-email triage + draft replies for Harbor & Pine)
4. 05.4 Evaluate: accuracy, failure types, negative tests, cost per item, time saved (`pilot-economics`)
5. 05.5 Human-in-the-loop design that actually checks (`oversight-under-load`)
6. 05.6 Shadow mode on production data, staged release, rollback, production-readiness checklist
7. 05.7 Before launch: logging spec, monitoring (sampled output review, eval re-run on vendor model change, cost alerts), change control for prompts and models
- Module practical: working pilot + eval report + monitoring spec + go/no-go recommendation.

**Module 6 — Making people use it**
1. 06.1 Workflow redesign: change the work, not just add a tool
2. 06.2 Training that transfers: a 60-minute role-based session (run it, script + exercises in labs)
3. 06.3 Champions network and office hours
4. 06.4 The honest adoption dashboard from real usage exports (admin analytics joined with HR/task data; defining a qualified event; privacy of usage monitoring) (`adoption-dynamics`)
5. 06.5 The comms pack: announcement, manager talking points, "will this replace me?" FAQ, works-council/union consultation
6. 06.6 Resistance conversations: the manager, the expert, the worried employee (roleplay)
- Module practical: training session pack + adoption dashboard + comms pack.

**Module 7 — Readouts, decisions and the operating rhythm**
1. 07.1 The steering pack: 5 slides, one decision
2. 07.2 Scale, fix or stop: the decision record; how to actually decommission a "retire"
3. 07.3 The steering meeting (`steering-committee`)
4. 07.4 When it goes wrong: incident runbook and tabletop (`incident-tabletop`)
5. 07.5 The operating rhythm: owners, RACI for a running AI service, monthly review, triggers, retirement
6. 07.6 The board said yes — now what: running phase 1 week by week (staffing, budget release, first sprint, first report)
7. 07.7 Handover: from project to operations, so it survives you
- Module practical: full Harbor & Pine readout + decision + phase-1 plan + handover pack.

### Stage 2 — Engagements (fixed six-lesson shape, §3.2)

| Module | Organization | Stated ask | The hard part (lesson NN.4) | Build or decide (NN.5) |
|---|---|---|---|---|
| 8 | **Northwind Outfitters** — 450-person online retailer | "A chatbot that replaces half of support by Q2" | Chatbot vs agent-assist; refund-policy liability (Air Canada pattern); the real problem is returns policy | Agent-assist pilot on 2,000 tickets + eval |
| 9 | **Meridian Mutual** — mid-size insurer | "Automate claims intake and spot fraud" | Regulated deployment verdict: high-risk classification, explainability, bias test on claims data; pass/flag/block gate | Document-extraction pilot + fairness check + deployment verdict |
| 10 | **Galil Health** — regional clinic network | "Ambient scribe for every doctor" | Vendor selection: RFP, demo vs evidence, clinical safety, privacy, clinician adoption (`vendor-rfp`) | Vendor scoring + contract terms + clinician pilot plan |
| 11 | **Givat Oren** — municipality, 220k residents | "A citizen chatbot like other cities have" | Public-sector constraints: procurement, transparency, accessibility, languages, wrong-advice risk (MyCity pattern); unions | Answer-quality eval of a permit-FAQ assistant in 3 languages; transparency register entry |
| 12 | **Atlas & Rowe** — 90-lawyer law firm | "Everyone wants Harvey/CoCounsel; partners are split" | Confidentiality, fake citations, and the billable-hour problem: time saved ≠ money earned; pricing change | Precedent-search assistant over a document set + citation verification eval; revised ROI |
| 13 | **Kinneret Plastics** — 600-person factory, 3 shifts | "Predictive maintenance with AI" | The data is not ready: say not-yet, and fund the foundation instead; frontline and multilingual workforce | Data readiness audit on maintenance logs; maintenance-manual assistant as the honest quick win |
| 14 | **Lumen SaaS** — 250-person B2B software company | "Ship an AI agent that resolves customer issues in the product" | Agentic AI: tool permissions, authority ladder, recoverability, audit trail (`agent-authority`) | Agent permission map + negative tests (try every action it must refuse) + scripted red-team + staged autonomy plan |
| 15 | **Crescent Bank** — 4,000 staff, 14 business units | "We have 40 pilots and nothing in production" | Operating model and scale: CoE → hub-and-spoke, decision rights, model risk management (`operating-model-scaler`) | Portfolio triage of 40 pilots + operating-model design + 12-month scale plan |
| 16 | **Open Hands** — 30-person nonprofit, no IT | "Help us use AI, we have no budget" | Doing it all in 4 weeks with free/cheap tools; donor-data privacy; one person as IT | Grant-writing and case-notes workflow; whole policy pack in one page |
| 17 | **Vantage Logistics** — rescue | "The last AI lead left; the board wants answers in 30 days" | Turnaround: inherited failing program, an open incident, cost overrun, broken trust | Stop/keep audit of everything running + incident closure + 30-day board brief |

Each engagement re-uses the field-kit templates; lessons point to them instead of re-teaching.

### Stage 3 — Capstone

**Module 18 — Your engagement**
1. 18.1 The unseen org: brief and data room (no hints, no hidden-truth until submission)
2. 18.2 Full deliverable set against the rubric
3. 18.3 Optional real engagement: running the method in your own workplace (ethics, permission, confidentiality)
4. 18.4 Your practice kit: turning everything you wrote into your own reusable playbook
- Capstone: full deliverable set (charter, findings memo, portfolio + ROI, policy pack, pilot + eval, adoption plan, steering pack, decision record, handover).

Rough size: 18 modules, ~110 lessons, ~32 h reading, ~160 h practice.

## 7. Lesson format

Front-matter and H1 exactly as in the build rules. Fixed `##` sections in every lesson:

1. `## The situation` — where you are in the engagement, what just happened.
2. `## What to do` — the method, step by step, with a worked example.
3. `## Watch out` — the common mistakes and how to recover (this is where IBM's "what fails" goes, short).
4. `## Your turn` — the task: inputs (data-room files, persona, template), steps, time, how you know you are done, `<details>` reference answer.
5. `## References`

## 8. Templates (`templates/`)

Engagement charter · 30-60-90 plan · access request pack · shadow-AI survey · stakeholder map ·
interview guide · task inventory · findings memo · opportunity map · use-case scorecard · ROI model
(CSV + instructions) · one-page business case · AI acceptable-use policy · approved tools and data
classes · vendor AI questionnaire · AI inventory · DPIA for AI · risk register · regulatory map ·
pilot charter · test-set spec · eval report · human-review design · training session plan · champions
playbook · adoption dashboard spec · comms plan · steering pack · decision record · incident runbook ·
operating rhythm · handover pack · RFP for AI vendors · agent permission map.

## 9. Projects (`projects/`)

One brief per engagement (the deliverables list and rubric), plus the capstone brief.

## 10. Build order

1. Foundations: README, `_sidebar.md`, glossary, templates (drafts), `labs/common/` (data generator,
   eval harness), simulation shell, persona-pack format + coach prompt.
2. Stage 1 (modules 1–7), in order: every later module re-uses its templates.
3. Simulations, in the order modules need them.
4. Engagements 8–17: one agent per module, at most two at a time; each writes its data room first,
   then personas, then lessons.
5. Capstone, final QA, check-course 0 problems.

## 11. Open questions (also in TODO_FOR_TAL.md)

1. ~~Read the actual IBM content~~ — done 2026-11-02, see `research/ibm-gap-map.md`.
2. ~~Free or paid?~~ — paid (Tal, 2026-11-02).
3. ~~Which jurisdictions?~~ — Israel first, then EU, then US (Tal, 2026-11-02).
4. Track B (code) in every build lab, or only in some engagements?
