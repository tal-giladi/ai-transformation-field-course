# Module 09 — notes for the main session

## Simulation preset proposals (no Meridian preset exists)

Lessons link only existing `generic` presets: `pilot-economics?preset=generic` (09.3, optional) and
`oversight-under-load?preset=generic` (09.5; its generic preset is already a claims-summary queue).
Proposed `meridian` presets, numbers from `curriculum/engagements/module-09.md`:

- **pilot-economics `meridian`**: volume 3,060 claims a month; automationRate 0.75 (he/ru/en documents
  pre-filled; ar not yet); accuracy 0.954 (illustrative pilot); minutesSaved 3.0 (keying 5.5 → 2.5);
  reviewMinutes 1.0; reworkMinutes 4; hourlyCost 145; tokensIn 2,400 / tokensOut 180 per claim (three
  documents); priceIn/Out 2 / 10 (Sonnet 5.5, 2 Nov 2026); fx 3.70; fixedMonthly 5,000; buildCost
  95,000. Shows that checking minutes, not tokens, decide the value.
- **oversight-under-load `meridian`**: 140 pre-filled claims a day per centre at peak, 4 handlers × 1.5 h
  of checking, 4.6% wrong fields, 1-minute check with source shown, target ≤ 10 wrong amounts reaching
  payment in two weeks.
- **steering-committee `meridian`**: cast Prof. Hanna Sela (chair, asks about the claimant), Avner
  Shamir (CEO, "where is my ₪20M?"), Ilana Bar-Lev (sponsor-as-advocate branch), Eran Paz (CFO),
  Michael Ohana (CRO), Natalia Gurevich (labels); paper = the 09.6 page one.
- **readiness-evidence-grader `meridian`**: the 09.1 first-read items (dashboard, 97.4%, AUC, ₪20M, June
  statement) as verified / reported / contradicted.

## Decisions taken in this module (for BUILD_PROGRESS / TODO_FOR_TAL)

- Entry role: internal Head of AI Transformation (differs from module 08's outside consultant), per the
  task.
- **EU AI Act: not applicable** to Meridian's claims systems (reasoning in 09.4 and the notes); used
  only as a benchmark and a re-check trigger.
- The fraud score is deliberately **not AI** under the 01.7 counting rule (a weighted rules list), to
  teach "classify by impact".
- LLM pilot numbers are an illustrative worked example (as in 05.4); vendor and rules-baseline numbers
  are real and reproducible.
- Expert deliverables live in `labs/module-09/expert/` (downloadable); the README warns to open them in
  09.6. Persona transcripts end with "Questions nobody asked" (questions, not answers) so the hidden
  facts are not spelled out in the download. The hidden truth and futures are only in 09.6 `<details>`.
- An answer key was generated to `curriculum/engagements/module-09-answer-key/` (writers only).

## Things Tal should review (sensitive content)

- The module's central finding is proxy discrimination against Arabic-speaking claimants and residents
  of listed postal areas. All data are synthetic and the risk-area list uses codes, not town names. The
  futures mention a fictional class-action motion by "an Arab civil-rights organisation" and a fictional
  information request from the CMISA public inquiries unit: no real organisation or real regulatory
  action is described. Worth a read before publishing.
- A fictional real-sounding vendor ("Kalanit Systems") is used; it is not a real company to my knowledge
  (no check of the Israeli companies register was made ⚠️).

## Facts I could not verify

- The text of the Prohibition of Discrimination Law and the CMISA consolidated circular's chapters were
  not opened directly; they are cited as quoted in the inter-ministerial report.
- Whether circular 2016-9-9 has since been folded into the consolidated circular with new numbering.
- No CMISA instrument specific to AI in claims was found; the lessons say so implicitly by relying on the
  claims circular, the outsourcing chapter and the (non-binding) inter-ministerial report.

## Cross-module consistency

- 01.7's counting rule ("a rules engine is not AI") is used in 09.4 and extended: govern by impact.
  Consider adding a line to 01.7 or 04.4 pointing forward to 09.4.
- Possible new template for the main session to consider (not drafted, not in the owner table): a
  **deployment verdict** (gate questions with pass / flag / block, verdict per system, conditions table,
  correction to the record, dissent). 09.4 uses the regulatory map + decision record instead.
- Glossary: I avoided redefining existing terms (shadow mode, negative test, no-AI baseline,
  measured / directional / assumed, recommend-against, integration check).

## Data room

- Size 2.53 MB (under 3 MB); `python generate.py` run twice, outputs identical (diff -r empty).
- 240 extraction documents are individual `.txt` files under `data-room/extraction/documents/`.
