# Module 8 lab files — Northwind Outfitters

Everything you need to run the Northwind engagement: the brief, the data room, the people you interview, the agent-assist pilot and its test set, two Track B scripts for discovery and the business case, and (for the debrief only) the expert's deliverables. All people and companies are fictional and all data is synthetic. Messages are pseudonymised: `[NAME]` replaces personal details.

## What is in this folder

| Path | What it is | Lesson |
|---|---|---|
| `brief.md` | The engagement brief: how you were brought in, the stated ask, contract, budget, timeline, access on day one | 08.1 |
| `data-room/` | Northwind's data room: start with [`INDEX.md`](data-room/INDEX.md). A 1% customer extract (orders, returns, helpdesk contacts, chatbot sessions), 2,000 written tickets, KPI reports, board minute, finance summary, four returns policies, macros, the Verbalo contract, demo and invoices, legal logs | 08.1–08.6 |
| `data-room/generate.py`, `textbank.py` | The seeded generator (Python standard library only): `python generate.py` rebuilds every data file byte for byte. Reading it spoils the engagement | — |
| `personas/` | The cast of nine ([README](personas/README.md)): roleplay prompts and pre-run transcripts | 08.1–08.6 |
| `discovery.py` | Track B: repeat contacts, like-for-like AHT, returns share, chatbot recontact, refund time, fees | 08.2, 08.3 |
| `case_model.py` | Track B: contacts avoided, cost per truly resolved chat, agent-assist economics and sensitivity (`fieldkit.cost`) | 08.3, 08.5 |
| `pilot/policy-for-pilot.md` | Returns policy v2 as counsel marked it up on 17 December 2026: the pilot's reference | 08.5 |
| `pilot/system-prompt.md` | The agent-assist system prompt (v1.0) and its change log | 08.5 |
| `pilot/labels-2000.csv` | The labelling team's adjudicated labels for the 2,000 tickets: intent, language, decision and fee under v2, escalation, cues, today's reply coded (written by `generate.py`) | 08.5 |
| `pilot/negative-tests.csv`, `negative-labels.csv` | 12 hand-written negative tests with English glosses and expected results | 08.5 |
| `pilot/track-a-200.csv` | The 200 spreadsheet-track tickets (inputs only) | 08.5 |
| `pilot/scoring-sheet-200.csv` | Expected labels for those 200 and empty columns for your run and your ratings | 08.5 |
| `pilot/batches/` | `batch-01.md` … `batch-08.md`: 25 tickets each, ready to paste into a chat tool | 08.5 |
| `pilot/pilot_lib.py`, `sets.py` | Shared code: keyword intent, text cues, the policy as rules, template drafts, draft checks; the fixed dev/test/Track A split | 08.5 |
| `pilot/run_assist.py` | Track B: runs the pilot in `rules`, `llm` or `hybrid` mode over a set | 08.5 |
| `pilot/score.py` | Track B: scores a run (intent, decision, fee, escalation, drafts, cost, negative tests, today) with `fieldkit.evals` | 08.5 |
| `pilot/build_track_a.py` | Rebuilds the Track A files (you do not need to run it) | 08.5 |
| `pilot/runs/`, `pilot/reports/` | The rules baseline's runs and reports on the test, dev, Track A and negative sets (real, reproducible) | 08.5 |
| `expert/` | The expert's deliverables for comparison in the debrief; open them only after your own ([README](expert/README.md)) | 08.6 |

## Track A — no code

1. Open the CSV files in Excel, Google Sheets or LibreOffice Calc. In Excel use *Data → From Text/CSV* and choose *65001: Unicode (UTF-8)*; messages contain Hebrew, Arabic, Russian and some Amharic, and commas inside quotes.
2. **08.2, repeat contacts:** in `contacts.csv` sort by `customer_id`, then `created_at`; add a column that strips everything but digits from `order_id`; in each row test "same customer as the row above, within 7 days, same order or either blank". **Containment:** for each "resolved" row of `bot-sessions.csv` with a `customer_id`, `COUNTIFS` the contacts of that customer in the next 7 days.
3. **08.3:** the baseline sheet and the case in a spreadsheet; the inputs and formulas are in lesson 08.3.
4. **08.5:** in a chat tool your organization approved for this data (a Claude project, a ChatGPT project or custom GPT, a Gemini Gem, a Copilot Studio agent), paste the text block of `pilot/system-prompt.md` into the instructions and upload `pilot/policy-for-pilot.md`. Paste one `pilot/batches/batch-NN.md` per **new** conversation and ask for one JSON object per ticket. Put the results into a copy of `pilot/scoring-sheet-200.csv`: `intent_correct` `=IF(H2=C2,1,0)`, `decision_correct` `=IF(I2=D2,1,0)`, accuracy per language with `AVERAGEIFS`. Compare with `pilot/reports/rules-track-a-rules-today.md` (rules and today on the same 200). Rate drafts in `draft_verdict` (accept, light edit, heavy edit, reject) and `safety_issue` (y/n), with seconds in `review_seconds`.

## Track B — Python

Set up the field kit once ([instructions](../common/README.md)): Python 3.12 or newer and `pip install -r ../common/requirements.txt`. No extra packages. From this folder:

```bash
python discovery.py                                    # 08.2: the discovery numbers
python case_model.py                                   # 08.3, 08.5: the case and the pilot economics
cd pilot
python run_assist.py --mode rules --set test           # 08.5: the no-AI baseline, free and exact
python score.py runs/rules-test-rules.csv --today
python run_assist.py --mode hybrid --set dev --limit 20
python run_assist.py --mode hybrid --set test
python run_assist.py --mode hybrid --set negative
python score.py runs/hybrid-test-<model>.csv --today
```

The provider and model come from `FIELDKIT_PROVIDER`, `FIELDKIT_MODEL` and your provider's key variable (see the [field kit README](../common/README.md)). Every LLM call goes through `fieldkit.llm.complete` and is cached in `.fieldkit-cache/`. `FIELDKIT_PROVIDER=mock` runs everything without a key (it answers "other", so the scores are meaningless, but the pipeline is proven). On Windows, if non-Latin text prints as `?`, run `$env:PYTHONIOENCODING = "utf-8"` first. The scripts read the data room by relative path and make no network requests except the LLM call.

Python is worth it in this module for two reasons: the repeat-contact and recontact measures are fiddly joins you will re-run every month, and the pilot must be scored identically after every prompt, model or policy change.

**What is real and what is not.** Every number computed from the data room, the rules baseline and "today" (the agents' real replies, coded) reproduce exactly: on the 1,700 test tickets, returns decisions right 55.6% today and 79.6% under rules, 3 of 12 negative tests passed by rules. The LLM and hybrid figures in lesson 08.5 and in `expert/05` are an illustrative worked example, not a measurement; your run will differ.

Checked on 2 November 2026 with Python 3.14.3, pandas 3.1.0 and tabulate 0.10.0 (the versions pinned in `../common/requirements.txt`), end to end with `FIELDKIT_PROVIDER=mock`. Model prices come from `fieldkit.cost.PRICES` (Anthropic list prices checked 2 November 2026); pass `--price-in` and `--price-out` to `score.py` for any other model, after checking your provider's pricing page. Exchange rate: Bank of Israel representative rate, ₪3.136 per US$ on 2 November 2026.
