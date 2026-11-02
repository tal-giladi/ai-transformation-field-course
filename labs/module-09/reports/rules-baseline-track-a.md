# Extraction eval — rules-baseline

Documents: 60 · fields scored: 204 · run file: `runs/rules-baseline.csv`

## Headline

- Field accuracy: **89.7%** (183 of 204; 95% interval 84.8–93.2%)
- Critical fields (dates, amounts, currency): **91.1%** of 158
- Documents with every field right (no correction needed): **68.3%** of 60
- Errors: 11 blank, 10 wrong value (a wrong value is worse: it looks filled in)
- Extra fields returned that were not asked for: 0

## By field type

| Type | Fields | Accuracy |
|---|---|---|
| amount | 76 | 94.7% |
| currency | 22 | 100.0% |
| date | 60 | 83.3% |
| identifier | 46 | 84.8% |

## Fairness slices

Accuracy per group with a 95% interval. *Ratio* = the group's accuracy divided by the best group's (groups with at least 30 scored fields). Read a low ratio together with its interval and the stratified table below before you call it a language effect.

### doc_language

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| ar | 57 | 87.7% | 76.8–93.9% | 0.91 |
| en | 50 | 96.0% | 86.5–98.9% | 1.00 |
| he | 46 | 89.1% | 77.0–95.3% | 0.93 |
| ru | 51 | 86.3% | 74.3–93.2% | 0.90 |

### claimant_language

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| ar | 59 | 88.1% | 77.5–94.1% | 0.92 |
| en | 50 | 96.0% | 86.5–98.9% | 1.00 |
| he | 42 | 88.1% | 75.0–94.8% | 0.92 |
| ru | 53 | 86.8% | 75.2–93.5% | 0.90 |

### region

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| Center | 79 | 91.1% | 82.8–95.6% | 1.00 |
| Jerusalem | 15 | 100.0% | 79.6–100.0% | n<30 |
| North | 71 | 83.1% | 72.7–90.1% | 0.91 |
| South | 11 | 100.0% | 74.1–100.0% | n<30 |
| Tel Aviv | 28 | 92.9% | 77.4–98.0% | n<30 |

### claimant_age_band

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| 18-24 | 11 | 100.0% | 74.1–100.0% | n<30 |
| 25-34 | 35 | 88.6% | 74.0–95.5% | 0.98 |
| 35-44 | 40 | 87.5% | 73.9–94.5% | 0.96 |
| 45-54 | 54 | 90.7% | 80.1–96.0% | 1.00 |
| 55-64 | 33 | 87.9% | 72.7–95.2% | 0.97 |
| 65-74 | 31 | 90.3% | 75.1–96.7% | 1.00 |

### capture_channel

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| app_photo | 67 | 86.6% | 76.4–92.8% | 0.89 |
| email_pdf | 77 | 97.4% | 91.0–99.3% | 1.00 |
| fax | 3 | 33.3% | 6.1–79.2% | n<30 |
| scanner_haifa | 23 | 82.6% | 62.9–93.0% | n<30 |
| scanner_ramat_gan | 34 | 88.2% | 73.4–95.3% | 0.91 |

### form_filled

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| handwritten | 24 | 79.2% | 59.5–90.8% | n<30 |
| printed | 148 | 91.2% | 85.6–94.8% | 1.00 |
| typed | 32 | 90.6% | 75.8–96.8% | 0.99 |

### doc_type

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| assessor_report | 6 | 100.0% | 61.0–100.0% | n<30 |
| claim_form | 56 | 85.7% | 74.3–92.6% | 0.91 |
| contractor_invoice | 32 | 93.8% | 79.9–98.3% | 1.00 |
| garage_invoice | 44 | 88.6% | 76.0–95.0% | 0.95 |
| health_receipt | 9 | 77.8% | 45.3–93.7% | n<30 |
| medical_invoice_abroad | 51 | 92.2% | 81.5–96.9% | 0.98 |
| police_confirmation | 6 | 100.0% | 61.0–100.0% | n<30 |

## Stratified: document language × capture channel

| Language | Capture | Fields | Accuracy |
|---|---|---|---|
| ar | app_photo | 23 | 87.0% |
| ar | email_pdf | 12 | 91.7% |
| ar | scanner_haifa | 15 | 86.7% |
| ar | scanner_ramat_gan | 7 | 85.7% |
| en | app_photo | 22 | 90.9% |
| en | email_pdf | 24 | 100.0% |
| en | scanner_ramat_gan | 4 | 100.0% |
| he | app_photo | 6 | 100.0% |
| he | email_pdf | 22 | 100.0% |
| he | fax | 3 | 33.3% |
| he | scanner_haifa | 8 | 75.0% |
| he | scanner_ramat_gan | 7 | 85.7% |
| ru | app_photo | 16 | 75.0% |
| ru | email_pdf | 19 | 94.7% |
| ru | scanner_ramat_gan | 16 | 87.5% |

## Errors (first 40)

| doc | type | lang | capture | field | gold | run |
|---|---|---|---|---|---|---|
| D009 | claim_form | ru | app_photo | loss_date | 2026-09-26 | (blank) |
| D015 | claim_form | ru | app_photo | loss_date | 2026-09-05 | (blank) |
| D015 | claim_form | ru | app_photo | policy_number | 31-6159198 | (blank) |
| D017 | garage_invoice | ar | scanner_haifa | total_amount | 5065.81 | 1.00 |
| D029 | claim_form | he | scanner_ramat_gan | policy_number | 55-4232370 | (blank) |
| D065 | medical_invoice_abroad | ru | app_photo | service_date | 2026-08-17 | (blank) |
| D068 | claim_form | ru | scanner_ramat_gan | loss_date | 2026-10-14 | (blank) |
| D078 | claim_form | ar | app_photo | loss_date | 2026-09-25 | (blank) |
| D080 | garage_invoice | he | scanner_haifa | invoice_number | 68975 | 6897 |
| D102 | health_receipt | ar | app_photo | receipt_number | 71249 | ٧١٢٤٩ |
| D126 | health_receipt | ar | scanner_ramat_gan | receipt_number | 27923 | ٢٧٩٢٣ |
| D158 | medical_invoice_abroad | ru | email_pdf | service_date | 2026-10-08 | (blank) |
| D162 | claim_form | he | fax | claimed_amount | 9040.00 | (blank) |
| D162 | claim_form | he | fax | loss_date | 2026-09-14 | (blank) |
| D191 | contractor_invoice | ar | scanner_haifa | vat_amount | 1021.88 | 21.88 |
| D201 | medical_invoice_abroad | en | app_photo | service_date | 2026-09-03 | 2026-03-09 |
| D206 | medical_invoice_abroad | en | app_photo | service_date | 2026-09-04 | 2026-04-09 |
| D218 | garage_invoice | he | scanner_haifa | total_amount | 16251.41 | 41.00 |
| D232 | garage_invoice | ar | email_pdf | invoice_number | 97569 | ٩٧٥٦٩ |
| D236 | garage_invoice | ar | app_photo | invoice_number | 98687 | ٩٨٦٨٧ |
| D238 | contractor_invoice | ru | scanner_ramat_gan | invoice_date | 2026-08-24 | (blank) |
