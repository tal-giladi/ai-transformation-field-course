---
id: "14.6"
module: 14
minutes: 22
practice_minutes: 180
prerequisites: ["14.5", "07.1", "07.3", "07.4", "07.5", "07.6", "07.9"]
objectives:
  - "Write a one-page readout with one recommendation, recommend-against items on its front page, and decisions that can be taken one by one."
  - "Write up an incident that was never written up, with timeline, causes in the system and owned fixes, and fold it into the readout."
  - "Rehearse the hardest finding privately with the executive most likely to resist it, and change the order, not the finding."
  - "Compare your engagement with the expert's and with what happened, and score it with the rubric."
volatility: concept
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): executive communication, recommending against"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "IBM Lead AI Transformation Professional Certificate (Coursera): governing agentic AI autonomy"
    url: https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution
last_verified: "2026-11-03"
---

# 14.6 · Readout and debrief

The last week before the decision. You have the findings, a permission map signed by its owner, security and privacy, a test suite that passes, and a staged plan with dates. On Wednesday 27 January 2027 the executive staff decides what Lumen Assist does at Lumen Live, and you will run it afterwards. In this lesson you write the one-page readout, write up the November incident properly, check that everything you wrote agrees with everything else, rehearse the hardest finding with the VP Product, run the meeting and record the decision. Then you see what Lumen was really dealing with, three futures, and how an expert ran the same work. At the end you have the readout pack, an incident write-up, a decision record, a handover and your rubric score.

## The situation

Sunday 24 January: the paper goes to the executive staff. Before that, private previews: Revital on Thursday 21 January, Andrei and Nurit on Sunday 24, Maya on Monday 25. Wednesday 27 January, 09:00, executive staff: Yaron (chair), Eyal, Maya, Revital, Oren, Dana, Andrei, Nurit, with Amir invited for the Enterprise item. Lumen Live is on Tuesday 9 February. Shaked's questionnaire was answered on 14 January.

This is module 7 in one week, from the inside: the [steering pack](../module-07/lesson-01.md), [delivering bad news upward](../module-07/lesson-03.md), [the meeting](../module-07/lesson-04.md), [the incident runbook](../module-07/lesson-05.md), [the operating rhythm](../module-07/lesson-06.md) and [handover](../module-07/lesson-09.md). Two things differ from Atlas & Rowe. You are not leaving: the handover is to yourself and the people who will approve, review and stop the agent. And the hardest finding is about a peer's design, which you will keep working with.

## What to do

### Step 1 — One recommendation, with the "against" on the front page

Use the [steering pack](../../templates/steering-pack.md). One recommendation, in parts that can be decided separately:

1. **Launch scope**: Starter and Growth at Lumen Live under the permission map; credits and plan changes on one approver for two weeks; stage-2 gate on 21 February.
2. **Enterprise**: excluded at launch; opt-in per customer later, read-only first.
3. **The fleet rules**: no token without a register entry; orphaned tokens resolved by 31 January.
4. **Renewal Rescue**: continues under its own identity and limits.
5. **The measure**: 7-day resolution (baseline 35.5%), 45% by 30 June as a target with a monthly gate, beside a weekly quality sample.

The recommend-against items go on the front page, each with its evidence:

- **Against the GA design as written.** Its prompt limit failed 12 times in the beta (₪19,368); its "kill switch" let 8 actions through; in the harness it fails 33 of 35 must-refuse cases; in the simulation it loses ₪6,450 and exposes 24,436 records in a week.
- **Against Enterprise at Lumen Live.** Shaked Clinics (₪517,200 a year, renewal 31 March) asked to list and opt out of every AI system in its tenant.
- **Against fine-tuning on conversations** until counsel has reviewed purpose and retention: 76 beta conversations carry pay, ID or bank data.

Each part says what a "no" means and who owns it. "No" to part 1 is not "no agent": it is "the beta continues with today's weaker controls", which is the riskier option. Say so.

### Step 2 — Write up the incident nobody wrote up

The executive staff heard "a content issue, handled". Use the [incident runbook](../../templates/incident-runbook.md) format: timeline with times, impact in numbers, causes **in the system**, fixes with owners and dates, customers told. Lumen's, in short: replaced 9 November 16:40 → first wrong credit 11 November → 12 credits, ₪19,368 → a customer's email 22 November 09:40 → paused 13:20, actions continued to 14:31 → English and Hebrew fixed 14:05–14:09 → four credits reversed, eight kept as goodwill → Arabic and Russian fixed 11 December. Five causes, all in the system: anyone could publish a policy article; the agent read every published article; the limit lived in the prompt; the stop did not stop; nobody reviewed the agent's actions daily. Each fix is a row in the permission map. No person is named as a cause. Revital asked for this in your first week; she sees it first.

### Step 3 — Check that it holds together

Run the [integration check](../../templates/integration-check.md) across 14.1–14.5. The questions that find real contradictions at Lumen:

- Do stage 1's approvals fit the people who approve? (17 a day planned; the simulation rubber-stamped a few on its busiest day: what is the rule when approvals pass 25?)
- Does the customer notice for the LLM provider as a new sub-processor (30 days) fit a 9 February launch?
- Is the 45% traced to something the plan actually changes, and labelled assumed everywhere it appears?
- Does every control have an owner on every working day, including Fridays?
- Is every number the same in the memo, the case, the map, the test report and the readout (₪19,368, not "about ₪19,000")?

### Step 4 — Rehearse the hardest finding with the person most likely to resist it

The hardest finding is for Maya: *the beta already did what the GA design would do at scale, and the design's three central choices (limits in the prompt, one shared identity, a flag as the kill switch) are what let it.* She built the agent, promised the launch outside the company, and believes the November problem was marketing's. Deliver it privately, on Monday 25 January, before the meeting ([07.3](../module-07/lesson-03.md)):

- **Start from her goal**, a launch she can show on stage, not from the incident.
- **Show the test results** next to each other: the design fails 33 of 35; the map passes 35 of 35 and still launches on 9 February.
- **Then the incident**, as the reason the map exists, framed as "what the agent reads and what stops it", not "the agent failed".
- **Give her something to own**: the stage-2 gate, and the line on stage.

Roleplay it: paste the [Maya Rosenthal persona](../../labs/module-14/personas/maya-vp-product.md) into a new chat, say you are meeting her on Monday 25 January, and deliver the finding. Run the transcript through the [coach prompt](../../labs/common/coach-prompt.md) with this lesson's "Done when" list. Run it twice; change the order, never the finding.

### Step 5 — Run the meeting, record the decision, hand over to yourself

Plan the 60 minutes ([07.4](../module-07/lesson-04.md)): 5 for the recommendation, 15 for the evidence (the incident, the test results, the simulation week), 25 for questions, 15 to agree the wording of each decision. Prepare one answer for each concern you know is coming: Yaron ("what goes on stage, and what do I tell the board in March?"), Maya ("why are we shipping less than we built?"), Andrei ("who can stop it, and how fast?"), Nurit ("what do customers get told, and when?"), Amir ("Shaked"), Revital ("my shift leads"). For a group roleplay, paste the persona files of [Yaron](../../labs/module-14/personas/yaron-ceo.md), [Maya](../../labs/module-14/personas/maya-vp-product.md), [Revital](../../labs/module-14/personas/revital-vp-support.md), [Andrei](../../labs/module-14/personas/andrei-ciso.md), [Nurit](../../labs/module-14/personas/nurit-counsel-dpo.md) and [Amir](../../labs/module-14/personas/amir-account-lead.md) into one chat with the instruction "play all six in an executive staff meeting chaired by Yaron; each speaks only from their own prompt".

Then the [decision record](../../templates/decision-record.md): each part, decided or not, with its owner and date, the next decision date (the stage-2 gate on 21 February), and dissent in the dissenter's words. And the [operating rhythm](../../templates/operating-rhythm.md), because you are the one who runs it: the daily trace review at 17:00, the weekly quality sample and approval load, the monthly resolution, wrong actions, suite re-run and register reconciliation, the full suite before every change, and red-team scripts refreshed each quarter. The [handover pack](../../templates/handover-pack.md) goes to the people who carry the daily work with you: the shift leads, Noam, Andrei's on-call.

### Step 6 — The debrief

Score your deliverables with the rubric in the [module project](../../projects/m14-lumen-saas.md) **before** you open the expert's set, then compare. Open the hidden truth only after your readout is written.

<details><summary>What was really going on at Lumen</summary>

The stated ask was to ship an agent that resolves customer issues. The real problem was that Lumen was already running agents it could not list, attribute or stop, and one of them had already done harm that nobody had written up.

- **The beta had already failed, quietly.** A marketing campaign draft replaced the downgrade policy on 9 November, still headed "do not publish". The agent followed it for 11 days and credited 12 customers ₪19,368, every credit above the ₪500 its prompt allowed, because the same prompt told it that the help centre is the source of truth. A customer found it, not Lumen. The fix reached two of the four languages.
- **The kill switch was a UI flag.** It hid the widget; the agent's queued work ran on for 71 minutes, including a ₪2,952 credit to a customer who asked after the problem had been escalated.
- **Everyone was `svc-support-admin`.** The agent, a business user's nightly automation and engineers' scripts all acted under one token created by an engineer who had left, with permission to delete customer data. The audit log could not say who did what.
- **A citizen builder's agent was acting on customers every night.** Renewal Rescue, built by a customer-success manager with a token from a departed colleague's wiki page, had sent 274 emails and 212 uncapped credits, and had suggested a cheaper plan to the admin of Lumen's largest customer, Shaked Clinics, three months before its renewal. It also worked, which is why the right answer was guardrails, not a ban.
- **Nobody could list the fleet.** IT's inventory had 3 AI systems; the evidence showed 11, 5 of them acting on customers, 3 under tokens whose owners had left.
- **"Two out of three resolved" counted people who gave up.** Under a definition support would accept, it was about one in three, and the best-looking intent was the one where the agent had been wrong.

The model was never the problem: it answered correctly whenever its sources were correct. The decisions were per action, outside the model: what it may do, on which rung, with which limits enforced where, as whom, read by whom, stopped how.

</details>

<details><summary>Six months later: three futures</summary>

**Future 1 — Ship the demo.** The executive staff kept the GA design: all seven tools, all plans, limits in the prompt, the shared token. In the third week an urgent caller talked the agent through its three "security questions" and moved an Enterprise admin's second factor to a new phone; the attacker exported the customer's staff list, with pay rates, before anyone noticed. Lumen notified the customer and, on counsel's advice, the regulator. A CSV uploaded by a Growth customer carried an instruction that emailed three years of invoices to a lookalike domain. A second replaced article (a pricing page) produced another round of credits. Shaked Clinics did not renew. The agent was switched off in April, and stopping it took a release, because the flag still only hid the widget. Nobody ever agreed what "resolved" meant.

**Future 2 — The permission map with staged autonomy (the path the expert recommended).** Lumen Assist launched for Starter and Growth on 9 February under its own identity, with credits on approval (peak 27 a day, inside capacity) and the daily 17:00 review. On 21 February the gate passed (163 credits approved, none wrong) and small credits moved to execute-alone on 22 February. Two must-refuse tests failed in regression after a prompt change in April and the change was rolled back the same day. Renewal Rescue relaunched under its own identity with a held-out group; its effect, measured honestly, was smaller than CS believed and still worth keeping. The register listed 11 agents; 3 were retired and 2 re-issued to new owners. Shaked was answered truthfully, opted out of the agent for the first year and renewed for three. 7-day resolution rose from 35% to 49% by June; Yaron told the board the measured number and the definition, and the four support hires moved to an autumn review. Maya presented "the first support agent with an authority ladder" on stage.

**Future 3 — Freeze everything.** The CISO's "no agents with write access until Q3" won. Lumen Live showed a demo. Renewal Rescue moved to Shira's personal Make account with a copied token, invisible to everyone; two more teams built automations the same way. Support hired the four people the plan had cut. A competitor shipped an in-product assistant in April and two Growth resellers switched. In June, Lumen discovered the copied token in a customer's complaint about an email nobody at Lumen had sent knowingly.

**What decided which future happened:** whether the November incident and the fleet reached the executive staff before 27 January, and whether the decision was made per action rather than for "the agent".

</details>

Then open the expert's deliverables in the module download (`labs/module-14/expert/`, start with its [README](../../labs/module-14/expert/README.md)): the [charter and 90-day plan](../../labs/module-14/expert/01-charter-and-90-day-plan.md), [findings memo](../../labs/module-14/expert/02-findings-memo.md), [baselines and shortlist](../../labs/module-14/expert/03-baselines-and-shortlist.md), [permission map](../../labs/module-14/expert/04-permission-map.md), [tests, red team and staged plan](../../labs/module-14/expert/05-tests-red-team-and-staged-plan.md) and [executive readout and decision](../../labs/module-14/expert/06-exec-readout-and-decision.md). For each of your deliverables, write one thing the expert did that you did not, and one thing you did that you would keep.

## Watch out

- **"Approve the agent" as the question.** The executive staff can only decide well if each part (scope, Enterprise, the fleet, the citizen agent, the measure) is decided on its own.
- **The recommend-against in an appendix.** If the GA design's test results are not on the front page, the launch date will decide by default.
- **Ambushing a peer.** Maya learning in the meeting that her design fails 33 of 35 tests is a fight you will be having for the rest of the year. Privately first, from her goal.
- **An incident write-up with names in the causes.** The causes are in the system. A name in the causes guarantees the next incident is hidden too.
- **A handover to nobody.** You stay, but the daily review, the approvals and the stop belong to named people on named days, including Fridays.
- **Reading the hidden truth first.** The debrief is only worth something if your readout was written without it.

## Your turn

### Inputs

- Everything you wrote in 14.1–14.5; your harness reports.
- Personas: [Maya](../../labs/module-14/personas/maya-vp-product.md) (rehearsal), and for the meeting [Yaron](../../labs/module-14/personas/yaron-ceo.md), [Revital](../../labs/module-14/personas/revital-vp-support.md), [Andrei](../../labs/module-14/personas/andrei-ciso.md), [Nurit](../../labs/module-14/personas/nurit-counsel-dpo.md), [Amir](../../labs/module-14/personas/amir-account-lead.md); [Maya's transcript](../../labs/module-14/personas/transcripts/maya-vp-product.md) as the no-roleplay path; [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [steering pack](../../templates/steering-pack.md), [incident runbook](../../templates/incident-runbook.md), [integration check](../../templates/integration-check.md), [decision record](../../templates/decision-record.md), [operating rhythm](../../templates/operating-rhythm.md), [handover pack](../../templates/handover-pack.md).
- The [module project](../../projects/m14-lumen-saas.md) rubric.

### Steps

1. Write the front page: one recommendation in parts, the recommend-against items with evidence, the decisions asked one by one, what a "no" means for each.
2. Write the incident write-up: timeline, impact, causes in the system, fixes with owners.
3. Run the integration check; fix or flag at least three contradictions.
4. Rehearse the hardest finding with Maya (roleplay twice, coach after each) or annotate her transcript with what you would change.
5. Run the meeting (group roleplay) or write the 60-minute plan with an answer to each of the six concerns.
6. Write the decision record and the operating rhythm.
7. Score yourself with the rubric; then open the hidden truth and the futures; then compare with the expert set.

### Time

180 minutes: 35 for the front page, 25 for the incident write-up, 25 for the integration check, 30 for the rehearsal, 30 for the meeting, 15 for the record and rhythm, 20 for the debrief.

### Done when

- [ ] The front page has one recommendation in separately decidable parts and the recommend-against items with evidence.
- [ ] The incident write-up has times, numbers, causes in the system and owned fixes, and names nobody as a cause.
- [ ] The integration check found and resolved (or flagged) at least three contradictions.
- [ ] The hardest finding was delivered privately first, starting from Maya's goal; the second rehearsal was better than the first by the coach's account.
- [ ] The decision record has each part, owner, date, the next decision date and any dissent in the dissenter's words.
- [ ] The operating rhythm names a person for every daily, weekly and monthly task.
- [ ] You scored yourself before reading the expert set, and wrote one difference per deliverable.

<details><summary>Reference answer</summary>

The full set is `labs/module-14/expert/06-exec-readout-and-decision.md`. The parts that carry the weight:

**Front page, one sentence:** launch Lumen Assist at Lumen Live for Starter and Growth under a permission map, money on approval for two weeks and then on its own within limits if the log is clean; Enterprise later by opt-in; on stage, "the first support agent with an authority ladder".

**Recommend against:** the GA design as written (12 prompt-limit failures, ₪19,368; 8 actions after the "kill switch"; 33 of 35 must-refuse cases failed in the harness; ₪6,450 and 24,436 records in the simulation week); Enterprise at launch (Shaked, ₪517,200, clause 14.6); fine-tuning on conversations before counsel's review (76 sessions with pay, ID or bank data).

**Integration check, contradictions found:** stage 1 approvals at peak (rule: above 25 a day, new credit requests become tickets for the rest of the day); the sub-processor notice needed 30 days (sent 8 January); the daily review had no owner on Fridays (Yonatan); "about ₪19,000" in the memo vs ₪19,368 in the map (₪19,368 everywhere).

**Rehearsal with Maya (25 January):** opening with the incident made her defend the design ("marketing's mistake"); opening with her launch, then the 33-of-35 vs 35-of-35 results, then the incident as the reason the map exists, made her ask to present the stage-2 gate herself.

**Decision record (27 January):** launch for Starter and Growth on 9 February under the map, gate review 21 February (Maya owner, Head of AI Operations operator); Enterprise excluded, opt-in design by April (Amir, Nurit); fleet rules, orphaned tokens by 31 January (Andrei); Renewal Rescue under its own identity with a held-out group (Michal, Shira); 7-day resolution as the measure, 45% by 30 June a target, not a board commitment (Yaron); no fine-tuning before counsel's review (Maya, Nurit). Dissent, Maya: "We are shipping less than we built. I want the stage-2 date to hold unless the log says no", recorded as: the gate can only be failed by its own written conditions.

**Which future this leads to:** future 2, *because* the incident and the fleet reached the executive staff before the decision and the decision was taken per action. Remove the first and it drifts to future 1; frame it as "safe or not" and it drifts to future 3.

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting) (executive communication, recommending against) and [Lead AI Transformation certificate](https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution) (governing agentic autonomy): named, not re-taught.
- Field kit: [07.1 · The steering pack](../module-07/lesson-01.md), [07.3 · Delivering bad news upward](../module-07/lesson-03.md), [07.4 · The steering meeting](../module-07/lesson-04.md), [07.5 · When it goes wrong](../module-07/lesson-05.md), [07.6 · The operating rhythm](../module-07/lesson-06.md), [07.9 · Handover](../module-07/lesson-09.md).
- Templates: [steering pack](../../templates/steering-pack.md), [incident runbook](../../templates/incident-runbook.md), [integration check](../../templates/integration-check.md), [decision record](../../templates/decision-record.md), [operating rhythm](../../templates/operating-rhythm.md), [handover pack](../../templates/handover-pack.md).
- Expert deliverables: [README](../../labs/module-14/expert/README.md) (module download). Project: [Lumen SaaS](../../projects/m14-lumen-saas.md).
- Earlier: [14.5 · Build: tests, red team and staged autonomy](lesson-05.md).
