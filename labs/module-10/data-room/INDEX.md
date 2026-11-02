# Galil Health — data room

Galil Health runs 14 community clinics in five regions of northern Israel for about 112,000 patients,
with 78 doctors and 42 nurses. The CIO hired you as an outside consultant for 10 weeks from Sunday 15
November 2026 (see `../brief.md`). This folder is what Galil gave you access to in the first week, under
the NDA and the data-processing agreement: exports, reports, contracts, vendor documents and logs.

Everything here is fictional and synthetic: the organization, the people, the patients and the four
vendors. Patient names and identity numbers were removed before the export; visits carry no clinical
content.

## How to open

**Spreadsheet (Track A).** CSV files are UTF-8 and contain Hebrew, Arabic, Russian and English text. In
Excel use *Data → From Text/CSV* and pick *65001: Unicode (UTF-8)*; Google Sheets and LibreOffice detect
it. Comments contain commas inside quotes: import, don't paste. Markdown (`.md`) files open in any text
editor.

**Python (Track B).**

```python
from fieldkit.data import data_room, load
room = data_room("module-10")
visits = load(room / "notara" / "visits-sample.csv")   # *_at and *_date columns parsed as Israel time
```

**Times.** Israel local time with the UTC offset (`+03:00` in summer, `+02:00` from 25 October 2026).

**The 8% sample.** IT's export of doctor visits is a random 8% of all visits from 1 September to 31
October 2026, with the documentation fields from Notara's audit log. `notara/doctor-days.csv` has the
full visit count for every doctor-day, so you can scale per-visit figures to a doctor's day.

**Rebuilding.** `generate.py` (Python 3.12+, standard library only, text in `textbank.py`) rebuilds every
file byte for byte with `python generate.py`, including the proof-of-concept files in `../poc/`. Reading it
spoils the engagement: finish module 10 first.

## Files

Lesson ids: 10.2 is module 10, lesson 2.

### company/

| File | What it is | Lessons |
|---|---|---|
| `company-profile.md` | Welcome-pack profile: clinics, patients, health funds, Notara, management | 10.1 |
| `org-chart.md` | Units, heads, staff numbers, the staff committee, the regions | 10.1, 10.2 |
| `clinics.csv` | The 14 clinics: region, type, Notara version, doctors, nurses, main patient languages | 10.1, 10.2, 10.5 |
| `board-minutes-2026-10-21.md` | Board minutes, item 4: the CEO's plan and the 2027 budget line | 10.1, 10.3, 10.6 |
| `kpi-report-2026-q3.md` | Clinical operations KPI report, Q3 with October (Operations and BI) | 10.1, 10.2, 10.3 |
| `finance-summary.md` | The CFO's summary: costs, locums, Notara, the board line, how projects are judged | 10.3, 10.5 |

### people/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `clinicians.csv` | Every doctor and nurse: clinic, specialty, FTE, languages spoken, start year | 120 | 10.2, 10.3, 10.5 |
| `clinician-survey-2026-10.csv` | The CMO's documentation survey, 4–22 October 2026: self-reported minutes, evenings, interpreting, would they use a scribe, main concern, tools used, comments (he/ar/ru/en) | 84 | 10.2, 10.3 |

### notara/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `visits-sample.csv` | 8% random sample of doctor visits, Sep–Oct 2026: clinic, doctor, slot, visit type, age band, the patient's preferred language (appointment system), the visit language (Notara field), relative present, interpreter, note opened and signed, seconds of active note time, after-hours seconds, note length, referral letter | 4,087 | 10.2, 10.3 |
| `doctor-days.csv` | Every doctor-day, Sep–Oct 2026, with the full number of visits | 2,413 | 10.2, 10.3 |
| `mednote-dictation-trial-2025.csv` | Weekly usage export from the MedNote dictation trial, March–May 2025: visits, notes dictated, average correction time per doctor | 108 | 10.2, 10.3 |

### quality/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `patient-safety-incidents.csv` | The incident-reporting log, January 2025 – October 2026, with English summaries by the quality coordinator | 56 | 10.2, 10.4 |

### it/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `proxy-ai-summary-2026-10.csv` | The firewall's weekly application summary for AI, translation and messaging apps, October 2026, by clinic and network (clinic LAN or guest Wi-Fi) | 198 | 10.2 |
| `cloud-committee-minutes-2022.md` | Minutes of the organizational cloud committee | — | 10.2, 10.4 |

### legal/

| File | What it is | Lessons |
|---|---|---|
| `health-fund-agreements-extract.md` | The information clauses of the service agreements with the two health funds | 10.2, 10.4, 10.5 |
| `notara-master-agreement-extract.md` | Galil's 2019 agreement with Notara Systems, data and price clauses | 10.4, 10.5 |
| `patient-privacy-notice-2023.md` | The privacy notice patients see on the website and in clinics | 10.4, 10.5 |
| `staff-committee-agreement-extract.md` | Collective agreement, technological change clause | 10.5 |

### vendors/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `rfp-draft-v0.md` | The CIO's draft request for proposal (not sent) | — | 10.1, 10.4 |
| `demo-day-scorecards.csv` | The steering group's and three clinicians' scores at the four demos, 26 Oct – 5 Nov 2026, with each demo's language and set-up | 216 | 10.1, 10.4, 10.5 |
| `scribewave-deck.md`, `scribewave-quote-2026-11.md`, `scribewave-dpa-extract.md` | ScribeWave: deck, the reseller's quote, data-processing agreement | — | 10.1, 10.4, 10.5 |
| `kolrefua-deck.md`, `kolrefua-dpa-extract.md`, `kolrefua-partner-letter.md` | Kol Refua: deck, data-processing agreement with sub-processor annex, a reference letter | — | 10.4, 10.5 |
| `mednote-release-notes.md`, `mednote-offer.md` | MedNote for Notara: release notes and the offer letter | — | 10.4, 10.5 |
| `rishma-deck.md`, `rishma-evaluation-summary.md`, `rishma-safety-case-extract.md`, `rishma-dpa-extract.md` | Rishma Health: deck, independent evaluation summary, clinical safety case, data-processing agreement | — | 10.4, 10.5 |

## What is not here

No patient records or clinical content, no audio, no Notara access, no payroll, no exit-interview notes,
no legal opinions (ask counsel), no Ministry of Health correspondence, and no measure of documentation
time (nobody at Galil has produced one). The proof-of-concept results arrive in lesson 10.4, in `../poc/`.
Ask for what you need in your access request (lesson 10.1).
