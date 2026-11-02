# Module 10 lab files — Galil Health

Everything you need to run the Galil Health engagement: the brief, the data room, the people you interview, the proof-of-concept results, a scoring sheet, two Track B scripts and (for the debrief only) the expert's deliverables. All people, organizations and vendors are fictional and all data is synthetic. No real patient's audio or record appears anywhere; the proof-of-concept visits were "recorded" by actors from scripts.

## What is in this folder

| Path | What it is | Lesson |
|---|---|---|
| `brief.md` | The engagement brief: how you were brought in, the stated ask, contract, budget, timeline, access on day one | 10.1 |
| `data-room/` | Galil's data room: start with [`INDEX.md`](data-room/INDEX.md). An 8% sample of doctor visits with Notara's documentation fields, doctor-day counts, the clinician list and survey, the KPI report, board minute, finance summary, the 2025 dictation trial, the incident log, the firewall's AI summary, the cloud committee's minutes, contract extracts, the patient privacy notice, and the four vendors' documents and demo-day scorecards | 10.1–10.6 |
| `data-room/generate.py`, `textbank.py` | The seeded generator (Python standard library only): `python generate.py` rebuilds every data file, and the files in `poc/`, byte for byte. Reading it spoils the engagement | — |
| `personas/` | The cast of nine ([README](personas/README.md)): roleplay prompts and pre-run transcripts | 10.1–10.6 |
| `poc/` | The proof of concept's results: [`README.md`](poc/README.md) (how it was run, column meanings), `visits-90.csv`, `review-sheet.csv` (one row per note: 4 vendors × 90 visits × 2 runs), `rfp-responses.csv` (each vendor's answer to every contract term), `sample-notes.md` (three visits, every vendor's note side by side). Open after you have written your PoC protocol | 10.4, 10.5 |
| `rfp-scoring-sheet.csv` | The scoring sheet: one row per vendor and criterion, weights, the steering group's demo-day scores, empty columns for your evidence scores and their reasons | 10.4, 10.5 |
| `discovery.py` | Track B: the language mix two ways, language match and its effect on documentation time, minutes per doctor-day, 24-hour signing, shadow-AI signals, the 2025 trial, the demo-day scores | 10.2, 10.3 |
| `poc_score.py` | Track B: PoC results per vendor and language with Wilson 95% intervals, the effect of relatives, unsure-marking, must-haves refused; weighted scores from your own scoring file | 10.4, 10.5 |
| `expert/` | The expert's deliverables for comparison in the debrief; open them only after your own ([README](expert/README.md)) | 10.6 |

## Track A — no code

1. Open the CSV files in Excel, Google Sheets or LibreOffice Calc. In Excel use *Data → From Text/CSV* and choose *65001: Unicode (UTF-8)*: comments and scripts contain Hebrew, Arabic and Russian.
2. **10.2, the language field:** in `notara/visits-sample.csv` build two pivots (count of `visit_id` by `visit_language`, and by `patient_pref_language`), then one against the other.
3. **10.2, documentation time:** add `=(O2+P2)/60` (note plus after-hours minutes). Average it per `clinician_id` with a pivot; look each doctor's average up in `notara/doctor-days.csv` and multiply by `visits`; take the median of that column.
4. **10.2, language match:** look up each visit's doctor in `people/clinicians.csv` and test `=ISNUMBER(SEARCH(I2, languages))`; pivot note minutes and `after_hours_sec>0` by the result and by `clinic_id`.
5. **10.4, the PoC:** pivot `poc/review-sheet.csv` by `vendor` and `language`: sum of `omitted_relevant` and `invented`, count of rows with `status` = scored, average of `wer_pct` and `minutes_to_correct`. Per 100 notes = sum ÷ count × 100.
6. **10.5, scoring:** fill `evidence_score_1to5` and `evidence_for_the_score` in a copy of `rfp-scoring-sheet.csv`; weighted score per vendor = `SUMPRODUCT(weight, score) / 13`.

The `vendor-rfp` simulation (`?preset=galil`) uses the same four vendors, claims, PoC results and terms; lessons 10.4 and 10.5 link it.

## Track B — Python

Set up the field kit once ([instructions](../common/README.md)): Python 3.12 or newer and `pip install -r ../common/requirements.txt`. No extra packages. From this folder:

```bash
python discovery.py                          # 10.2, 10.3: the discovery numbers
python poc_score.py                          # 10.4: the PoC results with intervals and the must-have gate
python poc_score.py --scores my-scores.csv   # 10.5: weighted totals from your scores (columns vendor,criterion,score)
```

No LLM call and no network access: both scripts read the data-room and PoC files by relative path. On Windows, if non-Latin text prints as `?`, run `$env:PYTHONIOENCODING = "utf-8"` first.

Python is worth it in this module for two reasons: scaling sampled note time to a doctor's day and joining visits to doctors' languages are fiddly in a spreadsheet and become the pilot's baseline and gate measure, and the PoC's intervals are tedious by hand and the same script re-scores any re-test after a vendor changes its model.

**What is real and what is not.** Every number in the lessons and the expert set is computed from these files and reproduces exactly. The organization, people, vendors, prices, contracts and PoC are fictional. Checked on 2 November 2026 with Python 3.14.3 and pandas 3.1.0 (the versions pinned in `../common/requirements.txt`).
