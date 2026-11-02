# Extraction eval — rules-baseline

Documents: 240 · fields scored: 788 · run file: `runs/rules-baseline.csv`

## Headline

- Field accuracy: **86.0%** (678 of 788; 95% interval 83.4–88.3%)
- Critical fields (dates, amounts, currency): **85.8%** of 571
- Documents with every field right (no correction needed): **62.9%** of 240
- Errors: 62 blank, 48 wrong value (a wrong value is worse: it looks filled in)
- Extra fields returned that were not asked for: 0

## By field type

| Type | Fields | Accuracy |
|---|---|---|
| amount | 290 | 88.3% |
| currency | 41 | 97.6% |
| date | 240 | 80.8% |
| identifier | 217 | 86.6% |

## Fairness slices

Accuracy per group with a 95% interval. *Ratio* = the group's accuracy divided by the best group's (groups with at least 30 scored fields). Read a low ratio together with its interval and the stratified table below before you call it a language effect.

### doc_language

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| ar | 166 | 83.1% | 76.7–88.1% | 0.93 |
| en | 96 | 89.6% | 81.9–94.2% | 1.00 |
| he | 396 | 86.6% | 82.9–89.6% | 0.97 |
| ru | 130 | 85.4% | 78.3–90.4% | 0.95 |

### claimant_language

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| ar | 178 | 83.1% | 77.0–87.9% | 0.92 |
| en | 100 | 90.0% | 82.6–94.5% | 1.00 |
| he | 368 | 86.1% | 82.2–89.3% | 0.96 |
| ru | 142 | 86.6% | 80.0–91.3% | 0.96 |

### region

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| Center | 241 | 88.8% | 84.2–92.2% | 1.00 |
| Jerusalem | 85 | 88.2% | 79.7–93.5% | 0.99 |
| North | 262 | 83.6% | 78.6–87.6% | 0.94 |
| South | 109 | 84.4% | 76.4–90.0% | 0.95 |
| Tel Aviv | 91 | 85.7% | 77.1–91.5% | 0.97 |

### claimant_age_band

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| 18-24 | 45 | 95.6% | 85.2–98.8% | 1.00 |
| 25-34 | 123 | 83.7% | 76.2–89.2% | 0.88 |
| 35-44 | 157 | 82.2% | 75.4–87.4% | 0.86 |
| 45-54 | 193 | 88.6% | 83.3–92.4% | 0.93 |
| 55-64 | 146 | 84.2% | 77.5–89.3% | 0.88 |
| 65-74 | 80 | 90.0% | 81.5–94.8% | 0.94 |
| 75+ | 44 | 84.1% | 70.6–92.1% | 0.88 |

### capture_channel

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| app_photo | 252 | 81.0% | 75.7–85.3% | 0.83 |
| email_pdf | 232 | 97.0% | 93.9–98.5% | 1.00 |
| fax | 36 | 61.1% | 44.9–75.2% | 0.63 |
| scanner_haifa | 105 | 78.1% | 69.3–84.9% | 0.81 |
| scanner_ramat_gan | 163 | 89.0% | 83.2–92.9% | 0.92 |

### form_filled

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| handwritten | 109 | 72.5% | 63.4–80.0% | 0.82 |
| printed | 565 | 88.7% | 85.8–91.0% | 1.00 |
| typed | 114 | 86.0% | 78.4–91.2% | 0.97 |

### doc_type

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| assessor_report | 50 | 84.0% | 71.5–91.7% | 0.86 |
| claim_form | 223 | 79.4% | 73.6–84.2% | 0.81 |
| contractor_invoice | 100 | 93.0% | 86.3–96.6% | 0.95 |
| garage_invoice | 180 | 88.3% | 82.8–92.2% | 0.91 |
| health_receipt | 90 | 85.6% | 76.8–91.4% | 0.88 |
| medical_invoice_abroad | 105 | 86.7% | 78.9–91.9% | 0.89 |
| police_confirmation | 40 | 97.5% | 87.1–99.6% | 1.00 |

## Stratified: document language × capture channel

| Language | Capture | Fields | Accuracy |
|---|---|---|---|
| ar | app_photo | 53 | 75.5% |
| ar | email_pdf | 30 | 96.7% |
| ar | fax | 10 | 70.0% |
| ar | scanner_haifa | 47 | 85.1% |
| ar | scanner_ramat_gan | 26 | 84.6% |
| en | app_photo | 43 | 83.7% |
| en | email_pdf | 45 | 95.6% |
| en | scanner_ramat_gan | 8 | 87.5% |
| he | app_photo | 111 | 84.7% |
| he | email_pdf | 110 | 99.1% |
| he | fax | 22 | 50.0% |
| he | scanner_haifa | 50 | 70.0% |
| he | scanner_ramat_gan | 103 | 91.3% |
| ru | app_photo | 45 | 75.6% |
| ru | email_pdf | 47 | 93.6% |
| ru | fax | 4 | 100.0% |
| ru | scanner_haifa | 8 | 87.5% |
| ru | scanner_ramat_gan | 26 | 84.6% |

## Errors (first 40)

| doc | type | lang | capture | field | gold | run |
|---|---|---|---|---|---|---|
| D004 | claim_form | ar | app_photo | claimed_amount | 8760.00 | (blank) |
| D004 | claim_form | ar | app_photo | loss_date | 2026-09-28 | (blank) |
| D004 | claim_form | ar | app_photo | policy_number | 55-6304852 | (blank) |
| D005 | police_confirmation | he | app_photo | event_date | 2026-10-01 | (blank) |
| D009 | claim_form | ru | app_photo | loss_date | 2026-09-26 | (blank) |
| D015 | claim_form | ru | app_photo | loss_date | 2026-09-05 | (blank) |
| D015 | claim_form | ru | app_photo | policy_number | 31-6159198 | (blank) |
| D017 | garage_invoice | ar | scanner_haifa | total_amount | 5065.81 | 1.00 |
| D021 | claim_form | he | scanner_ramat_gan | claimed_amount | 5040.00 | (blank) |
| D021 | claim_form | he | scanner_ramat_gan | policy_number | 30-3659195 | (blank) |
| D022 | garage_invoice | ar | scanner_ramat_gan | invoice_number | 55211 | ٥٥٢١١ |
| D025 | medical_invoice_abroad | ru | email_pdf | service_date | 2026-09-16 | (blank) |
| D027 | health_receipt | ar | app_photo | receipt_number | 10319 | ١٠٣١٩ |
| D029 | claim_form | he | scanner_ramat_gan | policy_number | 55-4232370 | (blank) |
| D031 | garage_invoice | he | app_photo | invoice_date | 2026-09-11 | (blank) |
| D033 | health_receipt | he | fax | total_amount | 520.00 | 20.00 |
| D035 | garage_invoice | ar | app_photo | invoice_number | 50592 | ٥٠٥٩٢ |
| D037 | contractor_invoice | he | scanner_haifa | vat_amount | 1228.47 | 228.47 |
| D039 | claim_form | he | app_photo | claimed_amount | 24780.00 | 0.00 |
| D041 | garage_invoice | ar | scanner_haifa | invoice_date | 2026-09-22 | (blank) |
| D046 | medical_invoice_abroad | en | app_photo | service_date | 2026-09-06 | 2026-06-09 |
| D053 | contractor_invoice | he | app_photo | total_amount | 2754.01 | 4.01 |
| D055 | medical_invoice_abroad | en | app_photo | service_date | 2026-09-03 | 2026-03-09 |
| D055 | medical_invoice_abroad | en | app_photo | total_amount | 2191.33 | 91.33 |
| D056 | medical_invoice_abroad | en | email_pdf | service_date | 2026-09-02 | 2026-02-09 |
| D058 | claim_form | ar | app_photo | policy_number | 31-5378750 | ٣١-٥٣٧٨٧٥٠ |
| D058 | claim_form | ar | app_photo | vehicle_plate | 31-880-52 | ٣١-٨٨٠-٥٢ |
| D063 | claim_form | he | app_photo | claimed_amount | 3440.00 | 0.00 |
| D064 | garage_invoice | he | scanner_haifa | invoice_number | 24775 | 2477 |
| D064 | garage_invoice | he | scanner_haifa | vat_amount | 1661.45 | 0.00 |
| D065 | medical_invoice_abroad | ru | app_photo | service_date | 2026-08-17 | (blank) |
| D066 | claim_form | ru | scanner_haifa | loss_date | 2026-08-18 | (blank) |
| D068 | claim_form | ru | scanner_ramat_gan | loss_date | 2026-10-14 | (blank) |
| D072 | assessor_report | he | scanner_haifa | assessed_amount | 10575.25 | (blank) |
| D075 | health_receipt | he | fax | service_date | 2026-10-06 | (blank) |
| D075 | health_receipt | he | fax | total_amount | 810.00 | 10.00 |
| D077 | claim_form | en | scanner_ramat_gan | currency | USD | (blank) |
| D078 | claim_form | ar | app_photo | loss_date | 2026-09-25 | (blank) |
| D080 | garage_invoice | he | scanner_haifa | invoice_number | 68975 | 6897 |
| D085 | garage_invoice | ar | scanner_haifa | invoice_number | 53980 | ٥٣٩٨٠ |
