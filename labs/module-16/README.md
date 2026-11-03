# Module 16 lab files — Open Hands

Everything you need to run the Open Hands engagement: the brief, the data room, the people you interview, the files for building and testing the two workflows, two small optional Python scripts, and (for the debrief only) the expert's deliverables. All people, families and organizations are fictional and all data is synthetic, but it imitates sensitive data about disabled children and their families: treat it that way.

> [!CAUTION]
> Build and test the workflows only on this synthetic data. In a real organization, the case-notes workflow runs only on the organization's own accounts, after the access fix, on de-identified text, within the data boundary you write in lesson 16.4 — never on a personal account and never with real case notes "to try it".

## What is in this folder

| Path | What it is | Lesson |
|---|---|---|
| `brief.md` | The engagement brief: how you were brought in, the stated ask, terms (40 hours, no fee, no budget), who you report to, access on day one | 16.1 |
| `data-room/` | Open Hands' data room: start with [`INDEX.md`](data-room/INDEX.md). Board minutes, budget, staff and volunteer lists, a one-week time log, the case register and a pseudonymised sample of 60 case notes, funders and donors, the grant library, the card statement, a Drive sharing report, an accounts list, the staff AI survey, policies and consent forms, the municipal agreement, vendor documents | 16.1–16.6 |
| `data-room/generate.py` and the other `.py` files there | The seeded generator (Python standard library only): `python generate.py` rebuilds every data file byte for byte. Reading it spoils the engagement | — |
| `personas/` | The cast of eight ([README](personas/README.md)): roleplay prompts and pre-run transcripts | 16.1–16.6 |
| `build/content-library/` | The grant drafter's only sources besides the boilerplate and outcomes framework: `numbers-2026-q1-q3.csv` (aggregated numbers Shira compiled) and `story-bank.md` (three stories approved by their families) | 16.5 |
| `build/grant-assistant-instructions.md` | Instructions for the grant drafter (v1.0) with change log | 16.5 |
| `build/casenotes-assistant-instructions.md` | Instructions for the case-note helper (v1.0) with change log | 16.5 |
| `build/grant-test-set.csv` | 10 grant sections across seven funders (English and Hebrew) and 3 negative tests, with what a good answer does | 16.5 |
| `build/casenotes-test-set.csv` | 9 positive tasks on notes from the sample, 1 consent test, 2 traps and 6 negative tests | 16.5 |
| `build/rating-sheet.csv` | Empty rating sheet for both test sets | 16.5 |
| `build/deid_check.py` | Optional Track B: flags identifiers in case notes, offline, rule-based | 16.5 |
| `discovery.py` | Optional Track B: access counts, donor sheet, survey, time-log pivot, funder hours, money already spent, consent counts | 16.2, 16.3 |
| `expert/` | The expert's deliverables for comparison in the debrief; open them only after your own ([README](expert/README.md)) | 16.6 |

## Track A — no code (the main path in this module)

1. Open the CSV files in Excel, Google Sheets or LibreOffice Calc. In Excel use *Data → From Text/CSV* and choose *65001: Unicode (UTF-8)*; the files contain Hebrew, Arabic and Russian text and commas inside quotes.
2. **16.2, access:** in `it/drive-sharing-audit.csv`, filter `item` = `Shared drives/Families` and pivot `principal_type`; look up each personal account's volunteer id in `people/volunteers.csv` (the email starts with the id) for `status` and `confidentiality_signed`. Filter `link_sharing` = `anyone with the link`.
3. **16.3, baseline:** pivot `people/time-log-2026-10.csv` with `staff_id` in rows, `activity` in columns and `SUM(minutes)/60`. Money: filter `finance/card-statement-2026.csv` by merchant; count Microsoft seats with a sign-in date after 14 August in `it/accounts-and-licences.csv`.
4. **16.5, build:** on the account you are allowed to use (for the course any chat tool is fine because the data is synthetic; in a real organization, the organization's own account), create a saved assistant — a Gemini Gem, a NotebookLM notebook, a ChatGPT or Claude project — paste the instructions and upload only the sources each instruction file lists. Paste each test item into a **new** conversation. Fill `build/rating-sheet.csv`. Run each trap (C11, C12) three times.

## Track B — Python (optional here)

Python adds little to most of this engagement: the data is small and a spreadsheet does it. Two scripts are provided because two jobs repeat every month after you leave: re-counting access, and checking an export for identifiers before anyone pastes text into a tool. Set up the field kit once ([instructions](../common/README.md)): Python 3.12 or newer and `pip install -r ../common/requirements.txt`. No extra packages, no API key, no network. From this folder:

```bash
python discovery.py                     # 16.2, 16.3: every count, with numerators and denominators
python discovery.py access money        # just the access and money sections
python build/deid_check.py              # 16.5: flags identifiers in data-room/cases/case-notes-sample.csv
python build/deid_check.py --text "..." # checks one piece of text
```

On Windows, if Hebrew or Arabic prints as `?`, run `$env:PYTHONIOENCODING = "utf-8"` first.

**What is real and what is not.** Every number computed from the data room reproduces exactly: 46 accounts on the family drive (31 personal, 23 inactive volunteers, 2 former staff; 9 roles need it), the care-sheet folder open by link since 14 August 2024, 14 donor-sheet editors (5 personal), 57.8 hours on the Adler-Haddad report in the logged week, ₪4,497 a year of avoidable software at ₪3.136 per US$, and the de-identification check flagging 7 of the 9 leaking notes. The AI test results in lesson 16.5 and in `expert/05` are an illustrative worked example, not a measurement; your run will differ.

Checked on 3 November 2026 with Python 3.14.3 and pandas 3.1.0 (the versions pinned in `../common/requirements.txt`). Nonprofit offers and prices were checked against the vendors' pages on 3 November 2026 (lesson 16.4); check them again before you rely on them. Exchange rate: Bank of Israel representative rate, ₪3.136 per US$ on 2 November 2026.
