# Eval: rules-test-rules

Run: none · rules · prompt rules-1.0 · deterministic  
Set: test (1700 tickets)

## Intent

Accuracy: **78.4%**

| label                  |   n |   precision_% |   recall_% |
|:-----------------------|----:|--------------:|-----------:|
| complaint_legal        |  37 |         100   |       70.3 |
| defect_damage          | 136 |         100   |       78.7 |
| exchange               |  73 |         100   |      100   |
| fee_dispute            |  83 |          60.2 |       78.3 |
| order_change_cancel    | 110 |         100   |      100   |
| other                  |  70 |          18.2 |      100   |
| payment_invoice        |  65 |         100   |      100   |
| product_question       | 163 |         100   |       76.1 |
| refund_status          | 210 |         100   |       70   |
| return_policy_question | 124 |          92   |       83.9 |
| return_request         | 275 |         100   |       60   |
| wismo                  | 354 |         100   |       78.2 |

By language

| language   |    n |   accuracy |
|:-----------|-----:|-----------:|
| ru         |  181 |       70.7 |
| en         |  129 |       78.3 |
| he         | 1149 |       78.8 |
| ar         |  230 |       81.7 |
| am         |   11 |      100   |

## Decision

All tickets: **87.4%**  
Returns tickets (a decision under the policy is due, n = 691): **79.6%**

Per decision

| label                |   n |   precision_% |   recall_% |
|:---------------------|----:|--------------:|-----------:|
| escalate_counsel     |  37 |         100   |       70.3 |
| exchange_free        |  60 |          96.8 |      100   |
| excluded_custom      |  17 |         100   |       88.2 |
| n/a                  | 762 |          79.3 |      100   |
| outside_window       | 111 |          93.7 |       80.2 |
| refund_4m_verify     |  13 |         100   |       84.6 |
| refund_minus_fee     | 307 |          96.9 |       80.5 |
| refund_no_fee_pickup | 183 |         100   |       69.9 |
| status_update        | 210 |         100   |       70   |

Returns tickets by language

| language   |   n |   accuracy |
|:-----------|----:|-----------:|
| ru         |  84 |       72.6 |
| en         |  52 |       76.9 |
| he         | 457 |       78.8 |
| am         |   6 |       83.3 |
| ar         |  92 |       91.3 |

Confusion on returns tickets (rows expected, columns predicted)

| expected             |   exchange_free |   excluded_custom |   n/a |   outside_window |   refund_4m_verify |   refund_minus_fee |   refund_no_fee_pickup |
|:---------------------|----------------:|------------------:|------:|-----------------:|-------------------:|-------------------:|-----------------------:|
| exchange_free        |              60 |                 0 |     0 |                0 |                  0 |                  0 |                      0 |
| excluded_custom      |               0 |                15 |     2 |                0 |                  0 |                  0 |                      0 |
| outside_window       |               0 |                 0 |    22 |               89 |                  0 |                  0 |                      0 |
| refund_4m_verify     |               0 |                 0 |     1 |                1 |                 11 |                  0 |                      0 |
| refund_minus_fee     |               0 |                 0 |    60 |                0 |                  0 |                247 |                      0 |
| refund_no_fee_pickup |               2 |                 0 |    40 |                5 |                  0 |                  8 |                    128 |

## Fee

Right decision and right fee: 258 of 320 (80.6%)

## Escalation

Should escalate: 85; caught 58 (recall 68.2%); flagged 67 (precision 86.6%)

Missed escalations

| ticket_id   | language   | escalate_reason   | cues                     |
|:------------|:-----------|:------------------|:-------------------------|
| T-10259     | he         | legal_threat      | opened legal             |
| T-14575     | en         | legal_threat      |                          |
| T-14603     | he         | legal_threat      | opened legal             |
| T-14962     | he         | legal_threat      | opened age legal         |
| T-15636     | he         | legal_threat      | opened legal             |
| T-31829     | ar         | legal_threat      | legal                    |
| T-36649     | he         | legal_threat      |                          |
| T-40866     | ru         | legal_threat      | immigrant legal          |
| T-43342     | he         | legal_threat      | age                      |
| T-44955     | he         | legal_threat      |                          |
| T-48342     | he         | legal_threat      | opened phone_order legal |
| T-53976     | ar         | legal_threat      | opened legal             |
| T-54796     | he         | legal_threat      |                          |
| T-56339     | he         | legal_threat      | age                      |
| T-62135     | he         | legal_threat      | opened legal             |
| T-63336     | he         | legal_threat      | opened legal             |
| T-63569     | he         | legal_threat      | legal                    |
| T-67481     | he         | legal_threat      |                          |
| T-75847     | en         | legal_threat      | immigrant legal          |
| T-76115     | he         | legal_threat      |                          |
| T-76981     | he         | legal_threat      | opened legal             |
| T-78145     | en         | legal_threat      | immigrant legal          |
| T-83360     | he         | legal_threat      |                          |
| T-89527     | en         | legal_threat      |                          |
| T-90640     | he         | legal_threat      | opened legal             |
| T-90780     | he         | legal_threat      | legal                    |
| T-90931     | he         | legal_threat      | immigrant                |

## Drafts (automatic checks)

Draft in the customer's language (Amharic: Hebrew): 88.8%  
Banned phrase (store credit only, 10%, 30 days full refund, chatbot traces): 0  
Fee above the legal cap stated: 0

## Cost

No model calls (rules and templates).

## Today (the agents' real replies, coded)

Returns tickets where today's reply matches the policy decision: **55.6%** (n = 691)  
Returns tickets where today's reply gives the customer less than the law: **32.7%**

Today's replies on returns tickets

| today_decision     |   tickets |
|:-------------------|----------:|
| refuse_window      |       116 |
| pickup_no_fee      |       113 |
| refund_legal_fee   |       102 |
| store_credit       |        94 |
| customer_ships     |        65 |
| refund_no_fee      |        61 |
| exchange_ok        |        60 |
| refund_minus_10pct |        46 |
| goodwill_credit    |        34 |

By language (matches policy)

| language   |   n |   share |
|:-----------|----:|--------:|
| am         |   6 |   0.667 |
| ar         |  92 |   0.652 |
| en         |  52 |   0.462 |
| he         | 457 |   0.547 |
| ru         |  84 |   0.548 |

Agent replies with a banned phrase: 140 of 1700

