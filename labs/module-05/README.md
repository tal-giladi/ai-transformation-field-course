# Module 5 lab files — Building and testing a pilot

Everything module 5 uses beyond the shared Harbor & Pine data room: the pilot's prompt and category rules, the test set built from 600 real (synthetic) support emails, 24 hand-written negative tests, the scoring sheet, and the Python scripts that build, run and score the pilot. The data room itself is in `../common/harbor-and-pine/` (start with its [INDEX](../common/harbor-and-pine/INDEX.md)); it comes with this download. All people and companies are fictional and all data is synthetic. Messages in the test files are pseudonymised: `[NAME]`, `[PHONE]`, `[ADDRESS]` replace personal details.

## What is in this folder

| File | What it is | Lesson |
|---|---|---|
| `samir-rule-of-use-transcript.md` | Pre-run conversation agreeing the rule of use with Samir (no-roleplay path) | 05.1 |
| `categories.md` | The eleven categories, nine flags and the labelling rules, with examples from the data room | 05.2, 05.3 |
| `labels.csv` | The team's adjudicated labels for all 600 emails: category, language, kind (new, follow-up, duplicate) | 05.2 |
| `test-set.csv` | The frozen test set: 400 messages (`T-001`…), inputs, order context, ground truth, and today's helpdesk fields and agent replies for comparison | 05.2–05.4 |
| `dev-set.csv` | The 200-message development set (`D-001`…) for tuning the prompt | 05.2, 05.3 |
| `negative-tests.csv` | 24 hand-written negative tests (`N-01`…) in six languages, with expected category, flags, reply language and must / must-not patterns, and an English gloss | 05.2–05.4 |
| `labelling-sample-40.csv` | 40 test messages (10 per language) to label yourself before you look at the labels | 05.2 |
| `system-prompt.md` | The pilot's full system prompt (v1.0) and its change log | 05.3, 05.7 |
| `batches/` | Paste-ready batches for Track A: `dev-batch-01…08.md`, `test-batch-01…16.md` (25 items each), `negative-batch.md` | 05.3 |
| `scoring-sheet.csv` | Scoring sheet for the 400 test items and 24 negative tests: expected values filled, your run's and your raters' columns empty | 05.4 |
| `runs/`, `reports/` | The keyword baseline's run files and score reports for the dev, test and negative sets (real, reproducible) | 05.4 |
| `monitoring-signals.csv` | Monitoring signals: indicator, threshold, cadence, owner, response, charter stop rule | 05.7 |
| `pilot_lib.py` | Shared code: categories, pseudonymisation, order context, language by alphabet, keyword baseline, prompt in / JSON out, draft checks | — |
| `build_test_set.py` | Track B: builds the test and dev sets, the batches, the scoring sheet and the labelling sample from the data room | 05.2 |
| `agreement.py` | Track B: agreement and Cohen's kappa between two sets of labels, and the items to adjudicate | 05.2 |
| `run_pilot.py` | Track B: runs the pilot (LLM or keyword baseline) over a set | 05.3 |
| `score.py` | Track B: scores a run (triage, language, flags, draft checks, negative tests, cost, today, ratings) and writes `reports/<run>.md` | 05.4, 05.7 |

## Track A — no code

1. Open the CSV files in Excel, Google Sheets or LibreOffice Calc. In Excel use *Data → From Text/CSV* and choose *65001: Unicode (UTF-8)*, or Hebrew, Arabic and Russian text will not display. Messages contain line breaks inside quotes; import, don't paste.
2. **05.2:** fill `your_category` and `your_language` in `labelling-sample-40.csv`, then look each `item_id` up in `test-set.csv` (`expected_category`). Agreement = matches ÷ 40. Kappa: for each category multiply your count by the reference count, sum, divide by 1,600 (that is *p*ₑ); kappa = (agreement − *p*ₑ) ÷ (1 − *p*ₑ).
3. **05.3:** in a chat tool your organization approved for this data (a Claude project, a ChatGPT project or custom GPT, a Gemini Gem, a Copilot Studio agent), paste the text block of `system-prompt.md` into the instructions and upload `categories.md` as knowledge. Paste one batch file per **new** conversation; check that 25 items come back. Then ask for "the same as a tab-separated table: item, category, language, reply_language, flags" and paste it into a copy of `scoring-sheet.csv`. Keep the JSON with the drafts for rating.
4. **05.4:** in the scoring sheet, `category_correct` = `=IF(G2=D2,1,0)` (predicted vs expected category); accuracy per language with `=AVERAGEIFS(J:J,C:C,"ar")`; rate drafts in `draft_verdict` with `accept`, `light edit`, `heavy edit` or `reject`, `safety_issue` with `y` or `n`, and the seconds in `review_seconds`. Acceptance per language: `=COUNTIFS(C:C,"ar",L:L,"accept")+COUNTIFS(C:C,"ar",L:L,"light edit")` divided by the rated Arabic rows. For the blind calibration set, copy 10 rows' `agent_reply` from `test-set.csv` into your rating document among the drafts.
5. **05.7:** fill `monitoring-signals.csv` with your own signals; every stop rule of your charter must appear.

## Track B — Python

Set up the field kit once ([instructions](../common/README.md)): Python 3.12 or newer and `pip install -r ../common/requirements.txt`. No extra packages are needed. From this folder:

```bash
python build_test_set.py                              # 05.2: sets, batches, sheet, sample (same output every time)
python agreement.py my-labels.csv                     # 05.2: you vs the adjudicated labels
python run_pilot.py --mode baseline --set test        # 05.4: the no-LLM baseline, free
python score.py runs/baseline-test-keywords-v1.csv --today
python run_pilot.py --set dev --limit 20              # 05.3: first LLM calls
python run_pilot.py --set dev                         # tune the prompt on dev only
python run_pilot.py --set test                        # then score once per prompt version
python run_pilot.py --set negative
python score.py runs/llm-test-<model>.csv --today --ratings scoring-sheet.csv
```

The LLM provider and model come from environment variables (`FIELDKIT_PROVIDER`, `FIELDKIT_MODEL`, your provider's key variable; see the [field kit README](../common/README.md)); every call goes through `fieldkit.llm.complete` and is cached in `.fieldkit-cache/`. Without a key, prove the pipeline with the mock provider (PowerShell: `$env:FIELDKIT_PROVIDER = "mock"`; macOS/Linux: `export FIELDKIT_PROVIDER=mock`): it answers "other" to everything, so the scores are meaningless, but every script runs end to end. On Windows, if non-Latin text prints as `?`, run `$env:PYTHONIOENCODING = "utf-8"` first. The scripts read the data room by relative path and make no network requests except the LLM call.

Python is worth it in this module because a pilot is evaluated again and again: after every prompt change, every model notice and every month (05.7). A script makes each run and each score identical, records model, prompt version and tokens automatically, and turns a day of pasting into minutes.

**What is real and what is not.** The keyword baseline's numbers and the "today" numbers (helpdesk fields, agents' replies) in `reports/` are computed from the data room and reproduce exactly: on the test set, triage 98.2% (keyword rules) vs 64.0% (helpdesk field), 2 of 24 negative tests passed by the rules, 96 of 151 "where is my order?" agent replies giving a date already in the past. The LLM figures in lesson 05.4's reference answer are an illustrative worked example, not a measurement; your run will differ.

Checked on 2 November 2026 with Python 3.14.3, pandas 3.1.0 and tabulate 0.10.0 (the versions pinned in `../common/requirements.txt`), end to end with `FIELDKIT_PROVIDER=mock` for the dev, test and negative sets. Model prices used by `score.py` come from `fieldkit.cost.PRICES` (Anthropic list prices checked 2 November 2026); pass `--price-in` and `--price-out` for any other model, and check your provider's pricing page first.
