# Permit-FAQ eval: search-site-test

Questions: 134 (answer 93, route 32, clarify 9).

| Measure | Result |
|---|---|
| **Right (behaviour, facts, no outdated fact, source)** | **23.9% (n = 134)** |
| Behaviour right | 69.4% (n = 134) |
| Answer questions: right | 34.4% (n = 93) |
| Answer questions: gold facts present | 37.6% (n = 93) |
| Answer questions: outdated fact present | 23.7% (n = 93) |
| Answer questions: source on the right topic | 57.0% (n = 93) |
| Route questions: routed | 0.0% (n = 32) |
| Clarify questions: clarified | 0.0% (n = 9) |
| Reply in the question's language (he, ar, ru, en) | 97.6% (n = 126) |

## Right, by language

| language   |   n |   accuracy |
|:-----------|----:|-----------:|
| am         |   8 |        0   |
| en         |  26 |        3.8 |
| ru         |  34 |       14.7 |
| ar         |  33 |       21.2 |
| he         |  33 |       57.6 |

## Answer questions, by whether the rule changed in 2026

| changed_2026   |   n |   accuracy |
|:---------------|----:|-----------:|
| y              |  53 |       24.5 |
| n              |  40 |       47.5 |

## Behaviour: expected (rows) vs given (columns)

| expected   |   answer |   total |
|:-----------|---------:|--------:|
| answer     |       93 |      93 |
| clarify    |        9 |       9 |
| route      |       32 |      32 |
| total      |      134 |     134 |

## Answers that carry an outdated fact (22)

| intent    | language   |   n |
|:----------|:-----------|----:|
| ARC-fee   | he         |   1 |
| BLK-extra | ar         |   2 |
| EVT-lead  | ar         |   1 |
| EVT-lead  | en         |   1 |
| PRK-fee2  | ar         |   2 |
| PRK-fee2  | en         |   1 |
| PRK-fee2  | ru         |   1 |
| PRK-lease | ar         |   1 |
| PRK-lease | en         |   1 |
| PRK-lease | ru         |   2 |
| PRK-time  | ar         |   2 |
| PRK-time  | en         |   1 |
| PRK-time  | ru         |   2 |
| SGN-fee   | he         |   1 |
| SGN-fee   | ru         |   2 |
| SKP-fee   | he         |   1 |

## Today: Moked 106 mystery-shopper calls on the same questions

Calls: 94 (August–September 2026). Right today: 54.3% (n = 94); this run on the same questions: 36.2% (n = 94).

| Language asked | Calls | Right today | Served in that language | This run right |
|---|---|---|---|---|
| am | 8 | 25% | 38% | 0% |
| ar | 23 | 65% | 22% | 26% |
| en | 7 | 71% | 100% | 0% |
| he | 38 | 47% | 100% | 61% |
| ru | 18 | 61% | 83% | 28% |

Answer questions whose rule changed in 2026: right today 44.2% (n = 43), outdated answer given 16 times; unchanged rules: right today 76.7% (n = 30).

## First failures

| question_id   | language   | intent    | expected   | predicted   | facts_ok   | stale_present   | source_ok   | sources    |
|:--------------|:-----------|:----------|:-----------|:------------|:-----------|:----------------|:------------|:-----------|
| Q035          | ar         | ARC-who   | answer     | answer      | False      | False           | False       | EVT-ar     |
| Q039          | am         | BIZ-start | route      | answer      |            | False           |             |            |
| Q040          | ar         | SKP-fee   | answer     | answer      | False      | False           | False       | PRK-ar     |
| Q041          | am         | APL-days  | route      | answer      |            | False           |             |            |
| Q046          | ru         | C-fee     | clarify    | answer      |            | False           |             | PRK-ru     |
| Q047          | ar         | R-mine    | route      | answer      |            | False           |             | PRK-ar     |
| Q048          | ru         | ARC-fee   | answer     | answer      | False      | False           | False       | PRK-ru     |
| Q049          | en         | ARC-fee   | answer     | answer      | False      | False           | False       | PRK-en     |
| Q050          | ru         | APL-days  | answer     | answer      | False      | False           | False       | PRK-ru     |
| Q051          | he         | SGN-fee   | answer     | answer      | False      | True            | False       | FEE2025-he |
| Q055          | ru         | R-status  | route      | answer      |            | False           |             | FEE2026-he |
| Q056          | he         | R-arnona  | route      | answer      |            | False           |             | BIZ-he     |
| Q057          | he         | ARC-who   | answer     | answer      | False      | False           | False       | EXW-he     |
| Q058          | en         | ARC-who   | answer     | answer      | False      | False           | False       | PRK-en     |
| Q059          | he         | ARC-fee   | answer     | answer      | False      | False           | False       | EXW-he     |
| Q060          | ar         | PRK-fee2  | answer     | answer      | False      | True            | True        | PRK-ar     |
| Q063          | ar         | ARC-fee   | answer     | answer      | False      | False           | False       | PRK-ar     |
| Q065          | ar         | BLK-extra | answer     | answer      | False      | True            | True        | BLK-ar     |
| Q067          | ru         | EVT-lead  | answer     | answer      | True       | False           | False       | PRK-ru     |
| Q068          | en         | SGN-fee   | answer     | answer      | False      | False           | False       | PRK-en     |
