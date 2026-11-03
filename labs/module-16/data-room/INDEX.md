# Open Hands — data room

Open Hands (עמותת ידיים פתוחות (ע"ר)) is a 30-person Israeli amuta in Kiryat Ata that accompanies about
440 families raising children with disabilities. The executive director asked you, a pro bono volunteer
consultant, for four weeks of help from Sunday 15 November 2026 (see `../brief.md`). This folder is what
Ronit and Yossi gave you in the first week: exports, documents, policies and a few notes. There is no
database, no BI team and no IT department: most of it came out of Google Drive and the Workspace admin
console, by hand.

Everything here is fictional and synthetic: the organization, the families, the staff, the volunteers, the
donors, the funders, the municipality of Kiryat Hadas and GrantGenie. Real vendors (Google, Microsoft,
OpenAI, Zoom, Mailchimp, Dropbox) appear only as vendors.

> [!CAUTION]
> The data room imitates sensitive data about disabled children and their families. Treat it the way you
> would treat the real thing: keep it on your own computer, do not paste it into a personal AI account to
> "try something", and follow the data boundary you write in lesson 16.4 when you build in 16.5.

## How to open

**Spreadsheet (Track A).** CSV files are UTF-8 and contain Hebrew, Arabic, Russian and English text. In
Excel use *Data → From Text/CSV* and pick *65001: Unicode (UTF-8)*; Google Sheets and LibreOffice detect
it. Notes contain commas inside quotes: import, don't paste. Markdown (`.md`) files open in any text editor.

**Python (Track B, optional in this module).**

```python
from fieldkit.data import data_room, load
room = data_room("module-16")
audit = load(room / "it" / "drive-sharing-audit.csv")
```

**Pseudonymisation.** Before handing over the files Yossi replaced names with `[NAME]` in case notes and
removed donor names and ID numbers (`[REMOVED]` where the live sheet holds a number). He did it by hand.

**Rebuilding.** `generate.py` (Python 3.12+, standard library only; text in `textbank.py`, the rest in the
other `.py` files) rebuilds every file byte for byte with `python generate.py`. Reading it spoils the
engagement: finish module 16 first.

## Files

Lesson ids: 16.2 is module 16, lesson 2.

### company/

| File | What it is | Lessons |
|---|---|---|
| `org-profile.md` | Welcome-pack profile: programmes, numbers, how the amuta works | 16.1 |
| `org-chart.md` | HR list: 30 people by team, role, FTE and languages; the board | 16.1, 16.2 |
| `board-minutes-2026-10.md` | Board minutes, 27 October 2026: the AI item, the treasurer's questions | 16.1, 16.3, 16.6 |
| `budget-2026.md` | Budget summary: income by source, expenditure lines, the approval rules | 16.1, 16.3, 16.4 |

### people/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `staff.csv` | Staff: id, name, role, team, FTE, languages, start date, work email, employment type | 30 | 16.1, 16.2, 16.4 |
| `volunteers.csv` | Volunteer list (Liat's sheet): programme, status, joined, last activity, email domain, confidentiality form, clearance for work with minors | 142 | 16.2, 16.4 |
| `time-log-2026-10.csv` | One week of time logging (Sun 4 – Thu 8 October 2026) that Ronit asked ten people to keep after the September board: start, minutes, activity, note | 367 | 16.3 |

### cases/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `case-register.csv` | Active families on 12 November 2026: coordinator, town, home language, child's age band, disability group, welfare involvement, referral source, programmes, intake date, consent version and options, whether the family is under the Adler-Haddad grant, last contact | 438 | 16.2, 16.3, 16.4 |
| `case-notes-sample.csv` | 60 case notes from September–November 2026, exported and pseudonymised by Yossi: coordinator, date, language, type, minutes spent writing, text | 60 | 16.4, 16.5 |

### fundraising/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `funders.csv` | The 14 institutional funders: amount, programme, report frequency and format, due dates, development's estimate of hours per report and per proposal | 14 | 16.2, 16.3, 16.5 |
| `donors.csv` | Donor sheet (extract of the live Google Sheet "Donors 2026 (master)"): type, city, language, whether an ID number is on file, gifts 2025–2026, payment method, receipt route, marketing consent, segment, notes | 1,134 | 16.2, 16.4 |
| `grant-library/boilerplate-2025.md` | Development's master text for proposals | — | 16.5 |
| `grant-library/adler-haddad-quarterly-template.md` | The largest funder's quarterly report template | — | 16.3, 16.5 |
| `grant-library/adler-haddad-q3-2026-report-extract.md` | The Q3 2026 report as submitted (extract) | — | 16.2, 16.4, 16.5 |
| `grant-library/outcomes-framework-2024.md` | Open Hands' own outcomes framework, adopted by the board in 2024 | — | 16.3, 16.5 |

### finance/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `card-statement-2026.csv` | The two organization credit cards, January–October 2026: merchant, description, amount, currency, ₪, card, category, approver | 104 | 16.2, 16.3, 16.4 |

### it/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `drive-sharing-audit.csv` | Google Drive sharing report exported by Yossi on 12 November 2026: item, owner, who it is shared with, principal type, role, link sharing, when sharing was added | 151 | 16.2, 16.4 |
| `accounts-and-licences.csv` | Every account and licence Yossi could list: Workspace users, Microsoft seats, other services, last sign-in, billing | 54 | 16.2, 16.3, 16.4 |
| `staff-ai-survey-2026-10.csv` | Ronit's own Google Form "Do you use AI?", 26 October 2026 | 22 | 16.1, 16.2 |
| `yossi-it-notes.md` | Yossi's IT notes (a Google Doc he keeps for himself) | — | 16.2, 16.4 |

### policies/

| File | What it is | Lessons |
|---|---|---|
| `privacy-and-confidentiality-policy-2019.md` | The privacy and confidentiality policy approved by the board in 2019 | 16.2, 16.4 |
| `consent-form-v1-2019.md` | Intake consent, 2019 – February 2023 | 16.2, 16.4, 16.5 |
| `consent-form-v2-2023.md` | Intake consent since March 2023 | 16.2, 16.4, 16.5 |
| `volunteer-handbook-extract.md` | Respite weekends: how volunteers are organised | 16.2, 16.4 |
| `municipal-service-agreement-extract.md` | The Kiryat Hadas service agreement: information clauses | 16.4 |

### comms/ and vendor/

| File | What it is | Lessons |
|---|---|---|
| `comms/newsletter-2026-09.md` | The September 2026 newsletter (email and Facebook) | 16.2, 16.4 |
| `vendor/grantgenie-terms-extract.md` | GrantGenie's terms and nonprofit offer, saved at sign-up | 16.2, 16.4 |
| `vendor/microsoft-renewal-notice.md` | Microsoft's July 2026 notice about the nonprofit licences, forwarded by Yossi | 16.3, 16.4 |

## What is not here

No full case files, no paper files, no WhatsApp groups, no personal accounts of staff or volunteers (you
will only learn about those by asking), no payroll, no audited accounts, no legal opinions (Open Hands has
no counsel; Mahut Pro Bono can arrange a pro bono lawyer), no time log for a normal week, no records of
what was uploaded to any AI tool.
