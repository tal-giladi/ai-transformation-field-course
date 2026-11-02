---
id: "10.6"
module: 10
minutes: 22
practice_minutes: 180
prerequisites: ["10.5", "07.1", "07.3", "07.4", "07.9"]
objectives:
  - "Write a steering pack with one recommendation, a recommend-against on its front page, and a decision asked in words that can be minuted."
  - "Run an integration check that traces every date to its dependency and every control to its cost."
  - "Rehearse the hardest finding privately with the CEO who announced the opposite, and change the delivery, not the finding."
  - "Compare your engagement with the expert's and with three futures, and score it with the rubric."
volatility: concept
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): the decision-ready case, recommending against, executive communication"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "Ministry of Health, director-general's circular 2/2021, 'Use of cloud computing in the health system' (reporting and documentation duties)"
    url: https://www.gov.il/BlobFolder/policy/mk02-2021/he/files_circulars_mk_mk02_2021.pdf
last_verified: "2026-11-02"
---

# 10.6 · Readout and debrief

The last week. You have the findings, the PoC, the scores, the contract terms and the pilot plan. On Tuesday 19 January 2027 the steering committee decides, and on Thursday you hand over and leave. In this lesson you write the steering pack, check that it holds together, rehearse the hardest finding with the CEO in private, run the meeting, and record the decision and the handover. Then you see what Galil was really dealing with, what happened a year later on three different paths, and how an expert ran the same engagement. At the end you have the readout pack, a decision record, a handover and your rubric score.

## The situation

Thursday 14 January 2027: the pre-read goes out. Sunday 17 January: thirty minutes with Shlomit, alone. Tuesday 19 January, 09:00–10:00: the steering committee (Shlomit in the chair, Igor, Wasim, Eyal, Hagit, Suha). Thursday 21 January: handover to Igor and Wasim and the end of your contract. The board meets at the end of January and expects the CEO's update on "the scribe for every doctor by Q2".

This is module 7's method compressed into a week: the [steering pack](../module-07/lesson-01.md), [delivering bad news upward](../module-07/lesson-03.md), [the meeting](../module-07/lesson-04.md) and [handover](../module-07/lesson-09.md). IBM's consulting certificate rewards recommending against when the evidence says so; here the recommend-against is aimed at the vendor the CEO told the board about.

## What to do

### Step 1 — One recommendation, and the recommend-against on the front page

Use the [steering pack](../../templates/steering-pack.md). One sentence first:

> Choose the scribe that passed Galil's own test in Hebrew, Arabic and Russian (Rishma, hosted in Israel), start with twelve doctors in Nazareth and Karmiel in March once Fund A approves, and roll out region by region only if the pilot passes on 6 May.

Then the decision asked, in words that can be minuted: Rishma named preferred vendor subject to counsel's and the DPO's review, Fund A's approval, the cloud committee and the staff committee's consultation; the pilot from 14 March with the stop rules; the gate on 6 May; the instruction on personal-device recording from 1 February; nurses' documentation evaluated separately in the second half of 2027.

And the recommend-against, plainly, with its evidence: **against signing any vendor for 120 seats before Fund A approves, and against ScribeWave on the quoted Standard plan.** Word error 27% in Arabic; 11.7 omissions per 100 notes in Arabic and 9.3 with a relative in the room; a plan that lets the vendor train on de-identified recordings; audio kept 90 days in the EU or the US; no notice of model changes. Also against MedNote's free year: correcting its notes took longer (6.0 minutes) than writing a note today (4.8), and year two has no price.

Every page says what a "no" means: doctors keep recording on consumer apps; 112 documentation minutes a doctor-day stay; the board hears "no vendor yet".

### Step 2 — Check that it holds together

Run the [integration check](../../templates/integration-check.md) across everything you wrote since November. For each date: what it depends on. For each control: who does it and in whose hours. The questions that catch real contradictions at Galil:

- Does any document still say the pilot starts "on 1 March", when Fund A's 45 days from 20 January end on 6 March?
- Does the capacity line (about 600 doctor-hours a month, ≈ ₪198,000 at ₪330 an hour) appear anywhere as savings?
- Is the weekly audit (10 notes per doctor, about 8 reviewer-hours a week) in anyone's hours and budget, or only in the pilot plan?
- Do the consent text, the contract and the privacy notice say the same thing about deletion and location?
- Is the staff committee's consultation at least 30 days before the pilot?
- Is every PoC number in the pack the same as in `poc/review-sheet.csv`?

### Step 3 — Rehearse the hardest finding with the CEO, in private

The hardest finding is for Shlomit: *the vendor she presented to the board failed Galil's own test in the language of 38% of its patients, the plan she was quoted would let it train on Galil's recordings and keep them abroad, and the 31 December date could never have been met without Fund A's approval.* If you found it in 10.3, there is a fourth part: she told Fund A's regional director the recordings would stay in Israel.

Deliver it before the room ([07.3](../module-07/lesson-03.md)):

- **Start with her goal, not your finding.** Doctors home at six; two posts filled by the summer.
- **Galil's facts before the vendor's.** The 112 minutes, where they sit (mixed-language clinics), the language field that hid it.
- **The PoC in one line, the funds as a date.** Not "you were misled", but "Fund A's 45 days set our start date".
- **Give her the sentence for the board.** *"We chose on evidence from our own clinics in Hebrew, Arabic and Russian; the vendor that looked best in the demo failed that test; twelve doctors start in March, and the rest follow region by region if the pilot passes in May."*

Roleplay it: paste the [Shlomit Avraham persona](../../labs/module-10/personas/shlomit-ceo.md) into a new chat, say you are meeting her on Sunday 17 January, and deliver the finding. Run the transcript through the [coach prompt](../../labs/common/coach-prompt.md) with this lesson's "Done when" list. Run it twice; change the delivery, never the finding.

### Step 4 — Run the meeting

Plan the 60 minutes ([07.4](../module-07/lesson-04.md)): 5 for the decision asked, 15 for the evidence, 25 for questions, 15 to get the decision minuted. Prepare one answer for each concern you know is coming: Shlomit ("so what do I tell the board?"), Igor ("the Notara interface estimate is theirs, not tested"), Wasim ("who audits the notes, and when do I stop it?"), Eyal ("what does it cost in year two, and where is the cash?"), Hagit ("nothing moves before Fund A and the cloud committee"), Suha ("what about the nurses in the room?").

For a group roleplay, paste the six persona files ([Shlomit](../../labs/module-10/personas/shlomit-ceo.md), [Igor](../../labs/module-10/personas/igor-cio.md), [Wasim](../../labs/module-10/personas/wasim-cmo.md), [Eyal](../../labs/module-10/personas/eyal-cfo.md), [Hagit](../../labs/module-10/personas/hagit-counsel-dpo.md), [Suha](../../labs/module-10/personas/suha-head-of-nursing.md)) into one chat with the instruction "play all six in a steering meeting chaired by Shlomit; each speaks only from their own prompt". End by asking for the decision in words that can be minuted.

### Step 5 — Record the decision and hand over

The [decision record](../../templates/decision-record.md): what was decided, by whom, owners, conditions, stop rules, the next decision date (6 May), and any dissent in the dissenter's own words. Then the [handover pack](../../templates/handover-pack.md) to Igor (owner) and Wasim (clinical owner): the deliverable map, the RFP and answers, the read-backs, the PoC protocol and results with `poc_score.py`, the scoring sheet, the contract terms, the pilot plan, the documentation-time measure (`discovery.py`) that the gate depends on, and the open questions for counsel. One more item belongs in the list: under the cloud circular, the new cloud use is reported to the Ministry's information-security officer within 30 days of signing, and the approval process is documented and kept. Name who does it. Test the handover: someone at Galil re-runs the baseline and the PoC table without you.

### Step 6 — The debrief

Score your deliverables with the rubric in the [module project](../../projects/m10-galil-health.md) **before** you open the expert's set, then compare. Open the hidden truth only after your readout is written.

<details><summary>What was really going on at Galil Health</summary>

The stated ask was a scribe for every doctor by Q2. The scribe was a good idea; the way it was about to be bought was not.

- **The demo ranking was upside down.** The steering group's demo-day scores put ScribeWave and Kol Refua first (3.62) and Rishma last (2.92). Each leader's headline number had been measured under conditions Galil doesn't have: scripted English visits in a studio with one speaker (ScribeWave), forty Hebrew visits in an investor's clinic (Kol Refua), dictation rather than conversation (MedNote). On Galil's own synthetic visits the order reversed: Rishma 3.92, ScribeWave and MedNote 2.31, Kol Refua 2.00.
- **The burden sat in the languages, and the KPI hid it.** Notara defaulted the visit language to Hebrew, so the KPI showed 77% Hebrew visits; patients' preferred languages were 38% Arabic, 30% Hebrew, 28% Russian. Visits where the doctor didn't speak the patient's language took 43% longer to document and were far more often finished at night, with relatives or nurses interpreting. A scribe that worked in Hebrew would have helped the doctors who needed it least.
- **The deadline was never real.** Fund A's agreement required its written approval, with 45 days to answer, before any outside party processed its members' medical information, and processing in Israel unless it agreed otherwise; the cloud committee required by the Ministry's circular had met once, in 2022; the patient privacy notice promised data stayed in Israel. And the reseller would hold its price to 31 March for anyone who asked.
- **AI scribing was already happening.** About a dozen doctors recorded visits on consumer apps on their own phones, over the guest Wi-Fi, and pasted summaries into Notara; one had already dropped an allergy. Doing nothing was not the safe option.
- **Galil had tried before.** A 2025 dictation trial faded from nine doctors to two in seven weeks and produced two near misses, both about what a relative said. Nobody wrote it up.
- **The money was retention, not minutes.** On capitation, freed time is capacity. The cash was in nine vacancies and ₪2.1M of locums, and in doctors who left because of notes in the evenings.

</details>

<details><summary>Twelve months later: three futures</summary>

**Future 1 — Sign ScribeWave by 31 December (the CEO's path).** Galil signed for all 120 seats to keep the discount, on the Standard plan, and filed Fund A's approval request afterwards. Hebrew notes were fine. Arabic-speaking doctors stopped using it in month three; Russian-speaking doctors kept it. The data-location question was still open with the DPO a year later, and Fund A asked Galil to suspend use for its members until it had reviewed the terms. The measured saving was about 25 minutes a day for the doctors who kept using it, not two hours. Several doctors kept their phone apps for the Arabic visits.

**Future 2 — MedNote, "free in year one" (the comfortable path).** No integration project, notes straight into Notara where it was current; the two Notara 7.4 regions waited for an upgrade nobody had budgeted. Doctors spent longer fixing conversation notes than they spent writing their own; use fell to a few enthusiasts by the spring. Year-two pricing arrived with the Notara renewal at ₪900 a clinician a month.

**Future 3 — Evidence, then a pilot (the path the expert recommended).** Fund A approved in early March; the cloud committee met for the first time in four years; the privacy notice was rewritten in four languages. The six-week pilot in Nazareth and Karmiel passed its gate in May, and Galil rolled Rishma out region by region. Arabic-speaking clinics adopted fastest. The Notara integration took four months, not three. Measured note time fell by about 35 minutes a day per doctor. The phone apps disappeared once doctors had a sanctioned tool, and two of the nine posts were filled by the autumn, one by a doctor who said the scribe was why she chose Galil.

**What decided which future happened:** whether anyone asked how the demo numbers were measured before the discount deadline, and whether that deadline was tested against the health funds' contracts before anyone signed.

</details>

Then open the expert's deliverables in the module download (`labs/module-10/expert/`, start with its [README](../../labs/module-10/expert/README.md)): the [charter](../../labs/module-10/expert/01-engagement-charter.md), [findings memo](../../labs/module-10/expert/02-findings-memo.md), [baselines and case](../../labs/module-10/expert/03-baselines-and-case.md), [RFP, claims and PoC](../../labs/module-10/expert/04-rfp-claims-and-poc.md), [vendor decision and pilot plan](../../labs/module-10/expert/05-vendor-decision-and-pilot-plan.md) and [steering readout](../../labs/module-10/expert/06-steering-readout.md). For each of your deliverables, write one thing the expert did that you did not, and one thing you did that you would keep.

## Watch out

- **A menu instead of a recommendation.** Four vendors with pros and cons hands the decision back to the person who liked the demo.
- **The recommend-against in an annex.** If ScribeWave's results are not on the front page, the room will not discuss them, and the discount will.
- **Correcting the CEO in the room.** The same facts delivered first in private, starting with her goal, are a different meeting.
- **"Approved, subject to approvals."** A decision record whose conditions have no owners and dates becomes future 1 by default when someone gets impatient.
- **A pilot with no gate date.** Without 6 May on the record, a pilot drifts into a rollout.
- **Leaving with the knowledge.** If Igor cannot re-run the baseline and the PoC scoring without you, the gate in May measures nothing.

## Your turn

### Inputs

- Everything you wrote in 10.1–10.5; the PoC files (module download, `labs/module-10/poc/`).
- Personas: [Shlomit](../../labs/module-10/personas/shlomit-ceo.md) (rehearsal), and for the meeting [Igor](../../labs/module-10/personas/igor-cio.md), [Wasim](../../labs/module-10/personas/wasim-cmo.md), [Eyal](../../labs/module-10/personas/eyal-cfo.md), [Hagit](../../labs/module-10/personas/hagit-counsel-dpo.md), [Suha](../../labs/module-10/personas/suha-head-of-nursing.md); [Shlomit's transcript](../../labs/module-10/personas/transcripts/shlomit-ceo.md) as the no-roleplay path; [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [steering pack](../../templates/steering-pack.md), [integration check](../../templates/integration-check.md), [decision record](../../templates/decision-record.md), [handover pack](../../templates/handover-pack.md), [deliverable map](../../templates/deliverable-map.md).
- The [module project](../../projects/m10-galil-health.md) rubric.

### Steps

1. Write the steering pack's front page: one sentence, the decision asked, the recommend-against with evidence, what a "no" means, the 2027 cost.
2. Run the integration check across your deliverables; fix or flag at least three contradictions.
3. Rehearse the hardest finding with Shlomit (roleplay twice, coach after each) or annotate her transcript with what you would change.
4. Run the meeting (group roleplay) or write the 60-minute plan with an answer to each of the six concerns.
5. Write the decision record and the handover pack outline, including the Ministry report after signing.
6. Score yourself with the rubric; then open the hidden truth and the futures; then compare with the expert set.

### Time

180 minutes: 40 for the pack, 25 for the integration check, 30 for the rehearsal, 30 for the meeting, 25 for the record and handover, 30 for the debrief.

### Done when

- [ ] The pack has one recommendation, a recommend-against on its front page with the PoC evidence, and a decision asked in minutable words.
- [ ] The integration check found and resolved (or flagged) at least three contradictions, including the pilot's start date against Fund A's approval.
- [ ] The hardest finding was delivered privately first, starting from the CEO's goal, and she has a sentence for the board.
- [ ] The decision record has owners and dates for every condition, the stop rules, the gate date and any dissent.
- [ ] The handover names an owner who can re-run the baseline and the PoC scoring without you.
- [ ] You scored yourself before reading the expert set, and wrote one difference per deliverable.

<details><summary>Reference answer</summary>

The full set is `labs/module-10/expert/06-steering-readout.md`. The parts that carry the weight:

**Front page, one sentence:** Choose the scribe that passed Galil's own test in Hebrew, Arabic and Russian (Rishma, hosted in Israel), start with twelve doctors in Nazareth and Karmiel in March once Fund A approves, and roll out region by region only if the pilot passes on 6 May.

**Recommend-against:** signing any vendor for 120 seats before Fund A approves, and ScribeWave on the Standard plan (Arabic word error 27%; 11.7 omissions per 100 notes in Arabic, 9.3 with relatives; training on de-identified recordings; 90-day audio in the EU or the US; no model-change notice); MedNote's free year (6.0 minutes to correct vs 4.8 to write; year two unpriced).

**Integration check, three contradictions found:** the pilot's first draft started on 1 March, before Fund A's answer (fixed: 14 March); the capacity line appeared in a draft board sentence as "₪2.4M saved a year" (removed: capacity, not cash); the weekly audit had no hours (₪22,000 of clinician time added to the pilot budget and to Wasim's team plan).

**Rehearsal with Shlomit (17 January):** the first attempt opened with the PoC table and she defended the demo for ten minutes; the second opened with her goal, then the 112 minutes and where they sit, then the PoC in a line, then Fund A as a date. She asked "so what do I tell the board?" and took the sentence; she asked to keep ScribeWave's extended offer as a fallback to 31 March.

**Decision record (19 January):** Rishma preferred, subject to four conditions with owners and dates (Hagit: contract by 3 Feb, Fund A requested 20 Jan; Igor: cloud committee 27 Jan, Ministry report after signing; Suha with HR: staff committee by 10 Feb); pilot 14 Mar – 20 Apr with Wasim's stop rules; personal-device instruction from 1 Feb; nurses deferred to H2; gate 6 May. Dissent: Shlomit, "Keep ScribeWave's March price on the table in case the funds are slow"; Igor, "The Notara interface estimate is Notara's word, not tested", recorded as a risk with an owner.

**Handover (21 January):** owner Igor, clinical owner Wasim; Igor's analyst re-ran `discovery.py` and `poc_score.py` and reproduced the baseline and the PoC table; one follow-up call on 29 April, before the gate.

**Which future this readout leads to:** future 3, *because* the deadline was tested against the funds' contracts before anyone signed, and the CEO had a sentence for the board that did not depend on the demo.

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting): the decision-ready case, recommending against, executive communication (named, not re-taught).
- Ministry of Health, [circular 2/2021 on cloud computing](https://www.gov.il/BlobFolder/policy/mk02-2021/he/files_circulars_mk_mk02_2021.pdf): reporting a new cloud use within 30 days of signing and keeping the approval records (sections 8.1–8.2). Check for a later version.
- Field kit: [07.1 · The steering pack](../module-07/lesson-01.md), [07.3 · Delivering bad news upward](../module-07/lesson-03.md), [07.4 · The steering meeting](../module-07/lesson-04.md), [07.9 · Handover](../module-07/lesson-09.md).
- Templates: [steering pack](../../templates/steering-pack.md), [integration check](../../templates/integration-check.md), [decision record](../../templates/decision-record.md), [handover pack](../../templates/handover-pack.md), [deliverable map](../../templates/deliverable-map.md).
- Simulation: [Vendor RFP](../../simulations/vendor-rfp/index.html?preset=galil) (its debrief shows the same futures per vendor).
- Expert deliverables: [README](../../labs/module-10/expert/README.md) (module download). Project: [Galil Health](../../projects/m10-galil-health.md).
- Earlier: [10.5 · Decide: scoring, contract terms and the clinician pilot](lesson-05.md).
