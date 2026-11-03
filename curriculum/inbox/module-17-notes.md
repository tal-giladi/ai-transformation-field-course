# Module 17 — notes for the main session (Vantage Logistics)

## Sidebar entries (for `_sidebar.md`)

- **Module 17 — Vantage Logistics**
  - 17.1 · The call — `lessons/module-17/lesson-01.md`
  - 17.2 · Discovery — `lessons/module-17/lesson-02.md`
  - 17.3 · Diagnosis — `lessons/module-17/lesson-03.md`
  - 17.4 · The hard part: a turnaround — `lessons/module-17/lesson-04.md`
  - 17.5 · Decide: the stop/keep audit and the incident closed — `lessons/module-17/lesson-05.md`
  - 17.6 · Readout and debrief — `lessons/module-17/lesson-06.md`
  - Module 17 quiz — `assessments/module-17-quiz.md`

## Proposed simulation presets (no `vantage` preset exists; lessons link Harbor & Pine's)

1. **`incident-tabletop?preset=vantage`** (for 17.5). Start: Tzir Docs 4.2 live, "contained" status already set by the vendor (trust starts low). Injects over five days from Monday 7 June 2027: (t0) logs show 7 post-fix mismatches; (t+3h) access log shows cross-customer opens after the Assist feature was off, via the portal file page; (t+6h) the opened documents include B2C manifests with consignee data (2,462 records); (day 2) nine customs value queries past their requested dates, three Gefen shipments held; (day 3) the vendor offers a hotfix 4.2.2 "next sprint" and asks to keep "contained"; (day 5) a second customer asks whether its invoices were seen. Best options: narrowest switches (auto-match off for numeric keys; portal page hides documents not owned by the file's customer), facts to counsel the same day, the licensed customs agent and counsel on declarations, customer by a person with facts, root cause as contributing causes. Never an option stating a legal deadline as right. Exposure per inject: cross-customer opens and records as in `discovery.py` section 5.
2. **`steering-committee?preset=vantage`** (for 17.6): cast = board chair Yehuda Karni (weight 2), audit committee chair Ilana Shaked (2), CEO Ofer Lavi (1.5, sponsor-as-advocate round on "Tzir was the right decision"), CFO Svetlana Morozov (1), a director who wants everything switched off (1). Rounds: incident closed or not; which numbers survive the auditor; why keep anything; the vendor; the half-year. Outcomes: approved with conditions (expert), sent back, "switch it all off", "blame the vendor". The facts each round needs are in `labs/module-17/expert/06-board-brief.md`.
3. Optional: `roi-defender?preset=vantage` with the four savings lines (₪3.1M fuel, ₪1.6M customs, ₪0.9M CS, ₪0.6M warehouse) and their evidence from 17.3.

## Facts and names

- **"Vantage Logistics"** is the plan's name. Unrelated firms with that name exist in Vietnam (Vantage Logistics Corp., Ho Chi Minh City) and Canada (a 3PL in Dorval, QC); none in Israel was found (search 3 Nov 2026). The brief, profile and data room say the company is fictional and that unrelated firms with similar names exist abroad. Tal may want a different name; renaming touches every file in `labs/module-17/`, the lessons, the project and the quiz.
- Fictional vendors and customers searched on 3 Nov 2026, no company found: Tzir AI, Kotev Assist, Ayin Drive, Mishkal ERP, Meches Pro, Mabat Fleet, Promptway, Gefen Medical Distribution. Others (Nezek Vision, Taarif Software, Shuk Online Imports and the 24 customer names in `gen_common.py`) are compound names unlikely to be real but were not each searched.
- **n8n** (real) is named only as the tool a CS team used; no price or term of n8n is stated (no card line for it).
- Companies Law s. 117 and the gov.il originals of PPA guideline 5/17 and the location-data opinion were not opened at a primary source; lessons describe them only in general terms and route the reading to counsel/HR (see the sources inbox).
- Israeli customs: the lessons cite the Customs Agents Law only as the statute that licenses agents; how declarations are corrected is routed to the licensed agent and counsel. No customs deadline is stated. The "response requested by" dates in `customs/customs-queries-2027.csv` are fictional customs letters' dates, not legal deadlines.
- Privacy: the lessons quote only the IAPP tutorial's "immediately" for serious security incidents under the 2017 regulations and say Amendment 13 has changed the law since; every reporting decision is counsel's. GDPR Article 33 is named for EU counsel; its 72-hour figure is not stated as the learner's deadline.

## Cross-module

- The module re-uses by link 07.2 (decision record), 07.3 (bad news upward), 07.5 (incident runbook) and 07.7 (pressure-test log), plus 01.x, 02.x, 03.7, 03.9, 04.3, 04.5, 06.5, 07.1, 07.4, 07.9. No new template is needed. A main-session option: add a "Reporting protocol (two or more principals)" section to `templates/engagement-charter.md` — 17.1 teaches it as a new move; it is short enough to live inside the lesson for now.
- 17.6 is the only engagement where the learner leaves after the readout; the handover is to owners who stay. Module 18's capstone may want to reference this.
- The fictional public LLM API is "Promptway" here (module 15 used "LLMHub"); intentionally different.

## For Tal to decide

- Whether to keep the name "Vantage Logistics" given the foreign namesakes (see above).
- Whether to build the `vantage` presets (above) or leave the Harbor & Pine links.
