# Givat Oren municipality — data room

Givat Oren is a city of about 221,000 residents in central Israel (Hebrew, Arabic, Russian, Amharic and
English at home). You are its Head of Digital Services, handed "a citizen chatbot" by the mayor's office
on 26 November 2026 (see `../brief.md`). This folder is what you gathered in the first days: exports,
reports, procedures, pages, letters and emails. As an employee you could ask for most of it; where a
file came from someone in particular, the file says so.

Everything here is fictional and synthetic: the city, its fees and procedures, its people, its
residents and its suppliers. Real laws are referred to by name; read them in their current version and
route legal questions to the legal adviser. Identifiers of residents are hashed (`caller_id`,
application ids); messages are synthetic.

## How to open

**Spreadsheet (Track A).** CSV files are UTF-8 and contain Hebrew, Arabic, Russian, English and some
Amharic. In Excel use *Data → From Text/CSV* and pick *65001: Unicode (UTF-8)*; Google Sheets and
LibreOffice detect it. Messages contain commas inside quotes: import, don't paste. Markdown (`.md`)
files open in any text editor.

**Python (Track B).**

```python
from fieldkit.data import data_room, load
room = data_room("module-11")
contacts = load(room / "service" / "moked-contacts.csv")   # *_at and *_date columns parsed as Israel time
```

**Times.** Israel local time with the UTC offset (`+03:00` in summer, `+02:00` from 25 October 2026).

**The 4% caller sample.** Moked 106's export is every contact of a random 4% of caller numbers from
1 June to 31 October 2026, so a resident's repeated contacts stay together. Multiply counts by 25 for
city totals. Callbacks are the department tasks created from those contacts. The permits export is
complete (every application from January to October 2026).

**Rebuilding.** `generate.py` (Python 3.12+, standard library only, text in `textbank.py`) rebuilds every
file byte for byte with `python generate.py`; it also writes the pilot's inputs in `../pilot/`. Reading
it spoils the engagement: finish module 11 first.

## Files

Lesson ids: 11.2 is module 11, lesson 2.

### city/

| File | What it is | Lessons |
|---|---|---|
| `city-profile.md` | Residents, languages, neighbourhoods, systems, channels | 11.1 |
| `org-chart.md` | Divisions, heads, Moked 106, Digital Services, the works committee | 11.1, 11.2 |
| `mayor-office-email-2026-11-26.md` | The chief of staff's email: the ask | 11.1 |
| `budget-2027-draft-extract.md` | Draft 2027 budget lines for Digital Services, the chatbot line, Moked 106 | 11.1, 11.3, 11.4 |
| `council-decision-fees-2025-12.md` | The council's fee decision for 2026 and the parking-permit rule change | 11.1, 11.2, 11.5 |

### service/ (Moked 106)

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `moked-contacts.csv` | Tikshoret export, 4% caller sample, 1 Jun – 31 Oct 2026: `caller_id`, `opened_at`, `channel`, `contact_language` (IVR choice or detected), `served_language`, `topic` (agent's category), `outcome`, `queue_wait_sec`, `handle_sec`, `agent_id`, `fcr_flag`, `callback_id` | 3,914 | 11.2, 11.3 |
| `callbacks.csv` | Department callback tasks created from those contacts: promised-by date, completion time, result | 943 | 11.2, 11.3 |
| `moked-kpi-report-2026-q3.md` | Moked 106 quarterly service report, Q3 2026 | — | 11.1, 11.2, 11.3 |
| `moked-staffing-2026.csv` | Agents, start dates, languages, contract, status | 26 | 11.2, 11.4 |
| `mystery-shopper-2026.csv` | The quality unit's mystery-shopper calls to 106, August–September 2026: question asked (ids match the pilot's test set), language, who answered in which language, the answer as summarised, the quality unit's result code | 120 | 11.2, 11.5 |

### permits/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `applications-2026.csv` | Rishuyit export, every permit application 1 Jan – 31 Oct 2026 (parking, signs, cafés, events, skips, archive, disabled parking): applicant language, neighbourhood, vehicle ownership, documents, decision, reason code, letter language, fee charged, objections, linked 106 contacts | 2,300 | 11.2, 11.3 |
| `reason-codes.csv` | The eight reason codes clerks choose from | 8 | 11.2 |
| `parking-permit-procedure-v4.md` | Procedure PRK-4, in force 1 July 2026 | — | 11.2, 11.4 |
| `parking-permit-checklist-clerks.md` | The checklist on the parking-permits desk | — | 11.2 |
| `decision-letter-templates.md` | Rishuyit letter templates with English glosses | — | 11.2, 11.4 |

### content/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `cms-pages.csv` | SiteBuilder page inventory: section, language, URL, last modified, owner department and editor, views, fee mentions, PDF links, third-party scripts | 1,240 | 11.2, 11.3, 11.4 |
| `site/` | The permits pages as published on 26 November 2026, one file per page and language (`PRK-ar.md` is the parking-permit page in Arabic), plus the two fee tables linked from the site | 26 | 11.2, 11.5 |

### chatbot/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `ruti-bot-log.csv` | Conversation export from "Ruti", a chatbot on three business-licensing pages | 640 | 11.2, 11.4 |
| `ruti-setup-notes.md` | How Ruti was built, by the clerk who built it | — | 11.2, 11.4 |

### governance/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `foi-log-2026.csv` | Freedom-of-information requests received in 2026 | 46 | 11.2, 11.4 |
| `foi-response-2026-09-ai.md` | The response to request FOI-2026-031 | — | 11.2, 11.4 |
| `accessibility-statement.md` | The website's accessibility statement as published | — | 11.4 |
| `accessibility-audit-2023-summary.md` | Summary of the 2023 accessibility audit and the tracker status | — | 11.4 |
| `information-security-procedure-2022-extract.md` | Procedure IS-07 on external services and embedded scripts | — | 11.2, 11.4 |

### procurement/

| File | What it is | Lessons |
|---|---|---|
| `procurement-procedure-extract.md` | The municipality's plain-language summary of when a tender is needed | 11.1, 11.4 |
| `civictalk-proposal.md` | CivicTalk's proposal for "Givat Oren Answers" | 11.1, 11.4 |
| `email-thread-2026-10.md` | Emails between the chief of staff and CivicTalk (exported at the legal adviser's request) | 11.4 |
| `framework-catalogue-extract.md` | A framework-agreement catalogue for local authorities | 11.4 |

### hr/

| File | What it is | Lessons |
|---|---|---|
| `works-committee-letter-2026-11-11.md` | The works committee's letter to the director-general | 11.1, 11.4 |
| `moked-106-agreement-2019-extract.md` | Local agreement on Moked 106 work arrangements | 11.4 |

## What is not here

No recordings of calls, no resident names or ID numbers, no council protocols beyond the fee decision,
no legal opinions (ask the legal adviser), no CivicTalk demo on Givat Oren data, no data from Ruti's
platform beyond the export the clerk made, no residents' survey micro-data, nothing from the mayor.
Ask for what you need in your access request (lesson 11.1).
