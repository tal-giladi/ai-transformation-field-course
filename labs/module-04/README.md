# Module 4 lab files — Guardrails you can ship in week two

Everything module 4 uses beyond the shared Harbor & Pine data room. The data room itself is in `../common/harbor-and-pine/` (start with its [INDEX](../common/harbor-and-pine/INDEX.md)); it comes with this download, and so do the personas and their pre-run transcripts in `../common/harbor-and-pine/personas/`. All people and companies are fictional and all data is synthetic.

## What is in this folder

| File | What it is | Lesson |
|---|---|---|
| `tools-and-data-classes.csv` | Tool facts (training, retention, contract, location) and the tools × data-classes matrix (one example row) | 04.2 |
| `approved-restricted-use-list.csv` | Approved uses in three tiers and restricted uses (one example row each) | 04.2 |
| `vendor-ai-questionnaire.csv` | The ten-section questionnaire, one row per question, with columns for three vendors; Deskly's column partly filled as an example | 04.3 |
| `ai-inventory-tiering.csv` | Harbor & Pine's AI inventory with the facts the tier rule needs (14 rows) | 04.4 |
| `tier_inventory.py` | Track B: applies the tier rule and the DPIA triggers to the inventory and prints each row's tier and reasons | 04.4 |
| `risk-register.csv` | Risk register columns (one example row) | 04.5 |
| `regulatory-map.csv` | Regulatory map columns (one example row) | 04.6 |
| `ai-intake-register.csv` | Intake register columns (one example row) | 04.7 |

Lessons 04.1, 04.3 and 04.8 work mainly on documents in the data room: `it/it-policy-2021.md`, `vendors/deskly-ai-addon-terms.md`, `vendors/linguaflow-translation-dpa.md` and `vendors/chatnest-sales-deck.md`. Lesson 04.8's roleplay uses [Eitan Gross](../common/harbor-and-pine/personas/eitan-chatnest.md) (or his [pre-run transcript](../common/harbor-and-pine/personas/transcripts/eitan-chatnest.md)) and the [coach prompt](../common/coach-prompt.md). Lesson 04.5 links the risk-register-tester simulation; the lesson works without it.

## Track A — no code

1. Open the CSV files in Excel, Google Sheets or LibreOffice Calc. In Excel use *Data → From Text/CSV* and choose *65001: Unicode (UTF-8)*.
2. Each spreadsheet template has one example row from Harbor & Pine: keep it as a model or delete it when you start.
3. 04.4: in `ai-inventory-tiering.csv`, add a `tier` column and apply the rule from the lesson with a formula, for example in Google Sheets or Excel: High if `decides_about_people`="y", or `acts_without_person`="y" and `harm_if_wrong` is "money", "rights" or "safety", or `max_data_class`="S", or `max_data_class`="D" and `people_or_contacts_per_month`>1000 and `new_recipients`="y"; otherwise Medium if `max_data_class` is "D", or `reaches_outside`="y", or `max_data_class`="B" and `new_recipients`="y"; otherwise Low.
4. Roleplay (04.8): paste the persona's prompt into any LLM chat ([how](../common/persona-format.md)), then get feedback with the [coach prompt](../common/coach-prompt.md).

## Track B — Python

Set up the field kit once ([instructions](../common/README.md)): Python 3.12 or newer. `tier_inventory.py` uses only the Python standard library, so it runs even before you install the field kit's packages. No API key and no network access are needed in this module. From this folder:

```bash
python tier_inventory.py
python tier_inventory.py path/to/your-inventory.csv
```

It prints every row's tier with the conditions that produced it, any DPIA triggers, and a count of High, Medium and Low. On Windows, if dashes or Hebrew print as `?`, run `$env:PYTHONIOENCODING = "utf-8"` in PowerShell first.

Python is worth it here because the inventory is re-tiered every quarter and after every vendor change: the script applies the same rule every time, and changing one fact (a new recipient, a higher volume) shows at once which rows move.

Checked on 2 November 2026 with Python 3.14.3.
