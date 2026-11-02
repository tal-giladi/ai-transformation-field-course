# Permit-FAQ eval: search-pack-negative

Questions: 12 (answer 4, route 8, clarify 0).

| Measure | Result |
|---|---|
| **Right (behaviour, facts, no outdated fact, source)** | **25.0% (n = 12)** |
| Behaviour right | 33.3% (n = 12) |
| Answer questions: right | 75.0% (n = 4) |
| Answer questions: gold facts present | 75.0% (n = 4) |
| Answer questions: outdated fact present | 0.0% (n = 4) |
| Answer questions: source on the right topic | 75.0% (n = 4) |
| Route questions: routed | 0.0% (n = 8) |
| Clarify questions: clarified | — |
| Reply in the question's language (he, ar, ru, en) | 90.0% (n = 10) |

## Right, by language

| language   |   n |   accuracy |
|:-----------|----:|-----------:|
| am         |   1 |        0   |
| fr         |   1 |        0   |
| ru         |   2 |        0   |
| ar         |   3 |       33.3 |
| he         |   3 |       33.3 |
| en         |   2 |       50   |

## Behaviour: expected (rows) vs given (columns)

| expected   |   answer |   total |
|:-----------|---------:|--------:|
| answer     |        4 |       4 |
| route      |        8 |       8 |
| total      |       12 |      12 |

## First failures

| question_id   | language   | intent   | expected   | predicted   | facts_ok   | stale_present   | source_ok   | sources   |
|:--------------|:-----------|:---------|:-----------|:------------|:-----------|:----------------|:------------|:----------|
| N03           | ar         | N03      | route      | answer      |            | False           |             | CAF-ar    |
| N04           | fr         | N04      | route      | answer      |            | False           |             |           |
| N05           | ar         | N05      | answer     | answer      | False      | False           | False       | DPK-en    |
| N06           | am         | N06      | route      | answer      |            | False           |             |           |
| N07           | ru         | N07      | route      | answer      |            | False           |             | EXW-ru    |
| N08           | he         | N08      | route      | answer      |            | False           |             | APL-he    |
| N10           | en         | N10      | route      | answer      |            | False           |             | CAF-en    |
| N11           | he         | N11      | route      | answer      |            | False           |             | SKP-he    |
| N12           | ru         | N12      | route      | answer      |            | False           |             | APL-ru    |
