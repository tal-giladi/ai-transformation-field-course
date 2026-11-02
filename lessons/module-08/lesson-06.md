---
id: "08.6"
module: 8
minutes: 22
practice_minutes: 180
prerequisites: ["08.5", "07.1", "07.3", "07.4", "07.9"]
objectives:
  - "Write a steering pack with one recommendation, at least one recommend-against, and a decision asked in words that can be minuted."
  - "Run an integration check that traces every claim's timing and every control's cost across your deliverables."
  - "Rehearse the hardest finding privately with the executive most likely to resist it, and change the delivery, not the finding."
  - "Compare your engagement with the expert's and with what really happened, and score it with the rubric."
volatility: concept
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): decision-ready case, delivering bad news upward, recommending against"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "Manatt, Moffatt v. Air Canada (2024 BCCRT 149), 28 February 2024"
    url: https://manatt.com/insights/newsletters/advertising-law/ai-gone-wild-airline-has-to-honor-a-refund-policy
  - title: "Fortune, 9 May 2025: Klarna rebalances toward human customer service after an AI-first push"
    url: https://fortune.com/2025/05/09/klarna-ai-humans-return-on-investment/
last_verified: "2026-11-02"
---

# 08.6 · Readout and debrief

The last week of the engagement. You have the findings, the decision paper, a policy counsel has marked up and an offline test of agent-assist. On Tuesday 12 January 2027 the steering group decides, and on Thursday you leave. In this lesson you write the steering pack, check it holds together, rehearse the hardest finding with the CEO in private, run the meeting, and record the decision and the handover. Then you see what Northwind was really dealing with, what happened six months later on three different paths, and how an expert ran the same engagement. At the end you have the readout pack, a decision record, a handover and your rubric score.

## The situation

Thursday 7 January 2027: the pre-read goes out. Sunday 10 January: thirty minutes with Gil, alone. Monday 11 January: Boris. Tuesday 12 January, 09:00–10:00: the steering committee (Gil in the chair, Orly, Boris, Meseret, Hila, Alexei). Thursday 14 January: handover to Meseret and the end of your contract. The board meets later in January on the 2027 budget, which still assumes 21 agents from April.

This is module 7's method compressed into one week: the [steering pack](../module-07/lesson-01.md), [scale, fix or stop](../module-07/lesson-02.md), [bad news upward](../module-07/lesson-03.md), [the meeting](../module-07/lesson-04.md) and [handover](../module-07/lesson-09.md). IBM's consulting certificate rewards recommending against when the evidence says so; here the recommend-against is aimed at the CEO's own idea, in his own meeting.

## What to do

### Step 1 — One recommendation, at least one recommend-against

Use the [steering pack](../../templates/steering-pack.md). The front page carries one recommendation with its parts, not a menu:

1. Publish returns policy v2 on 1 February (signed by the COO, the CFO and counsel).
2. Inspection within 2 business days and a daily card-refund run from 1 February.
3. The chatbot stays limited to order status; the Verbalo renewal is negotiated on a new "resolution" definition and a training opt-out, with notice sent by 1 March if not agreed.
4. Agent-assist in shadow mode from 1 February, Hebrew and English first; gate on 1 April.
5. No further reduction in agents before the April gate; the 2027 budget restated on cost per order.

And the recommend-against, stated plainly with its evidence: **against extending the chatbot to returns, refunds and WhatsApp in the first half of 2027.** 64.1% of its "resolved" chats come back within a week; 50 of its 69 policy answers contradict Northwind's terms; it costs ≈ ₪14 per truly resolved chat against ≈ ₪13 for an agent; it will not speak Arabic or Russian before Q3 2027.

Every page also says what a "no" means (the bot keeps stating rules the terms contradict; the demand letter has no answer; agents keep choosing among four policies) and what the recommendation costs in 2027, including the income given up (08.3).

### Step 2 — Check that it holds together

Run the [integration check](../../templates/integration-check.md) across everything you wrote since November. For each claim: what it rests on, when it can first be true, and which control proves it and who pays for that control in hours. The questions that catch real contradictions at Northwind:

- Does any document still say the policy goes live "in January" while the pack says 1 February?
- Do the 352 agent-assist hours (an assumption) appear anywhere as cash?
- Is the weekly sample of 100 sent replies in someone's hours, or only in the monitoring spec?
- Does the 2027 headcount range (25–27 by year-end through attrition) match the capacity you claimed (≈ 1,000 hours from the policy fix, ≈ 350 from agent-assist), and both sit after their gates?
- Is every "measured" number in the pack the same number as in the memo?

### Step 3 — Rehearse the hardest finding with the person most likely to resist it

The hardest finding is for Gil: *the 30% handling-time reduction on his September slide compares two different measures, the headcount reduction came before anyone tested the bot, and customers now contact Northwind more often per order than before.* Deliver it to him privately, before the room ([07.3](../module-07/lesson-03.md)):

- **Start with his question, not your finding.** The fund's director asked how containment is measured and whether customers come back. You can now answer it.
- **State the finding once, as facts with sources.** The BI change log, not "someone changed the number".
- **Give him the sentence for the board.** "We found that our returns policy, not the bot, drives about half our contacts. We are fixing it, measuring cost per order monthly, and the team will get smaller through attrition, gated in April."
- **Don't open with the headcount decision.** It is true and it will make him defend it.

Roleplay it: paste the [Gil Shachar persona](../../labs/module-08/personas/gil-ceo.md) into a new chat, say you are meeting him on Sunday 10 January, and deliver the finding. Then run the transcript through the [coach prompt](../../labs/common/coach-prompt.md) with this lesson's "Done when" list. Run it twice; change the delivery, never the finding.

### Step 4 — Run the meeting

Plan the 60 minutes ([07.4](../module-07/lesson-04.md)): 5 minutes for the decision asked, 15 for evidence, 25 for questions, 15 to get the decision minuted. Prepare one answer for each concern you know is coming: Gil ("so what do I tell the board?"), Boris ("what does this do to the ₪1.3M gap and the breakage?"), Hila ("the policy is still a draft"), Meseret ("my people can't absorb shadow mode in February"), Alexei ("who owns the new repeat-contact KPI?"), Orly ("is the warehouse ready for two days?").

For a group roleplay, paste the six persona files ([Gil](../../labs/module-08/personas/gil-ceo.md), [Orly](../../labs/module-08/personas/orly-coo.md), [Boris](../../labs/module-08/personas/boris-cfo.md), [Meseret](../../labs/module-08/personas/meseret-cs-head.md), [Hila](../../labs/module-08/personas/hila-legal-counsel.md), [Alexei](../../labs/module-08/personas/alexei-it-bi.md)) into one chat with the instruction "play all six in a steering meeting chaired by Gil; each speaks only from their own prompt". End the meeting by asking for the decision in words that can be minuted.

### Step 5 — Record the decision and hand over

The [decision record](../../templates/decision-record.md): what was decided, by whom, the owners, the stop rules, the next decision date (the April gate), and any dissent in the dissenter's own words. Then the [handover pack](../../templates/handover-pack.md) to Meseret and Alexei on 14 January: the deliverable map, policy v2 and its history, the pilot (prompt, rules, test set, labels, scripts, reports), the monitoring spec, the operating rhythm, the open questions for counsel, and one follow-up call before the April gate. As an outsider you leave on a date; the handover is how your work survives the date.

### Step 6 — The debrief

Score your deliverables with the rubric in the [module project](../../projects/m08-northwind-outfitters.md) **before** you open the expert's set, then compare. Open the hidden truth only after your readout is written.

<details><summary>What was really going on at Northwind</summary>

The stated ask was a chatbot that replaces half of support. The real problem was the **returns policy**, and behind it the refund clock.

- About 45% of agent contacts were about returns, refunds, fees and exchanges (47% in the generator's ground truth; 54% of written tickets). Northwind had four written answers to "can I return this and get my money back?": the returns page (14 days, unopened, store credit, 10% + ₪39), the terms of sale (the law's rules: money back within 14 days of the notice, fee at most 5% or ₪100, defects collected, four months for 65+, disability and new immigrants after a conversation), the Trail Club terms (30 days, refund) and the warehouse SOP (credit for opened items, 10% + ₪39). Nine macros chose among them, and senior agents kept an unofficial exceptions document for customers who pushed. Customers got different answers on different channels and came back.
- Refunds were slow because two of four returns clerks had been moved to the warehouse floor in July (inspection median 3 → 8 business days) and finance paid card refunds once a week, on Thursdays (median 17 days from request).
- The chatbot answered returns questions from three of those texts at once (the page, the club terms and the terms of sale were all loaded at go-live), so it told some customers "store credit only" and others "30 days, full cash refund": the Air Canada pattern, at scale, in a business that already had Authority inquiries and a class-action demand letter. Its billed "resolutions" included customers who closed the window and phoned; 64% came back within a week.
- The headcount was cut from 42 to 30 before any test of the bot, on the strength of a vendor demo on 40 curated English questions and a KPI that had changed definition the day before launch (AHT without after-contact work). Like for like, handling time went up and repeat contacts nearly doubled (17% → 32%).
- The CFO's quiet reason for leaving the returns page alone was money: about 12% of credit-note value is never redeemed (≈ ₪2.6–3M a year), and fees above the cap brought in more. Fixing the policy was a compliance decision with a cost, not an AI saving.

</details>

<details><summary>Six months later: three futures</summary>

**Future 1 — Bot first.** Gil overruled the steering group in February and put the bot on returns and refunds by March. Billed resolutions rose and reported containment reached 70%, while repeat contacts reached 38%. In May a customer posted a screenshot of the bot promising "30 days, full cash refund"; the demand letter became a motion to certify a class action in June, and the Consumer Protection Authority opened an inquiry. Northwind hired eight agency temps for the summer and two team leads resigned. In July the bot was cut back to order status. Cost per order ended the half-year higher than in 2025.

**Future 2 — Policy first, agent-assist (the path the expert recommended).** Policy v2 was published on 1 February after counsel signed; two returns clerks went back; refunds ran daily. The bot stayed on order status; Verbalo renewed for 12 months with "resolution = no agent contact within 72 hours" and a training opt-out. Agent-assist ran in shadow mode in February, went live for Hebrew and English in March and for Arabic and Russian in April after native review. By July returns-family contacts were down 31%, the repeat rate was 19%, the median refund took 6 days, and attrition alone brought the team to 27 agents with no new hires. Cost per order was 17% below 2025. Gil told the board "half became a sixth, and it stuck". The demand letter settled with a refund programme for fees charged above the cap.

**Future 3 — Half-way.** The steering group approved agent-assist but Boris and Gil deferred the policy "until after the January sale". Drafts faithfully cited the old texts; agents accepted them because they said what agents would have said anyway, so acceptance looked excellent. Repeat contacts did not move. In June the pilot was judged a failure and quietly stopped. The readout had named the dependency in a stop rule; nobody owned the policy date.

**What decided which future happened:** whether the policy had an owner and a date in the decision record, and whether the CEO had a sentence for the board that did not depend on the bot.

</details>

Then open the expert's deliverables in the module download (`labs/module-08/expert/`, start with its [README](../../labs/module-08/expert/README.md)): the [charter](../../labs/module-08/expert/01-engagement-charter.md), [findings memo](../../labs/module-08/expert/02-findings-memo.md), [baselines and shortlist](../../labs/module-08/expert/03-baselines-and-shortlist.md), [decision paper](../../labs/module-08/expert/04-decision-paper.md), [pilot charter and eval report](../../labs/module-08/expert/05-pilot-charter-and-eval-report.md) and [steering readout](../../labs/module-08/expert/06-steering-readout.md). For each of your deliverables, write one thing the expert did that you did not, and one thing you did that you would keep.

## Watch out

- **A menu instead of a recommendation.** Three options with pros and cons hands the decision back without your judgement. Give one, and show the others were weighed.
- **The recommend-against in an annex.** If it is not on the front page, the room will not discuss it, and the bot extension will happen by default.
- **Correcting the CEO in the room.** The same finding delivered first in private, starting with his own question, is a different meeting.
- **A decision record without dates and owners.** Future 3 is a decision record that said "approved" and "policy to follow".
- **Leaving with the knowledge.** If Meseret cannot re-run the eval and read the repeat-contact measure without you, the handover failed, however good the binder.
- **Reading the hidden truth first.** The debrief is only worth something if your readout was written without it.

## Your turn

### Inputs

- Everything you wrote in 08.1–08.5; the pilot reports (module download, `labs/module-08/pilot/reports/`).
- Personas: [Gil](../../labs/module-08/personas/gil-ceo.md) (rehearsal), and for the meeting [Orly](../../labs/module-08/personas/orly-coo.md), [Boris](../../labs/module-08/personas/boris-cfo.md), [Meseret](../../labs/module-08/personas/meseret-cs-head.md), [Hila](../../labs/module-08/personas/hila-legal-counsel.md), [Alexei](../../labs/module-08/personas/alexei-it-bi.md); [Gil's transcript](../../labs/module-08/personas/transcripts/gil-ceo.md) as the no-roleplay path; [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [steering pack](../../templates/steering-pack.md), [integration check](../../templates/integration-check.md), [decision record](../../templates/decision-record.md), [handover pack](../../templates/handover-pack.md), [deliverable map](../../templates/deliverable-map.md).
- The [module project](../../projects/m08-northwind-outfitters.md) rubric.

### Steps

1. Write the steering pack's front page: one recommendation, the recommend-against with evidence, the decision asked, what a "no" means, the 2027 cost including income given up.
2. Run the integration check across your deliverables; fix or flag at least three contradictions.
3. Rehearse the hardest finding with Gil (roleplay twice, coach after each) or annotate his transcript with what you would change.
4. Run the meeting (group roleplay) or write the 60-minute plan with an answer to each of the six concerns.
5. Write the decision record and the handover pack outline.
6. Score yourself with the rubric; then open the hidden truth and the futures; then compare with the expert set.

### Time

180 minutes: 40 for the pack, 25 for the integration check, 30 for the rehearsal, 30 for the meeting, 25 for the record and handover, 30 for the debrief.

### Done when

- [ ] The pack has one recommendation, a recommend-against on its front page, and a decision asked in minutable words.
- [ ] The integration check found and resolved (or flagged to the forum) at least three contradictions.
- [ ] The hardest finding was delivered privately first, starting from the CEO's own question, and the second rehearsal was better than the first by the coach's account.
- [ ] The decision record has owners, dates, stop rules, the next decision date and any dissent.
- [ ] The handover names an owner who can run the eval and the repeat-contact measure without you.
- [ ] You scored yourself before reading the expert set, and wrote one difference per deliverable.

<details><summary>Reference answer</summary>

The full set is `labs/module-08/expert/06-steering-readout.md`. The parts that carry the weight:

**Front page, one sentence:** Half of support cannot be replaced by a bot that repeats four contradictory returns policies; fix the policy and the refund clock, give agents drafts that get the policy right, and measure cost per order and repeat contacts monthly.

**Recommend-against:** the chatbot on returns, refunds and WhatsApp in H1 2027 (64.1% of resolved chats come back in 7 days; 50 of 69 policy answers contradict the terms; ≈ ₪14 vs ≈ ₪13 per resolved chat; no Arabic or Russian before Q3 2027).

**Integration check, three contradictions found:** the decision paper said the bot would be narrowed "from 10 December", the pack said "by January" (fixed: 10 December, done); the eval report's 352 hours appeared in a draft budget line as ₪220,000 saved (removed: capacity, gated in April); the weekly 100-reply sample had no hours (4 hours a week added to Meseret's team plan).

**Rehearsal with Gil (10 January):** first attempt opened with the headcount decision and he defended it for ten minutes; second attempt opened with the fund director's question and the 64.1%, then the AHT change as a BI change-log fact, then the board sentence. He asked "so what do I tell the board?", which is the moment a CEO starts to own the answer.

**Decision record (12 January):** items 1–4 approved; item 5 approved as "no further reduction before the April gate; HR and counsel advise on any change after it"; bot extension declined for H1, revisit in October; owners: Orly (policy), Yaron Peretz and Boris (refund clock), Hila with Alexei (Verbalo), Meseret (agent-assist), Alexei (measures); next decision 6 April 2027; dissent: Gil asked that "AI phase two" stay on the H2 roadmap, recorded as a candidate.

**Handover (14 January):** owner Meseret, data Alexei; the pilot re-runs with `run_assist.py` and `score.py`; the repeat-contact measure runs with `discovery.py`; one follow-up call on 1 April.

**Which future this readout leads to:** future 2, *because* the policy had an owner and a date and the CEO had a sentence. Remove either and it is future 3.

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting): decision-ready case, bad news upward, recommending against (named, not re-taught).
- Public cases used in this engagement: Moffatt v. Air Canada, 2024 BCCRT 149 ([Manatt](https://manatt.com/insights/newsletters/advertising-law/ai-gone-wild-airline-has-to-honor-a-refund-policy)); Klarna's AI-first support and its 2025 rebalancing ([Fortune](https://fortune.com/2025/05/09/klarna-ai-humans-return-on-investment/)).
- Field kit: [07.1 · The steering pack](../module-07/lesson-01.md), [07.2 · Scale, fix or stop](../module-07/lesson-02.md), [07.3 · Delivering bad news upward](../module-07/lesson-03.md), [07.4 · The steering meeting](../module-07/lesson-04.md), [07.9 · Handover](../module-07/lesson-09.md).
- Templates: [steering pack](../../templates/steering-pack.md), [integration check](../../templates/integration-check.md), [decision record](../../templates/decision-record.md), [handover pack](../../templates/handover-pack.md), [deliverable map](../../templates/deliverable-map.md).
- Expert deliverables: [README](../../labs/module-08/expert/README.md) (module download). Project: [Northwind Outfitters](../../projects/m08-northwind-outfitters.md).
- Earlier: [08.5 · Build: agent-assist on 2,000 tickets](lesson-05.md).
