# Field kit (shared lab files)

This folder comes with every module download. It holds what all the labs share:

| Path | What it is |
|---|---|
| `harbor-and-pine/` | The data room of Harbor & Pine, the warm-up organization for modules 1–7. Start with its `INDEX.md`. |
| `persona-format.md` | How the roleplay stakeholders work and how to run an interview with any LLM chat. |
| `coach-prompt.md` | The prompt that gives you feedback on an interview transcript or a deliverable. |
| `fieldkit/` | Small Python helpers for the Python track. |
| `requirements.txt` | Pinned Python packages for the Python track. |
| `check_setup.py` | Checks that your Python setup works. |

## Two ways to do every lab

**Track A — no code.** Open the CSV files in a spreadsheet (Excel, Google Sheets, LibreOffice
Calc) and use filters, pivot tables and formulas. Use any LLM chat for the AI steps: a project or
custom assistant with instructions, files uploaded where your plan allows it. Every lab can be done
this way.

**Track B — Python.** Where a lesson says Python is worth it (bigger data, repeatable evals,
scenarios), it gives a script built on `fieldkit`. You need Python 3.12 or newer and, for the AI
steps, an API key for one LLM provider (about US$10 covers the whole course with the default
settings; a local model through Ollama costs nothing).

> [!NOTE]
> Encoding: all files are UTF-8 and contain Hebrew, Arabic and Russian text. In Excel use
> Data → From Text/CSV and pick "65001: Unicode (UTF-8)" so the text displays correctly.

## Setting up Track B (once)

Open a terminal in this folder (`labs/common`) and run:

```bash
python -m venv .venv
```

Activate it — Windows PowerShell: `.venv\Scripts\Activate.ps1`; macOS or Linux: `source .venv/bin/activate`. Then:

```bash
python -m pip install -r requirements.txt
python check_setup.py
```

Choose your LLM provider with environment variables (PowerShell shown; on macOS/Linux use
`export NAME=value`):

```powershell
$env:FIELDKIT_PROVIDER = "anthropic"     # or openai, ollama, mock
$env:ANTHROPIC_API_KEY = "<your key>"    # or OPENAI_API_KEY; never save a key in a file
$env:FIELDKIT_MODEL = "claude-opus-5-5"  # optional: any current model id of your provider
python check_setup.py --llm
```

`mock` answers without a key or network, so you can test a script before spending anything.

## The helpers

| Module | Use it for |
|---|---|
| `fieldkit.data` | `data_room("harbor-and-pine")` finds a data room; `load(path)` reads a CSV with dates in Israel time. |
| `fieldkit.profile` | `profile(df)` (completeness, distinct values, top values per column), `duplicates(...)`, `share(...)`. |
| `fieldkit.baseline` | `elapsed_hours`, `working_hours` (Sunday–Thursday by default), `summarize` (median, p75, p90), `sample`. |
| `fieldkit.evals` | `run_eval` runs your pilot over a test set; `report` writes the markdown summary with per-label and per-language results. |
| `fieldkit.cost` | `token_cost`, `pilot_value` (net monthly value in ₪ after review and rework), `breakeven_months`, `npv`. |
| `fieldkit.llm` | `complete(prompt, system=...)` calls the provider you chose and caches replies on disk, so re-running an eval is free. |

A lab script starts like this (it lives in `labs/module-NN/`, next to `labs/common/`):

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))

from fieldkit.data import data_room, load
room = data_room("harbor-and-pine")
tickets = load(room / "support" / "tickets.csv")
```

Model prices in `fieldkit/cost.py` were checked on 2026-11-02; check your provider's pricing page
before you quote a cost to anyone.
