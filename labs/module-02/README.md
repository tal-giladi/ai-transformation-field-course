# Module 2 lab files — Discovery that finds the real work

Everything module 2 uses beyond the shared Harbor & Pine data room. The data room itself is in `../common/harbor-and-pine/` (start with its [INDEX](../common/harbor-and-pine/INDEX.md)); it comes with this download, and so do the personas and their pre-run transcripts in `../common/harbor-and-pine/personas/`. All people and companies are fictional and all data is synthetic.

## What is in this folder

| File | What it is | Lesson |
|---|---|---|
| `stakeholder-map.csv` | Stakeholder map, one row per person (one example row) | 02.1 |
| `observation-notes.md` | Sit-in notes: one hour each with two support agents, 17 Nov 2026 (for learners who cannot observe real work) | 02.3 |
| `task-inventory.csv` | Task inventory, one row per task (one example row) | 02.3 |
| `baseline.py` | Track B: volumes, first response four ways, the WISMO share from five signals, a random sample, where agent time goes, the delivery promise and the contact wave after container delays | 02.4 |
| `data-profile.csv` | Data profile checks, one row per check per dataset (one example row) | 02.5 |
| `profile_data.py` | Track B: profiles tickets, emails, the claims log, both catalogues, the ETA sheet and the WhatsApp tally for AI-readiness | 02.5 |
| `readiness-assessment.csv` | Readiness findings log (one example row) | 02.6 |

Lessons 02.2 and 02.7 need no files beyond the data room, the personas, the [coach prompt](../common/coach-prompt.md) and the templates each lesson links.

## Track A — no code

1. Open the CSV files in Excel, Google Sheets or LibreOffice Calc. In Excel use *Data → From Text/CSV* and choose *65001: Unicode (UTF-8)*, or Hebrew, Arabic and Russian text will not display.
2. Fill the four spreadsheet templates here; delete the example row when you start, or keep it as a model.
3. 02.4: timestamps end in a time-zone offset (`+03:00`); take the first 19 characters before converting. Working hours with a Friday–Saturday weekend: `NETWORKDAYS.INTL` with weekend code `7`. The phone log is in UTC (the `Z`): add 3 hours in summer, 2 hours from 25 October 2026.
4. 02.4 and 02.5: for the WhatsApp tally, add a column that groups the agents' `topic` labels (44 of them, in four languages) into tasks, then pivot.
5. Roleplays (02.2): paste a persona's prompt into any LLM chat ([how](../common/persona-format.md)); feedback with the [coach prompt](../common/coach-prompt.md).

## Track B — Python

Set up the field kit once ([instructions](../common/README.md)): Python 3.12 or newer and `pip install -r ../common/requirements.txt`. No API key is needed in this module: the scripts make no LLM calls and no network requests. Then, from this folder:

```bash
python baseline.py        # 02.4: the baseline sheet's numbers
python profile_data.py    # 02.5: data profiles for six datasets
```

Both import the shared helpers from `../common/fieldkit/` (`fieldkit.data`, `fieldkit.baseline`, `fieldkit.profile`) and read the data room by relative path. On Windows, if Hebrew, Arabic or Russian text prints as `?`, run `$env:PYTHONIOENCODING = "utf-8"` in PowerShell first.

Python is worth it here because baselines and profiles are re-run every month on fresh exports, the working-hours calculation and the three-file container join are slow and error-prone in a spreadsheet, and a script makes every number in the memo reproducible.

Checked on 2 November 2026 with Python 3.14.3 and pandas 3.1.0 (the versions pinned in `../common/requirements.txt`).
