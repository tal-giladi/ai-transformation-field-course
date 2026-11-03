---
id: "13.2"
module: 13
minutes: 20
practice_minutes: 180
prerequisites: ["13.1", "02.2", "02.4", "02.5", "02.7", "01.6"]
objectives:
  - "Interview the maintenance manager, a night technician, a shift supervisor and the second plant's manager so that the work, the definitions and the hidden tools come out, while protecting the people who speak."
  - "Run the same-word test on a KPI that two plants report, and measure both on one definition."
  - "Profile the maintenance records for a named use: outcomes recorded, completion times, identifiers, clocks, the parts list and the sensors, each with numerator and denominator."
  - "Escalate a safety finding the day you find it, and write a findings memo whose every finding carries a number, a source and a label."
volatility: implementation
sources:
  - title: "Work Safety Ordinance [New Version], 5730-1970 (פקודת הבטיחות בעבודה), s. 81 (lifting machines: thorough examination by a qualified examiner at least every fourteen months), Hebrew Wikisource"
    url: https://he.wikisource.org/wiki/פקודת_הבטיחות_בעבודה
  - title: "Organisation of Labour Supervision (Provision of Information and Training to Workers) Regulations, 5759-1999, regs 2 and 7(b), Hebrew Wikisource"
    url: https://he.wikisource.org/wiki/תקנות_ארגון_הפיקוח_על_העבודה_(מסירת_מידע_והדרכת_עובדים)
  - title: "law.co.il (Haim Ravia), Monitoring employees' email severely restricted — Isakov Inbar, National Labour Court, 8 February 2011"
    url: https://www.law.co.il/en/articles/2011/04/25/monitoring-employees-email-severely-restricted/
last_verified: "2026-11-03"
---

# 13.2 · Discovery

The CEO thinks machines break without warning and a platform will warn him. Your sponsor wants to know why Kinneret is late to Arava. Only the second question can be answered from the work and the records. In this lesson you sit with the maintenance manager, spend a night on the floor with a technician and a shift supervisor, visit the second plant, and profile two plants' maintenance records the way [02.5](../module-02/lesson-05.md) taught you: for a named use. At the end you have a findings memo with evidence labels, and one safety item already escalated.

## The situation

Weeks 2 and 3, 13–28 January 2027. Dalia has given you access to MaintPro, ProdTrack, the drive and the historian; Eli Peretz expects you at Plant G on Wednesday 20 January. You have the exports in the data room (module download, [INDEX](../../labs/module-13/data-room/INDEX.md)). Lina keeps the OEE reports going so you can be on the floor.

This is [02.2](../module-02/lesson-02.md) to [02.7](../module-02/lesson-07.md) in a factory with two plants. Two things are different from Harbor & Pine. First, the use you profile for is specific and demanding: a predictive model needs **outcome labels** (what failed, when, on which asset), not just activity. Second, much of what matters happens at night, in Arabic and Russian, between people who don't write it down.

## What to do

### Step 1 — Interview in the order the work happens

Use the [interview guide](../../templates/interview-guide.md) and the [stakeholder map](../../templates/stakeholder-map.md). Start with the maintenance manager, then the night, then the second plant:

- **Vladimir Kaplan, maintenance manager** (roleplay: [Vladi](../../labs/module-13/personas/vladimir-maintenance-manager.md); [transcript](../../labs/module-13/personas/transcripts/vladimir-maintenance-manager.md)). Ask about last week's breakdowns, not about AI. Find out why the failure codes are not used, where the real failure history lives, what the night shift needs, and what happens when he is away.
- **Nizar Abu-Hussein, night technician** ([persona](../../labs/module-13/personas/nizar-technician.md); [transcript](../../labs/module-13/personas/transcripts/nizar-technician.md)) and **Tigist Wondimu, shift supervisor** ([persona](../../labs/module-13/personas/tigist-shift-supervisor.md); [transcript](../../labs/module-13/personas/transcripts/tigist-shift-supervisor.md)), on the night of 19 January. Ask Nizar to show you the last alarm he handled, step by step, and which procedure and language he used. Ask Tigist how a stop is recorded, who chooses the reason, when the stop "ends", and who approves the first parts at night.
- **Eli Peretz, Plant G manager** ([persona](../../labs/module-13/personas/eli-plant-g-manager.md); [transcript](../../labs/module-13/personas/transcripts/eli-plant-g-manager.md)). Run the same-word test on "ready" (Step 3) and ask how the log, the SCADA and ProdTrack name the same machine. Walk the floor.
- **Khalil Mansour, works committee** ([persona](../../labs/module-13/personas/khalil-works-committee.md)): a short, informal coffee on 21 January to say when the formal meeting will be and that nothing is decided. The real conversation is in [13.4](lesson-04.md).

Protect people. Nizar will only tell you how he reads English manuals at 02:00 if he believes it will not come back to him; the *Isakov* judgment's principles (a legitimate purpose, disclosed in advance, proportionate) are the right instinct for your own notes too: record what is done, not who did it. Afterwards, run each transcript through the [coach prompt](../../labs/common/coach-prompt.md).

### Step 2 — Split the loss before you explain it

The deck says "breakdowns are the number one loss — and they can be predicted", with machine and mould stops added together (footnote 4). Split them in `production/downtime-events-2026.csv`: unplanned stops are everything except `PM`, `SETUP` and `NO_ORDER`; sum `duration_min` by `reason_code` and plant.

| Reason (both plants, 2026) | Hours | Share |
|---|---|---|
| MOULD | 5,479 | 46% |
| MECH + ELEC + HYD (machine faults) | 2,840 | 24% |
| WAIT_TECH | 1,538 | 13% |
| MAT (material, dryers) | 1,051 | 9% |
| OTHER and QA_HOLD | 1,024 | 9% |
| **Total** | **11,932** | |

Then split by shift: mould stops last on average 14.2 hours when they start at night and 4.0 hours by day. Tigist explains why: tooling works from 07:30, Sunday to Thursday. Label this **measured** for the hours and **directional** for the split, because the reason is the operator's choice at the terminal (and WAIT_TECH hides the real cause).

### Step 3 — The same-word test on "ready"

Slide 4 says Plant G repairs 1.6 times faster (3.5 h against 5.7 h). Read the footnotes, then ask Eli what has happened on the machine at the moment someone writes "ready" (מוכן). At Galil: the technician has handed the machine back. At Plant K the stop ends when production has restarted with approved parts. Measure both plants on one definition:

1. Build the crosswalk from Plant G's hall numbers to ProdTrack machines on **serial numbers** (`assets/asset-list-plant-g.csv` against `assets/mes-machines.csv`). Four hall numbers are not the ProdTrack number since the 2025 rearrangement: 3→G05, 5→G03, 9→G12, 12→G09.
2. For each repair in the log with a "ready" time, find the ProdTrack stop on the same machine that started within 30 minutes of the call: 333 of 379 match.
3. Compare: restart came a median **51 minutes** after "ready", every time. On ProdTrack's definition, Plant G's MTTR is **5.8 h**, Plant K's 5.7 h.

Galil is not faster; the word means something else. Show Eli before anyone else sees it. You built that slide; say so in the memo.

### Step 4 — Profile the maintenance records for the use "train a failure-prediction model"

Use the [data profile](../../templates/data-profile.md) from [02.5](../module-02/lesson-05.md). The use needs, per breakdown: the asset, what failed (the failure mode), when it stopped and restarted, and what was done. From `maintenance/work-orders-plant-k-2026.csv`, breakdown work orders (`wo_type` = BD):

| Field the use needs | Measure | Result | Label |
|---|---|---|---|
| What failed | `failure_code` blank / "99 – other" / another code | 66.6% / 19.3% / 14.2% of 861 | M |
| What was done | `action_text` only "fixed/done" (תוקן, בוצע, done, ok, تم, сделано…) | 43.4% | M |
| When it was fixed | `completed_at` in the 15 minutes before a shift change; closed by the planner on Thursday afternoons | 60.9%; 13.6% | M |
| How long it stopped | `downtime_min` blank or 0 | 64.7% | M |
| Which asset | Plant K machines carrying a ProdTrack code in the register | 9 of 26 | M |

Coding fell during the year (22% of January's breakdowns coded, 5% of December's). Plant G's log has no code column at all. Vladi's view of the code list ("pump — pump what?") is the same point ISO 14224 makes in [13.4](lesson-04.md): a component is not a failure mode.

Three more profiles, each for the use it would serve:

- **Sensors** (`sensors/condition-k21-k23-2026q4.csv`): 3 of 40 machines, from 1 October; about 60 hours missing per machine (an outage on 19–21 October); K21's vibration channel shows the same value, 2.38, for 197 running hours (stuck). K22's pump bearing failed on 2 December; its weekly vibration rose from 2.1 to 5.2 mm/s in the three weeks before.
- **Clocks.** Plant K files carry local time with the offset (`+02:00`, `+03:00`). Plant G's log is day-first local time; its SCADA export is month-first **in UTC** (open it: the first alarm of July is stamped `06/30/2026 21:35`). Write down each convention before you join anything.
- **Parts** (`parts/parts-list-shared-drive.csv` against `parts/erp-parts-2026-12-31.csv`): the drive copy was last saved on 16 March 2025; 37 of its 268 part numbers are superseded, no bin location matches the ERP (the warehouse was relabelled in August 2025), and Plant G's 38 parts are missing. 32 work orders say a part was not where the list said. The vendor's "₪310,000 excess stock" demo used this file (`vendor/email-thread-2026-12.md`).

### Step 5 — Check the figures you will be asked to defend

- **PM compliance 97%** counts closed work orders. 18 PMs on six machines (K03, K05, K07, K11, K14, K24) for July to September were closed by the planner on 30 September with no labour and no parts. Counting only PMs with labour recorded: 92.4%. Those six machines had 1.59 machine stops a month each before October and 3.17 after; the other twenty, 1.36 and 1.18. Ask Dalia privately what happened in the summer, and protect the planner: she closed what she was told to close.
- **Night calls** (`maintenance/night-calls-2026.csv`, Tigist's log): 78 calls to the maintenance manager from March to December, about 1.8 a week; the machine waited a median 42 minutes; 59% were solved by phone. Topics: unknown controller codes, hot runners, whether a mould may run with a cavity closed, parts.
- **Quality's scrap** (`production/scrap-weekly-2026.csv`): 98.2% of scrap carries a defect code. The best-coded outcome data in the company is in quality, not maintenance.

### Step 6 — Find the AI and the documents people actually use

Run the [shadow-AI census](../module-01/lesson-06.md) as questions about the work, not about AI. Nizar's "there are ways" and the WhatsApp extract (`maintenance/whatsapp-night-shift-2026-11.md`) show the same thing: technicians photograph English manual pages and ask a free chatbot on their phones; on 12 November one answer ("raise the tip to 300 °C for ten minutes") was followed and burnt a hot-runner heater. Record it as a fact about missing support, not as misconduct.

Then compare the procedures on the drive (`maintenance/shared-drive-listing.csv`, `docs/`). The Hebrew lockout procedure is revision D (2023) and includes step 6: discharge the hydraulic accumulator and verify 0 bar before opening the guard. The Arabic translation is revision B (2019) and the Russian revision A (2016); neither has the step. Nizar follows the Arabic one.

### Step 7 — Escalate safety the same day

Two items do not wait for the memo:

- **The lockout translations.** The regulations on information and training to workers require up-to-date instructions for the safe use and maintenance of equipment, and the written risk summary in Hebrew and in a language the worker understands. Tell the safety officer, Yaakov Dahan, the day you see it; it is his to act on.
- **The crane.** In `safety/periodic-examinations-register.csv`, Plant G's crane 2 (mould changes) was last examined on 11 August 2025 and was due on 11 October 2026; its status is typed "valid". The Work Safety Ordinance requires a lifting machine to be thoroughly examined by a qualified examiner at least once every fourteen months (s. 81). Tell Eli and Yaakov in person on 20 January. You are not the examiner; you do not decide whether the crane is safe.

Your memo reports what they did.

**Track B (Python).** `discovery.py` (module download) computes every number in Steps 2–5 from the exports, including the serial-number crosswalk and the "ready"-to-restart join, which are tedious in a spreadsheet and need re-running every month once the foundation starts:

```bash
python discovery.py              # everything
python discovery.py mttr pm      # one or more sections
```

## Watch out

- **Asking about AI instead of the work.** "Would predictive maintenance help?" gets opinions. "Show me the last alarm you handled" gets the manual photos, the Arabic procedure and the parts list.
- **Quoting one plant's KPI against another's** without asking what the word means in each. Same word, different event.
- **Joining on time before you know the clocks.** Read as local time, Plant G's alarms match almost no stops; read as UTC, they match nearly all.
- **Reading free text as a label.** "Pump noisy" tells you the component, not the failure mode or the cause.
- **Naming people.** The planner's bulk close, Nizar's phone, the supervisor's quick first-article checks are facts about the system. Write them without names.
- **Sitting on a safety item** until the memo is ready.

## Your turn

### Inputs

- The [data room](../../labs/module-13/data-room/INDEX.md) (module download): `production/`, `maintenance/`, `assets/`, `sensors/`, `scada/`, `parts/`, `docs/`, `safety/`, `vendor/predictiva-questionnaire-plant-g.md`, `vendor/email-thread-2026-12.md`.
- Personas: [Vladimir Kaplan](../../labs/module-13/personas/vladimir-maintenance-manager.md), [Nizar Abu-Hussein](../../labs/module-13/personas/nizar-technician.md), [Tigist Wondimu](../../labs/module-13/personas/tigist-shift-supervisor.md), [Eli Peretz](../../labs/module-13/personas/eli-plant-g-manager.md), or their [transcripts](../../labs/module-13/personas/transcripts/); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [interview guide](../../templates/interview-guide.md), [stakeholder map](../../templates/stakeholder-map.md), [data profile](../../templates/data-profile.md), [shadow-AI survey](../../templates/shadow-ai-survey.md), [findings memo](../../templates/findings-memo.md).

### Steps

1. Interview at least three of Vladi, Nizar, Tigist and Eli (or read the transcripts and mark what each interviewer found and missed).
2. Split unplanned downtime by reason and by shift (Track A: a pivot on `reason_code` × `plant`, then on `shift` for MOULD).
3. Run the same-word test on "ready" and measure both plants on one definition.
4. Profile the breakdown work orders, the sensors, the clocks and the parts list for the use "train a failure-prediction model".
5. Check PM compliance and the night calls; read the WhatsApp extract and the procedures on the drive.
6. Write down, with times, what you escalated and to whom.
7. Write the findings memo: the answer first, at least ten findings, each with a number, a source and a label.

**Track B (Python)**: run `python discovery.py` in `labs/module-13/` and check three of its numbers by hand in a spreadsheet.

### Time

180 minutes: 60 for the interviews, 70 for the measures, 50 for the memo.

### Done when

- [ ] Downtime is split into moulds, machine faults, waiting and material, with hours and the night effect.
- [ ] Both plants' MTTR is shown on one definition, with the crosswalk method stated.
- [ ] The failure-code profile has numerators and denominators, and says what the use needs that the data lacks.
- [ ] The clocks, the parts list and the sensors are each profiled with one number that matters.
- [ ] The lockout translations and the crane were escalated the day you found them, and the memo says what was done.
- [ ] No technician, planner or supervisor is named in a way that blames them.

<details><summary>Reference answer</summary>

The full memo is `labs/module-13/expert/02-findings-memo.md` (module download). Its first lines:

**The answer first.** Kinneret does not mainly lose time because machines fail without warning. It loses it because stops last too long — above all mould stops at night — and nobody records what failed. Predictive maintenance needs exactly the records we do not keep, and would watch the quarter of downtime that is machine faults, not the half that is moulds.

**Escalated the same day:** crane 2 at Plant G, examination overdue since 11 October 2026, tagged out on 20 January, examiner booked for 25 January; Arabic (rev. B) and Russian (rev. A) lockout procedures removed from the drive on 21 January and night technicians briefed by the safety officer.

**Findings (numbers):** moulds 46% of 11,932 unplanned hours, machine faults 24% (M; split D); night mould stops mean 14.2 h against 4.0 h by day (M); breakdown WOs coded 14.2%, "fixed/done" only 43.4%, 60.9% completed just before a shift change (M); Plant G "ready" a median 51 minutes before restart, MTTR 5.8 h on ProdTrack's definition against 5.7 h at Plant K (M); 9 of 26 Plant K machines with a ProdTrack code, four Plant G hall numbers ≠ ProdTrack (M); sensors on 3 of 40 machines from 1 October, one stuck channel, K22's rise visible three weeks before its failure (M); PM 92.4% with labour against 96.7% reported, six machines' Q3 PMs bulk-closed and their stops doubling in Q4 (M; reason R); drive parts list: 37 of 268 numbers superseded, no bin matching, the vendor's demo built on it (M); 78 night calls, median 42 minutes waiting (M); phone chatbots and a burnt heater (M, R); scrap 98.2% coded (M); Arava's late notices are our own words (M).

**What the transcripts' interviewers missed:** Vladi was asked where to find the failure history and answered "ask me" — nobody asked how he knows a machine is about to fail, so the eleven notebooks stayed hidden; Nizar said "there are ways" and nobody followed it, so the phone chatbot stayed hidden (the WhatsApp extract shows it); nobody asked Nizar whether he knew the Arabic lockout was older than the Hebrew; Tigist was not asked who approves first parts at night, which links the night shift to Arava's short-shot complaints; Eli was not asked about the cranes or about what was sent to the vendor.

</details>

## References

- [Work Safety Ordinance [New Version], 5730-1970](https://he.wikisource.org/wiki/פקודת_הבטיחות_בעבודה), s. 81: lifting machines examined by a qualified examiner at least every fourteen months. Hebrew Wikisource; the safety officer owns the reading.
- [Organisation of Labour Supervision (Provision of Information and Training to Workers) Regulations, 5759-1999](https://he.wikisource.org/wiki/תקנות_ארגון_הפיקוח_על_העבודה_(מסירת_מידע_והדרכת_עובדים)), regs 2 and 7(b).
- law.co.il, [*Isakov Inbar*](https://www.law.co.il/en/articles/2011/04/25/monitoring-employees-email-severely-restricted/) (National Labour Court, 2011): workplace monitoring principles; used here for how you record what people tell you.
- Field kit: [01.6 · The shadow-AI census](../module-01/lesson-06.md), [02.2 · The discovery interview](../module-02/lesson-02.md), [02.4 · Measuring a baseline from exports](../module-02/lesson-04.md), [02.5 · Profiling the data](../module-02/lesson-05.md), [02.7 · Writing a findings memo people believe](../module-02/lesson-07.md).
- Templates: [interview guide](../../templates/interview-guide.md), [stakeholder map](../../templates/stakeholder-map.md), [data profile](../../templates/data-profile.md), [shadow-AI survey](../../templates/shadow-ai-survey.md), [findings memo](../../templates/findings-memo.md).
- Simulation (practise the same interview moves on Harbor & Pine):

[Simulation: Discovery interview](../../simulations/discovery-interview/index.html?preset=harbor)

- Next: [13.3 · Diagnosis](lesson-03.md).
