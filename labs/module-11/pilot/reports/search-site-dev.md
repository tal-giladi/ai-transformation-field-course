# Permit-FAQ eval: search-site-dev

Questions: 40 (answer 27, route 10, clarify 3).

| Measure | Result |
|---|---|
| **Right (behaviour, facts, no outdated fact, source)** | **27.5% (n = 40)** |
| Behaviour right | 67.5% (n = 40) |
| Answer questions: right | 40.7% (n = 27) |
| Answer questions: gold facts present | 44.4% (n = 27) |
| Answer questions: outdated fact present | 14.8% (n = 27) |
| Answer questions: source on the right topic | 55.6% (n = 27) |
| Route questions: routed | 0.0% (n = 10) |
| Clarify questions: clarified | 0.0% (n = 3) |
| Reply in the question's language (he, ar, ru, en) | 97.4% (n = 38) |

## Right, by language

| language   |   n |   accuracy |
|:-----------|----:|-----------:|
| am         |   2 |        0   |
| ru         |  10 |       10   |
| en         |   6 |       16.7 |
| ar         |  11 |       36.4 |
| he         |  11 |       45.5 |

## Answer questions, by whether the rule changed in 2026

| changed_2026   |   n |   accuracy |
|:---------------|----:|-----------:|
| y              |  14 |       21.4 |
| n              |  13 |       61.5 |

## Behaviour: expected (rows) vs given (columns)

| expected   |   answer |   total |
|:-----------|---------:|--------:|
| answer     |       27 |      27 |
| clarify    |        3 |       3 |
| route      |       10 |      10 |
| total      |       40 |      40 |

## Answers that carry an outdated fact (4)

| intent    | language   |   n |
|:----------|:-----------|----:|
| EVT-lead  | ar         |   1 |
| PRK-fee2  | ru         |   1 |
| PRK-lease | ar         |   1 |
| SGN-min   | ru         |   1 |

## First failures

| question_id   | language   | intent    | expected   | predicted   | facts_ok   | stale_present   | source_ok   | sources    |
|:--------------|:-----------|:----------|:-----------|:------------|:-----------|:----------------|:------------|:-----------|
| Q001          | he         | C-time    | clarify    | answer      |            | False           |             | CAF-he     |
| Q002          | ar         | SGN-min   | answer     | answer      | False      | False           | False       | BIZ-ar     |
| Q003          | ar         | R-bizfee  | route      | answer      |            | False           |             | BIZ-ar     |
| Q005          | ru         | DPK-time  | answer     | answer      | False      | False           | False       | PRK-ru     |
| Q006          | ru         | BIZ-start | answer     | answer      | False      | False           | False       | SGN-ru     |
| Q007          | ar         | EVT-lead  | answer     | answer      | False      | True            | True        | EVT-ar     |
| Q009          | en         | BLK-free  | answer     | answer      | False      | False           | False       | PRK-en     |
| Q010          | ar         | C-time    | clarify    | answer      |            | False           |             | EVT-ar     |
| Q012          | ru         | SKP-max   | answer     | answer      | True       | False           | False       | PRK-ru     |
| Q013          | ar         | SGN-fee   | answer     | answer      | False      | False           | False       | BLK-ar     |
| Q014          | en         | CAF-fee   | answer     | answer      | False      | False           | False       | PRK-en     |
| Q016          | am         | PRK-fee2  | route      | answer      |            | False           |             |            |
| Q018          | en         | DPK-docs  | answer     | answer      | False      | False           | False       | PRK-en     |
| Q020          | ru         | R-waive   | route      | answer      |            | False           |             | SGN-ru     |
| Q021          | en         | R-status  | route      | answer      |            | False           |             | PRK-en     |
| Q022          | he         | C-docs    | clarify    | answer      |            | False           |             | BIZ-he     |
| Q024          | ru         | SGN-min   | answer     | answer      | False      | True            | True        | SGN-ru     |
| Q026          | he         | R-waive   | route      | answer      |            | False           |             | SGN-he     |
| Q027          | he         | R-status  | route      | answer      |            | False           |             | FEE2026-he |
| Q028          | ru         | CAF-fee   | answer     | answer      | False      | False           | False       | SGN-ru     |
