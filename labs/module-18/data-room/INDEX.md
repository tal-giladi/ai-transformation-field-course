# Tzurim Academic College — data room

Tzurim Academic College is a private academic college in the southern Shfela: about 6,840 students, 712 staff, six first-degree programmes and an MBA. You are an outside consultant, engaged on 3 February 2027 after the board asked for one recommendation on student retention and AI by 4 May 2027 (see `../brief.md`). This folder is what the VP Administration's office assembled from your first request: exports from the student information system, finance, the LMS and the inquiry portal, policies and procedures, reports, minutes, e-mails, a survey, IT summaries and a vendor's documents.

Everything here is fictional and synthetic: the college, its people, students, systems, vendors and numbers. Real laws are referred to by name; read them in their current version and route legal questions to counsel and the DPO. Students appear as student numbers; a few files hold first and last names because the unit that produced them held them.

## How to open

**Spreadsheet (Track A).** CSV files are UTF-8 and contain Hebrew, Arabic, Russian and English. In Excel use *Data → From Text/CSV* and pick *65001: Unicode (UTF-8)*; Google Sheets and LibreOffice detect it. Free-text fields contain commas inside quotes: import, don't paste. Import student-number columns as **text**, never as numbers. Markdown (`.md`) files open in any text editor.

**Python (Track B).**

```python
import pandas as pd
from fieldkit.data import data_room, load
room = data_room("module-18")
inq = load(room / "inquiries" / "student-inquiries-2025-26.csv")          # *_at columns parsed as Israel time
reg = pd.read_csv(room / "students" / "registry-students-2023-2025.csv", dtype=str, keep_default_na=False)
```

`load` parses columns whose names end in `_at` or `_date` and turns all-number columns into numbers; for files whose identifiers must stay text, read them with `dtype=str` as above. Look at each file's identifiers and time formats before you join anything.

**Rebuilding.** `generate.py` (Python 3.12+, standard library only; the other `.py` files in this folder are its parts) rebuilds every file byte for byte with `python generate.py`. Reading it spoils the capstone: do not open it until you have submitted your deliverables.

## Files

The capstone has no lesson-by-lesson guide to the files: deciding what to read, in which order, is part of the work.

### company/

| File | What it is |
|---|---|
| `college-profile.md` | The college in one page (January 2027) |
| `org-chart.md` | Who runs what, the DPO, the student union and the adjunct committee |
| `board-minutes-2027-01-20-extract.md` | The board session where the ask was made |
| `dropout-report-2026-12.md` | The registrar's annual first-year dropout report |
| `budget-2027-extract.md` | 2027 budget lines and the finance procedure's rules |

### students/

| File | What it is | Rows |
|---|---|---|
| `registry-students-2023-2025.csv` | Rishum 2 extract: students admitted in 2023, 2024 and 2025, with programme, track, first language from the admission form, reservist status, status after the first year and current status | 6,760 |
| `status-codes.csv` | Status codes in Rishum 2 | 10 |
| `exam-periods-first-year-2025-26.csv` | First-year students' exam periods 2025-26: exams in plan, registered, sat, passed, failed | 4,326 |

### finance/

| File | What it is | Rows |
|---|---|---|
| `tuition-accounts-2025-26.csv` | Finance ERP export, students admitted 2023–2025 enrolled in 2025-26: tuition, scholarships, plan, balances and blocks by semester, write-offs | 6,128 |
| `collections-memo-2023-09.md` | The VP Finance's 2023 memo on exam-registration blocks | — |

### inquiries/

| File | What it is | Rows |
|---|---|---|
| `student-inquiries-2025-26.csv` | Inquiry portal export, inquiries opened November 2025 – July 2026: text, category the student chose, units, reassignments, reply language, dates | 2,669 |
| `inquiry-routing.md` | Categories, routing and the student charter | — |

### student-success/

| File | What it is | Rows |
|---|---|---|
| `adviser-contacts-2025-26.csv` | The advisers' contact log | 1,184 |
| `early-contact-procedure-2024.md` | Procedure SS-03 | — |
| `emails-red-list-2026-03.md` | E-mail thread, March 2026 | — |
| `red-list-for-lecturers-2026-03-16.csv` | Export of the sheet in that thread | 288 |

### lms/

| File | What it is | Rows |
|---|---|---|
| `tavla-activity-monthly-first-year-2025-26.csv` | Tavla LMS monthly activity of first-year students, November 2025 – March 2026 | 11,497 |
| `engagement-insights-export-2026-03-15.csv` | Tavla Engagement Insights export, 15 March 2026 | 2,231 |
| `tavla-release-notes-2026-2.md` | Vendor release notes, February 2026 | — |

### policies/

| File | What it is |
|---|---|
| `academic-regulations-extract-2025-26.md` | Academic regulations: exams, accommodations, reserve duty, AI in assignments, misconduct |
| `tuition-regulations-2025-26.md` | Tuition regulations: payment, scholarships, blocks, arrangements |
| `reservist-students-policy-2025-26.md` | Support for students on reserve duty |
| `it-acceptable-use-2019.md` | IT acceptable-use policy (2019) |
| `faculty-ai-guidance-draft-2025-09.md` | Draft faculty guidance on generative AI |
| `student-privacy-notice-2022.md` | The privacy notice on the student portal |

### academic/

| File | What it is | Rows |
|---|---|---|
| `integrity-cases-2025-26.csv` | Disciplinary committee cases on suspected misconduct in assignments, 2025-26 | 46 |

### people/

| File | What it is | Rows |
|---|---|---|
| `staff-ai-survey-2026-06-responses.csv` | HR's staff survey on AI tools, raw responses | 276 |
| `staff-ai-survey-2026-06-summary.md` | HR's summary of the survey | — |
| `adjunct-committee-letter-2026-10-20.md` | Letter from the adjunct lecturers' committee | — |

### it/

| File | What it is | Rows |
|---|---|---|
| `systems-and-contracts.csv` | Systems, vendors, hosting, contracts, AI features, data processing agreements | 9 |
| `proxy-ai-summary-2026-06-to-09.csv` | Web proxy summary: AI-related domains by network segment and month | 180 |
| `office-ai-assistant-usage-2026-10.csv` | Usage of the 120 office AI assistant licences | 120 |

### vendor/

| File | What it is |
|---|---|
| `persevia-proposal.md` | Persevia's proposal (28 December 2026) |
| `persevia-case-study.md` | Persevia's case study |
| `persevia-pilot-terms.md` | Pilot terms and data processing addendum, extract |
| `emails-ceo-persevia-2027-01.md` | E-mail thread between the CEO, Persevia and IT, January 2027 |

## What is not here

Anything you need and do not find: ask for it in your access request. Some of it exists only in people's heads.
