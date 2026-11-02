# Northwind Outfitters — data room

Northwind Outfitters Ltd. sells outdoor and sports gear online across Israel: about 450 employees,
₪548M revenue in 2025, about 60,000 orders a month. The COO hired you as an outside consultant for 10
weeks from Sunday 8 November 2026 (see `../brief.md`). This folder is what Northwind gave you access to
in the first week, under the NDA and the data-processing agreement: exports, reports, policies,
contracts and logs.

Everything here is fictional and synthetic: the company, the people, the customers and the vendor.
Customer names, phone numbers and addresses were removed by BI before the extract (`[NAME]` in
messages).

## How to open

**Spreadsheet (Track A).** CSV files are UTF-8 and contain Hebrew, Arabic, Russian, English and some
Amharic text. In Excel use *Data → From Text/CSV* and pick *65001: Unicode (UTF-8)*; Google Sheets and
LibreOffice detect it. Messages contain commas inside quotes: import, don't paste. Markdown (`.md`)
files open in any text editor.

**Python (Track B).**

```python
from fieldkit.data import data_room, load
room = data_room("module-08")
contacts = load(room / "support" / "contacts.csv")   # *_at and *_date columns parsed as Israel time
```

**Times.** Israel local time with the UTC offset (`+03:00` in summer, `+02:00` from 25 October 2026).

**The 1% sample.** BI's standard extract is a random 1% of customers with *all* their orders, returns,
contacts and logged-in chatbot conversations, so that a customer's journey can be followed across
channels. Multiply counts by 100 for company totals. `support/written-tickets-2000.csv` is different:
2,000 written tickets drawn at random from the whole company for September–October 2026.

**Rebuilding.** `generate.py` (Python 3.12+, standard library only, text in `textbank.py`) rebuilds every
file byte for byte with `python generate.py`. Reading it spoils the engagement: finish module 08 first.

## Files

Lesson ids: 08.2 is module 8, lesson 2.

### company/

| File | What it is | Lessons |
|---|---|---|
| `company-profile.md` | Welcome-pack profile: business, customers, systems, service hours | 08.1 |
| `org-chart.md` | HR summary by unit, heads, team sizes; customer-service desks and language skills | 08.1, 08.2 |
| `board-update-2026-09.md` | Board minutes, 21 Sep 2026: the CEO's update on AI in customer service and the 2027 target | 08.1, 08.3, 08.6 |
| `kpi-report-2026-q2.md` | Customer Service KPI report, Q2 2026 (BI) | 08.1, 08.2, 08.3 |
| `kpi-report-2026-q3.md` | Customer Service KPI report, Q3 2026 (BI) | 08.1, 08.2, 08.3 |
| `finance-summary.md` | CFO's summary: cost of customer service, the 2027 draft, returns and refunds, how projects are judged | 08.3, 08.5, 08.6 |

### people/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `cs-headcount-2026.csv` | Agents on payroll at month end, contracts not renewed, resignations, hires, notes (Jan–Oct 2026) | 10 | 08.2, 08.3 |

### customers/ and orders/ (1% sample)

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `customers/customers-sample.csv` | `customer_id`, `joined_date`, `segment` (regular, trail_club, silver_trail), `site_language`, `city`, `marketing_opt_in` | 3,400 | 08.2, 08.3 |
| `orders/orders-sample.csv` | Orders placed 15 Mar – 31 Oct 2026: channel (web, app, phone, chat_assisted), main item, prices, promised date, delivery time, status | 4,598 | 08.2, 08.3 |
| `orders/returns.csv` | Every return of those orders: request, channel, reason code, opened or not, received, inspected, result, refund method, fees deducted, amount, refund date | 602 | 08.2, 08.3, 08.4 |

### support/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `contacts.csv` | Tikra helpdesk export for the 1% sample, 1 May – 31 Oct 2026: every conversation an agent handled (answered calls, email, web form, WhatsApp, chat). `channel`, `customer_id`, `order_id` (as typed), `language` (IVR choice or auto-detected), `category` (agent's choice), `tags`, `agent_id`, `queue_wait_sec`, `first_response_sec`, `handle_time_sec`, `after_contact_work_sec`, `status`, `csat`, `bot_session_id` | 2,075 | 08.2, 08.3 |
| `bot-sessions.csv` | Verbalo admin export for the same customers (when logged in; otherwise `customer_id` is blank): start, site and message language, the bot's intent, turns, outcome, billable resolution, thumbs, first message, last bot reply | 439 | 08.2, 08.3, 08.4 |
| `bot-transcripts-sample.md` | Eight full chatbot conversations, exported by IT | 8 | 08.2, 08.4 |
| `written-tickets-2000.csv` | 2,000 written tickets (email, web form, WhatsApp), 1 Sep – 31 Oct 2026, company-wide random extract: order facts, the customer's message and the agent's reply as sent | 2,000 | 08.3, 08.5 |
| `macros.csv` | The helpdesk's reply macros about returns, refunds and order status, with last editor and uses in the last 90 days | 9 | 08.2, 08.4 |

### policies/

| File | What it is | Lessons |
|---|---|---|
| `returns-page.md` | "Returns and exchanges" page on the website, as published | 08.2, 08.4 |
| `terms-of-sale-section-9.md` | Terms of sale, section 9 "Cancelling a purchase" | 08.2, 08.4 |
| `trail-club-terms.md` | Trail Club member terms, extract | 08.2, 08.4 |
| `warehouse-returns-sop.md` | SOP-WH-07, receiving and inspecting returns | 08.2, 08.3, 08.4 |

### vendor/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `verbalo-order-form.md` | The chatbot contract's order form (extract) | — | 08.1, 08.4 |
| `verbalo-demo-deck.md` | The vendor's proof-of-value results presented on 12 May 2026 | — | 08.1, 08.4 |
| `verbalo-demo-questions.csv` | The 40 questions behind the demo results | 40 | 08.4 |
| `verbalo-invoices.csv` | Monthly invoices June–October 2026 | 5 | 08.3, 08.4 |

### legal/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `contract-review-log.csv` | Legal counsel's log of contracts and reviews in 2026 | 8 | 08.2, 08.4 |
| `regulator-and-claims-log.csv` | Consumer Protection Authority inquiries, small claims and demand letters in 2026 | 14 | 08.2, 08.4, 08.6 |

## What is not here

No payroll detail, no full customer database, no live helpdesk or Verbalo access, no call recordings,
no legal memos (ask counsel), no 2025 contact data, no repeat-contact report (BI has never produced
one). Ask for what you need in your access request (lesson 08.1).
