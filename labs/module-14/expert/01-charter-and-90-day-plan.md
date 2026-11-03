# 01 · Charter and 90-day plan — Head of AI Operations, Lumen SaaS

*Expert deliverable for lesson 14.1. Written Sunday 29 November – Thursday 10 December 2026; agreed with Revital
Azoulay (VP Support) on 10 December. All people and companies are fictional.*

## Mandate (read back to Revital, 29 November)

> "Make Lumen Assist safe to ship and worth shipping: decide what it may do and prove it refuses what it must.
> Own every AI agent that touches a customer account."

**The question this work answers by 27 January:** what Lumen Assist may do at Lumen Live on 9 February, for
whom, under which controls, and how autonomy grows after that. The CEO's target ("50% of support contacts
resolved without a person by end of Q2") is an input to test, not the objective.

**Done on 27 January means:**

1. A one-page authority model the executive staff can decide on, with a permission map behind it, signed by
   the agent's owner (Maya), security (Andrei) and privacy (Nurit).
2. Every must-refuse test passing on the version that will ship, with the results dated.
3. A staged-autonomy plan with dates, gates written as yes/no conditions on the log, and stop rules.
4. A register of every AI agent and automation that touches customer data or accounts, each with an owner.
5. The 22 November incident written up, with fixes and owners.
6. A resolution measure everyone uses, with a baseline.

## What changes because I am an employee, not a consultant

| | At Lumen | What I do about it |
|---|---|---|
| Ownership | Whatever I approve, I run and answer for after February | No control I cannot staff; approvals sized to the shift leads' real hour a day |
| Peers, not clients | Maya owns the agent; Andrei the tokens; Nurit privacy; Amir Enterprise accounts | Decisions in their names, prepared by me; nothing goes to executive staff they have not seen |
| Inheritance | The beta, a shared token and other teams' automations already run | Inventory first, without a blame hunt: "register it and we make it safe" |
| No exit | I cannot stop after a phase | The 90-day plan has decision points instead: 10 Dec (plan), 17 Dec (diagnosis), 7 Jan (map), 21 Jan (tests), 27 Jan (decision) |
| Authority | I may pause the agent for safety, with Revital | Used once if needed; every other change through its owner |

## Scope

**In:** Lumen Assist (beta and GA); every agent or automation that acts on customer accounts or sends to
customers; the help-centre content the agent reads; the agent's identity, logging and kill switch; the
resolution measure; the answer to Shaked's section 7 (drafted for Amir and Nurit).
**Out, with owner:** the product roadmap (Maya); pricing and the 2027 support headcount (Revital, Oren); legal
opinions (Nurit, outside counsel if she wants); the core product's auto-scheduling under the EU AI Act (Nurit,
Q1 note).

## First read (day 1, from the data room)

| Number or claim | Where | Sort | Why |
|---|---|---|---|
| "Two out of three resolved" | Board update; dashboard (63.2%) | **Claim to test** | Defined as "no 'Talk to a person'": abandoned sessions count as resolved |
| 50% resolved by Q2 2027 | Board update | **Target, not a baseline** | No measured starting point under any agreed definition |
| ₪500 credit limit | GA design; prompt v7 | **Claim to test** | "Set in the system prompt": nothing says it is enforced |
| "Kill switch = feature flag" | Runbook | **Claim to test** | A flag that hides a widget may not stop queued jobs |
| "A content issue on the 22nd, handled" | Exec minutes | **Unverified** | No note attached; flags log shows the agent off 13:20–16:00 |
| 3 AI systems | IT inventory, Sept | **Claim to test** | Token list and card expenses suggest more |
| ~80 agent requests a day at GA | GA design | **Directional** | Projected from a 420-customer beta |
| ARR ₪50.5M, 3,100 customers | Profile; customers.csv | **Verified** | Adds up |

## Access request (sent 30 November)

Read-only admin console; the full conversation log for the beta (not only the sample); the LLM provider's
contract and data terms; exports of every workflow-tool account that uses an Admin API token; R&D's description
of how Assist executes tool calls (queue, retries); billing's list of the 22 November reversals.

## 90-day plan (to 28 February)

| Weeks | What | Output | With |
|---|---|---|---|
| 29 Nov – 10 Dec | Read, interview, inventory; incident timeline | 90-day plan; draft incident write-up | Revital, Maya, Andrei, Yonatan, Nurit, Shira |
| 13 – 17 Dec | Diagnosis: resolution baseline, approval capacity, the fleet | Findings memo and one-page case to Revital (17 Dec); 20 min with Yaron | Yaron, Svetlana (customer) |
| 20 Dec – 7 Jan | The permission map; Renewal Rescue decision; Shaked draft | Permission map v1 (7 Jan); section 7 draft to Amir (7 Jan) | Maya, Andrei, Nurit, Amir, Shira |
| 10 – 21 Jan | Must-refuse tests, red-team, kill-switch test, staged plan | Test and red-team report; staged plan (21 Jan) | Noam, Yonatan, R&D on-call, red-team contractor |
| 24 – 27 Jan | Readout; executive staff decides (27 Jan) | One page; decision record | Revital first, then exec staff |
| 9 Feb – 28 Feb | Lumen Live; stage 1; daily review; gate review 21 Feb | Daily log reviews; gate decision | Shift leads, Noam |

## Week 1

Sun: Revital (mandate, authority, preview rule). Mon: Maya (GA design). Tue: Andrei (tokens, audit log),
Yonatan (22 November timeline). Wed: Nurit (privacy, EU, terms); Shira (after the audit log pointed at 02:00
actions). Thu: write the incident timeline; draft the plan.

## Risks to this work

The date decides by default (mitigation: a launch scope ready on 7 January, so "not ready" is never the
answer); the incident becomes a blame story (no names in any written finding; the system, not people); Product
reads the map as a veto (Maya co-owns stage 2's gate); approvals overload two shift leads (stage 1 sized to 17 a
day against 30).
