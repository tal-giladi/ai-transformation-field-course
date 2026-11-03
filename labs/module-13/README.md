# Module 13 lab files — Kinneret Plastics

Everything you need to run the Kinneret Plastics engagement: the brief, the data room, the people you talk to, two Track B scripts for discovery and the data-readiness audit, the maintenance-manual assistant pilot with its knowledge pack and test set, and (for the debrief only) the expert's deliverables. All people, organizations, machines and data are fictional and synthetic. Employees appear as ids or first names.

## What is in this folder

| Path | What it is | Lesson |
|---|---|---|
| `brief.md` | The engagement brief: how the ask reached you, money and authority, timeline, access on day one | 13.1 |
| `data-room/` | Kinneret's data room: start with [`INDEX.md`](data-room/INDEX.md). Company profile, org chart, the meeting minutes, the KPI deck, the budget, the customer's letter; Plant K work orders, Plant G's maintenance log, failure codes, PM report, night calls, a WhatsApp extract, the drive listing; ProdTrack downtime and quality scrap; asset registers, MES machines, moulds; sensor data and SCADA alarms; the drive's parts list and the ERP's; manuals and procedures as on the drive; the examination register and safety programme; the vendor's proposal, case study, onboarding guide, questionnaire and emails; the local agreement, the works committee's letter and the languages table | 13.1–13.6 |
| `data-room/generate.py` and the other `.py` files there | The seeded generator (Python standard library only): `python generate.py` rebuilds every data file and the pilot's inputs byte for byte. Reading it spoils the engagement | — |
| `personas/` | The cast of nine ([README](personas/README.md)): roleplay prompts and pre-run transcripts | 13.1–13.6 |
| `discovery.py` | Track B: downtime split, MTTR on one definition (serial-number crosswalk), work-order profile, PM, night calls, parts, assets, sensors, scrap, examinations | 13.2, 13.3 |
| `readiness_audit.py` | Track B: the repeatable data-readiness audit (labels, back-coding, clocks, identifiers, sensors, verdicts); `--llm N` codes N uncoded work orders through `fieldkit.llm` | 13.5 |
| `pilot/knowledge-pack/` | Knowledge pack v1: 22 documents (6 manual extracts in English, 8 current procedures in Hebrew, approved Arabic and Russian translations of 4 safety procedures), each with revision and owner, approved 3 March 2027 | 13.5 |
| `pilot/knowledge-pack-all.md` | The same 22 documents in one file, to upload to a chat tool | 13.5 |
| `pilot/system-prompt.md` | The assistant's system prompt v1.0 and change log | 13.5 |
| `pilot/test-set.csv` | 118 questions (Hebrew 34, Arabic 34, Russian 34, English 16) with expected behaviour (answer / route / clarify), gold document and facts, outdated facts, and the split (24 dev, 94 test) | 13.5 |
| `pilot/negative-tests.csv` | 12 hand-written negative tests with English glosses and what passes | 13.5 |
| `pilot/track-a-60.csv`, `pilot/scoring-sheet-60.csv`, `pilot/batches/` | The spreadsheet track: 60 test questions, the scoring sheet, three batches of 20 to paste into a chat tool | 13.5 |
| `pilot/manual_lib.py`, `pilot/run_manual.py`, `pilot/score_manual.py` | Track B: corpora (the drive as it is, or the pack), BM25 search, the LLM run, the scorer | 13.5 |
| `pilot/runs/`, `pilot/reports/` | The search baselines' runs and reports on the test, Track A and negative sets (real, reproducible) | 13.5 |
| `expert/` | The expert's deliverables for comparison in the debrief; open them only after your own ([README](expert/README.md)) | 13.6 |

## What each lesson uses

| Lesson | Files |
|---|---|
| 13.1 The call | `brief.md`; `data-room/company/`, the PM report, the vendor's proposal, questionnaire and onboarding guide, `hr/`; personas Dalia and Amnon |
| 13.2 Discovery | `data-room/production/`, `maintenance/`, `assets/`, `sensors/`, `scada/`, `parts/`, `docs/`, `safety/`; personas Vladi, Nizar, Tigist, Eli (Khalil briefly); `discovery.py` |
| 13.3 Diagnosis | Your memo; the budget, the customer's letter, the proposal and onboarding guide; persona Orit; `discovery.py` |
| 13.4 The hard part | `vendor/`, `hr/`, `safety/`, `maintenance/failure-codes.csv`, the drive listing; personas Gilad, Khalil, Eli |
| 13.5 Build | `readiness_audit.py`; `pilot/`; `docs/` and the drive listing; personas Nizar and Vladi |
| 13.6 Readout | Your deliverables; personas Amnon, Dalia, Orit, Eli, Vladi, Khalil; `expert/` |

## Track A — no code

1. Open the CSV files in Excel, Google Sheets or LibreOffice Calc. In Excel use *Data → From Text/CSV* and choose *65001: Unicode (UTF-8)*; files contain Hebrew, Arabic and Russian (some headers are Hebrew) and commas inside quotes.
2. **13.2, the loss:** in `production/downtime-events-2026.csv` filter out `PM`, `SETUP`, `NO_ORDER`; pivot `duration_min` by `reason_code` and `plant`, then MOULD by `shift`. **Work orders:** filter `wo_type` = BD; pivot `failure_code`; count action texts that are only "תוקן", "בוצע", "done", "ok". **Completion times:** `=MOD(J2,1)` on `completed_at` after converting it to a date-time, then count values just before 06:45, 14:45 and 22:45.
3. **13.2, "ready":** match Plant G's hall numbers to ProdTrack machines on the serial number (`asset-list-plant-g.csv` against `mes-machines.csv`) before you compare anything.
4. **13.2, clocks:** in `scada/alarms-plant-g-2026h2.csv`, `=VALUE(MID(A2,4,2))>12` marks dates that cannot be day-first; the times are UTC.
5. **13.5, the assistant:** in a chat tool your organization approved for this data (a Claude Team or Enterprise project, a ChatGPT Business or Enterprise project or custom GPT, a Copilot Studio agent, a Gemini Gem), paste the text block of `pilot/system-prompt.md` into the instructions and upload `pilot/knowledge-pack-all.md`. Paste one `pilot/batches/batch-NN.md` per **new** conversation and ask for one JSON object per question. Put the results into a copy of `pilot/scoring-sheet-60.csv` and fill the check columns by reading each answer against `gold_facts` and `stale_facts`. Compare with `pilot/reports/search-drive-track-a.md` and `search-pack-track-a.md`. Run the 12 negative tests by hand.

## Track B — Python

Set up the field kit once ([instructions](../common/README.md)): Python 3.12 or newer and `pip install -r ../common/requirements.txt`. No extra packages. From this folder:

```bash
python discovery.py                                          # 13.2-13.3: the discovery numbers
python readiness_audit.py --out audit-2027-01.md             # 13.5: the audit, no AI
python readiness_audit.py --llm 40                           # + LLM coding of 40 uncoded work orders
cd pilot
python run_manual.py --mode search --corpus drive --set test # no AI, the drive as it is
python run_manual.py --mode search --corpus pack --set test  # no AI, knowledge pack v1
python score_manual.py runs/search-drive-test.csv
python run_manual.py --mode rag --corpus pack --set dev --limit 10
python run_manual.py --mode rag --corpus pack --set test
python run_manual.py --mode rag --corpus pack --set negative
python score_manual.py runs/rag-pack-test-<model>.csv --model claude-sonnet-5-5
python score_manual.py --sheet my-scoring-sheet-60.csv       # score your Track A sheet the same way
```

The provider and model come from `FIELDKIT_PROVIDER`, `FIELDKIT_MODEL` and your provider's key variable (see the [field kit README](../common/README.md)). Every LLM call goes through `fieldkit.llm.complete` and is cached in `.fieldkit-cache/`. `FIELDKIT_PROVIDER=mock` runs everything without a key (the scores are meaningless, but the pipeline is proven). On Windows, if non-Latin text prints as `?`, run `$env:PYTHONIOENCODING = "utf-8"` first. The scripts read the data room by relative path and make no network requests except the LLM call; the search mode, the scorer and the generator need only the standard library.

Python is worth it in this module for two reasons: the audit's joins (thousands of free-text work orders in four languages, three time conventions, a serial-number crosswalk, matches in time windows) must be re-run every month with identical rules as the foundation's progress measure, and the assistant must be re-scored with identical rules every time the knowledge pack changes.

**What is real and what is not.** Every number computed from the data room, the audit and the search baselines reproduces exactly: on the 94 test questions, search over the drive is right on 23.4%, search over the pack on 27.7%. The LLM figures in lesson 13.5 and in `expert/05` are an illustrative worked example, not a measurement; your run will differ.

Checked on 3 November 2026 with Python 3.14 and the versions pinned in `../common/requirements.txt`, end to end with `FIELDKIT_PROVIDER=mock`. Model prices come from `fieldkit.cost.PRICES`; Sonnet 5.5's US$2 / US$10 per million tokens was confirmed on the [Claude pricing page](https://claude.com/pricing) on 3 November 2026. Pass `--price-in` and `--price-out` to `score_manual.py` for any other model, after checking your provider's pricing page. Exchange rate: ₪3.136 per US$ (Bank of Israel representative rate, 2 November 2026).
