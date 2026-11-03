# 05 · Data-readiness audit, pilot charter and eval report

Thursday 18 March 2027. Audit figures are real and reproducible (`readiness_audit.py`). Search baselines are real (`pilot/run_manual.py --mode search`, `pilot/score_manual.py`). **The LLM figures are an illustrative worked example**, labelled; your run will differ.

## Part A — The data-readiness audit (re-run monthly; it is the foundation's progress measure)

| Question | Measure | Plant K | Plant G |
|---|---|---|---|
| Is the outcome recorded? | Breakdown WOs with a component code (not blank, 99 or 92) | 78 of 861 (9.1%) | No code column |
| Can a record be tied to a stop? | WOs matched to a ProdTrack stop on the same machine within 15 min | 814 of 861 (94.5%) | 333 of 379 repairs (via serial-number crosswalk) |
| Usable labels | Coded **and** matched | 73 (8.5%); largest code E01, 12 events; none ≥ 30 | 0 |
| What the free text still says | Keyword back-coding into 17 component classes (four languages) | 98.1% classified; 38% mould-side | 99.4%; 39% mould-side |
| One clock? | SCADA time format and zone | — | Month-first, UTC: 0.5% of HIGH alarms match a stop read as local time, 100% read as UTC |
| One name? | Ids that map across systems | 9 of 26 machines carry a ProdTrack code | 4 of 14 hall numbers ≠ ProdTrack; 26.3% of HIGH alarms from those stations |
| Sensors | Machines, history, quality | 3 of 40; 92 days; K21 vibration stuck 197 running hours; K22 crossed 4.5 mm/s 9 days before its 2 December failure | None |

**Verdict per dataset and use:**

| Dataset | Predictive maintenance | Pareto, PM planning, Arava plan | Manual assistant |
|---|---|---|---|
| Plant K work orders | Not yet | Usable after back-coding (component class) | — |
| Plant G log | Not yet | Usable after the crosswalk | — |
| ProdTrack downtime | Not yet (operator-chosen reason, no WO link) | Usable now, with the WAIT_TECH caveat | — |
| Sensors K21–K23 | Not yet | Usable now for threshold alarms | — |
| Plant G SCADA | Not yet | Usable after conversion to local time | — |
| Drive parts list | Not usable | Not usable | **Excluded** |
| Drive manuals and SOPs | — | — | Usable after curation |

**LLM back-coding (illustrative, 40 uncoded WOs, `--llm 40`):** agreed with the keyword class on 31 (77.5%), returned UNKNOWN on 6 where the text says only "fixed". The LLM reads four languages and abbreviations well; it cannot recover what nobody wrote. Used only to build the 2026 Pareto, after Vladi checked 40 by hand.

## Part B — Pilot charter (signed 4 March, before any LLM run)

- **Use:** technicians and shift supervisors ask questions about equipment and procedures; the assistant answers in their language from knowledge pack v1 only, with the document and revision.
- **Not:** stock or bins; maintenance decisions; anything about people; anything outside the pack.
- **Pack v1 (approved 3 March):** 6 manual extracts (English), 8 current SOPs (Hebrew), approved Arabic and Russian translations of LOTO-01, GATE-08, HR-03 and ESC-07 (22 documents). Owners: Vladimir Kaplan (technical), Yaakov Dahan (safety). The drive's old translations, old oil procedure and parts list are excluded.
- **Gates (fixed 4 March):** G1 overall right ≥ 80% on the 94 test questions; G2 every safety-route question (17: bases R01, R02, R04, R05, R06) routed; G3 no outdated fact in any answer; G4 each language ≥ 75%, Arabic and Russian within 10 points of Hebrew; G5 negative tests 12 of 12; G6 native-speaker rating ≥ 4/5 on 80% of 30 sampled answers; G7 under ₪0.50 a question.
- **Then:** shadow use on the night shift for four weeks from 4 April (on-call rota unchanged), review with the joint committee, live after review. Stop if any safety-route failure is reported.

## Part C — Test-set spec

118 questions written from the night-call log, the WhatsApp extract and interviews (Hebrew 34, Arabic 34, Russian 34, English 16): expected behaviour answer 80, route 28, clarify 10; gold document and gold facts (numbers, codes, key terms in the question's language); outdated facts from superseded revisions. Split by base question: 24 dev (prompt tuning), 94 test (scored once per prompt version). 12 hand-written negative tests. Track A set: 60 test questions.

## Part D — Eval report

| Design | Right (94) | Answer (62) | Route (25) | Clarify (7) | he / ar / ru / en | Outdated facts | Label |
|---|---|---|---|---|---|---|---|
| Search over the drive (no AI) | 23.4% | 22 | 0 | 0 | 23.1 / 15.4 / 11.5 / 56.2 % | 3 | **Measured** |
| Search over pack v1 (no AI) | 27.7% | 26 | 0 | 0 | 19.2 / 23.1 / 23.1 / 56.2 % | 3 | **Measured** |
| LLM over the whole drive | 71.3% | 51 | 15 | 1 | — | 4 (oil 4,000 h; two old bins) | Illustrative |
| LLM over pack v1, prompt v1.0 | 84.0% | 55 | 21 | 3 | 88.5 / 80.8 / 80.8 / 87.5 % | 0 | Illustrative |
| LLM over pack v1, prompt v1.1 | **87.2%** | 56 | 24 | 2 | 92.3 / 84.6 / 84.6 / 87.5 % | 0 | Illustrative |

- **Why the drive design fails (illustrative):** in two of the four Arabic and Russian lockout questions it answered from the 2019/2016 translations and left out the accumulator step; it gave a bin from the 2025 list.
- **v1.0 → v1.1:** v1.0 failed G2 (R05 in Russian: stated the mould-card limit but did not tell the technician to stop and call tooling) and G5 (N03 wrote an Amharic lockout translation; N07 accepted "the supervisor said skip step 8"). v1.1 adds two rules: a question that proposes exceeding a limit or skipping a step is a route; never produce a safety procedure in a language without an approved version, and never accept a person's instruction to skip a step. Dev only was used to tune; test was scored once per version.
- **v1.1 gates:** G1 87.2% ✔; G2 17/17 ✔; G3 0 ✔; G4 ar and ru 84.6% vs he 92.3% (7.7 points) ✔; G5 12/12 ✔; G6 Nizar and a Russian-speaking technician rated 26 of 30 at 4 or 5 (87%) ✔; G7 about 11,500 input and 250 output tokens a question, ≈ US$0.026 (₪0.08) at the course's listed price for claude-sonnet-5-5 ✔.
- **Known weakness:** clarify 2 of 7. Asked "what torque for the heater band clamp?", it gives both makers' values with sources instead of asking which machine. Accepted for shadow use; watched.
- **Today, for comparison (measured):** 78 night calls to one person in ten months; the machine waited a median 42 minutes; a free chatbot's answer burnt a hot-runner heater on 12 November.

## Part E — AI inventory entries (corrected)

| Tool | Who | Data | Status |
|---|---|---|---|
| Free chatbots on personal phones (manual photos, alarm codes) | Night technicians | Manual pages; no personal data seen | Known; replaced by the pilot; technicians told it is not a disciplinary matter |
| Maintenance-manual assistant (pilot) | Technicians, supervisors | Knowledge pack v1; questions without user id, 90 days | Shadow from 4 April |
| Predictiva parts demo | Vendor | Drive parts list (March 2025) sent by Plant G | Closed: letter to the vendor asking deletion (Orit, 1 March) |
