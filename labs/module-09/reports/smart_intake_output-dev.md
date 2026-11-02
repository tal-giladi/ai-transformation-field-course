# Extraction eval — smart_intake_output

Documents: 40 · fields scored: 134 · run file: `data-room/extraction/smart_intake_output.csv`

## Headline

- Field accuracy: **79.9%** (107 of 134; 95% interval 72.3–85.8%)
- Critical fields (dates, amounts, currency): **83.3%** of 96
- Documents with every field right (no correction needed): **67.5%** of 40
- Errors: 13 blank, 14 wrong value (a wrong value is worse: it looks filled in)
- Extra fields returned that were not asked for: 8 (fields: free_text_notes)

## By field type

| Type | Fields | Accuracy |
|---|---|---|
| amount | 49 | 81.6% |
| currency | 7 | 85.7% |
| date | 40 | 85.0% |
| identifier | 38 | 71.1% |

## Fairness slices

Accuracy per group with a 95% interval. *Ratio* = the group's accuracy divided by the best group's (groups with at least 30 scored fields). Read a low ratio together with its interval and the stratified table below before you call it a language effect.

### doc_language

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| ar | 31 | 48.4% | 32.0–65.2% | 0.56 |
| en | 16 | 81.2% | 57.0–93.4% | n<30 |
| he | 62 | 87.1% | 76.6–93.3% | 1.00 |
| ru | 25 | 100.0% | 86.7–100.0% | n<30 |

### claimant_language

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| ar | 33 | 51.5% | 35.2–67.5% | 0.59 |
| en | 16 | 81.2% | 57.0–93.4% | n<30 |
| he | 60 | 86.7% | 75.8–93.1% | 1.00 |
| ru | 25 | 100.0% | 86.7–100.0% | n<30 |

### region

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| Center | 41 | 90.2% | 77.5–96.1% | 0.96 |
| Jerusalem | 16 | 56.2% | 33.2–76.9% | n<30 |
| North | 36 | 94.4% | 81.9–98.5% | 1.00 |
| South | 23 | 39.1% | 22.2–59.2% | n<30 |
| Tel Aviv | 18 | 100.0% | 82.4–100.0% | n<30 |

### claimant_age_band

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| 18-24 | 4 | 100.0% | 51.0–100.0% | n<30 |
| 25-34 | 32 | 59.4% | 42.3–74.5% | 0.61 |
| 35-44 | 34 | 97.1% | 85.1–99.5% | 1.00 |
| 45-54 | 19 | 68.4% | 46.0–84.6% | n<30 |
| 55-64 | 26 | 88.5% | 71.0–96.0% | n<30 |
| 65-74 | 11 | 63.6% | 35.4–84.8% | n<30 |
| 75+ | 8 | 100.0% | 67.6–100.0% | n<30 |

### capture_channel

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| app_photo | 46 | 63.0% | 48.6–75.5% | 0.63 |
| email_pdf | 30 | 100.0% | 88.6–100.0% | 1.00 |
| fax | 9 | 100.0% | 70.1–100.0% | n<30 |
| scanner_haifa | 14 | 85.7% | 60.1–96.0% | n<30 |
| scanner_ramat_gan | 35 | 77.1% | 61.0–87.9% | 0.77 |

### form_filled

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| handwritten | 20 | 65.0% | 43.3–81.9% | n<30 |
| printed | 95 | 83.2% | 74.4–89.4% | 1.00 |
| typed | 19 | 78.9% | 56.7–91.5% | n<30 |

### doc_type

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| assessor_report | 8 | 87.5% | 52.9–97.8% | n<30 |
| claim_form | 39 | 71.8% | 56.2–83.5% | 1.00 |
| contractor_invoice | 20 | 95.0% | 76.4–99.1% | n<30 |
| garage_invoice | 28 | 75.0% | 56.6–87.3% | n<30 |
| health_receipt | 15 | 80.0% | 54.8–93.0% | n<30 |
| medical_invoice_abroad | 18 | 83.3% | 60.8–94.2% | n<30 |
| police_confirmation | 6 | 83.3% | 43.6–97.0% | n<30 |

## Stratified: document language × capture channel

| Language | Capture | Fields | Accuracy |
|---|---|---|---|
| ar | app_photo | 11 | 9.1% |
| ar | email_pdf | 4 | 100.0% |
| ar | scanner_haifa | 4 | 100.0% |
| ar | scanner_ramat_gan | 12 | 50.0% |
| en | app_photo | 9 | 66.7% |
| en | email_pdf | 3 | 100.0% |
| en | scanner_ramat_gan | 4 | 100.0% |
| he | app_photo | 16 | 75.0% |
| he | email_pdf | 16 | 100.0% |
| he | fax | 5 | 100.0% |
| he | scanner_haifa | 6 | 66.7% |
| he | scanner_ramat_gan | 19 | 89.5% |
| ru | app_photo | 10 | 100.0% |
| ru | email_pdf | 7 | 100.0% |
| ru | fax | 4 | 100.0% |
| ru | scanner_haifa | 4 | 100.0% |

## Errors (first 40)

| doc | type | lang | capture | field | gold | run |
|---|---|---|---|---|---|---|
| D021 | claim_form | he | scanner_ramat_gan | vehicle_plate | 58-708-47 | 58-708-57 |
| D022 | garage_invoice | ar | scanner_ramat_gan | invoice_number | 55211 | (blank) |
| D022 | garage_invoice | ar | scanner_ramat_gan | total_amount | 4815.11 | (blank) |
| D035 | garage_invoice | ar | app_photo | invoice_date | 2026-10-24 | (blank) |
| D035 | garage_invoice | ar | app_photo | total_amount | 8089.01 | (blank) |
| D035 | garage_invoice | ar | app_photo | vat_amount | 1233.92 | 4233.92 |
| D039 | claim_form | he | app_photo | policy_number | 31-8717789 | 31-8317789 |
| D039 | claim_form | he | app_photo | vehicle_plate | 42-770-80 | 52-770-80 |
| D042 | medical_invoice_abroad | en | app_photo | currency | THB | USD |
| D042 | medical_invoice_abroad | en | app_photo | service_date | 2026-10-02 | 2026-10-01 |
| D042 | medical_invoice_abroad | en | app_photo | total_amount | 22605.44 | 22905.44 |
| D058 | claim_form | ar | app_photo | claimed_amount | 7900.00 | (blank) |
| D058 | claim_form | ar | app_photo | loss_date | 2026-09-23 | (blank) |
| D058 | claim_form | ar | app_photo | policy_number | 31-5378750 | (blank) |
| D058 | claim_form | ar | app_photo | vehicle_plate | 31-880-52 | (blank) |
| D064 | garage_invoice | he | scanner_haifa | invoice_number | 24775 | 24375 |
| D105 | health_receipt | ar | app_photo | receipt_number | 59441 | (blank) |
| D105 | health_receipt | ar | app_photo | service_date | 2026-10-02 | (blank) |
| D105 | health_receipt | ar | app_photo | total_amount | 1620.00 | 1621.00 |
| D117 | assessor_report | he | scanner_haifa | inspection_date | 2026-10-12 | 2026-10-11 |
| D148 | claim_form | ar | scanner_ramat_gan | claimed_amount | 10000.00 | (blank) |
| D148 | claim_form | ar | scanner_ramat_gan | loss_date | 2026-08-20 | 2026-08-23 |
| D148 | claim_form | ar | scanner_ramat_gan | policy_number | 42-1441260 | (blank) |
| D148 | claim_form | ar | scanner_ramat_gan | vehicle_plate | 25-439-72 | (blank) |
| D184 | police_confirmation | he | app_photo | report_number | 523769/2026 | 523769/2036 |
| D219 | garage_invoice | he | app_photo | vat_amount | 817.71 | 17.71 |
| D228 | contractor_invoice | he | scanner_ramat_gan | vat_amount | 0.00 | 597.31 |

## Extra fields (data minimisation)

| doc | field | value |
|---|---|---|
| D025 | free_text_notes | Dx: растяжение связок голеностопа |
| D042 | free_text_notes | Dx: lower back pain |
| D095 | free_text_notes | Dx: sprained ankle, X-ray negative |
| D099 | free_text_notes | Dx: otitis media |
| D105 | free_text_notes | Dx: التهاب الحلق |
| D145 | free_text_notes | Dx: растяжение связок голеностопа |
| D164 | free_text_notes | Dx: otitis media |
| D233 | free_text_notes | Dx: боль в спине |
