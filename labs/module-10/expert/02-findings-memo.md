# 02 · Findings memo — Galil Health

To: Igor Shapiro (CIO). Copy after review: Wasim Haddad, Hagit Peretz, Suha Nasser. Thursday 26 November 2026.
Labels: **measured** (computed from Galil's data), **reported** (someone told me), **inferred** (my reading).
Visit figures come from the 8% sample of doctor visits, 1 September – 31 October 2026 (4,087 visits), scaled
with the full doctor-day counts (2,413 doctor-days).

## Answer first

Galil's documentation burden is real but not where the plan assumes. It sits in the visits where the doctor
and the patient do not share a language, and in the visits with relatives, which together are a large part
of Galil's work. The KPI report hides this because Notara records 77% of visits as Hebrew when about two thirds of
patients prefer Arabic or Russian. A scribe helps Galil only if it works in Galilee Arabic and Russian with
relatives in the room; the demo that impressed the steering group was in English. Some doctors are already
recording visits on consumer apps. Nothing should be signed before the vendors are tested on Galil's own
conditions and before counsel has seen what the health-fund agreements require.

## Findings

**F1 (measured). The language field is wrong.** Notara's `visit_language`: Hebrew 77.1%, Arabic 12.8%,
Russian 9.0%. The appointment system's preferred language for the same visits: Arabic 38.2%, Hebrew 30.1%,
Russian 28.4%, other 3.3%. 1,921 of 2,857 non-Hebrew visits (67%) are recorded as Hebrew; the field defaults to
Hebrew. *Consequence:* any language weighting taken from the KPI report under-weights Arabic and Russian by a
factor of about three.

**F2 (measured). Documentation time was never measured; here is a baseline.** Active note time: median 4.2
minutes a visit (mean 4.8); 18.6% of visits need work after hours. Per doctor-day (visits × that doctor's
mean note and after-hours time): median **112 minutes** (p75 136), of which after hours median 10 (mean 12).
Doctors report a median of 120 minutes a day and two evenings a week finishing notes (survey, 60 of 78
doctors, reported). *Consequence:* "saves 2 hours a day" is more than all the documentation time Galil
measures; any saving must be measured against 112.

**F3 (measured). The burden concentrates where languages don't match.** In 1,138 of 4,087 visits (27.8%)
the doctor does not speak the patient's preferred language. There, note time is 5.5 vs 3.9 minutes (median,
+43%) and 33% vs 13% of visits need after-hours work. Even when the doctor speaks Arabic or Russian, the note
takes longer than a Hebrew visit (4.0 and 4.3 vs 3.6 minutes): the note is written in Hebrew. Mismatch is
highest in the mixed clinics and specialist centres (Karmiel Women's Health 57%, Nahariya Paediatrics 51%,
Nof HaGalil 45%, Tiberias 42%) and near zero in Nazareth, Majd al-Krum and Maghar. *Consequence:* the
scribe's Arabic and Russian performance with relatives is the requirement, not a nice-to-have.

**F4 (measured + reported). Nurses interpret, uncounted.** Interpreter in mismatch visits: a relative
47.6%, a nurse 27.9%, nobody 9.3%, blank 9.2%, phone 5.9%; nurses interpret in about 8% of all doctor
visits. Nurses report a median of 42 minutes a day interpreting (survey, 24 of 42 nurses). Suha: they are
pulled from their own clinics (reported). *Consequence:* the quote's 42 nurse seats answer a question
nobody asked; nurses' benefit comes through the doctors' visits.

**F5 (measured + reported, unattributed). Recording on consumer apps already happens.** 22 survey
respondents tick "other" tools; 11 comments mention a phone, an app or an AI tool (in four languages). The
firewall shows consumer speech-to-text uploads on guest Wi-Fi in five clinics (6.9 GB in four weeks;
Karmiel 2.4 GB) and ChatGPT on the clinic network in nine. A doctor described the practice to me (reported,
not attributed): visits recorded on a personal phone, summary pasted into Notara, about ten colleagues.
Incident IN-2026-052 (September) records an allergy missing from a summary "from the phone". *Consequence:*
the risk of doing nothing is not zero; the pilot must give these doctors a sanctioned tool and a date.

**F6 (measured + reported). Galil tried before.** MedNote Dictation trial, March–May 2025: nine doctors
dictating in weeks 1–4, six in week 5, two from week 7 (usage export). Two near misses during the trial
(IN-2025-031, a drug name; IN-2025-044, a medicine stop said by a daughter). No report was written
(reported). *Consequence:* adoption and omissions of what relatives say are the two known failure modes.

**F7 (measured from documents). The demo ranking rests on demo conditions.** The steering group's
scorecards rank ScribeWave and Kol Refua first (3.62 weighted) and Rishma last (2.92). ScribeWave demoed in
English, Kol Refua in Hebrew, MedNote as dictation; only Rishma showed an Arabic and Hebrew visit, recorded.
Each headline number's footnote names conditions unlike Galil's (see the first-read sheet). *Consequence:*
the demo scores cannot be the basis of a choice.

**F8 (reported by counsel; documents). Outside parties have a say.** Fund A's agreement requires its prior
written approval (45 days) before an outside party processes members' medical information, and processing
in Israel unless approved; Fund B wants 30 days' notice. The organizational cloud committee (MOH circular
2/2021) met once in 2022. *Consequence:* 31 December cannot be a signature date; the approvals are on the
critical path. Counsel's readings, not mine.

## What I did not find

No evaluation by Galil of any vendor; no measure of documentation time before this memo; no exit-interview
detail beyond the KPI line; no evidence on how patients feel about recording beyond one interview (a
patient and her daughter: yes, if explained in Arabic and deleted).

**What the transcripts missed:** Wasim's tolerance of phone recording and the September incident (the
interviewer did not promise non-attribution); Elena's own near miss and what would make her stop; Suha's
staff-committee clause; Fatma's conditions for refusing (abroad, the health fund).
