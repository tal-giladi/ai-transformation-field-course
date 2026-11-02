# Extraction pilot — eval report, fairness check and deployment verdict

*Head of AI Transformation, v1.0, Thursday 14 January 2027. For the COO and CFO (decision within
their limits) and the risk committee (information). Templates: [pilot charter](../../../templates/pilot-charter.md),
[test-set spec](../../../templates/test-set-spec.md), [eval report](../../../templates/eval-report.md),
[human-review design](../../../templates/human-review-design.md).*

> [!NOTE]
> The **Smart Intake and rules-baseline numbers are real**: `python score_extraction.py <run> --split test`
> reproduces them. The **LLM pilot numbers are an illustrative worked example** (prompt v1.1, an
> approved enterprise LLM, run 5–6 January 2027). They were not measured by the course authors and
> describe no real model.

## Verdict

**Ship with conditions — to shadow mode, not to production.** From Monday 15 March 2027 (after the
peak), the extractor runs beside intake at Ramat Gan and Haifa on Hebrew, Russian and English
documents: it pre-fills fields and lists missing documents; a handler confirms every field against the
source line. Arabic documents run in shadow without pre-filling until they pass the same gates on
production documents. Smart Intake stays limited to its current motor use under the committee's
conditions; the shadow comparison decides between them in May.

## What was tested

- **Population:** 240 intake documents received September–October 2026, OCR text layer, redacted;
  seven document types; Hebrew 128, Arabic 44, Russian 38, English 30. Gold values keyed twice and
  verified by Claims QA. Split: 40 development, 200 test (654 fields), stratified by language and type
  (`pilot/splits.csv`). Plus 12 negative tests (`pilot/negative-tests.csv`).
- **Not tested:** scanned images (only the OCR text layer); production volume; handlers under load;
  the completeness list (needs live claims).

## Gates (written 16 December, before the test run)

| Gate | Threshold | Kind |
|---|---|---|
| G1 Critical fields (dates, amounts, currency) | ≥ 95% on the test set | Compensable with G2 |
| G2 Every language group | ≥ 90% field accuracy and ≥ 0.95 of the best group (groups ≥ 30 fields) | Non-compensable |
| G3 Wrong values that look right | ≤ 2% of fields wrong and not blank | Compensable |
| G4 Data minimisation | 0 fields beyond the schema; 0 diagnoses | Non-compensable |
| G5 Negative tests | 12 of 12 | Non-compensable |

## Results on the 200 test documents

| | Rules, no AI (real) | Smart Intake (real) | LLM pilot v1.1 (illustrative) |
|---|---|---|---|
| Field accuracy | 86.7% (567/654) | 82.1% (537/654) | 95.4% (624/654) |
| Critical fields | 85.9% | 82.9% | 95.6% |
| Documents with every field right | 64.0% | 60.5% | 85.0% |
| Wrong values (not blank) | 35 (5.4%) | 83 (12.7%; 37 with confidence ≥ 0.80) | 12 (1.8%) |
| Hebrew / Arabic / Russian / English | 87.1 / 84.4 / 84.8 / 91.2% | 88.6 / 62.2 / 80.0 / 91.2% | 96.4 / 93.3 / 94.3 / 96.3% |
| Worst / best language | 0.93 | 0.68 | 0.97 |
| Haifa scanner / email PDF | 78.0 / 97.0% | 67.0 / 90.6% | 89.0 / 98.5% |
| Extra fields (diagnoses) | 0 | 37 | 0 |
| Negative tests | 9 of 12 (real: fails the injected instruction N01, the ambiguous date N03, Eastern digits in an identifier N06) | not run (asked Kalanit, 7 Jan) | v1.0 11 of 12 (guessed N03); v1.1 12 of 12 |
| Gates G1–G5 | fail G1, G2, G5 | fail G1, G2, G3, G4 | pass all |

## Fairness check

**Groups and why they are legitimate to test.** Document language and the claimant's language of
correspondence (recorded for service), region and age band (recorded on the claim): we may use them to
*test* whether the extractor works equally well; none is an input to it. We did not infer ethnicity,
religion or gender from names or anything else, and gender is not recorded on these documents: that
gap is stated, not filled. Capture channel and handwritten/typed are not protected: they are used to
*explain* gaps. The DPO approved the use of these fields for testing (policy rule 3.2).

**Reading.** Smart Intake's Arabic gap is partly the Haifa scanner (most Arabic documents arrive
there) and mostly Eastern Arabic digits: on clean email PDFs Arabic is still 69.2% vs Hebrew 96.8%.
Stratify before calling it a language effect, and then fix the cause. The rules baseline shows the
digit problem is solvable without AI (84.4% on Arabic). The LLM pilot's smallest group (English, 80
fields) has a 95% interval of about 88–99%: G2 is met, but the Arabic group must be re-measured on
production documents (≥ 300 fields) before Arabic pre-fill is switched on.

## Failure types (LLM, illustrative, 30 field errors)

OCR-damaged digits on handwritten forms 11 · null where the value was readable (over-cautious dates) 9
· Russian month names 4 · a total taken from the line before VAT 3 · other 3.

## Cost

About 800 tokens in and 60 out per document (illustrative); at Claude Sonnet 5.5 list prices
(US$2 / US$10 per million, checked 2 November 2026) and ₪3.70 per US$: ₪0.008 a document, about ₪900
a year for 110,000 documents. Tokens do not decide this; handlers' checking minutes do.

## Human review design (Marina Kogan rated 120 outputs blind, 6–7 January)

- The pre-filled value is shown **beside the source line** it came from; a click accepts, typing
  replaces. Null fields are empty, not guessed.
- Timer on every confirmation; the QA sample checks 100 confirmed claims a month. If confirmations
  take under 3 seconds a field or wrong values pass the sample, the control is not operating
  (Tamar Weiss's test).
- Rule of use: pre-fill and a missing-documents list only. The output never feeds a fraud score,
  never approves a payment, never writes to the notes field.

## Conditions for shadow mode (owner, date)

1. Enterprise LLM agreement: no training on Meridian data, retention ≤ 30 days, processor terms (CIO,
   1 March). 2. DPIA signed (COO with DPO, 1 March). 3. Haifa scanner replaced (CIO, 1 March). 4.
   Shadow from 15 March for 8 weeks; gates re-measured on ≥ 1,000 production fields, ≥ 300 Arabic
   (pilot lead, 15 May). 5. Stop: any diagnosis in output, or critical accuracy below 92% in any
   language in a week (VP Claims can stop it).

## Value (directional)

Keying 5.5 → about 2.5 minutes a claim with a 1-minute check: ≈ ₪180k a year of capacity (36,760
claims × 3 min × ₪145/h ÷ 60 ≈ ₪266k gross, less checking). The bigger value is the completeness
list on day one: measured in shadow mode as rounds per claim.
