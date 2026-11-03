---
id: "17.2"
module: 17
minutes: 20
practice_minutes: 150
prerequisites: ["17.1", "02.2", "02.4", "02.7", "01.6", "01.7"]
objectives:
  - "Build an AI inventory from zero for an inherited programme by testing its register against licences, contracts, invoices, card lines, the proxy and tickets."
  - "Test an incident record against the logs and report the incident's real scope to both principals and counsel within the first week."
  - "Measure whether a human review step happens, and replace a vendor's accuracy figure with an error rate from a re-checked sample."
  - "Run interviews with people who lost trust in the programme, including one phone call you cannot repeat, and write a findings memo with every claim labelled."
volatility: implementation
sources:
  - title: "IAPP, 'The new Israeli data security regulations: A tutorial' (Privacy Protection (Data Security) Regulations, 5777-2017: serious security incidents)"
    url: https://iapp.org/news/a/the-new-israeli-data-security-regulations-a-tutorial
  - title: "Pearl Cohen, 'Israel: New Draft Guidelines on the Application of Privacy Law to AI' (4 May 2025)"
    url: https://www.pearlcohen.com/israel-new-draft-guidelines-on-the-application-of-privacy-law-to-ai/
  - title: "Kol Zchut, 'מעסיק חייב לשמור על פרטיות העובד' (employee privacy at work: cameras, location data, PPA guidance), updated 2 March 2025"
    url: https://www.kolzchut.org.il/he/%D7%A9%D7%9E%D7%99%D7%A8%D7%94_%D7%A2%D7%9C_%D7%A4%D7%A8%D7%98%D7%99%D7%95%D7%AA_%D7%94%D7%A2%D7%95%D7%91%D7%93%D7%99%D7%9D_%D7%91%D7%9E%D7%A7%D7%95%D7%9D_%D7%94%D7%A2%D7%91%D7%95%D7%93%D7%94
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): verified vs reported evidence; due diligence on claims"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
last_verified: "2026-11-03"
---

# 17.2 · Discovery

In an inherited programme almost every document was written by the people whose work you are checking, and the most important one, the incident record, was written from the vendor's word. In this lesson you build the inventory from zero, test the incident record against the logs and report what you find within the week, measure whether the human review happens, check "four regions live" against the routes, and interview the people who stopped trusting the programme — including the former lead, once. At the end you have an incident status note, an inventory, and a findings memo where every claim is labelled measured, reported or claimed.

## The situation

Monday 7 June to Thursday 17 June 2027. The reporting protocol is signed ([17.1](lesson-01.md)). You promised both principals the incident's real status by Thursday 10 June, and the findings by Thursday 17 June. IT has sent the exports you asked for: the customs pre-fill log, the portal's access log and document index, the tickets. The vendor has your written request for its raw logs. Nine people are on your list (see [the cast](../../labs/module-17/personas/README.md)), and the former head of AI has said he is "reachable once".

IBM's consulting certificate asks you to separate verified evidence from reported evidence and to trace every claim to its source. Here you do it against a programme whose sources are the claimants: the register, the deck and the dashboard were written by the former lead and the vendor; the incident record by IT on the vendor's word. The data room's raw exports are the only witnesses that were not trying to make a case.

## What to do

### Step 1 — Plan the interviews: order, safety, and the one call

Use the [interview guide](../../templates/interview-guide.md) and [02.2](../module-02/lesson-02.md). Three things are different in a rescue:

- **Order.** IT and security first (Monday): the incident cannot wait. Then the people who stopped the programme from below — the South's operations manager and the drivers' representative — before the people who promoted it, so that you hear the ground before the story. The CFO and the vendor mid-week. The former lead last, once you know what to ask.
- **Safety.** Three people have reasons to stay quiet: the incident lead who closed the ticket when asked, the manager who pulled a tool back against head office, the team lead whose workaround runs on her own card. Open each conversation with what you are *not* doing: "I'm not looking for who decided; I'm looking for what happened, so it can be closed properly."
- **The one call.** Plan it like a budget: three or four questions that only he can answer and that the data room cannot. "Why did you leave?" is not one of them. "What did you warn about, to whom, and on what date?" is.

### Step 2 — Build the inventory from zero

Use [01.6](../module-01/lesson-06.md) and [01.7](../module-01/lesson-07.md), and the [AI inventory](../../templates/ai-inventory.md). Start from the register (`ai/ai-register-2027-03.csv`, 8 rows), then test it against every other trace:

| Source | What it adds |
|---|---|
| `it/licence-usage-2027-05.csv` | Mishkal "Smart Match" (AP matching inside the ERP) and Meches Pro "HS Suggest" (tariff suggestions, on by default since the March release) |
| `vendor/contracts-ai.csv`, notes column | The same two, from the vendors' own release notes and documentation |
| `finance/card-and-expense-ai-2027.csv` | "PROMPTWAY *API USAGE" on the customer-service manager's card, every month, rising |
| `it/proxy-ai-hosts-2027-q2.csv` | `api.promptway.ai` from Customer Service ("allowed (uncategorised)"), `translate.freedocs.net` from both customs houses, large uploads |
| `incident/it-tickets-ai.csv` | The driver score used on a person (the 23 February data request); the March release note for HS Suggest |

Apply the counting rule. The Tzir value dashboard is a report the vendor computes, not an AI system: list it separately, because the savings came from it. The driver score is a feature of the route tool, but it is used to judge people, so it gets its own line. Result: **twelve AI systems** (eight in the register, four outside it), not seven.

### Step 3 — Test the incident record against the logs, and report it the same week

This is the step that changes the engagement. Open `customs/declarations-prefill-2027-05.csv` and add a column: `doc_owner_customer` differs from `customer_code` (the document attached to a declaration belongs to another importer). Pivot by `model_version`:

| Version | Period | Mismatched | Submitted to Customs |
|---|---|---|---|
| 4.1.3 | to 2 May | 0 | 0 |
| 4.2.0 | 3–20 May | 63 | 42 |
| 4.2.1 (the "fix") | 23 May – 3 June | **7** | 5 |

Then the portal. Join `portal/document-access-log-2027-05.csv` to `portal/document-index-2027-05.csv` on `doc_id` and keep the rows where `viewer_customer` differs from `owner_customer`: 30 opens of 22 documents by users of 12 other customers — **6 of them after 19 May**, all through the ordinary portal file page, not the assistant feature that was switched off. Seven of the 22 are B2C manifests of a parcel consolidator, with `personal_data_fields` "consignee name; street address; city; phone": **2,462 records** of private individuals (sum of `records`), 1,870 opened before 19 May and 592 after. And `customs/customs-queries-2027.csv`: nine value queries on mismatched declarations, three with goods held, all still "open" with requested response dates in May.

Compare with the record: "contained", "personal data: none", "customers affected: C1007", "Legal: n/a". The record is not a lie; it is the vendor's account copied into Vantage's system. Two earlier tickets (6 and 11 May) show the same pattern and were closed as "data quality".

What you do with it, the same day, under the protocol: a one-page **incident status note** to both principals (facts, numbers, sources, no blame), and the facts to the general counsel — which documents, whose data, which fields, how many records, who opened them, when, and that downloaded copies cannot be recalled. Whether the event must be reported under the Privacy Protection (Data Security) Regulations and to whom is counsel's decision; the regulations' duty for a serious security incident is to report immediately, which is exactly why counsel hears it this week rather than on 1 July. The step you recommend to the incident lead and the CEO: reopen the incident. [17.5](lesson-05.md) closes it.

### Step 4 — Test the review claim

The register says "licensed agent reviews every declaration"; the vendor says "99.2% accuracy". Measure both:

- In the May log, `review_seconds` (time on the approval screen): median **19 seconds**, 61% under 30; `fields_edited` is 0 on 93.4% of declarations.
- In `customs/qa-sample-2027-04.csv`, the customs compliance team re-checked 400 April pre-fills against the documents: `material_error` = Y on **28 of 400, 7.0%** (95% interval about 4.9–9.9%). In the same sample, fields accepted without edit are 99.1% — the vendor's "accuracy" is the share of fields nobody changed, which in a review that takes 19 seconds measures the reviewer, not the model.
- `customs/brokerage-staffing-monthly.csv`: the KPI went from 9 to 12 declarations per agent a day in March; actual output stayed around 9.2 because volume did not grow. The target did not free anyone; it took away the time to check.
- `hs_code_source`: 22.6% of May's tariff codes came from Meches HS Suggest, a second AI nobody evaluated beside the first.

### Step 5 — Test "four regions live"

In `operations/route-daily-by-depot.csv`, divide `routes_dispatched_as_planned` by `routes` per region and month. North runs at 0.68–0.72 from December; South at 0.35 in January, 0.25 in February, then zero; Centre zero from April (planner view only); Europe zero throughout. In the South, `late_stops` / `stops` is 4.0% before, **8.0%** with the tool and 3.9% after the pull-back. In the North, Kiryat Shmona overrides 56% of plans, and `operations/dispatcher-overrides-2027.csv` says why in five languages — "כביש 899 סגור", "منطقة عسكرية مغلقة", "Дорога закрыта", "Road closed, detour via Rt 85". The model card (`ai/tzir-route-model-card.md`) says the model learned from January 2021 to June 2023 traffic and adapts "once the telematics feed has been validated"; the tickets show the feed failing every night since 14 November. The dashboard's "310 active drivers" is licensed seats; `it/licence-usage-2027-05.csv` shows 107 of 334 seats active.

### Step 6 — Licences, invoices and the money

Join `finance/ap-invoices-ai.csv` (May) to the licence export: Ayin Drive (₪18,000), Nezek Vision (₪22,000) and the quote add-in (₪9,500) were invoiced in May for zero active users; Kotev Assist has 112 active of 450. `finance/ai-programme-cost-2027.csv`: ₪7.51M actual and forecast against ₪5.2M budgeted (+44%), of which ₪2.09M is the customer-portal assistant budgeted as "funded from AI savings". Eight contracts in `vendor/contracts-ai.csv` name the former lead as business owner.

### Step 7 — People: hear the grievance, don't run a hunt

`people/works-committee-letter-2027-03-03.md` (Hebrew, with HR's translation) and clause 14 of the collective agreement: cameras and a driver score introduced without the 30 days' notice and consultation the clause requires, and a driver summoned to a hearing on the score's data. The ticket of 23 February shows the data request. Whether clause 14 was breached and what follows for anyone is HR's and counsel's. What you need from the people is different: what drivers and dispatchers would keep, and on what terms. The Privacy Protection Authority treats location data about employees as a significant intrusion, allowed for an essential purpose, proportionately and transparently; cameras at work have their own guideline (5/17). You cite them so HR knows what to check, not to rule.

Interview: [Dmitri Volkov](../../labs/module-17/personas/dmitri-it-security.md), [Rania Haj-Yahia](../../labs/module-17/personas/rania-south-ops.md), [Tesfaye Worku](../../labs/module-17/personas/tesfaye-works-committee.md), [Svetlana Morozov](../../labs/module-17/personas/svetlana-cfo.md), [Yaniv Sasson](../../labs/module-17/personas/yaniv-tzir-vendor.md) and [Itai Barkan](../../labs/module-17/personas/itai-former-ai-lead.md) (once). Each has a transcript in [`transcripts/`](../../labs/module-17/personas/transcripts/); run yours through the [coach prompt](../../labs/common/coach-prompt.md).

### Step 8 — Write the findings memo, labelled

Use the [findings memo](../../templates/findings-memo.md) and [02.7](../module-02/lesson-07.md). Answer first, then one section per claim the work tests. Label every number **M** (measured from Vantage's own data), **R** (reported by a person) or **C** (claimed by a vendor or a document). End with what you did not look at and who owns it. Send it to both principals the same day.

## Watch out

- **Holding the incident for the memo.** The post-fix mismatches and the 2,462 records are a same-week finding. Status note to both principals and facts to counsel now; the memo can follow.
- **Counting the register.** Eight rows is what one person chose to list. AI arrives in ERP modules, vendor releases and card lines.
- **Quoting "accuracy" without its definition.** Ask what the denominator is: here it is fields nobody edited, in a review that takes 19 seconds.
- **Calling the South "resistance".** The South's late stops doubled with the tool and recovered without it. The people who pulled it back are your best witnesses.
- **Turning the hearing into a hunt.** You need the fact that monitoring data was used on a person; who did it and what follows is HR's and counsel's.
- **Wasting the one call.** If the former lead's call is spent on why he left, the warning he gave stays hidden.
- **Leaving the vendor's numbers unlabelled.** Every vendor figure in your memo carries a C until something of Vantage's confirms it.

## Your turn

### Inputs

- The [data room](../../labs/module-17/data-room/INDEX.md) (module download): `customs/`, `portal/`, `incident/`, `operations/route-daily-by-depot.csv`, `operations/dispatcher-overrides-2027.csv`, `it/`, `finance/`, `vendor/`, `people/`, `ai/`.
- Personas: at least four of [Dmitri](../../labs/module-17/personas/dmitri-it-security.md), [Rania](../../labs/module-17/personas/rania-south-ops.md), [Tesfaye](../../labs/module-17/personas/tesfaye-works-committee.md), [Svetlana](../../labs/module-17/personas/svetlana-cfo.md), [Yaniv](../../labs/module-17/personas/yaniv-tzir-vendor.md) and the one call with [Itai](../../labs/module-17/personas/itai-former-ai-lead.md), or their [transcripts](../../labs/module-17/personas/transcripts/); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [interview guide](../../templates/interview-guide.md), [AI inventory](../../templates/ai-inventory.md), [findings memo](../../templates/findings-memo.md).
- Track B: `labs/module-17/discovery.py` (module download).

### Steps

1. Write the interview plan: order, the safety line for each of the three people who have reasons to stay quiet, and the three or four questions for the one call.
2. Build the inventory: register against licences, contracts, cards, proxy and tickets. Apply the counting rule.
3. Test the incident record: mismatches by version and submission; cross-customer opens, documents, viewers and records, before and after 19 May; customs queries. Write the one-page status note for both principals and the list of facts for counsel.
4. Measure the review: seconds, edits, the QA error rate with its interval, the KPI, the second tariff-code source.
5. Test "four regions live": dispatch share by region and month, South late stops, overrides by depot and reason; the model's training period and the feed.
6. Join invoices to licences; total the programme's cost against its budget.
7. Run the interviews; then write the findings memo with every number labelled M, R or C.

**Track B (Python).** `python discovery.py` prints sections 1–7 above from the raw files, and `python discovery.py --llm` adds an LLM reading of the 994 override reasons, which dispatchers wrote in Hebrew, Arabic, Russian, Amharic and English and left uncoded 42 times: the model labels each free text, and the script reports the labels for the uncoded ones and the agreement with the dispatchers' own codes. Python is worth it here because the incident scope is a join of three exports that must be re-run, with identical rules, every time the vendor sends a new log or another mismatch appears — a spreadsheet pivot done once on 7 June is already out of date on 10 June.

### Time

150 minutes: 15 for the plan, 20 for the inventory, 35 for the incident and the status note, 15 for the review, 15 for the routes, 10 for the money, 40 for the interviews and the memo.

### Done when

- [ ] The inventory lists every AI system with its source, including those outside the register, and keeps the vendor's dashboard out of the count.
- [ ] The incident's scope is stated in numbers (mismatches, submitted, post-fix, opens, documents, customers, records, queries), compared line by line with the record, and was sent to both principals and counsel within the week.
- [ ] The review step is measured in seconds and edits, and the vendor's accuracy is replaced by the re-checked error rate with its interval.
- [ ] "Four regions live" is tested by region and month with dispatch share and late stops.
- [ ] The memo labels every number M, R or C and says what you did not look at and who owns it.
- [ ] Nobody you interviewed is named in the memo as the cause of anything.

<details><summary>Reference answer</summary>

The full memo is `labs/module-17/expert/02-findings-memo.md` (module download). The numbers that carry it, all reproducible with `discovery.py`:

**Answer first:** twelve AI systems run, not seven; the route tool is used in one region of four; about ₪0.76M a year of the ₪6.2M booked can be evidenced; the programme will cost about ₪7.51M against ₪5.2M; the incident is not closed.

**Incident (M):** 70 mismatched declarations — 63 under 4.2.0 (3–20 May), 7 under 4.2.1 (23 May – 3 June); 47 submitted (42 + 5); 21 declaring customers, 24 document owners. Portal: 30 cross-customer opens of 22 documents by users of 12 customers, 6 after 19 May via the portal file page. 7 Shuk Online B2C manifests opened: 2,462 records (1,870 before 19 May, 592 after). 9 customs queries on mismatched declarations, 3 shipments held (Gefen's), all open past their requested dates. Gefen: 11 of the 70 were its declarations (7 submitted); 7 of its documents were attached to others' files, 3 opened by others. Status note sent Thursday 10 June; counsel briefed Tuesday 8 June and Monday 14 June.

**Review (M):** median 19 s on the approval screen, 61% under 30 s, 93.4% with no field edited; QA 28/400 = 7.0% material errors (CI 4.9–9.9%) vs "99.2% accuracy" = 99.1% of fields not edited; KPI 9 → 12, output 9.2; 22.6% of tariff codes from HS Suggest.

**Routes (M):** dispatched as planned, May: North 0.68, Centre 0, South 0, Europe 0; South late stops 4.0% / 8.0% / 3.9%; North overrides 29%, Kiryat Shmona 56%; model trained on 2021–June 2023; feed failing since 14 November; 107 of 334 seats active.

**Outside the register (M):** Smart Match, HS Suggest, the CS triage on n8n + Promptway (₪6,333 on a card January–May; 20,074 requests, 231 MB uploaded in nine weeks), a free translator (10,416 requests, 818 MB from customs).

**Money (M):** May invoices for zero users: Ayin ₪18,000, Nezek ₪22,000, quote add-in ₪9,500; Kotev 112/450; ₪7.51M vs ₪5.2M.

**What the transcripts missed:** Dmitri was not asked for the logs after 21 May or whether the portal page still showed attachments, so "contained" survived the interview; Rania was asked about discipline ("an HR question") but not how the deck came to say four regions, so the COO's e-mail stayed hidden; Tesfaye was asked what drivers would need without a commitment to consult first, so the committee's terms stayed hidden; Svetlana was not asked how the board version of the savings table was prepared, so her dropped caveat stayed hidden; Yaniv was never told about reducing regions, so his offer designed to pass the notice date never surfaced; the call with Itai found the 14 April warning but not how the order forms were split.

</details>

## References

- IAPP, [The new Israeli data security regulations: a tutorial](https://iapp.org/news/a/the-new-israeli-data-security-regulations-a-tutorial): a database owner reports a serious security incident immediately; notifying data subjects is at the regulator's request. Amendment 13 has changed the law since: counsel works from the current text.
- Pearl Cohen, [Draft PPA guidelines on privacy law and AI](https://www.pearlcohen.com/israel-new-draft-guidelines-on-the-application-of-privacy-law-to-ai/) (May 2025): management responsibility, transparency, security of AI systems. A draft.
- Kol Zchut, [Employee privacy at work](https://www.kolzchut.org.il/he/%D7%A9%D7%9E%D7%99%D7%A8%D7%94_%D7%A2%D7%9C_%D7%A4%D7%A8%D7%98%D7%99%D7%95%D7%AA_%D7%94%D7%A2%D7%95%D7%91%D7%93%D7%99%D7%9D_%D7%91%D7%9E%D7%A7%D7%95%D7%9D_%D7%94%D7%A2%D7%91%D7%95%D7%93%D7%94) (Hebrew): workplace cameras (guideline 5/17), location data of employees.
- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting): verified vs reported evidence (named, not re-taught).
- Field kit: [01.6 · The shadow-AI census](../module-01/lesson-06.md), [01.7 · The AI inventory from zero](../module-01/lesson-07.md), [02.2 · The discovery interview](../module-02/lesson-02.md), [02.4 · Measuring a baseline from exports](../module-02/lesson-04.md), [02.7 · Writing a findings memo](../module-02/lesson-07.md), [07.5 · When it goes wrong](../module-07/lesson-05.md).
- Templates: [interview guide](../../templates/interview-guide.md), [AI inventory](../../templates/ai-inventory.md), [findings memo](../../templates/findings-memo.md).
- Earlier: [17.1 · The call](lesson-01.md). Next: [17.3 · Diagnosis](lesson-03.md).
