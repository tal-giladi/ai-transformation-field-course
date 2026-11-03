---
id: "12.3"
module: 12
minutes: 18
practice_minutes: 150
prerequisites: ["12.2", "03.1", "03.3", "03.7", "03.9"]
objectives:
  - "Build a baseline sheet by billing type, in which every number has a definition, a source and a label, including the one nobody has measured yet."
  - "Net a vendor's productivity slide the way a law firm's finance director will: capacity versus cash, hourly versus fixed fees, and the customer's share at renewal."
  - "Map and screen the candidates, including the platform you were asked about, and name the ones that are policy or pricing work, not AI."
  - "Write a one-page case for the first exit point with one decision asked, its cost and what a no means."
volatility: implementation
sources:
  - title: "Bank of Israel, representative exchange rate API (US$ = ₪3.136, 2 November 2026)"
    url: https://boi.org.il/PublicApi/GetExchangeRate?key=USD
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): fast screen, net the claim, the customer's share, decision-ready case"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "NatLawReview on ABA Formal Opinion 512 (29 July 2024): efficiencies from generative AI should be reflected in fees; no billing for learning a tool"
    url: https://natlawreview.com/article/american-bar-association-issues-formal-opinion-use-generative-ai-tools
last_verified: "2026-11-02"
---

# 12.3 · Diagnosis

You know what the firm does and what it already uses. Now you find out what AI would do to its money, which depends less on the tool than on how each piece of work is billed. In this lesson you build a baseline sheet by billing type, net the "₪23.3M" slide with the finance director's questions, map and screen the candidates, and write the one-page case for the 3 December readout, where either side may stop. At the end you have a baseline sheet, a netted claim, a shortlist and a one-page case.

## The situation

Thursday 26 November 2026. The findings memo is with Yoav. On Monday 16 November you met Eli Ben-Hamo, the finance director ([persona](../../labs/module-12/personas/eli-finance-director.md), [transcript](../../labs/module-12/personas/transcripts/eli-finance-director.md)). On Tuesday 1 December you meet Shmuel Atlas ([persona](../../labs/module-12/personas/shmuel-founding-partner.md), [transcript](../../labs/module-12/personas/transcripts/shmuel-founding-partner.md)), who leads the "no" camp. On Thursday 3 December the management committee hears your diagnosis.

IBM's consulting certificate teaches you to *net the claim* across the parties who pay for it and to count *the customer's share of the gain*. Module 3 turned that into the [ROI model](../../templates/roi-model.md) ([03.7](../module-03/lesson-07.md)). A law firm is the cleanest example you will meet of why it matters: the product the firm sells is the hour.

## What to do

### Step 1 — Baselines by billing type

The same saved hour means three different things here. On an **hourly** matter it is a fee not billed. On a **fixed-fee** matter it is margin. On a **capped** matter it is either (fees under the cap fall; hours over the cap were written off anyway). So every baseline is split by billing type. Use the [task inventory](../../templates/task-inventory.md) idea from [02.3](../module-02/lesson-03.md), one row per number:

| # | Measure | Value | Definition and source | Label |
|---|---|---|---|---|
| B1 | Research share of associate hours | 25.2% (coded RES 6.2%) | Narrative flag, `time-entries-2026-q3.csv` (3 groups) | measured |
| B2 | Research hours a year, whole firm | ≈ 25,700 | B1 × associates' 2026 hours, + partners at 5.1% | directional |
| B3 | Research by billing type | hourly 56.8%, fixed 24.0%, capped 14.5%, retainer 4.7% | Narrative flag × `billing_type` | measured |
| B4 | Research hours billed after write-offs (non-fixed) | 80.4% | `billed_hours` ÷ `hours` | measured |
| B5 | Associates' hours against target | 81%; 1 of 64 on target | `lawyers.csv`, Jan–Sep annualised | measured |
| B6 | Fixed fees: worked value over fee, 2025 | Tech & IP +38.1%; other groups 1–10% | `matters.csv` | measured |
| B7 | Fees per hour on Carmel's NDAs | ₪860 (2024, hourly) → ₪1,422 (2026, fixed ₪1,150 per NDA) | `carmel-nda-workstream.csv` | measured |
| B8 | Time to check one citation by hand | ≈ 10 minutes | Interviews | reported |
| B9 | Research time saved by a tool, net of checking | **not known** | — | to measure (12.5) |

B9 is the number every slide assumes and nobody has. Write it down as missing. The pilot in 12.5 exists to measure it.

### Step 2 — Learn the customer's share from the firm's own history

The firm has already run this experiment once. In 2025 Corporate and Tech & IP automated Carmel Retail Group's NDA template. Open `clients/carmel-nda-workstream.csv` and total by year:

| Year | NDAs | Hours per NDA | Fee per NDA | Fees | Fees per hour |
|---|---|---|---|---|---|
| 2024 | 461 | 2.38 | ₪2,046 | ₪943,250 | ₪860 |
| 2025 | 507 | 1.26 | ₪1,119 | ₪567,210 | ₪890 |
| 2026 (Jan–Oct) | 452 | 0.81 | ₪1,150 | ₪519,800 | ₪1,422 |

Read it as a story in three acts. In 2025 the work got faster and, billed by the hour, the fees fell with the hours: the client received the whole gain without asking. At the November 2025 renewal Carmel asked for a fixed ₪900 per NDA, citing the turnaround, and settled at ₪1,150 (`renewals-and-rate-negotiations.csv`). In 2026 NDA fees are about a third below 2024 although Carmel sends more NDAs, but the firm earns ₪1,422 an hour on them instead of ₪860. The client took most of the gain; the fixed price let the firm keep some. Eli's line from the interview: "Nobody noticed, because nobody looks per hour."

That is the planted lesson of this engagement: **faster turnaround gets renegotiated at renewal.** The renewals log shows it twice more (an employment retainer cut because "your templates are automated now", a start-up package cut after "faster turnaround"), a litigation panel lost to a competitor with fixed fees about 30% lower, and one open request: Carmel wants 15% off hourly rates from 2027.

### Step 3 — Net the slide

Noa's slide: "6.2 h × 90 lawyers × 44 weeks × ₪950 = ₪23.3M of capacity for ₪0.4M." Net it in four moves, in front of finance, not behind it:

1. **The hours.** 6.2 hours a week was self-reported by another vendor's customers at US and UK firms. Replace it with your own: research is about a quarter of associate time (B1), and B9 is unknown. Use an assumed saving and say so (30% net of checking, for the model).
2. **Capacity is not cash.** With associates at 81% of target (B5), freed hours have no buyer. Show them in hours.
3. **Hourly work loses fees.** Each research hour saved on billable work removes about ₪814 of fees (₪1,013 average associate rate × 80.4% billed).
4. **The customer takes a share.** Price it, using the firm's own history (Step 2) and the open request.

The model in the module download (`roi_model.py`, Track B; its results are in `roi-revised.csv` for Track A) does the arithmetic. If the firm signs 90 seats and changes nothing about billing, year 1 at a 30% saving and 60% adoption:

| Line | Year 1 |
|---|---|
| Research hours saved | 4,634 |
| Fees lost on billable work | −₪2,417,502 |
| Freed hours (capacity, not cash) | 1,666 |
| Customer's share (Carmel's 15% conceded) | −₪648,794 |
| Librarian to keep a whole-DMS index usable | −₪240,000 |
| Licence and set-up at ₪3.136 per US$ | −₪403,540 |
| **Net cash** | **−₪3,709,836** |
| Against doing nothing (where Carmel's 15% is also conceded) | −₪3,061,042 |

The sensitivity matters more than the point estimate: from −₪2.45M (a 20% saving and half the freed hours sold) to −₪4.5M (a 40% saving, none sold). No plausible input makes it positive while billing stays hourly. That is not an argument against AI. It is an argument that the decision is about pricing as much as about tools.

[Simulation: ROI defender](../../simulations/roi-defender/index.html?preset=harbor)

The simulation is set at Harbor & Pine, a different company, but the moves are the ones you just made: net each claim across the sponsor, the receiving team, control capacity and the customer's share, and keep capacity apart from cash.

### Step 4 — Map and screen the candidates

Use the [opportunity map](../../templates/opportunity-map.md) and the seven-question screen ([03.3](../module-03/lesson-03.md), [use-case scorecard](../../templates/use-case-scorecard.md)). Include the platform you were asked about; screen it like the rest.

| Candidate | What it is | Screen |
|---|---|---|
| Interim AI rule + one enterprise assistant | Policy and a tool under a written agreement | **Go** |
| Curate the research corpus and the 300 most-used precedents | Knowledge work, no AI | **Go** (it is the data gate for anything that searches the bank) |
| Precedent search over the curated corpus with a citation gate | Retrieval, rules and a reader | **Go with a condition**: curated corpus only; consent position from the ethics partner |
| Fixed-price packages for repeat work (Carmel first) | Pricing, no AI | **Go** |
| Parshan, 90 seats, before 31 December | Platform | **Stop for now**: fails the data gate (whole-DMS index, walls), the economics, and has no test on the firm's own material in Hebrew |
| AI-assisted document review in litigation disclosure | Classification over the firm's own documents | **Later**, with its own test (Shmuel would accept it) |

Two candidates on the shortlist are not AI at all. That is normal in this course and it is the point: the knowledge base and the price list decide whether any tool makes money.

### Step 5 — Talk to the sceptic before the committee

Meet Shmuel on 1 December. Do not argue the tool. Bring his own group's numbers (research written off on his matters more than anywhere else; the lost tender in the renewals log) and ask where he would accept help. His transcript shows how much he concedes when the questions are about the work. What you want from him: his conditions (a person checks every source; associates keep learning research), not his vote.

### Step 6 — The one-page case for the exit point

Use the [decision-ready case](../../templates/decision-ready-case.md) from [03.9](../module-03/lesson-09.md). One decision asked, its cost, what a no means, and what it does not promise. On 3 December the committee may stop the engagement; your page must make continuing a real choice, not a formality.

## Watch out

- **Hours × rate.** The slide's error is common because it feels like money. In a firm without a backlog, saved hours are capacity; on hourly matters, they are fees you will not bill.
- **Ignoring the customer.** Clients read the same articles as partners. The firm's own NDA history shows the share is taken, so price it before the client prices it for you.
- **"Fixed fees solve it."** Only if the price is set before the hours fall, and only on work the client agrees to buy that way. Disputes stay hourly.
- **A single ROI number.** Show the sensitivity and the assumed inputs. Eli will move the saving and the resale share himself; let him find the conclusion holds.
- **Screening the platform out by taste.** Screen it on the same seven questions; it fails on evidence (data gate, economics, Hebrew), not because a partner dislikes it.
- **Forgetting compensation.** If partners are paid partly on their own billed hours, the hourly-practice partners lose most from the tool. You do not fix pay, but you say in private why the vote splits.

## Your turn

### Inputs

- Data room (module download): `billing/time-entries-2026-q3.csv`, `billing/matters.csv`, `people/lawyers.csv`, `clients/carmel-nda-workstream.csv`, `clients/renewals-and-rate-negotiations.csv`, `clients/clients.csv`, `firm/finance-summary-2026.md`, `firm/partners-meeting-2026-10-22-minutes.md`, `vendor/parshan-demo-deck.md`.
- `roi_model.py` and `roi-revised.csv` (module download, `labs/module-12/`).
- Personas: [Eli](../../labs/module-12/personas/eli-finance-director.md), [Shmuel](../../labs/module-12/personas/shmuel-founding-partner.md), and their [transcripts](../../labs/module-12/personas/transcripts/eli-finance-director.md).
- Templates: [ROI model](../../templates/roi-model.md), [opportunity map](../../templates/opportunity-map.md), [use-case scorecard](../../templates/use-case-scorecard.md), [decision-ready case](../../templates/decision-ready-case.md).

### Steps

1. Build the baseline sheet (at least eight rows) with definition, source and label, including the missing B9.
2. Total the NDA workstream by year and write the three-act story in five lines.
3. Net the slide in four moves; build the year-1 table for "sign 90 seats, billing unchanged" and a three-by-three sensitivity.
4. Map and screen at least five candidates, including Parshan; mark which are not AI.
5. Interview Eli and Shmuel (roleplay or transcripts) and note what each would need to believe your case.
6. Write the one-page case for 3 December.

**Track B (Python).** `python roi_model.py` prints the inputs with their labels, the year-1 ledgers for doing nothing, scenario A and scenario B, and A's sensitivity; `python roi_model.py --saving 0.2 --resale 0.25` reruns it. Python is worth it because Eli will ask "and if…?" five times, and every answer must come from the same arithmetic.

### Time

150 minutes: 30 for the baseline sheet, 15 for the NDA story, 40 for netting and sensitivity, 20 for the map and screen, 25 for the interviews, 20 for the one-page case.

### Done when

- [ ] Every baseline has a definition, a source and a label; the net research time saved is marked unknown.
- [ ] The NDA history is told with fees, hours and fees per hour, and named as the customer's share.
- [ ] The slide is netted in four moves; capacity appears in hours, never as cash; the sensitivity is shown.
- [ ] Parshan is screened on the same questions as the other candidates; at least two candidates are not AI.
- [ ] The one-page case asks one decision, costs it, and says what a no means and what it does not promise.

<details><summary>Reference answer</summary>

The full version is `labs/module-12/expert/03-baselines-and-shortlist.md`.

**Baseline sheet (excerpt):** B1 research 25.2% of associate hours (coded 6.2%), measured; B2 ≈ 25,700 research hours a year, directional; B3 hourly 56.8 / fixed 24.0 / capped 14.5 / retainer 4.7%, measured; B4 80.4% billed; B5 81% of target, 1 of 64; B6 Tech & IP fixed fees +38.1%; B7 ₪860 → ₪1,422 per hour on NDAs; B8 ≈ 10 minutes per citation, reported; B9 not known.

**Slide netted:** 6.2 h is self-reported elsewhere; capacity has no buyer at 81% of target; ≈ ₪814 of fees per research hour saved on billable work; the customer's share priced from the NDA history and the open 15%. Year 1, 90 seats, billing unchanged: −₪3,709,836 net cash; −₪3,061,042 against doing nothing; sensitivity −₪2.45M to −₪4.5M.

**Shortlist:** interim rule + enterprise assistant (go); curation (go, not AI); precedent search with a citation gate over the curated corpus (go with condition); fixed-price packages for repeat work (go, not AI); Parshan 90 seats before 31 December (stop for now); disclosure review in litigation (later).

**One-page case, decision asked:** continue to phase 2 on this basis: no platform contract in December, an interim rule drafted for counsel, curation of the 78 research documents now, a two-group pilot with a citation gate, a fixed-price proposal for Carmel's repeat work. Cost: ₪96,000 phase fee, up to ₪40,000 tooling, two associates at half time for about four weeks. A no means the discount drives a two-year decision without a test on the firm's material, and consumer use continues on client documents. It does not promise more revenue in 2027.

**What the transcripts' interviewers missed:** Eli was never asked for his own Parshan model (there is none: the budget line is a cost only); Shmuel was never asked, without blame, how memos are checked, so his approval of the October memo stayed hidden.

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting): fast screen, net the claim, the customer's share, decision-ready case (named, not re-taught).
- US context only: NatLawReview's summary of [ABA Formal Opinion 512](https://natlawreview.com/article/american-bar-association-issues-formal-opinion-use-generative-ai-tools) (29 July 2024): efficiencies should reach clients through fees, and a lawyer may not bill to learn a tool. It binds no Israeli lawyer; it shows where clients' expectations come from. Israeli billing questions go to the ethics partner (12.4).
- Bank of Israel, [representative exchange rate](https://boi.org.il/PublicApi/GetExchangeRate?key=USD) (₪3.136 per US$, 2 November 2026).
- Field kit: [03.1 · Opportunity map](../module-03/lesson-01.md), [03.3 · The fast screen](../module-03/lesson-03.md), [03.7 · The ROI model that survives finance](../module-03/lesson-07.md), [03.9 · The decision-ready case](../module-03/lesson-09.md).
- Templates: [ROI model](../../templates/roi-model.md), [opportunity map](../../templates/opportunity-map.md), [use-case scorecard](../../templates/use-case-scorecard.md), [decision-ready case](../../templates/decision-ready-case.md).
- Simulation: [ROI defender](../../simulations/roi-defender/index.html?preset=harbor) (Harbor & Pine scenario).
- Earlier: [12.2 · Discovery](lesson-02.md). Next: [12.4 · The hard part](lesson-04.md).
