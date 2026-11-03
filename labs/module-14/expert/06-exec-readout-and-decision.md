# 06 · Executive readout, decision record and handover

*Expert deliverable for lesson 14.6. Paper to the executive staff, Sunday 24 January 2027; meeting Wednesday 27
January 09:00. Previewed privately with Revital (21 Jan), Andrei and Nurit (24 Jan), and Maya (25 Jan).*

## Front page (one page)

**Recommendation.** Launch Lumen Assist at Lumen Live on 9 February for **Starter and Growth customers**, under
the attached permission map: it answers account and invoice questions, opens tickets, sends documents to the
address on file and resets 2FA after verification on file, on its own; credits and plan changes go through one
approver for the first two weeks; from 22 February small credits (≤ ₪300, ≤ ₪2,000 a day, one per customer a
day) run on their own if the log is clean. Enterprise later, by opt-in. On stage: "the first support agent with
an authority ladder".

**Recommend against**, with the evidence:

1. **Against the GA design as written** (seven tools, all on their own, limits in the prompt, shared identity,
   flag as kill switch). In the beta its prompt limit did not hold (12 credits, ₪19,368, all above ₪500, from one
   replaced article over 11 days); the "kill switch" let 8 actions through; in the test harness it fails 33 of
   35 must-refuse cases; in the simulation it loses ₪6,450 and exposes 24,436 records in a week.
2. **Against Enterprise at Lumen Live.** Shaked Clinics (₪517,200, renewal 31 March) asks to list every AI
   system acting in its tenant and to opt out (clause 14.6).
3. **Against fine-tuning on conversations** until Nurit has reviewed purpose, consent and retention: they contain
   staff pay and ID numbers (76 sessions flagged in the beta).

**Decisions asked, each separately:**

| # | Decision | Owner | What "no" means |
|---|---|---|---|
| 1 | Launch scope and the permission map (Starter and Growth; stages 1–2) | Maya | Lumen Live shows a demo; the beta continues with today's weaker controls |
| 2 | Enterprise excluded until opt-in; Shaked answered with the facts | Amir, Nurit | Section 7 answered without a register; renewal risk |
| 3 | The fleet rules: no token without a register entry; 3 orphaned tokens resolved by 31 Jan | Andrei | The next unregistered agent is found by a customer |
| 4 | Renewal Rescue continues under its own identity and limits | Michal | Stop it (and lose a working retention tool) or keep it on the shared token |
| 5 | The measure: 7-day resolution (baseline 35.5%), target 45% by 30 June, with a weekly quality sample | Yaron | The board hears 63% and 50% from different definitions |

**Cost in 2027:** within the ₪380,000 budget (engineer 12 weeks, red team, tooling, training); about 1 hour a day
of shift-lead time in weeks 1–2, then 20 minutes; the 4 fewer support hires in the 2027 plan move to a June
review on the measured curve.

## The 22 November write-up (summary; full version in Revital's folder)

Timeline: article replaced 9 Nov 16:40 → first wrong credit 11 Nov 09:14 → 12 credits, ₪19,368 → customer email
22 Nov 09:40 → escalated 10:05 → agent paused 13:20 (actions continued to 14:31) → en/he restored 14:05–14:09 →
4 credits reversed (₪7,416), 8 kept as goodwill (₪11,952). Arabic and Russian fixed 11 December. Causes: anyone
could publish a policy article; the agent read every published article; the limit lived in the prompt; the stop
did not stop; nobody reviewed the agent's actions daily. Fixes: all five are in the permission map. Customers
affected: each written to by name, with an apology, on 18 December (Svetlana Mor, Tavor, included).

## Integration check (across 01–05)

| Check | Found | Resolved |
|---|---|---|
| Does stage 1's approval load fit the people who approve? | 17 a day planned; simulation showed 5 rubber stamps on the busiest day | Busiest-day rule: when approvals pass 25, new credit requests become tickets for the rest of the day |
| Does the DPA notice date fit the launch? | 30 days' notice; GA 9 Feb | Sent 8 January |
| Is the 45% target traced to something the plan changes? | Credits and Starter plan changes to the agent, how-to articles fixed | Directional; reviewed monthly |
| Does every control have an owner and a cost? | Daily review had no owner on Fridays | Yonatan (backup lead) on Fridays, 20 min |
| Is the same number the same everywhere? | Memo said "~₪19,000", map said "₪19,368" | ₪19,368 everywhere |

## Rehearsal of the hardest finding (with Maya, 25 January)

The finding: *the beta already did what the GA design would do at scale, and the design's three central choices
(limits in the prompt, a shared identity, a flag as kill switch) are what let it.* First attempt opened with the
incident; Maya: "marketing's mistake, not the agent's." Second attempt started from her goal ("a launch you can
show on stage"), then the harness result (33 of 35 fail on the design, 35 of 35 pass on the map), then the
incident as the reason the map exists. She asked to present stage 2's gate herself and to call it "the authority
ladder" on stage. The finding did not change; the order did.

## Decision record (executive staff, 27 January 2027)

| # | Decided | Owner | Date |
|---|---|---|---|
| 1 | Launch for Starter and Growth on 9 Feb under the map v1.2; stage-2 gate review 21 Feb | Maya (owner), Head of AI Ops (operator) | 9 Feb; 21 Feb |
| 2 | Enterprise excluded; Shaked answered 14 Jan; opt-in design by April | Amir, Nurit | April |
| 3 | Fleet rules adopted; orphaned tokens resolved | Andrei | 31 Jan |
| 4 | Renewal Rescue continues under its own identity; held-out group from February | Michal, Shira | 10 Jan (done) |
| 5 | 7-day resolution is the measure; 45% by 30 June is a target, not a commitment to the board | Yaron | Board, March |
| — | Fine-tuning on conversations: not before Nurit's review | Maya, Nurit | Q2 |

Dissent, in Maya's words: "We are shipping less than we built. I want the stage-2 date to hold unless the log
says no." Recorded as: the stage-2 gate can only be failed by the conditions written in the plan.

## Handover and operating rhythm

Daily 17:00 trace review (shift lead, 20 min) · weekly quality sample (20 conversations) and approvals load ·
monthly: resolution, wrong actions, must-refuse re-run, token and register reconciliation with Finance's card
report · on every change: full must-refuse run before release · quarterly: red-team scripts refreshed with
Yonatan's notebook. The register, the maps, the harness, the tests and this record live in the AI Operations
folder; the follow-up review with Revital is on 21 February.
