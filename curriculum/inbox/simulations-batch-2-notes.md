# Simulations batch 2 — notes for the main session

Written 2026-11-02 by the simulations agent. Nothing committed.

## Done

- `steering-committee` (07.4), `incident-tabletop` (07.5), `risk-register-tester` (04.5),
  `roi-defender` (03.7), `readiness-evidence-grader` (02.6): each `index.html` + `app.js` +
  `model.js` (pure, exports `validateScenario`) + `presets.js` (`harbor`) + `<name>.css`.
- `simulations/common/`: added `table.js` (`stackTable`, a table that becomes labelled blocks below
  640 px, with explicit ARIA roles) and a `table.stack` block in `sim.css`. Additive only; no batch-1
  file uses it, and batch-1 checks were re-run (below).
- `simulations/README.md`: the five sims in the table, URL examples, the batch-2 preset fields, and
  "How an engagement module adds a preset".

For BUILD_PROGRESS.md: tick "Simulations batch 2". Lesson links, all `?preset=harbor`: 02.6
readiness-evidence-grader, 03.7 roi-defender (after pilot-economics), 04.5 risk-register-tester,
07.4 steering-committee, 07.5 incident-tabletop.

## Checks run (scripts in the session scratchpad, not the repo)

- `node --check` on every `.js` in `simulations/`: clean.
- `scratchpad/sims/model-test-2.mjs`, 27 checks, all pass: every scenario passes `validateScenario`
  (and a deliberately broken one is caught); steering: all 20,736 paths enumerated, every outcome and
  every round reachable, the strong path ends "approved with conditions" with the sponsor kept, the
  blunt correction keeps the paper and loses the sponsor, no ask means no decision, the overclaim path
  is killed or sent back; incident: the runbook path harms nobody new, contains in 15 minutes and
  matches every step, the worst path harms 22 more and never contains, the late-fix decision only
  appears when unfixed, no "best" option states a legal deadline; risk register: owners' register
  credibility 25, a good tester reaches 83 with no unearned greens within budget, testing everything
  costs more than the budget; ROI: claims sum to ₪1,360,000, defensible ₪113,000 cash and 567 h, NPV
  ₪33,717, payback 22.5 months, three-year cost ₪267,000 so the board, claim 1's hours equal
  pilot-economics `harbor`; grader: honest + phase scores 100 and is approved, all-verified is
  over-claimed and gets the other reaction.
- `scratchpad/sims/ui-test-2.mjs` (batch 1's DOM stub): all ten flows pass (two per sim: a strong and a
  weak path to the debrief, restart, unknown preset): labels on every input/select, every button
  `type="button"`, no duplicate ids, no NaN/undefined in text.
- Batch 1 re-run after the `common/` change: `model-test.mjs` 21 passed, `ui-test.mjs` all flows pass.
- Built-in browser through the batch-1 static server: all five pages load with no console errors, no
  horizontal page scroll at 360 px after playing each one to the debrief, dark mode applies, keyboard
  Enter on a choice advances and moves focus to the next question, 1100 px two-column layout fine;
  pilot-economics re-checked (no errors, ₪10,051 still shown). The sandboxed-iframe case was not run
  (same reason as batch 1).
- Grep: no http(s) URLs, fonts, CDNs, fetch, innerHTML, alert/prompt/confirm, forms, localStorage
  (the only hits were "laptop." and "tabletop.css"). UTF-8, LF, no BOM.

## Harbor numbers assumed (also in each preset's `notes`)

- Steering: the paper (₪113,000 cash a year, about 570 agent-hours, ₪60,000 + ₪60,000 staged, May
  gate at under 4 minutes a review and fewer than 1 in 100 sent replies corrected), meeting on
  19 January 2027, WISMO down about 40% since the date fix, all "six months later" results.
- Incident: Monday 15 March 2027; damage/returns emails about two an hour; 7 replies promising
  refunds plus 1 disclosed address before detection; ₪21,000 to honour them; the cause (a shared-drive
  folder with the 2023 returns policy and a 2025 claims export added to the knowledge sources on
  10 March without a test or approval).
- Risk register: late November 2026; date fix live from 16 November 2026 with 312 re-dated orders and a
  41% drop in WISMO; 1,212 proxy visits from 11 machines; 212 PeopleWise-scored candidates; the dry-run
  results; training booked 7–11 February 2027; the Deskly AI history set to "indefinite".
- ROI: claims and basis use pilot-economics `harbor` (3,200 non-WISMO emails a month, 60% drafted, 80%
  right, 8 / 2 / 5 minutes, ₪130 an hour, build ₪120,000, about ₪49,000 a year to run); LinguaFlow
  contract ₪42,000 (₪12,000 kept for marketing); two temps × 3 months × ₪16,000; 15% cut in goodwill
  credits; the vendor's satisfaction-to-revenue ratio; gross margin 42% (from the finance summary).
- Grader: the 41 orders on the delayed container, the Deskly terms, the meeting reactions.

## Things the main session should decide

1. **Volume mismatch with the data room.** The data room's KPI report and tickets.csv have about 450
   email/web tickets a month (1,360 a quarter); batch 1's pilot-economics assumes 3,200 non-WISMO emails
   a month, and roi-defender and steering-committee follow pilot-economics so lesson 03.7 is consistent.
   If the data room's volume is right, the pilot is worth far less; then update pilot-economics,
   oversight-under-load and roi-defender's claim 1 together (roi's other claims and the cash case do not
   depend on volume).
2. **Board threshold wording.** The CFO's finance summary says the board approves anything above
   ₪150,000 *total over three years*. pilot-economics' note says "build cost ₪120,000 stays under the
   ₪150,000 line", which contradicts it (three-year cost ₪267,000). roi-defender teaches the
   three-year rule; the pilot-economics note should be corrected (I did not change batch-1 behaviour).
3. **Exchange rate.** The finance summary's planning rate is ₪3.70 per US$; pilot-economics uses 3.6.
4. New fictional details: Olga's Arabic-speaking colleague (unnamed), LinguaFlow as a paid translation
   contract (the data room has a LinguaFlow DPA), outside privacy counsel (unnamed).

## Not done

- No `generic` presets: all five are whole-scenario presets, like discovery and portfolio in batch 1;
  a generic organization would add little. Engagement presets follow the README recipe.
- No sandboxed-iframe run in a real browser (see batch 1).
- Batch 3 (agent-authority, vendor-rfp, operating-model-scaler).
