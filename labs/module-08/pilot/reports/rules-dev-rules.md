# Eval: rules-dev-rules

Run: none · rules · prompt rules-1.0 · deterministic  
Set: dev (300 tickets)

## Intent

Accuracy: **80.3%**

| label                  |   n |   precision_% |   recall_% |
|:-----------------------|----:|--------------:|-----------:|
| complaint_legal        |   4 |         100   |       75   |
| defect_damage          |  23 |         100   |       82.6 |
| exchange               |  14 |         100   |      100   |
| fee_dispute            |  28 |          75   |       75   |
| order_change_cancel    |  22 |         100   |      100   |
| other                  |  16 |          23.5 |      100   |
| payment_invoice        |  12 |         100   |      100   |
| product_question       |  19 |         100   |       73.7 |
| refund_status          |  31 |         100   |       67.7 |
| return_policy_question |  29 |         100   |       79.3 |
| return_request         |  44 |         100   |       63.6 |
| wismo                  |  58 |         100   |       82.8 |

By language

| language   |   n |   accuracy |
|:-----------|----:|-----------:|
| ru         |  27 |       66.7 |
| he         | 218 |       79.8 |
| en         |  18 |       83.3 |
| ar         |  36 |       91.7 |
| am         |   1 |      100   |

## Decision

All tickets: **87.7%**  
Returns tickets (a decision under the policy is due, n = 138): **81.2%**

Per decision

| label                |   n |   precision_% |   recall_% |
|:---------------------|----:|--------------:|-----------:|
| escalate_counsel     |   4 |         100   |       75   |
| exchange_free        |  11 |         100   |      100   |
| excluded_custom      |   5 |         100   |       80   |
| n/a                  | 127 |          77.4 |      100   |
| outside_window       |  18 |         100   |       72.2 |
| refund_4m_verify     |   4 |         100   |       75   |
| refund_minus_fee     |  72 |         100   |       79.2 |
| refund_no_fee_pickup |  28 |         100   |       85.7 |
| status_update        |  31 |         100   |       67.7 |

Returns tickets by language

| language   |   n |   accuracy |
|:-----------|----:|-----------:|
| ru         |  15 |       66.7 |
| en         |   7 |       71.4 |
| he         | 100 |       82   |
| ar         |  16 |       93.8 |

Confusion on returns tickets (rows expected, columns predicted)

| expected             |   exchange_free |   excluded_custom |   n/a |   outside_window |   refund_4m_verify |   refund_minus_fee |   refund_no_fee_pickup |
|:---------------------|----------------:|------------------:|------:|-----------------:|-------------------:|-------------------:|-----------------------:|
| exchange_free        |              11 |                 0 |     0 |                0 |                  0 |                  0 |                      0 |
| excluded_custom      |               0 |                 4 |     1 |                0 |                  0 |                  0 |                      0 |
| outside_window       |               0 |                 0 |     5 |               13 |                  0 |                  0 |                      0 |
| refund_4m_verify     |               0 |                 0 |     1 |                0 |                  3 |                  0 |                      0 |
| refund_minus_fee     |               0 |                 0 |    15 |                0 |                  0 |                 57 |                      0 |
| refund_no_fee_pickup |               0 |                 0 |     4 |                0 |                  0 |                  0 |                     24 |

## Fee

Right decision and right fee: 60 of 76 (78.9%)

## Escalation

Should escalate: 20; caught 11 (recall 55.0%); flagged 12 (precision 91.7%)

Missed escalations

| ticket_id   | language   | escalate_reason   | cues             |
|:------------|:-----------|:------------------|:-----------------|
| T-25082     | he         | legal_threat      | opened legal     |
| T-42664     | he         | legal_threat      | opened legal     |
| T-57903     | he         | legal_threat      |                  |
| T-61032     | ar         | legal_threat      | disability legal |
| T-66320     | he         | legal_threat      | unopened legal   |
| T-67309     | he         | legal_threat      | legal            |
| T-74642     | he         | legal_threat      | opened legal     |
| T-78193     | ru         | legal_threat      | opened legal     |
| T-87437     | ar         | legal_threat      | opened legal     |

## Drafts (automatic checks)

Draft in the customer's language (Amharic: Hebrew): 88.0%  
Banned phrase (store credit only, 10%, 30 days full refund, chatbot traces): 0  
Fee above the legal cap stated: 0

## Cost

No model calls (rules and templates).

