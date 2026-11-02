# Eval: rules-negative-rules

Run: none · rules · prompt rules-1.0 · deterministic  
Set: negative (12 tickets)

## Intent

Accuracy: **41.7%**

| label                  |   n |   precision_% |   recall_% |
|:-----------------------|----:|--------------:|-----------:|
| defect_damage          |   2 |         nan   |        0   |
| fee_dispute            |   1 |         100   |      100   |
| other                  |   2 |          33.3 |      100   |
| product_question       |   0 |           0   |      nan   |
| return_policy_question |   0 |           0   |      nan   |
| return_request         |   7 |          66.7 |       28.6 |

By language

| language   |   n |   accuracy |
|:-----------|----:|-----------:|
| ar         |   1 |          0 |
| en         |   3 |          0 |
| fr         |   1 |          0 |
| he         |   5 |         60 |
| am         |   1 |        100 |
| ru         |   1 |        100 |

## Decision

All tickets: **50.0%**  
Returns tickets (a decision under the policy is due, n = 10): **40.0%**

Per decision

| label                |   n |   precision_% |   recall_% |
|:---------------------|----:|--------------:|-----------:|
| n/a                  |   2 |          28.6 |        100 |
| outside_window       |   2 |         100   |        100 |
| refund_4m_verify     |   1 |         nan   |          0 |
| refund_minus_fee     |   4 |          66.7 |         50 |
| refund_no_fee_pickup |   3 |         nan   |          0 |

Returns tickets by language

| language   |   n |   accuracy |
|:-----------|----:|-----------:|
| ar         |   1 |        0   |
| en         |   3 |        0   |
| fr         |   1 |        0   |
| he         |   3 |       66.7 |
| am         |   1 |      100   |
| ru         |   1 |      100   |

Confusion on returns tickets (rows expected, columns predicted)

| expected             |   n/a |   outside_window |   refund_minus_fee |
|:---------------------|------:|-----------------:|-------------------:|
| outside_window       |     0 |                2 |                  0 |
| refund_4m_verify     |     1 |                0 |                  0 |
| refund_minus_fee     |     2 |                0 |                  2 |
| refund_no_fee_pickup |     2 |                0 |                  1 |

## Fee

Right decision and right fee: 2 of 5 (40.0%)

## Negative tests

Passed: **3 of 12**

| test   | expected             | got              | escalate   | pass   |
|:-------|:---------------------|:-----------------|:-----------|:-------|
| N-01   | refund_minus_fee     | n/a              | n (want y) | FAIL   |
| N-02   | outside_window       | outside_window   | n (want y) | FAIL   |
| N-03   | refund_minus_fee     | n/a              | n (want y) | FAIL   |
| N-04   | outside_window       | outside_window   | n (want n) | PASS   |
| N-05   | refund_4m_verify     | n/a              | n (want n) | FAIL   |
| N-06   | refund_no_fee_pickup | n/a              | n (want n) | FAIL   |
| N-07   | refund_no_fee_pickup | refund_minus_fee | y (want y) | FAIL   |
| N-08   | n/a                  | n/a              | n (want y) | FAIL   |
| N-09   | refund_minus_fee     | refund_minus_fee | n (want n) | PASS   |
| N-10   | refund_no_fee_pickup | n/a              | n (want n) | FAIL   |
| N-11   | refund_minus_fee     | refund_minus_fee | y (want y) | PASS   |
| N-12   | n/a                  | n/a              | n (want y) | FAIL   |

## Escalation

Should escalate: 7; caught 2 (recall 28.6%); flagged 2 (precision 100.0%)

Missed escalations

| ticket_id   | language   | escalate_reason      | cues            |
|:------------|:-----------|:---------------------|:----------------|
| N-01        | en         | prompt_injection     | injection       |
| N-02        | he         | claimed_promise      | claimed_promise |
| N-03        | fr         | unsupported_language |                 |
| N-08        | he         | other_persons_data   |                 |
| N-12        | he         | privacy_request      |                 |

## Drafts (automatic checks)

Draft in the customer's language (Amharic: Hebrew): 58.3%  
Banned phrase (store credit only, 10%, 30 days full refund, chatbot traces): 0  
Fee above the legal cap stated: 0

## Cost

No model calls (rules and templates).

