# Module 05 — notes for the main session

Written 2026-11-02 by the module 5 agent (resumed after a crash). Nothing committed.

## For the sidebar (lesson titles = H1s)

05.1 · The pilot charter · 05.2 · Building the test set from real data · 05.3 · Build it — Track A and Track B · 05.4 · Evaluate: accuracy, failures, cost and time saved · 05.5 · Human-in-the-loop design that actually checks · 05.6 · Shadow mode, staged release and rollback · 05.7 · Before launch: logging, monitoring and change control. Module quiz: `assessments/module-05-quiz.md`. Project: `projects/m05-pilot.md`.

## Templates

All seven M5 templates are complete drafts in `curriculum/inbox/templates/`: pilot-charter, value-measurement-plan, test-set-spec, eval-report, human-review-design, monitoring-spec, production-readiness-checklist. Spreadsheet versions: `labs/module-05/scoring-sheet.csv` (eval report) and `labs/module-05/monitoring-signals.csv` (monitoring spec), linked from the template pages as `labs/module-05/…` text (not as links, to avoid a broken path before merge; turn them into links if you like: `../labs/module-05/scoring-sheet.csv`).

Lessons also link module 4 by the build-spec names (`../module-04/lesson-02.md`, `lesson-05.md`; templates `data-boundary`, `dpia-for-ai`, `risk-register`, `ai-intake-register`); these resolved at the final check. With the seven M5 templates copied into `templates/` (tested in a scratch copy), `check-module.mjs 05` reports 0 problems.

## Labs: what is real and what is illustrative

- Real and reproducible (`build_test_set.py`, `run_pilot.py --mode baseline`, `score.py --today`): test set composition; pseudonymisation counts (names 840 + 53 second pass, phones 205, addresses 21); order numbers (352 helpdesk field, 38 found in text, 210 none); order context on 260 test items, expected date on 163 (138 of them WISMO); helpdesk category field right on 64.0% of test messages, language 91.2%; keyword baseline 98.2% test / 99.5% dev, 2 of 24 negative tests; agent replies: 5 of 368 in the wrong language (1.4%), 96 of 151 WISMO replies with a date already past (63.6%), 2 chatbot traces; oversight-under-load results quoted in 05.5 (computed with the simulation's `model.js`); pilot-economics variants (fieldkit `pilot_value`).
- Illustrative, labelled as such in 05.4's reference answer and the project model answer: all LLM figures (triage 97.5%, acceptance 82% with per-language 86/85/79/72, negative tests 22→24 of 24, rating time 1.9 min, failure counts). No API key was available, so no real LLM run was made. They are not attributed to any named model. If Tal wants real numbers, run `python run_pilot.py --set test` and `--set negative` with a key and replace them (also in `projects/m05-pilot.md`).
- `labels.csv` is generated from the answer key (`emails-truth.csv`: true category, language, kind) and ships in the module download as "the team's adjudicated labels". This puts true categories for all 600 emails in the module 5 zip; a learner in module 2 could use it to shortcut the WISMO-share exercise. Acceptable in my view; Tal may decide otherwise.
- The keyword baseline reaches 98.2% because the generated emails repeat a limited set of phrasings. Lessons say so and turn it into a design point (route on rules, use the model for drafts, reply language and flags). If the data room is ever made messier, the 05.4 numbers change; re-run `score.py`.
- Track B verified end to end on 2026-11-02 with Python 3.14.3 / pandas 3.1.0 / tabulate 0.10.0 and `FIELDKIT_PROVIDER=mock` (dev, test, negative); the JSON/draft-check path was also exercised with a fake JSON provider in a scratch script (not shipped).

## Cross-module inconsistencies (please decide or fix in the other module)

1. **Money and gate dates.** 03.7 / 03.9: ₪48,000 now and ₪72,000 from 1 April if gate 1 is met. The writer's notes timeline: steering 19 Jan approves "₪60,000 now and ₪60,000 at the May gate". Module 5 follows 03.7/03.9 (the brief said the charter must match them) and mentions the May steering review only as 07.2. Module 7 must pick one.
2. **Test set size.** 02.6 (R-08) and 02.5 speak of "200 coded messages"; 03.7 and module 5 use 400 (+200 dev). 05.2 explains the change (400 needed for the gate's per-language reading).
3. **Language staging.** 03.8 (roadmap, Step 6 and gantt) puts Russian and Arabic drafts four weeks / months after Hebrew and English; the usage export (`usage/ai-usage-export.csv`) shows Russian and Arabic agents inserting drafts from 1 February. 05.6 resolves it as a steering decision on 19 January (roadmap v1.1: all four languages from 1 February, with per-language spot checks and stop rules). 07.x should refer to roadmap v1.1.
4. **Shadow mode.** The writer's timeline says "1 Feb: shadow mode, then staged release"; the usage export has drafts inserted on 1 February. 05.6 runs shadow mode on WhatsApp (the channel the offline test did not cover) from 1 February and stage 1 (drafts on request) for email and web form from 1 February. Suggest updating the writer's notes timeline accordingly.
5. **Training 7–11 Feb vs inserts from 1 Feb.** 05.6 has the eight agents from a 28 January walkthrough using drafts until training; the export shows all 14 wave-1 licence holders inserting from day 1. Minor; module 6 may want to say the walkthrough covered everyone.
6. **Prompt versions.** 05.3/05.4/05.7 story: v1.0 (15 Dec) → v1.2 (frozen 22 Dec) → v1.3 (after negative tests) in production on 1 February; `labs/module-05/system-prompt.md` ships v1.0 only (the learner's starting point).
7. **Incident of 15 March (07.5).** 05.7 points to it; its negative tests (refund outside policy, another customer's data) match the incident-tabletop scenario.
8. **Module 6 training** is described in 05.5 as including "20 real drafts, 5 of them wrong (planted)". Module 6 may adopt or change this.

## Facts I could not fully verify (⚠️ in module-05-sources.md)

- OpenAI ChatGPT Business data terms and projects (403): named as an option only.
- PPA guide to regulation 10(d): law-firm summary only.
- PPA draft AI guidance: law-firm summary only (still a draft).
- EU AI Act Article 50: AI Act Explorer, not EUR-Lex.

## For Tal to decide

- Whether shipping `labels.csv` (true categories of the 600 emails) in the module 5 download is acceptable.
- Whether the illustrative LLM numbers should be replaced by a real run with an API key before publishing (recommended, ~US$2–5 for 624 items with a mid-tier model).

## Module time (for BUILD_PROGRESS)

Reading 18+18+20+20+18+18+20 = 132 min; practice 90+90+120+150+75+75+90 = 690 min; project 360 min; quizzes 30 min. Total 1,212 min ≈ 20.2 hours.
