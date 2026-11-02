# Extraction eval — smart_intake_output

Documents: 60 · fields scored: 204 · run file: `data-room/extraction/smart_intake_output.csv`

## Headline

- Field accuracy: **79.9%** (163 of 204; 95% interval 73.9–84.8%)
- Critical fields (dates, amounts, currency): **79.7%** of 158
- Documents with every field right (no correction needed): **55.0%** of 60
- Errors: 17 blank, 24 wrong value (a wrong value is worse: it looks filled in)
- Extra fields returned that were not asked for: 18 (fields: free_text_notes)

## By field type

| Type | Fields | Accuracy |
|---|---|---|
| amount | 76 | 82.9% |
| currency | 22 | 81.8% |
| date | 60 | 75.0% |
| identifier | 46 | 80.4% |

## Fairness slices

Accuracy per group with a 95% interval. *Ratio* = the group's accuracy divided by the best group's (groups with at least 30 scored fields). Read a low ratio together with its interval and the stratified table below before you call it a language effect.

### doc_language

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| ar | 57 | 63.2% | 50.2–74.5% | 0.69 |
| en | 50 | 92.0% | 81.2–96.8% | 1.00 |
| he | 46 | 87.0% | 74.3–93.9% | 0.95 |
| ru | 51 | 80.4% | 67.5–89.0% | 0.87 |

### claimant_language

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| ar | 59 | 64.4% | 51.7–75.4% | 0.70 |
| en | 50 | 92.0% | 81.2–96.8% | 1.00 |
| he | 42 | 85.7% | 72.2–93.3% | 0.93 |
| ru | 53 | 81.1% | 68.6–89.4% | 0.88 |

### region

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| Center | 79 | 86.1% | 76.8–92.0% | 1.00 |
| Jerusalem | 15 | 86.7% | 62.1–96.3% | n<30 |
| North | 71 | 69.0% | 57.5–78.6% | 0.80 |
| South | 11 | 100.0% | 74.1–100.0% | n<30 |
| Tel Aviv | 28 | 78.6% | 60.5–89.8% | n<30 |

### claimant_age_band

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| 18-24 | 11 | 90.9% | 62.3–98.4% | n<30 |
| 25-34 | 35 | 77.1% | 61.0–87.9% | 0.91 |
| 35-44 | 40 | 85.0% | 70.9–92.9% | 1.00 |
| 45-54 | 54 | 85.2% | 73.4–92.3% | 1.00 |
| 55-64 | 33 | 69.7% | 52.7–82.6% | 0.82 |
| 65-74 | 31 | 74.2% | 56.8–86.3% | 0.87 |

### capture_channel

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| app_photo | 67 | 74.6% | 63.1–83.5% | 0.85 |
| email_pdf | 77 | 88.3% | 79.3–93.7% | 1.00 |
| fax | 3 | 33.3% | 6.1–79.2% | n<30 |
| scanner_haifa | 23 | 78.3% | 58.1–90.3% | n<30 |
| scanner_ramat_gan | 34 | 76.5% | 60.0–87.6% | 0.87 |

### form_filled

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| handwritten | 24 | 66.7% | 46.7–82.0% | n<30 |
| printed | 148 | 79.1% | 71.8–84.8% | 0.84 |
| typed | 32 | 93.8% | 79.9–98.3% | 1.00 |

### doc_type

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| assessor_report | 6 | 100.0% | 61.0–100.0% | n<30 |
| claim_form | 56 | 82.1% | 70.2–90.0% | 0.97 |
| contractor_invoice | 32 | 84.4% | 68.2–93.1% | 1.00 |
| garage_invoice | 44 | 72.7% | 58.2–83.7% | 0.86 |
| health_receipt | 9 | 33.3% | 12.1–64.6% | n<30 |
| medical_invoice_abroad | 51 | 84.3% | 72.0–91.8% | 1.00 |
| police_confirmation | 6 | 100.0% | 61.0–100.0% | n<30 |

## Stratified: document language × capture channel

| Language | Capture | Fields | Accuracy |
|---|---|---|---|
| ar | app_photo | 23 | 56.5% |
| ar | email_pdf | 12 | 66.7% |
| ar | scanner_haifa | 15 | 73.3% |
| ar | scanner_ramat_gan | 7 | 57.1% |
| en | app_photo | 22 | 81.8% |
| en | email_pdf | 24 | 100.0% |
| en | scanner_ramat_gan | 4 | 100.0% |
| he | app_photo | 6 | 100.0% |
| he | email_pdf | 22 | 95.5% |
| he | fax | 3 | 33.3% |
| he | scanner_haifa | 8 | 87.5% |
| he | scanner_ramat_gan | 7 | 71.4% |
| ru | app_photo | 16 | 81.2% |
| ru | email_pdf | 19 | 78.9% |
| ru | scanner_ramat_gan | 16 | 81.2% |

## Errors (first 40)

| doc | type | lang | capture | field | gold | run |
|---|---|---|---|---|---|---|
| D009 | claim_form | ru | app_photo | loss_date | 2026-09-26 | (blank) |
| D017 | garage_invoice | ar | scanner_haifa | invoice_number | 91451 | 92451 |
| D017 | garage_invoice | ar | scanner_haifa | total_amount | 5065.81 | (blank) |
| D029 | claim_form | he | scanner_ramat_gan | loss_date | 2026-10-17 | 2026-10-18 |
| D029 | claim_form | he | scanner_ramat_gan | policy_number | 55-4232370 | 56-4232370 |
| D030 | contractor_invoice | ar | scanner_haifa | invoice_date | 2026-10-04 | 2026-10-05 |
| D057 | medical_invoice_abroad | ru | email_pdf | currency | GEL | USD |
| D065 | medical_invoice_abroad | ru | app_photo | service_date | 2026-08-17 | 2026-08-18 |
| D068 | claim_form | ru | scanner_ramat_gan | loss_date | 2026-10-14 | (blank) |
| D078 | claim_form | ar | app_photo | loss_date | 2026-09-25 | 2026-09-26 |
| D080 | garage_invoice | he | scanner_haifa | total_amount | 8554.17 | 855.42 |
| D091 | garage_invoice | ar | app_photo | vat_amount | 772.34 | (blank) |
| D102 | health_receipt | ar | app_photo | receipt_number | 71249 | (blank) |
| D102 | health_receipt | ar | app_photo | service_date | 2026-08-26 | (blank) |
| D102 | health_receipt | ar | app_photo | total_amount | 1380.00 | (blank) |
| D111 | claim_form | en | app_photo | policy_number | 30-9786740 | 31-9786740 |
| D121 | contractor_invoice | ru | email_pdf | vat_amount | 0.00 | 1391.59 |
| D126 | health_receipt | ar | scanner_ramat_gan | receipt_number | 27923 | (blank) |
| D126 | health_receipt | ar | scanner_ramat_gan | service_date | 2026-10-09 | (blank) |
| D126 | health_receipt | ar | scanner_ramat_gan | total_amount | 2730.00 | (blank) |
| D159 | medical_invoice_abroad | ru | email_pdf | currency | AMD | USD |
| D160 | contractor_invoice | he | email_pdf | vat_amount | 0.00 | 717.14 |
| D162 | claim_form | he | fax | claimed_amount | 9040.00 | (blank) |
| D162 | claim_form | he | fax | loss_date | 2026-09-14 | 2026-09-17 |
| D171 | medical_invoice_abroad | ru | email_pdf | currency | GEL | USD |
| D175 | medical_invoice_abroad | ru | app_photo | service_date | 2026-08-30 | 2026-09-29 |
| D201 | medical_invoice_abroad | en | app_photo | service_date | 2026-09-03 | 2026-03-09 |
| D206 | medical_invoice_abroad | en | app_photo | service_date | 2026-09-04 | 2026-04-09 |
| D212 | claim_form | ar | scanner_haifa | policy_number | 31-3120508 | 31-3150508 |
| D217 | medical_invoice_abroad | en | app_photo | currency | THB | USD |
| D225 | claim_form | ar | app_photo | loss_date | 2026-09-13 | 2026-09-16 |
| D232 | garage_invoice | ar | email_pdf | invoice_date | 2026-08-30 | 2026-08-29 |
| D232 | garage_invoice | ar | email_pdf | invoice_number | 97569 | (blank) |
| D232 | garage_invoice | ar | email_pdf | total_amount | 4801.29 | (blank) |
| D232 | garage_invoice | ar | email_pdf | vat_amount | 732.40 | (blank) |
| D236 | garage_invoice | ar | app_photo | invoice_date | 2026-09-28 | 2026-09-18 |
| D236 | garage_invoice | ar | app_photo | invoice_number | 98687 | (blank) |
| D236 | garage_invoice | ar | app_photo | total_amount | 10838.87 | (blank) |
| D236 | garage_invoice | ar | app_photo | vat_amount | 1653.39 | (blank) |
| D238 | contractor_invoice | ru | scanner_ramat_gan | invoice_number | 3519 | 6519 |

## Extra fields (data minimisation)

| doc | field | value |
|---|---|---|
| D024 | free_text_notes | Dx: acute gastroenteritis |
| D057 | free_text_notes | Dx: отит |
| D065 | free_text_notes | Dx: пищевое отравление |
| D081 | free_text_notes | Dx: острый гастроэнтерит |
| D084 | free_text_notes | Dx: lower back pain |
| D101 | free_text_notes | Dx: боль в спине |
| D110 | free_text_notes | Dx: sprained ankle, X-ray negative |
| D136 | free_text_notes | Dx: otitis media |
| D158 | free_text_notes | Dx: пищевое отравление |
| D159 | free_text_notes | Dx: растяжение связок голеностопа |
| D171 | free_text_notes | Dx: отит |
| D175 | free_text_notes | Dx: острый гастроэнтерит |
| D177 | free_text_notes | Dx: lower back pain |
| D201 | free_text_notes | Dx: lower back pain |
| D204 | free_text_notes | Dx: sprained ankle, X-ray negative |
| D206 | free_text_notes | Dx: acute gastroenteritis |
| D217 | free_text_notes | Dx: sprained ankle, X-ray negative |
| D240 | free_text_notes | Dx: otitis media |
