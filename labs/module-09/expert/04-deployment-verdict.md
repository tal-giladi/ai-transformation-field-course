# Deployment verdict — Kalanit 9.4 AI modules and the proposed winter pilot

*Pre-read for the board's risk management committee, Tuesday 15 December 2026. Author: Head of AI
Transformation; secretary: Michael Ohana (CRO). Sent Tuesday 8 December. Legal points were reviewed
by Ofer Klein (General Counsel) and Dr. Rana Haj-Yahia (DPO); this paper states facts and the
questions put to them, not legal conclusions. Templates: [regulatory map](../../../templates/regulatory-map.md),
[decision record](../../../templates/decision-record.md); the gate format follows IBM's pass / flag /
block and ship / ship with conditions / wait.*

## 0. Correction to the record

On 15 June 2026 management stated that no AI system makes or materially supports decisions on
claims. **Since 6 September 2026 that has not been true.** Kalanit Claims 9.4 went live with two modules
switched on by default: Smart Intake (pre-fills claim fields from documents) and Fraud Insight (scores
every motor claim; at 50 or more it routes the claim to the SIU and holds payment). The committee's
action 6.1 ("assessment to the committee before use") was not done. Neither module is in the AI
inventory. Both are added today (AI-05, AI-06).

## 1. Decisions requested

1. **Ratify** the interim change of 22 November: Fraud Insight auto-referral off; factors F08, F09 and
   F13 disabled; score visible to the SIU as a review aid only, with written reasons for any referral.
2. **Fraud Insight: wait** (blocked) until re-validated on confirmed outcomes and re-tested across
   groups. No extension to home claims; no Fraud Insight Pro.
3. **Smart Intake: wait** on any extension; the current motor use continues **only** while the
   conditions in section 6 are met (diagnoses no longer copied by 31 December, or it is switched off).
4. **The winter pilot as proposed: wait.** Approve instead an offline extraction pilot now and shadow
   mode after the peak, with the gates in section 6 (decision of the COO and CFO within their limits,
   for the committee's information).

## 2. What the systems are, and how they are classified

| | Smart Intake (AI-05) | Fraud Insight (AI-06) |
|---|---|---|
| What it does | Reads documents, pre-fills fields; the handler confirms each field | Adds points for 14 rule-based factors; 35+ amber badge; 50+ routes to the SIU and holds payment |
| AI under our counting rule (01.7)? | Yes (learned OCR and extraction) | **No**: a weighted rules list from the vendor's 2019–2021 consortium analysis, no learning |
| High-impact under the AI policy (rule 2)? | Yes, lower tier: it supports the amounts that are paid; a person confirms every field | **Yes**: it materially supports a decision about the claim (who is investigated, when payment is held), whatever we call it |
| Risk factors (inter-ministerial report, Dec 2025: decides vs assists, effect on rights, volume, data sensitivity) | Assists; affects payment amounts; ≈ 14,000 motor claims a year (two centres); health data in documents | Holds payments without a person in the loop; ≈ 18,600 motor claims a year; uses language and area |
| Tier | **Medium** | **High** |

**Why the label does not matter.** The Prohibition of Discrimination in Products, Services and Entry
into Places of Entertainment and Public Places Law, 5761-2000 (חוק איסור הפליה במוצרים, בשירותים
ובכניסה למקומות בידור ולמקומות ציבוריים) applies to insurance as a public service whatever technology is
used, and lists nationality, country of origin and place of residence among its grounds (as quoted in
the inter-ministerial report, December 2025). A spreadsheet that does what Fraud Insight does would be
gated the same way.

## 3. Regulatory map (Israel first)

| Instrument | What it asks here | System | Status / question |
|---|---|---|---|
| Supervisor's circular 2016-9-9, clarification and settlement of claims | Good faith, transparency, fairness (s. 3); documents list at first contact (8(a)(1)(d)); further documents within 14 business days (8(a)(6)); notice within 30 days of having all documents (8(b)); main findings when a decision rests on an investigation report (annex s. 6(c)) | Both; the claimant journey | Binding. Q to counsel: does an automatic payment hold need a continued-clarification notice with reasons? |
| Prohibition of Discrimination Law, 5761-2000, s. 3(a), 3(a1); exception s. 3(d)(1) | No discrimination in a public service (insurance included) on listed grounds incl. nationality, country of origin and place of residence, unless required by the nature of the service | Fraud Insight F08, F09; F13 (age) | **Q to General Counsel**: exposure from proxy factors; whether any is "required by the nature" of fraud detection. His preliminary view: disable F08/F09 now |
| CMISA consolidated circular: risk management (incl. model risk), outsourcing chapter | Risks identified and managed; outsourcing does not transfer responsibility | Both (vendor-configured) | In force; the vendor's liability cap (12.1) does not move responsibility |
| Inter-ministerial report on AI in the financial sector (Dec 2025) | Recommendations, not binding: risk-based tiers; general and specific explainability for high-risk decisions; human involvement for significant decisions; outcome testing for proxies; responsibility stays with the institution | Both | Used as the committee's benchmark |
| Privacy Protection Law, 5741-1981, Amendment 13; Data Security Regulations, 5777-2017; transfer regulations | Purpose limitation; health data of special sensitivity; DPIA (our policy); processor agreement (Reg. 15); transfer to an EU region | Smart Intake (Frankfurt; diagnoses into notes; vendor's right to train on anonymised data, cl. 9.2) | DPO: DPIA before any extension; notes field fixed now; cl. 9.2 an open risk |
| PPA draft guidance on AI (April 2025) | Transparency about AI processing; DPIA; accuracy | Both | Draft; followed |
| **EU AI Act** (Reg. 2024/1689 as amended by 2026/1744) | — | — | **Not applicable**: no EU establishment, Israeli customers, outputs used in Israel (Art. 2(1)); claims handling and fraud detection are not in Annex III (5(b) excludes fraud detection; 5(c) covers only life and health insurance risk assessment and pricing, application 2 Dec 2027). Re-check if Meridian ever prices health cover for EU residents |

## 4. The outcome test (Fraud Insight)

*Criteria written on 30 November, after the first look at referral rates on 18 November; said here so
the committee can weigh it.* Data: every motor claim registered 1 July – 31 October 2026 (5,536),
pseudonymised, approved by the DPO for this purpose under policy rule 3.2. Groups: language of
correspondence and postal area (recorded for service, not inferred), region, age band. No ethnicity or
religion was inferred from names or anything else. Screen: a group's referral rate more than 1.25×
the reference group's, with non-overlapping 95% intervals, is a finding (a referral is an adverse
outcome, so the four-fifths screen is applied in the other direction; it is an internal screen, not a
legal threshold).

| Group | Before 6 Sep (handlers) | After 6 Sep (Fraud Insight) | Ratio after |
|---|---|---|---|
| Hebrew (reference) | 3.4% of 2,065 | 5.4% of 1,697 (4.4–6.6%) | 1.00 |
| **Arabic** | 3.2% of 538 | **21.0% of 453 (17.5–25.0%)** | **3.87** |
| Russian | 4.0% of 301 | 3.8% of 261 | 0.71 |
| Postal area not on list (reference) | 3.4% of 2,591 | 5.3% of 2,179 | 1.00 |
| **Postal area on the "risk areas" list** | 3.8% of 423 | **25.9% of 343 (21.6–30.8%)** | **4.92** |
| North vs Center | 3.9% vs 3.1% | 13.5% vs 6.6% | 2.04 |
| Age 18–24 vs 35–44 | 3.7% vs 4.2% | 10.6% vs 8.0% | 1.32 (intervals overlap: watch) |

Mechanism (configuration export): F08 "interpreter required" (+10) fires on 90.3% of Arabic claims
and 0% of Hebrew; F09 "risk area" (+15) on 68.4% and 1.6%. Without them, Arabic auto-referrals fall
from 65 to 4, Hebrew from 33 to 31. **Before go-live, handlers referred both groups at the same rate.**

Does it find fraud? Unknown, and the vendor's evidence cannot tell: its back-test label (AUC 0.81) is
the SUSPECT flag, i.e. past referrals. Of 23 closed auto-referrals, 2 were confirmed fraud (8.7%;
interval 2.4–26.8%); 84 are open. Handlers' closed referrals since July 2025: 12.6% confirmed.

## 5. Gates

| Gate (evidence question) | Smart Intake | Fraud Insight |
|---|---|---|
| G1 In the inventory with an accountable owner? | **Flag**: added today; owner COO | **Flag**: added today; owner VP Claims |
| G2 Approved before production as policy 3.2 requires? | **Block** (retroactive): not approved; resolved by this decision | **Block**: not approved |
| G3 Accurate on Meridian's own documents/claims? | **Flag**: 82.1% of fields on 200 test documents vs vendor's 97.4% (lab, typed Hebrew); a no-AI rules script 86.7% | **Block**: never validated on confirmed outcomes |
| G4 Outcomes equal across groups? | **Flag**: Arabic documents 62.2% vs Hebrew 88.6%; mostly Eastern Arabic digits and the Haifa scanner | **Block**: 3.87× Arabic, 4.92× risk areas, through proxy factors |
| G5 Can we tell the claimant the main reasons? | Pass (a person confirms the values) | **Block**: the claimant was told "the system flagged your file"; no reason given |
| G6 Human oversight that operates, not only designed? | **Flag**: 37 of 83 wrong values had confidence ≥ 0.80 (not highlighted); checking takes 3.3 min, as long as keying | **Block**: no person before the payment hold |
| G7 Privacy: DPIA, minimisation, transfer, data use | **Block** until fixed: diagnoses copied into notes (45 of 240 documents); no DPIA; cl. 9.2 | Flag: no DPIA |
| G8 Vendor terms: change control, liability, exit | Flag: features on by default (7.3); liability capped (12.1) | Flag: same; configuration changeable any day at no cost |
| G9 Monitoring and a named person who can stop it | Flag: none today | Block: none today |

A block rules out both ship verdicts.

## 6. Verdicts and conditions

**Fraud Insight — wait.** Before it may return to the committee: a validation on confirmed outcomes
(SIU outcomes recorded for every case, at least 12 months), no factor that stands for a protected
ground (F08, F09, F13 removed; F05 "non-network garage" reviewed, it fires on 41.5% of Arabic and 20.6%
of Hebrew claims), an outcome test by group with the screen above, and a reason a handler can give a
claimant.

**Smart Intake — wait on extension; current use under conditions:**

| Condition | Metric | Warning | Hard limit | Cadence | Owner | Can stop it | If breached |
|---|---|---|---|---|---|---|---|
| No health data in notes | Diagnoses in free-text notes | any | any after 31 Dec | weekly sample of 50 | CIO (Noam Segal) | DPO | Switch off Smart Intake |
| Arabic invoices keyed by hand | Share of Arabic motor documents pre-filled | — | 0% until Kalanit 9.6 is tested | monthly | Haifa centre manager | VP Claims | Disable for Arabic |
| Wrong values reach payment | QA sample of 100 pre-filled claims a month | 1 wrong amount | 3 | monthly | Claims QA (Hadas Mor) | VP Claims | Disable; review |
| DPIA | Signed | — | by 31 Jan | once | COO with DPO | DPO | Switch off |

**Winter pilot — wait.** Offline pilot on the 240-document set now; shadow mode from mid-March after
the peak, if it meets gates written before testing (09.5).

## 7. Dissent

The COO's view: Smart Intake should be extended to home claims for the storm season because the
temporary clerks need help; she accepts the Fraud Insight decision. Not followed: on the evidence it
saves no time (3.5 + 3.3 minutes vs 6.7), and extending it during the peak adds health data and
Arabic invoices it reads worst.

## 8. Cost of delay, stated honestly

No measured fraud saving is lost: none was shown. Some intake capacity may be lost in the peak (the
pilot claimed −60% keying; measured, Smart Intake saves nothing net). The vendor's 15% Pro discount
expires. The documents-list fix (no AI) starts on 4 January regardless.

## 9. Evidence file

`motor_claims_2026-07_to_10.csv`, `bias_test.py` output (30 Nov), `fraud-insight-config-export.csv`,
`risk-areas-v3.csv`, SIU case log, Kalanit release notes and agreement, `smart_intake_output.csv` scored
by `score_extraction.py` (test split), time study, CL-2026-026307 file and complaint, DPO and General
Counsel notes (2 and 7 December).
