# IBM Course 1 — AI Literacy for Business Leaders (notes)

Read 2026-11-02 from the logged-in course (all video transcripts and readings; one plugin and one
coach dialogue opened). Notes in our own words. Slug: `ibm-ai-literacy-business-leaders`.

## How every module is built (applies to the whole certificate)

- Intro video → "the problem" video (a vague enterprise situation) → "how each role sees it" video
  (BU leader, transformation leader, data/ML lead, CFO-type, etc.) → "Terms you should know" (3 terms)
  → concept video → plugin (15-min interactive HTML widget hosted on GitHub Pages) → expert
  tutorial/demo (module 1 only here) → "the skill that travels" video (framed as an interview answer
  and a promotion story) → Coursera Coach dialogues (an AI chat that walks you through the skill on
  a use case you type in) → AI-graded written assignment.
- Scenario: always "a large, multi-business-unit enterprise" where AI arrived bottom-up. No named
  company, no data, no documents. The learner is "the enterprise AI transformation leader" (or an
  aspiring one) who already has the seat.
- Videos are partly avatar/slideshow narration.

## Module 1 — Demystify AI for Leaders

- Scenario: teams use GenAI on their own; one region loves a tool, the next hates it; a vendor pitches
  an "autonomous agent"; board asks for the return.
- Concepts / IBM terms:
  - "Fuzziness" — using one word "AI" for four different systems.
  - Nested family — AI ⊃ ML ⊃ deep learning; GenAI is a branch of ML, not beside it.
  - Predict-vs-generate test — first screen: generate → GenAI; predict on domain-specific data →
    classic ML / forecasting / optimisation. Three conditions favour classic ML: proprietary/private
    data, niche domain, an existing working model.
  - Agentic AI as a *pattern* (plan, call tools, act within permissions), not a fifth category.
  - "Bounded machine" / "competent without comprehension" — fluent ≠ judgment.
  - Three adoption levels: individual use, team workflow, built into a system others depend on.
  - "The AI Translator" skill — name the category, apply the screen, test fluent output.
- Concrete how-to given: yes, one small one. The exercise guide walks 6 steps to build an "AI
  Translation Card" (definitions, decision aid, 3–4 value spots tied to a workflow, one marked
  "probably not AI"). Uses a browser AI assistant with a starter sheet of prompts and a single
  check for the "side-by-side" mistake. Demo shows it for a procurement team.
  Useful nugget: a faster draft that still waits in the same approval queue reaches nobody sooner —
  the workflow has to change.
- Learner produces: the translation card (15 min); plugin sorts use cases into predict / generate / act;
  coach dialogues; written assignment.
- Gaps for Monday: no method to *find* the workflows (who to ask, how to observe); value spots are
  brainstormed from the learner's head, not from data; nothing on getting the team in the room, or
  what to do with the card after; no vendor-demo checklist beyond "is it really autonomous?".

## Module 2 — Spot High-Value AI Opportunities

- Scenario: too many AI ideas, no common method; a BU wants to copy a competitor; a vendor agent;
  board wants ROI.
- Concepts / IBM terms:
  - "Solution in search of a problem".
  - AI opportunity mapping — problem-first; "AI doesn't fit here" is a valid finding.
  - AI-fit score — 5 criteria × 1–5 (volume, repetitiveness, data availability, error tolerance,
    current cost) = 5–25; a conversation starter, not a rule.
  - Business value signal — kept separate from fit: metric + accountable owner + evidence.
  - "Consequence if wrong" — separate downside lens; fit × consequence decides fast rollout vs
    governed pilot vs redesign vs deprioritise.
  - Opportunity map (one shared map of all candidates); balanced portfolio; simpler-solution test.
  - "The Opportunity Filter" skill.
- Concrete how-to: the four-step filter (problem → fit → value → consequence) and the 5-criterion
  score. No intake form, no workshop agenda, no way to measure volume/cost.
- Learner produces: plugin scores one case for fit and weighs risk; two coach dialogues; assignment.
- Gaps: how to collect candidates (interviews, process walk, task inventory, shadow-AI census); how to
  get the numbers for "volume" and "current cost" (exports, time studies, sampling); how to run the
  prioritisation workshop with real stakeholders; how to tell the sponsor their idea scored low.

## Module 3 — Assess AI Readiness

- Scenario: one pilot succeeded, its sponsor wants to scale it; board asks "are we ready?".
- Concepts / IBM terms:
  - "Wish list vs diagnosis"; readiness ≠ activity.
  - Six dimensions: strategy, infrastructure, data, talent, governance, culture (+ leadership
    alignment "most underestimated"); interdependent, strength doesn't offset weakness.
  - AI-ready data ≠ dashboard/BI data (clean, labelled, governed, representative, current,
    permissioned, traceable — for a *specific* workload).
  - Binding constraint — the lowest/threshold-failing dimension sets the ceiling; output is a
    sequence, not a score.
  - Separate respondents by function so contradictions surface instead of averaging out.
  - "The Readiness Read" skill.
- Concrete how-to: principles only. No questionnaire, no scoring rubric per dimension, no benchmarks
  named, no data-profiling steps.
- Learner produces: plugin "find the bottleneck"; two coach dialogues; assignment.
- Gaps: an actual readiness questionnaire and interview plan; how to test whether data is AI-ready
  (profile a sample: completeness, labels, duplicates, access rights, lineage); how to present "not
  ready" to the sponsor who wants to scale; what the fix plan for each dimension looks like.

## Module 4 — Responsible AI Fundamentals for Leaders

- Scenario: an AI résumé screener bought like ordinary software; nobody can explain rejections;
  risk asks about a bias audit.
- Concepts / IBM terms:
  - Responsible AI as a lifecycle practice (not a launch sign-off).
  - Five principles: fairness, transparency, accountability, privacy, security.
  - Bias enters via data, algorithm, and human interpretation; fairness is criterion-dependent
    (equal allocation vs equal error rates vs representation) — leader must pick and justify.
  - Governance mechanism (committee, council or one embedded owner) — creates/enforces rules, resolves
    questions, updates rules, names owners; needs decision rights, evidence, escalation.
  - Deployer stays accountable for vendor tools.
  - "The Responsible AI Gate" skill: early screen, ask what data trained it, bias testing, explainability,
    regional compliance, who decides, evidence not claims, pilot, monitoring schedule.
- Plugin (opened): sort six proposals (résumé screener, loan scoring, ER triage, internal HR bot,
  marketing captions, billing chatbot) into high / limited / minimal tier (EU AI Act–style), then an
  ungraded sandbox where domain, who is affected and decision stakes shift the tier.
- Coach (opened): "Before You Greenlight" — AI chat; learner types a real or hypothetical use case,
  then is walked through framing, five gateway checks (data, fairness, values, compliance, human
  oversight), risk tier, deployer accountability, owner and KPIs.
- Gaps: no actual vendor questionnaire or evidence list; how to run a bias test on real outcomes (what
  data, which metric, what threshold); no DPIA/impact-assessment template; who to involve
  (legal/DPO/HR/works council) and in what order; how to write the approval record.

## Course-level verdict

- Reuse as vocabulary: fuzziness, predict-vs-generate, agent as a pattern, fluent ≠ judgment,
  AI-fit score (5 criteria), consequence-if-wrong, binding constraint, AI-ready ≠ BI-ready, the
  Responsible AI Gate, fairness is criterion-dependent.
- Fill: discovery (finding and measuring the work), real data handling, readiness questionnaires and
  data profiling, vendor evidence requests, a working bias test, and the stakeholder conversations
  (sponsor, CDO, HR, legal). Everything here is single-artifact, 15-minute, typed from the learner's
  own head into a template or an AI chat.
