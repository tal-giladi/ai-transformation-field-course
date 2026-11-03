# 05 · Stop/keep audit, incident closure and the decisions that could not wait

*Prepared 27–30 June 2027 for Ofer Lavi and Dr. Ilana Shaked; the audit table is `audit.py`'s output (module folder), checked by hand. Sent with the pre-read on Thursday 1 July.*

## Part A — the stop/keep audit

Nineteen lines: twelve AI systems by region or feature, and the vendor's dashboard. Rules from paper 04. Cost = May invoice; "saving" starts on the date the contract allows.

| Line | ₪ a month | Billed / active | Rule | Action | Owner | Contract step | Saving from |
|---|---|---|---|---|---|---|---|
| Route North | 36,760 | 110 / 102 | R4 | **Keep and fix**: feed, retrain on 2024–27 data, closures in the console, no driver score | Fadi Khatib | Retraining is in the order form | — |
| Route Centre | 29,100 | 78 / 5 | R3 | **Reduce** to 5 planner seats | Gal Rosen | MSA 7.4 notice by 1 Jul | 1 Oct (₪23,600/mo) |
| Route South | 33,280 | 98 / 0 | R3 | **Stop** | Rania Haj-Yahia | MSA 7.4 notice by 1 Jul | 1 Oct (₪33,280/mo) |
| Route Europe | 17,160 | 48 / 0 | R3 | **Stop** | Pieter van Dijk | MSA 7.4 notice by 1 Jul | 1 Oct (₪17,160/mo) |
| Route platform fee | 18,700 | — | R4 | Keep while North runs | Moti Azulay | Unaffected by 7.4 | — |
| Driver score | 0 | all regions | R2 | **Stop** now; written undertaking to the works committee | Moti Azulay | Feature switch | — |
| Tzir Docs | 130,000 | 3 houses | R1 | **Keep with conditions** (below) | Shlomo Peretz | 4.2.2 under 9.3; credits under 11.2 | — |
| Assist, status answers | 95,000 | 1,840 / 612 | R5 | **Keep under test** 90 days: deflection and wrong-answer rate | Ronit Cohen-Elbaz | None before 2029 | — |
| Assist, "my documents" | 0 | — | R1 | **Stop** permanently; remove from the order form | Dmitri Volkov | Written amendment | — |
| Kotev Assist | 42,750 | 450 / 112 | R3 | **Reduce** to 150 seats | Svetlana Morozov | Notice by 1 Oct | 1 Dec (₪28,500/mo) |
| Ayin Drive | 18,000 | 60 / 0 | R2 | **Stop**; 30 days' notice now | Moti Azulay | Notice sent 8 Jun | 1 Aug (₪18,000/mo) |
| Nezek Vision | 22,000 | 25 / 0 | R3 | **Stop**; claim March–August against the SOW end | Hanna Desta | No exit before 31 Aug | — |
| Quote add-in | 9,500 | 30 / 0 | R3 | **Stop**: non-renewal | Ronit Cohen-Elbaz | Notice by 31 Aug | — |
| Warehouse forecast | 6,000 (cloud) | — | R4 | **Keep**; a second person trained, documentation by 30 Sep | Hanna Desta; Lior Gabay | — | — |
| Mishkal Smart Match | in ERP | 6 users | R6→R4 | **Register and keep** | Svetlana Morozov | — | — |
| Meches HS Suggest | in licence | 31 users | R6→R1 | **Register; turn off** until evaluated beside Docs | Shlomo Peretz | Feature flag | — |
| CS e-mail triage (n8n + Promptway) | ≈ 2,000 (card) | CS team | R6→R2 | **Bring in**: approved model route under an agreement; stop the card; no customer documents in prompts meanwhile | Marina Levitan | Procurement | — |
| Free translator | 0 | customs clerks | R6→R2 | **Bring in**: Kotev Assist (sanctioned) for translation; site blocked after 14 days | Shlomo Peretz | — | — |
| Tzir value dashboard | — | — | not AI | **Retire as evidence**; Finance owns the measure | Svetlana Morozov | — | — |

**Totals.** May cost of the audited lines ₪452,250 a month. Savings once in effect ₪120,540 a month; **₪340,620 inside 2027**; the 2027 forecast falls from ₪7.51M to ₪7.17M (budget ₪5.2M). 2028 run-rate about **₪4.86M**: Route ₪0.73M, Docs ₪1.56M, Assist ₪1.14M, Kotev ₪0.17M, forecast cloud ₪0.07M, the AI team ₪1.19M. Docs' minimum commitment (9,000 declarations a month against about 6,200 used) is for the November renegotiation; MSA 7.4 does not cover it.

**Docs conditions (all before resuming outside Gefen's files, and reviewed at day 90, 30 September):** auto-match off for invoice keys without letters until 4.2.2 (consignee cross-check) passes a test on May's 70 mismatches; the supplier invoice shown beside the pre-fill; KPI 9–10 a day; a 5% weekly QA sample by the customs compliance team, material error under 3% for two consecutive months to continue, over 5% in any month to suspend; HS Suggest off; vendor releases to a test tenant first.

## Part B — closing INC-27-0518-01

Following the runbook ([07.5](../../../lessons/module-07/lesson-05.md), [template](../../../templates/incident-runbook.md)).

**1. Reopen and lead.** Reopened Monday 14 June by Dmitri at my recommendation, with Ofer's agreement and Ilana copied. Severity S1: harm reached customers and personal data reached people not entitled to it. Incident lead Dmitri; scribe Noa Peretz.

**2. Contain, narrowest first.** Done 14 June: (a) auto-match off for numeric-only invoice keys (the post-fix cause); (b) the portal file page hides documents whose owner differs from the file's customer; (c) Gefen's files pre-fill off from 21 June at Orit's request. Verified: no mismatches or cross-customer opens from 15 to 29 June in the logs.

**3. Scope from the logs.** 70 mismatched declarations (63 under 4.2.0, 7 under 4.2.1), 47 submitted, 21 declaring customers, 24 document owners. 30 cross-customer opens of 22 documents by 12 customers; 7 Shuk Online manifests, **2,462 records** of private individuals (names, street addresses, phones); 3 Gefen invoices opened by others. 9 customs queries, 3 shipments held, all past their requested response dates.

**4. Escalate with facts, decide nothing legal.** Yael Sharabi briefed on 8 June (first facts) and 14 June (full scope), with: which documents, whose data, which fields, how many records, who opened them and when, whether they can be retrieved (downloaded copies cannot), the database and the vendor's role. She and outside counsel decide whether the event must be reported to the Privacy Protection Authority, when, whether Shuk Online and the people in its manifests are told, and whether any data covered by the GDPR is involved (Vantage Europe's forwarding files use the same portal; the logs do not show where the people in the documents live). Shlomo Peretz (licensed customs agent) and counsel decide how the 47 submitted declarations are checked and corrected with Customs; Shlomo answered the 9 queries by 18 June. **The brief states no legal deadline; it states who decides and when they were briefed.**

**5. Communicate.** Gefen: meeting 21 June, written account 24 June with Ronit and Shlomo named. The other 20 declaring customers and the 23 other document owners: letters drafted for counsel's approval, sent 29 June. Shuk Online: by counsel. No public statement unless counsel advises one; if asked, "a software change by our vendor attached some customers' documents to other customers' files in May; we have stopped it, informed the customers affected and are correcting the declarations concerned."

**6. Root cause, rewritten.** The vendor's RCA ("duplicate supplier invoice numbers") describes the trigger, not the causes. Contributing causes, blameless: (1) a release changed matching logic without the notice MSA 4.3 requires, and Vantage had no way to test vendor releases; (2) matching used the invoice number alone, without the consignee; (3) the human review existed on paper — 19 seconds, a KPI that left no time; (4) the portal showed attachments without checking the document's owner; (5) two early tickets were closed as "data quality"; (6) the incident had no privacy branch, so legal was never asked; (7) "contained" was declared on the vendor's word.

**7. Restore in stages, and the closure criteria.** The incident closes when: no mismatches for 14 days after 4.2.2 (or with auto-match off); every affected customer informed; counsel's decisions recorded with their dates; every submitted declaration checked by the brokerage and corrected where needed; service credits claimed; the change-control step for vendor releases running. **On 1 July, four of six criteria were met; the incident is reported to the board as open, with dates.**

## Part C — decisions that could not wait for the board (decision records)

| Decision | Options | Chosen | Why | Decided by | Date |
|---|---|---|---|---|---|
| Tzir region reduction (MSA 7.4) | Waive this year for the vendor's offer (free 12-month four-region extension + credits); give notice; ask the board on 5 July (too late) | Notice: South and Europe removed, Centre reduced to 5 planners, from 1 October | The offer extends seats nobody uses and passes the notice date; notice keeps every option open (seats can be added later) | Ofer, with Ilana informed | Thu 1 July |
| Ayin Drive | Keep paused and paid; stop | Stop with 30 days' notice | R2; ₪18,000 a month for nothing | Moti | Tue 8 June |
| Driver score | Leave in the app unused; switch off | Off everywhere, written undertaking | R2; the committee's first demand | Moti, with HR | Thu 1 July |
| Gefen pre-fill | Keep; off for Gefen | Off for Gefen until QA evidence | Customer's request; cheap to grant | Shlomo | Mon 21 June |
