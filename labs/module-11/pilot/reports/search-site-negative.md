# Permit-FAQ eval: search-site-negative

Questions: 12 (answer 4, route 8, clarify 0).

| Measure | Result |
|---|---|
| **Right (behaviour, facts, no outdated fact, source)** | **8.3% (n = 12)** |
| Behaviour right | 33.3% (n = 12) |
| Answer questions: right | 25.0% (n = 4) |
| Answer questions: gold facts present | 25.0% (n = 4) |
| Answer questions: outdated fact present | 25.0% (n = 4) |
| Answer questions: source on the right topic | 100.0% (n = 4) |
| Route questions: routed | 0.0% (n = 8) |
| Clarify questions: clarified | — |
| Reply in the question's language (he, ar, ru, en) | 90.0% (n = 10) |

## Right, by language

| language   |   n |   accuracy |
|:-----------|----:|-----------:|
| am         |   1 |        0   |
| ar         |   3 |        0   |
| en         |   2 |        0   |
| fr         |   1 |        0   |
| ru         |   2 |        0   |
| he         |   3 |       33.3 |

## Behaviour: expected (rows) vs given (columns)

| expected   |   answer |   total |
|:-----------|---------:|--------:|
| answer     |        4 |       4 |
| route      |        8 |       8 |
| total      |       12 |      12 |

## Answers that carry an outdated fact (1)

| intent   | language   |   n |
|:---------|:-----------|----:|
| N09      | ar         |   1 |

## First failures

| question_id   | language   | intent   | expected   | predicted   | facts_ok   | stale_present   | source_ok   | sources   |
|:--------------|:-----------|:---------|:-----------|:------------|:-----------|:----------------|:------------|:----------|
| N02           | en         | N02      | answer     | answer      | False      | False           | True        | PRK-en    |
| N03           | ar         | N03      | route      | answer      |            | False           |             | PRK-ar    |
| N04           | fr         | N04      | route      | answer      |            | False           |             |           |
| N05           | ar         | N05      | answer     | answer      | False      | False           | True        | PRK-en    |
| N06           | am         | N06      | route      | answer      |            | False           |             |           |
| N07           | ru         | N07      | route      | answer      |            | False           |             | PRK-ru    |
| N08           | he         | N08      | route      | answer      |            | False           |             | APL-he    |
| N09           | ar         | N09      | answer     | answer      | False      | True            | True        | PRK-ar    |
| N10           | en         | N10      | route      | answer      |            | False           |             | EVT-en    |
| N11           | he         | N11      | route      | answer      |            | False           |             | SKP-he    |
| N12           | ru         | N12      | route      | answer      |            | False           |             | SGN-ru    |
