---
id: "13.6"
module: 13
minutes: 22
practice_minutes: 180
prerequisites: ["13.5", "07.1", "07.3", "07.4", "07.9"]
objectives:
  - "Write a readout for a management meeting chaired by the owner, with one recommendation, a recommend-against on its front page, and what the owner can tell the customer."
  - "Run an integration check across your deliverables and fix the contradictions before the pre-read goes out."
  - "Rehearse the hardest finding privately with the owner who made the ask, and change the delivery, not the finding."
  - "Record the decision with owners, dates and a re-decision date, hand over so the foundation survives you, and compare your engagement with the expert's and with what really happened."
volatility: concept
sources:
  - title: "Histadrut, AIG Israel workers' committee declare labour dispute over AI (13 August 2026)"
    url: https://global.histadrut.org.il/news/aig-israel-workers-committee-declare-labour-dispute-over-ai/
  - title: "Organisation of Labour Supervision (Safety Management Programme) Regulations, 5773-2013, reg. 5(6) and 5(10), Hebrew Wikisource"
    url: https://he.wikisource.org/wiki/תקנות_ארגון_הפיקוח_על_העבודה_(תכנית_לניהול_הבטיחות)
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): decision-ready case, delivering bad news upward, recommending against"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
last_verified: "2026-11-03"
---

# 13.6 · Readout and debrief

The owner asked for predictive maintenance. You are about to tell him, in front of his management team, that the company is not ready for it, that you want half of his AI budget spent on registers, tablets and a toolmaker's phone number, and that the thing that will help Arava this quarter has no AI in it at all. In this lesson you write the readout, check that it holds together, rehearse the hardest finding with the owner alone, run the meeting, and record the decision and the handover. Then you see what was really going on at Kinneret, what happened six months later on three different paths, and how an expert ran the same engagement. At the end you have the readout, a decision record, a handover and your rubric score.

## The situation

Thursday 18 March 2027: the pre-read goes out. Sunday 21 March: thirty minutes with Amnon, alone. Tuesday 23 March, 10:00–11:00: the management meeting (Amnon in the chair; Dalia Mizrahi, Orit Navon, Eli Peretz, Vladimir Kaplan, Rotem Levi, Michal Aharon; Khalil Mansour invited for the item on workers). Wednesday 31 March: Arava's deadline. Predictiva's "conference price" expires the same day.

You stay at Kinneret after Tuesday, with your OEE reports and whatever the meeting decides. This is module 7 compressed: the [steering pack](../module-07/lesson-01.md), [scale, fix or stop](../module-07/lesson-02.md), [bad news upward](../module-07/lesson-03.md), [the meeting](../module-07/lesson-04.md) and [handover](../module-07/lesson-09.md). IBM's consulting certificate rewards recommending against when the evidence says so; here the recommend-against is aimed at the owner's own idea, in his own company.

## What to do

### Step 1 — One recommendation, a recommend-against, and something for Arava

Use the [steering pack](../../templates/steering-pack.md). One recommendation, in parts, each with an owner and a date:

1. **Arava plan:** night mould response, shot counters on the hot-runner moulds, the six machines' PMs restored, QA cover for first-article approval at night (from 1 April; target OTIF 92% in Q3, 95% in Q4).
2. **Foundation:** common register incl. moulds (30 April), recording at the machine in three languages (Plant K 30 April, Plant G 30 June), live parts view (31 March), sensors on eight machines (30 September).
3. **Manual-assistant pilot:** shadow use on the night shift from 4 April; live after the joint committee's review.
4. **Protocol with the works committee** signed before any change on the floor (31 March).
5. **Money:** ₪730,000 of line 7400-210 in three stages, with the stop rule.

The recommend-against, on the front page, with its evidence: **no contract and no letter of intent with Predictiva in 2027, and no cameras.** 73 usable failure labels in 861 breakdowns, none of the 30 per mode the vendor itself requires (measured); the platform covers machine faults, 24% of lost hours, not moulds, 46% (measured); at its own best figure it returns ≈ ₪257k a year against ≈ ₪343k a year of cost (directional). And what "no" to your recommendation means: an Arava plan with nothing on night moulds, and the same records in January 2028.

### Step 2 — Check that it holds together

Run the [integration check](../../templates/integration-check.md) across everything since January. The questions that catch real contradictions at Kinneret:

- Do all documents give the same date for recording at Plant G (the case said 30 April; the protocol says nothing changes before the joint committee meets there)?
- Do the assistant's freed hours appear anywhere as shekels?
- The protocol says the assistant's logs carry no user id. Does the tool's admin console agree?
- Does the Arava plan promise an OTIF that depends on something nobody owns (QA cover at night is Rotem's decision)?
- Is every "measured" number the same in the memo, the case, the verdict and the readout?

### Step 3 — Rehearse the hardest finding with the owner

The hardest finding is for Amnon: **no Predictiva this year, and the conference conversation set a deadline that is not Kinneret's.** Deliver it to him alone on Sunday, before the room ([07.3](../module-07/lesson-03.md)):

- **Start with his question, not your finding.** On 12 January he said "Arava back to 95%". Start there.
- **Show, don't argue.** The night mould hours; Tigist's account of the October short shots; K22's vibration climbing for three weeks while nobody watched.
- **Give the vendor its due.** "Predictiva would watch the quarter that is machines. Here is what would make it worth buying in January 2028."
- **Give him something to own.** He tells Gilad himself that Kinneret will run a proof of concept in 2028 on its own data and its own protocol.

Roleplay it: paste the [Amnon Shaked persona](../../labs/module-13/personas/amnon-ceo.md) into a new chat, say you are meeting him on Sunday 21 March, and deliver the finding. Run the transcript through the [coach prompt](../../labs/common/coach-prompt.md) with this lesson's "Done when" list. Run it twice; change the delivery, never the finding.

### Step 4 — Run the meeting

Plan the 60 minutes ([07.4](../module-07/lesson-04.md)): 5 for the decision asked, 15 for evidence, 25 for questions, 15 to minute the decision. Prepare one answer for each concern you know is coming: Amnon ("so when do we become modern?"), Orit ("what are the gates and who owns each?"), Dalia ("what goes to Arava on 30 March?"), Eli ("Galil could start in April"), Vladi ("who types all this at three in the morning?"), Rotem ("night QA cover is a headcount question"), Michal and Khalil ("the protocol must be signed before the tablets arrive").

For a group roleplay, paste the files of [Amnon](../../labs/module-13/personas/amnon-ceo.md), [Dalia](../../labs/module-13/personas/dalia-vp-operations.md), [Orit](../../labs/module-13/personas/orit-cfo.md), [Eli](../../labs/module-13/personas/eli-plant-g-manager.md), [Vladi](../../labs/module-13/personas/vladimir-maintenance-manager.md) and [Khalil](../../labs/module-13/personas/khalil-works-committee.md) into one chat with the instruction "play all six in a management meeting chaired by Amnon; each speaks only from their own prompt". End by asking for the decision in words that can be minuted.

[Simulation: Steering committee](../../simulations/steering-committee/index.html?preset=harbor)

### Step 5 — Record the decision and hand over

The [decision record](../../templates/decision-record.md): what was decided, owners, dates, the stop rule, the **re-decision date for predictive maintenance (January 2028) with its criteria**, and any dissent in the dissenter's own words. The [handover pack](../../templates/handover-pack.md): business owner (Dalia), technical owners (Vladi for the register, recording and pack; Boaz Tal for the tools; Yaakov Dahan for the safety documents), a senior technician named to co-own the failure list and the pack before Vladi retires, the [deliverable map](../../templates/deliverable-map.md), `readiness_audit.py` re-run monthly, the test set and gates re-run after every pack change, the protocol and its six-month review. The safety management programme already requires a list of items needing periodic tests and of procedures with their update dates; the common register and the pack are now where those lists live, so name who keeps them. Write down the date you stop owning each part.

### Step 6 — The debrief

Score your deliverables with the rubric in the [module project](../../projects/m13-kinneret-plastics.md) **before** you open the expert's set, then compare. Open the hidden truth only after your readout is written.

<details><summary>What was really going on at Kinneret</summary>

The stated ask was predictive maintenance. The real problem was that **stops lasted too long — above all mould stops at night — and nobody recorded what failed**, so nobody, human or model, could learn from the breakdowns.

- Half of the unplanned hours were moulds, not machines. A hot runner that failed at 01:00 waited for the toolmakers until 07:30; night mould stops lasted three and a half times longer than day ones. Moulds had no id in the maintenance system, and no sensor on a machine would ever see them.
- The failure history was not in the systems. Work orders were closed at the end of the shift, in the office, in Hebrew, by technicians who mostly think in Arabic or Russian; "fixed" was the commonest description. The real history was in Vladi's eleven notebooks and a WhatsApp group.
- The two plants used the same word for different events. Galil's "ready" was the technician handing back; Kinneret's was production restarted with approved parts. Galil was not faster. The slide that said so had been built by the operations-excellence team.
- The PM figure hid a decision. Six machines' summer PMs were deferred for Arava's programme and closed on paper on 30 September; those machines broke down twice as often in the autumn.
- Knowledge ran through one phone. Night technicians called a manager who plans to retire in 2028; those who read Hebrew and English slowly photographed manuals for a free chatbot, and one of its answers burnt a heater. The Arabic lockout procedure they used was four years older than the Hebrew one and lacked the accumulator step.
- A crane used for mould changes was three months past its statutory examination, with "valid" typed in the register.
- The trigger was Arava, not technology. Arava's two short-shot complaints were night restarts approved by a supervisor because there was no inspector at night. Amnon read "machine breakdown" in his own company's late notices and heard "predictive maintenance".
- The vendor's evidence came from wind turbines with six years of coded data; its own onboarding guide asked for records Kinneret did not have, and its discount depended on Kinneret becoming a reference site.

</details>

<details><summary>Six months later: three futures</summary>

**Future 1 — Buy the platform.** Amnon signed with Predictiva at the end of March to keep the conference price. Kits went onto 37 machines by July. The "learning period" turned out to mean that Kinneret labelled past failures and new alerts; nobody could. From September the platform raised 40 to 60 anomaly alerts a week; by October technicians had stopped opening them. The camera option was switched on at Plant G "for operator behaviour"; the works committee declared a labour dispute, citing clause 15, and the cameras were switched off after three weeks. Night mould stops and night waits did not change. Arava's OTIF was 82% in Q3, and Arava moved 20% of its 2027 volume to the second source. The 36-month commitment, about ₪1.03M for the core offer, stayed on the books.

**Future 2 — Not yet, the foundation funded, the assistant in shadow use (the path the expert recommended).** Management approved ₪730,000 in three stages. The protocol was signed on 30 March in Hebrew and Arabic. By September: one register for 40 machines, the auxiliaries and 231 moulds; 88% of breakdown work orders carried a failure mode, chosen at the machine, a third of them in Arabic or Russian; shot counters and a mould PM plan; a live parts view and the drive copy gone; sensors on eight machines; the assistant used on the night shift after shadow use (night calls to Vladi from about 1.8 to about 0.6 a week; one wrong clarify case fixed in the pack in May); Arabic and Russian lockout revision D issued in March; the crane examined in January. Arava's OTIF was 92% in Q3, from mould response, PMs and night QA cover, not from prediction. A senior technician co-owned the failure list from June. The January 2028 re-decision had its criteria and a proof-of-concept protocol; Predictiva was invited to run it at Plant G.

**Future 3 — Half-way.** Management approved the assistant and the parts view, which were cheap and visible, and Orit funded nothing else: "the rest is bureaucracy". Recording stayed optional, so it stayed at 15%. The assistant was liked and used. In August Vladi retired early after a health scare, and his notebooks went home with him. In January 2028 the re-decision met the same records as in 2027, and Predictiva came back with the same proposal and a new conference price.

**What decided which future happened:** whether the foundation was funded and owned as the deliverable — not as the thing you do after the exciting part — and whether the works committee agreed how the records would be used before anything changed on the floor.

</details>

Then open the expert's deliverables in the module download (`labs/module-13/expert/`, start with its [README](../../labs/module-13/expert/README.md)): the [charter and first week](../../labs/module-13/expert/01-charter-and-first-week.md), [findings memo](../../labs/module-13/expert/02-findings-memo.md), [baselines and case](../../labs/module-13/expert/03-baselines-and-case.md), [readiness verdict and foundation](../../labs/module-13/expert/04-readiness-verdict-and-foundation.md), [audit and eval report](../../labs/module-13/expert/05-audit-and-eval-report.md) and [steering readout](../../labs/module-13/expert/06-steering-readout.md). For each of your deliverables, write one thing the expert did that you did not, and one thing you did that you would keep.

## Watch out

- **A recommend-against with nothing to do instead.** If the owner leaves the room without a plan for Arava, he will sign the only plan on the table.
- **Correcting the owner in front of his team.** The same finding, delivered privately first and starting with his own question, is a different meeting.
- **A decision record without a re-decision date.** "Not now" with no date becomes "never" or "next month", depending on who asks.
- **Funding the visible half.** The assistant and the parts view are popular; the register and the recording are what any future AI needs. Future 3 funded only the first.
- **Handing over to yourself.** Name the business and technical owners and the date you stop; name the person who learns what Vladi knows.
- **Reading the hidden truth first.** The debrief is only worth something if your readout was written without it.

## Your turn

### Inputs

- Everything you wrote in 13.1–13.5; the pilot reports (module download, `labs/module-13/pilot/reports/`) and your audit report.
- Personas: [Amnon](../../labs/module-13/personas/amnon-ceo.md) (rehearsal), and for the meeting [Dalia](../../labs/module-13/personas/dalia-vp-operations.md), [Orit](../../labs/module-13/personas/orit-cfo.md), [Eli](../../labs/module-13/personas/eli-plant-g-manager.md), [Vladi](../../labs/module-13/personas/vladimir-maintenance-manager.md), [Khalil](../../labs/module-13/personas/khalil-works-committee.md); [Amnon's transcript](../../labs/module-13/personas/transcripts/amnon-ceo.md) as the no-roleplay path; [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [steering pack](../../templates/steering-pack.md), [integration check](../../templates/integration-check.md), [decision record](../../templates/decision-record.md), [handover pack](../../templates/handover-pack.md), [deliverable map](../../templates/deliverable-map.md).
- The [module project](../../projects/m13-kinneret-plastics.md) rubric.

### Steps

1. Write the readout's front page: one recommendation in parts with owners and dates, the recommend-against with evidence, what a "no" means, and what goes to Arava.
2. Run the integration check; fix or flag at least three contradictions.
3. Rehearse the hardest finding with Amnon (roleplay twice, coach after each), or annotate his transcript with what you would change.
4. Run the meeting (group roleplay) or write the 60-minute plan with an answer to each of the seven concerns.
5. Write the decision record (with the January 2028 criteria) and the handover outline.
6. Score yourself with the rubric; then open the hidden truth and the futures; then compare with the expert set.

### Time

180 minutes: 40 for the readout, 25 for the integration check, 30 for the rehearsal, 30 for the meeting, 25 for the record and handover, 30 for the debrief.

### Done when

- [ ] The front page has one recommendation, a recommend-against with measured evidence, and what the owner can tell Arava.
- [ ] The integration check found and resolved (or flagged) at least three contradictions.
- [ ] The hardest finding was delivered privately first, starting from the owner's own question, and the second rehearsal was better than the first by the coach's account.
- [ ] The decision record names owners, the stop rule, the re-decision date with its criteria, and any dissent.
- [ ] The handover names a business owner, technical owners, the successor to the maintenance manager's knowledge, and the date you stop.
- [ ] You scored yourself before reading the expert set, and wrote one difference per deliverable.

<details><summary>Reference answer</summary>

The full set is `labs/module-13/expert/06-steering-readout.md` (module download). The parts that carry the weight:

**Front page, one sentence:** Kinneret loses deliveries because stops last too long — half of the lost hours are moulds, mostly at night — and because nobody records what failed; so we fix the night response for Arava now, build the records any AI needs this year, give the night technicians a tested assistant in their language, and decide on predictive maintenance in January 2028 on our own data.

**Recommend-against:** no Predictiva contract or letter of intent in 2027, no cameras (73 usable labels of 861, none of 30 per mode; machine faults 24% of lost hours, moulds outside the platform; ≈ ₪257k a year at best against ≈ ₪343k a year).

**Integration check, three contradictions fixed:** Plant G recording "by 30 April" against the protocol's joint-committee meeting on 6 April (fixed to 30 June everywhere); "₪14,000 a year saved" from night calls in a draft (removed: capacity, and not the reason); assistant logs "anonymous" while the admin console stores logins (changed to "stored without user id after export, 90 days" and a settings request to IT before shadow use).

**Rehearsal with Amnon (21 March):** the first attempt opened with the data-quality table; he heard "your factory is a mess" and said he would ask Gilad to "just start at Galil". The second opened with "Arava back to 95%", then the night mould hours and the short-shot story, then what would make Predictiva worth buying in 2028. He asked "so what do I tell Gilad?" — the moment he owned it.

**Decision record (23 March):** Arava items approved, sent to Arava on 30 March; foundation ₪730,000 in three stages, stop rule on 30 June; assistant in shadow from 4 April, review 6 May; protocol signed by 31 March; Predictiva declined for 2027, proof-of-concept protocol by October, re-decision January 2028; one MTTR definition in the April deck. Dissent, in Eli's words: "Galil could have started in April and been the first. We will be ready in January." Recorded; Plant G is the first proof-of-concept site if its records meet the bar.

**Handover:** business owner Dalia Mizrahi; technical owners Vladimir Kaplan, Boaz Tal, Yaakov Dahan; a senior technician co-owns the failure list and pack from June; Lina Haddad re-runs `readiness_audit.py` and `discovery.py` monthly; you stop owning the assistant on 30 June and the foundation on 31 December.

**Which future this readout leads to:** future 2, *because* the foundation was funded and owned, and the protocol came before the floor changed. Fund only the assistant and it is future 3.

</details>

## References

- Histadrut, [AIG Israel workers' committee declare labour dispute over AI](https://global.histadrut.org.il/news/aig-israel-workers-committee-declare-labour-dispute-over-ai/) (13 August 2026): what moving on AI without the committee looks like. A union source.
- [Organisation of Labour Supervision (Safety Management Programme) Regulations, 5773-2013](https://he.wikisource.org/wiki/תקנות_ארגון_הפיקוח_על_העבודה_(תכנית_לניהול_הבטיחות)), reg. 5(6) and 5(10): the lists the register and the pack now hold.
- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting): decision-ready case, bad news upward, recommending against (named, not re-taught).
- Field kit: [07.1 · The steering pack](../module-07/lesson-01.md), [07.2 · Scale, fix or stop](../module-07/lesson-02.md), [07.3 · Delivering bad news upward](../module-07/lesson-03.md), [07.4 · The steering meeting](../module-07/lesson-04.md), [07.9 · Handover](../module-07/lesson-09.md).
- Templates: [steering pack](../../templates/steering-pack.md), [integration check](../../templates/integration-check.md), [decision record](../../templates/decision-record.md), [handover pack](../../templates/handover-pack.md), [deliverable map](../../templates/deliverable-map.md).
- Expert deliverables: [README](../../labs/module-13/expert/README.md) (module download). Project: [Kinneret Plastics](../../projects/m13-kinneret-plastics.md).
- Earlier: [13.5 · Build: the readiness audit and a manual assistant](lesson-05.md).
