# Module 13 — notes for the main session

## Simulation preset proposal: `readiness-evidence-grader?preset=kinneret`

13.4 links the `harbor` preset as practice. A Kinneret preset would let learners sort Kinneret's own evidence. Proposed 18 items (status in brackets is the answer):

1. KPI deck: "Plant G repairs 1.6× faster" [contradicted: ready ≠ restart; 5.8 h vs 5.7 h on one definition]
2. Plant G questionnaire: "failure modes coded: yes" [contradicted: no code column]
3. Plant G questionnaire: "clocks synchronised" [contradicted: SCADA in UTC, month-first]
4. PM report: 97% compliance [contradicted as a measure of work done: 92.4% with labour; 18 bulk-closed]
5. MaintPro: 14.2% of breakdowns coded [verified]
6. Vladi: "nobody uses the codes" [reported → verified by 5]
7. Vladi: "night calls twice a week" [reported → verified: 1.8 a week]
8. Tigist: "mould stops wait for tooling at 07:30" [reported → verified: night mean 14.2 h vs 4.0 h]
9. Vendor: "94% prediction accuracy" [reported; conditions: recall, wind farm]
10. Vendor: "up to 50% less downtime" [reported; covers machine faults only]
11. Vendor: "₪310,000 excess stock" [contradicted: computed on the March 2025 replica]
12. Onboarding guide: "≥ 30 failures per mode" [verified as their requirement]
13. Historian: K21–K23 since 1 October [verified]
14. K22 vibration rose three weeks before failure [verified]
15. Exam register: crane 2 "valid" [contradicted: due 11 Oct 2026]
16. Drive: Arabic LOTO "translation available" [contradicted: rev. B lacks step 6]
17. Eli: "our Excel log is better than MaintPro" [reported]
18. Arava: OTIF 81% [verified as the customer's figure]
Verdict options: proceed / phase / not yet → not yet; the steering group's reaction to an honest report (approves the foundation) vs an over-claimed one (signs the vendor; future 1).

Other presets that would fit: `pilot-economics?preset=kinneret` (night mould response vs Predictiva: volume 229 night mould stops, hours, ₪181 an hour, cost ₪130k vs ₪343k a year); `steering-committee?preset=kinneret` (owner as sponsor-advocate branch). The lessons use only existing presets (`discovery-interview` harbor, `pilot-economics` generic, `readiness-evidence-grader` harbor, `oversight-under-load` generic, `steering-committee` harbor).

## Decisions taken that Tal may want to check

- **No foreign workers.** The plan allowed "Thai/Filipino contract workers possible — decide realistically". Israeli manufacturing has had very few foreign-worker permits (they are mostly in agriculture, construction and caregiving), so Kinneret's contract workers are Israeli manpower-agency workers, mostly Arabic speakers. The Foreign Workers Law is therefore not cited.
- **Works committee legal layer.** The local agreement (2021, clauses 14–16) is fictional. The only primary-ish source for a general duty to consult is Kol Zchut (dismissals); lessons say the wider scope is for labour counsel. If the course has a better source on consultation before technological change (case law), 13.4 could cite it.
- **ISO 14224** is cited from Wikipedia (the ISO page blocks bots). The lesson presents it as oil-and-gas standard used for its structure only.
- **Illustrative LLM figures.** As in module 11, 13.5 and expert/05 carry an illustrative LLM eval (labelled); search baselines and audit figures are real and reproducible.
- **Learner entry role.** "Internal lead with a day job" (an internal lead who also owns some of the audited data). It is the same family as 01.1's internal lead; the glossary entry is new.

## Facts not verified (also flagged in the sources inbox)

- PPA camera guidance read via Globes, not the PPA document; *Isakov* via a law-firm article.
- Training-log regulation amendment "2026" (ID numbers) came from a fetch summary; not used in lessons.
- Exchange rate ₪3.136 (2 November 2026) reused from the course, not re-opened.
- Plan names of ChatGPT, Copilot Studio and Gemini not re-verified (Claude's were).

## Cross-module

- Module 12's agent is writing in parallel; nothing in module 13 links to module 12.
- 13.1 links 11.1 (accidental owner) as the previous entry-role contrast.
- No new templates were needed; all links point to existing `templates/`.

## Files for the main session

- Data room size: about 1.9 MB (data-room) + 0.3 MB (pilot), under the 3 MB limit. `python generate.py` run twice, byte-identical.
- The generator is split into several modules in `data-room/` (gen_*.py, textbank.py, manuals_text.py, sops_text.py, pilot_questions.py) to keep each under ~400 lines.
