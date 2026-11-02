# Module 1 lab files — Walking in

Everything module 1 uses beyond the shared Harbor & Pine data room. The data room itself is in `../common/harbor-and-pine/` (start with its [INDEX](../common/harbor-and-pine/INDEX.md)); it comes with this download. All people and companies are fictional and all data is synthetic.

## What is in this folder

| File | What it is | Lesson |
|---|---|---|
| `change-request-log.csv` | Empty change-request log (one example row) for the scope work | 01.3 |
| `data-room-first-read.csv` | Claims register for the first-day data-room read (one example row) | 01.5 |
| `first_read.py` | Track B: lists every CSV in a data room with rows, date range and blank cells | 01.5 |
| `avi-it-interview-transcript.md` | Pre-run interview with Avi Mizrahi (IT), for learners who don't roleplay | 01.6 |
| `shadow-ai-census.csv` | Census table, one row per tool × department (one example row) | 01.6 |
| `census.py` | Track B: AI use from the proxy log, extensions, expenses, email replies and the SaaS list, by department | 01.6 |
| `dana-hr-interview-transcript.md` | Pre-run interview with Dana Katz (HR), for learners who don't roleplay | 01.7 |
| `ai-inventory.csv` | AI inventory with all fields (one example row: an excluded system) | 01.7, project |

Lessons 01.1–01.4 need no files beyond the data room, the personas in `../common/harbor-and-pine/personas/` and the templates linked from each lesson.

## Track A — no code

1. Open the CSV files in Excel, Google Sheets or LibreOffice Calc. In Excel use *Data → From Text/CSV* and choose *65001: Unicode (UTF-8)*, or Hebrew, Arabic and Russian text will not display.
2. Fill the four spreadsheet templates here (`change-request-log.csv`, `data-room-first-read.csv`, `shadow-ai-census.csv`, `ai-inventory.csv`): delete the example row when you start, or keep it as a model.
3. For the census (01.6), use filters and pivot tables on `../common/harbor-and-pine/it/proxy-log.csv`: add a column that marks a row as AI when `dest_host` is on your host list, then pivot by host and department with count, distinct count of `user_id` and median of `bytes_out`. Lesson 01.6 lists the hosts to start with.
4. Roleplays: paste a persona's prompt into any LLM chat ([how](../common/persona-format.md)); feedback with the [coach prompt](../common/coach-prompt.md).

## Track B — Python

Set up the field kit once ([instructions](../common/README.md)): Python 3.12 or newer and `pip install -r ../common/requirements.txt`. No API key is needed in this module: the scripts make no LLM calls and no network requests. Then, from this folder:

```bash
python first_read.py                        # 01.5: what is in the data room
python first_read.py --csv first-read-files.csv
python census.py                            # 01.6: shadow-AI census by department
```

Both scripts import the shared helpers from `../common/fieldkit/` and read the data room by relative path. `census.py` keeps its host list in `AI_HOSTS` at the top: add the AI services you find, because proxy categories lag behind new tools. Python is worth it here because the first read is repeated at the start of every engagement in this course, and the census is meant to be re-run every quarter on fresh exports.

Checked on 2 November 2026 with Python 3.14.3 and pandas 3.1.0 (the versions pinned in `../common/requirements.txt`).
