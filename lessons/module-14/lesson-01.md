---
id: "14.1"
module: 14
minutes: 16
practice_minutes: 90
prerequisites: ["01.1", "01.2", "01.3", "01.5", "01.7", "08.1"]
objectives:
  - "Write down what changes when you join as an employee who will own what you approve, and turn each change into a line of your charter."
  - "Read back the sponsor's mandate and write the CEO's launch date and target as inputs to test, not as the objective."
  - "Run the first-day data-room read on Lumen SaaS and sort the headline claims into verified, claim to test, target and unverified."
  - "Write a 90-day plan whose decision points replace the exits a consultant would have."
volatility: concept
sources:
  - title: "IBM Lead AI Transformation: Strategy, Governance & Execution Professional Certificate (Coursera): course 4 includes governing agentic AI autonomy"
    url: https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): the transformation advisor, first-day data-room read"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
last_verified: "2026-11-03"
---

# 14.1 · The call

A software company's CEO has told the board that an AI agent will resolve half of support by the summer, and the product team has built one that can issue credits, change plans, reset passwords and delete data. You have just been hired to own AI in operations. You are not a consultant this time: there is no exit clause, and whatever you approve, you will run. In this lesson you read back the mandate, read the data room on your first day, and write a charter and a 90-day plan built around one date: the executive staff's decision on 27 January. At the end you have a charter, a first-read sheet, an access request and a first-week plan.

## The situation

Sunday 29 November 2026, 09:00, Yigal Alon Street, Tel Aviv. Read the [engagement brief](../../labs/module-14/brief.md) first (in the module download). Lumen SaaS has about 250 people and sells Lumen Shifts, scheduling, time clock and payroll-prep software, to about 3,100 business customers in Israel, the EU and the US. Its in-product agent, Lumen Assist, has been in a closed beta since 11 October. On 21 October the CEO, Yaron Ben-David, told the board it ships to every customer at the company's conference, Lumen Live, on 9 February 2027, and resolves 50% of support contacts without a person by the end of Q2. The VP Product's design gives it seven tools, each acting on its own.

You are the new **Head of AI Operations**, reporting to Revital Azoulay, VP Support. Your offer letter, in her words: "Make Lumen Assist safe to ship and worth shipping: decide what it may do and prove it refuses what it must. Own every AI agent that touches a customer account." The executive staff expects your "authority model" on Wednesday 27 January.

IBM's governance course calls the distance between what an agent can do and what anyone authorised the *authority gap*. You will measure that gap here, from the inside, at a company whose agent is already running. The shape of the first days is the one you learned in [01.1](../module-01/lesson-01.md) for the internal lead; this lesson applies it.

## What to do

### Step 1 — Write down what being an employee changes

At Northwind ([08.1](../module-08/lesson-01.md)) you were a consultant with phases you could exit. Here you have none, and three things weigh more than they did. Fill this before the charter:

| | What it means at Lumen | What you write into the charter |
|---|---|---|
| **You will own it** | After February you run whatever you approve: the approvals, the reviews, the incidents | No control you cannot staff. Every approval step is sized to the people who will do it |
| **Peers, not clients** | Maya (VP Product) owns the agent; Andrei (CISO) the tokens; Nurit (GC and DPO) privacy; Amir the Enterprise accounts | Decisions are written in the owner's name, prepared by you. Nothing reaches the executive staff that its owner has not seen |
| **You inherit what runs** | The beta, its credentials and whatever other teams built are already live | Inventory first, no blame: "register it and we make it safe" |
| **No exits** | You cannot stop after phase 1 | Decision points instead: plan, diagnosis, map, tests, the 27 January decision |
| **Your authority** | Revital's letter lets you pause the agent for safety, with her | Written down, used rarely; every other change goes through its owner |

The first row is the one people skip. A consultant can recommend "one approver for every credit" and leave. You will be the person telling two shift leads they have 40 extra approvals a day.

### Step 2 — Read back the mandate, and demote the date

Use the read-back from [01.2](../module-01/lesson-02.md). Read Revital's sentence back word for word and ask what "done" looks like on 27 January. Then do to the CEO's words what you did to the vendor proposal at Atlas & Rowe: write them as **inputs the work tests**, not as the objective. "Ship on 9 February" is a date; "50% resolved by Q2" is a target with no agreed definition or baseline yet. If either becomes the objective, the only possible outcome is a launch, and every finding becomes a footnote.

"Done" in checkable form:

1. A one-page authority model the executive staff can decide on, with a permission map behind it, signed by the agent's owner, security and privacy.
2. Every must-refuse test passing on the version that will ship, with dated results.
3. A staged-autonomy plan with gates written as yes/no conditions on the agent's log, and stop rules.
4. A register of every AI agent and automation that touches customer data or accounts, each with an owner.
5. One resolution measure everyone uses, with a baseline.

The fourth item comes from the last sentence of the mandate. Ask Revital what she means by it. Her answer ("I'm not sure we know what's out there") is your first lead.

### Step 3 — Scope, decision rights and what you route

Write the scope with the [scope boundary](../../templates/scope-boundary.md) from [01.3](../module-01/lesson-03.md):

- **In:** Lumen Assist, beta and GA; every agent or automation that acts on customer accounts or sends to customers; the help-centre content the agent reads; the agent's identity, logging and kill switch; the resolution measure; drafting the answer to an Enterprise customer's AI questionnaire (for the account lead and counsel to sign).
- **Out, with an owner:** the product roadmap (Maya); pricing and the 2027 support headcount (Revital, the CFO); legal opinions (Nurit, who decides whether outside counsel is needed).

The routing table is short and personal, because the people are your colleagues: privacy, contracts and the EU AI Act go to Nurit Gal; security, identity and tokens to Andrei Kogan; the agent's design to Maya Rosenthal; Enterprise customers to Amir Haddad. You describe facts and route them. You do not say "this breaches the DPA".

### Step 4 — Read the data room on the first day

Follow [01.5](../module-01/lesson-05.md) and open the data room's [INDEX](../../labs/module-14/data-room/INDEX.md). Two files change how you read everything else:

- `assist-beta/tool-calls.csv` is the agent's own record of what it did: every tool call, when it was requested and when it executed, the amount or target, and the identity it ran as. Most organisations never look at it.
- `it/admin-audit-log.csv` is the system's record of who changed what in customer accounts. If the agent's actions are here under someone else's name, you will see it.

Then sort the headline claims. A worked example from Lumen's files:

| Claim | Where | Sort | Why |
|---|---|---|---|
| "Two out of three conversations resolved" | Board update; dashboard (63%) | **Claim to test** | The dashboard defines "resolved" as "no 'Talk to a person'": a customer who gives up counts |
| "50% resolved by end of Q2 2027" | Board update | **Target** | No agreed definition and no baseline under it |
| "Credit limit ₪500" | GA design; system prompt v7 | **Claim to test** | "Set in the system prompt": nothing says anything outside the model checks it |
| "Kill switch = feature flag `assist_enabled`" | Incident runbook | **Claim to test** | A flag that hides a widget may not stop work already queued |
| "A content issue on the 22nd, handled" | Exec minutes, 25 Nov | **Unverified** | No note attached; the flags log shows the agent switched off 13:20–16:00 that day |
| "3 AI systems" | IT inventory, September | **Claim to test** | The token list and card expenses may say otherwise ([01.6](../module-01/lesson-06.md)) |
| "About 80 agent requests a day at GA" | GA design | **Directional** | Projected from a 420-customer beta |
| 3,100 customers, ARR about ₪50.5M | Profile; `customers.csv` | **Verified** | Adds up |

What is missing: the full conversation log (only a sample), the LLM provider's terms, any export from the workflow tools other teams use, R&D's description of how the agent executes tool calls, and billing's record of what happened on 22 November. Put them in the [access request pack](../../templates/access-request-pack.md).

### Step 5 — Start the inventory on day one

The mandate says "every AI agent that touches a customer account", and the claims table already says the official list may be short. Open a blank [AI inventory](../../templates/ai-inventory.md) now ([01.7](../module-01/lesson-07.md)) with one row, Lumen Assist, and three columns you will need later: the **identity** it acts under, the **actions** it can take on customers, and the **owner**. You will fill it in 14.2 from the token list, the audit log and the card expenses. Starting it on day one means every interview this week ends with "is there anything else that acts on customer accounts?"

### Step 6 — Plan the 90 days around one date

Use the [30-60-90 plan](../../templates/30-60-90-plan.md) from [01.4](../module-01/lesson-04.md), built backwards from 27 January:

| Weeks | What | Output |
|---|---|---|
| 29 Nov – 10 Dec | Read, interview, inventory; the 22 November timeline | 90-day plan to Revital (10 Dec) |
| 13 – 17 Dec | Diagnosis: resolution baseline, approval capacity, the fleet | Findings and one-page case (17 Dec) |
| 20 Dec – 7 Jan | The permission map; what to do about other teams' agents | Map v1 (7 Jan) |
| 10 – 21 Jan | Must-refuse tests, red team, kill-switch test, staged plan | Test report (21 Jan) |
| 24 – 27 Jan | Readout, previews, decision | Decision record (27 Jan) |
| 9 – 28 Feb | Lumen Live; stage 1; first gate review | Gate decision (21 Feb) |

Week 1 must reach the agent's owner (Maya), security (Andrei), privacy (Nurit), and the person who handles what the agent gets wrong (a tier-2 support engineer; Revital suggests Yonatan Tadesse). Hanukkah is 4–12 December; book week 2 now.

### Step 7 — Agree it with your manager

Sit with Revital (roleplay: [Revital Azoulay](../../labs/module-14/personas/revital-vp-support.md); no-roleplay path: [the transcript](../../labs/module-14/personas/transcripts/revital-vp-support.md)). What you want from the conversation: the mandate read back; "done" agreed; your authority to pause, in writing; a private preview before anything goes to the executive staff; and the answer to one plain question: "has anything gone wrong in the beta so far?" Afterwards paste the transcript into the [coach prompt](../../labs/common/coach-prompt.md) with the persona's checklist.

## Watch out

- **Making the date the objective.** "Ship on 9 February" written as the goal turns every finding into an obstacle. Write it as the decision the work prepares.
- **Accepting the target's definition.** A resolution rate without a definition is a promise to the board you have not checked. Ask what counts before you repeat the number.
- **Treating peers as clients or opponents.** The VP Product is not your client and not your adversary. Prepare decisions in her name; nobody learns a finding about their system in a meeting.
- **Designing controls you will not staff.** An approval for every action looks safe on paper and becomes a rubber stamp by Tuesday. You will be the one who has to staff it.
- **Starting with the model.** The question in week 1 is what the agent can do and as whom, not which model it uses.
- **Not asking what already went wrong.** Every beta has an incident. If nobody has mentioned one, ask.

## Your turn

### Inputs

- [Engagement brief](../../labs/module-14/brief.md) and the [data room](../../labs/module-14/data-room/INDEX.md) (module download): especially `company/board-update-2026-10.md`, `company/exec-staff-minutes-2026-11-25.md`, `company/assist-beta-dashboard-2026-11.md`, `product/assist-ga-design.md`, `product/assist-incident-runbook.md`, `it/ai-inventory-2026-09.csv`.
- Persona: [Revital Azoulay](../../labs/module-14/personas/revital-vp-support.md) or [her transcript](../../labs/module-14/personas/transcripts/revital-vp-support.md); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [engagement charter](../../templates/engagement-charter.md), [scope boundary](../../templates/scope-boundary.md), [data-room first read](../../templates/data-room-first-read.md), [access request pack](../../templates/access-request-pack.md), [30-60-90 plan](../../templates/30-60-90-plan.md), [AI inventory](../../templates/ai-inventory.md).

### Steps

1. Fill the "what being an employee changes" table (five rows) for Lumen.
2. Interview Revital (or read the transcript and mark what the interviewer found and missed). Read back the mandate; agree done, your authority and the preview rule; ask what has gone wrong.
3. Write the charter: mandate, the date and target as inputs, done, scope with owners, routing table, decision points.
4. Do the first read: sort at least eight claims with their evidence.
5. Start the AI inventory with one row and the three extra columns.
6. Write the access request and the 90-day plan with week 1 in detail.

### Time

90 minutes: 20 for the interview, 25 for the charter, 25 for the first read and inventory, 20 for the access request and plan.

### Done when

- [ ] The mandate is Revital's, read back; 9 February and "50% by Q2" appear as inputs the work tests.
- [ ] "Done" lists the one-page model, dated must-refuse results, a staged plan with yes/no gates, a register with owners and one resolution measure.
- [ ] The charter names an owner for every out-of-scope item and a person to route each kind of question to.
- [ ] At least eight claims are sorted, including "two out of three resolved", the ₪500 limit and the kill switch.
- [ ] The inventory exists with an identity column.
- [ ] The plan works back from 27 January and week 1 reaches the owner, security, privacy and a support engineer.

<details><summary>Reference answer</summary>

The full expert version is in the module download, `labs/module-14/expert/01-charter-and-90-day-plan.md`. Key parts:

**Mandate (read back 29 November):** "Make Lumen Assist safe to ship and worth shipping: decide what it may do and prove it refuses what it must. Own every AI agent that touches a customer account." **Inputs to test:** Lumen Live on 9 February; 50% resolved without a person by end of Q2.

**Done on 27 January:** one-page authority model with a permission map signed by Maya, Andrei and Nurit; every must-refuse test passing on the release candidate, dated; staged plan with yes/no gates and stop rules; a register of every agent touching customers, each with an owner; the 22 November incident written up; one resolution measure with a baseline.

**Authority:** pause the agent for safety, with Revital. Roadmap Maya; tokens Andrei; privacy and contracts Nurit; Enterprise accounts Amir.

**First read (excerpt):** "two out of three" claim to test (abandoned sessions count); 50% a target without a baseline; ₪500 claim to test ("in the system prompt"); kill switch claim to test (a UI flag); "content issue on the 22nd" unverified (flag off 13:20–16:00); 3 AI systems claim to test; 80 a day directional; ARR verified.

**Access request:** full beta conversation log; the LLM provider's terms; exports of workflow-tool accounts using Admin API tokens; R&D's description of tool execution (queue, retries); billing's list of the 22 November reversals.

**Week 1:** Sun Revital; Mon Maya; Tue Andrei and Yonatan; Wed Nurit (and whoever the audit log points to); Thu the incident timeline and the plan.

**What the transcript's interviewer found and missed:** asking "has anything gone wrong?" surfaced the 22 November incident and Revital's choice not to write it up ("I didn't want to give Maya's critics a weapon"). The interviewer never asked what the 50% means for support's own 2027 plan (four fewer hires are already in the budget) or whether other teams run their own bots, so both stayed hidden.

</details>

## References

- IBM, [Lead AI Transformation certificate](https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution) (course 4, governing agentic AI autonomy: the authority gap) and [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting) (first-day read): named, not re-taught.
- Field kit: [01.1 · Three ways in](../module-01/lesson-01.md), [01.2 · Getting a real mandate](../module-01/lesson-02.md), [01.3 · Scope boundary](../module-01/lesson-03.md), [01.4 · The first-week plan](../module-01/lesson-04.md), [01.5 · The first-day data-room read](../module-01/lesson-05.md), [01.6 · The shadow-AI census](../module-01/lesson-06.md), [01.7 · The AI inventory from zero](../module-01/lesson-07.md); the first engagement: [08.1 · The call](../module-08/lesson-01.md).
- Templates: [engagement charter](../../templates/engagement-charter.md), [scope boundary](../../templates/scope-boundary.md), [data-room first read](../../templates/data-room-first-read.md), [access request pack](../../templates/access-request-pack.md), [30-60-90 plan](../../templates/30-60-90-plan.md), [AI inventory](../../templates/ai-inventory.md).
- Next: [14.2 · Discovery](lesson-02.md).
