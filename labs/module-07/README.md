# Module 7 lab files — Readouts, decisions and the operating rhythm

Everything module 7 uses beyond the shared Harbor & Pine data room: a softened steering paper to critique, roleplay scenes and pre-run transcripts for the conversation with the CEO and the steering meeting, the pilot log's gate-1 readings, the intake register at the end of March, a paper version of the incident tabletop, spreadsheet versions of the module's templates, and one Python script for the gate-1 evidence. The data room is in `../common/harbor-and-pine/` (start with its [INDEX](../common/harbor-and-pine/INDEX.md)); it comes with this download. Lessons 07.2, 07.6 and 07.8 also read two files from the module 6 download (`labs/module-06/champions-issues-log.csv` and `queue-rota-2027.csv`). All people and companies are fictional and all data is synthetic; the pilot's production readings for February–March 2027 are the course story's, written for the exercise.

## What is in this folder

| File | What it is | Lesson |
|---|---|---|
| `integration-check.csv` | Integration check log: five contradictions found on 14 January 2027, with resolutions (spreadsheet version of the template) | 07.1, 07.9 |
| `gate-1-readings.csv` | The pilot log's gate readings, 15 Feb – 28 Mar 2027, per channel and language: eligible tickets, tickets with a draft used, drafts shown and accepted, median review seconds | 07.2 |
| `gate-1-weekly.csv` | The same by week and channel, with the spot audit and the share of "where is my order?" contacts | 07.2 |
| `gate-1-other-readings.csv` | Other gate inputs: minutes per contact (drafted, holdout, before WhatsApp drafts), today's wrong-reply rate, peak forecasts, incident counts, stage-1 spend, each with its label | 07.2 |
| `intake-register-2027-03.csv` | The AI intake register on 31 March 2027: eleven entries, including a duplicate build found in March and four requests for new money | 07.2 |
| `gate1_evidence.py` | Track B: joins the usage export with the HR roster and the module 6 rota, and prints the gate table, the adoption gate and the hours at peak | 07.2 |
| `steering-paper-softened.md` | Your steering paper as the sponsor returned it, with the bad news edited out | 07.3 |
| `roleplay.md` | The 07.3 scene for Yoav and the 07.4 steering-meeting prompt (five members), with set-up steps | 07.3, 07.4 |
| `yoav-bad-news-transcript.md` | Pre-run conversation with Yoav on 17 January 2027 (no-roleplay path) | 07.3 |
| `steering-meeting-transcript.md` | Pre-run steering meeting of 19 January 2027 (no-roleplay path) | 07.4 |
| `incident-injects.md` | Paper tabletop of the 15 March 2027 incident: six injects and facilitator's notes | 07.5 |
| `operating-rhythm.csv` | Operating rhythm: columns and three example rows | 07.6 |
| `pressure-test-log.csv` | Pressure-test log: columns and one example row | 07.7 |
| `phase-1-plan.csv` | Phase-1 plan: columns and two example rows | 07.8 |
| `deliverable-map.csv` | Deliverable map: columns and three example rows | 07.9 |

## Track A — no code

1. Open the CSV files in Excel, Google Sheets or LibreOffice Calc. In Excel use *Data → From Text/CSV* and choose *65001: Unicode (UTF-8)*.
2. **07.2, gate table:** in `gate-1-readings.csv`, acceptance per segment = `drafts_accepted / drafts_shown`; for a channel or a language, sum both columns over its rows before dividing (never average the percentages). Share of tickets with a draft = `tickets_draft_used / eligible_tickets`, per week from `gate-1-weekly.csv`. Hours at peak: forecast contacts × share with a draft × minutes saved ÷ 60, per channel, from `gate-1-other-readings.csv`; the date fix's hours are 247 × (1 − WISMO share after ÷ WISMO share before).
3. **07.2, who stopped:** from the data room, pivot `usage/ai-usage-export.csv` (filter `feature = draft_inserted`; rows user, columns week = `INT((date − 1 Feb 2027) / 7) + 1`), then look up `usage/hr-roster.csv` for status and the module 6 rota for the queue. Report by queue, never by person (lesson 06.4).
4. **07.3–07.5:** the roleplays work in any LLM chat; follow `roleplay.md`. The paper tabletop needs a facilitator and two to five colleagues.
5. **07.6–07.9:** fill the CSV templates; each has example rows to replace.

## Track B — Python

Set up the field kit once ([instructions](../common/README.md)): Python 3.12 or newer and `pip install -r ../common/requirements.txt`. No extra packages and no API key are needed. From this folder:

```bash
python gate1_evidence.py                                         # gate table, adoption gate, hours at peak
python gate1_evidence.py --whatsapp-use 0.5 --whatsapp-saving 1.5  # what a half-fixed WhatsApp buys
python gate1_evidence.py --who                                   # analyst only: the per-person table
```

Why Python here: the gate needs two joins (usage export with the HR roster and the queue rota; pilot log by channel and language) that are easy to get wrong by hand, and the hours at peak depend on assumptions you will want to vary. The script prints use per queue by default; the per-person table prints only with `--who`, because the AUP promises usage reporting by team, not by person. It expects the module 6 download unpacked next to this folder (`../module-06/`); without it, the queue view is skipped. Checked with Python 3.14 and pandas 3.1.0 on 2 November 2026.
