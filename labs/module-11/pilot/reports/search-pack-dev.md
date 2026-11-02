# Permit-FAQ eval: search-pack-dev

Questions: 40 (answer 27, route 10, clarify 3).

| Measure | Result |
|---|---|
| **Right (behaviour, facts, no outdated fact, source)** | **55.0% (n = 40)** |
| Behaviour right | 67.5% (n = 40) |
| Answer questions: right | 81.5% (n = 27) |
| Answer questions: gold facts present | 81.5% (n = 27) |
| Answer questions: outdated fact present | 0.0% (n = 27) |
| Answer questions: source on the right topic | 81.5% (n = 27) |
| Route questions: routed | 0.0% (n = 10) |
| Clarify questions: clarified | 0.0% (n = 3) |
| Reply in the question's language (he, ar, ru, en) | 100.0% (n = 38) |

## Right, by language

| language   |   n |   accuracy |
|:-----------|----:|-----------:|
| am         |   2 |        0   |
| en         |   6 |       50   |
| he         |  11 |       54.5 |
| ru         |  10 |       60   |
| ar         |  11 |       63.6 |

## Answer questions, by whether the rule changed in 2026

| changed_2026   |   n |   accuracy |
|:---------------|----:|-----------:|
| y              |  14 |       78.6 |
| n              |  13 |       84.6 |

## Behaviour: expected (rows) vs given (columns)

| expected   |   answer |   total |
|:-----------|---------:|--------:|
| answer     |       27 |      27 |
| clarify    |        3 |       3 |
| route      |       10 |      10 |
| total      |       40 |      40 |

## First failures

| question_id   | language   | intent    | expected   | predicted   | facts_ok   | stale_present   | source_ok   | sources   |
|:--------------|:-----------|:----------|:-----------|:------------|:-----------|:----------------|:------------|:----------|
| Q001          | he         | C-time    | clarify    | answer      |            | False           |             | CAF-he    |
| Q002          | ar         | SGN-min   | answer     | answer      | False      | False           | False       | CAF-ar    |
| Q003          | ar         | R-bizfee  | route      | answer      |            | False           |             | CAF-ar    |
| Q010          | ar         | C-time    | clarify    | answer      |            | False           |             | SGN-ar    |
| Q016          | am         | PRK-fee2  | route      | answer      |            | False           |             |           |
| Q020          | ru         | R-waive   | route      | answer      |            | False           |             | SGN-ru    |
| Q021          | en         | R-status  | route      | answer      |            | False           |             | DPK-en    |
| Q022          | he         | C-docs    | clarify    | answer      |            | False           |             | BIZ-he    |
| Q026          | he         | R-waive   | route      | answer      |            | False           |             | SGN-he    |
| Q027          | he         | R-status  | route      | answer      |            | False           |             | SKP-he    |
| Q028          | ru         | CAF-fee   | answer     | answer      | False      | False           | False       | SKP-ru    |
| Q032          | ru         | R-fine    | route      | answer      |            | False           |             | PRK-ru    |
| Q033          | ru         | SKP-fee   | answer     | answer      | False      | False           | False       | DPK-ru    |
| Q034          | ar         | BIZ-start | answer     | answer      | False      | False           | False       | SGN-ar    |
| Q036          | en         | R-waive   | route      | answer      |            | False           |             | EXW-en    |
| Q037          | am         | ARC-fee   | route      | answer      |            | False           |             |           |
| Q038          | he         | R-mine    | route      | answer      |            | False           |             | DPK-he    |
| Q044          | en         | BIZ-start | answer     | answer      | False      | False           | False       | EXW-en    |
