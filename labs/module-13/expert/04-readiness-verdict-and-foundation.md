# 04 · Readiness verdict, foundation plan and constraints

For Dalia Mizrahi, Orit Navon and Amnon Shaked. Thursday 25 February 2027. Labels: **verified** (checked against data or seen), **reported** (someone says so), **contradicted** (data says otherwise).

## 1. The bar, written on Sunday 14 February — before the vendor's presentation

Predictive maintenance is "ready" at Kinneret when, **for the machines it would cover**:

| # | Criterion | Why |
|---|---|---|
| P1 | One register: every machine, auxiliary and mould has one id used by MaintPro, ProdTrack, the historian and the alarms | A prediction must land on the right asset |
| P2 | At least 12 months of breakdown records with a failure mode on ≥ 80% of them | The vendor's own prerequisite (onboarding guide 3.2) and ours |
| P3 | At least one failure mode with ≥ 30 recorded events on instrumented machines | The vendor's minimum per mode (3.2) |
| P4 | Time-synchronised sensor data on the target machines for ≥ 6 months, with known gaps | 3.3, and our own clocks |
| P5 | The outcome recorded: stop and restart times, what failed, what was done | Otherwise nothing can be checked |
| P6 | A named person with hours to review and label alerts in the learning period | 3.4 |
| P7 | The works committee has agreed how the records are used (local agreement clauses 14–15) | Without it the records will not be made honestly |
| P8 | The losses it would address are a large share of our downtime, measured | Otherwise it cannot move Arava |

## 2. The evidence against the bar

| # | Evidence | Status | Met? |
|---|---|---|---|
| P1 | 9 of 26 Plant K machines carry their ProdTrack code; moulds have no MaintPro id; 4 Plant G hall numbers ≠ ProdTrack numbers; SCADA stations by hall number | Verified | No |
| P2 | Plant K: 14.2% of breakdown WOs coded, falling during 2026; Plant G: no code column. "Failure modes coded: yes, in the log" (Plant G questionnaire) | Verified; questionnaire contradicted | No |
| P3 | Usable labels (coded and matched to a ProdTrack stop): 73 of 861 (8.5%); largest code 12 events; none ≥ 30 | Verified | No |
| P4 | 3 of 40 machines, from 1 October 2026; ~60 h missing per machine; K21 vibration stuck for 197 running hours; Plant G alarms in UTC, month-first | Verified | No |
| P5 | Completion times bunched at shift change (60.9%) and Thursday bulk closes (13.6%); Plant G "ready" ≠ restart (median 51 min later) | Verified | No |
| P6 | No reliability engineer; the maintenance manager plans to retire in 2028 | Reported | No |
| P7 | Committee letter of 12 January; protocol in draft since 23 February | Verified | In progress |
| P8 | Machine faults are 24% of unplanned hours; moulds 46% (not covered by the platform) | Verified (split directional) | No |

**Verdict: predictive maintenance — not yet.** Not "no": the bar is written, the foundation below meets P1, P2, P4, P5 and P7 by December 2027, and P3 can be tested in January 2028.

**What would change it:** 12 months of coded breakdowns on the eight instrumented machines, with at least two failure modes above 30 events, or a vendor proof of concept on Kinneret's own data that shows its false-alarm rate. **Re-decision: management meeting, January 2028**, with the vendor proof-of-concept protocol written in advance.

## 3. The foundation plan (₪730,000 of line 7400-210)

| Work | Owner | Done by | Cost | Gate evidence |
|---|---|---|---|---|
| Common asset register: machines, auxiliaries, 231 moulds, statutory items; crosswalk MaintPro–ProdTrack–historian–SCADA; QR labels | Vladimir Kaplan with Shlomi Biton; Fadi Khoury for moulds | 30 April | ₪45k | Every ProdTrack stop and WO maps to one id |
| Recording at the machine: MaintPro mobile on 6 shared tablets per plant hall area, Hebrew/Arabic/Russian screens, a 15-mode failure list written with technicians (ISO 14224's component / failure mode / cause structure as a reference, not a template), Plant G onto MaintPro | Vladimir Kaplan; HR for training | Plant K 30 April; Plant G 30 June | ₪260k | ≥ 80% of breakdown WOs with a mode by 30 September |
| Parts: live ERP view, drive copy deleted, bins labelled, critical spares | Avi Malka | 31 March | ₪40k | Drive copy gone; spot check of 30 bins |
| Night mould response and shot counters (Arava plan) | Fadi Khoury, Tigist Wondimu | 31 March | ₪130k | Night mould mean hours, monthly |
| Thresholds on K21–K23 (done 3 February); sensors and historian on K05, G11, K03, G08, G06, G07, G04, K04 | Vladimir Kaplan, Boaz Tal | 30 September | ₪140k | Data complete ≥ 95% of hours |
| Manual-assistant pilot (see 05) | Operations excellence; Vladimir Kaplan and Yaakov Dahan own the pack | Pilot from 4 April | ₪45k | Gates in the pilot charter |
| Contingency | Orit Navon | — | ₪70k | — |

**Stop rule:** fewer than half of breakdown WOs carry a failure mode on 30 June → stop stage 2 recording spend and review with the works committee.

## 4. Vendor read-back (Predictiva, after 15 February)

| Claim | Condition we found | Status |
|---|---|---|
| "Up to 50% less unplanned downtime" | Machine-mounted sensors; moulds "on the roadmap" | Applies at most to 24% of our downtime |
| "94% prediction accuracy" | 94% of NordVind's bearing failures had an alert ≥ 30 days before; false-alarm rate not shared | Recall only, in another industry, with six years of coded data |
| "ROI in 9 months" | NordVind | Not measured in plastics; no injection-moulding customer in production (Gilad) |
| "90-day learning period, then predictions" | Customer's reliability engineer labels every anomaly; data readiness service US$40,000 | We have no one to label |
| "₪310,000 excess stock" | Run on the drive's parts list of March 2025 (sent by Plant G without authorisation) | Contradicted as a figure |
| "Conference price until 31 March" | 15% discount tied to Kinneret being a reference site (Amnon's conversation) | A pressure date, not ours |
| Operator behaviour analytics | Cameras at each machine | Not recommended: clause 15 and the privacy principles below |

## 5. Constraints that shape the design (Israel first)

| Constraint | Source | Design rule | Owner |
|---|---|---|---|
| Up-to-date instructions for safe use and maintenance of equipment; the written risk summary in Hebrew and another language the worker understands; a training log | Organisation of Labour Supervision (Provision of Information and Training to Workers) Regulations, 5759-1999 (תקנות ארגון הפיקוח על העבודה (מסירת מידע והדרכת עובדים)), regs 2, 6, 7(b) | Old translations off the drive; approved Arabic and Russian rev. D of LOTO, gate, escalation and hot-runner SOPs before the assistant uses them; the assistant is a reference, not training | Yaakov Dahan |
| A safety management programme for a factory with 50+ workers: list of items needing periodic safety tests with due dates and follow-up; list of procedures with last update dates | Organisation of Labour Supervision (Safety Management Programme) Regulations, 5773-2013, regs 1, 5(6), 5(10) | Statutory items in the common register with computed (not typed) due dates; translations listed with their revision | Yaakov Dahan |
| Lifting machines examined at least every 14 months; air receivers every 26 months; examiner's report into the plant register | Work Safety Ordinance [New Version], 5730-1970 (פקודת הבטיחות בעבודה), ss. 81, 115, 119א | Crane escalation done 20 January; register owned centrally | Yaakov Dahan, Eli Peretz |
| Safety committee, trustees and safety officer | Organisation of Labour Supervision Law, 5714-1954 (חוק ארגון הפיקוח על העבודה), ss. 10–25 | The safety committee reviews the assistant's safety rules before the pilot | Yaakov Dahan |
| Technician ids in work orders and assistant logs are personal data; purpose limitation; workplace monitoring only for a legitimate, proportionate, disclosed purpose; camera footage not used for other purposes such as discipline | Privacy Protection Law, 5741-1981 (חוק הגנת הפרטיות) as amended (Amendment 13); *Isakov Inbar*, National Labour Court, 2011; Privacy Protection Authority guidance on workplace cameras (October 2017) | Records used for maintenance, not individual evaluation; assistant logs kept without user id, 90 days; no cameras; route the notice wording to counsel | Michal Aharon, counsel |
| Consultation before technological change; no monitoring without agreement; training in a language understood | Local agreement 2021, clauses 14–16 (Kinneret's); the duty to consult workers' representatives in good faith in an organised workplace (counsel to confirm scope) | Written protocol before any change on the floor: no individual performance reports, no discipline from the records, Arabic recording, paid training, joint committee | Michal Aharon, Khalil Mansour |
| EU AI Act, machinery rules | Kinneret operates machines in Israel and sells parts, not AI systems, to EU customers | Not in scope for these uses; revisit if a customer asks | — |

## 6. Protocol with the works committee (draft sent 25 February, Hebrew and Arabic)

1. Breakdown recording and the asset register are for maintenance and reliability. No report of individual technicians' performance will be produced from them; they will not be used for discipline (clause 15).
2. No cameras or location tracking are part of this project.
3. Recording is possible in Hebrew, Arabic and Russian; training is paid, in work hours, in the worker's language.
4. The joint committee (clause 14) meets before each stage starts; a technician named by the committee is in the assistant's test group.
5. No change in staffing results from this project in 2027.
6. Reviewed after six months.
