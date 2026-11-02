---
id: "10.3"
module: 10
minutes: 18
practice_minutes: 150
prerequisites: ["10.2", "03.1", "03.2", "03.3", "03.7", "03.9"]
objectives:
  - "Build a baseline sheet in which every number has a definition, a source and a label, including the ones the vendors quote."
  - "Map the candidates around a stated ask, including the plain fixes that need no AI, and turn the evidence into requirements a vendor must meet."
  - "Net a vendor's time-saving claim the way the CFO will: against the measured baseline, capacity apart from cash, and the cost of the expensive error."
  - "Write a one-page case that asks for one decision, costs it, and says what a no means and what it does not promise."
volatility: implementation
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): screening, net the claim, capacity vs cash, the decision-ready case"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "Patient's Rights Law, 5756-1996 (Hebrew Wikisource): section 17, the medical record"
    url: https://he.wikisource.org/wiki/חוק_זכויות_החולה
last_verified: "2026-11-02"
---

# 10.3 · Diagnosis

Your memo says the burden is real, sits in the languages, and some doctors already record visits on their phones. The CEO still holds a quote that expires on 31 December. Before the 3 December readout you have to turn the findings into requirements a vendor must meet, a case the CFO can accept, and one decision the CEO can take. In this lesson you build the baseline sheet, map the candidates (including two plain fixes that need no AI), net the "two hours a day" claim, and write the one-page case. At the end you have the readout's front page.

## The situation

Monday 30 November to Thursday 3 December 2026. The findings memo is drafted (10.2) and Wasim, Suha and Igor have read their parts. On Monday you see Eyal Dahan, the CFO (read [his transcript](../../labs/module-10/personas/transcripts/eyal-cfo.md) or interview [Eyal](../../labs/module-10/personas/eyal-cfo.md)). His rules: Galil is paid per registered patient, so time freed is capacity, not money, unless it fills a vacancy without a locum, avoids overtime or adds sessions the funds pay for; payback under two years if you claim money; the board approves anything above ₪300,000 over a project's life. On Tuesday you have the 20 minutes with Shlomit you asked for ([persona](../../labs/module-10/personas/shlomit-ceo.md); [transcript](../../labs/module-10/personas/transcripts/shlomit-ceo.md)).

This is module 3's method on a case where the solution was chosen before the problem: the [opportunity map](../module-03/lesson-01.md), [agent or not](../module-03/lesson-02.md), the [fast screen](../module-03/lesson-03.md), the [ROI model](../module-03/lesson-07.md) and the [decision-ready case](../module-03/lesson-09.md). IBM's consulting certificate calls the core move *net the claim*, and separates capacity from cash; here the claim to net is the vendor's, repeated by the CEO to the board.

## What to do

### Step 1 — The baseline sheet

Every row: value, definition, source, label. These are the numbers the rest of the engagement is measured against, so write them once and quote them the same way everywhere.

| Measure | Value | Label |
|---|---|---|
| Doctor visits a month | ≈ 26,000 (Sep 24,610 with holidays; Oct 27,315) | measured |
| Active note time per visit | median 4.2 min, mean 4.8 | measured |
| Documentation per doctor-day | median 112 min (p75 136) | measured (estimate) |
| After hours per doctor-day | median 10 min, mean 12 | measured |
| Mismatch visits | 27.8% (note +43%, after-hours work 33% vs 13%) | measured |
| Patients' preferred language | Arabic 38%, Hebrew 30%, Russian 28%, other 3% | measured |
| Nurse interpreting | ≈ 8% of doctor visits; 42 min a day per nurse | measured; reported |
| Locums; vacancies; leavers | ₪2.1M (2025); 9 posts; 6 in a year, 4 citing workload | reported by finance and HR |
| Vendor claim: "saves 2 hours a day" | 120 min | vendor (survey of 60 US early adopters) |

The last row is on the sheet on purpose. A claim you will be asked about belongs beside the measure it has to beat.

### Step 2 — Map the candidates, not just the ask

Three feeds ([03.1](../module-03/lesson-01.md)): the stated ask, what the data says, what people asked for. Then decide, per candidate, what kind of solution it is ([03.2](../module-03/lesson-02.md)):

| Candidate | Feed | Kind | Fast screen |
|---|---|---|---|
| A. Ambient scribe for doctors' visits | The ask; the data | Generation (a draft note); a doctor checks and signs | **Go with a condition**: no real audio to test on, so a proof of concept on synthetic visits first |
| B. Scribe for nurses' visits | The quote (120 seats) | Generation | **Stop for now**: nobody measured nurses' need; Suha says the gain is indirect |
| C. Make Notara's visit-language field required, or fill it from the appointment system | The data (10.2, F1) | **Plain configuration, no AI** | Go: a Notara setting; Igor |
| D. Book patients with a doctor who speaks their language where the clinic can | The data (mismatch) | **Plain scheduling, no AI** | Go with a condition: clinic managers can only do it where doctors' lists allow |
| E. Stop recording on personal devices; amnesty; a date for an approved tool | The census | **Policy, no AI** | Go: the CMO and counsel decide the wording |
| F. Draft referral letters (17% of visits have one) | A survey comment | Generation | Later: after A is proven |

C, D and E cost almost nothing and do not need a vendor. Put them in the case. C fixes the KPI that misled everyone; D attacks the cause of the costliest notes. Directionally: mismatch visits cost about 1.7 extra minutes of note time each; at ≈ 7,200 mismatch visits a month, moving a third of them to a doctor who speaks the patient's language would save about 70 doctor-hours a month (assumed: the third is a guess to test with clinic managers). It will not replace a scribe; it is what a good consultant notices before spending ₪1M a year.

### Step 3 — Turn the evidence into requirements

The RFP in 10.4 needs requirements a vendor can fail. Write them from Galil's findings, not from the demos:

1. Draft a Hebrew note from a conversation in Hebrew, Galilee Arabic or Russian, with relatives talking (F1, F3).
2. Capture what relatives say about medicines and allergies, and show the doctor where the tool was unsure (the 2025 near misses, IN-2026-052, Fatma's story).
3. Never invent a finding or a dose; the doctor confirms before signing. The note is the medical record the doctor is responsible for (Patient's Rights Law, section 17).
4. Work with Notara 9.2 and 7.4, or state the cost of not doing so.
5. Keep audio and notes where counsel, the DPO and the health funds allow; no training on Galil's data.
6. Prove 1–3 on Galil's own synthetic visits before any contract.

### Step 4 — Net the claim the way the CFO will

The CEO told the board "two hours a day". Net it in four moves:

1. **Against the baseline.** Galil measures 112 minutes of documentation a doctor-day in total. A tool cannot save 120 of them. Rishma's independent evaluation found −52 minutes a clinician-day elsewhere (range 40–70). For planning, use **30 minutes a doctor-day**, labelled *assumed* until the pilot measures it.
2. **Capacity, not cash.** 30 minutes × ≈ 1,200 doctor-days a month ≈ 600 doctor-hours a month, about 3.8 full-time doctors' hours. At ₪330 an hour that is ≈ ₪198,000 a month *of capacity*. Galil is paid per registered patient; nobody's salary changes. It is not a saving.
3. **Where cash could come from.** A post filled or kept without a locum saves about ₪300,000 a year (Eyal). A scribe for 78 doctors at ≈ ₪1.3M a year pays for itself in cash only if it keeps or fills about four to five posts a year. That is a real possibility (four of six leavers cited workload) and an *assumption*. Put it on the front page; Eyal will respect you for it.
4. **The expensive error.** An omitted allergy or a medicine change in a signed note. Galil has two near misses from the 2025 trial and one from a phone app this September. The proof of concept measures how often each vendor drops a relevant fact; the pilot audits it in real notes.

### Step 5 — Lay the options side by side

| | A. Sign ScribeWave now (120 seats, by 31 Dec) | B. RFP and proof of concept, then a pilot | C. Do nothing now |
|---|---|---|---|
| Evidence in Galil's conditions | None | 90 synthetic visits in 3 languages by 31 Dec | None |
| Arabic and Russian | Unknown: Hebrew beta, Arabic "Gulf" | Tested | — |
| Data terms | Standard plan: vendor may train on de-identified recordings; 90-day audio; EU or US | Must-have terms in the RFP | — |
| Health funds, cloud committee | Signature before approvals (counsel to confirm the exposure) | Built into the timeline | — |
| Shadow recording | Continues | Instruction now; sanctioned tool from the pilot | Continues |
| Cost now | ₪1,457,280 a year (≈ ₪1.72M on the Enterprise plan that excludes training) | ≤ ₪75,000 | ₪0 |
| What it gives up | — | The 12% discount, unless the reseller extends it | The goal |

### Step 6 — Write the one-page case, and see the CEO first

The [decision-ready case](../../templates/decision-ready-case.md) shape from [03.9](../module-03/lesson-09.md): one decision asked, its cost, what a "no" means, what it does not promise. In the private meeting, start from her goal, not from the demo: in the transcript, Shlomit's goal for July is "doctors go home at six, nobody else resigns because of notes". Then show the language finding, then ask which plan the quote is for. Give her a sentence for the board before she asks for one.

## Watch out

- **Netting only the vendor's claim.** Your own numbers need the same treatment: the 30 minutes is assumed, the retention effect is assumed, and the PoC will be small. Label them.
- **Capacity dressed as savings.** "₪2.4M a year freed" will be read as cash by the board and as dishonesty by the CFO.
- **Skipping the plain fixes.** A consultant who only evaluates the CEO's idea misses the language-field fix and the scheduling change that cost nothing.
- **Arguing with the demo.** "The demo was misleading" starts a fight the CEO must win. "The demo was in English; 38% of our patients prefer Arabic" is a fact she can use.
- **Letting the deadline frame the decision.** The discount is the reseller's deadline, not Galil's. Ask whether it can move before you treat it as a cost.

## Your turn

### Inputs

- Your findings memo (10.2) and the data room (module download): `company/finance-summary.md`, `company/kpi-report-2026-q3.md`, `vendors/scribewave-quote-2026-11.md`, `vendors/scribewave-dpa-extract.md`, `vendors/rishma-evaluation-summary.md`.
- Personas: [Eyal Dahan](../../labs/module-10/personas/eyal-cfo.md) and [Shlomit Avraham](../../labs/module-10/personas/shlomit-ceo.md), or their [transcripts](../../labs/module-10/personas/transcripts/); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [data profile](../../templates/data-profile.md), [opportunity map](../../templates/opportunity-map.md), [use-case scorecard](../../templates/use-case-scorecard.md), [ROI model](../../templates/roi-model.md), [decision-ready case](../../templates/decision-ready-case.md).

### Steps

1. Build the baseline sheet: at least eight rows, each with a definition, a source and a label, plus the vendor's claim beside the measure it must beat.
2. Map at least five candidates from three feeds; mark which are plain fixes with no AI; run the fast screen on each.
3. Write six requirements a vendor can fail, each traced to a finding.
4. Interview Eyal (or read the transcript); net "two hours a day" in four moves.
5. Write the options table.
6. Interview Shlomit (or read the transcript); write the one-page case with the decision asked, the cost, what a "no" means and the sentence for the board.

### Time

150 minutes: 25 for the baseline sheet, 25 for the map and screen, 15 for the requirements, 35 for Eyal and the netting, 20 for the options, 30 for Shlomit and the case.

### Done when

- [ ] Every number on the sheet has a definition, a source and a label; the vendor's "2 hours" sits beside the 112 minutes.
- [ ] At least two candidates are plain fixes with no AI, and the nurses' scribe is screened separately.
- [ ] The requirements include languages with relatives, unsure-marking, no invention, both Notara versions, data terms, and a PoC on Galil's visits.
- [ ] Capacity and cash are on separate lines; the retention condition for cash is stated as an assumption.
- [ ] The case asks for one decision, names the decline (no signature by 31 December), costs both, and says what a "no" means.

<details><summary>Reference answer</summary>

The full set is `labs/module-10/expert/03-baselines-and-case.md`. The front page:

**Decision asked (3 December).** Approve (1) an RFP to the four vendors on 6 December with Galil's conditions, locked criteria and must-have terms; (2) a proof of concept on 90 synthetic visits, ₪75,000 from the CIO's budget, results on 31 December; (3) a written request to the reseller to hold its price to 31 March 2027; (4) counsel to open the Fund A conversation now; (5) an interim instruction on recording visits with personal apps, with no discipline for past use. Also: the Notara language field made required (Igor) and language-matched booking tried in two mixed clinics (regional managers).

**Decline:** signing any vendor by 31 December.

**What a "no" means.** Galil signs on demo impressions: an English demo, a Standard plan under which the vendor may train on de-identified recordings, audio kept 90 days in the EU or the US, before the health funds have been asked, and with no evidence in Arabic, the preferred language of 38% of patients.

**Netting.** Measured documentation: 112 minutes a doctor-day; "2 hours saved" exceeds it. Planning assumption: 30 minutes a doctor-day ≈ 600 doctor-hours a month of capacity (≈ ₪198,000 a month at ₪330 an hour; capacity, not cash). Cash: only if the scribe keeps or fills four to five posts a year at ≈ ₪300,000 each (assumed).

**Cost.** ≤ ₪75,000 and four weeks; possibly the 12% discount (≈ ₪199,000 in year one) if the reseller does not extend it.

**Does not promise:** a vendor by 31 December, or two hours a day.

**Sentence for the board:** "We are choosing the scribe on evidence from our own clinics, in Hebrew, Arabic and Russian, and the first doctors will use it in the first quarter."

**What the transcripts missed:** Eyal's note that Notara announced a 9% increase from July 2027 (which will pay for MedNote's "free" year); Shlomit's promise to Fund A's regional director that recordings would stay in Israel.

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting): screening, net the claim, capacity vs cash, the decision-ready case (named, not re-taught).
- [Patient's Rights Law, 5756-1996](https://he.wikisource.org/wiki/חוק_זכויות_החולה), section 17: the record the doctor is responsible for, whoever drafted it.
- Field kit: [03.1 · Opportunity map](../module-03/lesson-01.md), [03.2 · Agent or not](../module-03/lesson-02.md), [03.3 · The fast screen](../module-03/lesson-03.md), [03.7 · The ROI model that survives finance](../module-03/lesson-07.md), [03.9 · The decision-ready case](../module-03/lesson-09.md).
- Templates: [data profile](../../templates/data-profile.md), [opportunity map](../../templates/opportunity-map.md), [use-case scorecard](../../templates/use-case-scorecard.md), [ROI model](../../templates/roi-model.md), [decision-ready case](../../templates/decision-ready-case.md).
- Earlier: [10.2 · Discovery](lesson-02.md). Next: [10.4 · The hard part: choosing on evidence](lesson-04.md).
