# Module 3 lab files — From findings to a funded portfolio

Everything module 3 uses beyond the shared Harbor & Pine data room. The data room itself is in `../common/harbor-and-pine/` (start with its [INDEX](../common/harbor-and-pine/INDEX.md)); it comes with this download. All people and companies are fictional and all data is synthetic.

## What is in this folder

| File | What it is | Lesson |
|---|---|---|
| `opportunity-map.csv` | Opportunity map, one row per candidate (one example row) | 03.1 |
| `use-case-scorecard.csv` | Fast screen and score, one row per candidate (one example row: a "stop") | 03.3, 03.4 |
| `group-roleplay.md` | The meeting prompt that lets one LLM chat play Yoav, Michal, Ronit and Samir together; scene A is the scoring workshop, scene B the alignment session | 03.5, 03.6 |
| `scoring-workshop-transcript.md` | Pre-run scoring workshop (26 Nov 2026), for learners who don't roleplay | 03.5 |
| `alignment-session-transcript.md` | Pre-run leadership alignment session (10 Dec 2026), for learners who don't roleplay | 03.6 |
| `roi-model.csv` | ROI model in the finance template's shape: costs and benefits by year, ledgers, labels, gates (example rows) | 03.7, project |
| `roi_model.py` | Track B: pilot economics, claims netted on four ledgers, three scenarios with NPV and payback, sensitivity, the peak-capacity check | 03.7 |
| `roi-model-harbor-solution.csv` | The filled Harbor & Pine model written by `roi_model.py --csv` (a solution file: build your own first) | 03.7 |

Lesson 03.2, 03.8 and 03.9 need no files beyond the data room, the personas in `../common/harbor-and-pine/personas/` and the templates linked from each lesson. The one-to-one with the CEO in 03.9 uses his persona and his pre-run transcript in the data room.

## Simulations

Three simulations go with this module. They open in the course, and each lesson works without them.

- `portfolio-sorter` with the Harbor & Pine preset (03.4): lock criteria, score nine cards, net error costs, ask the teams, see the hidden truths.
- `pilot-economics` with the Harbor & Pine preset (03.7): monthly net value, net hours and breakeven of the drafts pilot.
- `roi-defender` with the Harbor & Pine preset (03.7): net the sponsor's seven claims across four ledgers and find the number that survives the CFO.

## Track A — no code

1. Open the CSV files in Excel, Google Sheets or LibreOffice Calc. In Excel use *Data → From Text/CSV* and choose *65001: Unicode (UTF-8)*, or Hebrew text will not display.
2. Fill `opportunity-map.csv` and `use-case-scorecard.csv` one row per candidate; delete the example row when you start, or keep it as a model.
3. For the ROI model, copy `roi-model.csv` into a spreadsheet and add formulas: net per claim = claimed + adjustments; expected cash = measured + directional cash rows; NPV with `=NPV(12%, year1:year3) + year0`. Change one input at a time to build the sensitivity table.
4. Group roleplays: follow `group-roleplay.md`. Feedback with the [coach prompt](../common/coach-prompt.md).

## Track B — Python

Set up the field kit once ([instructions](../common/README.md)): Python 3.12 or newer and `pip install -r ../common/requirements.txt`. No API key is needed in this module: the script makes no LLM calls and no network requests. From this folder:

```bash
python roi_model.py                                       # 03.7: the whole model, printed
python roi_model.py --csv my-model.csv                    # also write the filled model as CSV
```

The script reads the customer-service cost from `company/finance-summary.csv` in the data room, uses `fieldkit.cost` (`pilot_value`, `token_cost`, `breakeven_months`, `npv`) and keeps every assumption in `INPUTS` and `CLAIMS` at the top, so you can change one and re-run. Python is worth it here because a sensitivity table is the same model run many times: one changed input recomputes every scenario, NPV and sensitivity line in a second, which is slow and error-prone by hand.

Checked on 2 November 2026 with Python 3.14.3, pandas 3.1.0 and tabulate 0.10.0 (the versions pinned in `../common/requirements.txt`). Token prices in the script are the simulation's examples (US$3 and US$15 per million); check your provider's pricing page before you quote a cost.
