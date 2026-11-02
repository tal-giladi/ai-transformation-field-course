# Extraction eval — smart_intake_output

Documents: 200 · fields scored: 654 · run file: `data-room/extraction/smart_intake_output.csv`

## Headline

- Field accuracy: **82.1%** (537 of 654; 95% interval 79.0–84.9%)
- Critical fields (dates, amounts, currency): **82.9%** of 475
- Documents with every field right (no correction needed): **60.5%** of 200
- Errors: 34 blank, 83 wrong value (a wrong value is worse: it looks filled in)
- Extra fields returned that were not asked for: 37 (fields: free_text_notes)

## By field type

| Type | Fields | Accuracy |
|---|---|---|
| amount | 241 | 84.6% |
| currency | 34 | 88.2% |
| date | 200 | 80.0% |
| identifier | 179 | 79.9% |

## Fairness slices

Accuracy per group with a 95% interval. *Ratio* = the group's accuracy divided by the best group's (groups with at least 30 scored fields). Read a low ratio together with its interval and the stratified table below before you call it a language effect.

### doc_language

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| ar | 135 | 62.2% | 53.8–70.0% | 0.68 |
| en | 80 | 91.2% | 83.0–95.7% | 1.00 |
| he | 334 | 88.6% | 84.8–91.6% | 0.97 |
| ru | 105 | 80.0% | 71.4–86.5% | 0.88 |

### claimant_language

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| ar | 145 | 64.1% | 56.1–71.5% | 0.71 |
| en | 84 | 90.5% | 82.3–95.1% | 1.00 |
| he | 308 | 88.3% | 84.2–91.4% | 0.98 |
| ru | 117 | 82.1% | 74.1–88.0% | 0.91 |

### region

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| Center | 200 | 86.0% | 80.5–90.1% | 0.96 |
| Jerusalem | 69 | 89.9% | 80.5–95.0% | 1.00 |
| North | 226 | 74.3% | 68.3–79.6% | 0.83 |
| South | 86 | 86.0% | 77.2–91.8% | 0.96 |
| Tel Aviv | 73 | 83.6% | 73.4–90.3% | 0.93 |

### claimant_age_band

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| 18-24 | 41 | 80.5% | 66.0–89.8% | 0.92 |
| 25-34 | 91 | 82.4% | 73.3–88.9% | 0.94 |
| 35-44 | 123 | 87.8% | 80.9–92.5% | 1.00 |
| 45-54 | 174 | 82.2% | 75.8–87.2% | 0.94 |
| 55-64 | 120 | 76.7% | 68.3–83.3% | 0.87 |
| 65-74 | 69 | 82.6% | 72.0–89.8% | 0.94 |
| 75+ | 36 | 80.6% | 65.0–90.2% | 0.92 |

### capture_channel

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| app_photo | 206 | 79.1% | 73.1–84.1% | 0.87 |
| email_pdf | 202 | 90.6% | 85.8–93.9% | 1.00 |
| fax | 27 | 63.0% | 44.2–78.5% | n<30 |
| scanner_haifa | 91 | 67.0% | 56.9–75.8% | 0.74 |
| scanner_ramat_gan | 128 | 88.3% | 81.6–92.8% | 0.97 |

### form_filled

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| handwritten | 89 | 64.0% | 53.7–73.2% | 0.69 |
| printed | 470 | 83.4% | 79.8–86.5% | 0.90 |
| typed | 95 | 92.6% | 85.6–96.4% | 1.00 |

### doc_type

| Group | Fields | Accuracy | 95% interval | Ratio to best |
|---|---|---|---|---|
| assessor_report | 42 | 88.1% | 75.0–94.8% | 0.88 |
| claim_form | 184 | 78.8% | 72.3–84.1% | 0.79 |
| contractor_invoice | 80 | 83.8% | 74.2–90.3% | 0.84 |
| garage_invoice | 152 | 77.6% | 70.4–83.5% | 0.78 |
| health_receipt | 75 | 81.3% | 71.1–88.5% | 0.81 |
| medical_invoice_abroad | 87 | 86.2% | 77.4–91.9% | 0.86 |
| police_confirmation | 34 | 100.0% | 89.8–100.0% | 1.00 |

## Stratified: document language × capture channel

| Language | Capture | Fields | Accuracy |
|---|---|---|---|
| ar | app_photo | 42 | 57.1% |
| ar | email_pdf | 26 | 69.2% |
| ar | fax | 10 | 50.0% |
| ar | scanner_haifa | 43 | 60.5% |
| ar | scanner_ramat_gan | 14 | 78.6% |
| en | app_photo | 34 | 85.3% |
| en | email_pdf | 42 | 95.2% |
| en | scanner_ramat_gan | 4 | 100.0% |
| he | app_photo | 95 | 88.4% |
| he | email_pdf | 94 | 96.8% |
| he | fax | 17 | 70.6% |
| he | scanner_haifa | 44 | 77.3% |
| he | scanner_ramat_gan | 84 | 89.3% |
| ru | app_photo | 35 | 74.3% |
| ru | email_pdf | 40 | 85.0% |
| ru | scanner_haifa | 4 | 25.0% |
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
| D026 | garage_invoice | ar | app_photo | total_amount | 21694.19 | 2169.42 |
| D026 | garage_invoice | ar | app_photo | vat_amount | 3309.28 | 330.93 |
| D027 | health_receipt | ar | app_photo | receipt_number | 10319 | (blank) |
| D027 | health_receipt | ar | app_photo | service_date | 2026-08-20 | (blank) |
| D029 | claim_form | he | scanner_ramat_gan | loss_date | 2026-10-17 | 2026-10-18 |
| D029 | claim_form | he | scanner_ramat_gan | policy_number | 55-4232370 | 56-4232370 |
| D030 | contractor_invoice | ar | scanner_haifa | invoice_date | 2026-10-04 | 2026-10-05 |
| D032 | garage_invoice | ar | scanner_haifa | total_amount | 4238.89 | 423.89 |
| D036 | health_receipt | he | app_photo | receipt_number | 27902 | 27905 |
| D041 | garage_invoice | ar | scanner_haifa | invoice_number | 29156 | 29756 |
| D041 | garage_invoice | ar | scanner_haifa | vat_amount | 1702.68 | (blank) |
| D046 | medical_invoice_abroad | en | app_photo | service_date | 2026-09-06 | 2026-06-09 |
| D056 | medical_invoice_abroad | en | email_pdf | service_date | 2026-09-02 | 2026-02-09 |
| D057 | medical_invoice_abroad | ru | email_pdf | currency | GEL | USD |
| D063 | claim_form | he | app_photo | vehicle_plate | 99-383-15 | 92-383-15 |
| D065 | medical_invoice_abroad | ru | app_photo | service_date | 2026-08-17 | 2026-08-18 |
| D068 | claim_form | ru | scanner_ramat_gan | loss_date | 2026-10-14 | (blank) |
| D072 | assessor_report | he | scanner_haifa | inspection_date | 2026-09-12 | 2026-09-13 |
| D076 | assessor_report | he | fax | inspection_date | 2026-10-13 | 2026-10-14 |
| D078 | claim_form | ar | app_photo | loss_date | 2026-09-25 | 2026-09-26 |
| D080 | garage_invoice | he | scanner_haifa | total_amount | 8554.17 | 855.42 |
| D083 | garage_invoice | he | scanner_ramat_gan | invoice_date | 2026-09-08 | 2026-09-07 |
| D085 | garage_invoice | ar | scanner_haifa | invoice_date | 2026-09-27 | (blank) |
| D085 | garage_invoice | ar | scanner_haifa | invoice_number | 53980 | 53580 |
| D085 | garage_invoice | ar | scanner_haifa | total_amount | 3300.45 | (blank) |
| D085 | garage_invoice | ar | scanner_haifa | vat_amount | 503.46 | (blank) |
| D087 | claim_form | he | scanner_haifa | claimed_amount | 10570.00 | (blank) |
| D087 | claim_form | he | scanner_haifa | vehicle_plate | 66-980-15 | 66-580-15 |
| D090 | claim_form | ar | email_pdf | claimed_amount | 3790.00 | 379.00 |
| D090 | claim_form | ar | email_pdf | loss_date | 2026-10-09 | 2026-09-29 |
| D090 | claim_form | ar | email_pdf | policy_number | 42-7505387 | 42-7105387 |
| D091 | garage_invoice | ar | app_photo | vat_amount | 772.34 | (blank) |
| D100 | health_receipt | he | app_photo | service_date | 2026-09-27 | 2026-09-28 |
| D100 | health_receipt | he | app_photo | total_amount | 520.00 | 720.00 |

## Extra fields (data minimisation)

| doc | field | value |
|---|---|---|
| D024 | free_text_notes | Dx: acute gastroenteritis |
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
| D100 | free_text_notes | Dx: כאבי גב תחתון |
| D101 | free_text_notes | Dx: боль в спине |
| D110 | free_text_notes | Dx: sprained ankle, X-ray negative |
| D114 | free_text_notes | Dx: растяжение связок голеностопа |
| D115 | free_text_notes | Dx: боль в спине |
| D118 | free_text_notes | Dx: בדיקת עיניים - קטרקט |
| D129 | free_text_notes | Dx: lower back pain |
| D136 | free_text_notes | Dx: otitis media |
| D141 | free_text_notes | Dx: التهاب الحلق |
| D149 | free_text_notes | Dx: растяжение связок голеностопа |
| D152 | free_text_notes | Dx: acute gastroenteritis |
| D158 | free_text_notes | Dx: пищевое отравление |
| D159 | free_text_notes | Dx: растяжение связок голеностопа |
| D171 | free_text_notes | Dx: отит |
| D172 | free_text_notes | Dx: דלקת גרון |
| D175 | free_text_notes | Dx: острый гастроэнтерит |
| D177 | free_text_notes | Dx: lower back pain |
| D189 | free_text_notes | Dx: acute gastroenteritis |
| D201 | free_text_notes | Dx: lower back pain |
