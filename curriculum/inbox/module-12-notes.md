# Module 12 — notes for the main session

Written 2026-11-03 by the module 12 agent. Nothing committed. `node curriculum/tools/check-module.mjs 12` → 0 problems.

## For the sidebar (lesson titles = H1s)

- **Module 12 — Atlas & Rowe** (suggested)
  - 12.1 · The call
  - 12.2 · Discovery
  - 12.3 · Diagnosis
  - 12.4 · The hard part
  - 12.5 · Build: precedent search with a citation gate
  - 12.6 · Readout and debrief
  - Module quiz: `assessments/module-12-quiz.md`. Project: `projects/m12-atlas-and-rowe.md`.

## Templates

No new templates. Every link goes to an existing file in `templates/`.

## Simulations linked (existing presets only) and presets proposed

Linked: `roi-defender?preset=harbor` (12.3, with a note that it is Harbor & Pine), `vendor-rfp?preset=generic` (12.4, with a note that it is not a legal-AI tender). No simulation in 12.5 or 12.6.

Proposed `atlas` presets (numbers from `curriculum/engagements/module-12.md`):

1. **roi-defender `atlas`** (12.3): sponsor claims "6.2 h/week × 90 × 44 × ₪950 = ₪23.3M", "₪0.4M cost", "zero hallucinations", "associates use ChatGPT anyway, so a firm tool is safer"; ledgers: firm fees (hourly 56.8% of research; ≈ ₪814 fees per saved billable research hour; associates at 81% of target), capacity, control (curation ₪180k, librarian ₪240k, checking ≈ 10 min/citation by hand), customer's share (Carmel 15% of ₪4.33M hourly = ₪0.65M; NDA history ₪2,046 → ₪1,150 per NDA). Defensible year-1 numbers: A −₪3.71M, B −₪0.69M, do nothing −₪0.65M.
2. **steering-committee `atlas`** (12.6): Yoav (chair, cannot campaign), Shmuel (sceptic, weight 2), Noa (advocate; the sponsor-as-advocate branch fits her), Orit (ethics), Eli (finance, non-voting); outcomes map to the three futures; the near-miss disclosure as a branch.
3. **oversight-under-load `atlas`** (12.5): research answers ≈ 3,000 a month, 4 citations each, misstated rate ≈ 14% (22/160) before the gate, ≈ 4% after rules; check 1.4 min with source shown vs 9.5 without.
4. **pilot-economics `atlas`**: not a good fit (value is in fees by billing type, not handling time); roi-defender is the right one.

## Facts not verified / to check before publishing

- The Bar Association's AI opinions (May 2024; September 2026) were read through Pearl Cohen and Calcalist; the primary Hebrew texts on israelbar.org.il were not found/opened ⚠️. Lessons attribute them "as reported".
- Israeli court decisions read via secondary sources: Feb 2025 Supreme Court (no docket number found), the AIG class action (page undated), Cohen v. Ramat Gan (Adm. Appeal 63194-08-25) ⚠️. Lessons tell learners to read the judgments before citing them.
- Rule 19 and section 90 read on Hebrew Wikisource, not the official consolidated text ⚠️.
- ABA Formal Opinion 512 read via NatLawReview (ABA PDF 403) ⚠️.
- Lexis+ AI and Microsoft 365 Copilot pages could not be opened; neither is named in lessons.
- Legal-AI vendors publish no prices; Parshan AI (fictional) prices are invented (US$120/seat/month, 20% discount, US$25,000 set-up).
- Hebrew text in the corpus, the memo comments and the Arabic and Russian survey comments were written by the agent: a native read of the Hebrew rulings and memos (`data-room/textbank.py`) is worth doing.

## Design decisions worth knowing

- Fictional rulings use a citation format that cannot collide with real Israeli dockets: `FCR-YYYY-NNN` (rulings), `ARM-` (firm memos), `ARP-` (clause notes); every corpus file carries a "FICTIONAL … not a statement of Israeli law" banner. No real case is cited as if it were in the corpus.
- Generator split into modules under 400 lines each (`generate.py`, `common.py`, `textbank.py`, `firm.py`, `activity.py`, `signals.py`, `corpus.py`, `km.py`, `pilot.py`, `documents.py`, `documents2.py`), per the coordinator's instruction. Two runs produce identical hashes for all 154 data files; data room 1.7 MB.
- `generate.py` also writes the pilot data files (questions, curation, drafts, labels, check sheet, batches); `pilot/system-prompt.md` and `pilot/negative-questions.csv` are hand-written.
- Search, gate rules and ROI are real, deterministic, no-AI baselines; LLM-judge, assistant-answer and timing figures in 12.5 and `expert/05`–`06` are an illustrative worked example and say so (no API key in the build), following modules 5 and 8.
- The ROI model's year-1 result is negative for every option against a zero baseline; the lessons compare against "doing nothing" (where Carmel's 15% is conceded) and make the point that B is about break-even and avoids A's loss. Tal may want to check this framing reads as intended.

## Cross-module notes

- 12.4 points to the RFP method in 10.4 for the June platform decision.
- `references/laws-and-guidance.md` has no legal-profession entries; suggested additions are at the end of `module-12-sources.md`.
- Module 18 (capstone) could reuse the citation gate as a generic control for any research assistant.
