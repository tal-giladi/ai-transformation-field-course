# Extraction eval — rules-baseline

Documents: 200 · fields scored: 654 · run file: `runs/rules-baseline.csv`

## Headline

- Field accuracy: **86.7%** (567 of 654; 95% interval 83.9–89.1%)
- Critical fields (dates, amounts, currency): **85.9%** of 475
- Documents with every field right (no correction needed): **64.0%** of 200
- Errors: 52 blank, 35 wrong value (a wrong value is worse: it looks filled in)
- Extra fields returned that were not asked for: 0

## By field type

| Type | Fields | Accuracy |
|---|---|---|
| amount | 241 | 88.8% |
| currency | 34 | 100.0% |
| date | 200 | 80.0% |
| identifier | 179 | 88.8% |

## Fairness slices

Accuracy per group with a 95% interval. *Ratio* = the group's accuracy divided by the best group's (groups with at least 30 scored fields). Read a low ratio together with its interval and the stratified table below before you call it a language effect.

### doc_language

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| ar | 135 | 84.4% | 77.4–89.6% | 0.93 |
| en | 80 | 91.2% | 83.0–95.7% | 1.00 |
| he | 334 | 87.1% | 83.1–90.3% | 0.95 |
| ru | 105 | 84.8% | 76.7–90.4% | 0.93 |

### claimant_language

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| ar | 145 | 84.1% | 77.3–89.2% | 0.92 |
| en | 84 | 91.7% | 83.8–95.9% | 1.00 |
| he | 308 | 86.7% | 82.4–90.0% | 0.95 |
| ru | 117 | 86.3% | 78.9–91.4% | 0.94 |

### region

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| Center | 200 | 87.5% | 82.2–91.4% | 0.94 |
| Jerusalem | 69 | 92.8% | 84.1–96.9% | 1.00 |
| North | 226 | 84.1% | 78.7–88.3% | 0.91 |
| South | 86 | 84.9% | 75.8–90.9% | 0.92 |
| Tel Aviv | 73 | 89.0% | 79.8–94.3% | 0.96 |

### claimant_age_band

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| 18-24 | 41 | 95.1% | 83.9–98.7% | 1.00 |
| 25-34 | 91 | 85.7% | 77.1–91.5% | 0.90 |
| 35-44 | 123 | 82.1% | 74.4–87.9% | 0.86 |
| 45-54 | 174 | 87.9% | 82.3–92.0% | 0.92 |
| 55-64 | 120 | 85.0% | 77.5–90.3% | 0.89 |
| 65-74 | 69 | 92.8% | 84.1–96.9% | 0.98 |
| 75+ | 36 | 83.3% | 68.1–92.1% | 0.88 |

### capture_channel

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| app_photo | 206 | 81.1% | 75.2–85.8% | 0.84 |
| email_pdf | 202 | 97.0% | 93.7–98.6% | 1.00 |
| fax | 27 | 55.6% | 37.3–72.4% | n<30 |
| scanner_haifa | 91 | 78.0% | 68.5–85.3% | 0.80 |
| scanner_ramat_gan | 128 | 92.2% | 86.2–95.7% | 0.95 |

### form_filled

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| handwritten | 89 | 73.0% | 63.0–81.2% | 0.82 |
| printed | 470 | 89.1% | 86.0–91.6% | 1.00 |
| typed | 95 | 87.4% | 79.2–92.6% | 0.98 |

### doc_type

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| assessor_report | 42 | 83.3% | 69.4–91.7% | 0.86 |
| claim_form | 184 | 80.4% | 74.1–85.5% | 0.83 |
| contractor_invoice | 80 | 92.5% | 84.6–96.5% | 0.95 |
| garage_invoice | 152 | 88.8% | 82.8–92.9% | 0.92 |
| health_receipt | 75 | 86.7% | 77.2–92.6% | 0.89 |
| medical_invoice_abroad | 87 | 88.5% | 80.1–93.6% | 0.91 |
| police_confirmation | 34 | 97.1% | 85.1–99.5% | 1.00 |

## Stratified: document language × capture channel

| Language | Capture | Fields | Accuracy |
|---|---|---|---|
| ar | app_photo | 42 | 78.6% |
| ar | email_pdf | 26 | 96.2% |
| ar | fax | 10 | 70.0% |
| ar | scanner_haifa | 43 | 83.7% |
| ar | scanner_ramat_gan | 14 | 92.9% |
| en | app_photo | 34 | 85.3% |
| en | email_pdf | 42 | 95.2% |
| en | scanner_ramat_gan | 4 | 100.0% |
| he | app_photo | 95 | 84.2% |
| he | email_pdf | 94 | 98.9% |
| he | fax | 17 | 47.1% |
| he | scanner_haifa | 44 | 70.5% |
| he | scanner_ramat_gan | 84 | 94.0% |
| ru | app_photo | 35 | 71.4% |
| ru | email_pdf | 40 | 95.0% |
| ru | scanner_haifa | 4 | 100.0% |
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
| D027 | health_receipt | ar | app_photo | receipt_number | 10319 | ١٠٣١٩ |
| D029 | claim_form | he | scanner_ramat_gan | policy_number | 55-4232370 | (blank) |
| D031 | garage_invoice | he | app_photo | invoice_date | 2026-09-11 | (blank) |
| D033 | health_receipt | he | fax | total_amount | 520.00 | 20.00 |
| D037 | contractor_invoice | he | scanner_haifa | vat_amount | 1228.47 | 228.47 |
| D041 | garage_invoice | ar | scanner_haifa | invoice_date | 2026-09-22 | (blank) |
| D046 | medical_invoice_abroad | en | app_photo | service_date | 2026-09-06 | 2026-06-09 |
| D053 | contractor_invoice | he | app_photo | total_amount | 2754.01 | 4.01 |
| D055 | medical_invoice_abroad | en | app_photo | service_date | 2026-09-03 | 2026-03-09 |
| D055 | medical_invoice_abroad | en | app_photo | total_amount | 2191.33 | 91.33 |
| D056 | medical_invoice_abroad | en | email_pdf | service_date | 2026-09-02 | 2026-02-09 |
| D063 | claim_form | he | app_photo | claimed_amount | 3440.00 | 0.00 |
| D065 | medical_invoice_abroad | ru | app_photo | service_date | 2026-08-17 | (blank) |
| D068 | claim_form | ru | scanner_ramat_gan | loss_date | 2026-10-14 | (blank) |
| D072 | assessor_report | he | scanner_haifa | assessed_amount | 10575.25 | (blank) |
| D078 | claim_form | ar | app_photo | loss_date | 2026-09-25 | (blank) |
| D080 | garage_invoice | he | scanner_haifa | invoice_number | 68975 | 6897 |
| D085 | garage_invoice | ar | scanner_haifa | invoice_number | 53980 | ٥٣٩٨٠ |
| D087 | claim_form | he | scanner_haifa | claimed_amount | 10570.00 | (blank) |
| D088 | claim_form | ar | fax | loss_date | 2026-09-21 | (blank) |
| D096 | claim_form | he | scanner_ramat_gan | claimed_amount | 12480.00 | 0.00 |
| D100 | health_receipt | he | app_photo | service_date | 2026-09-27 | (blank) |
| D102 | health_receipt | ar | app_photo | receipt_number | 71249 | ٧١٢٤٩ |
| D103 | assessor_report | he | app_photo | inspection_date | 2026-09-30 | (blank) |
| D104 | claim_form | ar | fax | loss_date | 2026-10-21 | (blank) |
| D107 | claim_form | he | app_photo | claimed_amount | 13150.00 | 0.00 |
| D107 | claim_form | he | app_photo | policy_number | 30-8196080 | (blank) |
| D118 | health_receipt | he | fax | receipt_number | 55598 | (blank) |
| D118 | health_receipt | he | fax | service_date | 2026-10-06 | (blank) |
| D119 | claim_form | ru | app_photo | loss_date | 2026-10-07 | (blank) |
| D126 | health_receipt | ar | scanner_ramat_gan | receipt_number | 27923 | ٢٧٩٢٣ |
| D127 | claim_form | he | scanner_ramat_gan | claimed_amount | 4730.00 | 0.00 |
