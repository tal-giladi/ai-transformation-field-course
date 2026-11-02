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

`?preset=` picks the scenario. An unknown or missing preset falls back to the default (`harbor`; for batch 3, the engagement preset)
and says so on the page. The learner can also switch scenarios with the picker.

## The simulations

| Simulation | What the learner practises | Presets | Link from |
|---|---|---|---|
| `discovery-interview` | 12 questions across five Harbor & Pine stakeholders; making it safe to talk, workflow and same-word questions vs leading ones; names the real problem (WISMO caused by a promised date that is never updated) and gets a debrief on facts found/missed, question quality and trust lost | `harbor` | 02.2 |
| `portfolio-sorter` | Locks criteria and weights before seeing nine cards; scores value/feasibility/risk on evidence; nets the expected cost of errors; must ask each receiving team what it can absorb; hidden truths and the expert portfolio after commit | `harbor` | 03.4 |
| `pilot-economics` | Volume × automation × accuracy × review and rework minutes × tokens → monthly net value, net hours (capacity, not cash), breakeven; charts of net value vs accuracy and vs review minutes; shows when review eats the saving | `harbor`, `generic` | 05.4 and 03.7 |
| `oversight-under-load` | A review queue over two working weeks (Sun–Thu); load, rubber-stamping, vigilance; toggles "source shown beside the draft" and "flag feedback on"; the capacity screen; must meet a target for errors reaching customers within a reviewer-hours limit | `harbor`, `generic` | 05.5 |
| `adoption-dynamics` | A 26-week rollout plan (training generic vs role-based, champions, office hours, workflow redesign, mandate, removing the old path); licences vs weekly active users vs qualified-use rate; a hidden "who stopped" view of quiet non-adoption; Goodhart under a mandate | `harbor`, `generic` | 06.4 |
| `readiness-evidence-grader` | Sorts 18 dated evidence items (interview notes, a KPI report, the handbook, export profiles, vendor statements, emails) into verified / reported / contradicted; picks proceed / phase / not yet; sees the steering group react to the same verdict with an honest and an over-claimed report | `harbor` | 02.6 |
| `roi-defender` | Seven sponsor claims (₪1.36M a year, "the 40%") under the CFO's review: nets each across four ledgers (sponsor's team, receiving team, control capacity, customer's share), labels measured / directional / assumed, separates capacity from cash, applies the 12% hurdle and the ₪150k three-year board line; defensible vs claimed number and which claims survived | `harbor` | 03.7 |
| `risk-register-tester` | Twelve owner-rated risks and a 15-point testing budget (ask the owner 1, sample the evidence 2, run a test 3); unearned greens, overstated reds; re-rates and sees the register's credibility before and after: earn the green | `harbor` | 04.5 |
| `steering-committee` | A branching steering meeting with the CEO, CFO, sponsor, IT and the support manager; answer first, evidence vs inference, concede, overclaim, defer, ask for the decision; the sponsor-as-advocate branch; approved / with conditions / sent back / killed and "six months later" | `harbor` | 07.4 |
| `incident-tabletop` | The draft pilot promises refunds outside policy and discloses another customer's address; six points over four days; contain, communicate, fix, report (privacy goes to the DPO or counsel, no legal deadline asserted); scored on harm, time to contain, trust and documentation; compared with a runbook | `harbor` | 07.5 |
| `agent-authority` | Grants a customer-support agent its tools (read account, issue credit, change plan, reset 2FA, delete data, email customer, create ticket), a rung each (not granted / one approver / two approvers / executes alone), limits (caps, daily totals, per-customer rate, tiers, verification, address on file, soft delete), logging, its own identity, a kill switch; runs the must-refuse tests and a scripted week (edge cases, injections, a confused customer, social engineering, a replaced help article); tasks resolved, damage, last reversible moment, audit trail; the authority ladder and staged autonomy | `lumen`, `generic` | 14.4 and 14.5 |
| `vendor-rfp` | Scores four ambient-scribe vendors on six criteria after the demos, again after the “demo conditions” reveal, again after a proof of concept on the clinics’ own synthetic recordings; picks a vendor, contract terms (training use, retention, location, sub-processors, model changes, safety, exit) and the steps before signing (DPO and counsel, clinician pilot, consent); compared with the evidence and the expert | `galil`, `generic` | 10.4 and 10.5 |
| `operating-model-scaler` | Chooses central CoE / federated / hub-and-spoke, decision rights, central review slots a quarter, model-risk validation depth and paved roads (platform, templates and evaluation kit, catalogue); plays 12 quarters with shadow builds, duplicates, a supervisor’s question, a resignation, a budget cut, model drift and a vendor release; pilots in production, time to decision, backlog, duplicates, incidents, shadow tools, cost; hub constants vs spoke variables | `crescent`, `generic` | 15.4 and 15.5 |

URL examples (from a lesson two folders deep):

- `../../simulations/discovery-interview/index.html?preset=harbor`
- `../../simulations/portfolio-sorter/index.html?preset=harbor`
- `../../simulations/pilot-economics/index.html?preset=harbor` (05.4) and `?preset=generic`
- `../../simulations/oversight-under-load/index.html?preset=harbor`
- `../../simulations/adoption-dynamics/index.html?preset=harbor`
- `../../simulations/readiness-evidence-grader/index.html?preset=harbor` (02.6)
- `../../simulations/roi-defender/index.html?preset=harbor` (03.7, after pilot-economics)
- `../../simulations/risk-register-tester/index.html?preset=harbor` (04.5)
- `../../simulations/steering-committee/index.html?preset=harbor` (07.4)
- `../../simulations/incident-tabletop/index.html?preset=harbor` (07.5)
- `../../simulations/agent-authority/index.html?preset=lumen` (14.4 and 14.5) and `?preset=generic`
- `../../simulations/vendor-rfp/index.html?preset=galil` (10.4 and 10.5) and `?preset=generic`
- `../../simulations/operating-model-scaler/index.html?preset=crescent` (15.4 and 15.5) and `?preset=generic`

## Presets and their parameters

All presets are in each folder's `presets.js` (pure data). Numbers for `harbor` follow
`curriculum/engagements/harbor-and-pine.md`; where the writer's notes give no number, the preset's
`notes` say it is an assumption. All people and companies are fictional.

### pilot-economics

| Parameter | Meaning | `harbor` | `generic` |
|---|---|---|---|
| `volume` | items per month in scope | 3,200 written contacts | 10,000 invoices |
| `automationRate` | share the AI handles (0–1) | 0.6 | 0.85 |
| `accuracy` | share of AI outputs right (0–1) | 0.8 | 0.92 |
| `minutesSaved` | minutes saved per right output | 8 | 4 |
| `reviewMinutes` | review minutes per handled item | 2 | 1 |
| `reworkMinutes` | extra minutes per wrong output | 5 | 6 |
| `hourlyCost` | fully loaded ₪ per hour | 130 (₪3.4M / 14 people) | 110 |
| `tokensIn`, `tokensOut` | tokens per item | 2,500 / 400 | 3,000 / 300 |
| `priceIn`, `priceOut` | US$ per million tokens (examples) | 3 / 15 | 1 / 4 |
| `fx` | ₪ per US$ (example) | 3.7 | 3.6 |
| `fixedMonthly` | ₪ a month | 4,000 | 8,000 |
| `buildCost` | one-off ₪ | 120,000 (under the ₪150k board line) | 250,000 |

Result for `harbor`: about ₪10,048 a month (exchange rate 3.70), 108.8 net hours (0.6 FTE), breakeven 11.9 months,
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

### Batch 2: scenario presets (data only)

All five batch-2 simulations are scenario presets: the engine in `model.js` knows nothing about
Harbor & Pine, and each `model.js` exports `validateScenario(preset)`, which returns a list of
problems (empty when the data is consistent). The field lists are at the top of each `presets.js`.

- `steering-committee`: `cast` (id, name, role, `concern`, starting `mood` 0–4, `weight`, `sponsor`),
  `paper` (lines of the paper the learner sent), `rounds` (speaker, prompt, optional `when`, `advocate`
  for the sponsor-as-advocate moment, `choices` with `type`, text, reply, `moods` deltas, `honesty`
  delta, `sets` flags), `outcomes` (kind `approved | conditions | sentBack | killed`, `when`, text,
  `later` variants), `lessonPoint`. Conditions are plain data (`flag`, `notFlag`, `support`, `mood`,
  `honesty`, `all`, `any`, `not`), described at the top of `model.js`. `harbor`: CEO and CFO weight 2,
  sponsor 1.5, others 1; approved needs support of at least 2.2 and an explicit ask.
- `incident-tabletop`: `start` (running, customers already harmed, trust), `fixedFlag`, `injects` (t in
  hours, clock text, info, `extra` lines by flag, `exposure` = customers harmed until the next inject
  while the feature is fully on and the cause is not fixed, `decisions` with options tagged by runbook
  `step` and `quality` best / ok / poor and `effects`), `runbook`, `flagNotes`, `scoring` (6 points per
  customer harmed; containment bands from 30 minutes to a day). Never write an option that states a
  legal deadline as the right answer: reporting questions go to the DPO or counsel.
- `risk-register-tester`: `budget` (15), `costs` (ask 1, sample 2, test 3), `risks` (owner, owner's
  rating, control as described, `evidence` per method with `strength` none / weak / strong, `truth`
  rating, control kind and why). A green counts as earned only with strong evidence. Make sure testing
  everything costs more than the budget.
- `roi-defender`: `hourlyCost`, `hurdleRate`, `costs` (build, running per year, years), `approval`
  levels (max total over the years), `claims` (claimed ₪ a year, basis, the deck's label and class,
  `adjustments` on the four ledgers with `real` true/false, optional `target` claim, and why; `truth`
  label and class). `harbor`: claimed ₪1,360,000; defensible ₪113,000 cash plus about 567 hours of
  capacity a year; NPV at 12% over three years about ₪33,700; payback 22.5 months; three-year cost
  ₪267,000, so the board approves. Claim 1's hours match `pilot-economics` `harbor`.
- `readiness-evidence-grader`: `items` (kind, source, date, area, text, `truth`, `by` = the verified items
  that confirm or contradict it, why, `challenge` for every item that is not verified),
  `overclaimThreshold` (2), `verdicts` (one `best`, reactions and tones for an honest and an
  over-claimed report, `changeIt`).

### Batch 3: engagement simulations (scenario presets)

Built before modules 10, 14 and 15 were written: each has a preset for its engagement and a `generic` one.
The facts each engagement preset assumes (names, numbers, dates, the expert answer) are listed in
`curriculum/inbox/simulations-batch-3-notes.md` so the module writers can match them or change the preset.
Each `model.js` exports `validateScenario(preset)`; the field lists are at the top of each `presets.js`.

- `agent-authority`: `currency`, `tiers`, `tools` (id, label, consequence, recoverability `band` easy / bounded /
  difficult / none, `needs`, `limits` of kinds `cap`, `dailyTotal`, `perCustomerDay`, `tiers`, `verify`,
  `ownAddressOnly`, `softDelete`, and `expertWhy`), `days`, `approvalCapacity` (approvals a day before they are
  rubber-stamped), `costs` (minutes), `detection` (daily review hour, weekly report, no-log delay),
  `killSwitchHours` / `noKillSwitchHours`, `softDeleteHours`, `routine` (requests a day per tool), `events`
  (day, hour, customer, what they say, the action the agent tries, `right` = do / handoff / refuse, why, and
  the `harm` with its window and last reversible moment; `catchAt` says whether one approver or only a second
  catches it; `cause` links repeats such as the replaced article), `probes` (the must-refuse tests),
  `startConfig` (what the product team demoed: everything on, no limits) and `expert` (config and a
  staged-autonomy plan). `lumen`: about 80 requests a day for one week (Sunday–Thursday), 30 approvals a
  day, invoice run Thursday 22:00, the replaced help article from Monday, found after 11 days with no log.
  The validator checks that the expert set-up refuses every probe and loses nothing.
- `vendor-rfp`: `criteria` (with weights), `vendors` (demo, `claims` with the measurement `conditions` and
  whether they hold here, `docs`, `demoImpression` and `truth` scores 1–5 per criterion, `poc` results,
  `terms` answers accepts / refuses with a note, price, `later`), `pocMetrics`, `terms` (must-have or not),
  `beforeSigning` (right or wrong), `expert`. The validator checks that the evidence ranks the expert's pick
  first and the demos do not, and that the pick accepts every must-have. `galil`: ScribeWave, Kol Refua,
  MedNote for Notara, Rishma Health (expert pick). Never state a legal requirement: privacy questions go to
  the DPO and counsel.
- `operating-model-scaler`: `units` (maturity 1–3, `appetite` for building outside the process, `pilots` with
  theme, risk tier, `weak`, `dependsOn`), `arrivals`, `money`, `build`, `review`, `shadow`, `risk`,
  `regulator`, `keyPerson`, `driftTheme`, `events` (quarter, options with `effects` from a fixed list
  described at the top of `presets.js`), `startConfig` (the organization as it works today),
  `federatedConfig`, `naiveAnswers`, `expert` (config and answers), `hubSpoke`. The validator checks that the
  expert design beats today's on production and federated on incidents and duplicates. `crescent`:
  14 units, 40 pilots (10 weak), 12 quarters from Q1 2027, budget ₪11M a year (a 15% cut announced in Q3 2028).

## How to add a preset

1. Open the simulation's `presets.js`, copy an existing entry and give it a new key (lowercase,
   e.g. `insurance`). The key is what goes after `?preset=`.
2. Write a `label` (shown in the picker) and a `brief` (the "Your situation" paragraph: who the
   learner is, what is being decided, what "done" looks like). Use fictional names only.
3. Change the numbers or the scenario content. Keep every number realistic for that organization and
   say in `notes` which ones are assumptions.
4. For a scenario preset (discovery, portfolio and all of batches 2 and 3): every fact must be reachable by some question, every
   flag a question `requires` must be set by another question, exactly one diagnosis is correct, and
   the expert's picks must fit the teams' capacities. The batch-1 model test (see the notes file) checks this for `harbor`.
   For batch-2 and batch-3 simulations run `validateScenario` from the simulation's `model.js` on the new preset;
   for `steering-committee` also play every path once (the batch-2 test enumerates all of them) and
   check that each outcome you wrote can be reached.
5. Check: `node --check simulations/<name>/presets.js`, then load the model in node and run the new
   preset (see `curriculum/inbox/simulations-batch-1-notes.md` and `simulations-batch-2-notes.md` for the tests used), then
   open the page through a local static server (ES modules do not load from `file://`).

## How an engagement module adds a preset

An engagement module (8–17) re-uses a simulation with its own organization by adding one entry to that
simulation's `presets.js`; no code changes.

1. Pick a key named after the engagement (`insurance`, `hospital`…) and copy the `harbor` entry.
2. Replace the cast, the issues and the numbers with the engagement's own, from `labs/module-NN/brief.md`
   and its data room. For `steering-committee`, write the members' concerns first, then one round per
   concern, then the sponsor-as-advocate round, then the decision round; write the outcomes last.
3. Keep the lesson's point and rewrite `lessonPoint` only if the engagement adds something.
4. Put every number that is not in the engagement's data room in `notes` as an assumption.
5. Run `validateScenario` (and the path enumeration for `steering-committee`) and open the page with
   `?preset=<key>`. Link it from the engagement lesson as
   `[Simulation: Steering committee](../../simulations/steering-committee/index.html?preset=<key>)`.

## Code layout

- `common/` — `shell.js` (page shell, preset picker, About panel, live region), `controls.js`
  (labelled slider + number box, toggle, select, button, stat tile), `chart.js` (inline-SVG line
  and bar charts with a table alternative), `format.js` (₪, %, hours, minutes, months), `random.js`
  (seeded random), `math.js`, `storage.js` (optional localStorage, always in try/catch), `dom.js`,
  `table.js` (a table that becomes labelled blocks below 640 px, class `stack`),
  `sim.css` (light and dark, responsive from 360 px, visible focus).
- `<name>/index.html` loads `../common/sim.css`, `<name>.css` and `app.js` only.
- `<name>/model.js` is the pure model (no DOM), testable in node. `<name>/app.js` is the UI.
- No `<form>` elements (the Academy's CSP forbids form actions), no `alert`/`prompt`, no popups,
  no `innerHTML`, no network requests.
