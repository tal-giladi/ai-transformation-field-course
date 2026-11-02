# Simulations batch 1 — notes for the main session

Written 2026-11-02 by the simulations agent (agent 2). Nothing committed.

## Done

- `simulations/common/` (shell, controls, chart, format, random, math, storage, dom, sim.css).
- `discovery-interview`, `portfolio-sorter`, `pilot-economics`, `oversight-under-load`,
  `adoption-dynamics`: each `index.html` + `app.js` + `model.js` (pure) + `presets.js` + `<name>.css`.
- `simulations/README.md` for writers (presets, parameters, URLs, lesson ids, how to add a preset).

For BUILD_PROGRESS.md: tick "Simulations batch 1". Lesson links: 02.2 discovery-interview,
03.4 portfolio-sorter, 05.4 + 03.7 pilot-economics, 05.5 oversight-under-load, 06.4 adoption-dynamics,
all with `?preset=harbor`.

## Checks run

- `node --check` on every `.js`: clean.
- Model test (21 checks, all pass): kept outside the repo in the session scratchpad
  (`scratchpad/sims/model-test.mjs`); it imports each `model.js` and `presets.js` by file URL. It checks:
  harbor pilot numbers (₪10,051/month, 108.8 h, breakeven 11.9 months; breakeven accuracy and max
  review minutes really give zero), "review eats the saving" at 6 min; oversight target missed by
  default, met with source + feedback, not met by more reviewers alone, catch rate never rises with
  volume; adoption deterministic per seed, licences constant, counts ordered, mandate gives ~90% WAU
  but ~18% qualified use, the good plan ~70% (20 seeds); discovery scenario integrity (every fact
  reachable, every required flag set somewhere, one correct diagnosis) and a 12-question path that
  finds all key facts; portfolio expert ranking puts the expert picks on top and within capacity.
- UI test under a hand-written DOM stub (scratchpad `ui-test.mjs`): every app loads, all controls
  labelled, all buttons `type="button"`, no NaN/undefined in text, each flow clicked through to the
  debrief, preset switch and unknown preset handled.
- Real browser (built-in pane, local static server in the scratchpad): all five pages load with no
  console errors, no horizontal scroll at 360 px after interaction, dark mode colours apply, the
  portfolio and discovery flows run end to end. The pane blocks sub-resources of sandboxed documents
  (ERR_BLOCKED_BY_CLIENT), so the `sandbox allow-scripts` case itself was not run in a browser; the
  code wraps every sandbox-sensitive call (localStorage, history.replaceState) in try/catch, uses no
  forms/popups/cookies/parent access, and relies on the Academy's `Access-Control-Allow-Origin: *`
  for module scripts. Worth one check after the first import.
- Grep: no http(s) URLs, fonts, CDNs, fetch, innerHTML, alert/prompt, forms. The only `http://` is the
  SVG namespace string in `common/dom.js` (not a request). Every `index.html` loads only
  `../common/sim.css`, its own CSS and `app.js`. All files UTF-8, LF, no BOM.

## Decisions and assumptions (check when modules 2, 3, 5, 6 are written)

- Harbor numbers not in the writer's notes are assumptions, marked in the presets' `notes`:
  3,200 non-WISMO emails a month, 60% handled, 80% accuracy, 8 min saved, 2 min review, 5 min rework,
  ₪130/h (from ₪3.4M ÷ 14), build ₪120k, fixed ₪4k/month; 90 drafts a day for oversight; 6,000
  contacts a month in the portfolio cards. If the data room (Foundation C) lands on different
  volumes, update `pilot-economics/presets.js`, `oversight-under-load/presets.js` and the portfolio
  cards' `volume`/`benefitBasis` so the lessons, the data room and the sims agree.
- Token prices ($3/$15 per million) and the exchange rate (3.6) are labelled examples; lesson 05.4
  should tell learners to put in current prices.
- New fictional names not in the persona table: Hadar Klein (B2B sales lead), Rina (claims clerk,
  already in the notes), adoption team first names. Add Hadar to the persona pack if a lesson uses her.
- `discovery-interview` uses Michal, Samir, Olga, Tamar and Yoav (02.2 lists Samir, Olga, Tamar;
  Michal and Yoav add the sponsor and the stated-ask trap).
- Expert portfolio for 03.4: date fix + proactive delay emails (no AI), support-email drafts from
  February, B2B quote drafts with prices from the ERP. The 03.4 lesson's answer should match.
- The adoption model's "qualified-use rate" denominator is the people who do the target work
  (12 of 14 in harbor), so it can exceed the weekly-active share; the chart shows counts, which are
  always ordered licences ≥ active ≥ qualified.

## Not done

- Batches 2 and 3 (steering-committee, incident-tabletop, risk-register-tester, roi-defender,
  readiness-evidence-grader; agent-authority, vendor-rfp, operating-model-scaler).
- Engagement presets (`?preset=insurance` etc.) for modules 8–17: add when those modules are planned.
- No sandboxed-iframe run in a real browser (see above).
