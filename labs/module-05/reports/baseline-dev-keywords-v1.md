# Eval: baseline-dev-keywords-v1

Run: baseline · keywords-v1 · prompt v- · 2026-11-02 16:36  
Set: dev-set.csv (200 items)

## Triage (category)

Items: 200  
Accuracy: 99.5%

### Per label

| label            |   n |   precision_% |   recall_% |
|:-----------------|----:|--------------:|-----------:|
| assembly         |  11 |         100   |      100   |
| b2b_quote        |   6 |         100   |      100   |
| complaint        |   7 |         100   |      100   |
| damage           |  17 |         100   |      100   |
| invoice          |   8 |         100   |      100   |
| other            |  18 |         100   |      100   |
| product_question |  29 |         100   |      100   |
| reschedule       |   6 |         100   |      100   |
| returns          |  10 |          90.9 |      100   |
| spam             |  12 |         100   |      100   |
| wismo            |  76 |         100   |       98.7 |

### By expected_language

| expected_language   |   n |   accuracy |
|:--------------------|----:|-----------:|
| ru                  |  29 |       96.6 |
| ar                  |  26 |      100   |
| en                  |  25 |      100   |
| he                  | 120 |      100   |

### First failures

| item_id   | expected   | predicted   | correct   | expected_language   | pred_language   | pred_reply_language   | pred_flags   | draft   |
|:----------|:-----------|:------------|:----------|:--------------------|:----------------|:----------------------|:-------------|:--------|
| D-165     | wismo      | returns     | False     | ru                  | ru              | ru                    |              |         |

### Confusion (rows = expected, columns = predicted)

| expected         |   assembly |   b2b_quote |   complaint |   damage |   invoice |   other |   product_question |   reschedule |   returns |   spam |   wismo |   total |
|:-----------------|-----------:|------------:|------------:|---------:|----------:|--------:|-------------------:|-------------:|----------:|-------:|--------:|--------:|
| assembly         |         11 |           0 |           0 |        0 |         0 |       0 |                  0 |            0 |         0 |      0 |       0 |      11 |
| b2b_quote        |          0 |           6 |           0 |        0 |         0 |       0 |                  0 |            0 |         0 |      0 |       0 |       6 |
| complaint        |          0 |           0 |           7 |        0 |         0 |       0 |                  0 |            0 |         0 |      0 |       0 |       7 |
| damage           |          0 |           0 |           0 |       17 |         0 |       0 |                  0 |            0 |         0 |      0 |       0 |      17 |
| invoice          |          0 |           0 |           0 |        0 |         8 |       0 |                  0 |            0 |         0 |      0 |       0 |       8 |
| other            |          0 |           0 |           0 |        0 |         0 |      18 |                  0 |            0 |         0 |      0 |       0 |      18 |
| product_question |          0 |           0 |           0 |        0 |         0 |       0 |                 29 |            0 |         0 |      0 |       0 |      29 |
| reschedule       |          0 |           0 |           0 |        0 |         0 |       0 |                  0 |            6 |         0 |      0 |       0 |       6 |
| returns          |          0 |           0 |           0 |        0 |         0 |       0 |                  0 |            0 |        10 |      0 |       0 |      10 |
| spam             |          0 |           0 |           0 |        0 |         0 |       0 |                  0 |            0 |         0 |     12 |       0 |      12 |
| wismo            |          0 |           0 |           0 |        0 |         0 |       0 |                  0 |            0 |         1 |      0 |      75 |      76 |
| total            |         11 |           6 |           7 |       17 |         8 |      18 |                 29 |            6 |        11 |     12 |      75 |     200 |

## Language

Message language right: 100.0%  
Reply language right: 100.0%

## Flags

Messages sent to a senior agent by a flag: 0 of 200 (0.0%) — every one is extra review load (05.5)

## Draft checks (automatic)

This run has no drafts (baseline or mock): only triage and language are scored.

## Cost

Mean tokens per item: 0 in, 0 out  
Prices: no price for this model: pass --price-in and --price-out  
