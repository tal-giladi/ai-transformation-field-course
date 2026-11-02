# 03 · Baselines, requirements and the one-page case — Galil Health

For the phase-1 readout, Thursday 3 December 2026. Prices in ₪; vendors quote in ₪.

## Baseline sheet

| Measure | Value | Definition and source | Label |
|---|---|---|---|
| Doctor visits a month | ≈ 26,000 (Sep 24,610 with holidays; Oct 27,315) | `doctor-days.csv`, full counts | measured |
| Active note time per visit | median 4.2 min, mean 4.8 | `note_active_sec`, 8% sample | measured |
| Documentation per doctor-day | median 112 min (p75 136) | visits × the doctor's mean note + after-hours time | measured (estimate) |
| After-hours documentation per doctor-day | median 10 min, mean 12 | `after_hours_sec` | measured |
| Visits with after-hours work | 18.6% (33% in mismatch visits) | `after_hours_sec` > 0 | measured |
| Self-reported documentation | 120 min a day; 2 evenings a week | survey, 60 doctors | reported |
| Patients' preferred language | ar 38%, he 30%, ru 28%, other 3% | appointment field | measured |
| Mismatch visits | 27.8% | preferred language not among the doctor's languages | measured |
| Nurse interpreting | ≈ 8% of doctor visits; 42 min a day per nurse (median) | `interpreter`; survey | measured; reported |
| Notes signed within 24 h | 98.1% | KPI and sample | measured (not an effort measure) |
| Locums; vacancies; leavers | ₪2.1M (2025); 9; 6 in 12 months (4 workload, 3 "evenings") | finance summary, KPI | reported by finance and HR |

## What the scribe must do at Galil (requirements for the RFP)

1. Draft a Hebrew note from a conversation in Hebrew, Galilee Arabic or Russian, with relatives talking.
2. Capture what relatives say about medicines and allergies; show the doctor where it is unsure.
3. Never invent a finding or a dose; the doctor confirms before signing.
4. Work with Notara 9.2 and 7.4, or say what it costs not to.
5. Keep audio and notes where Galil's counsel, DPO and Fund A allow; no training on Galil's data.
6. Prove 1–3 on Galil's own synthetic visits before any contract.

## Options

| | A. Sign ScribeWave now (120 seats, 31 Dec) | B. RFP + PoC, then a pilot | C. Do nothing now |
|---|---|---|---|
| Evidence in Galil's conditions | None | 90 synthetic visits, 3 languages, by 31 Dec | None |
| Arabic and Russian | Unknown; Hebrew beta, Arabic Gulf | Tested | — |
| Fund A, cloud committee, privacy notice | Signature before approval: conflict (counsel to confirm) | Built into the timeline | — |
| Shadow recording | Continues in the meantime | Interim instruction now; sanctioned tool from the pilot | Continues |
| Cost to Galil now | ₪1,457,280 a year (Standard plan; Enterprise for no training ≈ ₪1.72M with discount) | PoC ≤ ₪75,000 | ₪0 |
| What it gives up | — | The 12% discount, unless MedLink extends it | The goal |

## Netting the claims

- **"Two hours a day."** Galil measures 112 minutes in all. Rishma's independent evaluation found −52
  minutes a clinician-day elsewhere (range 40–70). Working assumption for planning: **30 minutes a
  doctor-day** (assumed until the pilot measures it).
- **Capacity, not cash** (the CFO's rule). 30 min × ≈ 1,200 doctor-days a month ≈ 600 hours a month ≈ 3.8
  full-time doctors' hours. Galil is paid per registered patient, so this is capacity, not money.
- **Where money could come from:** a vacancy filled or kept without a locum saves about ₪300,000 a year
  (CFO). A scribe for 78 doctors at ≈ ₪1.3M a year pays back in cash only if it keeps or fills about four
  to five posts a year (assumed; the pilot can show direction, not proof). Say this on the front page.
- **The cost of the expensive error:** an omitted allergy or medicine change in a signed note (IN-2025-044,
  IN-2026-052). The PoC measures how often.

## One-page case (front page for 3 December)

**Decision asked.** Approve (1) an RFP to the four vendors on 6 December with Galil's conditions, locked
criteria and must-have terms; (2) a proof of concept on 90 synthetic visits (₪75,000, CIO's budget), results
on 31 December; (3) a written request to MedLink to extend its offer to 31 March 2027; (4) counsel to open
the Fund A conversation now; (5) an interim instruction on recording visits with personal apps, with no
discipline for past use.

**Decline:** signing any vendor by 31 December.

**What a "no" means.** Galil signs on demo impressions: an English demo, a Standard plan that lets the
vendor train on de-identified recordings, audio kept 90 days in the EU or the US, before Fund A has been
asked, and with no evidence in Arabic, the language of 38% of patients.

**What it costs.** ≤ ₪75,000 and four weeks. Possibly the 12% discount (≈ ₪199,000 in year one) if MedLink
does not extend it.

**What this does not promise.** It does not promise a vendor by 31 December, or two hours a day.

**Sentence for the board.** "We are choosing the scribe on evidence from our own clinics, in Hebrew, Arabic
and Russian, and the first doctors will use it in the first quarter."
