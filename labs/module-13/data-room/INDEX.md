# Kinneret Plastics — data room

Kinneret Plastics is a family-owned injection-moulding company in the Galilee: about 600 people, two plants (Plant K near Tiberias and Plant G near Karmiel, acquired in January 2025), three shifts, 40 moulding machines. You are its operations-excellence manager, told on 7 January 2027 to lead "predictive maintenance with AI" (see `../brief.md`). This folder is what you gathered in the first weeks: exports from the maintenance, production, quality and stores systems, the shared drive's manuals and procedures, reports, letters, a vendor's proposal and two works-committee documents. As an employee you could ask for most of it; where a file came from someone in particular, the file says so.

Everything here is fictional and synthetic: the company, its people, customers, machines, machine makers and suppliers. Real laws are referred to by name; read them in their current version and route legal questions to counsel and the safety officer. Employees appear as ids or first names; no personal data beyond what a manager would see.

## How to open

**Spreadsheet (Track A).** CSV files are UTF-8 and contain Hebrew, Arabic, Russian and English (some headers are Hebrew). In Excel use *Data → From Text/CSV* and pick *65001: Unicode (UTF-8)*; Google Sheets and LibreOffice detect it. Free-text fields contain commas inside quotes: import, don't paste. Markdown (`.md`) files open in any text editor.

**Python (Track B).**

```python
from fieldkit.data import data_room, load
room = data_room("module-13")
wo = load(room / "maintenance" / "work-orders-plant-k-2026.csv")   # *_at columns parsed as Israel time
```

`load` parses columns whose names end in `_at` or `_date`. Files whose time columns are named differently (Plant G's log, the SCADA export, the sensor file) are read as text: look at them before you convert anything.

**Rebuilding.** `generate.py` (Python 3.12+, standard library only; the other `.py` files in this folder are its parts) rebuilds every file byte for byte with `python generate.py`; it also writes the pilot's inputs in `../pilot/`. Reading it spoils the engagement: finish module 13 first.

## Files

Lesson ids: 13.2 is module 13, lesson 2.

### company/

| File | What it is | Lessons |
|---|---|---|
| `company-profile.md` | Business, plants, customers, systems, people (January 2027) | 13.1 |
| `org-chart.md` | Who runs what, maintenance and tooling, the works committee | 13.1, 13.2 |
| `management-meeting-2027-01-07-minutes.md` | The meeting where the ask was made | 13.1 |
| `kpi-deck-2026-12-extract.md` | December operations KPI deck: maintenance and downtime slides | 13.1, 13.2, 13.3 |
| `budget-2027-extract.md` | 2027 operations budget lines, incl. "AI and Industry 4.0" | 13.1, 13.3, 13.4 |
| `arava-letter-2026-12-14.md` | The largest technical-parts customer's letter on 2026 performance | 13.1, 13.3 |

### maintenance/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `work-orders-plant-k-2026.csv` | MaintPro export, Plant K, all work orders of 2026: type, times, technician, problem and action text, failure code, downtime, parts, labour, who closed it | 1,475 | 13.2, 13.3, 13.5 |
| `maintenance-log-plant-g-2026.csv` | Plant G's maintenance log (Excel, Hebrew headers): date, call time, machine, fault, action, technician, status, "ready at" | 682 | 13.2, 13.5 |
| `failure-codes.csv` | The failure-code list in MaintPro (2019) | 24 | 13.2, 13.5 |
| `pm-compliance-report-2026.md` | The planner's 2026 preventive-maintenance compliance report | — | 13.2, 13.3 |
| `night-calls-2026.csv` | Shift supervisors' log of night calls to the maintenance manager (from March 2026) | 78 | 13.2, 13.3, 13.5 |
| `whatsapp-night-shift-2026-11.md` | Extract of the night-shift maintenance WhatsApp group, November 2026 | — | 13.2, 13.5 |
| `shared-drive-listing.csv` | Listing of the maintenance shared drive (manuals, procedures, parts list) | 27 | 13.2, 13.5 |

### production/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `downtime-events-2026.csv` | ProdTrack (MES) stops, both plants, 2026: machine, start, end (production restarted), reason code chosen at the terminal, note | 3,992 | 13.2, 13.3, 13.5 |
| `scrap-weekly-2026.csv` | Quality's weekly scrap per machine with defect codes | 2,080 | 13.2, 13.3 |

### assets/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `asset-register-plant-k.csv` | MaintPro asset register, Plant K (machines and auxiliaries) | 53 | 13.2, 13.5 |
| `asset-list-plant-g.csv` | Plant G's machine list (Excel from the previous owners, Hebrew headers) | 19 | 13.2, 13.5 |
| `mes-machines.csv` | Machines as ProdTrack knows them, both plants | 40 | 13.2, 13.5 |
| `mould-list.csv` | Tooling department's mould list, both plants | 231 | 13.2, 13.3 |

### sensors/ and scada/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `sensors/condition-k21-k23-2026q4.csv` | Historian export for the three machines with condition monitoring, hourly, 1 October – 31 December 2026 | 6,443 | 13.2, 13.4, 13.5 |
| `scada/alarms-plant-g-2026h2.csv` | Plant G line SCADA alarm export, July–December 2026 (as exported, column names in English) | 2,945 | 13.2, 13.5 |

### parts/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `parts-list-shared-drive.csv` | "The parts list" technicians use: the Excel on the maintenance drive | 268 | 13.2, 13.5 |
| `erp-parts-2026-12-31.csv` | Stores extract from the ERP on 31 December 2026, both plants | 343 | 13.2, 13.5 |

### docs/ (the maintenance shared drive's manuals and procedures, as they are)

Equipment manual extracts (English, as the makers supply them: `MAN-*`) and Kinneret's procedures (`SOP-*`), one file per document, language and revision, as found on `\\kp-fs01\maintenance` in January 2027. The shared-drive listing says where each one sits on the drive. 17 files. Lessons 13.2 and 13.5.

### safety/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `periodic-examinations-register.csv` | Register of items that need periodic examination by a qualified examiner (lifting machines, air receivers), both plants | 10 | 13.2, 13.4 |
| `safety-program-extract.md` | Extract of the 2026 safety management programme: examinations and the list of procedures | — | 13.2, 13.4 |

### vendor/

| File | What it is | Lessons |
|---|---|---|
| `predictiva-proposal.md` | Predictiva's proposal (December 2026) | 13.1, 13.4 |
| `predictiva-case-study.md` | The case study attached to the proposal | 13.4 |
| `predictiva-onboarding-guide-extract.md` | Section 3 of the vendor's onboarding guide | 13.4 |
| `predictiva-questionnaire-plant-g.md` | The vendor's data-readiness questionnaire as Plant G filled it | 13.2, 13.4 |
| `email-thread-2026-12.md` | Emails between the vendor and Kinneret, December 2026 | 13.1, 13.4 |

### hr/

| File | What it is | Lessons |
|---|---|---|
| `local-agreement-2021-extract.md` | Local collective agreement, clauses 14–16 | 13.4 |
| `works-committee-letter-2027-01-12.md` | The works committee's letter to management | 13.1, 13.4 |
| `workforce-languages-2026.md` | First languages and reading of Hebrew technical text, production and maintenance | 13.2, 13.4, 13.5 |

## What is not here

No sensor data for any machine other than K21–K23, no PLC programs, no Plant G CMMS (there is none), no maintenance manager's notes, no photos, no recordings, no personal data of employees, no legal opinions, no Predictiva demo on Kinneret's machines, no quality micro-data beyond the weekly scrap, nothing from Arava beyond the letter. Ask for what you need in your access request (lesson 13.1).
