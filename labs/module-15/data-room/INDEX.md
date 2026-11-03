# Crescent Bank — data room

Crescent Bank is a mid-sized Israeli bank: about 4,000 people, 14 business units, 58 branches, about 1.1 million customers. You are the head of its new AI Centre of Excellence, reporting to the COO, from Sunday 3 January 2027 (see `../brief.md`). This folder is what the COO office, IT, Risk, Finance, Procurement and Information Security gave you in the first two weeks: the AI pilot register the COO office compiled from the units in December, the eval results the units reported, the Model Committee's queue and minutes, the model inventory, Model Risk Management's work plan, the AI policy, the bank's answers to the supervisor's AI-governance survey, IT's architecture notes, usage exports, card and expense lines, an extract of the proxy log, the AI contracts, the people who work on AI and the documents that set the budget.

Everything here is fictional and synthetic: the bank, its people, customers, vendors and systems. Real laws and Bank of Israel directives are referred to by name and number; read them in their current version, and route legal and regulatory questions to the bank's counsel, the Chief Compliance Officer and the CRO. Customers never appear; employees appear by name only where a manager would see them.

## How to open

**Spreadsheet (Track A).** CSV files are UTF-8 and contain Hebrew, Arabic, Russian and English. In Excel use *Data → From Text/CSV* and pick *65001: Unicode (UTF-8)*; Google Sheets and LibreOffice detect it. Free-text fields contain commas inside quotes: import, don't paste. Markdown (`.md`) files open in any text editor.

**Python (Track B).**

```python
from fieldkit.data import data_room, load
room = data_room("module-15")
reg = load(room / "ai" / "pilot-register-2026-12.csv")
```

The register is as the units typed it: unit names in English, Hebrew or as a code; dates in four formats; money as `248000`, `₪248,000` or `248k`. `load` parses columns whose names end in `_date` and turns the dates it cannot read into blanks, so read the register with `pd.read_csv(..., dtype=str)` instead; `discovery.py` and `triage.py` in the module folder show one way to clean it.

**Rebuilding.** `generate.py` (Python 3.12+, standard library only; the `gen_*.py` files in this folder are its parts) rebuilds every file here byte for byte with `python generate.py`. Reading it spoils the engagement: finish module 15 first.

## Files

Lesson ids: 15.2 is module 15, lesson 2.

### company/

| File | What it is | Lessons |
|---|---|---|
| `company-profile.md` | The bank in one page, January 2027 | 15.1 |
| `org-chart.md` | Who runs what, committees | 15.1, 15.4 |
| `board-minutes-2026-11-24-extract.md` | The board item where the ask was made and the CoE approved | 15.1, 15.3, 15.6 |
| `ai-programme-budget-2027.md` | The central AI programme budget for 2027 and its assumptions | 15.1, 15.3, 15.5 |
| `cfo-budget-review-2027-01-12.md` | The CFO's 15% savings proposal for AI | 15.2, 15.3, 15.5 |

### ai/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `pilot-register-2026-12.csv` | The COO office's AI pilot register, compiled from the units' submissions, December 2026 | 43 | 15.1–15.5 |
| `eval-summaries.csv` | Every evaluation the units reported: date, test items, languages, metric, value, threshold, who ran it | 42 | 15.2, 15.3, 15.5 |
| `assistant-usage-2026.csv` | Tzofen Assist admin export: seats, onboarded users, weekly active users, prompts and agent-studio sessions per department and week, May–December 2026 | 250 | 15.2, 15.5 |
| `intake-requests-2026.csv` | Requests for new AI tools that reached the COO office in 2026 and are not yet answered | 20 | 15.2, 15.4 |
| `architecture-notes.md` | IT Architecture's notes on the pilots it reviewed | — | 15.2, 15.4, 15.5 |

### governance/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `ai-policy-v1-2025.md` | The AI policy approved in June 2025 | — | 15.1, 15.4 |
| `model-committee-minutes-2026.md` | The Model Committee's 2026 minutes, AI items | — | 15.2, 15.4 |
| `model-review-queue-2026-12.csv` | AI submissions to the Model Committee and where each stands on 31 December 2026 | 19 | 15.2, 15.3, 15.4 |
| `model-inventory-2026-12.csv` | MRM's model inventory (all models in use, with materiality and Directive 369 phase-in status) | 142 | 15.2, 15.4 |
| `mrm-workplan-2027.md` | Model Risk Management's 2027 work plan: people, review slots, allocation | — | 15.2, 15.3, 15.4 |
| `bsd-ai-survey-response-2026-extract.md` | Extract of Crescent's answers to the Banking Supervision Department's AI-governance survey (2026) | — | 15.2, 15.4, 15.6 |

### branches/ and customers/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `branches/branch-faq-usage-2026-q4.csv` | Daily questions, answers with a source and thumbs-down per branch for the Branch staff FAQ, October–December 2026 | 2,046 | 15.2, 15.5 |
| `branches/branch-managers-forum-2026-11-minutes.md` | Northern branch managers' forum, 19 November 2026 | — | 15.2 |
| `customers/complaints-monthly-2026.csv` | Complaints received per month, unit and channel, with closing time | 240 | 15.3, 15.5 |

### finance/, procurement/, security/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `finance/card-and-expense-software-2026.csv` | Corporate-card lines and expense claims booked to "software and online services", 2026 | 124 | 15.2 |
| `procurement/vendor-contracts-ai.csv` | Contracts with AI vendors and with vendors whose products include AI: dates, renewal, notice, value, DPA, data location | 18 | 15.2, 15.3, 15.5 |
| `security/proxy-ai-hosts-2026-q4.csv` | Proxy log, daily totals per department and host for hosts categorised as AI or translation, October–December 2026 | 1,056 | 15.2 |

### people/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `ai-people-by-unit.csv` | Everyone who works on AI, by unit, role, employment and pilots (HR and unit heads, December 2026) | 46 | 15.3, 15.4, 15.5 |
| `staff-directory-extract.csv` | Directory extract: managers, owners and validators, with status | 38 | 15.2, 15.5 |

## What is not here

No customer data, no model code, no validation reports, no vendor documentation beyond the contracts list, no legal opinions, no correspondence with the Bank of Israel beyond the survey extract, no internal audit reports, no HR records of individuals. Nothing from personal devices. Ask for what you need in your access request (lesson 15.1); some of it only people can tell you (`../personas/`).
