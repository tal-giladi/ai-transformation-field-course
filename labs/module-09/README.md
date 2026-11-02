# Module 9 lab — Meridian Mutual

Everything the Meridian Mutual engagement needs: the brief, the data room, the people you can
interview, the pilot files, the Track B scripts and the expert's deliverables. All organizations,
people and data are fictional and synthetic. Start with [the brief](brief.md), then
[the data room's INDEX](data-room/INDEX.md).

## What is in this folder

| Path | What it is |
|---|---|
| [`brief.md`](brief.md) | How you came in, the stated ask, budget, timeline, access on day one |
| [`data-room/`](data-room/INDEX.md) | The data room: claims register sample, document requests, CRM, payments, the full motor extract, SIU case log, complaints, time study, policies, committee minutes, vendor papers and configuration, 240 intake documents with verified values and the vendor's extraction output. `INDEX.md` lists every file |
| [`personas/`](personas/README.md) | Nine roleplay stakeholders and a pre-run transcript for each |
| `pilot/` | The extraction pilot: `system-prompt.md` (v1.0), `splits.csv` (40 development, 200 test), `track-a-sheet.csv` (60 test documents for Track A), `negative-tests.csv` and `negative-tests/` (12 checks on 6 documents), `make_splits.py` (rebuilds the splits) |
| `baselines.py` | 09.3: three cycle-time baselines, the segments of the wait, document rounds, the winter peak, handler time and money |
| `bias_test.py` | 09.4: SIU referral rates by group before and after the fraud score went live, with 95% intervals; which factors fire; what referrals turned into |
| `extract_rules.py` | 09.5: a no-AI baseline extractor (labels and regular expressions); writes `runs/rules-baseline.csv`; `--negative` runs the negative tests |
| `run_extraction.py` | 09.5: your LLM pilot over the documents, through `fieldkit.llm`; `--split dev|test`, `--negative` |
| `score_extraction.py` | 09.5: field-level eval and fairness slices for any run file (or the filled Track A sheet); writes `reports/<run>.md` |
| `runs/`, `reports/` | The rules baseline's run file, and the reports for the rules baseline and the vendor's Smart Intake (all documents, and per split) |
| [`expert/`](expert/README.md) | The expert's deliverables. **Open them in 09.6, after writing your own** |

## What each lesson uses

| Lesson | Files |
|---|---|
| 09.1 The call | `brief.md`; `data-room/` company, plans, reports, policies, governance, vendor release notes and email; persona Ilana |
| 09.2 Discovery | `data-room/claims/`, `siu/`, `complaints/`, the claims manual, the Fraud Insight configuration; personas Yusuf, Marina, Samira (Natalia optional); `baselines.py --section documents`, `bias_test.py` |
| 09.3 Diagnosis | register, document requests, payments, CRM, time study, SIU log, dashboard, finance summary, proposal, vendor email; persona Natalia; `baselines.py`, `bias_test.py --outcomes` |
| 09.4 The hard part | motor extract, configuration export, risk-areas list, SIU log, complaints, release notes, agreement, AI policy, minutes, inventory; personas Michael, Rana, Gil, Tamar; `bias_test.py` |
| 09.5 Build and decide | `pilot/`, `data-room/extraction/`, time study; personas Marina, Rana; `run_extraction.py`, `extract_rules.py`, `score_extraction.py` |
| 09.6 Readout and debrief | your deliverables; personas Ilana and the committee; `expert/` |

## Track A — no code

Open the CSV files in a spreadsheet (UTF-8; in Excel use *Data → From Text/CSV* and pick *65001:
Unicode (UTF-8)*). Use pivot tables and filters. Two formulas you need:

**Days between two timestamps.** Timestamps look like `2026-09-17T11:05:40+03:00`. Take the date part
with `=DATEVALUE(LEFT(A2,10))` and subtract.

**A 95% interval for a rate (Wilson).** For *k* referrals out of *n* claims, with *p* = *k*/*n* and
*z* = 1.96:

$$\frac{p + \frac{z^2}{2n} \pm z\sqrt{\frac{p(1-p)}{n} + \frac{z^2}{4n^2}}}{1 + \frac{z^2}{n}}$$

In a sheet with *k* in B2 and *n* in C2:
`=(B2/C2 + 1.96^2/(2*C2) - 1.96*SQRT(B2/C2*(1-B2/C2)/C2 + 1.96^2/(4*C2^2))) / (1 + 1.96^2/C2)` for the
lower bound, and the same with `+ 1.96*SQRT(…)` for the upper. Two groups whose intervals overlap are
not clearly different.

**The extraction pilot.** Use `pilot/system-prompt.md` as the instructions of a chat project. Open
`pilot/track-a-sheet.csv`, hide the columns `verified_value`, `smart_intake_value` and `rules_value`,
and for each document paste its text (from `data-room/extraction/documents/`) with its type and the
fields listed in the sheet. Copy each value into `your_value`, written as the gold is: dates
`YYYY-MM-DD`, amounts with a dot and no thousands separator (`4815.11`), identifiers as printed with
Western digits. Then unhide and add `=EXACT(J2,L2)` per row (J = verified, L = yours), and pivot the
result by `doc_language`, `capture_channel` and `region`.

## Track B — Python

Python 3.12+, the shared field kit and its pinned packages (no extra dependency for this module): set up
once as in [`labs/common/README.md`](../common/README.md). From this folder (`labs/module-09`):

```bash
python baselines.py                               # 09.3
python bias_test.py                               # 09.4, by language; --by risk_area | region | age | channel
python bias_test.py --factors
python bias_test.py --outcomes
python extract_rules.py                           # 09.5, the no-AI baseline
python score_extraction.py runs/rules-baseline.csv --split test
python score_extraction.py data-room/extraction/smart_intake_output.csv --split test
python run_extraction.py --split dev              # your pilot; iterate here, then --split test once
python run_extraction.py --negative
```

Choose the LLM provider with `FIELDKIT_PROVIDER` and `FIELDKIT_MODEL` (see the field kit README).
`FIELDKIT_PROVIDER=mock` runs the pipeline without a key and returns nothing useful. With a real model
the 240 documents cost a few US cents at list prices (about 800 tokens in and 60 out per document;
check your provider's price page and date it). Replies are cached in `.fieldkit-cache/`, so re-scoring
costs nothing.

> [!WARNING]
> The documents are synthetic, but treat them as if they were real claim files: send them only to an
> LLM account your organization has approved for this data, with no training on your inputs. Never
> paste real claimants' documents into a personal account; that is the shadow-AI finding of this module.

## Rebuilding the data room

`python data-room/generate.py` rebuilds every generated file byte for byte (Python standard library
only). Reading the generator spoils the engagement; finish the module first.
