# Extraction eval — rules-baseline

Documents: 40 · fields scored: 134 · run file: `runs/rules-baseline.csv`

## Headline

- Field accuracy: **82.8%** (111 of 134; 95% interval 75.6–88.3%)
- Critical fields (dates, amounts, currency): **85.4%** of 96
- Documents with every field right (no correction needed): **57.5%** of 40
- Errors: 10 blank, 13 wrong value (a wrong value is worse: it looks filled in)
- Extra fields returned that were not asked for: 0

## By field type

| Type | Fields | Accuracy |
|---|---|---|
| amount | 49 | 85.7% |
| currency | 7 | 85.7% |
| date | 40 | 85.0% |
| identifier | 38 | 76.3% |

## Fairness slices

Accuracy per group with a 95% interval. *Ratio* = the group's accuracy divided by the best group's (groups with at least 30 scored fields). Read a low ratio together with its interval and the stratified table below before you call it a language effect.

### doc_language

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| ar | 31 | 77.4% | 60.2–88.6% | 0.92 |
| en | 16 | 81.2% | 57.0–93.4% | n<30 |
| he | 62 | 83.9% | 72.8–91.0% | 1.00 |
| ru | 25 | 88.0% | 70.0–95.8% | n<30 |

### claimant_language

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| ar | 33 | 78.8% | 62.2–89.3% | 0.95 |
| en | 16 | 81.2% | 57.0–93.4% | n<30 |
| he | 60 | 83.3% | 72.0–90.7% | 1.00 |
| ru | 25 | 88.0% | 70.0–95.8% | n<30 |

### region

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| Center | 41 | 95.1% | 83.9–98.7% | 1.00 |
| Jerusalem | 16 | 68.8% | 44.4–85.8% | n<30 |
| North | 36 | 80.6% | 65.0–90.2% | 0.85 |
| South | 23 | 82.6% | 62.9–93.0% | n<30 |
| Tel Aviv | 18 | 72.2% | 49.1–87.5% | n<30 |

### claimant_age_band

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| 18-24 | 4 | 100.0% | 51.0–100.0% | n<30 |
| 25-34 | 32 | 78.1% | 61.2–89.0% | 0.95 |
| 35-44 | 34 | 82.4% | 66.5–91.7% | 1.00 |
| 45-54 | 19 | 94.7% | 75.4–99.1% | n<30 |
| 55-64 | 26 | 80.8% | 62.1–91.5% | n<30 |
| 65-74 | 11 | 72.7% | 43.4–90.3% | n<30 |
| 75+ | 8 | 87.5% | 52.9–97.8% | n<30 |

### capture_channel

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| app_photo | 46 | 80.4% | 66.8–89.3% | 0.83 |
| email_pdf | 30 | 96.7% | 83.3–99.4% | 1.00 |
| fax | 9 | 77.8% | 45.3–93.7% | n<30 |
| scanner_haifa | 14 | 78.6% | 52.4–92.4% | n<30 |
| scanner_ramat_gan | 35 | 77.1% | 61.0–87.9% | 0.80 |

### form_filled

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| handwritten | 20 | 70.0% | 48.1–85.5% | n<30 |
| printed | 95 | 86.3% | 78.0–91.8% | 1.00 |
| typed | 19 | 78.9% | 56.7–91.5% | n<30 |

### doc_type

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| assessor_report | 8 | 87.5% | 52.9–97.8% | n<30 |
| claim_form | 39 | 74.4% | 58.9–85.4% | 1.00 |
| contractor_invoice | 20 | 95.0% | 76.4–99.1% | n<30 |
| garage_invoice | 28 | 85.7% | 68.5–94.3% | n<30 |
| health_receipt | 15 | 80.0% | 54.8–93.0% | n<30 |
| medical_invoice_abroad | 18 | 77.8% | 54.8–91.0% | n<30 |
| police_confirmation | 6 | 100.0% | 61.0–100.0% | n<30 |

## Stratified: document language × capture channel

| Language | Capture | Fields | Accuracy |
|---|---|---|---|
| ar | app_photo | 11 | 63.6% |
| ar | email_pdf | 4 | 100.0% |
| ar | scanner_haifa | 4 | 100.0% |
| ar | scanner_ramat_gan | 12 | 75.0% |
| en | app_photo | 9 | 77.8% |
| en | email_pdf | 3 | 100.0% |
| en | scanner_ramat_gan | 4 | 75.0% |
| he | app_photo | 16 | 87.5% |
| he | email_pdf | 16 | 100.0% |
| he | fax | 5 | 60.0% |
| he | scanner_haifa | 6 | 66.7% |
| he | scanner_ramat_gan | 19 | 78.9% |
| ru | app_photo | 10 | 90.0% |
| ru | email_pdf | 7 | 85.7% |
| ru | fax | 4 | 100.0% |
| ru | scanner_haifa | 4 | 75.0% |

## Errors (first 40)

| doc | type | lang | capture | field | gold | run |
|---|---|---|---|---|---|---|
| D021 | claim_form | he | scanner_ramat_gan | claimed_amount | 5040.00 | (blank) |
| D021 | claim_form | he | scanner_ramat_gan | policy_number | 30-3659195 | (blank) |
| D022 | garage_invoice | ar | scanner_ramat_gan | invoice_number | 55211 | ٥٥٢١١ |
| D025 | medical_invoice_abroad | ru | email_pdf | service_date | 2026-09-16 | (blank) |
| D035 | garage_invoice | ar | app_photo | invoice_number | 50592 | ٥٠٥٩٢ |
| D039 | claim_form | he | app_photo | claimed_amount | 24780.00 | 0.00 |
| D058 | claim_form | ar | app_photo | policy_number | 31-5378750 | ٣١-٥٣٧٨٧٥٠ |
| D058 | claim_form | ar | app_photo | vehicle_plate | 31-880-52 | ٣١-٨٨٠-٥٢ |
| D064 | garage_invoice | he | scanner_haifa | invoice_number | 24775 | 2477 |
| D064 | garage_invoice | he | scanner_haifa | vat_amount | 1661.45 | 0.00 |
| D066 | claim_form | ru | scanner_haifa | loss_date | 2026-08-18 | (blank) |
| D075 | health_receipt | he | fax | service_date | 2026-10-06 | (blank) |
| D075 | health_receipt | he | fax | total_amount | 810.00 | 10.00 |
| D077 | claim_form | en | scanner_ramat_gan | currency | USD | (blank) |
| D089 | assessor_report | he | scanner_ramat_gan | inspection_date | 2026-09-07 | (blank) |
| D095 | medical_invoice_abroad | en | app_photo | service_date | 2026-08-11 | 2026-11-08 |
| D095 | medical_invoice_abroad | en | app_photo | total_amount | 845.44 | 44.00 |
| D105 | health_receipt | ar | app_photo | receipt_number | 59441 | ٥٩٤٤١ |
| D145 | medical_invoice_abroad | ru | app_photo | service_date | 2026-08-02 | (blank) |
| D148 | claim_form | ar | scanner_ramat_gan | policy_number | 42-1441260 | ٤٢-١٤٤١٢٦٠ |
| D148 | claim_form | ar | scanner_ramat_gan | vehicle_plate | 25-439-72 | ٢٥-٤٣٩-٧٢ |
| D199 | claim_form | he | app_photo | claimed_amount | 5310.00 | (blank) |
| D228 | contractor_invoice | he | scanner_ramat_gan | total_amount | 3915.69 | (blank) |
