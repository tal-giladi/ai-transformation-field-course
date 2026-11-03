# Atlas & Rowe — data room

Atlas & Rowe, Advocates is a Tel Aviv commercial law firm: 90 lawyers (26 partners, 64 associates),
Hebrew and English work product, fees of about ₪151M in 2025. The managing partner hired you as an
outside consultant from Sunday 15 November 2026 (see `../brief.md`). This folder is what the firm gave
you under your confidentiality undertaking: billing and HR extracts, IT logs, policies, a client's
guidelines, the vendor's documents, the knowledge bank's index and the research corpus exported for
the vendor's proof of concept.

Everything here is fictional and synthetic: the firm, its people, its clients, the vendor and every
ruling. **The rulings, memos and clause notes in `knowledge/` were written for this course; they are not
Israeli law and cite no real case.** Client names are replaced by codes (`C-014` and so on), except
Carmel Retail Group, which agreed to be named and to meet you. The consultant never sees client files.

## How to open

**Spreadsheet (Track A).** CSV files are UTF-8 and contain Hebrew, English, some Arabic and Russian. In
Excel use *Data → From Text/CSV* and pick *65001: Unicode (UTF-8)*; Google Sheets and LibreOffice
detect it. Narratives contain commas inside quotes: import, don't paste. Markdown (`.md`) files open in
any text editor.

**Python (Track B).**

```python
from fieldkit.data import data_room, load
room = data_room("module-12")
time = load(room / "billing" / "time-entries-2026-q3.csv")
```

**Rebuilding.** `generate.py` (Python 3.12+, standard library only; the text and logic are split across
`textbank.py`, `common.py`, `firm.py`, `activity.py`, `signals.py`, `corpus.py`, `km.py`, `pilot.py`,
`documents.py` and `documents2.py`) rebuilds every file here and in `../pilot/` byte for byte with
`python generate.py`. Reading the code spoils the engagement: finish module 12 first.

## Files

Lesson ids: 12.2 is module 12, lesson 2.

### firm/

| File | What it is | Lessons |
|---|---|---|
| `firm-profile.md` | Welcome-pack profile: practice groups, clients, billing, systems | 12.1 |
| `org-chart.md` | Partners by practice group, desks, management and support | 12.1, 12.2 |
| `partners-meeting-2026-10-22-minutes.md` | The partners' meeting where the AI proposal was discussed and the vote deferred | 12.1, 12.3, 12.6 |
| `finance-summary-2026.md` | Finance director's summary: fees, realisation by billing type and group, hours, compensation model, 2027 requests | 12.1, 12.3, 12.5 |

### people/ and billing/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `people/lawyers.csv` | All 90 lawyers: role, group, desk, year admitted, languages, billable target, hours 2025 and Jan–Sep 2026, standard rate | 90 | 12.2, 12.3 |
| `billing/matters.csv` | Every matter active in 2025–2026: client code, group, desk, responsible partner, billing type and terms, worked value and fees billed 2025 and Jan–Sep 2026 | 562 | 12.3, 12.5 |
| `billing/time-entries-2026-q3.csv` | TimeLedger export, 1 Jul – 30 Sep 2026, Litigation, Tech & IP and the International desk: activity code, hours, narrative, billed and written-off hours, reason | 5,218 | 12.2, 12.3 |

Activity codes: `RES` research, `DRF` drafting, `REV` review, `COR` correspondence and calls, `MTG`
meetings, `CRT` court, `NEG` negotiation. Fixed-fee matters are not billed line by line.

### clients/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `clients.csv` | Clients with fees 2024, 2025 and Jan–Sep 2026, outside-counsel guidelines and their AI clause, next renewal | 140 | 12.3, 12.4 |
| `renewals-and-rate-negotiations.csv` | Finance's log of renewals, rate reviews and tenders, 2025–2026 | 16 | 12.2, 12.3, 12.4 |
| `carmel-nda-workstream.csv` | Carmel's NDAs by month, Jan 2024 – Oct 2026: count, turnaround, hours, pricing, fees | 34 | 12.3, 12.5 |
| `carmel-ocg-2026.md` | Carmel's outside-counsel guidelines, effective 1 October 2026 (extract) | — | 12.2, 12.4 |

### it/, finance/, surveys/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `it/proxy-ai-domains-2026-09-10.csv` | The proxy's daily log of AI sites by user, 1 Sep – 31 Oct 2026 (office and VPN traffic only) | 864 | 12.2, 12.4 |
| `it/dlp-alerts-2026.csv` | Data-loss-prevention alerts, Jan – Oct 2026 | 14 | 12.2, 12.4 |
| `finance/expense-claims-software-2026.csv` | Software subscriptions claimed as expenses, Jan – Oct 2026 | 86 | 12.2 |
| `surveys/ai-use-survey-2026-10.csv` | Anonymous survey on AI use, October 2026 (47 of 90 lawyers answered) | 47 | 12.2 |

### policies/, risk/

| File | What it is | Lessons |
|---|---|---|
| `policies/it-acceptable-use-2019.md` | The firm's IT acceptable-use policy (2019) | 12.2, 12.4 |
| `policies/engagement-letter-template-2023.md` | Standard engagement terms, sections 9–13 | 12.4 |
| `policies/draft-ai-policy-2026.md` | A partner's draft AI policy, circulated 29 October 2026, not approved | 12.4 |
| `risk/ethics-log-2026.csv` | The ethics partner's log of questions and incidents, 2026 | 12.2, 12.4 |
| `risk/pi-renewal-questionnaire-2027.md` | The professional-indemnity insurer's AI questions, due 15 January 2027 | 12.4, 12.6 |

### vendor/

| File | What it is | Lessons |
|---|---|---|
| `parshan-demo-deck.md` | The vendor's slides from the partners' demo, 8 October 2026 | 12.1, 12.4 |
| `parshan-order-form.md` | Draft order form (not signed) | 12.4 |
| `parshan-security-answers.md` | Answers to IT's security questions | 12.4 |

Parshan AI is a fictional vendor. Real legal-AI products are named only in the lessons, as the market.

### km/, knowledge/, research/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `km/precedent-bank-index.csv` | Index of Mikbatz, the precedent bank: type, group, uploaded, last reviewed, status, uses in the last 12 months | 1,180 | 12.2, 12.3, 12.5 |
| `km/km-curation-proposal-2024.md` | The head of KM's 2024 proposal to review the bank (deferred) | — | 12.3, 12.5 |
| `knowledge/corpus/*.md` | The 78 research documents Tamar exported for the vendor's proof of concept: fictional rulings (`FCR-`), firm memos (`ARM-`) and clause notes (`ARP-`), with numbered paragraphs (¶) | 78 files | 12.5 |
| `knowledge/corpus-all.md` | The same 78 documents in one file, for uploading to a chat tool | — | 12.5 |
| `knowledge/corpus-index.csv` | One row per corpus document: type, title, date, topic, language, court, author, paragraphs | 78 | 12.5 |
| `research/memo-non-compete-draft-v2.md` | A research memo draft with the reviewers' comments, exported on request | — | 12.2, 12.4 |

## What is not here

No client files, no emails, no partner points or pay, no 2025 time entries, no time entries for
Corporate (outside the International desk), Real estate, Banking or Employment, no phone or home
traffic (the proxy sees only office and VPN traffic), no record of what was typed into AI tools, no
legal opinions (ask the ethics partner). Ask for what you need in your access request (lesson 12.1).
