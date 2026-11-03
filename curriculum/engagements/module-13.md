# Kinneret Plastics — writer's notes for module 13 (never imported)

The sixth Stage 2 engagement. The learner is **the internal lead with a day job**: Kinneret Plastics'
operations-excellence manager, three years in the company, a Lean Six Sigma black belt, told at the
January management meeting to "do AI". The stated ask is "predictive maintenance with AI". The hard part
(13.4) is that **the data is not ready**: the learner has to say "not yet" to the owner's idea and get the
foundation funded instead (a common asset register, failure and outcome recording, sensors where they
matter, a parts list that is true), with a frontline, unionised, multilingual workforce whose work the
foundation changes. 13.5 builds the two honest things: a reproducible **data-readiness audit** of the
maintenance records (Track B is genuinely useful: thousands of free-text work orders, two plants, three
time conventions) and a **maintenance-manual assistant** (grounded Q&A over manuals and SOPs, answering
in Hebrew, Arabic, Russian and English) with an eval. The data room is built by
`labs/module-13/data-room/generate.py` (seed 20270110), which also writes the pilot's knowledge pack and
test set in `labs/module-13/pilot/`. Ground truth learners never see is only in this file.

## The organization

- **Kinneret Plastics Ltd.** (כנרת פלסטיק בע"מ; Arabic كينيرت للبلاستيك; Russian Киннерет Пластикс), a
  fictional family-owned injection-moulding company founded in 1978 by Shmuel Shaked; run since 2009 by
  his son **Amnon Shaked** (CEO, 64% owner; his sister holds 36% and sits on the board). Revenue 2026
  ₪412M; EBITDA ₪38M. Customers: caps and closures for beverage and dairy (52% of revenue), technical
  parts for home appliances (31%; the largest customer is "Arava Home Appliances", fictional, 17% of
  revenue), crates and logistics items (17%).
- **About 600 people**: Plant K (Kinneret, industrial zone south of Tiberias) 372, Plant G (Galil, an
  industrial park near Karmiel, acquired in January 2025 from its founders as "Galil Polymer Industries")
  176, head office and sales (at Plant K) 52. Three shifts (06:45–14:45, 14:45–22:45, 22:45–06:45),
  Sunday 06:45 to Friday 06:45, weekend crews for orders.
- **Languages** (HR 2026 file, Plant K production and maintenance): Arabic first language 46%
  (villages of the Lower Galilee and Tiberias), Hebrew 27%, Russian 17% (mostly 1990s immigrants, most
  technicians over 50), Amharic 6%, other 4%. About 40 operators come through a manpower agency
  (contract workers), mostly Arabic speakers. No foreign workers under the Foreign Workers Law: the
  brief's "Thai/Filipino contract workers" option was rejected as unrealistic for a Galilee plastics
  plant (note in the notes inbox). The CMMS screens are Hebrew only.
- **Machines**: 40 injection-moulding machines (IMMs). Plant K: 26 (K01–K08 "Haiwei HW" 1999–2008,
  K09–K20 "Kessler KX" 2010–2019, K21–K23 "Kessler KX-e" 2024 with built-in condition monitoring,
  K24–K26 "Haiwei HW-3" 2016). Plant G: 14 ("Morandi MP" 2003–2012 and "Haiwei HW-3" 2017–2019). All
  three machine makers are fictional. Auxiliaries: dryers, chillers, two compressor stations with air
  receivers, overhead cranes for mould changes (two per plant), robots. About 230 moulds, owned by the
  tooling department (a separate list, not in the CMMS).
- **Systems** (fictional): CMMS "MaintPro" at Plant K since 2014 (Hebrew UI; failure-code field added
  in 2019, optional); Plant G keeps maintenance in an Excel log (its CMMS licence lapsed at the
  acquisition); MES "ProdTrack" in both plants since 2025 (machine states and downtime reasons, entered
  by operators and shift supervisors at the machine terminal); ERP for stock and purchasing; a
  historian for K21–K23 since 1 October 2026; Plant G's line SCADA (alarms only); the maintenance shared
  drive (`\\kp-fs01\maintenance`) with manuals, SOPs and "the parts list".

## Who the learner is, and what changes

**You are Kinneret Plastics' operations-excellence manager** (מנהל/ת מצוינות תפעולית), reporting to
Dalia Mizrahi (VP operations and Plant K manager). Three years in: you ran the OEE programme, you
designed the MES downtime reason codes in 2025, and you ran the 2025 SMED project on mould changes. On
Thursday 7 January 2027, at the annual management meeting, Amnon said: "2027 is the year of AI. We start
with predictive maintenance. You will lead it." He had met a vendor (Predictiva) at a December industry
conference and liked a case study.

What changes for an internal lead (13.1, pointing to 01.1): you have access, history and credibility on
the floor, but you are not neutral — your own OEE dashboards and downtime codes are part of the data you
are about to audit, technicians remember the 2025 "tablets on machines" episode (the works committee
objected to the operator-ID login), and the person who gave the ask owns the company. You keep your day
job (OEE reporting, the Arava corrective-action plan). You have no budget of your own; the 2027 budget
has a ₪1.5M "AI and Industry 4.0" line Amnon added, which the CFO controls. You cannot commit anything
above ₪50,000 without the CFO and the CEO. Nobody at Kinneret has run an AI project.

## Stated ask vs hidden truth

- **Stated ask (CEO):** "Predictive maintenance with AI", starting with Predictiva's platform on all 40
  machines, "so machines tell us before they break". Vendor quote: onboarding US$60,000; US$95 per asset
  per month for at least 40 assets for 36 months; sensor retrofit kits through its integrator at ₪9,800
  per machine for 37 machines; "first predictions after a 90-day learning period".
- **Hidden truth.** Kinneret does not lose deliveries because machines fail without warning; it loses
  them because **stoppages last too long and nobody records why they happened**.
  1. **No outcome labels.** Breakdown work orders do not record what failed: the failure-code field is
     blank or "99 – other" on most of them; the action text is "תוקן" ("fixed") or "done". There is
     nothing for a model to learn from, at either plant. The real failure history is in the maintenance
     manager's notebooks (2004 onwards) and in a night-shift WhatsApp group.
  2. **Most unplanned downtime is not the machine.** Moulds (hot runners, cooling-water leaks, ejector
     pins), material (dryers, wet resin) and waiting (for a technician at night, for a part) together are
     most of the unplanned hours. Moulds have no asset id in the CMMS; machine-mounted sensors would not
     see them.
  3. **Sensors exist on 3 of 40 machines**, with three months of history, one stuck vibration channel and
     one real failure (K22 pump bearing, 2 December). Nothing to train on; enough to set a simple alarm.
  4. **Two plants, two meanings, three clocks.** At Plant G a machine is "ready" (מוכן) when the
     technician finishes; at Plant K "ready" means production restarted with QA approval of the first
     parts. The December KPI deck compares MTTR on the two definitions (Plant G looks twice as good).
     Plant K's CMMS writes ISO local time with offset; Plant G's Excel log writes DD/MM/YYYY local time;
     Plant G's SCADA exports US-format MM/DD/YYYY in UTC. No common asset register: the same machine has
     three names, and four Plant G machines are numbered differently in the MES and the Excel log since
     the 2025 hall rearrangement.
  5. **The parts list technicians and the vendor use is a stale replica**: an Excel copy of the ERP
     catalogue on the shared drive, last refreshed 16 March 2025 by a planner who left; part numbers
     superseded since, bins moved in the August 2025 warehouse reorganisation, no Plant G parts. Night
     technicians look for parts in the wrong bin; Predictiva's spare-parts demo used the replica.
  6. **The PM compliance figure is inflated.** "PM compliance 97%" counts closed PM work orders. In the
     Q3 order rush (Arava's summer programme) PMs on six machines were deferred and then bulk-closed on
     30 September as "בוצע" with no labour time and no parts. Those machines broke down more in Q4.
  7. **Knowledge is on one person's phone.** Night technicians call Vladimir Kaplan (maintenance manager)
     at home; the shift supervisors' night-call log shows the machine waiting while they do. Technicians
     who don't read Hebrew or English well use photos of manual pages and a free chatbot on their
     phones; one answer pasted into the WhatsApp group gives a wrong hot-runner setting.
  8. **Safety in the translations.** The lockout/tagout SOP was revised in 2023 (rev. D: discharge the
     hydraulic accumulator and verify zero pressure before opening the guard on machines with
     accumulators). The Arabic translation on the drive is rev. B (2019) and the Russian rev. A (2016);
     both lack the step. Arabic speakers are the largest group on the floor. (Organisation of Labour
     Supervision (Provision of Information and Training to Workers) Regulations 5759-1999: up-to-date
     instructions for safe use and maintenance of equipment (reg. 2); the written risk summary in Hebrew
     and another language the worker understands (reg. 7(b)).)
  9. **An overdue statutory examination.** Plant G's overhead crane G-CR2 (mould changes) was last
     examined on 11 August 2025; the Work Safety Ordinance requires a thorough examination of a lifting
     machine by a qualified examiner at least once every fourteen months (s. 81): due 11 October 2026. The
     asset-register work finds it. The learner must escalate the same day to the safety officer and the
     Plant G manager, not hold it for the readout.
  10. **The trigger is a customer, not a technology.** Arava's December letter: on-time-in-full 81%
     against 95% contracted for 2026; a corrective-action plan by 31 March 2027 or part of the 2027 volume
     moves to a second source. Amnon read "unplanned downtime" in the letter and heard "predictive
     maintenance".
  11. **Quality's data is the best-coded in the company**: weekly scrap by machine with defect codes
     (Arava requires it), almost fully coded. It is the most likely future source of an early-warning
     signal (process drift before a stoppage), and nobody in maintenance looks at it.
  12. **The vendor's evidence is from another industry and other conditions**: the case study is a wind
     farm operator (vibration on gearboxes, 1,400 turbines, six years of SCADA, coded failures);
     Predictiva's own onboarding guide asks for 12 months of history with at least 30 recorded failures
     per failure mode; its "operator behaviour analytics" option uses cameras at the machines (employee
     monitoring; Privacy Protection Authority camera guidance, October 2017; the 2021 local agreement's
     monitoring clause).
- **The honest answer:** "Not yet" for predictive maintenance, with a date and the evidence that would
  change it; fund the foundation from the ₪1.5M line (about half of it): a common asset register incl.
  moulds and the crosswalk; failure and outcome recording at the point of repair (mobile, in four
  languages, with a short failure-mode list technicians helped write, ISO 14224 as the reference); the
  parts list replaced by a live ERP view; sensors and a historian on the eight machines that cause most
  machine downtime; mould maintenance by shot count; an honest PM measure; one "ready" definition across
  plants. The quick win is the **maintenance-manual assistant** for technicians (grounded in the approved
  pack, answers in the technician's language, cites document and revision, refuses to help bypass a guard
  or interlock, sends LOTO and stored-energy questions to the current SOP and a person, never answers
  stock from the stale list). Re-decide predictive maintenance in January 2028 on 12 months of coded
  failures from the instrumented machines, with a vendor proof of concept on Kinneret's own data. Agree
  everything that changes technicians' work with the works committee first, in writing, with no
  individual performance monitoring from the new records.

## Planted findings (each discoverable, never stated)

Paths relative to `labs/module-13/data-room/`.

| # | Finding | Where |
|---|---|---|
| 1 | Breakdown work orders carry no failure outcome: code blank or "99" on most; action text "fixed/done"; coding falls during the year | `maintenance/work-orders-plant-k-2026.csv` (`failure_code`, `action_text`), `maintenance/failure-codes.csv`; Plant G log has no code column at all |
| 2 | Stale replica of the parts list (refreshed 16 Mar 2025): superseded part numbers, moved bins, no Plant G parts; WOs mention parts not found | `parts/parts-list-shared-drive.csv` vs `parts/erp-parts-2026-12-31.csv`; `maintenance/work-orders-plant-k-2026.csv` (`action_text`, `parts_used`); `vendor/predictiva-proposal.md` (demo on "your parts list") |
| 3 | "Ready" at Plant G = technician finished; at Plant K = production restarted with QA approval; KPI deck compares MTTR across the two | `maintenance/maintenance-log-plant-g-2026.csv` (`סטטוס`/`מוכן ב-`), `production/downtime-events-2026.csv` (event end = restart), `company/kpi-deck-2026-12-extract.md` (footnote) |
| 4 | Sensors on 3 of 40 machines since 1 Oct 2026; gaps; a vibration channel stuck for nine days; one failure (K22, 2 Dec) | `sensors/condition-k21-k23-2026q4.csv`, `assets/asset-register-plant-k.csv` (`condition_monitoring`), `maintenance/work-orders-plant-k-2026.csv` |
| 5 | Three time conventions: ISO local with offset (Plant K CMMS, MES), DD/MM/YYYY local (Plant G log), MM/DD/YYYY UTC (Plant G SCADA) | `scada/alarms-plant-g-2026h2.csv`, `maintenance/maintenance-log-plant-g-2026.csv`, `production/downtime-events-2026.csv` |
| 6 | No common asset register: three names per machine; four Plant G machines numbered differently in MES and the Excel log; moulds not in the CMMS | `assets/*`, `production/downtime-events-2026.csv`, `maintenance/maintenance-log-plant-g-2026.csv` |
| 7 | Most unplanned downtime is moulds, material and waiting, not machine components | `production/downtime-events-2026.csv` (`reason_code`) |
| 8 | Repair durations unmeasurable at Plant K: completion times bunch at shift ends and on Thursday afternoons (planner's bulk close) | `maintenance/work-orders-plant-k-2026.csv` (`completed_at`, `closed_by`) |
| 9 | PM compliance 94% = closed PM WOs; six machines' Q3 PMs bulk-closed on 30 Sep with no labour or parts; more Q4 breakdowns on them | `maintenance/pm-compliance-report-2026.md`, `maintenance/work-orders-plant-k-2026.csv` |
| 10 | Night calls to the maintenance manager; machine waiting while they talk | `maintenance/night-calls-2026.csv` |
| 11 | Shadow AI: technicians' phone chatbot answers pasted into WhatsApp, one wrong hot-runner setting; "see Vladi's notebook" | `maintenance/whatsapp-night-shift-2026-11.md`, `maintenance/work-orders-plant-k-2026.csv` (`action_text`) |
| 12 | Arabic LOTO is rev. B (2019), Russian rev. A (2016); rev. D (2023) added accumulator discharge | `docs/` (`SOP-LOTO-01-*`), `maintenance/shared-drive-listing.csv` |
| 13 | Plant G crane G-CR2 examination overdue (due 11 Oct 2026) | `safety/periodic-examinations-register.csv` |
| 14 | Arava letter: OTIF 81% vs 95%; CAPA by 31 Mar 2027 or second source | `company/arava-letter-2026-12-14.md` |
| 15 | Quality's scrap data almost fully coded; drift before stoppages visible on some machines | `production/scrap-weekly-2026.csv` |
| 16 | Vendor: wind-farm case study; onboarding guide asks 12 months and ≥ 30 failures per mode; camera option; Plant G questionnaire answered "ready" throughout | `vendor/*` |
| 17 | Vladi's notebooks (2004 on): the real failure history | Vladimir persona only (hinted in WO text) |
| 18 | Q3 PM deferral was Dalia's decision for the Arava summer programme | Dalia persona only |
| 19 | Amnon told Predictiva at the conference "we'll be your first plastics reference" | Amnon and Gilad personas only |

## The cast

| Persona | Role | Type | Hidden / unlock |
|---|---|---|---|
| Amnon Shaked | CEO and 64% owner | Owner of the ask | Arava letter is the trigger; promised Predictiva a reference visit; fears losing Arava more than he wants AI. Unlock: "what would make the Arava letter go away?"; asked what was said to the vendor |
| Dalia Mizrahi | VP operations, Plant K manager | Sponsor, your manager | Deferred Q3 PMs on six machines for Arava's summer programme and let them be closed; knows PM 94% is soft. Unlock: non-attribution + "what happened to PMs during the summer programme?" |
| Orit Navon | CFO | CFO | Controls the ₪1.5M line; will fund "infrastructure" only with a measured baseline and a stop rule; has had a bad ERP project. Unlock: show the netting; ask what she would need to release half |
| Vladimir (Vladi) Kaplan | Maintenance manager, Plant K | Middle manager, data steward | Notebooks since 2004; failure-code list "written by a consultant in 2019, nonsense"; gets about two night calls a week; wants to retire in 2028. Unlock: ask how he knows a machine is about to go; respect; ask to see the notebook |
| Nizar Abu-Hussein | Night-shift maintenance technician | Frontline, secret enthusiast | Uses a free chatbot with photos of manual pages; closes WOs at shift end with "תוקן"; read the Arabic LOTO; parts in wrong bins. Unlock: "show me what you did last night with the alarm on K07"; non-attribution |
| Tigist Wondimu | Shift supervisor, production, Plant K | Frontline, receiving team | Keeps the night-call log; operators pick "WAIT_TECH" honestly but restart is recorded at the first QA-approved shot; mould problems coded as machine by maintenance. Unlock: ask how the night goes when a machine stops at 02:00 |
| Eli Peretz | Plant G manager | Second plant, enthusiast | "Ready" at G means the technician finished; filled the vendor's questionnaire "ready" everywhere; G-CR2 inspection slipped in the move. Unlock: same-word test ("when you say ready, what has happened?"); asking about the cranes |
| Khalil Mansour | Works-committee chair (Histadrut) | Union | 2021 local agreement: consultation on technological change, no individual monitoring without agreement; 2025 tablets episode; will support recording if no discipline from it and training in Arabic. Unlock: asked before anything is fixed; ask what workers would need |
| Gilad Har-Even | Account executive, Predictiva | Vendor AE | Case study is wind; onboarding needs 12 months and 30 failures per mode; "learning period" means labelling by customer; camera option; Amnon promised a reference. Unlock: exact data requirements; ask for a plastics reference |

Transcripts leave hidden: Amnon's reference promise; Dalia's PM deferral; Orit's "half the line" condition;
Vladi's notebooks in full; Nizar's phone chatbot; Tigist's restart definition detail; Eli's crane slip;
Khalil's 2021 monitoring clause history; Gilad's 30-failures requirement.

## Timeline

- Data: CMMS and Plant G log 1 Jan – 31 Dec 2026; MES downtime 1 Jan – 31 Dec 2026; sensors 1 Oct – 31 Dec
  2026 (hourly); Plant G alarms 1 Jul – 31 Dec 2026; scrap weekly 2026; night calls 2026; WhatsApp export
  November 2026; parts replica 16 Mar 2025; ERP parts 31 Dec 2026.
- 2025: Jan acquisition of Plant G; Mar parts replica; Aug warehouse reorganisation; Aug G-CR2 examined;
  2025 MES and tablets. 2026: 30 Sep PM bulk close; 1 Oct historian; 11 Oct G-CR2 due; 2 Dec K22 failure;
  14 Dec Arava letter; Dec conference.
- 2027: Thu 7 Jan the ask; Sun 10 Jan 13.1 (Dalia Mon 11 Jan, Amnon Tue 12 Jan); 13–28 Jan 13.2 (Vladi Sun
  17 Jan, night shift Tue 19 Jan, Plant G Wed 20 Jan with G-CR2 escalated that day, Khalil Thu 21 Jan);
  31 Jan – 11 Feb 13.3 (one-page case to Dalia and Orit Thu 11 Feb); 14–25 Feb 13.4 (Gilad Mon 15 Feb,
  Khalil Tue 23 Feb, verdict Thu 25 Feb); 28 Feb – 18 Mar 13.5 (pack v1 approved Wed 3 Mar; audit and eval
  report Thu 18 Mar); Tue 23 Mar management steering (13.6); Wed 31 Mar Arava CAPA due. Six months later:
  September 2027.

## The futures (13.6 debrief)

1. **Buy the platform.** Amnon signs Predictiva in April; kits on 37 machines by July; the "learning
   period" turns out to mean Kinneret labels past failures, which nobody can. From September the platform
   raises 40–60 anomaly alerts a week; technicians stop opening them by October. The camera option is
   switched on at Plant G for "operator behaviour"; the works committee declares a labour dispute; the
   option is switched off. Arava's OTIF stays at 82% (moulds and night waits unchanged); Arava moves
   20% of the 2027 volume to a second source. The 36-month commitment (≈ ₪1.03M for the core offer, more with cameras) stays on the books.
2. **Not yet, foundation funded, manual assistant (the expert path).** Steering approves ₪730k of the
   ₪1.5M. The works committee signs the recording protocol (no individual performance use, training in
   Arabic, Russian and Amharic). By September: common register of 40 machines, auxiliaries and 231
   moulds; breakdown WOs with a failure mode 88% (from 14%); mould shot counters and a mould PM plan;
   live parts view; sensors on 8 critical machines; the assistant used on night shift (night calls to
   Vladi down from about 1.8 to about 0.6 a week; Arabic and Russian LOTO rev. D issued in March); OTIF to
   Arava 92% in Q3 (mould PM and night response, not prediction); G-CR2 examined in January. PdM
   re-decision in January 2028 with a proof-of-concept protocol on Kinneret's own coded data.
3. **Half-way.** The assistant goes live and is liked, but Orit funds only the assistant and the parts
   view ("the rest is bureaucracy"); failure recording stays optional; Vladi retires early in August after
   a health scare and his notebooks go home with him. In January 2028 the re-decision finds the same data
   as in 2027, and Predictiva comes back with the same proposal.

**What decided which future:** whether the foundation was funded and owned as the deliverable, and
whether the works committee agreed the recording protocol before anything changed on the floor.

## Numbers (where each finding is planted)

Computed from the generated files (seed 20270110) with `labs/module-13/discovery.py`,
`labs/module-13/readiness_audit.py` and the pilot's `run_manual.py --mode search` / `score_manual.py`;
reproducible in a spreadsheet. Paths relative to `labs/module-13/data-room/`.

**Volumes.** `maintenance/work-orders-plant-k-2026.csv` 1,475 (BD 861, PM 420, CM 190, INS 4);
`maintenance/maintenance-log-plant-g-2026.csv` 682; `production/downtime-events-2026.csv` 3,992;
`production/scrap-weekly-2026.csv` 2,080; `sensors/condition-k21-k23-2026q4.csv` 6,443;
`scada/alarms-plant-g-2026h2.csv` 2,945; `maintenance/night-calls-2026.csv` 78; parts replica 268, ERP 343;
assets K 53, G 19, MES 40, moulds 231; exam register 10; drive docs 17; pack 22; test set 118.

1. **Labels:** Plant K BD WOs 861: code blank 66.6%, "99" 19.3%, other 14.2%; by month Jan 22% → Dec 5%;
   component code (not blank/99/92) 9.1%; matched to a ProdTrack stop ±15 min 94.5%; usable 73 (8.5%);
   largest code E01 with 12; none ≥ 30. Action text only "fixed/done" 43.4%; notebook/Vladi 3.1%;
   part-not-found 32. Keyword back-coding: K 98.1% classified (38% mould-side), G 99.4% (39%).
2. **Parts replica:** 37 of 268 superseded (13.8%); 0 of 231 active rows with the ERP bin; 38 Plant G
   parts absent. HV-COIL-028: replica B-7-2, ERP K1-D14-02 (the WhatsApp message).
3. **"Ready":** MTTR K (stop→restart) 5.7 h (n = 1,023); G log call→"ready" 3.5 h (n = 379); G
   stop→restart 5.8 h (n = 683); 333 of 379 log repairs matched; restart after "ready" median 51 min.
   Deck: "Plant G repairs 1.6× faster".
4. **Sensors:** 3 of 40; from 1 Oct; outage 19–21 Oct (~60 h per machine missing); K21 vibration 2.38 for
   197 RUN hours (8–17 Nov); K22 above 4.5 mm/s from 22 Nov (9 days before the 2 Dec failure); six machine
   stops on K21–K23 in the window, one a slow degradation.
5. **Clocks:** SCADA 1,804 of 2,945 rows have second field > 12 (month-first), 38.7% ambiguous; HIGH alarms
   matched to a ProdTrack stop ±10 min: 0.5% as local, 100% as UTC; 26.3% of HIGH alarms from the four
   renumbered stations. Sensor file: 3 duplicate local stamps on 25 Oct if the offset is dropped.
6. **Names:** 9 of 26 Plant K machines with a ProdTrack code; hall 3→G05, 5→G03, 9→G12, 12→G09 (serial
   numbers); criticality 0 of 53; moulds with a numeric shot count 19.5%, last service blank 58.4%.
7. **Downtime:** unplanned 11,932 h: mould 5,479 (46%), machine 2,840 (24%), WAIT_TECH 1,538 (13%; 79% at
   night), material 1,051 (9%), other 732, QA hold 292. Night mould stops 229, 3,255 h, mean 14.2 h vs 4.0
   by day. Top 8 machines (K05, G11, K03, G08, G06, G07, G04, K04) = 32.1% of machine-fault hours.
8. **Completion times:** 60.9% of BD WOs completed in the 15 min before a shift change; 13.6% closed by the
   planner on Thursday afternoons; downtime_min blank or 0 64.7%; started_at blank 46.3%.
9. **PM:** reported 96.7% (406/420, deck 97%); with labour 92.4%; 18 PMs bulk-closed 30 Sep (K03, K05, K07,
   K11, K14, K24); machine stops per machine-month Jan–Sep / Oct–Dec: deferred six 1.59 / 3.17, others 1.36
   / 1.18.
10. **Night calls:** 78 (Mar–Dec), 1.8 a week, machine waiting median 42 min, 64 h; solved by phone 59%;
    came in 10. Top topics: unknown controller code 21, cavity closed 14, hot runner 12, Haiwei AL 9.
11. **WhatsApp:** 12 Nov chatbot "300 °C" → burnt heater; HV-COIL-028 bin; "the tablet is in the office".
12. **LOTO:** he rev D (2023) step 6 accumulator; ar rev B (2019) and ru rev A (2016) without it.
13. **Exam:** עגורן 2 (G-CR2) last 2025-08-11, due 2026-10-11, status typed "valid".
14. **Arava:** OTIF 81% vs 95%; 14 of 22 notices "machine breakdown"; two October short-shot 8Ds, night.
15. **Scrap:** 98.2% coded.
16. **Vendor:** core offer US$196,800 + ₪410,600 ≈ ₪1,027,765 over 36 months (₪342.6k a year) at ₪3.136;
    cameras US$36,000 + ₪76,000.

**Pilot (test split, 94: answer 62, route 25, clarify 7; he 26, ar 26, ru 26, en 16).** Real: search over
the drive 23.4% (answers 22/62; he 23.1, ar 15.4, ru 11.5, en 56.2; outdated 3); search over pack 27.7%
(26/62). Track A set (60): drive 21.7%, pack 28.3%. Negative tests: search cannot refuse (0/12).
Illustrative (story): LLM over the drive 71.3%; pack + prompt v1.0 84.0% (55/62, 21/25, 3/7; he 23, ar 21,
ru 21, en 14; failed G2 on R05-ru and G5 on N03, N07); v1.1 87.2% (56/62, 24/25, 2/7; he 24, ar 22, ru 22,
en 14; safety routes 17/17; negative 12/12; ratings 26/30); ≈ 11,500/250 tokens, US$0.026, ₪0.08 a
question (claude-sonnet-5-5 at US$2/10 per million). LLM back-coding of 40 WOs: 31 agree, 6 UNKNOWN.
Case: ₪181 blended per unplanned hour (₪310 × 40% + ₪95 assumed × 60%); B night moulds ≈ 1,420 h ≈ ₪257k;
C six PMs ≈ 400 h ≈ ₪72k; PdM best case 1,420 h ≈ ₪257k vs ₪343k a year; foundation ₪730k (B 130, D 40,
E 45, F 305, G 140, contingency 70).
