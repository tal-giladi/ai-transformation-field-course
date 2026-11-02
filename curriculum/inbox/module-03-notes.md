# Module 03 — notes for the main session

Written 2026-11-02 by the module 3 agent. Nothing committed.

## For the sidebar (lesson titles = H1s)

03.1 · The opportunity map · 03.2 · Agent or not · 03.3 · The fast screen · 03.4 · Scoring with evidence, not opinions · 03.5 · Running the scoring workshop · 03.6 · The leadership alignment session · 03.7 · The ROI model that survives finance · 03.8 · The roadmap · 03.9 · The decision-ready case. Module quiz: `assessments/module-03-quiz.md`. Project: `projects/m03-portfolio.md`.

## Templates

All eight M3 templates are complete drafts in `curriculum/inbox/templates/`: opportunity-map, agentic-opportunity-frame, use-case-scorecard, scoring-workshop-script, alignment-session-agenda, roi-model, roadmap, decision-ready-case. Spreadsheet versions in `labs/module-03/` (`opportunity-map.csv`, `use-case-scorecard.csv`, `roi-model.csv`), linked from the template pages as `../labs/module-03/<file>.csv`. With the templates copied into `templates/`, `check-module.mjs 03` reports 0 problems (tested in a scratch copy).

## Simulations vs data room (lessons follow the data room)

1. **portfolio-sorter, `delayNotify` card:** evidence says WISMO "spikes 3–10 days after container delays"; the data room puts the cluster a median 12 days after the container's original ETA (10–15), i.e. 0–4 days after the promised date passes (writer's notes, finding 1). Volume "1,500 delay emails a month": orders on containers that slipped 7+ days are about 210 a month (May–Oct, `orders.csv` × `shipments.csv`). Suggest "about 210 orders a month get a delay email".
2. **portfolio-sorter, `damageClaims` card:** "about 260 claims a month" vs 149 claims in six months (about 25 a month) in `claims/damage-claims-log.csv`; "missing for about 35%" vs 32.2%. Lesson 03.4 turns this into a "check the card against the data" point (Step 6, reference answer, quiz q5; module quiz q4; project model answer). If you fix the card, those lines still read correctly as a past check, but 03.4 Step 3's error-cost table quotes 260 × 12% × ₪1,200 from the card; update it to the new card numbers.
3. **portfolio-sorter, `assembly` card:** "about 9% of tickets", "540 a month" vs 6.2% true (answer key), about 25 a month in the helpdesk. Same handling as 2.
4. **portfolio-sorter, `quotes` card and the B2B team:** proposer and contact "Hadar Klein, B2B sales lead". `company/org-chart.md` has no Hadar Klein; the Head of B2B Sales is **Yaniv Carmi** (HP-1025). Lessons use Yaniv. Suggest renaming in the sim. Yaniv's two-week time study (68 quotes, 45 min, 140 a month) exists only in the sim; lessons mark it "reported".
5. **roi-defender, claim `temps`:** the text says "the temps' 960 hours", but the netting moves ₪96,000 (= 738 hours at ₪130) out of claim 1; the README's "about 567 hours of capacity" follows the shekel figure (with 960 hours it would be 346). Suggest dropping "960 hours" from the text or saying "₪96,000 of claim 1's capacity". Lessons quote capacity in shekels (₪73,740) to avoid it.
6. **roi-defender, the temps claim is fragile on peak timing:** two full-time temps give about 320 hours a month in the peak; the pilot frees 108.8 net hours a month (pilot-economics). Even with the date fix's expected ~120 hours (half of ~247 WISMO hours a month in October), only one temp is clearly covered. Lesson 03.7 keeps the instructed headline (₪113k cash, NPV ₪33,717, payback 22.5 months, ₪267k → board) as the expected case, flags this as the case's most fragile assumption (sensitivity: one temp only → NPV −₪81,571) and makes it gate 1 condition (d). If you want the sim to teach it too, add it to the claim's `truth.note`.
7. **roi-defender, claim `drafts` basis:** "three weeks of shadow mode" in a January 2027 deck, but the roadmap (03.8, and the 03.5/03.6 decisions) puts shadow mode in February–March 2027, after the board. Lessons say "measured on a sample of 400 real emails". Suggest removing "and three weeks of shadow mode".
8. **The temps exist only in roi-defender** (assumption for the exercise). The 03.6 pre-run transcript has Samir mention them ("I took on two temps in November for the peak, like every year"). Suggest adding to `personas/samir-cs-manager.md` (WHAT YOU KNOW: two temps each November–January, about ₪16,000 a month each, decided with Michal) and to the writer's notes, so a roleplay can surface them.
9. **simulations/README.md, pilot-economics table:** `fx` shows 3.6 for `harbor`; the preset uses 3.7 (the CFO's planning rate). Cosmetic.

## Other cross-module points

10. **Weekdays in pre-run transcripts:** `personas/transcripts/yoav-ceo.md` says "Tuesday 2 December 2026" (it is a Wednesday); `personas/transcripts/ronit-cfo.md` says "Monday 17 November 2026" (a Tuesday). Module 3 cites both meetings without weekdays.
11. **Timeline with module 2:** M2's findings memo is dated 1 December with decisions on 10 December. Module 3 runs the opportunity map, frames and screen 16–24 November and the scoring workshop on Thursday 26 November, from findings already in hand ("the memo goes to Michal on 1 December"); the Yoav one-to-one is 2 December (his transcript), the alignment session 10 December, the ROI model to Ronit by 14 January, the board pre-read 21 January. Free-ChatGPT use is described as stopped by the 12 November interim rule (M1/M2).
12. **Gantt in 03.8** uses a mermaid `gantt` block; please check it renders in the Academy viewer.
13. **Group roleplay:** `labs/module-03/group-roleplay.md` is a meeting prompt that loads the four persona prompts; it lives in module 3's lab, not in `labs/common/`. If later modules (07.4) want the same pattern, it could move to `labs/common/`.

## Facts I could not fully verify (also ⚠️ in module-03-sources.md)

- *Moffatt v. Air Canada*: tribunal page, CanLII and CBC returned 403; used a law-firm summary (negligent misrepresentation, CA$650.88). The lesson states no decision date.
- Klarna's May 2025 reversal is from a secondary report of a Bloomberg interview.
- PPA draft AI guidance: law-firm summary only (still a draft).

## For Tal to decide

- Nothing blocking. One design choice to confirm: 03.7 presents the instructed ₪113k / ₪33,717 expected case and, in the same lesson, shows that it rests on a peak-capacity assumption that today's numbers only half support (point 6). I think that makes the lesson stronger; the alternative is to change the roi-defender temps claim to one temp (₪48,000), which would make the expected NPV negative and change the board story.

## Module time (for BUILD_PROGRESS)

Reading 159 min + practice 745 min + project 360 min + quizzes 30 min ≈ 21.6 hours.

## Track B check

`labs/module-03/roi_model.py` was run on 2026-11-02 with Python 3.14.3, pandas 3.1.0, tabulate 0.10.0 in a scratch venv; its output matches lesson 03.7 (pilot-economics harbor: 108.8 net hours, ₪10,048 a month, breakeven 11.9 months; roi-defender harbor: expected ₪113,000 cash, NPV ₪33,717, payback 22.5 months, three-year cost ₪267,000 → board). It makes no LLM or network calls. `roi-model-harbor-solution.csv` is its `--csv` output.
