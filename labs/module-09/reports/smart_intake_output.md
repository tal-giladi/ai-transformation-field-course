# Extraction eval — smart_intake_output

Documents: 240 · fields scored: 788 · run file: `data-room/extraction/smart_intake_output.csv`

## Headline

- Field accuracy: **81.7%** (644 of 788; 95% interval 78.9–84.3%)
- Critical fields (dates, amounts, currency): **83.0%** of 571
- Documents with every field right (no correction needed): **61.7%** of 240
- Errors: 47 blank, 97 wrong value (a wrong value is worse: it looks filled in)
- Extra fields returned that were not asked for: 45 (fields: free_text_notes)

## By field type

| Type | Fields | Accuracy |
|---|---|---|
| amount | 290 | 84.1% |
| currency | 41 | 87.8% |
| date | 240 | 80.8% |
| identifier | 217 | 78.3% |

## Fairness slices

Accuracy per group with a 95% interval. *Ratio* = the group's accuracy divided by the best group's (groups with at least 30 scored fields). Read a low ratio together with its interval and the stratified table below before you call it a language effect.

### doc_language

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| ar | 166 | 59.6% | 52.0–66.8% | 0.67 |
| en | 96 | 89.6% | 81.9–94.2% | 1.00 |
| he | 396 | 88.4% | 84.9–91.2% | 0.99 |
| ru | 130 | 83.8% | 76.6–89.2% | 0.94 |

### claimant_language

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| ar | 178 | 61.8% | 54.5–68.6% | 0.69 |
| en | 100 | 89.0% | 81.4–93.7% | 1.00 |
| he | 368 | 88.0% | 84.3–91.0% | 0.99 |
| ru | 142 | 85.2% | 78.4–90.1% | 0.96 |

### region

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| Center | 241 | 86.7% | 81.9–90.4% | 1.00 |
| Jerusalem | 85 | 83.5% | 74.2–89.9% | 0.96 |
| North | 262 | 77.1% | 71.6–81.8% | 0.89 |
| South | 109 | 76.1% | 67.3–83.2% | 0.88 |
| Tel Aviv | 91 | 86.8% | 78.4–92.3% | 1.00 |

### claimant_age_band

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| 18-24 | 45 | 82.2% | 68.7–90.7% | 0.92 |
| 25-34 | 123 | 76.4% | 68.2–83.1% | 0.85 |
| 35-44 | 157 | 89.8% | 84.1–93.6% | 1.00 |
| 45-54 | 193 | 80.8% | 74.7–85.8% | 0.90 |
| 55-64 | 146 | 78.8% | 71.4–84.6% | 0.88 |
| 65-74 | 80 | 80.0% | 70.0–87.3% | 0.89 |
| 75+ | 44 | 84.1% | 70.6–92.1% | 0.94 |

### capture_channel

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| app_photo | 252 | 76.2% | 70.6–81.0% | 0.83 |
| email_pdf | 232 | 91.8% | 87.6–94.7% | 1.00 |
| fax | 36 | 72.2% | 56.0–84.2% | 0.79 |
| scanner_haifa | 105 | 69.5% | 60.2–77.5% | 0.76 |
| scanner_ramat_gan | 163 | 85.9% | 79.7–90.4% | 0.94 |

### form_filled

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| handwritten | 109 | 64.2% | 54.9–72.6% | 0.71 |
| printed | 565 | 83.4% | 80.1–86.2% | 0.92 |
| typed | 114 | 90.4% | 83.5–94.5% | 1.00 |

### doc_type

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| assessor_report | 50 | 88.0% | 76.2–94.4% | 0.90 |
| claim_form | 223 | 77.6% | 71.7–82.6% | 0.80 |
| contractor_invoice | 100 | 86.0% | 77.9–91.5% | 0.88 |
| garage_invoice | 180 | 77.2% | 70.6–82.7% | 0.79 |
| health_receipt | 90 | 81.1% | 71.8–87.9% | 0.83 |
| medical_invoice_abroad | 105 | 85.7% | 77.8–91.1% | 0.88 |
| police_confirmation | 40 | 97.5% | 87.1–99.6% | 1.00 |

## Stratified: document language × capture channel

| Language | Capture | Fields | Accuracy |
|---|---|---|---|
| ar | app_photo | 53 | 47.2% |
| ar | email_pdf | 30 | 73.3% |
| ar | fax | 10 | 50.0% |
| ar | scanner_haifa | 47 | 63.8% |
| ar | scanner_ramat_gan | 26 | 65.4% |
| en | app_photo | 43 | 81.4% |
| en | email_pdf | 45 | 95.6% |
| en | scanner_ramat_gan | 8 | 100.0% |
| he | app_photo | 111 | 86.5% |
| he | email_pdf | 110 | 97.3% |
| he | fax | 22 | 77.3% |
| he | scanner_haifa | 50 | 76.0% |
| he | scanner_ramat_gan | 103 | 89.3% |
| ru | app_photo | 45 | 80.0% |
| ru | email_pdf | 47 | 87.2% |
| ru | fax | 4 | 100.0% |
| ru | scanner_haifa | 8 | 62.5% |
| ru | scanner_ramat_gan | 26 | 88.5% |

## Errors (first 40)

| doc | type | lang | capture | field | gold | run |
|---|---|---|---|---|---|---|
| D004 | claim_form | ar | app_photo | policy_number | 55-6304852 | 51-6304852 |
| D006 | garage_invoice | he | scanner_haifa | invoice_number | 74184 | 04184 |
| D009 | claim_form | ru | app_photo | loss_date | 2026-09-26 | (blank) |
| D016 | contractor_invoice | he | app_photo | invoice_date | 2026-09-13 | 2026-09-16 |
| D017 | garage_invoice | ar | scanner_haifa | invoice_number | 91451 | 92451 |
| D017 | garage_invoice | ar | scanner_haifa | total_amount | 5065.81 | (blank) |
| D021 | claim_form | he | scanner_ramat_gan | vehicle_plate | 58-708-47 | 58-708-57 |
| D022 | garage_invoice | ar | scanner_ramat_gan | invoice_number | 55211 | (blank) |
| D022 | garage_invoice | ar | scanner_ramat_gan | total_amount | 4815.11 | (blank) |
| D026 | garage_invoice | ar | app_photo | total_amount | 21694.19 | 2169.42 |
| D026 | garage_invoice | ar | app_photo | vat_amount | 3309.28 | 330.93 |
| D027 | health_receipt | ar | app_photo | receipt_number | 10319 | (blank) |
| D027 | health_receipt | ar | app_photo | service_date | 2026-08-20 | (blank) |
| D029 | claim_form | he | scanner_ramat_gan | loss_date | 2026-10-17 | 2026-10-18 |
| D029 | claim_form | he | scanner_ramat_gan | policy_number | 55-4232370 | 56-4232370 |
| D030 | contractor_invoice | ar | scanner_haifa | invoice_date | 2026-10-04 | 2026-10-05 |
| D032 | garage_invoice | ar | scanner_haifa | total_amount | 4238.89 | 423.89 |
| D035 | garage_invoice | ar | app_photo | invoice_date | 2026-10-24 | (blank) |
| D035 | garage_invoice | ar | app_photo | total_amount | 8089.01 | (blank) |
| D035 | garage_invoice | ar | app_photo | vat_amount | 1233.92 | 4233.92 |
| D036 | health_receipt | he | app_photo | receipt_number | 27902 | 27905 |
| D039 | claim_form | he | app_photo | policy_number | 31-8717789 | 31-8317789 |
| D039 | claim_form | he | app_photo | vehicle_plate | 42-770-80 | 52-770-80 |
| D041 | garage_invoice | ar | scanner_haifa | invoice_number | 29156 | 29756 |
| D041 | garage_invoice | ar | scanner_haifa | vat_amount | 1702.68 | (blank) |
| D042 | medical_invoice_abroad | en | app_photo | currency | THB | USD |
| D042 | medical_invoice_abroad | en | app_photo | service_date | 2026-10-02 | 2026-10-01 |
| D042 | medical_invoice_abroad | en | app_photo | total_amount | 22605.44 | 22905.44 |
| D046 | medical_invoice_abroad | en | app_photo | service_date | 2026-09-06 | 2026-06-09 |
| D056 | medical_invoice_abroad | en | email_pdf | service_date | 2026-09-02 | 2026-02-09 |
| D057 | medical_invoice_abroad | ru | email_pdf | currency | GEL | USD |
| D058 | claim_form | ar | app_photo | claimed_amount | 7900.00 | (blank) |
| D058 | claim_form | ar | app_photo | loss_date | 2026-09-23 | (blank) |
| D058 | claim_form | ar | app_photo | policy_number | 31-5378750 | (blank) |
| D058 | claim_form | ar | app_photo | vehicle_plate | 31-880-52 | (blank) |
| D063 | claim_form | he | app_photo | vehicle_plate | 99-383-15 | 92-383-15 |
| D064 | garage_invoice | he | scanner_haifa | invoice_number | 24775 | 24375 |
| D065 | medical_invoice_abroad | ru | app_photo | service_date | 2026-08-17 | 2026-08-18 |
| D068 | claim_form | ru | scanner_ramat_gan | loss_date | 2026-10-14 | (blank) |
| D072 | assessor_report | he | scanner_haifa | inspection_date | 2026-09-12 | 2026-09-13 |

## Extra fields (data minimisation)

| doc | field | value |
|---|---|---|
| D024 | free_text_notes | Dx: acute gastroenteritis |
| D025 | free_text_notes | Dx: растяжение связок голеностопа |
| D042 | free_text_notes | Dx: lower back pain |
| D044 | free_text_notes | Dx: катаракта, осмотр |
| D046 | free_text_notes | Dx: otitis media |
| D051 | free_text_notes | Dx: otitis media |
| D055 | free_text_notes | Dx: acute gastroenteritis |
| D056 | free_text_notes | Dx: sprained ankle, X-ray negative |
| D057 | free_text_notes | Dx: отит |
| D065 | free_text_notes | Dx: пищевое отравление |
| D081 | free_text_notes | Dx: острый гастроэнтерит |
| D084 | free_text_notes | Dx: lower back pain |
| D094 | free_text_notes | Dx: sprained ankle, X-ray negative |
| D095 | free_text_notes | Dx: sprained ankle, X-ray negative |
| D099 | free_text_notes | Dx: otitis media |
| D100 | free_text_notes | Dx: כאבי גב תחתון |
| D101 | free_text_notes | Dx: боль в спине |
| D105 | free_text_notes | Dx: التهاب الحلق |
| D110 | free_text_notes | Dx: sprained ankle, X-ray negative |
| D114 | free_text_notes | Dx: растяжение связок голеностопа |
| D115 | free_text_notes | Dx: боль в спине |
| D118 | free_text_notes | Dx: בדיקת עיניים - קטרקט |
| D129 | free_text_notes | Dx: lower back pain |
| D136 | free_text_notes | Dx: otitis media |
| D141 | free_text_notes | Dx: التهاب الحلق |
| D145 | free_text_notes | Dx: растяжение связок голеностопа |
| D149 | free_text_notes | Dx: растяжение связок голеностопа |
| D152 | free_text_notes | Dx: acute gastroenteritis |
| D158 | free_text_notes | Dx: пищевое отравление |
| D159 | free_text_notes | Dx: растяжение связок голеностопа |
