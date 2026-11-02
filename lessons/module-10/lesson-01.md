---
id: "10.1"
module: 10
minutes: 16
practice_minutes: 90
prerequisites: ["01.1", "01.2", "01.5", "08.1"]
objectives:
  - "Write decision rights for a clinical engagement: who decides clinical safety, patients' information, money and the vendor, and what the consultant decides."
  - "Read back the sponsor's objective, write the CEO's ask as the claim the engagement tests, and place exits in a statement of work."
  - "Run the first-day data-room read on Galil Health's files and sort its headline numbers into verified, contradicted, claim to test and unverifiable."
  - "Plan the first week so the clinicians, the counsel and the person with the ask are reached before the first readout."
volatility: implementation
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): the advisor role, framing and scoping, due diligence on claims and vendors"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "Patient's Rights Law, 5756-1996 (Hebrew Wikisource): section 2 definitions, section 17 medical record, section 19 confidentiality"
    url: https://he.wikisource.org/wiki/חוק_זכויות_החולה
  - title: "IAPP, Israel marks a new era in privacy law: Amendment 13 ushers in sweeping reform (in force 14 August 2025)"
    url: https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform
last_verified: "2026-11-02"
---

# 10.1 · The call

A regional clinic network wants "an ambient scribe for every doctor", and its CEO already likes one vendor. The CIO wants an outsider to run the selection properly before anyone signs. In this lesson you write the engagement charter with decision rights fit for a clinical setting, read the data room on day one, and plan the first week. At the end you have a charter ready to sign, a first-read sheet and a five-day plan.

## The situation

Sunday 15 November 2026, 08:30, Galil Health's management offices in Karmiel. Read the [engagement brief](../../labs/module-10/brief.md) first (in the module download). In short: Galil runs 14 community clinics in five regions of the north for about 112,000 patients, with 78 doctors and 42 nurses. On 21 October the CEO, Shlomit Avraham, told the board Galil would give "an ambient scribe to every doctor by Q2 2027". An ambient scribe listens to the visit and drafts the clinical note for the doctor to check. Four vendors demoed in two weeks; Shlomit loved ScribeWave, whose reseller offered 12% off 120 seats if signed by 31 December.

Igor Shapiro, the CIO, called you on 9 November: "I need someone from outside to run the selection properly and tell us which one, with evidence, before anyone signs." He signed your proposal on 12 November: three phases, ₪198,000 + VAT, 15 November to 21 January.

You have done this at Northwind ([08.1](../module-08/lesson-01.md)). Two things are new. The sponsor is the CIO, but the clinical decision belongs to the Chief Medical Officer and the decision about patients' information to the counsel and Privacy Protection Officer (DPO). And the work is a *selection*: if you pick the vendor, you have become a party. IBM's consulting certificate frames the advisor's job as due diligence on claims and vendors; here you set it up so Galil can select, and you can't be accused of selling.

## What to do

### Step 1 — Write the decision rights before anything else

At Northwind the question was "what does being outside change?" ([01.1](../module-01/lesson-01.md)). At Galil add a second question: **who decides what?** In a clinic, three decisions are not the sponsor's and certainly not yours:

| Decision | Who decides at Galil | Why it can't be yours or the CIO's |
|---|---|---|
| Is the tool clinically safe enough to pilot, and when to stop? | Dr. Wasim Haddad, CMO | A signed note is part of the medical record; the clinician is responsible for it (Patient's Rights Law, section 17) |
| May patients' audio and notes go to this vendor, there, on these terms? | Adv. Hagit Peretz, counsel and DPO, with external counsel where needed | Health information is especially sensitive under the Privacy Protection Law as amended by Amendment 13 (in force 14 August 2025); confidentiality binds Galil (section 19) |
| How much, and from which budget? | The CEO up to ₪300,000; the board above | Galil's approval rules (finance summary) |
| Which vendor? | The steering group, chaired by the CEO | The consultant designs the evidence and scores it; Galil selects |
| Integration with Notara | Igor, CIO | His systems and his team |

Write this table into the charter. It is what lets you say "that's Wasim's call" in a room where the CEO wants you to say "ScribeWave is fine". It also protects you from the most common failure of a selection consultant: being remembered as the person who chose the vendor that went wrong.

### Step 2 — Read back the objective and write the ask as a claim

The method is [01.2](../module-01/lesson-02.md), as at Northwind. Two objectives exist:

- **Igor's** (signed): "A recommendation, backed by evidence from Galil's own conditions, on which ambient-scribe vendor Galil should contract with, on what terms, and how it should be piloted with clinicians before any network-wide rollout."
- **Shlomit's** (board minute): "An ambient scribe for every doctor by Q2 2027."

Write Igor's as the objective and Shlomit's as the claim the engagement tests. Then make "done" checkable: a minuted decision of the steering group on 19 January; every piece of evidence labelled measured, reported or assumed; a proof of concept on Galil's own synthetic visits in Hebrew, Arabic and Russian, with thresholds agreed before the run; a named owner who accepts the handover.

"Synthetic" matters. You will not touch real patient audio in this engagement. The proof of concept uses visits written from real-shaped scenarios and recorded by actors. Put that in the charter now, so nobody suggests "just send them last week's recordings".

### Step 3 — Put exits and scope into the statement of work

Use the [engagement charter](../../templates/engagement-charter.md) template's SOW outline and the [scope boundary](../../templates/scope-boundary.md) from [01.3](../module-01/lesson-03.md). The brief gives two exits: the 3 December readout and the proof-of-concept results on 31 December. Make each real: what is delivered, who decides whether to continue. "Don't buy anything now" must be a permitted outcome, said out loud on day one.

The hard scope calls at Galil:

- **Nurses.** The quote has 120 seats; the ask says "every doctor". In: how nurses are affected. Out: deciding nurses' own documentation tool. That is a separate decision.
- **The Notara 7.4 upgrade.** Two regions run an old version some vendors don't support. In as a constraint and a cost; out as a decision (IT and finance).
- **Legal opinions and clinical decisions.** Out, routed to Hagit and Wasim by name.
- **Negotiation.** Out. You prepare terms; Galil negotiates. A consultant who negotiates with the CEO's preferred vendor has become a party.

### Step 4 — Read the data room on the first day

Follow [01.5](../module-01/lesson-05.md). Open the data room's [INDEX](../../labs/module-10/data-room/INDEX.md). Two facts shape how you read everything:

- The Notara export is an **8% random sample of doctor visits** from September and October 2026, with the note fields from Notara's audit log; `notara/doctor-days.csv` has the full visit count per doctor-day, so you can scale per visit to per day.
- The vendors' documents are **the vendors' own**. Every number in them has a footnote or none. Read the footnotes first.

Then sort the headline numbers. A worked example from Galil's files:

| Number or statement | Where | Sort | Why |
|---|---|---|---|
| "98% transcription accuracy" | ScribeWave deck slide 4; board minute | Claim to test | Footnote: 200 scripted English visits, studio microphone, one speaker, US accents |
| "Saves doctors 2 hours a day" | Deck slide 5; board minute | Claim to test | Footnote: survey of 60 early adopters, self-reported |
| "Doctors spend about 2 hours a day on notes" | Board minute; KPI footnote 2 | Unverifiable today | KPI: "documentation time per visit: not measured" |
| 77% of visits in Hebrew | KPI report | Claim to test | Footnote 1: "as recorded in Notara"; Galil's motto is "in your language" |
| Notes signed within 24 h: 98% | KPI report | Verified, for what it measures | It measures signing, not effort |
| "Your data never leaves Israel" | Kol Refua deck slide 5 | Contradicted | Its own DPA, Annex B: a US speech-recognition API |
| "Zero integration effort" | MedNote offer | Contradicted for two regions | `clinics.csv`: Upper Galilee and Kinneret on Notara 7.4; release notes: 7.x not supported |
| "Medical information stored in Israel" | Patient privacy notice (2023) | Verified, as a promise | Bears on any vendor hosting in the EU or US |

What is missing: any evaluation of a vendor by Galil, any measure of documentation time, the health-fund agreements in full, every vendor's full data-processing agreement, any report of earlier trials. Those go into the [access request pack](../../templates/access-request-pack.md).

### Step 5 — Plan the first week around clinicians, counsel and the CEO

Use the [30-60-90 plan](../../templates/30-60-90-plan.md) shortened to ten weeks, with a day-by-day first week. Igor has booked Wasim (Monday), Hagit (Tuesday), half a day in the Karmiel clinic with a family doctor (Wednesday) and the Head of Nursing (Thursday). Keep them; add two things:

- **A list, not a meeting room.** Half a day watching a real list teaches you more about documentation than any survey. Ask the patients' consent for your presence through the doctor.
- **The CEO before the first readout.** Her assistant offered 20 minutes "after the first readout". Ask for them before it; if you can't get them, write in the charter that the readout goes to her privately first.

### Step 6 — Agree it with the sponsor

Sit with Igor (roleplay: [Igor Shapiro](../../labs/module-10/personas/igor-cio.md); no-roleplay path: [the transcript](../../labs/module-10/personas/transcripts/igor-cio.md)). What you want: the objective read back, decision rights agreed, exits and change control agreed, and anything he knows about earlier attempts and about his own contract with Notara. Ask what he would choose if it were only his decision: a sponsor's private preference shapes a selection more than any criterion. Afterwards paste the transcript into the [coach prompt](../../labs/common/coach-prompt.md) with the persona's checklist.

## Watch out

- **Becoming the selector.** If your charter says "the consultant will select the vendor", the CEO will blame you for the outcome and the losing vendors will call you biased. Write: the consultant designs and scores, Galil selects.
- **Writing the CEO's ask as the objective.** Then the engagement can only succeed by delivering a scribe to every doctor by Q2. Write it as the claim you test.
- **Decision rights in your head only.** In the first hard meeting someone will ask you whether a vendor's terms are "legal" or a tool is "safe". The charter's table lets you name who decides, without looking evasive.
- **Real patient data "just for the test".** Synthetic visits only. Put it in writing before a vendor offers to "run last month's recordings".
- **Taking the sponsor's neutrality for granted.** Igor will integrate whatever is bought. He has a preference and a history. Ask.
- **Meeting the CEO last.** As at Northwind: a CEO who first hears that her vendor failed in a steering meeting will defend the vendor.

## Your turn

### Inputs

- [Engagement brief](../../labs/module-10/brief.md) and the [data room](../../labs/module-10/data-room/INDEX.md) (module download): especially `company/board-minutes-2026-10-21.md`, `company/kpi-report-2026-q3.md`, `company/clinics.csv`, `vendors/` (decks, quote, offer, DPAs), `legal/patient-privacy-notice-2023.md`, `vendors/rfp-draft-v0.md`.
- Persona: [Igor Shapiro](../../labs/module-10/personas/igor-cio.md) or [his transcript](../../labs/module-10/personas/transcripts/igor-cio.md); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [engagement charter](../../templates/engagement-charter.md), [scope boundary](../../templates/scope-boundary.md), [data-room first read](../../templates/data-room-first-read.md), [access request pack](../../templates/access-request-pack.md), [30-60-90 plan](../../templates/30-60-90-plan.md).

### Steps

1. Write the decision-rights table: clinical safety, patients' information, money, vendor, integration, and what you decide.
2. Interview Igor (or read the transcript and mark what the interviewer found and missed). Read the objective back; agree done, exits and change control.
3. Write the charter: objective, the stated ask as a claim, done, entry-role table, decision rights, scope, SOW with exits.
4. Do the first read: list every file, mark its provenance, and sort at least eight headline numbers with the evidence.
5. Write the access request for what is missing.
6. Write the first-week plan, day by day, and the risks to the engagement.

### Time

90 minutes: 20 for the interview, 30 for the charter, 25 for the first read, 15 for the plan and the access request.

### Done when

- [ ] The objective is Igor's, read back; Shlomit's ask appears as the claim the engagement tests.
- [ ] The decision-rights table names Wasim for safety, Hagit for patients' information, the CEO and board for money, the steering group for the vendor; you design and score.
- [ ] The SOW has three phases with an exit, a deliverable and a decider at each; "don't buy now" is a permitted outcome.
- [ ] The charter says the proof of concept uses synthetic visits only.
- [ ] At least eight numbers are sorted with their evidence, including "98%", "2 hours" and the KPI's language mix.
- [ ] The first week reaches a real clinic list, counsel and the CEO (or names the risk if the CEO can't be reached).

<details><summary>Reference answer</summary>

The full expert version is in the module download, `labs/module-10/expert/01-engagement-charter.md`. Key parts:

**Objective (Igor, read back 15 November):** "A recommendation, backed by evidence from Galil's own conditions, on which ambient-scribe vendor Galil should contract with, on what terms, and how it should be piloted with clinicians before any network-wide rollout", with "that IT can actually integrate" added at read-back. **Stated ask tested:** "an ambient scribe for every doctor by Q2 2027" (board, 21 October), ScribeWave preferred, 12% discount to 31 December.

**Decision rights:** clinical safety and stop rules, Wasim; patients' information, Hagit (with external counsel); money, Shlomit up to ₪300,000, the board above; vendor, the steering group; integration, Igor; the consultant designs the evidence, scores it, and never negotiates.

**SOW:** Diagnose 15 Nov – 3 Dec, ₪62,000, exit at the 3 December readout; Select 6 Dec – 14 Jan, ₪114,000, exit after the PoC results on 31 December; Readout and handover 17–21 Jan, ₪22,000. Changes by written request signed by Igor. PoC on synthetic visits only, ≤ ₪75,000 on Igor's signature.

**First read (excerpt):** "98%" claim to test (scripted English, studio, one speaker); "2 hours saved" claim to test (self-reported survey); "2 hours on notes" unverifiable (not measured); 77% Hebrew claim to test (Notara field); 24-hour signing 98% verified but measures signing; 9 vacancies and ₪2.1M locums verified; Kol Refua "never leaves Israel" contradicted (Annex B); MedNote "zero integration" contradicted for two regions; Rishma "2.1% omissions" claim to test (independent, Hebrew not included); cloud committee "established" claim to test (one meeting in 2022); privacy notice "stored in Israel" verified as a promise.

**Missing, requested on day 2:** the patients' preferred-language field; anonymised exit-interview summaries; the health-fund agreements in full; every vendor's full DPA and sub-processor list; any report of earlier trials.

**First week:** Sun Igor and the first read; Mon Wasim; Tue Hagit; Wed half a day on Elena's list in Karmiel; Thu Suha, first cut of the language and documentation-time measures, weekly note. Shlomit: 20 minutes requested before 3 December.

**What the transcript's interviewer found and missed:** found the 2025 dictation trial by asking whether Galil had tried before; missed Igor's private preference for MedNote and the Notara master agreement's data clause (7.2), both of which pull the selection towards the incumbent.

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting): the advisor's role and due diligence on claims and vendors (named, not re-taught).
- [Patient's Rights Law, 5756-1996](https://he.wikisource.org/wiki/חוק_זכויות_החולה) (חוק זכויות החולה): section 17 (the medical record and who keeps it), section 19 (confidentiality). Route every reading to Galil's counsel.
- IAPP, [Amendment 13 to Israel's Privacy Protection Law](https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform) (in force 14 August 2025).
- Field kit: [01.1 · Three ways in](../module-01/lesson-01.md), [01.2 · Getting a real mandate](../module-01/lesson-02.md), [01.3 · Scope boundary](../module-01/lesson-03.md), [01.5 · The first-day data-room read](../module-01/lesson-05.md); the first engagement's version: [08.1 · The call](../module-08/lesson-01.md).
- Templates: [engagement charter](../../templates/engagement-charter.md), [scope boundary](../../templates/scope-boundary.md), [data-room first read](../../templates/data-room-first-read.md), [access request pack](../../templates/access-request-pack.md), [30-60-90 plan](../../templates/30-60-90-plan.md).
- Next: [10.2 · Discovery](lesson-02.md).
