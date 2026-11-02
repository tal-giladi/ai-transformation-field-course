# Eval: rules-track-a-rules

Run: none · rules · prompt rules-1.0 · deterministic  
Set: track-a (200 tickets)

## Intent

Accuracy: **81.5%**

| label                  |   n |   precision_% |   recall_% |
|:-----------------------|----:|--------------:|-----------:|
| complaint_legal        |   4 |         100   |      100   |
| defect_damage          |  21 |         100   |       81   |
| exchange               |   4 |         100   |      100   |
| fee_dispute            |  10 |          61.5 |       80   |
| order_change_cancel    |  16 |         100   |      100   |
| other                  |  11 |          26.2 |      100   |
| payment_invoice        |   8 |         100   |      100   |
| product_question       |  20 |         100   |       80   |
| refund_status          |  20 |         100   |       75   |
| return_policy_question |  14 |          92.3 |       85.7 |
| return_request         |  31 |         100   |       58.1 |
| wismo                  |  41 |         100   |       82.9 |

By language

| language   |   n |   accuracy |
|:-----------|----:|-----------:|
| ru         |  35 |       74.3 |
| ar         |  40 |       82.5 |
| he         | 100 |       83   |
| en         |  25 |       84   |

## Decision

All tickets: **89.5%**  
Returns tickets (a decision under the policy is due, n = 80): **80.0%**

Per decision

| label                |   n |   precision_% |   recall_% |
|:---------------------|----:|--------------:|-----------:|
| escalate_counsel     |   4 |         100   |      100   |
| exchange_free        |   3 |         100   |      100   |
| excluded_custom      |   5 |         100   |       60   |
| n/a                  |  96 |          82.8 |      100   |
| outside_window       |  16 |         100   |       81.2 |
| refund_4m_verify     |   1 |         100   |      100   |
| refund_minus_fee     |  31 |          96.2 |       80.6 |
| refund_no_fee_pickup |  24 |         100   |       79.2 |
| status_update        |  20 |         100   |       75   |

Returns tickets by language

| language   |   n |   accuracy |
|:-----------|----:|-----------:|
| he         |  33 |       75.8 |
| en         |   9 |       77.8 |
| ru         |  21 |       81   |
| ar         |  17 |       88.2 |

Confusion on returns tickets (rows expected, columns predicted)

| expected             |   exchange_free |   excluded_custom |   n/a |   outside_window |   refund_4m_verify |   refund_minus_fee |   refund_no_fee_pickup |
|:---------------------|----------------:|------------------:|------:|-----------------:|-------------------:|-------------------:|-----------------------:|
| exchange_free        |               3 |                 0 |     0 |                0 |                  0 |                  0 |                      0 |
| excluded_custom      |               0 |                 3 |     2 |                0 |                  0 |                  0 |                      0 |
| outside_window       |               0 |                 0 |     3 |               13 |                  0 |                  0 |                      0 |
| refund_4m_verify     |               0 |                 0 |     0 |                0 |                  1 |                  0 |                      0 |
| refund_minus_fee     |               0 |                 0 |     6 |                0 |                  0 |                 25 |                      0 |
| refund_no_fee_pickup |               0 |                 0 |     4 |                0 |                  0 |                  1 |                     19 |

## Fee

Right decision and right fee: 26 of 32 (81.2%)

## Escalation

Should escalate: 11; caught 9 (recall 81.8%); flagged 9 (precision 100.0%)

Missed escalations

| ticket_id   | language   | escalate_reason   | cues             |
|:------------|:-----------|:------------------|:-----------------|
| T-14962     | he         | legal_threat      | opened age legal |
| T-75847     | en         | legal_threat      | immigrant legal  |

## Drafts (automatic checks)

Draft in the customer's language (Amharic: Hebrew): 90.0%  
Banned phrase (store credit only, 10%, 30 days full refund, chatbot traces): 0  
Fee above the legal cap stated: 0

## Cost

No model calls (rules and templates).

## Today (the agents' real replies, coded)

Returns tickets where today's reply matches the policy decision: **61.3%** (n = 80)  
Returns tickets where today's reply gives the customer less than the law: **26.2%**

Today's replies on returns tickets

| today_decision     |   tickets |
|:-------------------|----------:|
| pickup_no_fee      |        20 |
| refuse_window      |        16 |
| refund_minus_10pct |        10 |
| refund_legal_fee   |        10 |
| goodwill_credit    |         6 |
| store_credit       |         6 |
| refund_no_fee      |         5 |
| customer_ships     |         4 |
| exchange_ok        |         3 |

By language (matches policy)

| language   |   n |   share |
|:-----------|----:|--------:|
| ar         |  17 |   0.765 |
| en         |   9 |   0.444 |
| he         |  33 |   0.667 |
| ru         |  21 |   0.476 |

Agent replies with a banned phrase: 16 of 200

