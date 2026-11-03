---
id: "13.1"
module: 13
minutes: 16
practice_minutes: 90
prerequisites: ["01.1", "01.2", "01.5", "02.6", "11.1"]
objectives:
  - "Write down what changes when you are the internal lead with a day job — your own data under audit, a CEO-owner who gave the ask, a unionised floor that remembers your last project — and turn each change into a line of the mandate."
  - "Get a mandate from your sponsor with the objective read back, the stated ask recorded as the claim you test, and done defined before anyone looks at the vendor's evidence."
  - "Run the first-day read on Kinneret's files and sort the headline statements into verified, contradicted, claim to test and unverifiable."
  - "Plan a first week that reaches the sponsor, the owner, the night shift and the data before the vendor presents."
volatility: implementation
sources:
  - title: "Organisation of Labour Supervision Law, 5714-1954 (חוק ארגון הפיקוח על העבודה): safety committees, trustees and the safety officer (ss. 10–25), Hebrew Wikisource"
    url: https://he.wikisource.org/wiki/חוק_ארגון_הפיקוח_על_העבודה
  - title: "Kol Zchut, protections from dismissal in collective agreements: the duty to consult workers' representatives in an organised workplace (updated 2 March 2025)"
    url: https://www.kolzchut.org.il/he/הגנות_מפיטורים_בהסכמים_קיבוציים
  - title: "Histadrut, AIG Israel workers' committee declare labour dispute over AI (13 August 2026)"
    url: https://global.histadrut.org.il/news/aig-israel-workers-committee-declare-labour-dispute-over-ai/
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): the advisory boundary, the first-day read"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
last_verified: "2026-11-03"
---

# 13.1 · The call

The owner of the company stood up at the annual management meeting and said "2027 is the year of AI; we start with predictive maintenance; you lead it." You know the plant, the floor knows you, and some of the data you are about to judge is yours. In this lesson you work out what being the internal lead changes, get a mandate from your sponsor that keeps the CEO's idea as a claim to test, read the data room on the first day, and plan the first week. At the end you have a mandate memo, a first-read sheet, an access request, a first-week plan and a short note to the CEO.

## The situation

Sunday 10 January 2027, 07:15, your desk at Plant K. Read the [engagement brief](../../labs/module-13/brief.md) first (in the module download). In short: Kinneret Plastics makes injection-moulded caps, closures and technical parts in two Galilee plants, with about 600 people on three shifts and 40 machines. You are its operations-excellence manager. On Thursday Amnon Shaked, the CEO and 64% owner, said in front of the management team that you will lead "predictive maintenance with AI"; he had seen a vendor, Predictiva, at a conference in December. There is a ₪1.5M "AI and Industry 4.0" line in the 2027 budget that the CFO controls. Arava, the largest technical-parts customer, wrote in December that on-time-in-full delivery was 81% against 95% and wants a corrective-action plan by 31 March. Predictiva presents on 15 February; management decides on 23 March.

You met the three ways in at [01.1](../module-01/lesson-01.md). At Givat Oren ([11.1](../module-11/lesson-01.md)) you were the accidental owner, handed the subject by job title. Here you are the **internal lead with a day job**: you were picked because you are good, you keep your other work, and you are not neutral. IBM's consulting certificate calls the line between what you answer and what you route your *advisory boundary*; inside a factory that line runs through the safety officer and the works committee as much as through finance.

## What to do

### Step 1 — Write down what being the internal lead changes

Fill the entry-role table from [01.1](../module-01/lesson-01.md) before you plan anything:

| | What it means here | What goes into the mandate |
|---|---|---|
| **Who gave the ask** | The owner, publicly, at the annual meeting. Contradicting him in the room costs more than it would cost a consultant | The mandate is your sponsor's (Dalia); the CEO gets a short written note every two weeks |
| **Budget** | None of yours. The ₪1.5M line is the CFO's and the CEO's to release; you can commit nothing above ₪50,000 | "No commitment and no promise to any supplier by the project lead" |
| **Your history** | You designed the MES downtime codes and ran the 2025 tablets project the works committee objected to | Your own data is audited like everyone else's; say so in the memo; someone else re-checks your numbers |
| **The floor knows you** | Access and trust, and old grievances | The works committee is met before any vendor visit; nothing with workers' identifiers leaves the plant |
| **Day job continues** | OEE reporting and the Arava plan | The Arava plan becomes part of the deliverable, not a parallel project |
| **You stay** | Whatever is set up, you or your team will run it | Every part has a named owner who is not you by a date |

The third row is the one internal leads leave out. If the deck's repair-time slide turns out to compare two different definitions, and you built the slide, the credible move is to say so first.

### Step 2 — Get the objective from the sponsor, not the slogan from the owner

The method is [01.2](../module-01/lesson-02.md): the objective in the sponsor's words, read back, then "done". Two objectives exist and the mandate holds both without pretending they are the same:

- **The stated ask** (CEO): "Predictive maintenance with AI, starting with Predictiva on all 40 machines." Record it as *the claim this work tests*.
- **The objective** you propose for Dalia to correct: find out what causes the unplanned downtime that makes Kinneret late to Arava, and test whether predictive maintenance, or something else, would reduce it; bring management one recommendation with costs and dates.

Done must be checkable on 23 March: a decision in the minutes with an owner and a date per part; every number labelled measured, directional or assumed; predictive maintenance judged against criteria written **before** the vendor's presentation (you will write them in [13.4](lesson-04.md), using the readiness bar from [02.6](../module-02/lesson-06.md)); nothing installed and no data sent outside Kinneret; and any safety finding escalated the same day, not held for the readout.

That last line is particular to a factory. Kinneret has more than 50 workers: it has a safety officer, a safety committee and a safety management programme under the Organisation of Labour Supervision Law, 5714-1954 (חוק ארגון הפיקוח על העבודה) and its regulations. Your data work will walk through lockout procedures, cranes and pressure vessels. Write into the mandate who you call when you find something.

### Step 3 — Scope that keeps the cause in view

Use the [scope boundary](../../templates/scope-boundary.md) from [01.3](../module-01/lesson-03.md). Three calls at Kinneret:

- **Both plants or one?** Both. The December deck compares them, the vendor wants to start at Plant G, and the plants record maintenance differently. Scoping out Plant G would hide the most interesting contradiction.
- **Moulds?** In. The ask says "machines", but moulds belong to the tooling department and are where much of the downtime sits. If you scope by asset type you may scope out the cause.
- **Cameras and people analytics?** Out, in writing. The vendor offers them; the local agreement says no monitoring without agreement; the works committee has already written.

### Step 4 — Read the data room on the first day

Follow [01.5](../module-01/lesson-05.md): inventory every file, note where it came from, list what is missing, sort the statements. Open the data room's [INDEX](../../labs/module-13/data-room/INDEX.md). Two facts change how you read the rest: the work orders are Plant K's only (Plant G keeps an Excel log), and ProdTrack, the MES, records stops at both plants from stop to production restart.

A worked example from Kinneret's files:

| Statement | Where | Sort | Why |
|---|---|---|---|
| "Plant G repairs 1.6× faster" (3.5 h against 5.7 h) | `company/kpi-deck-2026-12-extract.md`, slide 4 | **Claim to test** | Footnotes 1 and 2: Plant K from stop to restart, Plant G from call to "ready" |
| "Breakdowns are the number one loss — and they can be predicted" | Same deck, slide 5 | **Claim to test** | Footnote 4: "breakdowns" includes moulds; split them |
| PM compliance 97% | `maintenance/pm-compliance-report-2026.md` | **Claim to test** | Counts closed work orders; "all PMs closed by the end of September" |
| OTIF 81% against 95%; 14 of 22 notices "machine breakdown" | `company/arava-letter-2026-12-14.md` | **Verified** as the customer's view | The reasons are Kinneret's own notices |
| "Plant G data readiness: ready" | `vendor/predictiva-questionnaire-plant-g.md` | **Claim to test** | The same word as the deck: what does "ready" mean at Galil? |
| "Up to 50% less downtime, 94% accuracy, ROI in 9 months" | `vendor/predictiva-proposal.md` | **Claim to test** | The case study is a wind farm |
| Vendor needs 12 months of coded history and ≥ 30 failures per mode | `vendor/predictiva-onboarding-guide-extract.md` | **Verified** as their requirement | Compare with our records in week 2 |
| Failure codes are recorded | `maintenance/failure-codes.csv` | **Unverifiable** today | The list exists; whether it is used needs the profile |
| Condition monitoring on 3 of 26 Plant K machines, 0 of 14 at Plant G | Deck, `assets/asset-register-plant-k.csv` | **Verified** | — |
| No monitoring without the committee's agreement | `hr/local-agreement-2021-extract.md`, clause 15 | **Verified** | The proposal includes cameras |

What is missing goes into the [access request pack](../../templates/access-request-pack.md): the customer-service team's 22 late-shipment notices; Plant G's machine numbering; the supervisors' night-call log; the historian export; tooling's mould list; the ERP stores extract; IT's listing of the maintenance drive; the safety officer's periodic-examination register; HR's languages table.

### Step 5 — Plan a first week that reaches four places

- **The sponsor:** Dalia on Monday, mandate read back and corrected.
- **The owner:** fifteen minutes with Amnon on Tuesday. Not a plan; a question: what does success on 31 March look like to him? Listen for Arava.
- **The floor at night:** most of what you need to know happens between 22:45 and 06:45, when one technician covers 26 machines. Book a night on the floor in week 2.
- **The data and its definitions:** MaintPro, ProdTrack, the historian, Plant G's log; the planner and the shift supervisors who make the records.

And the people who could stop it later: the works committee (before the vendor visit, because clause 14 asks for consultation before new technology that changes work), the safety officer (before you touch procedures), the CFO (before any number becomes a promise). An organised workplace in Israel carries a duty to consult the workers' representatives in good faith, at least before dismissals, even without a clause; the scope beyond that is a question for labour counsel, not for you. In August 2026 the works committee at AIG Israel declared a labour dispute after management moved on AI pilots without agreement: a reminder of what "later" costs.

### Step 6 — Get the mandate, and talk to the owner

Meet Dalia (roleplay: [Dalia Mizrahi](../../labs/module-13/personas/dalia-vp-operations.md); no-roleplay path: [the transcript](../../labs/module-13/personas/transcripts/dalia-vp-operations.md)). What you want: the objective read back and corrected; done and scope agreed; access to both plants; who decides on 23 March. Ask her, in private, what she honestly thinks. Then meet Amnon (roleplay: [Amnon Shaked](../../labs/module-13/personas/amnon-ceo.md); [transcript](../../labs/module-13/personas/transcripts/amnon-ceo.md)): find out what success means to him and exactly what was said to the vendor. Afterwards run each transcript through the [coach prompt](../../labs/common/coach-prompt.md) with the persona's checklist.

> [!TIP]
> To the CEO, "we're evaluating Predictiva properly, on our own data" is true and lets him keep his idea while you test it. "The data isn't ready" on day one is a conclusion you have not earned yet, and he will hear it as an excuse.

## Watch out

- **Answering the owner with a plan for the vendor.** A rollout plan for Predictiva accepts the conclusion before anyone has looked. Give him a date, a format and the question you are answering.
- **Treating your own data as a neutral source.** You built the reason codes and the slide. Say so, and have someone check your numbers.
- **Scoping by asset type.** "Machines" leaves out moulds. Scope by the loss you are trying to explain.
- **Holding a safety finding for the readout.** An overdue examination or a wrong lockout step goes to the safety officer the same day; the readout reports what was done.
- **Meeting the vendor before the works committee.** The committee has written already. A vendor visit to the floor first is the 2025 tablets story again.
- **Sending a plan to the CEO on Sunday.** He gets a note with a date; the sponsor gets the mandate.

## Your turn

### Inputs

- [Engagement brief](../../labs/module-13/brief.md) and the [data room](../../labs/module-13/data-room/INDEX.md) (module download): `company/` (all), `maintenance/pm-compliance-report-2026.md`, `vendor/predictiva-proposal.md`, `vendor/predictiva-questionnaire-plant-g.md`, `vendor/predictiva-onboarding-guide-extract.md`, `hr/local-agreement-2021-extract.md`, `hr/works-committee-letter-2027-01-12.md`.
- Personas: [Dalia Mizrahi](../../labs/module-13/personas/dalia-vp-operations.md) and [Amnon Shaked](../../labs/module-13/personas/amnon-ceo.md), or their [transcripts](../../labs/module-13/personas/transcripts/); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [engagement charter](../../templates/engagement-charter.md) (use it as the mandate memo), [scope boundary](../../templates/scope-boundary.md), [data-room first read](../../templates/data-room-first-read.md), [access request pack](../../templates/access-request-pack.md), [30-60-90 plan](../../templates/30-60-90-plan.md).

### Steps

1. Fill the entry-role table for Kinneret (six rows).
2. Interview Dalia (or read the transcript and mark what the interviewer found and missed). Read the objective back; agree done, scope, access and who decides.
3. Interview Amnon for fifteen minutes (or read the transcript). Find out what success on 31 March means and what was said to the vendor.
4. Write the mandate memo: objective, the stated ask as a claim, done, entry-role table, scope with reasons, advisory boundary with named people, reporting rhythm.
5. Do the first read: every file with its provenance, at least eight statements sorted with evidence, and what is missing.
6. Write the access request, the first-week plan with its risks, and a note to Amnon of at most six lines.

### Time

90 minutes: 15 for the table, 25 for the two interviews, 25 for the mandate, 15 for the first read, 10 for the access request, the plan and the note.

### Done when

- [ ] The objective is the sponsor's, read back, with Arava in it; "predictive maintenance" appears as the claim tested.
- [ ] Done includes criteria written before the vendor's evidence, labelled numbers, owners and dates, and same-day escalation of safety findings.
- [ ] The memo says you commit no money and promise no supplier anything, and that your own data is audited like the rest.
- [ ] The advisory boundary names the safety officer, HR and the works committee, the CFO and counsel for the questions you will not answer.
- [ ] At least eight statements are sorted with evidence, including the MTTR slide, PM compliance and the vendor's claims.
- [ ] The first week reaches the sponsor, the owner, the night shift and the data before 15 February.

<details><summary>Reference answer</summary>

The full expert version is in the module download, `labs/module-13/expert/01-charter-and-first-week.md`. Key parts:

**Objective (Dalia, read back 11 January):** "By 23 March, find out what causes the unplanned downtime that makes Kinneret late to Arava, and test whether predictive maintenance, or something else, would reduce it; bring management one recommendation with costs and dates, *and give Dalia something for the Arava plan by 31 March whatever happens with AI*." (Her correction in italics.)

**Stated ask tested:** "Predictive maintenance with AI, starting with Predictiva's platform on all 40 machines."

**Scope:** unplanned downtime at both plants (machines, moulds, material, waiting), maintenance records, sensors, parts availability, the Arava plan. Out: ERP replacement, new machines, quality systems beyond the scrap data, anything with cameras; revisit after 23 March.

**Advisory boundary:** safety and statutory examinations → Yaakov Dahan; workers' consultation and monitoring → Michal Aharon and the works committee, legal readings to labour counsel; money → Orit Navon; employee personal data → HR; Plant G decisions → Eli Peretz.

**First read (excerpt):** MTTR slide claim to test (two definitions); "breakdowns are the number one loss" claim to test (moulds included); PM 97% claim to test; Arava's 81% verified; Plant G "ready" claim to test; vendor claims to test; vendor requirements verified; failure codes unverifiable until profiled.

**First week:** Sun first read and memo; Mon Dalia; Tue Amnon; Wed exports; Thu quality and customer service, first note to Amnon. Week 2: Vladi, a night shift, Plant G, Khalil informally.

**Note to Amnon:** "Amnon, the work is aimed at what you said on Tuesday: Arava back to 95%. By 23 March you'll have one page: what we do, what it costs, what it gives Arava, with dates. We're evaluating Predictiva properly, on our own data, including at their presentation on 15 February. Nothing is signed or promised to any supplier until that meeting. Next note: 28 January."

**What the transcripts' interviewers missed:** with Dalia, they asked whether she trusts the PM figure instead of what happened to PMs during the summer programme, so her decision to defer six machines' PMs stayed hidden; with Amnon, they asked what the vendor "expects" rather than what he said at the conference, so his offer to be Predictiva's "first plastics reference" stayed hidden.

</details>

## References

- [Organisation of Labour Supervision Law, 5714-1954](https://he.wikisource.org/wiki/חוק_ארגון_הפיקוח_על_העבודה): safety committee, trustees and safety officer (ss. 10–25). Hebrew Wikisource text; check the current version.
- Kol Zchut, [protections from dismissal in collective agreements](https://www.kolzchut.org.il/he/הגנות_מפיטורים_בהסכמים_קיבוציים): the duty to consult workers' representatives in an organised workplace. Its wider scope is for labour counsel.
- Histadrut, [AIG Israel workers' committee declare labour dispute over AI](https://global.histadrut.org.il/news/aig-israel-workers-committee-declare-labour-dispute-over-ai/) (13 August 2026). A union source.
- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting): advisory boundary, first-day read (named, not re-taught).
- Field kit: [01.1 · Three ways in](../module-01/lesson-01.md), [01.2 · Getting a real mandate](../module-01/lesson-02.md), [01.3 · Scope boundary](../module-01/lesson-03.md), [01.5 · The first-day data-room read](../module-01/lesson-05.md), [02.6 · The readiness assessment](../module-02/lesson-06.md).
- Templates: [engagement charter](../../templates/engagement-charter.md), [scope boundary](../../templates/scope-boundary.md), [data-room first read](../../templates/data-room-first-read.md), [access request pack](../../templates/access-request-pack.md), [30-60-90 plan](../../templates/30-60-90-plan.md).
- Next: [13.2 · Discovery](lesson-02.md).
