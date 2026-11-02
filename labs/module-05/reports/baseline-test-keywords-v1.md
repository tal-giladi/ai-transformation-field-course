# Eval: baseline-test-keywords-v1

Run: baseline · keywords-v1 · prompt v- · 2026-11-02 19:35  
Set: test-set.csv (400 items)

## Triage (category)

Items: 400  
Accuracy: 98.2%

### Per label

| label            |   n |   precision_% |   recall_% |
|:-----------------|----:|--------------:|-----------:|
| assembly         |  22 |         100   |      100   |
| b2b_quote        |  13 |         100   |      100   |
| complaint        |  14 |         100   |       92.9 |
| damage           |  36 |          97.3 |      100   |
| invoice          |  17 |         100   |      100   |
| other            |  37 |          90.2 |      100   |
| product_question |  56 |         100   |      100   |
| reschedule       |  12 |         100   |      100   |
| returns          |  19 |          90.5 |      100   |
| spam             |  23 |         100   |       87   |
| wismo            | 151 |         100   |       98   |

### By expected_language

| expected_language   |   n |   accuracy |
|:--------------------|----:|-----------:|
| ru                  |  58 |       94.8 |
| he                  | 239 |       98.3 |
| en                  |  53 |      100   |
| ar                  |  50 |      100   |

### First failures

| item_id   | expected   | predicted   | correct   | expected_language   | pred_language   | pred_reply_language   | pred_flags   | draft   |
|:----------|:-----------|:------------|:----------|:--------------------|:----------------|:----------------------|:-------------|:--------|
| T-024     | spam       | other       | False     | he                  | he              | he                    |              |         |
| T-046     | spam       | other       | False     | he                  | he              | he                    |              |         |
| T-105     | wismo      | returns     | False     | ru                  | ru              | ru                    |              |         |
| T-117     | spam       | other       | False     | he                  | he              | he                    |              |         |
| T-259     | complaint  | damage      | False     | he                  | he              | he                    |              |         |
| T-260     | wismo      | other       | False     | ru                  | ru              | ru                    |              |         |
| T-355     | wismo      | returns     | False     | ru                  | ru              | ru                    |              |         |

### Confusion (rows = expected, columns = predicted)

| expected         |   assembly |   b2b_quote |   complaint |   damage |   invoice |   other |   product_question |   reschedule |   returns |   spam |   wismo |   total |
|:-----------------|-----------:|------------:|------------:|---------:|----------:|--------:|-------------------:|-------------:|----------:|-------:|--------:|--------:|
| assembly         |         22 |           0 |           0 |        0 |         0 |       0 |                  0 |            0 |         0 |      0 |       0 |      22 |
| b2b_quote        |          0 |          13 |           0 |        0 |         0 |       0 |                  0 |            0 |         0 |      0 |       0 |      13 |
| complaint        |          0 |           0 |          13 |        1 |         0 |       0 |                  0 |            0 |         0 |      0 |       0 |      14 |
| damage           |          0 |           0 |           0 |       36 |         0 |       0 |                  0 |            0 |         0 |      0 |       0 |      36 |
| invoice          |          0 |           0 |           0 |        0 |        17 |       0 |                  0 |            0 |         0 |      0 |       0 |      17 |
| other            |          0 |           0 |           0 |        0 |         0 |      37 |                  0 |            0 |         0 |      0 |       0 |      37 |
| product_question |          0 |           0 |           0 |        0 |         0 |       0 |                 56 |            0 |         0 |      0 |       0 |      56 |
| reschedule       |          0 |           0 |           0 |        0 |         0 |       0 |                  0 |           12 |         0 |      0 |       0 |      12 |
| returns          |          0 |           0 |           0 |        0 |         0 |       0 |                  0 |            0 |        19 |      0 |       0 |      19 |
| spam             |          0 |           0 |           0 |        0 |         0 |       3 |                  0 |            0 |         0 |     20 |       0 |      23 |
| wismo            |          0 |           0 |           0 |        0 |         0 |       1 |                  0 |            0 |         2 |      0 |     148 |     151 |
| total            |         22 |          13 |          13 |       37 |        17 |      41 |                 56 |           12 |        21 |     20 |     148 |     400 |

## Language

Message language right: 100.0%  
Reply language right: 99.2%

## Flags

Messages sent to a senior agent by a flag: 0 of 400 (0.0%) — every one is extra review load (05.5)

## Draft checks (automatic)

This run has no drafts (baseline or mock): only triage and language are scored.

## Cost

Mean tokens per item: 0 in, 0 out  
Prices: no price for this model: pass --price-in and --price-out  

## Today (same messages, no AI)

Helpdesk category field right (mapped to the pilot's categories): 64.0%  
Helpdesk auto-detected language right: 91.2%  
Messages with an agent reply: 368 of 400  
Agent replies in a language other than the customer's: 5 (1.4%)  
"Where is my order?" replies that give a date already in the past on the day they were sent: 96 of 151 (63.6%)  
Agent replies with chatbot traces: 2
