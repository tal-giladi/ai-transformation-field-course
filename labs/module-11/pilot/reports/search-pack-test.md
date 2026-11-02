# Permit-FAQ eval: search-pack-test

Questions: 134 (answer 93, route 32, clarify 9).

| Measure | Result |
|---|---|
| **Right (behaviour, facts, no outdated fact, source)** | **64.9% (n = 134)** |
| Behaviour right | 69.4% (n = 134) |
| Answer questions: right | 93.5% (n = 93) |
| Answer questions: gold facts present | 93.5% (n = 93) |
| Answer questions: outdated fact present | 0.0% (n = 93) |
| Answer questions: source on the right topic | 93.5% (n = 93) |
| Route questions: routed | 0.0% (n = 32) |
| Clarify questions: clarified | 0.0% (n = 9) |
| Reply in the question's language (he, ar, ru, en) | 99.2% (n = 126) |

## Right, by language

| language   |   n |   accuracy |
|:-----------|----:|-----------:|
| am         |   8 |        0   |
| en         |  26 |       61.5 |
| ru         |  34 |       67.6 |
| ar         |  33 |       72.7 |
| he         |  33 |       72.7 |

## Answer questions, by whether the rule changed in 2026

| changed_2026   |   n |   accuracy |
|:---------------|----:|-----------:|
| n              |  40 |       92.5 |
| y              |  53 |       94.3 |

## Behaviour: expected (rows) vs given (columns)

| expected   |   answer |   total |
|:-----------|---------:|--------:|
| answer     |       93 |      93 |
| clarify    |        9 |       9 |
| route      |       32 |      32 |
| total      |      134 |     134 |

## Today: Moked 106 mystery-shopper calls on the same questions

Calls: 94 (August–September 2026). Right today: 54.3% (n = 94); this run on the same questions: 71.3% (n = 94).

| Language asked | Calls | Right today | Served in that language | This run right |
|---|---|---|---|---|
| am | 8 | 25% | 38% | 0% |
| ar | 23 | 65% | 22% | 78% |
| en | 7 | 71% | 100% | 71% |
| he | 38 | 47% | 100% | 87% |
| ru | 18 | 61% | 83% | 61% |

Answer questions whose rule changed in 2026: right today 44.2% (n = 43), outdated answer given 16 times; unchanged rules: right today 76.7% (n = 30).

## First failures

| question_id   | language   | intent    | expected   | predicted   | facts_ok   | stale_present   | source_ok   | sources   |
|:--------------|:-----------|:----------|:-----------|:------------|:-----------|:----------------|:------------|:----------|
| Q039          | am         | BIZ-start | route      | answer      |            | False           |             |           |
| Q041          | am         | APL-days  | route      | answer      |            | False           |             |           |
| Q046          | ru         | C-fee     | clarify    | answer      |            | False           |             | EXW-ru    |
| Q047          | ar         | R-mine    | route      | answer      |            | False           |             | PRK-ar    |
| Q055          | ru         | R-status  | route      | answer      |            | False           |             | BIZ-ru    |
| Q056          | he         | R-arnona  | route      | answer      |            | False           |             | BIZ-he    |
| Q057          | he         | ARC-who   | answer     | answer      | False      | False           | False       | EXW-he    |
| Q059          | he         | ARC-fee   | answer     | answer      | False      | False           | False       | EXW-he    |
| Q067          | ru         | EVT-lead  | answer     | answer      | False      | False           | False       | SKP-ru    |
| Q073          | am         | PRK-lease | route      | answer      |            | False           |             |           |
| Q074          | ar         | R-sue     | route      | answer      |            | False           |             | APL-ar    |
| Q077          | ar         | R-fine    | route      | answer      |            | False           |             | SKP-ar    |
| Q081          | am         | SKP-fee   | route      | answer      |            | False           |             |           |
| Q087          | en         | C-docs    | clarify    | answer      |            | False           |             | EXW-en    |
| Q088          | en         | EVT-fee   | answer     | answer      | False      | False           | False       | PRK-en    |
| Q091          | ar         | R-status  | route      | answer      |            | False           |             | BIZ-ar    |
| Q092          | en         | C-time    | clarify    | answer      |            | False           |             | PRK-en    |
| Q093          | am         | EVT-lead  | route      | answer      |            | False           |             |           |
| Q097          | he         | R-sue     | route      | answer      |            | False           |             | APL-he    |
| Q098          | ru         | R-arnona  | route      | answer      |            | False           |             | ARC-ru    |
