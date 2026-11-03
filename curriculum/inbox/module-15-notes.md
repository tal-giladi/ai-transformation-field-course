# Module 15 — notes for the main session

Written 3 November 2026 by the module 15 agent. Nothing committed. `node curriculum/tools/check-module.mjs 15` → 0 problems.

## For `_sidebar.md` (main session)

- **Module 15 — Crescent Bank**
  - 15.1 · The call → `lessons/module-15/lesson-01.md`
  - 15.2 · Discovery → `lesson-02.md`
  - 15.3 · Diagnosis → `lesson-03.md`
  - 15.4 · The hard part: an operating model that scales → `lesson-04.md`
  - 15.5 · Decide: triage, design and a 12-month plan → `lesson-05.md`
  - 15.6 · Readout and debrief → `lesson-06.md`
  - Module 15 quiz → `assessments/module-15-quiz.md`
  (Use the course's running numbers in the link text; the titles above match the H1s.)

## Simulation: `operating-model-scaler`, preset `crescent`

The engagement matches the preset: the 14 units, all 40 pilots with their themes, risk tiers and the 10 weak ones (the triage rules reproduce exactly the preset's 10 weak and its tiers 15/14/11), the four duplicate pairs, the assistant with its two dependents, 3 slots a quarter at ₪150,000, full validation, the central/hub/federated team costs, platform ₪2.4M, templates ₪200,000, catalogue ₪150,000, the contractor ₪350,000, and the expert's design and answers. Linked in 15.3, 15.4 (twice), 15.5 (twice), 15.6. Numbers quoted in the lessons were produced by running `model.js` in node (scratch script, not in the repo): expert after 4/12 quarters 26/36 in production; today 2/7; central with 6 slots 5/18; federated 40 live with 10 weak; expert with the assistant cut 33 after 12 and 2 stalled.

What I would change in the preset (the lessons stay consistent with it and say why the plan differs):

1. **Year-one throughput is optimistic.** The expert reaches 26 in production after four quarters. A bank needs procurement, DPIAs, change control and (for staff tools) consultation with the employees' representatives; the plan in 15.5 commits to 14 by March 2028 and the expert future shows 17. Suggest `build.byMaturity` 1: 4, 2: 3, 3: 2 and a one-quarter onboarding delay on the platform, or note in the preset that the counts are a ranking, not a forecast.
2. **Timing of events.** The data room surfaces the shadow builds, the complaints duplicate and the 15% cut in January 2027 (the cut is the 2027 budget review), while the sim fires them in Q2 2027, Q3 2027 and Q3 2028. The lessons say the simulation compresses three years. Optionally move the budget event to q 1–2 for `crescent`.
3. **Money scope.** The sim's ₪11M a year is the central programme only; the engagement adds about ₪9.1M of AI lines in the units' budgets (pilot vendors, the assistant's licences), so the CFO's 15% is ₪3.02M of ₪20.13M. Consider a line in the preset's notes.
4. **Key person.** The sim has the head of validation and two validators leave in Q2 2028; the data room's MRM is a head and two validators (the plan's "model-risk team with two people"), and the head's fintech offer is a hidden fact in the CRO persona; future 3 has him leave in May 2027. Both are consistent with "people risk in MRM"; no change needed unless you want the event earlier.
5. **Kesher CRM wave.** The sim's vendor-release wave is Q3 2029; the data room has Kesher release 27.1 switching on generative features in October 2027 (renewal notice by 2 March 2027). Lessons treat it as an intake item, not the sim event.

## Facts and decisions for Tal

- **Directive 369 phase-in date.** Circular 2792-06 §12 says existing non-material models must comply within eighteen months of 21 August 2025, i.e. by 21 February 2027; the lessons use that date. The circular's text also contains a confusing "(August 21, 2024 [2025])" in §12(b); the Hebrew original is binding (⚠️ manual check by a Hebrew reader if exact wording matters).
- **Directive 310** was read in its 09/21 Hebrew version; a 02/23 version exists (⚠️ manual check). It is only named in the lessons.
- **The Bank of Israel press-release page** for 17 May 2026 showed a bot check; the attached .docx opened and is the cited source. A secondary claim (bizportal) of ~70 AI applications in Israeli banks and a Gartner-based self-assessment questionnaire was not verified and is not used.
- **SR 11-7 was superseded by SR 26-2 (17 April 2026)**, which excludes generative and agentic AI from scope. 15.4 uses this as "don't import a US reading". No other module cites SR 11-7.
- **Vendor and product names are invented** (Tzofen, Tzofen Assist, Ananim Cloud AI, Mishov Analytics, Bahir Labs, Kolelet AI, Rishum Docs, Mismach Check, Imut Docs, Pinkas AI, Katvan AI, Sichon AI, Kishron Rank, Hatama AI, LLMHub / llmhub.io, AIWriterPro, freetrans.net, Kesher Systems / Kesher 360, Notzer Fraud Systems, Shomer AML, Hadas Data, Atid, Mizrah). A quick check that none is a real product in Israel would be prudent before publishing; `llmhub.io` and `aiwriterpro.com` are used as hostnames in the proxy extract.
- **Real regulator, fictional bank.** Personas and lessons say what the fictional bank told the Bank of Israel's survey and that its CCO expects follow-up; every place says nothing is a statement of what the real Banking Supervision Department did or would do. Tal may want to review the futures in 15.6 (future 1 says "the supervisor asked for the inventory in Q1 2028" — copied from the simulation's event, which carries the same disclaimer).
- **A possible template.** No template name is reserved for M15. An "operating-model design" template (archetype comparison, hub–spoke line, tier rule, decision table, queue, paved roads, catalogue fields) would help 15.4 and the capstone; I re-used governance charter, intake register, operating rhythm and roadmap instead. Tal decides whether to add one.

## Cross-module

- 04.7's "three numbers for the board" and 07.2's merge and decommission steps are used as written; 07.6 operating rhythm is linked from 15.4 and 15.6.
- Module 14 (another agent) was not touched.

## Time estimate

Lessons: minutes 17 + 19 + 16 + 22 + 21 + 22 = 117; practice 90 + 150 + 100 + 150 + 180 + 180 = 850; project about 240; quizzes 30. Total about 1,237 minutes ≈ **20.6 hours**.
