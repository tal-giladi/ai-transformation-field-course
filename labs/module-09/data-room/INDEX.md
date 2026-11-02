# Meridian Mutual — data room

Meridian Mutual Insurance Company Ltd. is a mid-size Israeli insurer (motor, home, health and travel;
about 1,050 employees; about 36,000 non-bodily-injury claims a year). You joined on Sunday
1 November 2026 as Head of AI Transformation, reporting to the COO, with the board's risk management
committee above you. This folder is what you were given, or asked for, in your first weeks.

Everything here is fictional and synthetic: the company, the people, the claimants, the vendor.
Claims data covers claims reported 1 November 2024 – 31 October 2026 as exported on Wednesday
4 November 2026, unless a file says otherwise. Personal identifiers were removed or pseudonymised by
BI and the scanning room before the export, at the DPO's request.

## How to open

**Spreadsheet (Track A).** CSV files are UTF-8 and contain Hebrew, Arabic and Russian text. In Excel
use *Data → From Text/CSV* and pick *65001: Unicode (UTF-8)*; Google Sheets and LibreOffice detect it.
Use filters and pivot tables. Markdown (`.md`) and text (`.txt`) files open in any editor.

**Python (Track B).** Scripts in the module folder use the field kit:

```python
from fieldkit.data import data_room, load
room = data_room("module-09")
claims = load(room / "claims" / "claims_register_sample.csv")   # *_at and *_date columns parsed as Israel time
```

**Times.** Timestamps are Israel local time with the UTC offset (`+03:00` in summer time, `+02:00`
in winter time). Some files carry dates only.

**Sample.** The claims register is a sample: every 40th claim number. Multiply counts by 40 for
company volumes. The motor extract, the SIU case log and the complaints log are complete, not samples.

**Rebuilding.** `generate.py` (Python 3.12+, standard library only) rebuilds every generated file
byte for byte (`python generate.py`). You do not need to run it. Reading it spoils the engagement:
finish module 9 first.

## Files

Lesson ids: 09.2 is module 9, lesson 2.

### company/

| File | What it is | Lessons |
|---|---|---|
| `meridian-at-a-glance.md` | Welcome pack: lines, claims organisation, seasons, systems | 09.1 |
| `org-chart.md` | Management chart and the claims division's headcount | 09.1, 09.2 |
| `finance-summary.md` | CFO's planning figures: claims paid, cost per hour, how cases are judged, budget | 09.3, 09.6 |

### plans/ and reports/

| File | What it is | Lessons |
|---|---|---|
| `plans/pilot-proposal-2026-11.md` | The COO's draft proposal: the winter pilot, targets, budget | 09.1, 09.3, 09.6 |
| `reports/claims-kpi-dashboard-2026-10.md` | BI's monthly claims KPI dashboard (whole company) with definitions | 09.1, 09.3 |

### claims/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `claims_register_sample.csv` | Kalanit Claims register, every 40th claim: line, type, centre, region, postal area, channel, language of correspondence, interpreter flag, age band, dates from loss to closure, decision, amounts, document-request rounds, SIU flag, Fraud Insight fields, Smart Intake flag, handler | 1,827 | 09.2, 09.3 |
| `doc_requests.csv` | Kalanit document-request letters for the sampled claims: round, date sent, documents asked for, how many were on the standard list, when everything asked for had arrived | 2,960 | 09.2, 09.3 |
| `crm_contacts.csv` | CRM "Kesher" export (the tool keeps six months: May–October 2026) for the sampled claims that came in directly (not through an agent): first notice, status calls, handler notes, in four languages | 557 | 09.2, 09.3 |
| `motor_claims_2026-07_to_10.csv` | Every motor claim registered 1 July – 31 October 2026 (requested from BI for the review), with the Fraud Insight score, band and factors, SIU referral and outcome | 5,536 | 09.4 |

### finance/, siu/, complaints/, ops/

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `finance/claim_payments.csv` | ERP payments for the sampled claims: payee (claimant, garage, assessor), amount, approval, payment date | 2,716 | 09.3 |
| `siu/siu_case_log.csv` | The SIU's own case log, every case opened since 1 July 2025: source of the referral, score, investigator, status, outcome, "amount saved" as the SIU reports it | 1,637 | 09.2, 09.4 |
| `complaints/complaints_log_2026.csv` | Public complaints officer's log, January–October 2026: topic code, language, how it arrived, summary in Hebrew | 349 | 09.2, 09.4 |
| `ops/intake-time-study-2026-10.csv` | Claims QA's time study of intake in October 2026: minutes sorting, keying, checking Smart Intake's pre-fill, and finding missing documents, with observer notes | 120 | 09.3, 09.5 |

### policies/ and governance/

| File | What it is | Lessons |
|---|---|---|
| `policies/claims-manual-excerpt.md` | Claims manual v7.2, chapters on intake, documents and the SIU | 09.2, 09.3, 09.4 |
| `policies/ai-policy-2026.md` | Meridian's AI policy (board, June 2026) | 09.1, 09.4 |
| `governance/risk-committee-minutes-2026-06-15.md` | Risk committee minutes: AI policy, management statement, Kalanit 9.4 in the IT portfolio | 09.1, 09.4, 09.6 |
| `governance/ai-inventory-2026-06.csv` | The AI inventory presented in June 2026 | 09.1, 09.4 |

### vendor/

| File | What it is | Lessons |
|---|---|---|
| `kalanit-claims-9.4-release-notes.md` | Release notes for Kalanit Claims 9.4 (go-live 6 September 2026) | 09.1, 09.4 |
| `kalanit-agreement-excerpt.md` | The software and maintenance agreement: releases, configuration, data use, liability, sub-processors | 09.4 |
| `fraud-insight-config-export.csv` | Fraud Insight configuration exported from Kalanit: factors, weights, thresholds | 09.4 |
| `risk-areas-v3.csv` | The "risk areas" list the configuration refers to | 09.4 |
| `email-kalanit-fraud-insight-pro-2026-10-20.md` | The account executive's email to the COO | 09.1, 09.4 |

### extraction/

The intake documents for the pilot (lesson 09.5) and the vendor's output on the same documents.

| File | What it is | Rows | Lessons |
|---|---|---|---|
| `documents/D001.txt` … `D240.txt` | 240 intake documents received September–October 2026, as the OCR text layer the document system stores: claim forms, garage and contractor invoices, police confirmations, assessor reports, medical invoices from abroad, private clinic receipts; Hebrew, Arabic, Russian, English | 240 files | 09.4, 09.5 |
| `documents_index.csv` | One row per document: type, document language, line, claimant's language, region, age band, capture channel (app photo, email PDF, branch scanner, fax), handwritten or typed | 240 | 09.5 |
| `gold_fields.csv` | The values two Claims QA staff keyed and verified for each document's fields, in standard formats (dates YYYY-MM-DD, amounts with a dot) | 788 | 09.5 |
| `smart_intake_output.csv` | Kalanit Smart Intake's output on the same 240 documents (a batch run Kalanit did for Meridian in October), with confidence scores | 833 | 09.4, 09.5 |
