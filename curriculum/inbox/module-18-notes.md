# Module 18 — notes for the main session (capstone)

## Sidebar entries (titles match the H1s)

- 18.1 · The unseen org — `lessons/module-18/lesson-01.md`
- 18.2 · The full deliverable set and the integration check — `lessons/module-18/lesson-02.md`
- 18.3 · The executive presentation — `lessons/module-18/lesson-03.md`
- 18.4 · Optional: a real engagement in your own workplace — `lessons/module-18/lesson-04.md`
- 18.5 · Your practice kit and portfolio — `lessons/module-18/lesson-05.md`
- Module 18 quiz — `assessments/module-18-quiz.md`

Suggested module line: `- **Module 18 — Capstone: Your Engagement**`.

## Design decisions

- The unseen org is **Tzurim Academic College**, a fictional private (non-budgeted) college with 6,840 students and 712 staff, a sector no earlier module used. Stated ask: an AI early-warning system for dropout. Writer's notes with the hidden truth, every planted finding and the futures: `curriculum/engagements/module-18.md`.
- **No hints before submission.** Lessons 18.1–18.3 use Kinneret Plastics (13) and Harbor & Pine (07) for worked examples and reference answers, never Tzurim. The hidden truth, futures and expert links are only in `projects/m18-capstone.md` inside `<details><summary>Open only after you have submitted your deliverables</summary>`; the expert set is in `labs/module-18/expert/`, which is downloadable, so the lessons, the lab README, the expert README and the project page warn plainly not to open it early. Please don't add links into `expert/` anywhere learners see before the project page.
- No Track B discovery script for the capstone (unlike modules 8–17), on purpose: learners write their own on `fieldkit`. The only script outside the generator is `expert/make_test_set.py`, which rebuilds the expert's test set and prints the portal's routing baseline (real numbers).
- No new templates. Module-specific sheets in the lab: `capstone-checklist.csv`, `presentation-scoring-sheet.csv`, `real-engagement/permission-and-data-plan.md`, `practice-kit/practice-kit-index.csv`, `practice-kit/portfolio-piece-checklist.md`.
- `fieldkit.data.load` converts all-number columns to numbers, which drops leading zeros of student numbers in this data room. The INDEX and the lab README tell learners to read identifier files with `pd.read_csv(..., dtype=str)`. A `keep_text=[...]` option in `fieldkit.data.load` would help every module; consider it for `labs/common/` (shared, not edited here).
- 18.2 and 18.3 reuse Kinneret facts from 13.6 and module 13's expert set (bar dated 14 February; IC-01 to IC-03; the rehearsal). If module 13 changes, re-check those two lessons.

## Checks run

- `python generate.py` twice: byte-identical (diff -r), 2.55 MB, 36 data files.
- `python expert/make_test_set.py` twice: identical `test-set-240.csv` (md5 8d15c1410b6cf44c90dd492beee2284b).
- `node curriculum/tools/check-module.mjs 18`: 0 problems.

## Facts I could not fully verify (⚠️)

- The PPA's 2025 anonymisation guidelines and Guideline 5/17 on workplace cameras are cited via the Chambers 2026 guide (secondary); gov.il not opened.
- The Hebrew Wikisource text of the Privacy Protection Law does not label Amendment 13 by name; section numbers (2(8), 2(9), 3, 11) are from that page.

## For Tal

- A stray placeholder file was created by mistake at `C:\TALGIL~2\placeholder.txt` (a new folder `C:\TALGIL~2`, outside the repo). The safety check blocked removing the folder; please delete the folder by hand.
- Capstone project time: about 15 hours beyond the exercises in 18.1–18.3. Module total about 42 hours.
