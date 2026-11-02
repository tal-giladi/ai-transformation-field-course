# Steering readout, decision record and handover — Northwind Outfitters

Expert deliverable for lesson 08.6. Steering committee Tuesday 12 January 2027, 09:00–10:00; pre-read
sent Thursday 7 January; private sessions with Gil (10 January) and Boris (11 January). Templates:
[steering pack](../../../templates/steering-pack.md), [decision record](../../../templates/decision-record.md),
[integration check](../../../templates/integration-check.md), [handover pack](../../../templates/handover-pack.md).

## 1. The pack: front page

**Decision asked.** Approve: (1) publish returns policy v2 on 1 February (signed by COO, CFO, counsel);
(2) inspection within 2 business days and a daily card-refund run from 1 February; (3) the chatbot stays
limited to order status, and the Verbalo renewal is negotiated on a new "resolution" definition with the
training opt-out, notice sent by 1 March if not agreed; (4) agent-assist in shadow mode from 1
February, Hebrew and English first, gate on 1 April; (5) no further reduction in agents before the April
gate; the 2027 budget restated on cost per order. **Decline:** the chatbot on returns, refunds and
WhatsApp in 2027 H1.

**One sentence.** Half of support cannot be replaced by a bot that repeats four contradictory returns
policies; fix the policy and the refund clock, give agents drafts that get the policy right, and measure
cost per order and repeat contacts monthly.

**What changed since 3 December.** Counsel marked up policy v2 (17 December). The offline test: drafts
consistent with v2 on 95.8% of returns tickets against 55.6% for today's replies (illustrative for the
model; today's figure measured); rules alone 79.6%. The bot has answered no returns questions since 10
December; billed resolutions fell from 6,000 (October) to an estimated 3,800 (December).

**What a "no" means.** The bot extension proceeds on a policy counsel has flagged; the demand letter
has no answer; agents keep choosing between four policies.

**What it costs in 2027.** Two returns clerks ≈ ₪252,000; SMS job ≈ ₪40,000 + ₪3,000 a month;
agent-assist ₪150,000 one-off + ≈ ₪12,000 a month; deductions and breakage given up (measured in the
extract, scaled): fees above the cap ≈ ₪1.4M, defect deductions ≈ ₪0.4M, shipping ≈ ₪2.3M (★ business
choice), part of ≈ ₪2.6M breakage. The 2027 customer-service budget of ₪6.09M (21 agents from April) is
not supported by evidence; we propose a range of 25–27 agents by year-end through attrition, gated.

## 2. The recommend-against, stated plainly

We recommend **against** extending the chatbot to returns, refunds and WhatsApp. Evidence: 64.1% of its
"resolved" chats are followed by an agent contact within 7 days; 50 of 69 of its policy answers
contradict Northwind's own terms; its cost per truly resolved chat (≈ ₪14) is above an agent's (≈ ₪13);
it does not speak Arabic or Russian before Q3 2027.

## 3. The hardest finding and the rehearsal

**Hardest finding (for Gil):** "The 30% handling-time reduction on your September slide compares two
different measures, and the headcount reduction was made before anyone tested the bot. Customers now
contact us more often per order than before."

Rehearsed with Gil privately on Sunday 10 January. What worked: his own question from the fund first
("how is containment measured, do customers come back?") and the answer to it; then the AHT definition
as a BI change log fact, not a blame; then what he can tell the board: "We found that our returns
policy, not the bot, drives half our contacts. We are fixing it, measuring cost per order monthly, and
the team will get smaller through attrition, gated in April." What failed in the first rehearsal: opening
with the headcount decision (he went defensive).

## 4. Integration check (excerpt)

| Claim | Where it rests | Timing traced to | Control and its cost |
|---|---|---|---|
| ≈ 6,800 fewer contacts a month | Assumed reductions on directional shares (03) | Policy live 1 Feb; refund clock 1 Feb | BI repeat-contact measure, monthly (Alexei, 2 days a month) |
| 352 net hours from agent-assist | Assumed 4.0 min saved; illustrative acceptance | Shadow 1 Feb; gate 1 Apr | Timer in Tikra; 100 native-rated drafts per language (≈ 40 agent-hours) |
| Decision right 95.8% | Offline test, frozen | Re-run on any prompt or model change | Eval re-run ≈ ₪60 and 2 hours each time |
| No wrong refunds sent | Agent sends every reply | From day 1 of shadow mode | Weekly sample of 100 sent replies (Meseret's team, 4 hours) |
| Bot cost falls | Contract renegotiation | Notice by 1 March | Counsel review before signing |

Contradictions found and fixed before the pre-read: the decision paper said the bot would be narrowed
"from 10 December", a draft of the pack said "by January" (10 December, done); the 352 agent-assist
hours appeared in a draft budget line as ₪220,000 saved (removed: capacity, gated in April); the weekly
100-reply sample had no hours (4 hours a week added to the customer-service team plan).

## 5. Decision record (as minuted, 12 January 2027)

**Decided:** items (1)–(4) approved; item (5) approved with a change: "no further reduction before the
April gate; HR and counsel to advise on any change after it". Bot extension: declined for H1 2027,
revisit at the October steering. **Owners:** policy v2 Orly; refund clock Yaron Peretz and Boris; bot
contract Hila with Alexei; agent-assist Meseret (owner), Alexei (sandbox); measures Alexei. **Stop
rules:** as in the pilot charter. **Next decision:** Tuesday 6 April 2027 gate (scale / fix / stop for
agent-assist; budget restatement). **Dissent noted:** Gil asked that "AI phase two" remain on the
roadmap for H2; recorded as a candidate, not a commitment.

## 6. Handover (Thursday 14 January)

Owner: Meseret Tadesse, with Alexei Morozov for data. Pack: the deliverable map; policy v2 and its
change history; the pilot (prompt v1.2, rules, test set, labels, scripts, eval reports); the monitoring
spec (weekly sent-reply sample, banned-phrase check, negative-test re-run on every change, repeat-contact
measure monthly); the operating rhythm (monthly review, Meseret chairs; quarterly steering, Orly
chairs); open questions for counsel (bot chats and the four-month rule; used items; the demand letter);
contacts at Verbalo. One follow-up call with the consultant on 1 April, before the gate.
