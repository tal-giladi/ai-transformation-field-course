# Vantage Logistics

Run the whole rescue at Vantage Logistics, a fictional Israeli logistics and freight-forwarding group with about 1,200 people in four regions, as the interim AI lead the board engaged for 30 days after its head of AI resigned. You report to the chair of the audit committee and to the CEO. Your job is to find out what the AI programme really is, close the incident it left open, decide what stops and what continues system by system, and give the board a brief it can test on 5 July. This is module 17's practical: one integrated deliverable set, every document consistent with every other.

## The brief

Read [the engagement brief](../labs/module-17/brief.md) (in the module download). In short: you start on Sunday 6 June 2027; the board's questions are in its minute of 3 June; the region-reduction notice under the vendor's agreement must go by Thursday 1 July, the same day as the audit committee's pre-read; the board meets on Monday 5 July; your engagement ends on Tuesday 6 July. The data room is `labs/module-17/data-room/` (start with its [INDEX](../labs/module-17/data-room/INDEX.md)); the people are in `labs/module-17/personas/` ([the cast](../labs/module-17/personas/README.md)); the audit sheet and the Track B scripts are in `labs/module-17/`.

## Deliverables

| # | Deliverable | Template | Lesson |
|---|---|---|---|
| 1 | **Reporting protocol** signed by both principals; **mandate memo** (objective read back, the headlines as claims, done, entry-role table, scope, advisory boundary); first-read sheet; access request; **day-one triage**; 30-day plan | [engagement charter](../templates/engagement-charter.md), [scope boundary](../templates/scope-boundary.md), [data-room first read](../templates/data-room-first-read.md), [access request pack](../templates/access-request-pack.md), [30-60-90 plan](../templates/30-60-90-plan.md) | [17.1](../lessons/module-17/lesson-01.md) |
| 2 | **Incident status note** (week one) and **findings memo** with every number labelled: inventory from zero, the incident from the logs, the review measured, the regions tested, licences and money, people | [AI inventory](../templates/ai-inventory.md), [interview guide](../templates/interview-guide.md), [findings memo](../templates/findings-memo.md) | [17.2](../lessons/module-17/lesson-02.md) |
| 3 | **Baseline table** (one measure and owner per system), **savings restated** (cash and capacity apart), **overrun decomposed**, the binding constraint, non-AI fixes, the **one-page case** | [ROI model](../templates/roi-model.md), [opportunity map](../templates/opportunity-map.md), [decision-ready case](../templates/decision-ready-case.md) | [17.3](../lessons/module-17/lesson-03.md) |
| 4 | **Turnaround plan**: dated audit rules, **pressure-test log** of the inherited programme, control test, **trust-repair plan** by audience, the agreement with both principals | [pressure-test log](../templates/pressure-test-log.md), [risk register](../templates/risk-register.md), [comms plan](../templates/comms-plan.md) | [17.4](../lessons/module-17/lesson-04.md) |
| 5 | **Stop/keep audit** of all nineteen lines with the money; **incident closure record** by the runbook with closure criteria; Docs' conditions; **three decision records** | [AI inventory](../templates/ai-inventory.md), [incident runbook](../templates/incident-runbook.md), [decision record](../templates/decision-record.md) | [17.5](../lessons/module-17/lesson-05.md) |
| 6 | **30-day board brief** (the five answers, three recommend-againsts, the section for the audit committee), **integration check**, notes of the **rehearsal** with the CEO, **decision record** with a stop rule, **handover** | [steering pack](../templates/steering-pack.md), [integration check](../templates/integration-check.md), [decision record](../templates/decision-record.md), [handover pack](../templates/handover-pack.md), [deliverable map](../templates/deliverable-map.md) | [17.6](../lessons/module-17/lesson-06.md) |

## Steps

1. Read the brief and the INDEX; fill the entry-role table; write and agree the reporting protocol with Ilana and Ofer; write the mandate memo, the first read, the access request, the triage and the plan (17.1).
2. Interview at least four of Dmitri, Rania, Tesfaye, Svetlana and Yaniv, and plan and use your one call with Itai; build the inventory; test the incident record, the review, the regions and the invoices; send the status note in week one; write the findings memo (17.2; Track B: `discovery.py`).
3. Build the baseline table; compute the fuel and warehouse effects; restate the savings; decompose the overrun; write the case and walk it through, CEO first (17.3).
4. Fix the audit rules; pressure-test the deck and its "Next" slide; test the controls; plan trust repair; interview Tesfaye and Rania with consultation promised; agree the plan with both principals (17.4).
5. Run the audit (Track B: `audit.py`; Track A: `audit-sheet.csv`); close the incident by the runbook; write Docs' conditions and the three decision records; meet Orit and Yaniv (17.5).
6. Write the brief and the committee section; run the integration check; rehearse with Ofer twice; plan the board item; write the decision record and the handover (17.6).
7. Score your set with the rubric below **before** you open the hidden truth and the expert set in 17.6; then compare.

Time: about 4 hours beyond the lessons' own exercises, most of it in steps 5–7.

## Self-assessment rubric

| Criterion | What "strong" looks like | What "weak" looks like |
|---|---|---|
| Entry and protocol | A written protocol both principals agreed before any finding: CEO first on management findings, chair the same day, governance facts to the chair without conclusions, legal to counsel; the March headlines, "contained" and "savings back on track" recorded as claims | Reporting to "the board and the CEO" undefined; "savings back on track" adopted as the goal; the incident record taken at its word |
| Incident discovery | The incident's scope from the logs (mismatches by version, submitted, post-fix; cross-customer opens, documents, customers, records; customs queries) compared with the record and sent to both principals and counsel within the week | The incident held for the memo; "contained" repeated; scope from the vendor's analysis |
| Evidence | Twelve systems with sources, the dashboard kept out of the count; the review measured in seconds and a re-checked error rate with its interval; regions tested by month; every number labelled M, R or C | The register taken as the inventory; vendor accuracy quoted; "adoption problems" in the regions |
| Money | One measure and owner per system; fuel and warehouse effects against a comparison; ₪6.2M restated to what is evidenced, cash and capacity apart; the overrun explained by cause | The dashboard's figure scaled or argued with; capacity counted as cash; the overrun hidden in the restatement |
| Turnaround | Rules dated before the list, applied per system and region; the inherited "Next" slide pressure-tested; controls tested; each audience gets one kept promise first; the works committee promised consultation before change | Decisions for "the platform"; rules written after the list; messages instead of actions; the committee told what will happen |
| Audit and decisions | Nineteen lines each with a rule, action, owner, contract step and a dated saving; the vendor's offer recognised and the notice given; Docs kept only under checkable conditions with a stop rule | Savings booked before contracts allow them; the offer accepted; "keep with conditions" without a measure |
| Incident closure | Containment proven from the logs; facts to counsel and the customs agent with who decides each question; no legal deadline stated as yours; the root cause rewritten as contributing causes with fixes; closure criteria and which are met | Legal questions answered; the vendor's root cause adopted or the agents blamed; "closed" on someone's request |
| People affected | The customer gets one apology and facts with dates; the drivers' committee gets the score switched off and a written answer; nobody interviewed is blamed in writing | A blanket "no personal data"; a vision presented to the committee; names in the memo |
| Board brief | The board's five questions answered in order with labels; three recommend-againsts; governance facts to the committee with sources and no characterisation; the CEO's own sentence; "contained, not closed" | A programme-level verdict; conclusions about the CEO; a surprise for him in the room; "closed" |
| Follow-through | A decision record with owners, a stop rule, re-decision dates and dissent; a handover where every line has an owner who stays after day 30 and the measures run on fixed rules | You remain the owner of anything; measures left to the next hire |

## Model answer

<details><summary>Model answer</summary>

The expert's deliverable set is in the module download, `labs/module-17/expert/` ([README](../labs/module-17/expert/README.md)):

- [01 · Reporting protocol, mandate memo and the 30-day plan](../labs/module-17/expert/01-protocol-charter-and-30-day-plan.md)
- [02 · Findings memo](../labs/module-17/expert/02-findings-memo.md)
- [03 · What each system is worth, and the one-page case](../labs/module-17/expert/03-baseline-and-case.md)
- [04 · The turnaround plan, the audit rules and the pressure-test](../labs/module-17/expert/04-turnaround-plan-and-pressure-test.md)
- [05 · Stop/keep audit, incident closure and the decisions that could not wait](../labs/module-17/expert/05-stop-keep-audit-and-incident-closure.md)
- [06 · The 30-day board brief, rehearsal, decision record and handover](../labs/module-17/expert/06-board-brief.md)

Every count, sum and share computed from the data room is real and reproducible with `discovery.py` and `audit.py`. Lesson 17.6 reveals what was really going on at Vantage and three futures; read them only after scoring yourself.

</details>
