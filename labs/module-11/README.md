# Module 11 lab files — Givat Oren municipality

Everything you need to run the Givat Oren engagement: the brief, the data room, the people you talk to, the permit-FAQ pilot with its knowledge pack and test set, three Track B scripts, and (for the debrief only) the expert's deliverables. All people, organizations and data are fictional and synthetic. Residents' identifiers are hashed; messages are synthetic.

## What is in this folder

| Path | What it is | Lesson |
|---|---|---|
| `brief.md` | The engagement brief: how the ask reached you, money and authority, timeline, access on day one | 11.1 |
| `data-room/` | Givat Oren's data room: start with [`INDEX.md`](data-room/INDEX.md). City profile, org chart, the ask, the draft budget, the council's fee decision; Moked 106 contacts (4% caller sample), callbacks, Q3 report, staffing, mystery-shopper calls; permit applications, procedures, checklist, letter templates; the CMS inventory and the permits pages as published; the "Ruti" chatbot log; FOI log and answer; accessibility statement and audit; information security procedure; procurement procedure, vendor proposal, emails, framework catalogue; works committee documents | 11.1–11.6 |
| `data-room/generate.py`, `textbank.py` | The seeded generator (Python standard library only): `python generate.py` rebuilds every data file and the pilot's inputs byte for byte. Reading it spoils the engagement | — |
| `personas/` | The cast of nine ([README](personas/README.md)): roleplay prompts and pre-run transcripts | 11.1–11.6 |
| `discovery.py` | Track B: repeat contacts, callbacks, service language, permits and letters, website content, Ruti, mystery shopper | 11.2, 11.3 |
| `case_model.py` | Track B: the agent assistant's hours and the content fix's contacts, labelled (`fieldkit.cost`) | 11.3, 11.5 |
| `pilot/knowledge-pack/` | Knowledge pack v1: 44 documents (11 permits-and-fees topics × Hebrew, Arabic, Russian, English), each with owner and effective date, approved 14 January 2027 | 11.5 |
| `pilot/knowledge-pack-all.md` | The same 44 documents in one file, to upload to a chat tool | 11.5 |
| `pilot/system-prompt.md` | The assistant's system prompt (v1.0) and change log | 11.5 |
| `pilot/test-set.csv` | 174 questions (he 44, ar 44, ru 44, en 32, am 10) with expected behaviour (answer / route / clarify), gold topic and facts, outdated facts, and the split (40 dev, 134 test) | 11.5 |
| `pilot/negative-tests.csv` | 12 hand-written negative tests with English glosses and what each tests | 11.5 |
| `pilot/track-a-80.csv`, `pilot/scoring-sheet-80.csv`, `pilot/batches/` | The spreadsheet track: 80 test questions, the scoring sheet, and four batches of 20 to paste into a chat tool | 11.5 |
| `pilot/faq_lib.py` | Shared code: corpora, BM25 search, language detection, the automatic checks | 11.5 |
| `pilot/run_faq.py` | Track B: runs `search` (no AI) or `rag` (LLM) over the website (`site`) or the pack (`pack`) | 11.5 |
| `pilot/score_faq.py` | Track B: scores a run, or your filled Track A sheet, and compares with today's agents (`--today`) | 11.5 |
| `pilot/runs/`, `pilot/reports/` | The search baselines' runs and reports on the test, dev, Track A and negative sets (real, reproducible) | 11.5 |
| `expert/` | The expert's deliverables for comparison in the debrief; open them only after your own ([README](expert/README.md)) | 11.6 |

## What each lesson uses

| Lesson | Files |
|---|---|
| 11.1 The call | `brief.md`; `data-room/city/`, the Q3 report, `content/site/PRK-*.md`, the FOI answer, the accessibility statement, the vendor proposal, the procurement procedure, the works committee letter; personas Ronit and Eyal |
| 11.2 Discovery | `data-room/service/`, `permits/`, `content/`, `chatbot/`, `governance/`, `pilot/test-set.csv` (for the mystery-shopper join); personas Larisa, Tsega, Amal, Dmitri; `discovery.py` |
| 11.3 Diagnosis | Your memo; the budget extract, the Q3 report, the proposal; persona Ronit; `case_model.py` |
| 11.4 The hard part | `procurement/`, `governance/`, `hr/`, `chatbot/ruti-setup-notes.md`, `content/cms-pages.csv`; personas Samer, Moshe, Liron |
| 11.5 Build | `pilot/`; `content/site/`; `service/mystery-shopper-2026.csv`; personas Tsega and Samer |
| 11.6 Readout | Your deliverables; personas Eyal, Ronit, Samer, Larisa, Dmitri, Moshe; `expert/` |

## Track A — no code

1. Open the CSV files in Excel, Google Sheets or LibreOffice Calc. In Excel use *Data → From Text/CSV* and choose *65001: Unicode (UTF-8)*; files contain Hebrew, Arabic, Russian and some Amharic, and commas inside quotes.
2. **11.2, repeat contacts:** in `moked-contacts.csv` sort by `caller_id`, `topic`, `opened_at`; add `=AND(B3=B2, G3=G2, DATEVALUE(LEFT(C3,10))-DATEVALUE(LEFT(C2,10))<14)` and average it per topic with a pivot. **Callbacks:** in `callbacks.csv`, `=IF(E2="","never",IF(DATEVALUE(LEFT(E2,10))<=DATEVALUE(D2),"on time","late"))`. **Language:** a pivot of `contact_language` against `served_language`.
3. **11.2, pages:** open `content/site/` and `city/council-decision-fees-2025-12.md` side by side; mark each page current or out of date.
4. **11.5:** in a chat tool your organization approved for this data (a Claude project, a ChatGPT project or custom GPT, a Gemini Gem, a Copilot Studio agent), paste the text block of `pilot/system-prompt.md` into the instructions and upload `pilot/knowledge-pack-all.md`. Paste one `pilot/batches/batch-NN.md` per **new** conversation and ask for one JSON object per question. Put the results into a copy of `pilot/scoring-sheet-80.csv` and fill the check columns by reading each answer against `gold_facts` and `stale_facts`. Compare with `pilot/reports/search-site-track-a.md` and `search-pack-track-a.md` (site search, pack search and today's agents on the same 80 questions).

## Track B — Python

Set up the field kit once ([instructions](../common/README.md)): Python 3.12 or newer and `pip install -r ../common/requirements.txt`. No extra packages. From this folder:

```bash
python discovery.py                                        # 11.2: the discovery numbers
python case_model.py                                       # 11.3: the case, labelled
cd pilot
python run_faq.py --mode search --corpus site --set test   # 11.5: no AI, the website as it is
python run_faq.py --mode search --corpus pack --set test   # no AI, the approved pack
python score_faq.py runs/search-site-test.csv --today
python run_faq.py --mode rag --corpus pack --set dev --limit 10
python run_faq.py --mode rag --corpus pack --set test
python run_faq.py --mode rag --corpus pack --set negative
python score_faq.py runs/rag-pack-test-<model>.csv --model claude-sonnet-5-5 --today
python score_faq.py --sheet my-scoring-sheet-80.csv        # score your Track A sheet the same way
```

The provider and model come from `FIELDKIT_PROVIDER`, `FIELDKIT_MODEL` and your provider's key variable (see the [field kit README](../common/README.md)). Every LLM call goes through `fieldkit.llm.complete` and is cached in `.fieldkit-cache/`. `FIELDKIT_PROVIDER=mock` runs everything without a key (the scores are meaningless, but the pipeline is proven). On Windows, if non-Latin text prints as `?`, run `$env:PYTHONIOENCODING = "utf-8"` first. The scripts read the data room by relative path and make no network requests except the LLM call. The search mode needs only the standard library.

Python is worth it in this module for two reasons: the repeat-contact and callback measures are joins the Resident Service Division will re-run every month, and the assistant must be re-scored with identical rules every time the council changes a fee.

**What is real and what is not.** Every number computed from the data room, the search baselines and "today" (the quality unit's mystery-shopper calls, joined to the test questions) reproduce exactly: on the 134 test questions, site search is right on 23.9%, pack search on 64.9% (93.5% of answer questions), today's agents on 54.3% of the 94 calls that asked those questions. The LLM figures in lesson 11.5 and in `expert/05` are an illustrative worked example, not a measurement; your run will differ.

Checked on 2 November 2026 with Python 3.14.3, pandas 3.1.0 and tabulate 0.10.0 (the versions pinned in `../common/requirements.txt`), end to end with `FIELDKIT_PROVIDER=mock`. Model prices come from `fieldkit.cost.PRICES` (Anthropic list prices checked 2 November 2026); pass `--price-in` and `--price-out` to `score_faq.py` for any other model, after checking your provider's pricing page. Exchange rate: Bank of Israel representative rate, ₪3.136 per US$ on 2 November 2026.
