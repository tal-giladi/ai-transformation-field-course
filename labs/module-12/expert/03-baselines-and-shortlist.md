# 03 · Baselines, the slide netted, shortlist and one-page case — Atlas & Rowe

For the committee of Thursday 3 December 2026 (exit point 1). Labels: measured / directional / assumed.

## Baseline sheet

| # | Measure | Value | Definition and source | Label |
|---|---|---|---|---|
| B1 | Research share of associate hours | 25.2% (coded RES 6.2%) | Narrative contains research words; time entries Q3, 3 groups | measured (3 groups) |
| B2 | Research hours a year, firm | ≈ 25,700 | B1 × associates' 2026 hours + partners' 5.1% | directional |
| B3 | Research by billing type | hourly 56.8 / fixed 24.0 / capped 14.5 / retainer 4.7% | Same | measured |
| B4 | Research billed after write-off (non-fixed) | 80.4% | billed ÷ worked hours | measured |
| B5 | Associates vs target | 81%; 1 of 64 at target | `lawyers.csv` | measured |
| B6 | Tech & IP fixed fees: hours over fee | +38.1% (2025) | worked value ÷ fee − 1 | measured |
| B7 | NDA fee per hour before / after re-pricing | ₪860 → ₪1,422 | NDA workstream | measured |
| B8 | Stale research documents | 13 of 78 (index marks 2) | corpus vs index | measured |
| B9 | Citations failing a basic check, vendor PoC | 28 of 80 | pilot test set | measured |
| B10 | Time to check one citation by hand | ≈ 10 min | interviews | reported |
| B11 | Research time saved with a tool, net of checking | not known | — | to measure in the pilot |

## The slide, netted

"6.2 h × 90 × 44 × ₪950 = ₪23.3M of capacity for ₪0.4M." Four corrections, in order:

1. **The hours.** 6.2 h a week is self-reported by another vendor's customers. B11 is unknown; the
   research that a search tool touches is about a quarter of associate time (B1), not a fixed 6.2 h.
2. **Capacity is not cash.** With associates at 81% of target (B5), freed hours are not sold.
3. **On hourly work, a saved hour is a lost fee** (B3, B4): about ₪814 of fees per research hour saved
   on billable work (₪1,013 average associate rate × 80.4%).
4. **The customer's share.** Clients re-price when work gets faster (B7): the firm should expect it,
   and price for it.

`roi_model.py`, year 1, at an assumed 30% saving, 60% adoption: signing 90 seats with billing unchanged
loses ≈ ₪3.06M of cash against doing nothing (fees lost ₪2.42M; Carmel's 15% conceded; tools ₪0.40M;
librarian ₪0.24M). Sensitivity: from −₪2.45M (20% saving, half the hours resold) to −₪4.5M (40%, none
resold). No plausible input makes it positive while billing stays hourly.

## Opportunity map and screen (excerpt)

| Candidate | Type | Screen | Note |
|---|---|---|---|
| Interim AI rule + one enterprise assistant | Policy + tool | **Go** | Stops consumer use on client data; no data gate |
| Curate the research corpus and top 300 precedents | No AI | **Go** | The data gate for anything that searches the bank |
| Precedent search over the curated corpus + citation gate | Retrieval + rules + reader | **Go with condition** | Condition: curated corpus; consent position from Orit |
| Fixed-price packages for repeat work (Carmel first) | Pricing, no AI | **Go** | Keeps part of the gain; answers the open renewal |
| Parshan, 90 seats, before 31 December | Platform | **Stop for now** | Fails the data gate (whole-DMS index, walls), the economics, and has no test on firm material in Hebrew |
| AI-assisted document review in litigation disclosure | Retrieval/classification | Later | Shmuel's group would accept it; needs its own test |

## One-page case (front)

**Decision asked on 3 December:** continue to phase 2 on this basis: no platform contract in December;
an interim rule and one enterprise assistant drafted for counsel; curation of the 78 research
documents now; a two-group pilot of precedent search with a citation gate; a fixed-price proposal for
Carmel's repeat work.

**What it costs:** phase 2 fee ₪96,000; pilot tooling up to ₪40,000; two associates at half time for
curation (non-billable, ≈ 4 weeks).

**What a no means:** the vendor's discount drives a two-year, 90-seat decision without a test on the
firm's own material; consumer use continues on client documents; the insurer's questions are answered
without a rule.

**What it does not promise:** a revenue increase in 2027. It promises a firm that knows what its tools
do, and a price model where faster work is not only lost fees.
