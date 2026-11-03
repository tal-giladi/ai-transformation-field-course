# Module 12 lab files — Atlas & Rowe

Everything you need to run the Atlas & Rowe engagement: the brief, the data room, the people you interview, the precedent-search pilot with its citation-verification gate and test sets, Track B scripts for discovery and the business case, and (for the debrief only) the expert's deliverables. All people, firms, clients and vendors are fictional and all data is synthetic. **The rulings, memos and clause notes in the corpus are fictional and are not a statement of Israeli law; nothing here is legal advice.**

## What is in this folder

| Path | What it is | Lesson |
|---|---|---|
| `brief.md` | The engagement brief: how you were brought in, the stated ask, contract, budget, timeline, access on day one | 12.1 |
| `data-room/` | The firm's data room: start with [`INDEX.md`](data-room/INDEX.md). HR and billing extracts, a quarter of time entries, the proxy and DLP logs, an AI-use survey, expenses, policies, a client's guidelines, the vendor's documents, the precedent bank's index, the 78-document research corpus, a memo with reviewers' comments | 12.1–12.6 |
| `data-room/generate.py` and its modules | The seeded generator (Python standard library only): `python generate.py` rebuilds every data-room and pilot data file byte for byte. Reading it spoils the engagement | — |
| `personas/` | The cast of nine ([README](personas/README.md)): roleplay prompts and pre-run transcripts | 12.1–12.6 |
| `discovery.py` | Track B: research by narrative vs code, write-offs, hours against target, fixed-fee overruns, AI use vs survey, the bank's review state, the NDA history | 12.2, 12.3 |
| `roi_model.py` | Track B: the revised business case, by billing type, with the customer's share; scenarios and sensitivity (`fieldkit` data loading) | 12.3, 12.5 |
| `roi-revised.csv` | The model's year-1 table for Track A (written by `roi_model.py`) | 12.3, 12.5 |
| `pilot/system-prompt.md` | The research assistant's instructions (v1.0) and change log | 12.5 |
| `pilot/questions.csv` | 48 research questions (24 Hebrew, 24 English) with gold and stale documents | 12.5 |
| `pilot/questions-scoring-sheet.csv`, `pilot/batches/` | Track A: the scoring sheet and the two question batches to paste | 12.5 |
| `pilot/curation-2026-12.csv` | The knowledge team's review of the 78 research documents: status before and after, what replaced what | 12.5 |
| `pilot/drafts/` | 40 research answers with 160 citations (general chat assistant; the vendor's proof of concept) | 12.5 |
| `pilot/citation-labels.csv` | The labelled answer for every citation: exists, paragraph, quote, current, supports, verdict | 12.5 |
| `pilot/citation-check-sheet.csv` | Track A: the same citations with empty columns for your checks and timing | 12.5 |
| `pilot/negative-questions.csv` | Eight negative tests with expected behaviour | 12.5 |
| `pilot/corpus_lib.py`, `search.py`, `verify_citations.py` | Track B: corpus loading and keyword search (BM25), the search eval, the citation gate | 12.5 |
| `pilot/runs/`, `pilot/reports/` | The no-AI baselines: search uncurated, curated and with Hebrew prefix stripping; the gate's rules with the KM status and the curated status; the keyword-overlap check (real, reproducible) | 12.5 |
| `expert/` | The expert's deliverables for comparison in the debrief; open them only after your own ([README](expert/README.md)) | 12.6 |

## Track A — no code

1. Open the CSV files in Excel, Google Sheets or LibreOffice Calc. In Excel use *Data → From Text/CSV* and choose *65001: Unicode (UTF-8)*; the files contain Hebrew, English and some Arabic and Russian, and commas inside quotes.
2. **12.2, research time:** in `billing/time-entries-2026-q3.csv` add a column that is 1 when `narrative` contains a research word (the formula is in lesson 12.2), then pivot `hours` by `role` and that column, and `written_off_hours` ÷ `hours` by `activity_code` and that column. **AI use:** count distinct `user_id` in `it/proxy-ai-domains-2026-09-10.csv`, joined to `people/lawyers.csv` with `XLOOKUP` on `lawyer_id`.
3. **12.3:** total `clients/carmel-nda-workstream.csv` by year; the baseline sheet and the netting are laid out in lesson 12.3; `roi-revised.csv` has the model's result.
4. **12.5, search:** in a chat tool your firm approved for this data (a Claude project, a ChatGPT project or custom GPT, a Gemini Gem, a Copilot Studio agent), paste the text block of `pilot/system-prompt.md` into the instructions and upload the corpus (all 78 files, then only the 65 current ones in a second project). Paste `pilot/batches/questions-en.md` and `questions-he.md` into new conversations and score in `pilot/questions-scoring-sheet.csv`. Compare with `pilot/reports/search-raw.md` and `search-curated.md`.
5. **12.5, citation gate:** in `pilot/citation-check-sheet.csv` use the lookup formulas in lesson 12.5 against `data-room/knowledge/corpus-index.csv` and `pilot/curation-2026-12.csv`; check quotes and support by reading the paragraph (or asking your approved assistant); score against `pilot/citation-labels.csv`.

## Track B — Python

Set up the field kit once ([instructions](../common/README.md)): Python 3.12 or newer and `pip install -r ../common/requirements.txt`. No extra packages. From this folder:

```bash
python discovery.py                                   # 12.2, 12.3: the discovery numbers
python roi_model.py                                   # 12.3, 12.5: scenarios, ledgers, sensitivity
cd pilot
python search.py                                      # 12.5: search over all 78 documents
python search.py --curated                            # only the current documents
python verify_citations.py --curated                  # the gate's rules on the 160 citations
python verify_citations.py --curated --support llm    # + an LLM judge for support
python search.py --curated --answer                   # your assistant answers the 48 questions
python verify_citations.py --curated --drafts runs/answers-curated-<model>
```

The provider and model come from `FIELDKIT_PROVIDER`, `FIELDKIT_MODEL` and your provider's key variable (see the [field kit README](../common/README.md)). Every LLM call goes through `fieldkit.llm.complete` and is cached in `.fieldkit-cache/`. `FIELDKIT_PROVIDER=mock` runs everything without a key (the mock answers "other", so LLM scores are meaningless, but the pipeline is proven). On Windows, if Hebrew prints as `?`, run `$env:PYTHONIOENCODING = "utf-8"` first. The scripts read the data room by relative path and make no network requests except the LLM call.

Python is worth it in this module because the research flag and the citation gate must run identically every time the corpus, the prompt or the model changes, and because finance will ask "and if…?" of the business case more than once.

**What is real and what is not.** Every number computed from the data room, the search results, the gate's rule checks and the ROI model reproduce exactly (for example: curated search puts a correct document first for 48 of 48 questions and a stale one in the top three for 0 of 12, against 39 and 12 uncurated; the gate's rules catch 48 of 70 bad citations with 0 false alarms). The LLM-judge, assistant-answer and timing figures in lesson 12.5 and in `expert/05` are an illustrative worked example, not a measurement.

Checked on 2 November 2026 with Python 3.14.3, pandas 3.1.0 and tabulate 0.10.0 (the versions pinned in `../common/requirements.txt`), end to end with `FIELDKIT_PROVIDER=mock`. Prices: Anthropic list prices checked 2 November 2026; exchange rate: Bank of Israel representative rate, ₪3.136 per US$ on 2 November 2026.
