# Proof of concept — Galil Health ambient scribe (December 2026)

These files are the result of the proof of concept run in lesson 10.4. Open them after you have written
your own PoC protocol: they show what Galil's run produced.

## How it was run

- **Visits.** 90 synthetic visits, 30 in Hebrew, 30 in Arabic, 30 in Russian, written by the CMO's team from
  real-shaped scenarios (primary care and the four specialist centres) and recorded by drama students
  playing doctors, patients and relatives in two of Galil's consultation rooms, 8–10 December 2026. No real
  patient took part. `visits-90.csv` lists them.
- **Runs.** Each vendor received the 90 recordings under an NDA for synthetic data and processed each one
  **twice** (13–20 December), so each vendor produced 180 notes. Kol Refua returned empty notes for every
  Arabic recording.
- **Review.** Six clinicians, two per language, compared every note with the script's fact list
  (21–30 December), blind to the vendor where the format allowed. `review-sheet.csv` has one row per note.
- **RFP answers.** `rfp-responses.csv` holds each vendor's answer to every contract term in the RFP
  (received by 20 December).

## Columns of `review-sheet.csv`

| Column | Meaning |
|---|---|
| `vendor`, `poc_visit_id`, `run`, `language` | Which note |
| `status` | `scored` or `no_output` |
| `wer_pct` | Word error rate of the vendor's transcript against the script, % |
| `facts_total` | Clinically relevant facts in the script's fact list |
| `omitted_relevant` | Facts from the list missing or wrong in the note |
| `invented` | Findings in the note that were not said in the visit |
| `omissions_flagged` | Omissions that sat inside a passage the tool had marked "unsure" |
| `passages_flagged` | Passages the tool marked "unsure" in this note |
| `minutes_to_correct` | Reviewer's timed minutes to bring the note to a signable state |
| `reviewer_id`, `reviewer_note` | Who reviewed it; a short note |

Rates "per 100 notes" are counts divided by the notes the vendor produced, times 100.
