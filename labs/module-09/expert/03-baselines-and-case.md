# Baselines, shortlist and one-page case — AI in claims

*Head of AI Transformation, Thursday 26 November 2026. For Ilana Bar-Lev; reviewed with Natalia
Gurevich (definitions) and Yusuf Darawshe (process). Templates: [opportunity map](../../../templates/opportunity-map.md),
[use-case scorecard](../../../templates/use-case-scorecard.md), [ROI model](../../../templates/roi-model.md),
[decision-ready case](../../../templates/decision-ready-case.md). Reproduce with `python baselines.py`.*

## 1. Three baselines, one definition

| Measure | Definition | Source | Value | Use it for |
|---|---|---|---|---|
| Dashboard "handling time" | File complete → decision, SIU excluded | BI, whole company | 10.5 days mean YTD (sample: mean 10.6, median 8.1, n=743) | The regulatory 30-day clock only |
| Kalanit cycle | Registered → closed | Register sample | median 41.1 days (n=787) | Nothing: closure is administration |
| **Claimant's wait** | **Reported → last indemnity payment** | Register + ERP | **median 32 days, p75 46, p90 64 (n=696, paid in 2026)** | **The baseline**. Natalia uses the same definition |
| Direct-channel check | First CRM contact → last payment | CRM + ERP, May–Oct | median 25 days (n=165) | A check: agents' claims (the slower channel) are not in the CRM |

Agreed with Natalia on 23 November: the claimant's wait is the programme's baseline; the dashboard
number stays, renamed "time to decision after a complete file". This also answers internal audit's
open 2025 finding, once BI adds it to the dashboard.

## 2. Where the 32 days go (claims decided January–October 2026, medians)

```mermaid
flowchart LR
  A[Reported] -->|2.5 d intake| B[Registered]
  B -->|1.1 d| C[First documents list]
  C -->|12.8 d document chase<br/>mean 18.5| D[File complete]
  D -->|8.3 d| E[Decision]
  E -->|1.6 d| F[Paid]
```

Rounds drive the wait: one round 24 days median (n=380), two 41 (n=219), three or more 60 (n=97).

## 3. The peak

January ≈ 5,100 claims (2025 and 2026) against ≈ 2,500 in May–October; home claims up to 2,500 a
month; intake lag median 5.6 days in January. Any change that needs handlers' attention waits until
March.

## 4. Opportunity map and shortlist

| Candidate | Type | Evidence | Verdict |
|---|---|---|---|
| A. Complete documents list on day one (agent portal mandatory fields, intake checklist, Arabic/Russian letters, travel-medical list fixed) | Plain process and automation, no AI | 45.4% of later requests were on the standard list; 5.6% same-day lists | **Go, first**, from 4 January (small, inside the peak, no new system) |
| B. Extraction with a completeness check at intake (reads what arrived, lists what is missing, pre-fills fields for the handler) | AI assist, human confirms | Keying 5.5 min/claim; finding missing documents 6.8 min/claim | **Go with conditions**: offline pilot now, shadow mode after the peak |
| C. Smart Intake as is | Vendor AI | 81.7% field accuracy, Arabic 59.6%; no time saved; diagnoses copied | Not as is; compare with B in the pilot |
| D. Fraud Insight on home / Pro | Rules score sold as AI | Proxies; labels are referrals; ₪20M unsourced | **Stop / not now** (see the verdict) |
| E. Sanctioned translation for foreign documents | AI assist | 12 shadow-AI notes; Marina | Go, through the approved enterprise tool, small |

## 5. Money (labels: M measured, D directional, A assumed)

| Line | Yearly | Label |
|---|---|---|
| Keying time today: 5.5 min × 36,760 claims × ₪145/h | ₪488k | M (time study n=120; 2025 volume) |
| Finding missing documents: 6.8 min × 36,760 × ₪145/h | ₪606k | M |
| B: half of keying saved, checking adds 1.5 min a claim | ≈ ₪110k net | D (pilot to measure) |
| A + B: rounds from 1.62 to 1.3 → a third of the "finding" time | ≈ ₪200k | A |
| Claimants' wait: second rounds avoided → median wait closer to 24 days than 32 | not in ₪ | D |
| Fraud: confirmed fraud ₪2.34M YTD; no evidence a score adds to it | ₪0 counted | M (the ₪0 is a decision) |
| Pilot B: build and evaluation ₪95k; shadow mode ₪60k; LLM tokens ≈ ₪1–2k a month at full volume | ₪155k one-off | A (quotes pending) |

Capacity, not cash, until Yusuf decides what the hours buy (the winter temps).

## 6. One-page case (front page)

> **Ask.** Approve ₪155,000 of the ₪240,000 for (A) a day-one documents list from 4 January and (B)
> an extraction-and-completeness pilot, offline now, in shadow mode from mid-March, Hebrew, Russian
> and English first. Do **not** extend Fraud Insight or buy Pro; switch off its auto-referral (done
> 22 November).
>
> **Why.** Claimants wait a median 32 days, of which 12.8 are spent chasing documents; 45% of later
> requests ask for things that should have been asked for on day one (*measured*). Typing is ₪488k a
> year; finding missing documents ₪606k (*measured*).
>
> **What we expect.** Rounds per claim from 1.62 to about 1.3 and the median wait toward 24 days by
> July (*directional*); about ₪300k of handler capacity a year (*assumed*, measured in shadow mode).
>
> **Cost of waiting.** Each month at today's rate ≈ 1,380 claims (45% of ≈ 3,060) need a second round. The vendor's
> 15% Pro discount is not a cost of waiting.
>
> **What a no means.** The winter runs as today; the documents list is fixed anyway (no AI needed).
