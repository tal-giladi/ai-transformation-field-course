---
id: "02.6"
module: 2
minutes: 18
practice_minutes: 90
prerequisites: ["02.5"]
objectives:
  - "Set a one-line bar for each readiness dimension before reading the evidence, for named use cases."
  - "Write every finding as observation plus consequence, dated, with its source and a status of verified, reported or contradicted."
  - "Give each use case a verdict — proceed, phase or not yet — with the findings it turns on and the evidence that would change it."
volatility: concept
sources:
  - title: "NIST AI Risk Management Framework 1.0 — Core (MANAGE 1.1, MAP 2.3, MAP 4.1)"
    url: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
  - title: "Pearl Cohen — Israel: New Draft Guidelines on the Application of Privacy Law to AI (4 May 2025)"
    url: https://www.pearlcohen.com/israel-new-draft-guidelines-on-the-application-of-privacy-law-to-ai/
last_verified: "2026-11-02"
---

# 02.6 · The readiness assessment as a deliverable

A readiness assessment is where discovery becomes a judgment someone can act on: for each thing the organization wants to do with AI, is the organization around it ready — the work, the data, the owners, the people, the rules, the measurement, the technology — and if not, what has to change first. In this lesson you write Harbor & Pine's assessment from everything you gathered in 02.1–02.5: a bar for each dimension, a log of dated findings each marked verified, reported or contradicted, and a verdict per use case of proceed, phase or not yet. At the end you have the assessment, ready for the steering group, and you have seen how an honest report and an over-claimed one land differently.

## The situation

Thursday 26 November 2026, four weeks in. Michal has asked for a readiness assessment at Monday's steering check-in (Michal, Ronit, Yoav), ahead of your findings memo on 1 December and the decision on 10 December about what to have working by the board meeting. Yoav will read it looking for permission to proceed with the bot. Ronit will read it looking for the first claim she can knock over.

You hold a lot of evidence of very different strength: interview notes, a KPI report, the handbook, profiles you ran yourself on full exports, a one-week hand tally, vendor documents, the sit-in notes. The assessment's credibility depends on never writing a claim stronger than its source.

IBM's readiness course frames this as a dated finding against a stated bar, every claim labelled by provenance, and a recommendation that is allowed to say "not yet". Lesson 01.7 kept the maturity view separate from the AI inventory; this is that view, written as a deliverable.

## What to do

### Step 1 — Name the use cases

Readiness is always readiness *for something*. Use the ideas that came out of discovery and the one the CEO announced:

- **A.** Draft replies for email and web-form messages; an agent checks and sends every one.
- **B.** Suggest decisions on damage claims.
- **C.** Tell customers proactively when their container is late (plain automation, no AI).
- **D.** A customer-facing chatbot on the website (the CEO's announcement).
- **E.** Anything on the WhatsApp channel.

### Step 2 — Set the bar for each dimension, before you look

Seven dimensions; one line each saying what "ready" means for these use cases. Writing the bar first stops you from fitting the bar to the evidence afterwards.

| Dimension | The bar (Harbor & Pine, these use cases) |
|---|---|
| Work and process | The process can be walked on paper: steps, owner per step, trigger, volume; the root cause of the volume is known |
| Data | The data the use reads is complete for its fields, current, joinable, and has a recorded outcome where the use needs one |
| Ownership | A named person owns each output and each data source the use depends on |
| People and adoption | The people who will use or check it have the time and the skill, and want it |
| Governance, privacy and legal | An AI-use rule is in force; the permission question for each dataset has an answer from counsel or the DPO |
| Measurement | Baselines with definitions exist for what the use should change |
| Technology and security | The tool's data use, storage location and settings are known and acceptable |

### Step 3 — Grade every piece of evidence

Three statuses, and only three:

- **Verified** — you checked it against data you hold, or saw it yourself.
- **Reported** — someone says so; you have not checked. An interview, a vendor statement, a document that describes rather than records.
- **Contradicted** — data you hold says otherwise.

Rules that keep you honest: an interview tells you where to look, a policy tells you what should happen, and only data you hold or saw tells you what does. Two documents that agree are still one source if one copies the other. A self-report becomes verified only when you check it.

Examples from your own files:

| Evidence | Status | Why |
|---|---|---|
| Samir: "about a third of everything is where-is-my-order" | Verified | Five signals in 02.4 put it between 31% and 44% |
| KPI report: "Average first response 2.0 hours" | Contradicted as a headline | Reproduces as 1.97 h under its own definition; the customer's median wait is 6.1 h (02.4) |
| Handbook §8: "Every claim is reviewed by QA within 48 hours" | Contradicted | No QA role, no QA column, median 8 days (02.3) |
| Senior agent: drafts Russian replies in a free chatbot | Reported, consistent with verified traces | Six replies with chatbot traces in `emails.csv`; proxy log (01.6); the individual practice itself not seen |
| WhatsApp volume: 630 conversations in a week | Verified that the tally says so; volume reported | A hand tally of estimates, one week |
| Deskly AI add-on terms: content may be used to train models unless the customer opts out | Reported | Vendor document; nobody has looked at Harbor & Pine's settings |
| ChatNest: "70% deflection" | Reported, conditions unknown | Vendor figure from other clients; nothing tests it here |

### Step 4 — Write findings, not observations

An observation is "the claim outcome is missing for 32% of claims". A finding adds what it means for the decision: "...so claims cannot train or test a decision aid until outcomes are recorded; use B is not yet ready". Each finding row gets: dimension, observation → consequence, evidence, status, date, use cases affected, owner, action and due date. Verified gaps get an owner and a date; reported items get a verification task.

Translate twice where governance is involved: once as an obligation ("customer messages and photos sit on shared phones outside any system"), once as an operating consequence ("so the main channel has no baseline, no test set and no access control").

### Step 5 — A verdict per use case, not one for the company

Three verdicts:

- **Proceed** — ready now; the remaining gaps are small and owned.
- **Phase** — start a bounded part now, under named conditions; the rest when the conditions are met.
- **Not yet** — what must be true first, in what order.

Each verdict names the findings it turns on and **what would change it**: the evidence that would move it up. "Not yet" with a sequence is a plan; "not yet" alone is a refusal.

Do not average the dimensions into a score. A use case with excellent technology and no recorded outcome is not "70% ready"; it is not ready.

### Step 6 — Say what you did not check

A short list at the end: the things you did not look at and why. At Harbor & Pine: the showrooms; Deskly's actual admin settings; the WhatsApp phones themselves; anything from the delivery company. It protects the report from the over-claim the steering group will otherwise assume.

### Step 7 — Practise the reaction

[Simulation: Readiness evidence grader](../../simulations/readiness-evidence-grader/index.html?preset=harbor)

The simulation gives you 17 dated evidence items to sort into verified, reported and contradicted, then asks for a verdict and shows the steering group reacting to an honest report and to an over-claimed one.

## Watch out

- **The over-claimed report.** Calling interview statements and vendor figures "verified" gets a fast yes and a slow collapse: the first one that falls in the meeting makes everyone re-check everything. Label honestly; an honest report with three contradictions in it is more credible, not less.
- **One verdict for everything.** "Not ready for AI" throws away the use case that is ready (C) and the one that can start bounded (A). Verdict per use case.
- **A verdict with no route.** "Not yet" without "what would change it" reads as a block, and the sponsor goes around you.
- **A readiness score.** Averaging dimensions hides the single gate that fails.
- **Undated findings.** The organization changes and so does the bar; a finding without a date will be quoted long after it stopped being true.
- **Naming people.** Findings are about the work. "A senior agent" and "the support team", never names, especially next to a workaround.
- **Skipping the legal dimension because there is no lawyer in the room.** Route the questions (02.5) and record them as open findings with an owner.

## Your turn

### Inputs

- Everything you produced in 02.1–02.5: stakeholder map, interview notes, sit-in notes and task inventory, baseline sheet, data profiles.
- In the module download: [`company/customer-service-handbook.md`](../../labs/common/harbor-and-pine/company/customer-service-handbook.md), [`company/kpi-report-2026-q3.md`](../../labs/common/harbor-and-pine/company/kpi-report-2026-q3.md), [`vendors/deskly-ai-addon-terms.md`](../../labs/common/harbor-and-pine/vendors/deskly-ai-addon-terms.md), [`vendors/chatnest-sales-deck.md`](../../labs/common/harbor-and-pine/vendors/chatnest-sales-deck.md), [`policies/data-retention-note.md`](../../labs/common/harbor-and-pine/policies/data-retention-note.md), [`people/timesheets.csv`](../../labs/common/harbor-and-pine/people/timesheets.csv).
- Template: [readiness assessment](../../templates/readiness-assessment.md); spreadsheet findings log `labs/module-02/readiness-assessment.csv` in the module download.

### Steps

1. Write the five use cases and the bar for each of the seven dimensions.
2. Grade at least 15 pieces of evidence verified / reported / contradicted, with why.
3. Write at least 12 findings (observation → consequence), each dated, with evidence, status, use cases affected, owner and action.
4. Give each use case a verdict, the findings it turns on, and what would change it.
5. Write "what we did not check".
6. Run the simulation once with an honest report and once over-claiming; note what changed in the reaction.

### Time

90 minutes.

### Done when

- [ ] Every dimension has a one-line bar written before the findings.
- [ ] Every finding has an observation, a consequence, a date, a source and one of three statuses.
- [ ] No interview statement, policy or vendor document is marked verified without a check you name.
- [ ] Every use case has its own verdict with "what would change it".
- [ ] No individual is named next to a workaround.
- [ ] "What we did not check" has at least three items.

<details><summary>Reference answer</summary>

**Readiness assessment — Harbor & Pine — 26 November 2026.** Sources: 9 interviews, 2 hours of observation, 6 exports profiled, 1 hand tally, 7 documents.

| ID | Dim. | Finding (observation → consequence) | Evidence | Status | Date | Uses | Owner | Action, due |
|---|---|---|---|---|---|---|---|---|
| R-01 | Work | 31–44% of contacts ask "where is my order", driven by a promised date that is a fixed lead time (VN 42, CN 38 days) while VN/CN orders since June arrive a median 11 days late → a bot would repeat the wrong date; the cause is upstream | `tickets.csv`, `phone-log.csv`, tally, `orders.csv`, settings | Verified | 18 Nov | C, D | Michal | Delay notice, from Dec |
| R-02 | Ownership | ETA updates stop in the logistics sheet; nobody owns telling the customer; the lead-time table belongs to marketing, last changed 14 Feb 2023 → no owner for the fix today | Mailbox, sheet vs orders, settings file | Verified | 19 Nov | C, D | Michal to assign | Owner named by 10 Dec |
| R-03 | Measurement | KPI "2.0 h" = mean working hours, Q3 email, business days; customer's median wait 6.1 h (web form 10.0 h) → the board's baseline is not the customer's | `tickets.csv` (2,319) | Contradicted (headline) | 18 Nov | A, D | Samir | Report both from Dec |
| R-04 | Measurement | "Resolution 100%" = reply sent; 23.4% of resolved tickets with an order get a follow-up within 14 days → resolution cannot measure a pilot | `tickets.csv` | Contradicted | 19 Nov | A, D | Samir | Follow-up rate as KPI |
| R-05 | Data | Most written contacts are on four shared WhatsApp phones (630 in a tallied week vs 94 helpdesk tickets); no export; order numbers match no ERP order → no baseline, test set or join for the main channel | Tally, `tickets.csv`, observation | Verified (tally, observation); volume reported | 20 Nov | E, D | Michal, Avi | Channel decision, Jan |
| R-06 | Data | Claim outcome blank for 32.2% (31.4% of claims opened by 30 Sep); no reason field → no label | Claims log | Verified | 19 Nov | B | Samir | Record decision + reason, from 1 Dec, 8 weeks |
| R-07 | Work | QA review "within 48 h" exists only in the handbook; median 8 days to decision → the decision process cannot be walked on paper | Handbook, org chart, claims log | Contradicted | 17 Nov | B | Samir | Map decision criteria, Jan |
| R-08 | Data | Helpdesk language auto-detected (121 blank, 85 wrong), category 28.5% Other → test set must be hand-coded | `tickets.csv` | Verified | 19 Nov | A | You | 200 coded messages (05.2) |
| R-09 | Data | The vendor demo used a 2023 catalogue copy (prices a median 12.7% low, 29 discontinued items) → product answers must read the ERP | Catalogues, ChatNest deck | Verified | 19 Nov | D | Liat, Avi | Archive copies, Dec |
| R-10 | Governance | Customer emails pasted into free chatbots; six sent replies carry chatbot traces; interim AI rule in force since 12 Nov → need an approved tool, or the practice returns | `emails.csv`, proxy log, interview | Verified (traces); practice reported | 20 Nov | A | Michal | Approved tool decision, Dec |
| R-11 | Governance | Purpose of using past messages for AI, claims log access, data on WhatsApp phones, the post-Amendment-13 database review: all unanswered → no dataset is cleared for use A yet | Privacy notice, IT's note | Reported (open) | 20 Nov | A, B, E | Ronit to counsel | Answers by 15 Jan |
| R-12 | People | Support at 92.2% utilisation in Nov–Jan → no training or pilot work before February | `timesheets.csv` | Verified | 18 Nov | A, D | Samir | Pilot start Feb |
| R-13 | People | Senior agents willing to help design a drafting tool, not a bot "from above" | Interviews | Reported | 12 Nov | A | Samir | Two agents on the pilot team |
| R-14 | Technology | Deskly's AI add-on terms allow training on de-identified content unless opted out (§3.2), analytics kept 24 months (§3.4), storage in the US (§5.1); settings unchecked | Vendor terms | Reported | 20 Nov | A | Avi | Check settings; opt-out decision, Dec |
| R-15 | Measurement | Handling time per task unmeasured (timer on 51%, tally estimates) → no cost baseline for A | 02.4 | Verified (gap) | 18 Nov | A | Samir | Time study 6–17 Dec |

| Use case | Verdict | Turns on | What would change it |
|---|---|---|---|
| C. Delay notice (no AI) | **Proceed** | R-01, R-02 | — (needs an owner by 10 Dec) |
| A. Draft replies, agent sends | **Phase**: build the test set and time study now; shadow mode from February | R-08, R-10, R-11, R-12, R-14, R-15 | Counsel's answer on purpose; approved tool; 200-message test set; time-study medians |
| B. Claim decision aid | **Not yet** | R-06, R-07 | Eight weeks of recorded decisions and reasons; written decision criteria |
| D. Customer-facing chatbot | **Not yet** | R-01, R-03, R-04, R-09 | C live and measured for a quarter; the vendor's deflection measured on Harbor & Pine's own data |
| E. WhatsApp | **Not yet** | R-05, R-11 | A channel decision and a business integration with a real export |

**What we did not check.** The showrooms; Deskly's admin settings; the WhatsApp phones; the delivery company's records; any data from before May 2026.

**In the simulation.** Called honestly, "phase" is approved with Ronit saying she can check any finding; calling the KPI and the vendor figure "verified" gets a quick approval that unravels when the first one falls.

</details>

## References

- NIST, [AI RMF 1.0 Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) — MANAGE 1.1 (determine whether development or deployment should proceed), MAP 2.3 (data collection and selection), MAP 4.1 (legal risks of components, including third-party data).
- Pearl Cohen, [Israel: new draft guidelines on the application of privacy law to AI](https://www.pearlcohen.com/israel-new-draft-guidelines-on-the-application-of-privacy-law-to-ai/) — the PPA's draft expectations behind the governance dimension.
- Template: [readiness assessment](../../templates/readiness-assessment.md). Related: [01.7 · The AI inventory from zero](../module-01/lesson-07.md) (inventory, maturity view and legal register kept apart).
- Previous: [02.5 · Profiling the data](lesson-05.md). Next: [02.7 · Writing a findings memo people believe](lesson-07.md).
