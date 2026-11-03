---
id: "13.4"
module: 13
minutes: 22
practice_minutes: 150
prerequisites: ["13.3", "02.6", "04.6", "04.8", "06.5"]
objectives:
  - "Write the bar for 'ready for predictive maintenance' before the vendor presents, and grade the evidence against it as verified, reported or contradicted."
  - "Turn a 'not yet' into a funded foundation: each gap with an owner, a cost, a date and the evidence that will show it is closed, plus the date and criteria for the re-decision."
  - "Read a vendor's claims back with their conditions, and say what would make the product worth buying."
  - "Design the foundation around a unionised, multilingual front line: consultation before change, no individual monitoring, safety instructions in a language workers understand."
volatility: implementation
sources:
  - title: "ISO 14224:2016, Petroleum, petrochemical and natural gas industries — Collection and exchange of reliability and maintenance data for equipment (Wikipedia summary; the ISO page blocks automated access)"
    url: https://en.wikipedia.org/wiki/ISO_14224
  - title: "Organisation of Labour Supervision (Provision of Information and Training to Workers) Regulations, 5759-1999, regs 2, 6, 7(b), 8, Hebrew Wikisource"
    url: https://he.wikisource.org/wiki/תקנות_ארגון_הפיקוח_על_העבודה_(מסירת_מידע_והדרכת_עובדים)
  - title: "Organisation of Labour Supervision (Safety Management Programme) Regulations, 5773-2013, regs 1, 5(6), 5(10), Hebrew Wikisource"
    url: https://he.wikisource.org/wiki/תקנות_ארגון_הפיקוח_על_העבודה_(תכנית_לניהול_הבטיחות)
  - title: "Work Safety Ordinance [New Version], 5730-1970, ss. 81, 115, 119א, Hebrew Wikisource"
    url: https://he.wikisource.org/wiki/פקודת_הבטיחות_בעבודה
  - title: "Globes, the Privacy Protection Authority's guidance on surveillance cameras in the workplace (18 October 2017)"
    url: https://www.globes.co.il/news/article.aspx?did=1001208219
  - title: "law.co.il (Haim Ravia), Monitoring employees' email severely restricted — Isakov Inbar, National Labour Court, 8 February 2011"
    url: https://www.law.co.il/en/articles/2011/04/25/monitoring-employees-email-severely-restricted/
  - title: "Kol Zchut, protections from dismissal in collective agreements: duty to consult workers' representatives (updated 2 March 2025)"
    url: https://www.kolzchut.org.il/he/הגנות_מפיטורים_בהסכמים_קיבוציים
  - title: "Histadrut, AIG Israel workers' committee declare labour dispute over AI (13 August 2026)"
    url: https://global.histadrut.org.il/news/aig-israel-workers-committee-declare-labour-dispute-over-ai/
last_verified: "2026-11-03"
---

# 13.4 · The hard part: not yet, and fund the foundation

Every engagement has one thing that makes it hard. At Kinneret it is saying "not yet" to the owner's idea and getting the money spent on something less exciting instead: a register, a way of recording failures that technicians will actually use, sensors on a few machines, a parts list that is true. The people whose work changes speak four languages, are represented by a works committee that has already written to management, and remember your last project. In this lesson you write the readiness bar before the vendor presents, read the vendor's claims back, grade the evidence, turn "not yet" into a funded foundation with gates, and design it with the front line rather than at it. At the end you have the verdict and foundation paper for 25 February and a draft protocol with the works committee.

## The situation

Sunday 14 to Thursday 25 February 2027. Orit read your case over the weekend and wrote "good — now show me the vendor is really not ready to use, not just not ready to sell". Predictiva presents to management on Monday 15 February at 10:00; you meet Gilad Har-Even afterwards. Khalil Mansour, the works-committee chair, has a meeting with you and Michal Aharon (HR) on Tuesday 23 February. Amnon has told Dalia he is "open, but I want to hear why not".

You have run a readiness assessment once, at Harbor & Pine ([02.6](../module-02/lesson-06.md)). Here it carries the decision: the readiness verdict **is** the deliverable. IBM's readiness course separates what is reported from what is verified and warns about the over-claimed report; you will meet both, from the vendor and from the second plant.

## What to do

### Step 1 — Write the bar on Sunday, before the presentation

Use the [readiness assessment](../../templates/readiness-assessment.md) template. Name the use ("predict machine failures early enough to plan the repair") and write, for the machines it would cover, what must be true. Write it before Monday, so nobody can say you set the bar after seeing the demo.

| # | Criterion | Why |
|---|---|---|
| P1 | One register: every machine, auxiliary and mould has one id, used by MaintPro, ProdTrack, the historian and the alarms | A prediction must land on the right asset |
| P2 | ≥ 12 months of breakdown records with a failure mode on ≥ 80% | The vendor's prerequisite (onboarding guide 3.2) and ours |
| P3 | At least one failure mode with ≥ 30 recorded events on instrumented machines | The vendor's minimum per mode |
| P4 | Time-synchronised sensor data on the target machines for ≥ 6 months, gaps known | 3.3, and our three clocks |
| P5 | The outcome recorded: stop and restart, what failed, what was done | Otherwise no prediction can be checked |
| P6 | A named person with hours to review and label alerts | 3.4: the "learning period" |
| P7 | The works committee has agreed how the records are used | Without it, records are made to protect people, not to inform |
| P8 | The losses it addresses are a large, measured share of downtime | Otherwise it cannot move Arava |

Notice that most of the bar comes from the vendor's own onboarding guide. You are not inventing obstacles; you are reading their prerequisites as written.

### Step 2 — Read the vendor's claims back

Meet Gilad after the presentation (roleplay: [Gilad Har-Even](../../labs/module-13/personas/gilad-predictiva-ae.md); no-roleplay path: [transcript](../../labs/module-13/personas/transcripts/gilad-predictiva-ae.md)). Use the [claim read-back](../../templates/claim-read-back.md) from [04.8](../module-04/lesson-08.md): read each claim back in his words, then ask for its conditions.

| Claim | Ask | What you are listening for |
|---|---|---|
| "94% prediction accuracy" | 94% of what, measured how? What was the false-alarm rate? | Recall on one customer's bearing failures; false alarms "proprietary" |
| "Up to 50% less unplanned downtime" | Which downtime? Moulds? | Machine-mounted sensors only |
| "ROI in 9 months" | At which customer, in which industry? Is there an injection-moulding reference? | A wind farm with six years of coded data; no plastics customer in production |
| "90-day learning period" | What does our side do during it? | Our reliability engineer labels every anomaly — we have none |
| "₪310,000 excess stock" | Which file? | The drive's March 2025 parts list, sent by Plant G |
| "Conference price until 31 March" | What does the discount depend on? | Being a reference site |

Sign nothing, promise no date. The deadline is theirs, not yours.

### Step 3 — Grade the evidence and write the verdict

Grade each criterion with the evidence you already have from 13.2: **verified** (you checked it in the data or saw it), **reported** (someone said so), **contradicted** (the data says otherwise). Kinneret's grading, in short: P1 not met (9 of 26 machines carry their ProdTrack code; moulds have no id; four Plant G hall numbers differ); P2 not met (14.2% of breakdowns coded at Plant K and falling; no code column at Plant G; the Plant G questionnaire's "failure modes coded: yes" is **contradicted**); P3 not met (73 usable labels, largest mode 12 events); P4 not met (3 of 40 machines, three months, a stuck channel, UTC alarms); P5 not met (completion bunched at shift change; "ready" ≠ restart); P6 not met (reported); P7 in progress; P8 not met (machine faults 24% of lost hours, moulds outside the platform).

Write the verdict the way the template asks: **not yet**, the criteria that decide it, what would change it, and when you will look again.

> "Predictive maintenance — not yet. Not 'no': the bar is written; the foundation below meets P1, P2, P4, P5 and P7 by December 2027, and P3 can be tested in January 2028. Re-decision at the January 2028 management meeting, on 12 months of coded breakdowns from the eight instrumented machines, with a vendor proof of concept on Kinneret's own data that reports its false-alarm rate."

Before you write it, sort a similar set of evidence on Harbor & Pine and watch how a steering group reacts to an over-claimed report against an honest one:

[Simulation: Readiness evidence grader](../../simulations/readiness-evidence-grader/index.html?preset=harbor)

### Step 4 — Turn "not yet" into a funded foundation

A "not yet" with nothing funded behind it becomes "never", and the vendor comes back with the same proposal next year. Each unmet criterion becomes a piece of work with an owner, a cost, a date and the evidence that will show it is closed:

| Gap | Work | Owner | By | Cost | Evidence it is closed |
|---|---|---|---|---|---|
| P1 | Common register incl. 231 moulds and statutory items; crosswalk MaintPro–ProdTrack–historian–SCADA; QR labels | Vladimir Kaplan, Shlomi Biton, Fadi Khoury | 30 April | ₪45k | Every stop and work order maps to one id |
| P2, P5 | Recording at the machine on shared tablets, screens in Hebrew, Arabic and Russian, a failure-mode list of about 15 modes written **with** technicians; Plant G onto MaintPro | Vladimir Kaplan; HR for training | K 30 April, G 30 June | ₪260k | ≥ 80% of breakdowns with a mode by 30 September |
| P4 | Thresholds on K21–K23 now; sensors and historian on the eight machines with most machine-fault hours (32% of them) | Vladimir Kaplan, Boaz Tal | 30 September | ₪140k | ≥ 95% of hours complete |
| P6 | A senior technician named as co-owner of the failure list and alert review from June (Vladi retires in 2028) | Vladimir Kaplan | 30 June | Within budget | Named, with hours |
| P7 | Protocol with the works committee (Step 5) | Michal Aharon | 31 March | — | Signed |
| Parts | Live ERP view, drive copy deleted | Avi Malka | 31 March | ₪40k | Spot check of 30 bins |

For the failure-mode list, use ISO 14224 as a reference, not a template. It is written for the petroleum, petrochemical and natural gas industries, and its useful idea is the separation of the equipment, the **failure mode** (what you observed: leaking, no output, abnormal vibration), the **failure mechanism** and the **cause**. Vladi's "pump — pump what?" is exactly that point. A list of fifteen modes that technicians recognise and can choose in Arabic at the machine is worth more than forty codes nobody reads. Notice the irony: ISO 14224 is itself evidence from another industry, which is why you borrow its structure and not its tables.

### Step 5 — Design it with the front line, not at it

Recording at the machine changes technicians' work and creates records with their ids on them. Three constraints shape the design; map them in the [regulatory map](../../templates/regulatory-map.md) with a source, a design rule and an owner each:

- **Consultation before change.** Kinneret's local agreement (clause 14, fictional) asks for written notice and good-faith consultation 30 days before new technology that changes work, and a joint committee on training. Beyond the agreement, an organised workplace carries a duty to consult the workers' representatives in good faith, at least before dismissals, even without a clause; the scope beyond that is for labour counsel. The AIG Israel dispute of August 2026 is what skipping it looks like.
- **No individual monitoring from the records.** Work orders and assistant logs carry technician ids: personal data under the Privacy Protection Law, 5741-1981 (חוק הגנת הפרטיות). Israeli labour case law (*Isakov Inbar*, National Labour Court, 2011) frames workplace monitoring as legitimate only with a disclosed policy, a defined purpose and proportionate means; the Privacy Protection Authority's 2017 guidance on workplace cameras says footage gathered for one purpose may not be used for another, such as discipline. Design rule: records are for maintenance; no per-technician performance reports; no discipline from them; no cameras; assistant logs kept without user id. The notice wording goes to counsel.
- **Safety instructions in a language workers understand.** The regulations on information and training to workers require up-to-date instructions for the safe use and maintenance of equipment (reg. 2), a training log (reg. 6) and the written risk summary in Hebrew and another language the worker understands (reg. 7(b)). The safety management programme regulations ask for a list of procedures with their last update dates (reg. 5(10)) and of items needing periodic tests (reg. 5(6)); the Work Safety Ordinance sets the intervals (lifting machines 14 months, s. 81; air receivers 26 months, s. 115). Design rule: approved Arabic and Russian revisions of the safety procedures before anything uses them; statutory items in the common register with computed due dates. Owner: the safety officer.

Then meet Khalil (roleplay: [Khalil Mansour](../../labs/module-13/personas/khalil-works-committee.md); [transcript](../../labs/module-13/personas/transcripts/khalil-works-committee.md)) before anything is fixed, with Michal present so agreements can be written. Ask what workers would need. Promise only what you can sign; commitments on staffing are management's, through HR. Leave with a written next step: a draft protocol in Hebrew and Arabic.

### Step 6 — Say "not yet" so it can be heard

You will deliver this to the CEO in 13.6. Prepare the sentence now: start from his question ("what will fix Arava?"), give the verdict with its date, and give him what he can do instead this quarter. "The data isn't ready" is an excuse; "here is the bar, here is the date, here is what we fund so we meet it, and here is what fixes Arava now" is a decision.

## Watch out

- **Writing the bar after the demo.** It will look fitted. Date it before.
- **"No" instead of "not yet".** Without criteria and a date, it is a veto, and the owner will go around it.
- **A verdict without money behind it.** Fund the foundation or the same proposal returns next year with the same data.
- **A failure-code list written by a consultant again.** Write it with the technicians who will use it, in their languages, and keep it short.
- **Promising the works committee what you cannot sign.** Commit to how the records are used; route staffing commitments to management and HR.
- **Treating the vendor as the enemy.** Read their claims back with conditions; tell them what would make you buy in 2028.

## Your turn

### Inputs

- Your case from 13.3; the [data room](../../labs/module-13/data-room/INDEX.md) (module download): `vendor/` (all), `hr/` (all), `safety/`, `maintenance/failure-codes.csv`, `maintenance/shared-drive-listing.csv`.
- Personas: [Gilad Har-Even](../../labs/module-13/personas/gilad-predictiva-ae.md), [Khalil Mansour](../../labs/module-13/personas/khalil-works-committee.md), [Eli Peretz](../../labs/module-13/personas/eli-plant-g-manager.md) (for the questionnaire), or their [transcripts](../../labs/module-13/personas/transcripts/); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [readiness assessment](../../templates/readiness-assessment.md), [claim read-back](../../templates/claim-read-back.md), [regulatory map](../../templates/regulatory-map.md), [risk register](../../templates/risk-register.md), [comms plan](../../templates/comms-plan.md).

### Steps

1. Write the bar (at least six criteria) with today's date, before you read the vendor's case study.
2. Interview Gilad (or read the transcript); fill the claim read-back for at least five claims.
3. Grade every criterion as verified, reported or contradicted, with the evidence.
4. Write the verdict: not yet / phase / proceed, the deciding criteria, what would change it, the re-decision date.
5. Write the foundation plan: each gap with work, owner, date, cost and closing evidence; a stop rule.
6. Build the constraints map (consultation, privacy and monitoring, safety and language), each with source, design rule and owner.
7. Meet Khalil (or read the transcript) and draft the protocol in five or six points.

### Time

150 minutes: 20 for the bar, 30 for the vendor, 25 for grading and verdict, 30 for the foundation plan, 25 for the constraints, 20 for the works committee.

### Done when

- [ ] The bar is dated before the vendor's presentation and most of it can be traced to the vendor's own prerequisites.
- [ ] Every criterion is graded with evidence; the Plant G questionnaire is marked contradicted where the data says so.
- [ ] The verdict is "not yet" with criteria, a date and what would change it — not "no".
- [ ] Every gap has an owner, a cost, a date and closing evidence; there is a stop rule.
- [ ] The constraints map says who owns each legal reading (safety officer, HR, counsel), and you gave no legal opinion.
- [ ] The protocol says how records are and are not used, and the works committee saw it before anything changed on the floor.

<details><summary>Reference answer</summary>

The full paper is `labs/module-13/expert/04-readiness-verdict-and-foundation.md` (module download).

**Verdict:** "Predictive maintenance — not yet. P1–P6 and P8 not met (verified); P7 in progress. Re-decision January 2028 on 12 months of coded breakdowns from the eight instrumented machines and a proof of concept on Kinneret's own data reporting its false-alarm rate."

**Vendor read-back (excerpt):** 94% = recall on NordVind's bearing failures, false alarms not shared; 50% = machine faults only, 24% of our lost hours; no injection-moulding customer in production; the learning period needs a reliability engineer to label every alert (data-readiness service US$40,000); the ₪310,000 parts figure was computed on the March 2025 drive list; the conference price depends on Kinneret being a reference site.

**Foundation:** ₪730k in three stages (register ₪45k; recording ₪260k; parts ₪40k; night mould response ₪130k; sensors ₪140k; assistant ₪45k; contingency ₪70k); stop rule: under half of breakdowns coded on 30 June.

**Protocol (draft sent 25 February in Hebrew and Arabic):** records for maintenance and reliability only, no individual performance reports, no discipline from them; no cameras or tracking; recording in Hebrew, Arabic and Russian; paid training in the worker's language; the joint committee meets before each stage; a committee-named technician in the assistant's test group; no staffing change from this project in 2027; review after six months.

**What the transcripts' interviewers missed:** with Gilad, they asked what the platform needs but not how many failures per mode, so the 30-per-mode minimum came only from the onboarding guide; they never asked for a plastics reference, nor what the discount depends on (Amnon's reference promise). With Khalil, they asked what workers need but not what workers heard or fear most, so the Plant G camera visit — the single change that would remove half the opposition if dropped in writing — stayed implicit.

</details>

## References

- [ISO 14224](https://en.wikipedia.org/wiki/ISO_14224) (2016 edition, petroleum, petrochemical and natural gas industries): collection and exchange of reliability and maintenance data. Summary page; the ISO catalogue page blocked automated access and should be checked by hand.
- [Organisation of Labour Supervision (Provision of Information and Training to Workers) Regulations, 5759-1999](https://he.wikisource.org/wiki/תקנות_ארגון_הפיקוח_על_העבודה_(מסירת_מידע_והדרכת_עובדים)); [Safety Management Programme Regulations, 5773-2013](https://he.wikisource.org/wiki/תקנות_ארגון_הפיקוח_על_העבודה_(תכנית_לניהול_הבטיחות)); [Work Safety Ordinance [New Version], 5730-1970](https://he.wikisource.org/wiki/פקודת_הבטיחות_בעבודה). Hebrew Wikisource texts; the safety officer owns the reading.
- Privacy Protection Authority guidance on workplace cameras, as reported by [Globes](https://www.globes.co.il/news/article.aspx?did=1001208219) (18 October 2017); [*Isakov Inbar*](https://www.law.co.il/en/articles/2011/04/25/monitoring-employees-email-severely-restricted/) (National Labour Court, 2011). Route questions on notice and lawful basis to counsel or the DPO.
- Kol Zchut, [duty to consult workers' representatives](https://www.kolzchut.org.il/he/הגנות_מפיטורים_בהסכמים_קיבוציים); Histadrut, [AIG Israel labour dispute over AI](https://global.histadrut.org.il/news/aig-israel-workers-committee-declare-labour-dispute-over-ai/) (13 August 2026).
- The EU AI Act does not reach these uses: Kinneret operates machines in Israel and sells parts, not AI systems, to EU customers. Revisit if a customer asks.
- Field kit: [02.6 · The readiness assessment as a deliverable](../module-02/lesson-06.md), [04.6 · Which law applies to you](../module-04/lesson-06.md), [04.8 · Vendor and claim due diligence](../module-04/lesson-08.md), [06.5 · The comms pack](../module-06/lesson-05.md).
- Templates: [readiness assessment](../../templates/readiness-assessment.md), [claim read-back](../../templates/claim-read-back.md), [regulatory map](../../templates/regulatory-map.md), [risk register](../../templates/risk-register.md), [comms plan](../../templates/comms-plan.md).
- Next: [13.5 · Build: the readiness audit and a manual assistant](lesson-05.md).
