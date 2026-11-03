---
id: "17.5"
module: 17
minutes: 22
practice_minutes: 180
prerequisites: ["17.4", "07.2", "07.5", "01.7", "04.3"]
objectives:
  - "Run a stop/keep audit of every AI system by joining what it costs, who uses it, what is open about it, what the contract allows and the evidence of value, and decide each line by the rules."
  - "Close an open AI incident with the runbook: reopen it, contain it narrowest first, scope it from the logs, route every reporting question to counsel with the facts, rewrite the root cause without blame, and set closure criteria."
  - "Take the decisions that cannot wait for the board — a contract notice, a stop, a customer's request — as decision records with options, owner and date."
  - "Meet the customer harmed by the incident and the vendor who caused it, give facts before apologies, and recognise an offer designed to pass a deadline."
volatility: implementation
sources:
  - title: "IAPP, 'The new Israeli data security regulations: A tutorial' (serious security incidents: report immediately; notifying data subjects at the regulator's request)"
    url: https://iapp.org/news/a/the-new-israeli-data-security-regulations-a-tutorial
  - title: "GDPR Article 33, Notification of a personal data breach to the supervisory authority (gdpr-info.eu)"
    url: https://gdpr-info.eu/art-33-gdpr/
  - title: "NIST SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile (April 2025)"
    url: https://csrc.nist.gov/pubs/sp/800/61/r3/final
  - title: "Knesset Research and Information Center, 'The status of the customs agent: a comparative review' (18 March 2014, Hebrew)"
    url: https://fs.knesset.gov.il/globaldocs/MMM/f970aa75-2f7b-e511-80d1-00155d0ad6b2/2_f970aa75-2f7b-e511-80d1-00155d0ad6b2_11_19515.pdf
  - title: "Bank of Israel, representative exchange rate API (USD, 2 November 2026: ₪3.136)"
    url: https://boi.org.il/PublicApi/GetExchangeRate?key=USD
last_verified: "2026-11-03"
---

# 17.5 · Decide: the stop/keep audit and the incident closed

Everything you found now has to become decisions someone can execute, and the incident has to end on facts rather than on someone's request. In this lesson you run the stop/keep audit of all nineteen lines — Track B joins the contracts, invoices, licence usage and tickets in one pass — close the incident with the runbook while counsel decides what only counsel can, take the three decisions that cannot wait for the board, and meet the customer who was harmed and the vendor who caused it. At the end you have the audit table with its money, an incident closure record with criteria, and three decision records.

> [!WARNING]
> This lesson deals with real-shaped harm: other people's personal data seen by people not entitled to it, declarations filed with customs on wrong information, a customer's shipments of medical supplies held. In a real incident, whether and what to report to the Privacy Protection Authority, to data subjects, to an EU supervisory authority or to Customs is decided by counsel, the privacy protection officer and the licensed customs agent, the same day you know the facts. This course is not legal advice and states no deadline as yours to meet.

## The situation

Sunday 27 June to Thursday 1 July 2027. The plan was agreed with both principals on Thursday ([17.4](lesson-04.md)). The incident was reopened on 14 June and contained the same day; counsel has had the facts since 8 and 14 June. The vendor sent the rest of its logs on 22 June and, with them, an offer. Gefen's VP Supply Chain met you on 21 June. The region notice must leave on Thursday 1 July, the same day as the pre-read.

This is module 7 applied under pressure: [scale, fix or stop](../module-07/lesson-02.md) for nineteen lines instead of one pilot, and [when it goes wrong](../module-07/lesson-05.md) for an incident you inherited half-handled.

## What to do

### Step 1 — Build the audit table: one join, nineteen lines

The inventory from [17.2](lesson-02.md) has twelve systems; audit them at the level a decision can be taken — by region for the route tool, by feature where one feature harms and another does not. Nineteen lines, each with:

| Column | From |
|---|---|
| Cost a month (May) | `finance/ap-invoices-ai.csv`, by contract, line and region |
| Seats billed and active | `it/licence-usage-2027-05.csv` |
| Open tickets, incident link | `incident/it-tickets-ai.csv` |
| Contract step and the date it allows | `vendor/contracts-ai.csv`, `vendor/tzir-msa-extract.md` |
| Evidence of value, labelled | your 17.3 table |
| Risk | your 17.2 memo and 17.4 control test |
| Rule, action, owner, saving and from when | the rules of 17.4 |

A worked excerpt:

| Line | ₪/month | Billed / active | Rule | Action | Contract step | Saving from |
|---|---|---|---|---|---|---|
| Route North | 36,760 | 110 / 102 | R4 | Keep and fix: feed, retrain, closures, no score | In the order form | — |
| Route Centre | 29,100 | 78 / 5 | R3 | Reduce to 5 planner seats | MSA 7.4 notice by 1 July | 1 Oct, ₪23,600 a month |
| Route South | 33,280 | 98 / 0 | R3 | Stop | MSA 7.4 notice by 1 July | 1 Oct, ₪33,280 |
| Route Europe | 17,160 | 48 / 0 | R3 | Stop | MSA 7.4 notice by 1 July | 1 Oct, ₪17,160 |
| Driver score | 0 | all regions | R2 | Stop now; undertaking to the committee | Feature switch | — |
| Tzir Docs | 130,000 | 3 houses | R1 | Keep with conditions | Fix under MSA 9.3; credits under 11.2 | — |
| Assist "my documents" | 0 | — | R1 | Stop permanently | Written amendment | — |
| Kotev Assist | 42,750 | 450 / 112 | R3 | Reduce to 150 seats | Notice by 1 October | 1 Dec, ₪28,500 |
| Ayin Drive | 18,000 | 60 / 0 | R2 | Stop | 30 days' notice, no refund | 1 Aug, ₪18,000 |
| Nezek Vision | 22,000 | 25 / 0 | R3 | Stop; claim the months after the POC ended | No exit before 31 Aug | — |
| Warehouse forecast | 6,000 | — | R4 | Keep; a second person; documentation | — | — |
| CS e-mail triage (n8n + Promptway) | ≈ 2,000 (card) | CS team | R6→R2 | Bring in on an approved route; stop the card | Procurement | — |

The money follows from the table, not from a target: savings once in effect **₪120,540 a month**; **₪340,620 inside 2027** given the notice terms; the 2027 forecast falls from ₪7.51M to ₪7.17M against the ₪5.2M budget; the 2028 run-rate is about **₪4.86M**. Nezek's months after the POC are a claim against its statement of work, not a saving: leave them out of the total.

Two lines need a sentence each in the paper. **Docs** is kept, because customs pre-fill is the module with the most value and the most risk, and stopping it moves every declaration back to manual work during an incident; its conditions are the point (Step 3). **Assist's status answers** stay under a 90-day test even though deflection measured zero, because the contract runs to 2029 and stopping the feature saves nothing; the test decides what to ask for at the renegotiation.

### Step 2 — Reopen and close the incident by the runbook

Use the [incident runbook](../../templates/incident-runbook.md). The incident is inherited, so start by putting the runbook's steps over what was done:

1. **Log and lead.** Reopened on 14 June by the incident lead, Dmitri Volkov, on your written recommendation and with the CEO's agreement, the chair copied. Severity: harm reached customers, and personal data reached people not entitled to it — the top severity in any runbook.
2. **Contain, narrowest first.** Not "switch off Docs": (a) auto-match off for invoice numbers without letters (the post-fix cause); (b) the portal file page hides documents whose owner is not the file's customer (the feature switched off on 19 May was never the only door); (c) pre-fill off for the customer who asked. Then prove it: no mismatches and no cross-customer opens in the logs from 15 to 29 June.
3. **Scope from the logs.** The numbers from 17.2, now complete: 70 mismatches, 47 submitted; 30 cross-customer opens of 22 documents by 12 customers; 2,462 records of private individuals in seven opened manifests; three of the customer's invoices opened by others; nine customs queries, three shipments held.
4. **Escalate the legal questions, with facts, and decide none of them.** For counsel: which documents, whose data, which fields, how many records, who opened them and when, that downloaded copies cannot be recalled, which system held them, the vendor's role. Counsel and the privacy protection officer decide whether the event is reported to the Privacy Protection Authority and when (the Data Security Regulations require a database owner to report a serious security incident immediately; whether this one is serious depends on the database and the scope, which is exactly what counsel weighs), whether the consolidator and the people in its manifests are told, and whether any data falls under the GDPR (Article 33 has its own clock for EU controllers). For the licensed customs agent and counsel: how the 47 submitted declarations are checked against each importer's own invoices and corrected. Your closure record states who decides, when they were briefed and what they decided — never a deadline of your own.
5. **Communicate.** The harmed customer by a person with facts; the other 20 declaring customers and 23 document owners by letters counsel approves; the consolidator by counsel. If asked publicly: one true sentence that owns it.
6. **Rewrite the root cause, without blame.** The vendor's analysis (`incident/tzir-rca-2027-05-28.md`) names a trigger — "duplicate supplier invoice numbers" — and recommends that Vantage's agents review every declaration. Replace it with the contributing causes, each one a system fix: a release changed matching logic without the notice the agreement requires (`incident/tzir-release-notes-4.2.md` vs MSA 4.3) and Vantage had no way to test vendor releases; matching on invoice number alone, without the consignee; a review that existed on paper under a KPI that left no time; a portal page that showed attachments without checking ownership; two early tickets closed as "data quality"; no privacy branch; "contained" declared on the vendor's word. NIST's incident-response profile and every postmortem practice since make the same point: look for the conditions that let a reasonable person's action cause harm, not for the person.
7. **Restore in stages, and write closure criteria.** The incident closes when: no mismatches for 14 days after the vendor's consignee check (or with auto-match off); every affected customer informed; counsel's decisions recorded with their dates; every submitted declaration checked by the brokerage and corrected where needed; service credits claimed; the change-control step for vendor releases running. On 1 July four of six are met: **the board hears "contained, not closed", with the two remaining dates.**

[Simulation: Incident tabletop](../../simulations/incident-tabletop/index.html?preset=harbor)

The tabletop is Harbor & Pine's incident (a draft promising refunds and disclosing an address), not Vantage's. Play it to rehearse the order — contain narrowest first, route reporting to counsel, communicate, then fix — and compare your Vantage log with its runbook.

### Step 3 — Write Docs' conditions so they can be checked

"Keep with conditions" is only honest if each condition can be seen to be met or missed. For Tzir Docs, reviewed at day 90 (30 September): auto-match off for invoice keys without letters until the vendor's consignee cross-check passes a test on May's 70 mismatches; the supplier invoice displayed beside the pre-fill; the KPI back to 9–10 a day; a 5% weekly QA sample by the customs compliance team; a stop rule (material error above 5% in any month suspends pre-fill until two months under 3%); the tariff-suggestion feature in the brokerage software off until it is evaluated beside Docs; vendor releases to a test tenant first.

### Step 4 — Take the decisions that cannot wait, as decision records

Use the [decision record](../../templates/decision-record.md). Three cannot wait for 5 July:

- **The region notice.** Options: give notice under MSA 7.4 (South and Europe removed, Centre reduced, from 1 October); waive it for the vendor's offer; leave it to the board on 5 July. The vendor's offer — "a free 12-month extension of all four regions plus service credits if Vantage waives the notice this year" — sounds generous. Read what it does: it extends seats nobody uses past the only date on which Vantage can remove them, and the credits are owed under clause 11.2 anyway. Leaving it to the board misses the date. Recommendation: give notice; seats can be added back later, removed seats cannot be un-paid. Decided and signed by the CEO; the chair informed (protocol line 4).
- **The cameras.** Stop with 30 days' notice (8 June); any safety technology later goes through clause 14.
- **The customer's request.** Pre-fill off for its files until a QA result can be shown; decided by the head of customs brokerage on 21 June.

Each record: options, the evidence, who decided, the date, what would change it.

### Step 5 — Meet the customer, then the vendor

**The customer.** Roleplay: [Orit Ben-Shushan](../../labs/module-17/personas/orit-gefen-customer.md), Gefen Medical Distribution (no-roleplay path: [transcript](../../labs/module-17/personas/transcripts/orit-gefen-customer.md)). Apologise once, specifically ("you should have had a written answer a month ago"), then facts with numbers, then what is not yet known and when it will be, then what changes. Don't say "no personal data was involved" — she has not asked, the statement was wrong once already, and her concern is her own commercial data. Then ask what Gefen needs to stay. Don't commit money or customs corrections you cannot commit: name who decides.

**The vendor.** Roleplay: [Yaniv Sasson](../../labs/module-17/personas/yaniv-tzir-vendor.md). Ask for the release history against clause 4.3, the logs under 9.3, the credits under 11.2, and a date for the consignee check. Mention the region notice and listen for the offer; recognise it; sign nothing. Run both transcripts through the [coach prompt](../../labs/common/coach-prompt.md).

## Watch out

- **Auditing "the platform".** One vendor, three modules, four regions: nineteen decisions, not one.
- **Booking savings the contract doesn't allow yet.** Each saving carries its start date. Nezek's months are a claim, not a saving.
- **Containing by switching off the visible feature.** The portal page was a second door. Prove containment from the logs.
- **Writing the law into the closure record.** "We must report within X" is counsel's sentence, not yours. Record who decides, when briefed, what they decided.
- **Adopting the vendor's root cause.** "Your suppliers reuse invoice numbers" is the trigger. The causes are the release without notice, the key without the consignee, the review on paper.
- **Blaming the agents.** Nineteen seconds under a KPI of twelve a day is a design, not carelessness.
- **Taking the generous offer.** An offer that arrives a week before a notice date is usually about the date.
- **Apologising instead of answering.** The customer wants facts with dates. One apology, then numbers.

## Your turn

### Inputs

- Your work from 17.2–17.4.
- The [data room](../../labs/module-17/data-room/INDEX.md) (module download): `finance/ap-invoices-ai.csv`, `it/licence-usage-2027-05.csv`, `vendor/contracts-ai.csv`, `vendor/tzir-msa-extract.md`, `incident/` (all), `customs/declarations-prefill-2027-05.csv`, `portal/document-access-log-2027-05.csv`, `portal/document-index-2027-05.csv`, `customs/customs-queries-2027.csv`, `customers/gefen-email-2027-05-19.md`.
- Track A: `labs/module-17/audit-sheet.csv` (the nineteen lines with cost, seats and open tickets filled; the decision columns empty). Track B: `labs/module-17/audit.py`.
- Personas: [Orit Ben-Shushan](../../labs/module-17/personas/orit-gefen-customer.md), [Yaniv Sasson](../../labs/module-17/personas/yaniv-tzir-vendor.md), [Dmitri Volkov](../../labs/module-17/personas/dmitri-it-security.md) (or transcripts); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [AI inventory](../../templates/ai-inventory.md), [incident runbook](../../templates/incident-runbook.md), [decision record](../../templates/decision-record.md), [vendor AI questionnaire](../../templates/vendor-ai-questionnaire.md) (for the questions to the vendor).

### Steps

1. Fill the audit sheet: evidence label, risk, rule, action, owner, contract step, saving and its start date, for all nineteen lines. Total the savings inside 2027 and once in effect; restate the 2027 forecast and the 2028 run-rate.
2. Write the incident closure record by the runbook's seven steps: containment proven from the logs, the full scope, the facts for counsel and for the licensed customs agent, the communication plan, the rewritten root cause, the closure criteria and which are met on 1 July.
3. Write Docs' conditions so each can be checked, with a stop rule.
4. Write the three decision records (region notice, cameras, the customer's request).
5. Meet Orit, then Yaniv (roleplay or annotate the transcripts). Record what Gefen needs to stay and what the vendor offered.

**Track B (Python).** `python audit.py` joins May's invoice lines, the licence export, open tickets and the contract terms to the nineteen lines, applies the rules, prints the table, the money (inside 2027, once in effect, the 2028 run-rate) and the incident scope, and writes `out/audit.csv`; `python audit.py --sheet` rebuilds the Track A sheet. Python is worth it here because the audit is a join of five sources that change every month — new invoices, new licence counts, new tickets — and it must be re-run with identical rules until the last notice takes effect in December. One note on money: the card's US$ lines use the issuer's monthly conversion as recorded; at the Bank of Israel representative rate of ₪3.136 per US$ (2 November 2026) May's US$604.35 would be about ₪1,895.

### Time

180 minutes: 50 for the audit, 50 for the incident closure record, 15 for Docs' conditions, 20 for the decision records, 45 for the two meetings.

### Done when

- [ ] All nineteen lines have a rule, an action, an owner, a contract step and a dated saving; the totals follow from the table.
- [ ] Containment is shown from the logs after the date it was applied, not assumed.
- [ ] The closure record lists the facts given to counsel and the customs agent, names who decides each legal question, and states no legal deadline of your own.
- [ ] The root cause is written as contributing causes with a system fix each, and blames no person.
- [ ] Closure criteria exist, and the board will hear which are not yet met.
- [ ] The region decision record shows the vendor's offer as an option and why it was not taken.
- [ ] The customer heard one apology and facts with dates, and you know what it needs to stay.

<details><summary>Reference answer</summary>

The full version is `labs/module-17/expert/05-stop-keep-audit-and-incident-closure.md` (module download); `audit.py` reproduces the table and the money.

**Audit:** stop 7 (Route South, Route Europe, the driver score, Assist "my documents", Ayin Drive, Nezek Vision, the quote add-in), reduce 2 (Route Centre to 5 planners, Kotev to 150 seats), keep 5 (Route North "keep and fix", the platform fee, Docs with conditions, Assist status "under test", the warehouse forecast), register 2 (Smart Match kept; HS Suggest turned off until evaluated), bring in 2 (the CS triage, the translator), retire 1 (the dashboard as evidence). May cost of the audited lines ₪452,250 a month; saving once in effect ₪120,540 a month; inside 2027 ₪340,620; 2027 forecast ₪7,510,868 → ₪7,170,248; 2028 run-rate ₪4,864,520 (Route ₪731,520, Docs ₪1,560,000, Assist ₪1,140,000, Kotev ₪171,000, cloud ₪72,000, team ₪1,190,000).

**Incident:** reopened 14 June; contained the same day (auto-match off for numeric keys; portal page hides documents not owned by the file's customer; Gefen's pre-fill off from 21 June), proven by no mismatches or cross-customer opens 15–29 June. Scope: 70 / 47 submitted; 30 opens, 22 documents, 12 customers; 2,462 records; 9 queries, 3 held. Counsel briefed 8 and 14 June with the facts; counsel decides reporting, who is told and any GDPR question; Shlomo and counsel decide the declarations (the nine queries answered by 18 June). Root cause: seven contributing causes, each with a fix. Closure criteria: six; four met on 1 July — the board hears "contained, not closed".

**Decision records:** region notice signed by Ofer on 1 July (South and Europe removed, Centre reduced, from 1 October; the vendor's free-extension offer rejected because it carries unused seats past the only removal date and the credits are owed anyway); Ayin stopped 8 June; Gefen's pre-fill off 21 June.

**Orit:** after the facts, she named what Gefen needs: a written account within a week with named owners, pre-fill off for its declarations until a QA result, a quarterly QA report, the ₪85,000 air shipment covered (Ofer to decide by 1 July). The transcript's interviewer gave the facts well but never asked what Gefen would need to stay, so the competitor's offer (about 6% lower, "no AI on your declarations") stayed hidden.

</details>

## References

- IAPP, [The new Israeli data security regulations: a tutorial](https://iapp.org/news/a/the-new-israeli-data-security-regulations-a-tutorial): serious security incidents reported immediately by the database owner; notification of data subjects at the regulator's request. Counsel works from the current text after Amendment 13.
- [GDPR Article 33](https://gdpr-info.eu/art-33-gdpr/): the EU controller's notification duty and the processor's duty to tell the controller. For EU counsel.
- NIST, [SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) (April 2025): incident response within risk management.
- Knesset Research and Information Center, [The status of the customs agent](https://fs.knesset.gov.il/globaldocs/MMM/f970aa75-2f7b-e511-80d1-00155d0ad6b2/2_f970aa75-2f7b-e511-80d1-00155d0ad6b2_11_19515.pdf) (Hebrew): the Customs Agents Law, 5725-1964.
- Bank of Israel, [representative exchange rate](https://boi.org.il/PublicApi/GetExchangeRate?key=USD): ₪3.136 per US$ on 2 November 2026.
- [Simulation: Incident tabletop](../../simulations/incident-tabletop/index.html?preset=harbor) (Harbor & Pine's incident; educational model).
- Field kit: [01.7 · The AI inventory from zero](../module-01/lesson-07.md), [04.3 · Vendor and tool review](../module-04/lesson-03.md), [07.2 · Scale, fix or stop](../module-07/lesson-02.md), [07.5 · When it goes wrong](../module-07/lesson-05.md).
- Templates: [AI inventory](../../templates/ai-inventory.md), [incident runbook](../../templates/incident-runbook.md), [decision record](../../templates/decision-record.md), [vendor AI questionnaire](../../templates/vendor-ai-questionnaire.md).
- Earlier: [17.4 · The hard part: a turnaround](lesson-04.md). Next: [17.6 · Readout and debrief](lesson-06.md).
