# Vantage Logistics — data room

Vantage Logistics is an Israeli logistics and freight-forwarding group: about 1,200 people in four regions (North, Centre, South and Europe), trucking, warehousing and customs brokerage. You are its interim AI lead for 30 days from Sunday 6 June 2027, engaged by the board (see `../brief.md`). This folder is what the board secretary, Finance, IT, Operations, the customs brokerage, Customer Service and Legal gave you in your first week: the board papers, the former head of AI's register and handover note, the vendor's documents and dashboard, contracts and invoices, licence and proxy exports, the IT tickets and the incident record, operational exports for routes, fleet, warehouses, customs declarations and the customer portal, and the letters that matter.

Everything here is fictional and synthetic: the company, its people, customers, vendors and systems. Real Israeli and EU laws are referred to by name; read them in their current version, and route legal questions to Vantage's general counsel (who is also its privacy protection officer), its licensed customs agents and outside counsel. Customers appear by code and company name; private individuals never appear by name (the portal export counts records, it does not contain them).

## How to open

**Spreadsheet (Track A).** CSV files are UTF-8 and contain Hebrew, Arabic, Russian, Amharic and English. In Excel use *Data → From Text/CSV* and pick *65001: Unicode (UTF-8)*; Google Sheets and LibreOffice detect it. Free-text fields contain commas inside quotes: import, don't paste. Markdown (`.md`) files open in any text editor.

**Python (Track B).**

```python
from fieldkit.data import data_room, load
room = data_room("module-17")
decl = load(room / "customs" / "declarations-prefill-2027-05.csv")
```

Some exports keep identifiers with leading letters and numbers that look like numbers (`invoice_key`); read them with `pd.read_csv(..., dtype=str)`. `discovery.py` and `audit.py` in the module folder show one way.

**Rebuilding.** `generate.py` (Python 3.12+, standard library only; the `gen_*.py` files in this folder are its parts) rebuilds every file here byte for byte with `python generate.py`. Reading it spoils the engagement: finish module 17 first.

## Files

Lesson ids: 17.2 is module 17, lesson 2.

### company/ and correspondence/

| File | What it is | Lessons |
|---|---|---|
| `company/company-profile.md` | The group in one page, June 2027 | 17.1 |
| `company/org-chart.md` | Who runs what, the board's audit committee, the works committee | 17.1, 17.4 |
| `company/board-minutes-2027-06-03-extract.md` | The board's special session that engaged you, with its questions | 17.1, 17.6 |
| `company/board-deck-ai-programme-2027-03-25.md` | The former head of AI's board update, March 2027 | 17.1–17.4 |
| `company/budget-2027-ai-and-savings.md` | The 2027 AI programme budget and the AI savings booked in the operating budget | 17.1, 17.3, 17.5 |
| `company/delegation-of-authority-extract.md` | Who may sign what | 17.2, 17.4 |
| `correspondence/operations-emails-2027.md` | E-mails between the COO and the customs brokerage | 17.2, 17.3 |
| `correspondence/incident-emails-2027-05.md` | The vendor's "contained" e-mail, the CEO's reply, the resignation | 17.2, 17.5 |

### ai/ and vendor/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `ai/ai-register-2027-03.csv` | The former head of AI's register of AI systems | 8 | 17.1, 17.2, 17.5 |
| `ai/handover-note-itai-barkan-2027-05-27.md` | His handover note | — | 17.1, 17.2 |
| `ai/tzir-route-model-card.md` | The route model's vendor model card | — | 17.2, 17.5 |
| `ai/forecast-backtest-2027-04.md` | The in-house warehouse forecast's back-test | — | 17.3, 17.5 |
| `vendor/contracts-ai.csv` | Contracts with AI vendors and vendors whose products include AI or feed it | 11 | 17.2, 17.5 |
| `vendor/tzir-msa-extract.md` | Clauses of the Tzir master agreement | — | 17.2, 17.4, 17.5 |
| `vendor/tzir-order-forms.md` | The three Tzir order forms | — | 17.2, 17.5 |
| `vendor/tzir-value-dashboard-2027-05.md` | The vendor's value dashboard and its methodology | — | 17.3 |

### operations/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `route-daily-by-depot.csv` | Routes, routes planned in Tzir Route, dispatched as planned, overridden, stops, kilometres (naive baseline, plan, actual) and late stops per depot and working day, October 2026 – 3 June 2027 | 1,760 | 17.2, 17.3, 17.5 |
| `dispatcher-overrides-2027.csv` | Overrides where the dispatcher entered a reason, from 10 January 2027 | 994 | 17.2, 17.5 |
| `fleet-km-fuel-monthly.csv` | Telematics kilometres, stops, fuel litres and cost by region and month, January 2025 – May 2027 | 116 | 17.3 |
| `warehouse-overtime-weekly.csv` | Pallets, hours, overtime and agency hours and cost per week at the two distribution centres, July 2026 – May 2027 | 96 | 17.3, 17.5 |

### customs/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `declarations-prefill-2027-05.csv` | Every import declaration pre-filled by Tzir Docs, 1 May – 3 June 2027: version, invoice number and matching key, whose document was matched, the tariff-code source, the agent, seconds on the approval screen, fields edited, submission, status | 5,635 | 17.2, 17.5 |
| `qa-sample-2027-04.csv` | The customs compliance team's re-check of 400 pre-filled declarations from April | 400 | 17.2, 17.3, 17.5 |
| `customs-queries-2027.csv` | Queries from the customs houses, February – June 2027 | 35 | 17.2, 17.5 |
| `brokerage-staffing-monthly.csv` | Licensed agents, frozen posts, declarations, overtime and the KPI target by month | 17 | 17.3 |

### portal/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `assist-sessions-2027.csv` | Tzir Assist sessions in the customer portal, 15 March – 3 June 2027 | 2,135 | 17.2, 17.3 |
| `document-access-log-2027-05.csv` | Every view or download of a document in the portal, 1 May – 3 June 2027 | 1,812 | 17.2, 17.5 |
| `document-index-2027-05.csv` | The documents in that log: owner, type, file, personal-data fields, record count | 1,804 | 17.2, 17.5 |
| `cs-contacts-weekly-2027.csv` | Customer-service contacts per week and channel, January – May 2027 | 66 | 17.3 |

### finance/ and it/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `finance/ap-invoices-ai.csv` | Supplier invoice lines for AI and related contracts, October 2026 – May 2027 | 121 | 17.2, 17.5 |
| `finance/card-and-expense-ai-2027.csv` | Corporate-card and expense lines booked to software and online services, January – May 2027 | 25 | 17.2 |
| `finance/ai-programme-cost-2027.csv` | Cost centre 7700-AI: budget, actual to May and forecast to December, by line and month | 132 | 17.3, 17.5 |
| `it/licence-usage-2027-05.csv` | Seats billed, assigned and active in the last 30 days per system and region, 31 May 2027 | 20 | 17.2, 17.5 |
| `it/proxy-ai-hosts-2027-q2.csv` | Proxy log, weekly totals per department and host for AI, translation and AI-vendor hosts, April – May 2027 | 126 | 17.2 |

### incident/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `INC-27-0518-01-record.md` | The incident record as it stands on 3 June | — | 17.1, 17.2, 17.5 |
| `tzir-rca-2027-05-28.md` | The vendor's root cause analysis | — | 17.5 |
| `tzir-release-notes-4.2.md` | The vendor's release notes for 2 May | — | 17.5 |
| `it-tickets-ai.csv` | IT tickets for AI systems and their feeds, October 2026 – June 2027 | 150 | 17.2, 17.5 |

### people/ and customers/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `people/staff-directory-extract.csv` | Managers, owners and the people the AI programme depends on | 22 | 17.1, 17.5 |
| `people/works-committee-letter-2027-03-03.md` | The works committee's letter (Hebrew, with HR's translation) | — | 17.2, 17.4 |
| `people/collective-agreement-extract.md` | Clause 14 of the collective agreement (technology) | — | 17.4 |
| `customers/key-accounts.csv` | The top 20 accounts, revenue, contract or tender dates | 20 | 17.2, 17.6 |
| `customers/gefen-email-2027-05-19.md` | A key customer's e-mail after the incident | — | 17.1, 17.5 |

## What is not here

No personal data of individuals (the portal index counts records), no model code, no vendor logs beyond the exports, no legal opinions, no correspondence with the customs authorities or the Privacy Protection Authority, no internal audit reports, no HR files. Nothing from the former head of AI's mailbox except what he copied to others. Ask for what you need in your access request (lesson 17.1); some of it only people can tell you (`../personas/`).
