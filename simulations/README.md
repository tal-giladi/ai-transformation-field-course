# Simulations (for writers, not learners)

Interactive educational models for "AI Transformation in the Field". Plain HTML, CSS and vanilla ES
modules; no build step, no network, no fonts, no CDN. Each simulation lives in its own folder and
uses only that folder plus `common/`. They run in the Academy as sandboxed iframes
(`sandbox allow-scripts`) and are public even though the course is paid: put nothing in them that
must stay behind the paywall.

Every simulation has the same shape: a header with the "Educational model — simplified on purpose"
label, a scenario picker, a one-paragraph "Your situation" brief, an "About this model" panel that
states the equations and assumptions in plain words, the interactive part, and a debrief that names
the lesson's point. Each one teaches one decision in 5–15 minutes. The lesson must still work without it.

## How to link one from a lesson

Put the link on its own line; the text must start with `Simulation:`. From a lesson file two
folders below the course root:

```markdown
[Simulation: Pilot economics](../../simulations/pilot-economics/index.html?preset=harbor)
```

`?preset=` picks the scenario. An unknown or missing preset falls back to the default (`harbor`)
and says so on the page. The learner can also switch scenarios with the picker.

## The simulations

| Simulation | What the learner practises | Presets | Link from |
|---|---|---|---|
| `discovery-interview` | 12 questions across five Harbor & Pine stakeholders; making it safe to talk, workflow and same-word questions vs leading ones; names the real problem (WISMO caused by a promised date that is never updated) and gets a debrief on facts found/missed, question quality and trust lost | `harbor` | 02.2 |
| `portfolio-sorter` | Locks criteria and weights before seeing nine cards; scores value/feasibility/risk on evidence; nets the expected cost of errors; must ask each receiving team what it can absorb; hidden truths and the expert portfolio after commit | `harbor` | 03.4 |
| `pilot-economics` | Volume × automation × accuracy × review and rework minutes × tokens → monthly net value, net hours (capacity, not cash), breakeven; charts of net value vs accuracy and vs review minutes; shows when review eats the saving | `harbor`, `generic` | 05.4 and 03.7 |
| `oversight-under-load` | A review queue over two working weeks (Sun–Thu); load, rubber-stamping, vigilance; toggles "source shown beside the draft" and "flag feedback on"; the capacity screen; must meet a target for errors reaching customers within a reviewer-hours limit | `harbor`, `generic` | 05.5 |
| `adoption-dynamics` | A 26-week rollout plan (training generic vs role-based, champions, office hours, workflow redesign, mandate, removing the old path); licences vs weekly active users vs qualified-use rate; a hidden "who stopped" view of quiet non-adoption; Goodhart under a mandate | `harbor`, `generic` | 06.4 |

URL examples (from a lesson two folders deep):

- `../../simulations/discovery-interview/index.html?preset=harbor`
- `../../simulations/portfolio-sorter/index.html?preset=harbor`
- `../../simulations/pilot-economics/index.html?preset=harbor` (05.4) and `?preset=generic`
- `../../simulations/oversight-under-load/index.html?preset=harbor`
- `../../simulations/adoption-dynamics/index.html?preset=harbor`

## Presets and their parameters

All presets are in each folder's `presets.js` (pure data). Numbers for `harbor` follow
`curriculum/engagements/harbor-and-pine.md`; where the writer's notes give no number, the preset's
`notes` say it is an assumption. All people and companies are fictional.

### pilot-economics

| Parameter | Meaning | `harbor` | `generic` |
|---|---|---|---|
| `volume` | items per month in scope | 3,200 non-WISMO emails | 10,000 invoices |
| `automationRate` | share the AI handles (0–1) | 0.6 | 0.85 |
| `accuracy` | share of AI outputs right (0–1) | 0.8 | 0.92 |
| `minutesSaved` | minutes saved per right output | 8 | 4 |
| `reviewMinutes` | review minutes per handled item | 2 | 1 |
| `reworkMinutes` | extra minutes per wrong output | 5 | 6 |
| `hourlyCost` | fully loaded ₪ per hour | 130 (₪3.4M / 14 people) | 110 |
| `tokensIn`, `tokensOut` | tokens per item | 2,500 / 400 | 3,000 / 300 |
| `priceIn`, `priceOut` | US$ per million tokens (examples) | 3 / 15 | 1 / 4 |
| `fx` | ₪ per US$ (example) | 3.6 | 3.6 |
| `fixedMonthly` | ₪ a month | 4,000 | 8,000 |
| `buildCost` | one-off ₪ | 120,000 (under the ₪150k board line) | 250,000 |

Result for `harbor`: about ₪10,051 a month, 108.8 net hours (0.6 FTE), breakeven 11.9 months,
breakeven accuracy 61.4%, at most 4.4 review minutes per draft before it loses money.

### oversight-under-load

`itemsPerDay`, `reviewers`, `hoursPerReviewer`, `errorRate`, `checkMinutes` (a real check without
the source), `sourceShown`, `flagFeedback`, `days` (10), and `target: { maxEscaped,
maxReviewerHoursPerDay }`. `harbor`: 90 drafts a day, 3 agents × 1.5 h, 20% wrong, 3-minute check;
target ≤ 10 wrong replies in two weeks with ≤ 6 agent-hours a day (met only with both toggles on).
`generic`: 400 claim summaries a day, 8 adjusters × 3 h, 8% wrong, 5-minute check; target ≤ 20 with
≤ 30 adjuster-hours a day. Model constants (check-time speed-up, catch rates, vigilance decay) are
in `K` in `model.js` and shown on the page.

### adoption-dynamics

`teamSize`, `opportunityShare` (share whose work includes the target tasks), `usesPerWeek`,
`minutesPerUse`, `seed`, `names` (fictional first names), `oldWays` (what people go back to), plus
`team` and `task` (text). `harbor`: 14 support agents, 12 answer email, pilot from 1 February 2027.
`generic`: 40 sales-operations staff, 75% prepare quotes. Model constants are in `K` in `model.js`.

### discovery-interview and portfolio-sorter

These presets are whole scenarios, not parameters. `discovery-interview`: `budget`, `cast` (id,
name, role, starting trust 0–4), `facts` (four marked `key`), `questions` (who, type, text, answer,
guarded answer, `needTrust`, `requires`/`requiresAny` flags, `sets` flags, `reveals` facts, `trust`
change), `diagnoses` (one `correct`), `lessonPoint`. `portfolio-sorter`: `teams` (capacity in hours a
month and the answer when asked), `cards` (claimed benefit, evidence, volume, error rate, cost per
error, build cost, team, hours to absorb, hidden `truth`, `expertRating`), `expert` (criteria,
picks, `mustHave`), `lessonPoint`. The field lists are at the top of each `presets.js`.

## How to add a preset

1. Open the simulation's `presets.js`, copy an existing entry and give it a new key (lowercase,
   e.g. `insurance`). The key is what goes after `?preset=`.
2. Write a `label` (shown in the picker) and a `brief` (the "Your situation" paragraph: who the
   learner is, what is being decided, what "done" looks like). Use fictional names only.
3. Change the numbers or the scenario content. Keep every number realistic for that organization and
   say in `notes` which ones are assumptions.
4. For a scenario preset (discovery, portfolio): every fact must be reachable by some question, every
   flag a question `requires` must be set by another question, exactly one diagnosis is correct, and
   the expert's picks must fit the teams' capacities. The batch-1 model test (see the notes file) checks this for `harbor`.
5. Check: `node --check simulations/<name>/presets.js`, then load the model in node and run the new
   preset (see `curriculum/inbox/simulations-batch-1-notes.md` for the test used for batch 1), then
   open the page through a local static server (ES modules do not load from `file://`).

## Code layout

- `common/` — `shell.js` (page shell, preset picker, About panel, live region), `controls.js`
  (labelled slider + number box, toggle, select, button, stat tile), `chart.js` (inline-SVG line
  and bar charts with a table alternative), `format.js` (₪, %, hours, minutes, months), `random.js`
  (seeded random), `math.js`, `storage.js` (optional localStorage, always in try/catch), `dom.js`,
  `sim.css` (light and dark, responsive from 360 px, visible focus).
- `<name>/index.html` loads `../common/sim.css`, `<name>.css` and `app.js` only.
- `<name>/model.js` is the pure model (no DOM), testable in node. `<name>/app.js` is the UI.
- No `<form>` elements (the Academy's CSP forbids form actions), no `alert`/`prompt`, no popups,
  no `innerHTML`, no network requests.
