---
id: "07.2"
module: 7
minutes: 20
practice_minutes: 120
prerequisites: ["07.1", "05.7", "05.1"]
objectives:
  - "Read a pilot's gate per segment (channel, language, category) and decide scale, fix or stop for each segment, with the evidence label behind each verdict."
  - "Write a decision record that states the options, the money released and held, the conditions of the next gate, who can stop it, what would change the decision, and any departure from the pre-agreed gate rule."
  - "Apply 'fund nothing new this cycle' to a queue of requests, and merge a duplicate build at the level where it can be merged now."
  - "Decommission a 'retire' completely: access, data, contract, records, and a check that the benefit landed and the old path is gone."
volatility: concept
sources:
  - title: "IBM Lead AI Transformation: Strategy, Governance & Execution Professional Certificate (Coursera) — course 6, Measure AI Value and Scaling Transformation (pilot isn't scale; non-compensable gates vs readiness factors; scale / sustain / retire)"
    url: https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera) — course 4, Design AI Transformation Roadmaps; course 5, AI Business Cases and ROI Models (staged gates)"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
last_verified: "2026-11-02"
---

# 07.2 · Scale, fix or stop

A gate is where a pilot either earns its next stage of money or stops pretending. In this lesson you run Harbor & Pine's gate 1 on 1 April 2027: read the eight weeks of production evidence segment by segment, decide scale, fix or stop for each part of the pilot, write the decision record the committee signs, keep every new request out of this cycle's money, merge a duplicate build that turned up in March, and decommission the translation service the pilot replaces. At the end you have a decision record, a re-gate with dates, and a decommissioning checklist with every line closed or owned.

## The situation

This lesson jumps forward. It is Thursday 1 April 2027, gate 1. The steering meeting of 19 January ([07.4](lesson-04.md)) approved phase 1 with ₪48,000 now and ₪72,000 at this gate if all four conditions are met; the board confirmed it on 28 January. Phase 1 ran from 1 February ([07.8](lesson-08.md) follows it week by week), and on 15 March a draft promised a refund outside policy and disclosed another customer's address ([07.5](lesson-05.md) runs that incident). You will go back to January and March in the next lessons; here you use what they produced.

The committee meets at 10:00: Yoav (chair), Ronit, Michal, Samir, Avi and you. Stage 1 spent ₪46,800 of its ₪48,000. On your desk: the pilot log's gate readings, the usage export from the admin console, the incident log, the champions' issues log from module 6 ([06.3](../module-06/lesson-03.md)), and the intake register as it stood on 31 March. Three requests for new money are also on the agenda, and Ronit has asked when the translation contract actually stops costing money.

IBM's leadership course says a pilot is not scale, separates gates that cannot be traded against anything (law, safety, minimum performance, an owner, monitoring) from readiness factors, and gives three verdicts: scale, sustain, retire. Its consulting course adds staged money against yes/no gates. Both stop at the verdict. Here you read the evidence, write the record and do the decommissioning.

## What to do

### Step 1 — Read the gate as written, one segment at a time

Read the four conditions exactly as the charter and ROI model wrote them in December ([05.1](../module-05/lesson-01.md), [03.7](../module-03/lesson-07.md)), on the measurement period they set (15 February – 28 March, after two learning weeks). Then split every number by the segments that behave differently: here, channel (email and web form; WhatsApp) and language. A pilot-wide average hides exactly the part that fails.

From `labs/module-07/gate-1-readings.csv`, `gate-1-weekly.csv` and `gate-1-other-readings.csv` (module download; the pilot log is the course story's, synthetic):

| Gate 1 condition | Email + web form | WhatsApp | All channels | Label |
|---|---|---|---|---|
| (a) ≥ 80% of drafts accepted, ≥ 70% in each language | **82.5%**; he 85.9, en 83.6, ru 81.1, ar 73.9 | **58.3%**; he 61.9, en 70.0 (n = 20), ru 56.8, ar 51.0 | **72.9%**; ar 63.3 | measured (agent marks on 2,092 drafts) |
| (b) median review ≤ 2.5 minutes | 2.0–2.5 min by language | 1.3–1.6 min | 1.8 min | measured (timer) |
| (c) wrong replies reaching customers ≤ today | spot audit: 9 of 480 sent drafted replies = 1.9%, against 9 of 300 = 3.0% for post-fix agent replies | | | measured on a sample; **the sample missed the March cluster** |
| (d) hours at peak cover 320 (two temps) | pilot 29 h | pilot 3 h | pilot 32 h + date fix 121 h = **153 h** | pilot: attributed for email (holdout), directional for WhatsApp; date fix: measured share, directional hours |
| Adoption gate: drafts used on ≥ 60% of eligible tickets two weeks running | **73–77%** every week | 30% → 9% | 29–44% | measured (pilot log) |

Three readings stand out. Email and web form pass every condition that can be read on them. WhatsApp, which is about 70% of eligible tickets, fails acceptance and adoption. And (d) does not reach even one temp (160 hours) at today's WhatsApp use, because the pilot's hours were always going to come from the big channel.

The usage export tells you where use stopped, which the pilot log cannot: twelve people inserted drafts in weeks 1–3, seven in weeks 6–8. Three agents stopped in week 4, the week they moved into the new WhatsApp pod; of the others who dropped out, one is on maternity leave and one resigned, which is not non-adoption; two marketing licences were never used. The champions' log says why the pod stopped: WhatsApp drafts are six to eight lines when customers expect two (issue I-05), the WhatsApp style needs a WhatsApp test set that is late (I-10), and migrated quick replies still give the checkout date (I-07). Module 6 built this view and the adoption pre-read of 28 March ([06.4](../module-06/lesson-04.md)), which already asked for WhatsApp drafts to be switched off until the WhatsApp style passes a test set; Samir switched them off on Monday 29 March. Note how the finding is written: a queue and a design defect, not three names. The AUP promises usage reporting by team, not by person, and a decision record is read by more people than any dashboard.

One more reading belongs to the gate, though no condition names it: the stop rule for language (acceptance below 60% for two weeks) was written per language, not per channel. Combined, Arabic sat at 63% and never triggered it; WhatsApp Arabic alone, at 51%, would have. A stop rule that averages over the segment that fails is not a stop rule. Fix it in the record.

### Step 2 — Check the gates nothing can buy first

Before weighing value, check the conditions that no amount of value compensates for. If one fails, the verdict for that segment is stop or fix, however good the hours look.

| Non-compensable gate | Reading on 1 April | Status |
|---|---|---|
| Lawful use of the data | Counsel's answer of 15 January (pseudonymised, inside the approved tool); DPIA addendum for WhatsApp signed 28 January | pass |
| Harm | Seven refund promises outside policy and one disclosed address, 10–15 March; contained within 15 minutes, cause removed, negative tests added, customers honoured; counsel holds the reporting question ([07.5](lesson-05.md)) | pass **with** the post-incident controls (money flag, source change control) live |
| Minimum performance | Email and web form above every threshold; WhatsApp below | pass / **fail** |
| Accountable owner | Samir, named in the charter, switched drafts off on 15 March | pass |
| Monitoring and response | Live since 1 February; missed a cluster the spot audit could not see | pass with a change (money flag as a monitored signal) |

Only then look at value. A strong (b) does not compensate a failing (a) on WhatsApp; a good hours forecast does not compensate an untested source change.

### Step 3 — Decide per segment

The verdicts are scale (widen it), fix (keep it in its envelope, fix a named thing by a date, re-gate), and stop (switch off and decommission). "Sustain", in IBM's words, is a fix with no change.

| Segment | Verdict | Why, in one line |
|---|---|---|
| Drafts on email and web form, four languages | **Scale**: from pilot to service, owned by Samir, drafts on by default for every eligible ticket | Every condition passes, attributed by the holdout (3.3 minutes saved per drafted contact) |
| Pre-filled drafts (stage 3 of 05.6) | **Not now** | Its entry condition (four weeks ≥ 85% on the categories) is met for WISMO, but after an incident with seven approvals in under ten seconds, making stamping easier waits for the re-gate |
| Drafts on WhatsApp | **Fix**: off since 29 March; WhatsApp test set and style, back in shadow mode, checkpoint on Thursday 13 May, re-gate on Thursday 1 July | Fails (a) and adoption for named, fixable reasons (length, style, quick replies); it is where the case's hours are |
| Damage and returns drafts | **Keep** with the money flag and source shown | Restored after three days in shadow on 19 March; no repeat since |
| LinguaFlow seats for Customer Service | **Retire** (Step 7) | Russian and Arabic email drafts replace it; the cash line in the case depends on it actually stopping |

### Step 4 — Write the decision record

A decision record is short, signed and specific. It says what was decided, what else was considered and why not, on which evidence with which label, with what money, under which conditions, who can stop it, and what would change it. The [decision record](../../templates/decision-record.md) template has the fields; three of them are where records usually fail.

**Departures from the pre-agreed rule.** Gate 1 said "all yes" for the ₪72,000. It is not all yes. If the committee releases any of the money, that is a new decision and must say so: "Gate 1 was not met (a, d, adoption). The committee departs from the gate rule to release ₪30,000 of stage 2, for the WhatsApp fix only, because it buys the evidence that decides the rest; ₪42,000 is held." A gate that fails while the money flows anyway, without a sentence like this, teaches everyone that gates are decoration.

**What would change it.** Write the conditions of the re-gate as yes/no, with the instrument: on 1 July, WhatsApp acceptance ≥ 70% in each of Hebrew, Arabic and Russian on at least 100 drafts each; drafts used on ≥ 50% of WhatsApp tickets for two consecutive weeks; at least 1.5 minutes saved per WhatsApp contact against a 10% WhatsApp holdout; no harm stop rule without containment the same day. And what happens on a no: WhatsApp drafts off, the ₪42,000 not spent, the next peak staffed with temps, and the board told in July.

**Dissent.** If someone disagreed, write who and what. Yoav wanted pre-filled drafts switched on now "to show progress to the board"; the record says so and says why the committee did not. A record without dissent is either a unanimous committee or an edited one, and the next reader cannot tell which.

### Step 5 — Fund nothing new this cycle

A gate that is not fully met is the worst moment to start new things: the team's attention is the scarcest resource, and each new build competes with the fix for the same people. Four requests reached this meeting:

| Request (intake register) | Asks | Decision this cycle | Where it goes |
|---|---|---|---|
| IN-07 Instagram reply drafts (Noa) | about ₪25,000 | Not funded | Next cycle's intake review (H2 planning, June); needs a channel decision first |
| IN-09 B2B quote drafts (Yaniv) | about ₪40,000 | Not funded | Precondition not met (12 of 30 price agreements in Priority); re-screen when 30 are in |
| IN-10 ChatNest proof of concept (Yoav, from the vendor) | vendor time, our data | Not now | Roadmap L3 re-screen on 28 October 2027, as agreed in December |
| IN-11 Assembly answers (Olga, Shani) | team time | Not now | Roadmap L2 re-screen on 30 June |

The rule has three parts. The held ₪42,000 is not a pot: it is released for the WhatsApp fix or not at all. Every request gets a written answer, a reason and a date, so nobody needs to build it on a personal card in the meantime. And the exception is narrow: safety, law, or a fix to something already running.

### Step 6 — Merge the duplicate build where it can be merged now

The incident review asked for one thing beyond the fix: find every other copy of the 2023 returns policy in an AI tool. It found IN-08, a "B2B reply helper": a shared project in the approved chat tool, built on 3 February by two of Yaniv's account managers, drafting replies to hotel and office customers. Its uploaded files are a January price-list export, the 2023 returns policy copied from the same shared-drive folder that caused the incident, and 40 hotel email threads with names and phone numbers. It overlaps the drafts service (replies) and the unfunded quotes bet (prices). Nobody registered it, and nobody did anything wrong by the letter of the policy: the tool is approved.

Merging is two moves, and only the first one is possible this cycle.

1. **Merge the knowledge now.** One policy library, owned by Samir, under the source change control adopted after the incident; the helper is pointed at it. The 2023 policy and the email threads are deleted from the project (the threads also break the data boundary: personal data in a shared project without a reason). The helper is registered (IN-08, owner Yaniv, tier medium) and its prompt goes into the same version log.
2. **Merge the build next cycle.** Two tools drafting replies for the same company, with two sets of rules, will drift apart again. Whether B2B email becomes a queue of the drafts service, or the helper is retired, is a decision for the H2 intake review, with the quotes bet. Until then it runs in its corrected form.

The mistake to avoid is the opposite of each move: shutting the helper down on the day you find it (the account managers go back to personal accounts, and the next one is not found by a search), or blessing it as it is (two libraries, one of them stale).

### Step 7 — Decommission the retire, completely

"Retire" is the verdict most often left half-done: the decision is minuted, and a year later the seats are still billed, the extension still runs on six machines, and the vendor still holds the account. Decommissioning is a checklist with an owner per line and a check at the end. For LinguaFlow's Customer Service seats (approved in November as IN-01; Ronit gave notice on 4 March to cut them from 1 May; marketing keeps a small plan):

| Line | What exactly | Owner | Date |
|---|---|---|---|
| Decision and date | Retire the Customer Service seats; marketing's small plan stays | Committee | 1 Apr |
| People | Tell the agents what replaces it (drafts for Russian and Arabic email; inbound translation in the drafts panel) and what to do for WhatsApp until July (type, or ask a native-speaking colleague) | Samir | 4 Apr |
| Access | Remove the seats; remove the Business sign-in for Customer Service; device policy blocks the extension on Customer Service machines | Avi | 30 Apr |
| Data | Export the shared glossary (DPA §8: exportable any time); confirm in writing that the Customer Service accounts' data is deleted (the DPA says within 30 days of termination) | Avi | 31 May |
| Contract | Notice confirmed; the next invoice shows only marketing's plan | Ronit | 1 May / first invoice |
| Records | Intake register IN-01 updated; AI inventory, tools-and-data-classes list, DPIA scope and risk register updated; the ROI model's benefit line moves from directional to banked | You | 7 May |
| Check after 30 days | Proxy log: no LinguaFlow traffic from Customer Service; expense claims: no personal translation subscriptions; extension inventory: none on Customer Service machines | Avi | 1 Jun |

Retire the non-AI leftovers in the same sweep: the helpdesk's order-status macro, which repeats the checkout date after it has passed, and the WhatsApp quick replies migrated from the phones (issue I-07). A retired path that is still one click away is not retired.

### Step 8 — Re-forecast the case, and say it plainly

The record ends with the money, in the ROI model's terms. Cash already banked: ₪17,000 a year (translation, once Step 7 is checked). Temps: at today's WhatsApp use the hours cover none; if WhatsApp drafts reach email's level of use with about 2 minutes saved per contact, about 215 hours, one temp (₪48,000). Two temps are not supported by any reading. The expected cash case is therefore ₪65,000 a year if the fix works, against ₪49,000 a year to run: thin in cash, and mostly a capacity case (about 29 hours a month at peak from email today, about 90 with WhatsApp fixed). Ronit should hear this from you at the gate, and the board in your next update, not in September.

## Watch out

- **The average verdict.** "73% overall, close to 80%" hides a channel that works and a channel that does not. Split before you decide.
- **Money flowing past a failed gate without a sentence.** If the committee releases money anyway, the record says the gate failed and why the committee departs from it.
- **Scaling the part that fails because it is the big one.** WhatsApp is where the hours are, which is why it gets a fix with a date, not a pass.
- **A stop rule that averages.** Write stop rules per segment that can fail on its own (channel × language here).
- **Starting the new things with the held money.** "Fund nothing new" means the held amount is not a pot for the requests in the queue.
- **Shutting down a duplicate build on discovery.** The users move to personal accounts and the next one is invisible. Fix its sources now, decide its future in the next cycle.
- **A retire that stops at the minute.** Seats, extension, vendor data, invoice, records and a 30-day check. Until the invoice line changes, the benefit is not banked.

## Your turn

### Inputs

- Module download, `labs/module-07/`: `gate-1-readings.csv`, `gate-1-weekly.csv`, `gate-1-other-readings.csv` (the pilot log's readings, synthetic), `intake-register-2027-03.csv`.
- Data room (`labs/common/harbor-and-pine/`): `usage/ai-usage-export.csv` and `usage/hr-roster.csv`; `vendors/linguaflow-translation-dpa.md`.
- Module 6 download: `labs/module-06/champions-issues-log.csv` and `queue-rota-2027.csv`.
- Your pilot charter and value measurement plan ([05.1](../module-05/lesson-01.md)), ROI model ([03.7](../module-03/lesson-07.md)), monitoring spec ([05.7](../module-05/lesson-07.md)).
- Templates: [decision record](../../templates/decision-record.md), [AI intake register](../../templates/ai-intake-register.md).

### Steps

1. Fill the gate table per channel and language for (a)–(d) and the adoption gate, each with its label.
2. Check the non-compensable gates; mark any segment that fails one.
3. Decide scale, fix or stop per segment, one line of reason each.
4. Write the decision record: decision, options and why not, evidence with labels, money released and held, any departure from the gate rule, re-gate conditions and what happens on a no, who can stop it, dissent.
5. Answer each request in the intake register for this cycle, with a reason and a date.
6. Write the two-step merge for IN-08.
7. Write the decommissioning checklist for the LinguaFlow seats and the two non-AI leftovers.
8. Re-forecast the case in cash and capacity.

**Track B (Python).** From `labs/module-07/` with the field kit set up, run `python gate1_evidence.py`. Python is worth it here because the gate needs two joins a spreadsheet makes tedious and error-prone (the usage export with the HR roster to separate quiet non-adoption from leave and resignation; the pilot log by channel and language for every condition), and because the hours at peak depend on assumptions you will want to vary: `python gate1_evidence.py --whatsapp-use 0.5 --whatsapp-saving 1.5` shows what a half-fixed WhatsApp buys.

### Time

120 minutes: 30 for the gate table and the non-compensable check, 15 for the verdicts, 35 for the decision record, 15 for the request queue and the merge, 15 for the decommissioning checklist, 10 for the re-forecast.

### Done when

- [ ] Every gate condition is read per channel and language, with its label, and the pilot-wide average is not the basis of any verdict.
- [ ] Each segment has scale, fix or stop with a reason.
- [ ] The record states that gate 1 was not fully met and why any money is released anyway.
- [ ] The re-gate has yes/no conditions, a date, an instrument and a consequence of "no".
- [ ] Every request in the queue has an answer, a reason and a date, and the held money is not re-allocated.
- [ ] The decommissioning checklist covers people, access, data, contract, records and a 30-day check.

<details><summary>Reference answer</summary>

**Decision record DR-2027-04 — reply drafts, gate 1 — steering committee, Thursday 1 April 2027**

*Present:* Yoav Ben-Ami (chair), Ronit Avraham, Michal Peretz, Samir Haddad, Avi Mizrahi, pilot lead (secretary).

**Decision.** Gate 1 was not fully met: (a) and the adoption gate fail on WhatsApp, and (d) reaches 153 hours against 320. The committee decides, per segment: **scale** drafts on email and web form from pilot to service from Sunday 4 April (owner Samir; operating rhythm as in 07.6); **fix** WhatsApp drafts (off since 29 March; WhatsApp test set and style, then shadow mode; checkpoint Thursday 13 May, when drafts return on demand if the test set passes) with a re-gate on Thursday 1 July; **keep** damage and returns drafts with the money flag and source shown; **retire** LinguaFlow's Customer Service seats; **not now** for pre-filled drafts.

**Money.** Stage 1: ₪46,800 of ₪48,000 spent. The committee departs from the gate rule to release **₪30,000** of stage 2 for the WhatsApp fix only: WhatsApp test set of 300 messages labelled by Olga and Lina (about 30 hours, ₪3,900 internal); WhatsApp style and a short-draft mode (integrator, 3 days, ₪12,000); a 10% WhatsApp holdout and logging (2 days, ₪8,000); money flag and source change control built into the integration (1.5 days, ₪6,000). **₪42,000 is held** until 1 July and is not available to other requests.

**Evidence** (pilot log 15 Feb – 28 Mar; usage export weeks 1–8). Email and web form: 82.5% accepted (ar 73.9%), 2.0–2.5 minutes review, 3.3 minutes saved per drafted contact against the holdout (attributed), drafts used on 73–77% of tickets every week. WhatsApp: 58.3% accepted (ar 51.0%, ru 56.8%), used on 9–30% of tickets, 0.5 minutes saved (directional). Spot audit 1.9% wrong against 3.0% today (measured on a sample; it missed the March cluster). Date fix: WISMO share of written contact 44% → 22.5%, about 121 hours at peak (directional). Quiet non-adoption: the WhatsApp pod stopped using drafts in week 4, the week it was formed (champions' log I-05, I-07, I-10); the other drop-outs are a leave and a resignation; two unused marketing licences reclaimed. Reported by queue, not by person (AUP §6).

**Options considered.** Release all ₪72,000 (rejected: two failing conditions, and the money would buy pre-filled drafts before WhatsApp works). Stop the pilot (rejected: email and web form pass every condition and Russian and Arabic agents would lose their tool; the LinguaFlow seats would have to come back). Fix with part of the money (chosen).

**Re-gate, Thursday 1 July 2027, all yes.** WhatsApp acceptance ≥ 70% in each of he, ar, ru on ≥ 100 drafts each; drafts used on ≥ 50% of WhatsApp tickets for two consecutive weeks; ≥ 1.5 minutes saved per WhatsApp contact against the holdout; no harm stop rule without same-day containment; spot audit at or below today's rate. *If yes:* the ₪42,000 is released (integration hardening and contingency) and gate 2 on 30 September decides one temp. *If no:* WhatsApp drafts off; the ₪42,000 is not spent; email and web form continue as a service if the running cost is cut to match; the November peak is staffed with two temps; the board is told in July.

**Changed controls.** Stop rules are per channel × language from today. The money flag (any draft mentioning a refund, credit or compensation gets a second look) is a monitored signal. Source and prompt changes follow change control (07.5 review, adopted 22 March).

**Who can stop it.** Samir or the pilot lead, the same day, on any stop rule; the chair at the re-gate.

**Requests this cycle.** IN-07, IN-09, IN-10, IN-11 not funded, each with the reason and date in Step 5; answers sent by Michal on 4 April.

**Duplicate build IN-08.** Sources merged now (2023 policy and email threads deleted from the project on 1 April by Yaniv with Avi; pointed at Samir's policy library; registered); build merge decided at the H2 intake review in June.

**Dissent.** Yoav asked to switch on pre-filled WISMO drafts now "so the board sees progress". Not adopted: after an incident in which seven drafts were approved in under ten seconds, the committee will not make approval easier before the re-gate. Yoav accepted the decision and asked for a one-page board update by 15 April.

**Re-forecast.** Cash banked: ₪17,000 a year (translation, after the 30-day check). Expected if the fix works: ₪65,000 a year (₪17,000 + one temp ₪48,000, directional), against ₪49,000 a year to run. Capacity: about 29 hours a month at peak today, about 90 with WhatsApp fixed. Two temps: not supported by any reading.

*Signed:* Yoav Ben-Ami, Ronit Avraham. *Next review:* 1 July 2027.

**Decommissioning checklist** as in Step 7, plus: the order-status macro deleted (Samir, 4 April); migrated WhatsApp quick replies replaced by two approved ones (Avi, 4 April, closes I-07).

</details>

## References

- IBM, [Lead AI Transformation certificate](https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution), course 6 (pilot isn't scale; non-compensable gates and readiness factors; scale / sustain / retire); IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting), courses 4 and 5 (staged money against gates). Named, not re-taught.
- Templates: [decision record](../../templates/decision-record.md), [AI intake register](../../templates/ai-intake-register.md), [ROI model](../../templates/roi-model.md), [monitoring spec](../../templates/monitoring-spec.md).
- Earlier: [03.7 · The ROI model](../module-03/lesson-07.md), [05.1 · The pilot charter](../module-05/lesson-01.md), [05.6 · Shadow mode, staged release and rollback](../module-05/lesson-06.md), [04.7 · Governance that runs](../module-04/lesson-07.md); module 6's adoption dashboard, [06.4](../module-06/lesson-04.md). Next: [07.3 · Delivering bad news upward](lesson-03.md); what the service needs from April, [07.6](lesson-06.md).
- Module project: [Readout — Harbor & Pine](../../projects/m07-readout.md).
