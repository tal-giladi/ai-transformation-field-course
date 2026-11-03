# 02 · Findings memo

To: Dalia Mizrahi. Copy: Vladimir Kaplan, Eli Peretz (sections on their plants shown to them first). From: operations-excellence manager. Thursday 28 January 2027. Labels: **M** measured from the exports, **R** reported by a person, **I** inferred. Periods: 2026 calendar year unless stated. Unplanned = every ProdTrack stop except PM, mould change (SETUP) and no order.

## The answer first

Kinneret does not mainly lose time because machines fail without warning. It loses it because **stops last too long — above all mould stops at night — and nobody records what failed**. Predictive maintenance needs exactly the records we do not keep, and would watch the quarter of downtime that is machine faults, not the half that is moulds.

## Safety items escalated the same day (not waiting for this memo)

- **20 January, 11:40: Plant G crane 2 (mould changes) is past its statutory examination.** Last examined 11 August 2025, due 11 October 2026 (`safety/periodic-examinations-register.csv`, status typed "valid"). The Work Safety Ordinance requires a lifting machine to be examined by a qualified examiner at least every fourteen months (s. 81). Told Eli Peretz and Yaakov Dahan in person; crane 2 tagged out the same afternoon; examiner booked for 25 January (R).
- **19–21 January: the Arabic (2019, rev. B) and Russian (2016, rev. A) lockout procedures on the drive lack the accumulator-discharge step** that the Hebrew rev. D (2023) has (`docs/SOP-LOTO-01-*`). A night technician follows the Arabic one (R). Told Yaakov Dahan on 21 January; he removed both from the drive and briefed night technicians orally the same week.

## Findings

1. **Moulds, not machines, are the largest unplanned loss (M).** 11,932 unplanned hours: moulds 46% (5,479 h), machine faults 24% (2,840 h), waiting for a technician 13% (1,538 h), material 9% (1,051 h), other and QA hold 9%. The December deck shows "breakdowns" = machine + mould. Reasons are chosen by operators (directional, R Tigist).
2. **Mould stops at night last three and a half times longer (M, R).** Mean 14.2 h at night against about 4 h by day; 229 night mould stops took 3,255 h. Tooling works Sunday–Thursday from 07:30 (R Vladi, Tigist).
3. **The failure history is not in the systems (M, R).** Of 861 Plant K breakdown work orders, the failure code is blank on 66.6% and "99 – other" on 19.3%; 43.4% of action texts say only "fixed/done"; coding fell during the year. Plant G's log has no code column. Completion times bunch at shift change (60.9% in the 15 minutes before) and on Thursday afternoons (13.6% closed by the planner), so repair durations cannot be measured from MaintPro. The real history is the maintenance manager's memory and a night-shift WhatsApp group (R, M).
4. **"Ready" means different things at the two plants (M, R).** Plant K's MTTR (5.7 h) runs from stop to production restart; Plant G's (3.5 h) from call to "ready", when the technician hands back. Matched to ProdTrack, Plant G's restart comes a median 51 minutes after "ready"; on the same definition Plant G is 5.8 h. Galil is not faster.
5. **One machine, three names (M).** Plant K's register carries a ProdTrack code for 9 of 26 machines; no criticality anywhere; moulds have no id in MaintPro (231 in tooling's list, 19.5% with a shot count). At Plant G four hall numbers (3, 5, 9, 12) are not the ProdTrack numbers since the 2025 rearrangement (matched on serial numbers). Plant G's SCADA exports month-first dates in UTC; its log, day-first local time.
6. **Sensors on 3 of 40 machines, three months of history (M).** K21–K23 since 1 October; 60-odd hours missing per machine (an outage on 19–21 October); K21's vibration channel shows the same value for 197 running hours (stuck). K22's pump bearing failed on 2 December; its vibration crossed the maker's 4.5 mm/s warning on 22 November and nobody had set an alarm (R Vladi; now set).
7. **PM compliance is lower than reported, and it shows (M, R).** Reported 96.7% (closed ÷ scheduled). 18 PMs on six machines (K03, K05, K07, K11, K14, K24) for July–September were closed by the planner on 30 September with no labour or parts. With labour recorded: 92.4%. Those six machines had 1.59 machine stops per machine-month in January–September and 3.17 in October–December; the other twenty, 1.36 and 1.18.
8. **The parts list technicians use is a stale copy (M, R).** The drive's list was last saved on 16 March 2025: 37 of its 268 part numbers (13.8%) are superseded in the ERP, no bin location matches (the warehouse was re-labelled in August 2025), and Plant G's 38 parts are not in it. 32 work orders say a part was not where the list said. The vendor's ₪310,000 "excess stock" demo used this file (M, emails).
9. **Night knowledge runs through one phone (M, R).** 78 logged night calls to the maintenance manager from March to December (about 1.8 a week); the machine waited a median 42 minutes per call, 64 hours in all; 59% were solved by phone. Topics: unknown alarm codes, hot runners, whether a mould may run with a cavity closed, parts.
10. **AI is already on the night shift (M, R).** Technicians photograph English manual pages and ask a free chatbot on personal phones (R). In the WhatsApp group on 12 November, a chatbot answer ("raise the tip to 300 °C for 10 minutes") was followed and burnt a hot-runner heater (M). No approved tool exists; no data policy covers it.
11. **Quality's data is the best-coded in the company (M).** Weekly scrap by machine with defect codes: 98.2% of scrap coded. Short shots rise in the weeks before some machine stops. Nobody in maintenance looks at it.
12. **The trigger is Arava, and Arava's reasons are our own notices (M).** OTIF 81% against 95%; 14 of 22 late notices said "machine breakdown". Both October short-shot complaints were night production after a restart (letter); at night the shift supervisor approves first parts (R).

## What we did not check

Danny's 22 notices against ProdTrack stop by stop (next week); the notebook history; Plant G's parts stock; the cost of an hour (Orit, 13.3).

## Who this protects

No technician is named. The planner closed what she was told to close. The deck's MTTR slide was mine; the definition problem is mine to fix.
