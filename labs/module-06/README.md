# Module 6 lab files — Making people use it

Everything module 6 uses beyond the shared Harbor & Pine data room. The data room itself is in `../common/harbor-and-pine/` (start with its [INDEX](../common/harbor-and-pine/INDEX.md)); it comes with this download, and so do the personas in `../common/harbor-and-pine/personas/`. All people and companies are fictional and all data is synthetic.

## What is in this folder

| File | What it is | Lesson |
|---|---|---|
| `workflow-redesign.csv` | The step table of the workflow redesign (three example rows) | 06.1 |
| `training/session-script.md` | The 60-minute role-based session "Your drafts, your call": run sheet, session 2, role versions | 06.2 |
| `training/exercise-cards.md` | Eight exercise cards: real customer messages in Hebrew, Arabic, Russian and English with a draft that hides one error each (two cards written for the session) | 06.2 |
| `training/trainer-answer-key.md` | The answers and the check each card teaches (trainers and champions only) | 06.2 |
| `training/job-aid.md` | The one-page job aid beside the screen | 06.2 |
| `training/run-sheet.csv` | Groups, dates, co-trainers and queue cover for 7–11 February 2027 | 06.2 |
| `training/proficiency-check.csv` | The exit-check sheet (two example rows) | 06.2 |
| `queue-rota-2027.csv` | Samir's queue rota by pilot week, 1 February – 28 March 2027: main queue, WhatsApp days, champion time, leave, training | 06.3, 06.4 |
| `champions-issues-log.csv` | The champions' issues log, weeks 1–8 | 06.3, 06.4, 06.6 |
| `adoption_dashboard.py` | Track B: joins the usage export, the HR roster and the rota; prints the vendor view, the population, the qualified-use rate, the threshold check, licences, and quiet non-adoption | 06.4 |
| `adoption-dashboard-metrics.csv` | The dashboard's metric definitions, who sees each and what it is never used for | 06.4 |
| `faq-first-draft-with-dana-comments.md` | A first FAQ draft from the COO's office with the HR manager's comments, to rewrite | 06.5 |
| `comms-plan.csv` | The comms sequence: when, audience, message, messenger, channel, languages, approver, feedback route | 06.5 |
| `roleplay/scene-cards.md` | March 2027 updates to paste after the Samir, Olga and Dana persona prompts | 06.6 |
| `roleplay/transcript-samir-2027-03-30.md`, `transcript-olga-2027-03-31.md`, `transcript-dana-2027-03-31.md` | Pre-run conversations for learners who prefer not to roleplay | 06.6 |

The data room files used most in this module: `usage/ai-usage-export.csv` and `usage/hr-roster.csv` (06.4), `support/emails.csv` (06.2), `company/customer-service-handbook.md` and `support/whatsapp-week-tally.csv` (06.1). Lesson 06.4 links the adoption-dynamics simulation; the lesson works without it.

> [!NOTE]
> The exercise cards contain last year's real (synthetic) customer messages. In a real organization, keep printed cards inside the office and shred them after the session, as you would any customer data.

## Track A — no code

1. Open the CSV files in Excel, Google Sheets or LibreOffice Calc. In Excel use *Data → From Text/CSV* and choose *65001: Unicode (UTF-8)*.
2. 06.4: in `../common/harbor-and-pine/usage/ai-usage-export.csv` add a column `week` with `=INT((A2-DATE(2027,2,1))/7)+1` (column A is the date). Insert a pivot table: rows `user_email`, columns `week`, values sum of `events`, filter `feature` = `draft_inserted`. Next to it, look up each person's `role`, `employment_status` and `status_since_date` from `hr-roster.csv` (XLOOKUP or VLOOKUP on email). For each week, count the people in the population (support agent roles, active on that week's Monday) with 5 or more. Then look up each person's `main_queue` per week from `queue-rota-2027.csv`.
3. Roleplays (06.5, 06.6): paste the persona's prompt into any LLM chat, then the scene card as a second message ([how](../common/persona-format.md)); get feedback with the [coach prompt](../common/coach-prompt.md).

## Track B — Python

Set up the field kit once ([instructions](../common/README.md)): Python 3.12 or newer and the packages in `../common/requirements.txt` (this script needs pandas only). No API key and no network access are needed. From this folder:

```bash
python adoption_dashboard.py
python adoption_dashboard.py --threshold 10
python adoption_dashboard.py --who
```

The first prints the team-level dashboard tables; `--threshold` changes the qualified-event threshold; `--who` adds the per-person view of quiet non-adoption, meant for the pilot lead only (read the note at the top of the script). On Windows, if Hebrew or dashes print as `?`, run `$env:PYTHONIOENCODING = "utf-8"` in PowerShell first.

Python is worth it here because the dashboard is rebuilt every week from a new export, and the joins (HR status by week, the rota by week) are where spreadsheet copies go wrong.

Checked on 2 November 2026 with Python 3.14.3 and pandas 3.1.0.
