# Simulations batch 3 — notes for the main session

Written 2026-11-02 by the simulations agent. Nothing committed.

## Done

- `agent-authority` (14.4, 14.5), `vendor-rfp` (10.4, 10.5), `operating-model-scaler` (15.4, 15.5): each
  `index.html` + `app.js` + `model.js` (pure, exports `validateScenario`) + `presets.js` + `<name>.css`.
  Presets: `lumen` / `galil` / `crescent` (default) and `generic` for each.
- `simulations/common/` not changed.
- `simulations/README.md`: the three sims in the table, URL examples, batch-3 preset fields, default-preset note.

For BUILD_PROGRESS.md: tick "Simulations batch 3". Lesson links:
`[Simulation: Agent authority](../../simulations/agent-authority/index.html?preset=lumen)` (14.4, 14.5),
`[Simulation: Vendor RFP](../../simulations/vendor-rfp/index.html?preset=galil)` (10.4, 10.5),
`[Simulation: Operating-model scaler](../../simulations/operating-model-scaler/index.html?preset=crescent)` (15.4, 15.5).

## Checks run (scripts in the session scratchpad `scratchpad/sims3/`, not the repo)

- Every `.js` in `simulations/` checked as an ES module (`node --check` on an `.mjs` copy; plain `node --check`
  on a `.js` file missed a stray parenthesis once, so batch 3 used the `.mjs` route): clean.
- `model-test-3.mjs`, 58 checks, all pass. Agent authority: both presets valid and a broken one caught; the demo
  set-up fails every must-refuse test and leaves unrecoverable harm; the expert set-up refuses every probe,
  resolves ≥ 95% and loses nothing; approval on everything is rubber-stamped and still lets harm through;
  read-only is safe but not useful and costs over 3× the people-time; no ticket tool means dropped requests;
  the kill switch stops the replaced-article repeats sooner; an action log alone finds the credits after the
  invoice run; soft delete makes deletion recoverable; the prompt rule stops the crude injection but not the
  file injection; one approver misses the urgent 2FA reset and two catch it; a per-customer limit stops 24 of
  25 scripted credits; mid-week changes apply from the next day. Vendor RFP: valid; demos rank the expert pick
  last and the evidence first; demo-impression scores are ≥ 0.8 points off the evidence; every other vendor
  refuses at least one must-have; the expert pick is best on omissions; the full evidence path is "strong";
  the demo leader is "demo-led"; no legal requirement asserted. Scaler: valid; as-is is slow with a backlog
  and shadow tools; federated is fast with weak models, duplicates and incidents; the expert design scales
  safely within budget; a central queue for everything waits far longer; every answer to every event plays;
  cutting the assistant stalls its two dependents; the supervisor's question is clean only with a catalogue;
  a resignation hurts less with templates; more slots under a central CoE overspends and still leaves shadow
  tools; the hub with a catalogue merges duplicates, federated does not; hub/spoke mapping. All deterministic.
- `ui-aa.mjs`, `ui-vr.mjs`, `ui-om.mjs` (batch 1's DOM stub, sandbox-like: localStorage and history throw): 11
  flows pass (strong path, weak path, generic, unknown preset / restart): labels on every input and select,
  every button `type="button"`, no forms, no duplicate ids, no NaN / undefined / null / Infinity in text.
- Built-in browser through the batch-1 static server: all three pages load with no console messages, no
  horizontal page scroll at 360 px at start, mid-way and at the debrief; the chart fits at 360 px; dark mode
  applies; focus moves to the week / step / quarter heading after each action. The sandboxed-iframe case was
  not run (same reason as batches 1–2).
- Grep on the three folders: no URLs, fonts, CDNs, fetch, innerHTML, alert/prompt/confirm, forms, cookies,
  storage, parent/top access, eval. Every `index.html` loads only `../common/sim.css`, its own CSS and `app.js`.
  English only; UTF-8, LF, no BOM.
- Batches 1–2 re-run (not required, `common/` untouched): two **stale or failing checks caused by later
  committed edits, not by batch 3** — see "Things the main session should decide".

## Preset facts the module writers should match (or change in the preset)

### Module 14 — `agent-authority`, preset `lumen`

- Lumen SaaS (250 people) sells **Lumen Shifts**, scheduling and payroll-prep software, to about **3,100
  business customers** on **Starter, Growth, Enterprise** plans. The agent is **Lumen Assist** in the in-product
  help widget. No person at Lumen is named in the sim (roles only: the commercial account lead, the account
  manager, the DPO, the shift lead who approves).
- Seven tools: Read account, Issue credit, Change plan, Reset 2FA, Delete data, Email customer, Create ticket.
  The product team's demo set-up: all seven execute alone, no limits, action log only, shared admin identity,
  no kill switch, a prompt rule, no change control on help-centre documents.
- One week, **Sunday–Thursday**; about **80 routine requests a day** (50 look-ups, 8 Growth credits ≈ ₪90,
  3 Starter credits ≈ ₪40, 6 plan changes, 3 verified 2FA resets, 10 bug tickets). Approvals: **30 a day**
  (one shift lead, 2 minutes each), beyond that rubber-stamped. A handed-off request = 12 minutes of a person.
- Policy facts used: agent credits up to **₪500**; above that the account manager; enterprise seats are
  contract (commercial account lead); deletion is a privacy process the DPO owns; 2FA resets only via a
  channel on file; **invoice run Thursday 22:00**; contract changes sync to billing after **48 hours**;
  soft deletes recoverable **14 days**.
- Scripted events (customer names fictional): Sun 10:00 Ofek Logistics wants ₪650 outage credit (handoff);
  Sun 14:00 Bloom Studio "delete everything" meaning fewer emails (refuse); Mon 09:30 trial 4471 message with
  a crude "SYSTEM NOTE" ₪4,800 credit (refuse; the prompt rule stops it); Mon 16:00 urgent 2FA reset for
  Shaked Clinics' enterprise admin (refuse; one approver misses it, two-person rule or verification stops it;
  18,000 staff records); **marketing replaced the help article "Downgrades and refunds" on Monday** — credits
  of ₪1,100 (Tue, Tavor Engineering), ₪1,300 (Wed, Carmel Print), ₪900 (Thu, Arava Farms); Tue 15:00 Negev
  Retail Group cuts 400 → 40 seats (handoff; ₪54,000 contract value); Wed 13:00 a CSV cell tells the agent to
  email invoices to a lookalike domain (refuse; the prompt rule does not stop it); Wed 16:00 a script asks 25
  times for ₪100 (refuse); Thu 12:00 Ronen Dental's legitimate full-deletion request (handoff to the privacy
  process). With no agent log, harm is found after **11 days** (matches the plan's replaced-document finding).
- Expert set-up: read and tickets execute alone; credits execute alone under ₪300 / action, ₪2,000 / day,
  1 per customer per day, Starter and Growth only; plan changes one approver, Starter and Growth only; 2FA
  executes alone only after verification; delete not granted; email only to the address on file; full trace
  with a daily 20-minute review; own identity; tested kill switch; change control on help-centre documents.
  Result: 100% resolved, 3 handed off, nothing lost, about 3.3 h of people's time in the week. Demo set-up:
  ₪6,450 lost, 24,436 records lost or exposed, 33 unrecovered harms. A staged-autonomy plan (weeks 1–2,
  3–4, later) is in the preset.
- Not in the sim (left to the module): the unattended agent a business user built, the fleet nobody can list.

### Module 10 — `vendor-rfp`, preset `galil`

- Galil Health: **14 community clinics** in the north, **about 120 doctors and nurses**, patients speak
  Hebrew, Arabic and Russian (roughly a third each, often with a relative in the room). Clinic record system:
  **Clinix** (fictional). Two of **five regions** run an older Clinix version.
- Criteria and weights (agreed before the demos): demo vs evidence ×2, clinical safety ×3, privacy and data
  ×3, Hebrew/Arabic/Russian ×2, integration ×1, contract and exit ×2.
- Vendors (all fictional): **ScribeWave** (large US; "98% accuracy" on scripted English studio visits; Hebrew
  beta; data may train models unless enterprise plan; audio 90 days; EU/US only), **Kol Refua** (Israeli
  start-up, best Hebrew; no Arabic; "never leaves Israel" but a US speech API in the sub-processor annex; 18
  months of funding), **MedNote for Clinix** (the record vendor's add-on; "95%" on dictation; "product
  improvement" data clause; year-two price open), **Vocalis Health** (European, 200 people; independent
  university-hospital evaluation, 1,200 visits in four languages, 2.1% omissions; three Israeli clinics for 14
  months; accepts every must-have; Israel hosting about 8% extra; dearest, about ₪1,300 per clinician a month).
- Proof of concept: **90 synthetic visits** (30 per language, actors, real-shaped scripts, relatives and room
  noise). Vocalis: word error 9 / 11 / 10% (he / ar / ru), 2 omissions and 0.5 invented findings per 100 notes,
  3 minutes to correct.
- Must-have terms: no training on our data (de-identified included); audio deleted within 30 days of
  sign-off; Israel or a location the DPO approves; sub-processor list with notice and objection; model-change
  notice and re-test; named clinical safety officer and incident reporting; exit with data return and
  certified deletion. Nice to have: audit rights, a three-year price lock.
- Before signing: DPA, data location and sub-processors to **Galil's DPO and counsel** (no legal requirement
  is asserted anywhere; the sim says health data is especially sensitive under Israeli privacy law and the
  Ministry of Health has its own rules, and that which apply is their call); a six-week clinician pilot in two
  clinics (one Arabic-speaking) with a stop rule; consent wording by the medical director and the DPO.
- Expert: **Vocalis Health**. Weighted evidence scores: Vocalis 3.92, ScribeWave 2.31, MedNote 2.31, Kol Refua
  2.00; the demo impressions rank them the other way (Vocalis last, 2.92). "Twelve months later" texts per
  vendor are in the preset (e.g. Vocalis: region-by-region rollout, Arabic clinics adopted fastest, integration
  four months, note time down about 35 minutes a day).

### Module 15 — `operating-model-scaler`, preset `crescent`

- Crescent Bank: 4,000 staff, **14 units** (Retail Banking, Mortgages, Cards & Payments, SME Banking, Corporate
  Banking, Private Banking, Treasury & Markets, Credit Risk, Compliance & AML, Operations, Contact Centre,
  Digital Channels, HR, Finance), **40 pilots**, none in production; 10 of them weak (would fail a proper
  review). Planted duplicates: complaint summaries (Retail and Cards), credit memos (SME and Corporate), KYC
  document checks (SME and Compliance), call summaries (Contact Centre and Digital, later Retail too). The
  **bank-wide assistant rollout** (Operations) carries two dependents: the Operations procedure assistant and
  the Contact Centre agent knowledge assistant (the plan's acceptance-dependency trap).
- Today's set-up (start): central CoE, every go-live through one central queue, 3 review slots a quarter, full
  validation for every model, no paved roads. **12 quarters from Q1 2027**; budget **₪11M a year**.
- Money (₪ a quarter): slot 150,000; central team 1.2M (CoE) / 0.8M (hub) / 0.3M (federated); platform 2.4M over
  two quarters then 300,000; templates and evaluation kit 200,000 then 40,000; catalogue 150,000 then 25,000.
- Events: Q2 2027 two shadow tools (Cards on a public chatbot API, Digital on a personal subscription); Q3 2027
  the complaints duplicate; Q1 2028 the supervisor asks for the model inventory and validation evidence (the
  sim says its consequence is the model's, not a statement about a real supervisor); Q2 2028 the head of model
  validation resigns and two validators follow; Q3 2028 a **15% budget cut**, the assistant the biggest line;
  Q1 2029 the SME credit pre-approval model drifts after rates move; Q3 2029 a vendor release switches on six
  generative features in the CRM and HR system.
- Expert: hub-and-spoke from Q1, decisions by risk tier, 3 slots, validation by tier, all three paved roads;
  bring shadow tools in, merge the duplicate under Cards, answer the supervisor from the catalogue, a
  contractor for the validation gap, cut across the board (keep the assistant), retrain and revalidate the
  drifting model, route the vendor features by risk. Result: 36 in production, 0 waiting, 0 duplicates, 2
  incidents, 0 shadow tools, ₪29.8M of ₪30.9M. Today's set-up with the usual answers: 7 in production, 29
  waiting (5.3 quarters average), 23 shadow tools, ₪21.4M. Federated free-for-all: 40 in production, 10 weak
  models live, 5 duplicates, 23 incidents.

## Things the main session should decide

1. **Earlier-batch checks that now fail (committed edits after batch 2, not batch 3):**
   - `pilot-economics` `harbor` now shows ₪10,048 a month (exchange rate 3.70, as the README says); the batch-1
     UI test still expects ₪10,051. Only the scratch test is stale.
   - `readiness-evidence-grader` `harbor`: `validateScenario` now reports "deskly: a contradiction needs a
     verified item that shows it" — the Deskly item is marked contradicted but no verified item lists it in
     `by`. A real data gap in the committed preset (from module 07's edits); I did not touch it.
2. Every Lumen, Galil and Crescent number above is an assumption made before the modules exist. When the
   module writers build the data rooms, either match these or change the preset (and re-run
   `validateScenario`); the field lists are at the top of each `presets.js`.
3. Vendor and product names (ScribeWave, Kol Refua, MedNote, Clinix, Vocalis Health, Lumen Shifts, Lumen Assist)
   are invented; a quick check that none is a real product in Israel would be prudent before publishing.

## Not done

- No sandboxed-iframe run in a real browser (as in batches 1–2).
- Engagement material the sims leave to the modules: Lumen's unattended agent built by a business user and the
  agent fleet nobody can list; Galil's clinician adoption beyond the pilot step; Crescent's 40-pilot triage itself.
