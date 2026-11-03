# Module 15 lab files — Crescent Bank

Everything you need to run the Crescent Bank engagement: the brief, the data room, the people you talk to, a triage sheet for the spreadsheet track, two Track B scripts (discovery and portfolio triage), and (for the debrief only) the expert's deliverables. All people, organizations, vendors and data are fictional and synthetic. Bank of Israel directives and Israeli laws are real and referred to by name and number; what they require of any given AI use is for the bank's CRO, CCO and counsel to say.

## What is in this folder

| Path | What it is | Lesson |
|---|---|---|
| `brief.md` | The engagement brief: how you were brought in, money and authority, timeline, access on day one, constraints | 15.1 |
| `data-room/` | Crescent's data room: start with [`INDEX.md`](data-room/INDEX.md). Company profile, org chart, the board minute, the AI programme budget, the CFO's budget review; the pilot register, eval summaries, the assistant's usage, intake requests, IT's architecture notes; the AI policy, Model Committee minutes and queue, the model inventory, MRM's work plan, the answers to the supervisor's survey; the Branch FAQ's usage and the branch managers' forum; complaints; card and expense lines; AI contracts; the proxy extract; the people who work on AI and a staff directory | 15.1–15.6 |
| `data-room/generate.py` and the `gen_*.py` files there | The seeded generator (Python standard library only): `python generate.py` rebuilds every data file byte for byte. Reading it spoils the engagement | — |
| `personas/` | The cast of nine ([README](personas/README.md)): roleplay prompts and pre-run transcripts | 15.1–15.6 |
| `triage-sheet.csv` | Track A: all 43 register rows with their latest evaluation and empty columns for your copy, tier, issues, task family, action and merge decisions | 15.5 |
| `discovery.py` | Track B: the register's shape and gaps, rows that are the same build, owners, AI in real use, AI spend and traffic outside the register, the queue in slots, the assistant's usage with three denominators, auto-renewing contracts, the money | 15.2, 15.3 |
| `triage.py` | Track B: the triage rules (clean, tier, stop, merge, route), patterns among kept builds, the central review load under four designs, the money released; writes `out/triage.csv`; `--llm` asks an LLM whether same-pattern pairs are the same task | 15.5 |
| `expert/` | The expert's deliverables for comparison in the debrief; open them only after your own ([README](expert/README.md)) | 15.6 |

## What each lesson uses

| Lesson | Files |
|---|---|
| 15.1 The call | `brief.md`; `data-room/company/`, `governance/ai-policy-v1-2025.md`, `governance/bsd-ai-survey-response-2026-extract.md`, `governance/mrm-workplan-2027.md`; persona Dalit |
| 15.2 Discovery | `data-room/ai/`, `governance/`, `branches/`, `finance/`, `security/`, `procurement/`, `people/`; personas Irina, Nir, Karim, Hagit, Tsega, Lina, Olga; `discovery.py` |
| 15.3 Diagnosis | Your memo; the register, the work plan, the queue, the budget, the CFO's memo, complaints; personas Dalit and Avner |
| 15.4 The hard part | `governance/`, `ai/architecture-notes.md`, `ai/intake-requests-2026.csv`, `people/ai-people-by-unit.csv`, contracts, the org chart; personas Irina, Lina, Nir, Tsega; the simulation |
| 15.5 Decide | `triage-sheet.csv` or `triage.py`; `ai/`, contracts, `people/`, the CFO's memo; personas Hagit, Karim, Dalit; the simulation |
| 15.6 Readout | Your deliverables; personas Avner, Dalit, Irina, Nir, Lina; `expert/` |

The simulation is at `simulations/operating-model-scaler/index.html?preset=crescent` in the course (linked from 15.3–15.6); it is an educational model of the same bank, and every lesson works without it.

## Track A — no code

1. Open the CSV files in Excel, Google Sheets or LibreOffice Calc. In Excel use *Data → From Text/CSV* and choose *65001: Unicode (UTF-8)*; files contain Hebrew, Arabic, Russian and English, and commas inside quotes.
2. **15.2, the register:** sort `ai/pilot-register-2026-12.csv` by `environment`, then `test_set`, and look for rows that share both. Add a column with `=COUNTIFS(L:L,L2,T:T,T2)` (environment and test set) to flag them. Look up `business_owner` in `people/staff-directory-extract.csv` (`=XLOOKUP(F2,'directory'!A:A,'directory'!D:D)`). Normalise money first: `₪` and commas out, `k` × 1000.
3. **15.2, outside the register:** in `finance/card-and-expense-software-2026.csv` filter `merchant` for "AI" and "LLM" and check each against `procurement/vendor-contracts-ai.csv`; in `security/proxy-ai-hosts-2026-q4.csv` pivot `requests` and `upload_kb` by `department` and `host`, filtering out categories that start with "Sanctioned".
4. **15.2, usage:** in `ai/assistant-usage-2026.csv` sum `weekly_active_users`, `seats_assigned` and `users_onboarded` by `week_start` for December; for October–November pivot by `department`. In `branches/branch-faq-usage-2026-q4.csv` pivot `questions` by week.
5. **15.2, contracts:** add `notice_by = end − notice_days` and filter `auto_renew = Y` with a notice date before 15 March 2027.
6. **15.5, triage:** in a copy of `triage-sheet.csv`, fill `copy_of`, `tier` (the rule in 15.4), `issues` (against the stop rules), `task_family`, `action` and `merge_into`. Then pivot `budget_2027_ils` by `action`, and count the kept builds by tier to compute the review load (low 0.5, medium 1, high 2 slots; only high to the central queue under the new design).

## Track B — Python

Set up the field kit once ([instructions](../common/README.md)): Python 3.12 or newer and `pip install -r ../common/requirements.txt`. No extra packages. From this folder:

```bash
python discovery.py                 # 15.2-15.3: the discovery numbers, no AI
python triage.py                    # 15.5: the triage, the review load and the money, no AI
python triage.py --llm              # + an LLM second opinion on same-pattern pairs (about 70 short calls)
python triage.py --slots 4          # what one more AI slot a quarter changes
```

The provider and model for `--llm` come from `FIELDKIT_PROVIDER`, `FIELDKIT_MODEL` and your provider's key variable (see the [field kit README](../common/README.md)); every call goes through `fieldkit.llm.complete` and is cached in `.fieldkit-cache/`. `FIELDKIT_PROVIDER=mock` runs it without a key (the answers are meaningless, but the pipeline is proven). On Windows, if Hebrew prints as `?`, run `$env:PYTHONIOENCODING = "utf-8"` first. The scripts read the data room by relative path and make no network request except the LLM call; `triage.py` writes `out/triage.csv` (delete the folder when you are done).

Python is worth it in this module because the triage is not a one-off: the catalogue will be re-triaged every quarter with the same rules, the register's formats (three spellings of a unit, four date formats, three money formats) must be cleaned the same way every time, and duplicates hide across Hebrew and English descriptions that a spreadsheet filter misses. The LLM is a second opinion on pairs, never the decision.

**What is real.** Every number the two scripts print reproduces exactly from the data room (seed 20270103): 43 rows, 40 builds, 10 stops, 4 merges, 3 copies, 26 kept (12 low, 8 medium, 6 high), 80 slots today against 12 under decision rights by tier, ₪2.74M of unit lines released. The simulation's numbers in the lessons come from its `crescent` preset and are an educational model.

Checked on 3 November 2026 with Python 3.14 and the versions pinned in `../common/requirements.txt`, end to end with `FIELDKIT_PROVIDER=mock`. Card lines in US$ use the card issuer's monthly conversion recorded in the data; the course's reference rate is ₪3.136 per US$ (Bank of Israel representative rate, 2 November 2026).
