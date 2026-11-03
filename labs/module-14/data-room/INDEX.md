# Lumen SaaS — data room

Lumen SaaS is a Tel Aviv software company of about 250 people. Its product, Lumen Shifts, does shift
scheduling, time clock and payroll prep for about 3,100 business customers in Israel, the EU and the US, on
Starter, Growth and Enterprise plans. You joined on Sunday 29 November 2026 as Head of AI Operations,
reporting to the VP Support (see `../brief.md`). This folder is what you were given access to in your first
week: customer and billing extracts, the Lumen Assist beta's logs, support tickets, IT's token list and audit
log, the help centre's history, policies, product documents and one customer's security questionnaire.

Everything here is fictional and synthetic: the company, its people, its customers and every message.

## How to open

**Spreadsheet (Track A).** CSV files are UTF-8 and contain Hebrew, English, Arabic and Russian. In Excel use
*Data → From Text/CSV* and pick *65001: Unicode (UTF-8)*; Google Sheets and LibreOffice detect it. Some text
fields contain commas inside quotes: import, don't paste. Timestamps are Israel local time. Markdown (`.md`)
files open in any text editor.

**Python (Track B).** The module's scripts read these files with the standard library:

```python
import csv
from fieldkit.data import data_room
room = data_room("module-14")
with (room / "assist-beta" / "tool-calls.csv").open(encoding="utf-8") as f:
    calls = list(csv.DictReader(f))
```

`fieldkit.data.load()` also works: these files are in Israel time without an offset, and `load()` reads them as Israel time.

**Rebuilding.** `generate.py` (Python 3.12+, standard library only; the logic is split across `common.py`,
`textbank.py`, `customers.py`, `beta.py`, `fleet.py`, `kb.py`, `stats.py`, `docs1.py`, `docs2.py` and
`docs3.py`) rebuilds every file here byte for byte with `python generate.py`. Reading the code spoils the
engagement: finish module 14 first.

## Files

Lesson ids: 14.2 is module 14, lesson 2.

### company/

| File | What it is | Lessons |
|---|---|---|
| `company-profile.md` | Welcome-pack profile: product, customers by plan and country, support, systems | 14.1 |
| `org-chart.md` | Executives and teams | 14.1, 14.2 |
| `board-update-2026-10.md` | The CEO's board update on Lumen Assist (extract) | 14.1, 14.3, 14.6 |
| `exec-staff-minutes-2026-11-25.md` | Executive staff minutes, the week before you started (extract) | 14.1 |
| `assist-beta-dashboard-2026-11.md` | Product's weekly beta dashboard | 14.1, 14.3 |

### customers/, people/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `customers/customers.csv` | Every account: plan, country, UI language, seats, billing, price, ARR, renewal date, admin email, beta flag, status | 3,217 | 14.2, 14.3 |
| `customers/enterprise-contracts.csv` | Enterprise contracts: seats, price, ACV, term, outage-credit clause, AI terms, account lead | 120 | 14.2, 14.4 |
| `customers/growth-renewals-2026.csv` | Annual Growth renewals, 1 Feb – 26 Nov 2026: active-user change over 90 days and outcome | 521 | 14.4 |
| `people/staff-directory.csv` | Lumen staff with department, title, start date, status and leaving date | 268 | 14.2 |
| `people/support-shifts.csv` | Support shifts, shift leads and the time they have for approvals | 11 | 14.4, 14.5 |

### assist-beta/

The closed beta of Lumen Assist, 11 October – 26 November 2026.

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `sessions.csv` | One row per conversation: customer, plan, language, intent, turns, outcome, CSAT, PII detector flags, prompt version | 1,599 | 14.2, 14.3 |
| `retrievals.csv` | Help-centre articles the agent retrieved per conversation, with rank and score | 2,768 | 14.2 |
| `tool-calls.csv` | Every tool call: requested and executed time, tool, customer, amount, target, status, the identity it ran as, note | 1,307 | 14.2, 14.3, 14.4 |
| `transcripts-sample.md` | Eleven conversation excerpts exported by Product for quality review | — | 14.2, 14.4, 14.5 |

Intents come from the product's classifier. Outcomes: `closed_by_customer`, `abandoned` (customer left),
`handoff` (customer chose "Talk to a person"), `ticket_created` (the agent opened a ticket).

### support/, billing/, support-kb/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `support/tickets.csv` | Deskly tickets, 11 Oct – 26 Nov 2026, all channels, with the linked Assist session and internal notes | 1,983 | 14.2, 14.3 |
| `billing/credits-ledger.csv` | Every credit, 2 Aug – 26 Nov 2026: amount, reason, note, issued by, channel, invoice run, status, reversal | 826 | 14.2, 14.3, 14.4 |
| `support-kb/help-centre-articles.csv` | Help-centre index: article, language, owner team, current revision, searchable by Assist | 96 | 14.2 |
| `support-kb/help-centre-revisions.csv` | Every published revision: when, by whom, team, change note | 253 | 14.2, 14.4 |
| `support-kb/articles/` | Three versions of article HC-214 | 3 files | 14.2 |

### it/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `it/api-tokens.csv` | Admin API service tokens: who created them, team, scopes, last used, expiry | 14 | 14.2, 14.4 |
| `it/admin-audit-log.csv` | Admin API and console write actions, 1 Sep – 26 Nov 2026: actor, token, user agent, source, action, customer, result | 1,778 | 14.2, 14.4 |
| `it/ai-inventory-2026-09.csv` | IT's register of AI systems, September 2026 | 3 | 14.2 |
| `it/saas-expenses-ai-2026.csv` | Card expenses for AI and automation services, Jan – Nov 2026 | 99 | 14.2 |
| `it/feature-flags-log.csv` | Changes to Lumen Assist's feature flags | 6 | 14.2, 14.4 |

### policies/, product/, legal/

| File | What it is | Lessons |
|---|---|---|
| `policies/credit-policy.md` | Who may credit how much; annual plans; reversal | 14.2, 14.4 |
| `policies/account-security-procedure.md` | 2FA resets and documents with staff data | 14.4, 14.5 |
| `policies/data-deletion-procedure.md` | Deletion requests, soft and hard delete | 14.4, 14.5 |
| `policies/help-centre-publishing.md` | Who may publish help-centre articles; translations | 14.2, 14.4 |
| `policies/ai-acceptable-use-2026.md` | The company's AI rules, February 2026 | 14.2, 14.4 |
| `product/assist-ga-design.md` | Product's design for general availability at Lumen Live | 14.1, 14.4 |
| `product/assist-system-prompt-v7.md` | The live system prompt (excerpt) | 14.4, 14.5 |
| `product/assist-incident-runbook.md` | What to do when the agent misbehaves | 14.4 |
| `product/widget-strings.csv` | The assistant widget's interface text in four languages | 14.4 |
| `legal/shaked-security-questionnaire-2026-11.md` | An Enterprise customer's AI questions, due 15 January 2027 | 14.4, 14.6 |
| `legal/customer-dpa-extract.md` | The standard customer data-processing terms (extract) | 14.4 |

## What is not here

No full conversation logs (the sample only), no model or vendor documents for the LLM API Lumen Assist uses,
no source code, no exports from workflow tools, no Enterprise usage data, no emails or Slack.
Ask for what you need in your access request (lesson 14.1).
