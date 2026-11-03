# 05 · Portfolio triage and the 12-month scale plan

*For the Management Committee, Monday 15 March 2027. Reproducible with `python triage.py` (rules in the script's header); a person reviewed every line.*

## 1. Triage of the 43 rows

| Action | Builds | Rows | 2027 unit lines released |
|---|---|---|---:|
| **Clean** (same build, listed twice) | 3 | OPS-04 (= MTG-01), PRV-03 (= TRS-01), OPS-05 (= FIN-02) | ₪420,000 |
| **Stop** | 10 | RET-02, MTG-02, MTG-04, CRD-04, PRV-01, PRV-02, CMP-02, CC-03, DIG-01, HR-01 | ₪1,560,000 |
| **Merge** (second build retired, one owner serves both units) | 4 | RET-01 → CRD-01, SME-01 → CORP-01, SME-02 → CMP-01, DIG-02 → CC-01 | ₪760,000 (merge work ₪180,000) |
| **Route** (keep, through the tier route) | 26 | low 12, medium 8, high 6 | — |

### Why each stop (the evidence, not the opinion)

| Build | Evidence | Who decides, what happens |
|---|---|---|
| RET-02 Next-best-offer | Uplift test never run; compliance question on purpose of use of transaction data open since October | Hagit; the question stays with Lina and the DPO if it returns |
| MTG-02 Valuation sanity check | False-accept 0.18 against 0.05; uses a 2023 price-index snapshot | Rachel; manual check continues |
| MTG-04 Broker email drafts | No users since August; no test set | Rachel; Katvan AI notice by 15 March |
| CRD-04 Chargeback summaries | The rules engine already summarises the case (Karim agrees) | Karim |
| PRV-01 Client letters | 2 users, no test set | Michael; Katvan AI notice by 15 March |
| PRV-02 Portfolio commentary | 14% factual errors on holdings against 2%; owner left in September; suitability wording never reviewed | Michael, with Lina |
| CMP-02 AML alert triage | False negatives 9% against 1%; 11 true positives auto-closed in the labelled set | Samer, with Lina; the 11 alerts re-opened |
| CC-03 Complaint routing | Accuracy 0.61 against 0.85 | Revital |
| DIG-01 Customer chatbot | 0.76 against 0.90; wrong on 2026 fees; Arabic answered in Hebrew; live on 2% without approval | Tom; A/B switched off on 16 March; a new case may return through intake |
| HR-01 CV screening | Selection-rate ratio by home town 0.62 against 0.80; features include home town and graduation year; contract renewed without a DPA | Anat, with counsel on the contract and on equal opportunity |

Each stop gets the decommissioning checklist from 07.2 (people told what replaces it, access removed, data returned or deleted with written confirmation, contract notice, records updated, a check after 30 days).

### Merges

| Task | Kept build and owner | Retired build | Evidence | Merge work |
|---|---|---|---|---|
| Complaint summaries | CRD-01, Bahir, owner Maya Elkayam (Cards) | RET-01 Mishov (notice given 28 Jan) | 0.91 on 300 of the bank's complaints in four languages vs the vendor's own 90% | Retail's channels and themes added; branch complaints from Q3 |
| Credit memo drafting | CORP-01, Pinkas, owner Daniel Friedman | SME-01 (contractor POC ended 31 Dec) | 0.97 on 120 memos vs no test set | SME memo template |
| KYC document checks | CMP-01, Imut Docs, owner Samer Khoury | SME-02 Mismach Check (notice before June) | 0.96 on 250 vs 0.89 on 90; licence covers business customers | SME document types |
| Conversation summaries | CC-01, Kolot, **one** owner Revital Cohen | DIG-02 Bahir chat summaries | 0.89 on 200 (Arabic 0.81: fix before medium sign-off) vs spot check | Chat channel; Kesher macro reviewed by IT; Retail's branch-call request served from it later |

### The 26 kept builds, by tier

- **Low (12):** RET-03 Branch FAQ, MTG-03 Mortgage FAQ, CRD-03 Dispute letters, CORP-02 RM briefs, TRS-01 Market summaries (fix: baseline), OPS-01 Assistant, OPS-02 Procedure assistant, CC-02 Knowledge assistant, DIG-03 In-app search, HR-02 HR FAQ, FIN-01 Variance commentary, FIN-02 Invoice matching.
- **Medium (8):** RET-04 Churn early warning, MTG-01 Document extraction, CRD-01 Complaint summaries, CRK-02 Covenant extraction, CMP-01 KYC checks, OPS-03 Reconciliation, CC-01 Call summaries (fix: one owner), FIN-03 Expense audit sampling.
- **High (6):** CRD-02 Fraud triage, SME-03 SME pre-approval (backtest on 2024 data, before the rate changes: re-test on 2026 data before validation), CORP-01 Credit memo, TRS-02 Surveillance, TRS-03 Liquidity, CRK-01 Early-warning signals (in validation since September 2026).

**Patterns, not duplicates:** five Q&A-over-documents builds (RET-03, MTG-03, OPS-02, CC-02, HR-02) are the same pattern on different content: one template and one platform pattern, five owners. Merging them would lose the owners who keep the content current — the Branch FAQ's fee error was a content-ownership failure, not a model failure.

**The assistant:** kept. OPS-02 and CC-02 run inside it (agent studio, indexes deleted 30 days after the subscription ends). The rollout is staged: the 380 onboarded first, branches trained from April with the Arabic and Russian letter template, the rest by September. Condition agreed with the CFO: weekly active users at least 50% of assigned seats by 30 September, or the seat count is cut to use.

## 2. The 12-month plan (April 2027 – March 2028)

| Quarter | Operating model | Portfolio | In production (cumulative, approved route) |
|---|---|---|---|
| Q2 2027 | Policy v2 to the Board Risk Committee (20 April); hub hiring (10); catalogue v1 by 31 May; validation contractor April–September; CCO corrects the survey answer through liaison in April; shadow route closes 31 March | Stops and decommissioning complete by 30 June; merges start; Katvan AI notices; Kesher renewal with AI features off by default | 2 by 30 June: CRD-03 dispute letters, FIN-02 invoice matching (low, interim controls on the sandbox moved to production terms) |
| Q3 2027 | Platform live (September); evaluation kit and templates v1; spokes' AI leads named | Low-tier wave on the platform; Arabic fix for CC-01 | 5 by 30 September: + RET-03, OPS-02, CC-02 |
| Q4 2027 | Second evaluator; first full quarter of the three numbers | Medium-tier standard reviews start | 10 by 31 December: + OPS-01 (full rollout), MTG-03, HR-02, FIN-01, CRK-01 (validated) |
| Q1 2028 | Policy review; re-plan 2028 | High-tier queue ordered | 14 by 31 March: + CRD-01, CMP-01, CC-01, CORP-01 |

The other 12 (CORP-02, TRS-01, DIG-03; RET-04, MTG-01, CRK-02, OPS-03, FIN-03; CRD-02, SME-03, TRS-02, TRS-03) have dates in Q2–Q4 2028 in the catalogue. The simulation's expert run reaches 26 by the end of 2027 because it has no procurement, DPIA or works-committee time; this plan commits to 14 (educational model vs plan).

**Gates (yes/no, not dates):** no low-tier go-live without a catalogue entry and a passed kit; no medium without the hub's sign-off and, where personal data, the DPO's DPIA decision; no high without the Model Committee; no build with two owners.

## 3. The money (2027)

| | Board's design | Proposed |
|---|---:|---:|
| Central team | 4,800,000 (16) | 3,200,000 (hub, 10) |
| Validation capacity | 1,800,000 | 1,800,000 |
| Validation contractor (six months) | — | 350,000 |
| Platform build + run (on IT's landing zone) | in the production fund | 2,400,000 + 600,000 |
| Templates and evaluation kit | — | 320,000 |
| Catalogue | — | 225,000 |
| Reorganisation (job descriptions, spoke training) | — | 300,000 |
| Production fund / run of go-lives | 2,600,000 | 500,000 |
| Tools, training, contingency | 1,800,000 | 300,000 |
| **Central programme** | **11,000,000** | **9,995,000** |
| Unit AI lines | 9,130,000 | 6,570,000 (after stop, merge, clean; + merge work) |
| **All AI spend** | **20,130,000** | **16,565,000** |
| Saving against the CFO's ₪3,020,000 | — | **₪3,565,000**, assistant kept |

Labels: unit lines and the assistant are measured from the register and contracts; the central lines are the plan's estimates (directional); the platform's split with IT's capex is assumed until Nir confirms.
