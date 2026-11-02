# Permit-FAQ eval: search-site-track-a

Questions: 80 (answer 56, route 19, clarify 5).

| Measure | Result |
|---|---|
| **Right (behaviour, facts, no outdated fact, source)** | **25.0% (n = 80)** |
| Behaviour right | 70.0% (n = 80) |
| Answer questions: right | 35.7% (n = 56) |
| Answer questions: gold facts present | 39.3% (n = 56) |
| Answer questions: outdated fact present | 26.8% (n = 56) |
| Answer questions: source on the right topic | 60.7% (n = 56) |
| Route questions: routed | 0.0% (n = 19) |
| Clarify questions: clarified | 0.0% (n = 5) |
| Reply in the question's language (he, ar, ru, en) | 97.5% (n = 80) |

## Right, by language

| language   |   n |   accuracy |
|:-----------|----:|-----------:|
| en         |  16 |        6.2 |
| ar         |  20 |       15   |
| ru         |  20 |       20   |
| he         |  24 |       50   |

## Answer questions, by whether the rule changed in 2026

| changed_2026   |   n |   accuracy |
|:---------------|----:|-----------:|
| y              |  33 |       21.2 |
| n              |  23 |       56.5 |

## Behaviour: expected (rows) vs given (columns)

| expected   |   answer |   total |
|:-----------|---------:|--------:|
| answer     |       56 |      56 |
| clarify    |        5 |       5 |
| route      |       19 |      19 |
| total      |       80 |      80 |

## Answers that carry an outdated fact (15)

| intent    | language   |   n |
|:----------|:-----------|----:|
| BLK-extra | ar         |   2 |
| EVT-lead  | ar         |   1 |
| EVT-lead  | en         |   1 |
| PRK-fee2  | ar         |   1 |
| PRK-lease | ar         |   1 |
| PRK-lease | en         |   1 |
| PRK-lease | ru         |   2 |
| PRK-time  | ar         |   1 |
| PRK-time  | ru         |   1 |
| SGN-fee   | he         |   1 |
| SGN-fee   | ru         |   2 |
| SKP-fee   | he         |   1 |

## Today: Moked 106 mystery-shopper calls on the same questions

Calls: 48 (August–September 2026). Right today: 58.3% (n = 48); this run on the same questions: 37.5% (n = 48).

| Language asked | Calls | Right today | Served in that language | This run right |
|---|---|---|---|---|
| ar | 16 | 62% | 19% | 19% |
| en | 3 | 100% | 100% | 0% |
| he | 19 | 53% | 100% | 58% |
| ru | 10 | 50% | 90% | 40% |

Answer questions whose rule changed in 2026: right today 47.8% (n = 23), outdated answer given 8 times; unchanged rules: right today 81.2% (n = 16).

## First failures

| question_id   | language   | intent    | expected   | predicted   | facts_ok   | stale_present   | source_ok   | sources    |
|:--------------|:-----------|:----------|:-----------|:------------|:-----------|:----------------|:------------|:-----------|
| Q040          | ar         | SKP-fee   | answer     | answer      | False      | False           | False       | PRK-ar     |
| Q046          | ru         | C-fee     | clarify    | answer      |            | False           |             | PRK-ru     |
| Q047          | ar         | R-mine    | route      | answer      |            | False           |             | PRK-ar     |
| Q049          | en         | ARC-fee   | answer     | answer      | False      | False           | False       | PRK-en     |
| Q050          | ru         | APL-days  | answer     | answer      | False      | False           | False       | PRK-ru     |
| Q051          | he         | SGN-fee   | answer     | answer      | False      | True            | False       | FEE2025-he |
| Q055          | ru         | R-status  | route      | answer      |            | False           |             | FEE2026-he |
| Q056          | he         | R-arnona  | route      | answer      |            | False           |             | BIZ-he     |
| Q057          | he         | ARC-who   | answer     | answer      | False      | False           | False       | EXW-he     |
| Q058          | en         | ARC-who   | answer     | answer      | False      | False           | False       | PRK-en     |
| Q059          | he         | ARC-fee   | answer     | answer      | False      | False           | False       | EXW-he     |
| Q065          | ar         | BLK-extra | answer     | answer      | False      | True            | True        | BLK-ar     |
| Q068          | en         | SGN-fee   | answer     | answer      | False      | False           | False       | PRK-en     |
| Q069          | ar         | EVT-lead  | answer     | answer      | False      | True            | True        | EVT-ar     |
| Q070          | ar         | PRK-lease | answer     | answer      | False      | True            | True        | PRK-ar     |
| Q074          | ar         | R-sue     | route      | answer      |            | False           |             | APL-ar     |
| Q077          | ar         | R-fine    | route      | answer      |            | False           |             | BIZ-ar     |
| Q078          | ru         | DPK-docs  | answer     | answer      | False      | False           | False       | PRK-ru     |
| Q083          | en         | BLK-extra | answer     | answer      | False      | False           | False       | PRK-en     |
| Q088          | en         | EVT-fee   | answer     | answer      | False      | False           | False       | PRK-en     |
