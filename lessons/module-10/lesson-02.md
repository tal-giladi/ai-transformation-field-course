---
id: "10.2"
module: 10
minutes: 20
practice_minutes: 180
prerequisites: ["10.1", "01.6", "02.2", "02.4", "02.5"]
objectives:
  - "Interview a CMO, a frontline doctor, a head of nursing and a patient, and get the facts each would not volunteer."
  - "Measure documentation time per visit and per doctor-day from a record system's audit fields where nobody had measured it."
  - "Test a language field against a second source and show what a wrong default does to every decision built on it."
  - "Find unsanctioned AI use from a survey, a firewall summary and an incident log, and report it without exposing anyone."
volatility: implementation
sources:
  - title: "Patient's Rights Law, 5756-1996 (Hebrew Wikisource): section 17 medical record, section 19 confidentiality, section 20 disclosure"
    url: https://he.wikisource.org/wiki/חוק_זכויות_החולה
  - title: "Mako, 5 March 2026: Ministry of Health emergency directive limiting generative-AI use in health organizations (signed by the ministry's information-security and cyber officer)"
    url: https://www.mako.co.il/news-lifestyle/2026_q1/Article-1fc042e638dbc91027.htm
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): verified vs reported, the same-word test"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
last_verified: "2026-11-02"
---

# 10.2 · Discovery

The CEO's slide says doctors spend two hours a day on notes and a scribe will give them back. Before you test any vendor, you need Galil's own version of that sentence: how long notes really take, where, for whom, and what doctors already do about it. In this lesson you interview four people (the CMO, a family doctor, the head of nursing and a patient), measure documentation time and the language mix from Notara's export, and look for AI that is already in use. At the end you have a findings memo with every finding labelled and traced to its evidence.

## The situation

Monday 16 to Thursday 26 November 2026. Your charter is signed (10.1). Igor booked Dr. Wasim Haddad (CMO) for Monday, half a day on Dr. Elena Volkova's list in Karmiel for Wednesday and Suha Nasser (Head of Nursing) for Thursday. Wasim arranged, with her consent, a conversation with a patient, Fatma Abu-Ras, 64, and her daughter, in Majd al-Krum on Tuesday 24 November. The phase-1 readout is on Thursday 3 December.

This is module 2's discovery run on a clinical network: [interviews](../module-02/lesson-02.md) that ask for the work, [baselines from exports](../module-02/lesson-04.md), [profiling the data](../module-02/lesson-05.md) before you trust it, and the [shadow-AI census](../module-01/lesson-06.md). IBM's consulting certificate calls the distinction you keep *verified versus reported*; every finding gets a label: **measured**, **reported** or **inferred**.

## What to do

### Step 1 — Map who knows what

| Person | Knows | Needs | Risks by talking |
|---|---|---|---|
| Wasim (CMO) | What makes a note dangerous; past incidents | A tool that doesn't drop what relatives say | Admitting he tolerated something |
| Elena (family doctor, Karmiel) | What a day of notes is really like | Her evenings back | Being named for what she does about it |
| Suha (Head of Nursing) | Who interprets; what nurses carry | Nurses counted and consulted | Nothing, if asked the right question |
| Fatma (patient, with her daughter) | What a visit is like from the chair | Correct medicines, a doctor who looks up | Being "studied" |

Put them on the [stakeholder map](../../templates/stakeholder-map.md).

### Step 2 — Interview for the work, and test three words

Use the [interview guide](../../templates/interview-guide.md). Three words mean different things to different people at Galil:

- **"Accurate."** To the vendor, words in the transcript. To Wasim, "how often a clinically relevant fact is missing or wrong in the note". Ask: "When a note is wrong, what is usually wrong with it?"
- **"The language of the visit."** To the KPI report, a field in Notara. To Elena, a Russian conversation she types in Hebrew. Ask: "Which language was the last visit in, and which language did you write it in?"
- **"Recording."** To a vendor, a feature. To a patient, a stranger listening. Ask Fatma: "What would make it all right, and what would make you say no?"

Protect the people who answer. Elena will only tell you how she really gets her notes done once you have promised that nothing goes into your notes with her name or anyone else's. Write the promise down and keep it.

Run each interview as a roleplay ([Wasim](../../labs/module-10/personas/wasim-cmo.md), [Elena](../../labs/module-10/personas/elena-family-doctor.md), [Suha](../../labs/module-10/personas/suha-head-of-nursing.md), [Fatma](../../labs/module-10/personas/fatma-patient.md)) and score it with the [coach prompt](../../labs/common/coach-prompt.md), or read the [transcripts](../../labs/module-10/personas/transcripts/) and mark what each interviewer found and missed.

**The patient is different.** Fatma is not a data source; she is the person a scribe would record. Let her tell a visit in order, speak to her rather than to her daughter, use no technical words, and don't argue for or against recording. Her July visit (her daughter told a substitute doctor she had stopped a blood-pressure pill; it was never written down; the pharmacy kept dispensing it) is the clinical risk of this whole engagement in one story: what a relative says is what gets lost.

### Step 3 — Test the language field before you use it

The KPI report shows visits by language: Hebrew 77.1%, Arabic 12.8%, Russian 9.0%. Footnote 1 says the figure is Notara's "visit language" field. Profile it the way [02.5](../module-02/lesson-05.md) taught: where does the field come from, and is there a second source? `notara/visits-sample.csv` has both `visit_language` (Notara) and `patient_pref_language` (the appointment system, set when the patient registers).

In a spreadsheet: a pivot of each column, then a pivot of one against the other.

| Source | Hebrew | Arabic | Russian | Other |
|---|---|---|---|---|
| Notara `visit_language` | 77.1% | 12.8% | 9.0% | 1.0% |
| Appointment `patient_pref_language` | 30.1% | 38.2% | 28.4% | 3.3% |

1,921 of the 2,857 visits whose patient prefers another language (67%) are recorded as Hebrew: the field defaults to Hebrew and most doctors never change it. Label: **measured**. Consequence: any decision weighted by the KPI's language mix, including how much "Hebrew support" matters in a vendor, is off by a factor of about three for Arabic and Russian.

While you are there, profile the other fields you will use: `relative_present` is blank in 39.5% of visits (optional field), `interpreter` in 9%. Report rates for the rows where the field is filled, and say so.

### Step 4 — Build the baseline nobody measured

"Documentation time per visit: not measured" (KPI report). Notara's audit log knows two things per note: how long the note window was active (`note_active_sec`) and how much of that happened after clinic hours (`after_hours_sec`). Write the definition card first ([02.4](../module-02/lesson-04.md)):

> **Documentation minutes per doctor-day:** for each doctor, the mean of (`note_active_sec` + `after_hours_sec`) ÷ 60 over that doctor's sampled visits, times the number of visits on each of that doctor's days in `doctor-days.csv`. Source: Notara audit log, 8% sample of visits and full daily counts, 1 September – 31 October 2026. Excludes time reading results and writing letters outside a visit note.

The result on Galil's data:

| Measure | Value | Label |
|---|---|---|
| Active note time per visit | median 4.2 min, mean 4.8 | measured |
| Visits with after-hours work | 18.6% | measured |
| Documentation per doctor-day | median **112 min** (p75 136) | measured (estimate) |
| of which after hours | median 10 min, mean 12 | measured |
| Doctors' own estimate (survey, 60 of 78) | median 120 min a day; 2 evenings a week | reported |
| Notes signed within 24 hours | 98.1% | measured, but it measures signing, not effort |

Two things to say plainly in the memo. The doctors' estimate is close to the measure; the burden is real. And "saves doctors 2 hours a day" is more than **all** the documentation time Galil's own system records.

### Step 5 — Find where the burden sits

A network average hides where the time goes. Join the visits to `people/clinicians.csv` (each doctor's languages) and mark each visit: does the doctor speak the patient's preferred language? In a spreadsheet: a lookup of the doctor's `languages` and `=ISNUMBER(SEARCH(I2, langs))`.

| | Doctor speaks the language (2,949 visits) | Mismatch (1,138 visits, 27.8%) |
|---|---|---|
| Note time per visit, median | 3.9 min | **5.5 min** (+43%) |
| Visits with after-hours work | 13% | **33%** |
| Who interprets | — | relative 47.6%, nurse 27.9%, nobody 9.3%, blank 9.2%, phone 5.9% |

Even when the doctor speaks Arabic or Russian, the note takes longer than a Hebrew visit (4.0 and 4.3 vs 3.6 minutes median): the note is written in Hebrew. By clinic, mismatch runs from about 1% in Nazareth, Majd al-Krum and Maghar (Arabic-speaking doctors and patients) to 45% in Nof HaGalil and 57% in Karmiel Women's Health. Suha's nurses report a median of 42 minutes a day interpreting (survey, reported); in the export, a nurse interprets in about 8% of all doctor visits.

The finding: Galil's documentation problem is a **language problem** as much as a typing problem. A scribe that works in Hebrew helps the visits that need it least.

### Step 6 — Run the shadow-AI census

Use the method of [01.6](../module-01/lesson-06.md): survey, logs, incidents, interviews, never one source alone.

- **Survey.** `tools_used_for_notes`: Notara templates 43, "other" 22, none 18, dictation 1. Eleven comments mention a phone, an app or an AI tool, in Hebrew, Russian, Arabic and English: "אני מקליטה את השיחה בטלפון ומבקשת סיכום" (*I record the conversation on my phone and ask for a summary*); "Записываю приём на телефон, приложение делает выжимку по-русски" (*I record the visit on my phone; the app makes a summary in Russian*).
- **Firewall.** `it/proxy-ai-summary-2026-10.csv`: "AI speech-to-text (consumer)" on the **guest Wi-Fi** in five clinics, with large uploads (Karmiel 2.4 GB in four weeks; 6.9 GB in all), and ChatGPT on the clinic network in nine.
- **Incidents.** IN-2026-052, Karmiel, 17 September: a penicillin allergy said by a patient's son in Russian was missing from the record; the doctor said the summary "from the phone" left it out.
- **Interview.** Elena, after your promise: she records most visits on her personal phone, pastes a translated summary into Notara, and knows about ten colleagues who do the same.

Report it as a system finding, never as people: "visits are being recorded on personal devices with consumer apps in at least five clinics" (measured + reported, unattributed). Two consequences belong next to it. The risk of doing nothing is not zero: patient audio is already leaving Galil to services nobody has reviewed. And it is the kind of use the Ministry of Health's information-security officer told health organizations to stop in March 2026, when, during the war with Iran, he ordered an immediate cut in public generative-AI tools and banned entering patient data into them (as reported by Mako; ask counsel what is in force now). How Galil responds (an instruction, an amnesty, a date for an approved tool) is the CMO's and counsel's decision, not yours.

### Step 7 — Find what was tried before

`notara/mednote-dictation-trial-2025.csv` is in the data room with no explanation. Count, per week, the doctors who dictated at least 10% of their visits: nine in weeks 1–4, six in week 5, five in week 6, two from week 7. The incident log has two documentation near misses in the same weeks (IN-2025-031: metformin transcribed for metoprolol; IN-2025-044: a daughter's report that her mother had stopped Eliquis, missing from the dictated summary). Igor tells you about the trial if you ask whether Galil has tried before; Wasim tells you about the incidents if you ask about safety. Label: measured (usage, incidents), reported (why).

**Track B (Python).** `python discovery.py` in `labs/module-10/` (module download) prints every number in steps 3–7. Python is worth it here because the per-doctor scaling (mean note time from a sample times the full daily counts) and the language-match join are fiddly in a spreadsheet, and Galil will need exactly this measure again: it is the pilot's baseline in 10.5 and its gate in May.

### Step 8 — Write the findings memo

Follow [02.7](../module-02/lesson-07.md) and the [findings memo](../../templates/findings-memo.md) template: the answer first, then each finding with evidence, label and consequence, then what you did not find. Three rules here:

1. **Every number names its source and sample.** "4.2 minutes per visit, median, 8% sample of doctor visits, Sep–Oct 2026".
2. **Nobody is named for what they told you.** Elena is "a doctor"; the shadow use is "at least five clinics".
3. **Legal readings are counsel's.** The memo says "visits are recorded on personal devices"; whether that breaches anything is Hagit's question.

## Watch out

- **Trusting a field because it's in the system.** The language field looked authoritative. Every field you build on needs a second source.
- **Using the survey as the baseline.** Self-report is a good sign of pain and a bad measure of minutes. Use the audit log for minutes and the survey for evenings and concerns.
- **A network average.** 112 minutes a doctor-day hides that mismatch visits take 43% longer. Cut by language and clinic before you write a requirement.
- **Exposing the doctor who helped you.** If "Elena's app" is mentioned in a steering meeting, no clinician will talk to you again, and the shadow use goes further underground.
- **Treating the patient as a case study.** Use Fatma's story only with her consent, without her name, and to shape the consent wording, not to win an argument.
- **Ignoring what was tried.** A trial that faded is the best predictor you have of how the next one fails.

## Your turn

### Inputs

- Data room (module download): `notara/visits-sample.csv`, `notara/doctor-days.csv`, `notara/mednote-dictation-trial-2025.csv`, `people/clinicians.csv`, `people/clinician-survey-2026-10.csv`, `it/proxy-ai-summary-2026-10.csv`, `quality/patient-safety-incidents.csv`, `company/kpi-report-2026-q3.md`.
- Personas: [Wasim](../../labs/module-10/personas/wasim-cmo.md), [Elena](../../labs/module-10/personas/elena-family-doctor.md), [Suha](../../labs/module-10/personas/suha-head-of-nursing.md), [Fatma](../../labs/module-10/personas/fatma-patient.md), or their [transcripts](../../labs/module-10/personas/transcripts/); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [stakeholder map](../../templates/stakeholder-map.md), [interview guide](../../templates/interview-guide.md), [data profile](../../templates/data-profile.md), [shadow-AI survey](../../templates/shadow-ai-survey.md), [findings memo](../../templates/findings-memo.md).
- Track B: `labs/module-10/discovery.py`.

### Steps

1. Fill the stakeholder map for the four people.
2. Interview at least two by roleplay (one must be Elena or Fatma) and read the other transcripts; for each, write one hidden fact you got and one you did not.
3. Profile the language field against the preferred language; profile `relative_present` and `interpreter`.
4. Write the definition card and compute documentation minutes per visit and per doctor-day; set them beside the survey.
5. Split note time and after-hours work by language match and by clinic.
6. Run the shadow-AI census from three sources; write the finding without names.
7. Read the 2025 trial week by week and find its incidents.
8. Write the findings memo (answer first; 6–9 findings; labels; consequences; what you did not find).

**Track B (Python).** Run `python discovery.py`, check two of its numbers against your spreadsheet, then use it for the memo.

### Time

180 minutes: 60 for interviews, 70 for the measurements (40 with Track B), 50 for the memo.

### Done when

- [ ] The language mix is shown from two sources, with the share of non-Hebrew visits recorded as Hebrew.
- [ ] Documentation time has a definition card, a per-visit and a per-doctor-day figure, and the survey beside it labelled reported.
- [ ] The memo shows where the burden concentrates (language match, clinics) with counts.
- [ ] The shadow-AI finding uses at least three sources and names nobody.
- [ ] The 2025 trial's usage curve and its two incidents are in the memo.
- [ ] Every finding has a label, its evidence and a consequence; no finding gives a legal reading.

<details><summary>Reference answer</summary>

The full memo is `labs/module-10/expert/02-findings-memo.md` in the module download. The opening and three findings:

**Answer first.** Galil's documentation burden is real but not where the plan assumes. It sits in visits where doctor and patient do not share a language, and in visits with relatives. The KPI report hides this because Notara records 77% of visits as Hebrew when about two thirds of patients prefer Arabic or Russian. A scribe helps Galil only if it works in Galilee Arabic and Russian with relatives in the room; the demo that impressed the steering group was in English. Some doctors are already recording visits on consumer apps.

**F2 (measured).** Documentation per doctor-day: median 112 minutes (p75 136), after hours median 10; per visit median 4.2 minutes; 18.6% of visits need after-hours work. Doctors report 120 minutes (survey, reported). *Consequence:* "saves 2 hours a day" exceeds all documentation time Galil measures; savings must be measured against 112.

**F3 (measured).** Mismatch in 27.8% of visits; note time 5.5 vs 3.9 minutes (+43%); after-hours work 33% vs 13%; highest in Karmiel Women's Health (57%), Nahariya Paediatrics (51%), Nof HaGalil (45%), Tiberias (42%). *Consequence:* Arabic and Russian performance with relatives is the requirement.

**F5 (measured + reported, unattributed).** Consumer speech-to-text uploads on guest Wi-Fi in five clinics (6.9 GB in four weeks); 11 survey comments on phones, apps or AI; IN-2026-052 (allergy missing from a summary "from the phone"); a doctor's account of about ten colleagues. *Consequence:* doing nothing is not risk-free; the pilot must offer a sanctioned tool and a date.

**Interviews, what the transcripts got and missed:**

| Person | Found | Missed |
|---|---|---|
| Wasim | Hard visits; the two 2025 near misses; nurses interpret; offers to write the PoC scripts | That he knows doctors record on phones and the September incident (no non-attribution promise was made) |
| Elena | The phone app, after the promise; about ten colleagues; what a usable tool must do | Her own near miss (the allergy) and what would make her stop |
| Suha | Nurses interpret, about 40 minutes a day, recorded nowhere | The staff committee's consultation clause for recording technology |
| Fatma | The July visit and the stopped pill; yes to recording if explained in Arabic and deleted | What would make her refuse: recordings "abroad" or sent to the health fund |

</details>

## References

- [Patient's Rights Law, 5756-1996](https://he.wikisource.org/wiki/חוק_זכויות_החולה), sections 17, 19 and 20 (the record, confidentiality, disclosure): why personal-device recording is counsel's question, not yours.
- Mako, [Ministry of Health emergency directive on generative AI](https://www.mako.co.il/news-lifestyle/2026_q1/Article-1fc042e638dbc91027.htm) (5 March 2026, as reported; the directive itself was not published online): ask counsel what applies now.
- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting): verified vs reported (named, not re-taught).
- Field kit: [01.6 · The shadow-AI census](../module-01/lesson-06.md), [02.2 · The discovery interview](../module-02/lesson-02.md), [02.4 · Measuring a baseline from exports](../module-02/lesson-04.md), [02.5 · Profiling the data](../module-02/lesson-05.md), [02.7 · Writing a findings memo people believe](../module-02/lesson-07.md).
- Templates: [stakeholder map](../../templates/stakeholder-map.md), [interview guide](../../templates/interview-guide.md), [data profile](../../templates/data-profile.md), [shadow-AI survey](../../templates/shadow-ai-survey.md), [findings memo](../../templates/findings-memo.md).
- Earlier: [10.1 · The call](lesson-01.md). Next: [10.3 · Diagnosis](lesson-03.md).
