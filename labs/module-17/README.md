# Module 17 lab files — Vantage Logistics

Everything you need to run the Vantage Logistics rescue: the brief, the data room, the people you talk to, an audit sheet for the spreadsheet track, two Track B scripts (discovery and the stop/keep audit), and (for the debrief only) the expert's deliverables. All people, organizations, vendors and data are fictional and synthetic. Israeli and EU laws are real and referred to by name; what they require of Vantage is for its general counsel, outside counsel and its licensed customs agents to say.

## What is in this folder

| Path | What it is | Lesson |
|---|---|---|
| `brief.md` | The engagement brief: how the board engaged you, the stated ask, money and authority, the two principals, the dates, access on day one, constraints | 17.1 |
| `data-room/` | Vantage's data room: start with [`INDEX.md`](data-room/INDEX.md). Board papers and the March deck; the former head of AI's register and handover note; the vendor's agreement, order forms, dashboard, model card, release notes and root-cause analysis; contracts, invoices, card lines and the programme's cost; licence and proxy exports; IT tickets and the incident record; exports of routes, overrides, fleet kilometres and fuel, warehouse overtime, customs pre-fills, the customs QA sample and queries, the customer portal; the works committee's letter and the collective agreement; key accounts and a customer's e-mail | 17.1–17.6 |
| `data-room/generate.py` and the `gen_*.py` files there | The seeded generator (Python standard library only): `python generate.py` rebuilds every data file byte for byte. Reading it spoils the engagement | — |
| `personas/` | The cast of nine ([README](personas/README.md)): roleplay prompts and pre-run transcripts | 17.1–17.6 |
| `audit-sheet.csv` | Track A: the nineteen lines of the stop/keep audit with May cost, seats billed and active, and open tickets filled in; empty columns for your evidence label, risk, rule, action, owner, contract step and saving | 17.5 |
| `discovery.py` | Track B: AI outside the register, the route tool by region and month, licences against invoices, how pre-fills are reviewed and the QA error rate, the incident's scope from the logs, the savings against telematics, payroll and contacts, the money; `--llm` labels the dispatchers' multilingual override reasons | 17.2, 17.3 |
| `audit.py` | Track B: the audit rules, the nineteen-line audit table joined from invoices, licences, tickets and contract terms, the money (inside 2027, once in effect, the 2028 run-rate), the incident scope; writes `out/audit.csv`; `--sheet` rebuilds `audit-sheet.csv` | 17.5 |
| `expert/` | The expert's deliverables for comparison in the debrief; open them only after your own ([README](expert/README.md)) | 17.6 |

## What each lesson uses

| Lesson | Files |
|---|---|
| 17.1 The call | `brief.md`; `data-room/company/`, `ai/ai-register-2027-03.csv`, `ai/handover-note-itai-barkan-2027-05-27.md`, `incident/INC-27-0518-01-record.md`, `vendor/tzir-order-forms.md`, `vendor/tzir-msa-extract.md`, `customers/gefen-email-2027-05-19.md`; personas Ilana and Ofer |
| 17.2 Discovery | `data-room/customs/`, `portal/`, `incident/`, `operations/`, `it/`, `finance/`, `vendor/`, `people/`, `ai/`; personas Dmitri, Rania, Tesfaye, Svetlana, Yaniv, Itai; `discovery.py` |
| 17.3 Diagnosis | Your memo; `operations/fleet-km-fuel-monthly.csv`, `operations/warehouse-overtime-weekly.csv`, `vendor/tzir-value-dashboard-2027-05.md`, `customs/brokerage-staffing-monthly.csv`, `portal/cs-contacts-weekly-2027.csv`, `finance/ai-programme-cost-2027.csv`; personas Ofer and Ilana |
| 17.4 The hard part | The March deck, the agreement, the works committee's letter and the collective agreement, the model card, the tickets; personas Tesfaye, Rania, Ofer |
| 17.5 Decide | `audit-sheet.csv` or `audit.py`; invoices, licences, contracts, the incident files, the pre-fill and portal logs, customs queries; personas Orit, Yaniv, Dmitri |
| 17.6 Readout | Your deliverables; personas Ofer and Ilana; `expert/` |

No simulation has a Vantage preset yet. The lessons link Harbor & Pine's presets of the ROI defender (17.3), the risk register tester (17.4), the incident tabletop (17.5) and the steering committee (17.6) to practise the moves; every lesson works without them.

## Track A — no code

1. Open the CSV files in Excel, Google Sheets or LibreOffice Calc. In Excel use *Data → From Text/CSV* and choose *65001: Unicode (UTF-8)*; files contain Hebrew, Arabic, Russian, Amharic and English, and commas inside quotes. Import `invoice_key` as text, or Excel will drop its leading letters and zeros.
2. **17.2, the incident:** in `customs/declarations-prefill-2027-05.csv` add `=IF(J2<>D2,1,0)` (document owner differs from the declaring customer) and pivot it by `model_version` and `status`. In `portal/document-access-log-2027-05.csv` add the document's owner with `=XLOOKUP(F2,'document-index'!A:A,'document-index'!B:B)` and the record count the same way; filter rows where the viewer differs from the owner; split before and after 19 May.
3. **17.2, the review:** median of `review_seconds`, share under 30, share with `fields_edited` = 0; in `customs/qa-sample-2027-04.csv` count `material_error` = Y.
4. **17.2, the regions:** in `operations/route-daily-by-depot.csv` pivot `routes_dispatched_as_planned` and `routes` by month (first seven characters of `date`) and `region`, and divide; do the same for `late_stops` / `stops` in the South.
5. **17.3, the effects:** km per stop by region and month from `operations/fleet-km-fuel-monthly.csv`, December–May against November–April a year earlier; average weekly `overtime_hours` and `overtime_cost_ils` per distribution centre before and after 3 January 2027, and the ratio of the two ratios.
6. **17.5, the audit:** in a copy of `audit-sheet.csv` fill the empty columns with the rules from 17.4, then sum `saving_month_ils` by the month each saving starts.

## Track B — Python

Set up the field kit once ([instructions](../common/README.md)): Python 3.12 or newer and `pip install -r ../common/requirements.txt`. No extra packages. From this folder:

```bash
python discovery.py             # 17.2-17.3: the discovery numbers, no AI
python discovery.py --llm       # + an LLM labels the override reasons (30 distinct texts)
python audit.py                 # 17.5: the audit table, the money and the incident scope, no AI
python audit.py --sheet         # also rebuilds audit-sheet.csv
```

The provider and model for `--llm` come from `FIELDKIT_PROVIDER`, `FIELDKIT_MODEL` and your provider's key variable (see the [field kit README](../common/README.md)); every call goes through `fieldkit.llm.complete` and is cached in `.fieldkit-cache/`. `FIELDKIT_PROVIDER=mock` runs it without a key (the labels are meaningless, but the pipeline is proven). On Windows, if Hebrew prints as `?`, run `$env:PYTHONIOENCODING = "utf-8"` first. The scripts read the data room by relative path and make no network request except the LLM call; `audit.py` writes `out/audit.csv` (delete the folder when you are done).

Python is worth it in this module because the incident's scope and the audit are joins of several exports that keep changing — the vendor sends new logs, new invoices arrive, another mismatch appears — and both must be re-run with identical rules until the incident closes and the last notice takes effect. The LLM is a second opinion on free text, never the decision.

**What is real.** Every number the two scripts print reproduces exactly from the data room (seed 20270606): 70 mismatched declarations (63 before the fix, 7 after), 47 submitted, 30 cross-customer opens of 22 documents, 2,462 records of individuals in opened manifests, a 7.0% material error rate in the QA sample, 107 of 334 route seats active, ₪7.51M of 2027 cost against ₪5.2M, about ₪0.76M of evidenced savings, ₪340,620 saved inside 2027 by the audit.

Checked on 3 November 2026 with Python 3.14 and the versions pinned in `../common/requirements.txt`, end to end with `FIELDKIT_PROVIDER=mock`. The card's US$ lines use the issuer's monthly conversion recorded in the data; the course's reference rate is ₪3.136 per US$ (Bank of Israel representative rate, 2 November 2026).
