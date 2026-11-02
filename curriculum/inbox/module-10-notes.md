# Module 10 — notes for the main session

Written 2026-11-02 by the module 10 agent. Nothing committed. `node curriculum/tools/check-module.mjs 10`
→ only the expected broken links to `templates/rfp-for-ai-vendors.md` (draft in the templates inbox).

## Things Tal must decide

1. **"Rishma Health" is a real Israeli company** (voice biomarkers; Globes, Times of Israel, Calcalist),
   and the `vendor-rfp` preset uses the name for a fictional European scribe vendor with invented facts
   (200 people, nine countries, prices, an evaluation). Portraying a real health-tech company with made-up
   facts is a publishing risk. Recommendation: rename it everywhere before publishing, after checking the
   new name (e.g. a coined word). Files: `simulations/vendor-rfp/presets.js` (owned by the simulations
   batch), and in module 10 `labs/module-10/**` (data room via `generate.py`, PoC files, personas, expert,
   scoring sheet), `lessons/module-10/*`, `assessments/module-10-quiz*`, `projects/m10-galil-health.md`,
   `curriculum/engagements/module-10.md`. A single `sed` on "Rishma Health" and "Rishma" plus
   `python labs/module-10/data-room/generate.py` does it; re-run `validateScenario` for the preset.
2. **"Notara"** is close to "Klinix", a real Israeli clinic-management system, and to "NotaraSummary", a real
   AI scribe. Lower risk, but worth a rename at the same time (it appears in the preset and in module 10).
3. Lesson 10.4 is about 4,900 words (the build spec aims at 1,500–3,000). It carries the RFP, the
   claim read-backs, the regulatory map and the PoC; splitting would break the six-lesson engagement
   shape. Left as is; trim the regulatory step if Tal wants it shorter.

## For the sidebar (lesson titles = H1s)

- **Module 10 — Galil Health** (suggested)
  - 10.1 · The call
  - 10.2 · Discovery
  - 10.3 · Diagnosis
  - 10.4 · The hard part: choosing on evidence
  - 10.5 · Decide: scoring, contract terms and the clinician pilot
  - 10.6 · Readout and debrief
  - Module quiz: `assessments/module-10-quiz.md`. Project: `projects/m10-galil-health.md`.

## Templates

- New: `curriculum/inbox/templates/rfp-for-ai-vendors.md` (complete draft in the build-spec format; its
  example is Harbor & Pine's chat-assistant RFP after the ChatNest read-back). The spreadsheet part is
  `labs/module-10/rfp-scoring-sheet.csv`, linked from the template as `../labs/module-10/rfp-scoring-sheet.csv`.
  Lessons 10.4, 10.5 and the project link `../../templates/rfp-for-ai-vendors.md` (broken until published).
  The template's own links (`../lessons/module-10/lesson-04.md`, `lesson-05.md`) resolve once it sits in `templates/`.
- Everything else re-uses published templates.

## The `vendor-rfp` preset `galil`: what matches and what I would change

Matched exactly: 14 clinics, five regions, two on older Notara; vendors, claims and their conditions, demo
descriptions, documents, demo-impression and truth scores (weighted 3.62 / 3.62 / 3.54 / 2.92 → 2.31 / 2.00 /
2.31 / 3.92), PoC word error rates and correction minutes, terms and replies, prices, the expert pick, the
"twelve months later" texts (used as the three futures in 10.6), the before-signing steps.

Changes I would make to the preset:

1. **PoC rates from 90 visits cannot be the preset's numbers.** "0.5 invented findings per 100 notes" needs
   at least 200 notes; 90 notes give multiples of 1.1. The module therefore has each vendor process each
   recording twice (180 notes; Kol Refua 120, no Arabic). Counts: omissions 13 / 6 / 20 / 4, invented
   5 / 1 / 4 / 1 → per 100: 7.2 / 5.0 / 11.1 / 2.2 and 2.8 / 0.8 / 2.2 / 0.6 (preset: 7 / 5 / 11 / 2 and
   3 / 1 / 2 / 0.5). Suggest `pocIntro` say "each recording processed twice (180 notes)" and the PoC table
   show counts, and that the debrief mention the 95% intervals (Rishma 0.9–5.6 per 100 overlaps
   ScribeWave's 4.3–12.0): a small PoC selects for a pilot, it does not prove safety.
2. **"About 120 doctors and nurses".** The ask is "every doctor"; the module has 78 doctors and 42 nurses and
   treats nurses as a separate decision. Suggest the brief say "78 doctors and 42 nurses".
3. **Before signing.** The preset's right options are DPO/counsel, the pilot and consent. The module adds two
   that are realistic and Israel-specific: the health fund's prior approval (a contract clause in the data
   room) and reporting to the Ministry of Health under its cloud circular 2/2021. Suggest adding one right
   option: "Ask the health funds whose agreements govern members' data for their approval before any data
   moves."
4. **Retention.** The module keeps the must-have (30 days) but makes retention instructable, because counsel's
   open question is whether audio is part of the medical record. Optional note in the preset's `why`.
5. **Future 1** in 10.6 adds that Fund A asked Galil to suspend use for its members, and future 3 that two
   vacancies were filled by the autumn; both are consistent with the preset's texts but go beyond them.

## Facts not verified / to check before publishing

- MOH circular 2/2021 on cloud computing: read in full from the gov.il PDF; whether a later circular replaced
  it was not established ⚠️.
- The March 2026 MOH emergency directive on generative AI is known only from Mako's report ⚠️; lessons say
  so and tell learners to check its current status.
- AMAR's own guidance on software as a medical device was not found ⚠️; lessons name AMAR, cite the Medical
  Equipment Law and use the MHRA's July 2026 guidance only as a UK comparator.
- All Israeli statutes were read on Hebrew Wikisource, not the official text ⚠️.
- Hebrew, Arabic and Russian text in `data-room/textbank.py` (survey comments, incidents, PoC sample
  scripts) was written by the agent: a native-speaker read is worth doing, especially the Galilee Arabic.
- Galil's health-fund agreements, the staff committee agreement, the Notara contract and the privacy notice
  are fictional documents; they are written to be plausible, not as statements about real health funds.

## Design decisions worth knowing

- Persona names were chosen to avoid collisions with Harbor & Pine (Michal, Avi) and module 09 (Rana,
  Samira): counsel is Hagit Peretz, the CFO Eyal Dahan, the Head of Nursing Suha Nasser, Fatma's daughter Hiba.
- Data room: seed 20261115, about 0.9 MB plus 80 KB of PoC files; two runs give identical hashes. The visit
  export is an 8% sample with full doctor-day counts so per-visit times scale to a doctor's day.
- No LLM is called in this module's labs (the decision is a vendor selection, not a build), so both Track B
  scripts are deterministic; checked with Python 3.14.3 and pandas 3.1.0.

## Simulation link

`[Simulation: Vendor RFP](../../simulations/vendor-rfp/index.html?preset=galil)` in 10.4 and 10.5 (and in
10.6's references).
