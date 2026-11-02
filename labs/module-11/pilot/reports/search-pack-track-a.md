# Permit-FAQ eval: search-pack-track-a

Questions: 80 (answer 56, route 19, clarify 5).

| Measure | Result |
|---|---|
| **Right (behaviour, facts, no outdated fact, source)** | **63.7% (n = 80)** |
| Behaviour right | 70.0% (n = 80) |
| Answer questions: right | 91.1% (n = 56) |
| Answer questions: gold facts present | 91.1% (n = 56) |
| Answer questions: outdated fact present | 0.0% (n = 56) |
| Answer questions: source on the right topic | 91.1% (n = 56) |
| Route questions: routed | 0.0% (n = 19) |
| Clarify questions: clarified | 0.0% (n = 5) |
| Reply in the question's language (he, ar, ru, en) | 98.8% (n = 80) |

## Right, by language

| language   |   n |   accuracy |
|:-----------|----:|-----------:|
| en         |  16 |       62.5 |
| he         |  24 |       62.5 |
| ar         |  20 |       65   |
| ru         |  20 |       65   |

## Answer questions, by whether the rule changed in 2026

| changed_2026   |   n |   accuracy |
|:---------------|----:|-----------:|
| n              |  23 |       87   |
| y              |  33 |       93.9 |

## Behaviour: expected (rows) vs given (columns)

| expected   |   answer |   total |
|:-----------|---------:|--------:|
| answer     |       56 |      56 |
| clarify    |        5 |       5 |
| route      |       19 |      19 |
| total      |       80 |      80 |

## Today: Moked 106 mystery-shopper calls on the same questions

Calls: 48 (August–September 2026). Right today: 58.3% (n = 48); this run on the same questions: 70.8% (n = 48).

| Language asked | Calls | Right today | Served in that language | This run right |
|---|---|---|---|---|
| ar | 16 | 62% | 19% | 75% |
| en | 3 | 100% | 100% | 67% |
| he | 19 | 53% | 100% | 74% |
| ru | 10 | 50% | 90% | 60% |

Answer questions whose rule changed in 2026: right today 47.8% (n = 23), outdated answer given 8 times; unchanged rules: right today 81.2% (n = 16).

## First failures

| question_id   | language   | intent   | expected   | predicted   | facts_ok   | stale_present   | source_ok   | sources   |
|:--------------|:-----------|:---------|:-----------|:------------|:-----------|:----------------|:------------|:----------|
| Q046          | ru         | C-fee    | clarify    | answer      |            | False           |             | EXW-ru    |
| Q047          | ar         | R-mine   | route      | answer      |            | False           |             | PRK-ar    |
| Q055          | ru         | R-status | route      | answer      |            | False           |             | BIZ-ru    |
| Q056          | he         | R-arnona | route      | answer      |            | False           |             | BIZ-he    |
| Q057          | he         | ARC-who  | answer     | answer      | False      | False           | False       | EXW-he    |
| Q059          | he         | ARC-fee  | answer     | answer      | False      | False           | False       | EXW-he    |
| Q074          | ar         | R-sue    | route      | answer      |            | False           |             | APL-ar    |
| Q077          | ar         | R-fine   | route      | answer      |            | False           |             | SKP-ar    |
| Q088          | en         | EVT-fee  | answer     | answer      | False      | False           | False       | PRK-en    |
| Q092          | en         | C-time   | clarify    | answer      |            | False           |             | PRK-en    |
| Q097          | he         | R-sue    | route      | answer      |            | False           |             | APL-he    |
| Q101          | ru         | R-mine   | route      | answer      |            | False           |             | PRK-ru    |
| Q102          | ar         | C-fee    | clarify    | answer      |            | False           |             | PRK-ar    |
| Q103          | ar         | R-exempt | route      | answer      |            | False           |             | CAF-ar    |
| Q105          | ru         | R-sue    | route      | answer      |            | False           |             | APL-ru    |
| Q108          | he         | R-bizfee | route      | answer      |            | False           |             | CAF-he    |
| Q110          | he         | SKP-fee  | answer     | answer      | False      | False           | False       | DPK-he    |
| Q113          | ru         | R-bizfee | route      | answer      |            | False           |             | CAF-ru    |
| Q120          | en         | R-sue    | route      | answer      |            | False           |             | APL-en    |
| Q123          | he         | R-fine   | route      | answer      |            | False           |             | BIZ-he    |
