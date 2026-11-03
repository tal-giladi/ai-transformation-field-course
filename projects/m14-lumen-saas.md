# Lumen SaaS

Run the whole engagement at Lumen SaaS, a 250-person Israeli B2B software company, as its new head of AI operations: from your first day to the executive staff's decision and the operating rhythm you will run afterwards. The CEO has promised the board an in-product AI agent that resolves half of support; the product team has built one that can issue credits, change plans, reset passwords and delete data; and nobody has noticed that agents are already acting on customer accounts under one shared identity. Your job is to find out what is really running, measure what the agent actually resolves, write a permission map action by action, prove the agent refuses what it must, and bring one per-action recommendation to the executive staff. This is module 14's practical: one integrated deliverable set, every document consistent with every other.

> [!WARNING]
> All work in this project uses the synthetic data room, the mock agent in the harness and the simulation. In a real organisation, never run negative tests or red-team scripts against a live agent or real customer accounts, and never change a live agent's tools, credentials or limits without its owner's and security's written agreement.

## The brief

Read [the engagement brief](../labs/module-14/brief.md) (in the module download). In short: you start Sunday 29 November 2026 as Head of AI Operations, reporting to Revital Azoulay (VP Support); budget ₪380,000 to March; you may pause the agent for safety with Revital; the executive staff decides the launch scope on Wednesday 27 January 2027; Lumen Live is on Tuesday 9 February; Shaked Clinics' security questionnaire is due 15 January and its renewal is on 31 March. The data room is `labs/module-14/data-room/` (start with its [INDEX](../labs/module-14/data-room/INDEX.md)); the people are in `labs/module-14/personas/` ([the cast](../labs/module-14/personas/README.md)); the test harness is in `labs/module-14/harness/`.

You are not a lawyer, and this project is not legal advice: every legal reading in your deliverables is attributed to Lumen's General Counsel and DPO or to the source she points to.

## Deliverables

| # | Deliverable | Template | Lesson |
|---|---|---|---|
| 1 | **Charter and 90-day plan**: the mandate read back, the date and target as inputs, what being an employee changes, scope with owners, first-read sheet, access request, the inventory started | [engagement charter](../templates/engagement-charter.md), [scope boundary](../templates/scope-boundary.md), [data-room first read](../templates/data-room-first-read.md), [access request pack](../templates/access-request-pack.md), [30-60-90 plan](../templates/30-60-90-plan.md) | [14.1](../lessons/module-14/lesson-01.md) |
| 2 | **Findings memo and AI inventory**: what the agent did with the replaced article, who acts as whom, the fleet from tokens, logs and expenses, the design's controls tested against the log; every finding labelled; no person named as a cause | [findings memo](../templates/findings-memo.md), [AI inventory](../templates/ai-inventory.md), [stakeholder map](../templates/stakeholder-map.md), [interview guide](../templates/interview-guide.md) | [14.2](../lessons/module-14/lesson-02.md) |
| 3 | **Baseline sheet, shortlist and one-page case**: resolution under two definitions with a quality check, the target restated, approval capacity, the bottleneck, five candidates screened | [agentic opportunity frame](../templates/agentic-opportunity-frame.md), [use-case scorecard](../templates/use-case-scorecard.md), [value measurement plan](../templates/value-measurement-plan.md), [decision-ready case](../templates/decision-ready-case.md) | [14.3](../lessons/module-14/lesson-03.md) |
| 4 | **Agent permission map** for Lumen Assist, a miniature map and decision for the citizen-built agent, the fleet rules, a regulatory routing table, draft answers to Shaked's section 7 | [agent permission map](../templates/agent-permission-map.md), [regulatory map](../templates/regulatory-map.md), [risk register](../templates/risk-register.md), [AI intake register](../templates/ai-intake-register.md) | [14.4](../lessons/module-14/lesson-04.md) |
| 5 | **Must-refuse and must-do tests, red-team scripts, test report, kill-switch drill, red-team brief, staged-autonomy plan** | [agent permission map](../templates/agent-permission-map.md) (sections 3–4), [test-set spec](../templates/test-set-spec.md), [eval report](../templates/eval-report.md), [production-readiness checklist](../templates/production-readiness-checklist.md) | [14.5](../lessons/module-14/lesson-05.md) |
| 6 | **Executive readout** (one recommendation in parts, recommend-against on the front page), **incident write-up**, **integration check**, notes of the **hardest-finding rehearsal**, **decision record**, **operating rhythm** | [steering pack](../templates/steering-pack.md), [incident runbook](../templates/incident-runbook.md), [integration check](../templates/integration-check.md), [decision record](../templates/decision-record.md), [operating rhythm](../templates/operating-rhythm.md), [handover pack](../templates/handover-pack.md) | [14.6](../lessons/module-14/lesson-06.md) |

## Steps

1. Read the brief and the INDEX; write the charter and the first read; start the inventory; interview Revital (14.1).
2. Reconstruct the HC-214 timeline, split the audit log by user agent, build the fleet, test the three design controls; interview at least three of Maya, Andrei, Yonatan, Nurit and Shira; write the memo (14.2; Track B: `discovery.py`).
3. Measure resolution two ways, define the quality sample, restate the target, size approvals, screen the candidates, write the case; talk to Svetlana and Yaron (14.3).
4. Write the permission map, the citizen agent's map and decision, the fleet rules, the routing table with Nurit and Shaked's answers with Amir; optionally run the map in the simulation (14.4).
5. Derive the tests from your map, write red-team scripts in four languages, run them (Track A in a spreadsheet; Track B: `harness/run_harness.py`, scripted then `--agent llm`), write the report, the drill, the brief and the staged plan; negotiate with Maya (14.5).
6. Write the readout and the incident write-up; run the integration check; rehearse the hardest finding with Maya twice; run the meeting; write the decision record and the operating rhythm (14.6).
7. Score your set with the rubric below **before** you open the hidden truth and the expert set in 14.6; then compare.

Time: about 4 hours beyond the lessons' own exercises, most of it in steps 5 to 7.

## Self-assessment rubric

| Criterion | What "strong" looks like | What "weak" looks like |
|---|---|---|
| Mandate as an employee | The mandate read back; the date and target as inputs; every control sized to people who will run it; decisions prepared in their owners' names | The launch date as the objective; controls nobody can staff; findings first heard by their owners in a meeting |
| Discovery from the log | The agent's tool calls joined to sources and revisions; the shared identity split by user agent; the fleet from tokens, the directory and expenses; the design's controls tested with numbers | The design document taken as fact; the inventory copied from IT; the model blamed for a source problem |
| Protecting people | The citizen builder approached with "show me"; no person named as a cause anywhere | The builder treated as a culprit; a name in the incident's causes |
| The real problem | Authority and visibility identified as the bottleneck; the register and identities shortlisted though they contain no AI | The question left as "is the model good enough?" |
| Measurement | Resolution defined and baselined two ways; a quality sample beside it; the target restated with a gate and labelled assumed | The dashboard figure repeated; a target promised |
| The permission map | Every action, including those not granted; worst case, band and last reversible moment; the lowest rung that does the job; limits where the damage is, each enforced outside the model; approvals within capacity | One row for "the agent"; limits in the prompt; approvals on everything; delete granted |
| Identity, trace and stop | Own identity with least scopes; a full trace read daily; a kill switch at the tool layer, drilled; source control per language | The shared token kept; an action log read weekly; a UI flag as the stop; fixes in one language |
| Tests and red team | Each control has a test only it stops; must-do tests; scripts in every customer language; soft and person passes reported separately; findings become test rows | Brainstormed attacks only; English only; refusals counted as controls; a red-team PDF |
| Staged autonomy | Stages with dates, yes/no gates on the log and stop rules; re-test on every change; the never list | "Widen when it looks good"; no stop rules; tests run once |
| Readout and follow-through | One recommendation in parts; recommend-against on the front page; the incident written up with causes in the system; the hardest finding delivered privately; owners named for every daily, weekly and monthly task | "Approve the agent: yes or no"; the incident left as "handled"; a peer ambushed; a rhythm with no names |

## Model answer

<details><summary>Model answer</summary>

The expert's deliverable set is in the module download, `labs/module-14/expert/` ([README](../labs/module-14/expert/README.md)):

- [01 · Charter and 90-day plan](../labs/module-14/expert/01-charter-and-90-day-plan.md)
- [02 · Findings memo](../labs/module-14/expert/02-findings-memo.md)
- [03 · Baselines, the fleet and the shortlist](../labs/module-14/expert/03-baselines-and-shortlist.md)
- [04 · Agent permission map](../labs/module-14/expert/04-permission-map.md)
- [05 · Must-refuse tests, red-team report and staged-autonomy plan](../labs/module-14/expert/05-tests-red-team-and-staged-plan.md)
- [06 · Executive readout, decision record and handover](../labs/module-14/expert/06-exec-readout-and-decision.md)

The expert's permission maps are in `expert/maps/` in the harness format, and their test reports in `expert/reports/`. Every number computed from the data room, the harness and the simulation is real and reproducible; the red-team contractor's findings, the kill-switch drill and the events after 21 January are an illustrative worked example and say so. Lesson 14.6 reveals what was really going on at Lumen and three futures; read them only after scoring yourself.

</details>
