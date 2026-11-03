# Module 18 lab files — the capstone: Tzurim Academic College

Everything you need to run the capstone engagement at Tzurim Academic College, a fictional private college, with no hints: the brief, the data room, the people you can talk to, a checklist for your deliverable set and a scoring sheet for your presentation. Also the worksheets for the optional real engagement (18.4) and for your practice kit and portfolio (18.5). All people, organizations, products and data are fictional and synthetic.

> [!CAUTION]
> The `expert/` folder holds the expert's complete deliverable set: the answer to the capstone. Do not open it, and do not read the data room's `.py` files, until you have submitted your own deliverables and scored them. Opening either early wastes the only unseen engagement in the course.

## What is in this folder

| Path | What it is | Lesson |
|---|---|---|
| `brief.md` | The engagement brief: how you were brought in, the stated ask, money, authority, timeline, access on day one | 18.1 |
| `data-room/` | Tzurim's data room: start with [`INDEX.md`](data-room/INDEX.md). Company documents, student records, tuition accounts, exam periods, inquiries, adviser contacts, LMS activity and scores, policies, a staff survey, IT summaries, a vendor's documents | 18.1–18.3 |
| `data-room/generate.py` and the other `.py` files there | The seeded generator (standard library only): `python generate.py` rebuilds every file byte for byte. Reading it spoils the capstone | — |
| `personas/` | The cast of nine ([README](personas/README.md)): roleplay prompts and pre-run transcripts | 18.1–18.3 |
| `capstone-checklist.csv` | Your deliverable set: each deliverable, its template, the lesson that taught it, the rubric criterion, your version and self-score, the integration-check items | 18.2 |
| `presentation-scoring-sheet.csv` | The 7-criterion rubric for your recorded 10-minute presentation | 18.3 |
| `real-engagement/permission-and-data-plan.md` | Permission letter and data-handling plan for the optional real engagement | 18.4 |
| `practice-kit/practice-kit-index.csv`, `practice-kit/portfolio-piece-checklist.md` | Your practice-kit index and the checklist for turning an engagement into a portfolio piece | 18.5 |
| `expert/` | The expert's deliverables, the pilot's test set and its baseline script. **Only after you submit** | Project debrief |

## What each lesson uses

| Lesson | Files |
|---|---|
| 18.1 The unseen org | `brief.md`, `data-room/` (your choice of what to read), `personas/` (the sponsor first, then your plan) |
| 18.2 The full deliverable set | Your deliverables; `capstone-checklist.csv`; every file you need from `data-room/` and `personas/` |
| 18.3 The executive presentation | Your case; the persona of the executive you choose; `presentation-scoring-sheet.csv` |
| 18.4 Optional real engagement | `real-engagement/permission-and-data-plan.md` |
| 18.5 Practice kit and portfolio | `practice-kit/`; your deliverables from modules 8–18 |

## Track A — no code

1. Open the CSV files in Excel, Google Sheets or LibreOffice Calc. In Excel use *Data → From Text/CSV* and choose *65001: Unicode (UTF-8)*; files contain Hebrew, Arabic, Russian and English text and commas inside quotes.
2. Import every identifier column (student numbers, inquiry ids) as **Text**, not as a number: in the import preview, select the column and set its type to Text.
3. Use filters, pivot tables, `COUNTIFS`, `XLOOKUP` (or `VLOOKUP`) and date arithmetic. Working days: `NETWORKDAYS.INTL(start, end, 7)` treats Friday and Saturday as the weekend.
4. For the pilot, use a chat tool your organization (or you, for this synthetic data) has approved: a Claude, ChatGPT or Gemini project or custom assistant, or a Copilot Studio agent. Build your own test set from the inquiries file and score it in a sheet, as in [05.2](../../lessons/module-05/lesson-02.md) and [05.4](../../lessons/module-05/lesson-04.md).

## Track B — Python

Set up the field kit once ([instructions](../common/README.md)): Python 3.12 or newer and `pip install -r ../common/requirements.txt`. No extra packages. The capstone has no ready-made scripts: you write your own, as you would in a real engagement, starting from the field kit's helpers.

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))   # labs/common

import pandas as pd
from fieldkit.data import data_room, load
from fieldkit.profile import profile
from fieldkit.evals import run_eval, report

room = data_room("module-18")
# Keep identifiers as text: load() turns all-number columns into numbers.
reg = pd.read_csv(room / "students" / "registry-students-2023-2025.csv", dtype=str, keep_default_na=False)
print(profile(reg))
```

Put your scripts in a folder of your own next to this one (for example `labs/my-capstone/`), so a fresh module download never overwrites them. Every LLM call goes through `fieldkit.llm.complete`; choose the provider with `FIELDKIT_PROVIDER` and `FIELDKIT_MODEL` and your provider's key in the environment ([field kit README](../common/README.md)). `FIELDKIT_PROVIDER=mock` runs a pipeline without a key. On Windows, if non-Latin text prints as `?`, run `$env:PYTHONIOENCODING = "utf-8"` first.

Python is worth it here if you want your profiling and joins re-runnable when you find a mistake on day 10, and your pilot's eval re-scored with identical rules every time the prompt changes. Both tracks reach the same deliverables.

Checked on 3 November 2026 with Python 3.14: `python generate.py` run twice gives byte-identical files; the data room is 2.55 MB.
