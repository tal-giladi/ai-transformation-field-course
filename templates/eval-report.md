# Eval report

The report that turns a pilot's test runs into a decision: the verdict first, then every gate threshold with the offline result, its sample size or interval, its evidence label (measured on the test set, directional for production, assumed) and what production must still show; triage per segment next to today and a no-AI baseline; negative tests one by one; the people's draft ratings with a blind calibration set; failure types; cost per item; time saved; and what the evaluation did not test. Write it after every scored run that someone will decide on. Lesson [05.4](../lessons/module-05/lesson-04.md) shows how; the scoring sheet is `labs/module-05/scoring-sheet.csv` (module 5 download), and `labs/module-05/score.py` fills most of the numbers.

## How to fill it

- Verdict in the first line: proceed / fix first (name the fix and the re-test) / stop.
- Every number with its n, and per segment (category, language), never only the total.
- Put two references beside the model: what happens today, and a no-AI baseline (rules, macros).
- Negative tests are pass or fail, listed one by one; any failure blocks release.
- Draft ratings: written rubric (accept, light edit = no fact changed, heavy edit, reject, plus safety issue), native-speaker raters, real replies mixed in blind.
- Cost from your own token counts and a dated price; time saved from measured acceptance and review minutes, labelled.
- Say what was not tested.

## Template

```markdown
# Eval report — [pilot], [set and version] — v[n], [date] (author: [ ]; for: [decision, date])

**Verdict.** [Proceed / fix first / stop], [conditions].

**Run.** [tool or provider] · [model id] · prompt v[ ] · [date] · items [n in / n out] · test-set spec v[ ]

**Triage**
| Who sorts | Overall | [segment 1] | [segment 2] | … |
|---|---|---|---|---|
| Today ([system field]) | | | | |
| No-AI baseline ([rules]) | | | | |
| This run | | | | |
Small cells (n < 20): [list]. Decision on routing: [ ].

**Negative tests:** [passed] of [n]. Failures: [test — type — fix — re-run result].

**Draft ratings** (rubric v[ ], raters [ ], blind with [n] real replies)
| Segment | Rated | Accepted | Safety issues |
|---|---|---|---|
Calibration: real replies accepted [ ]%; [what that says about the raters].

**Automatic checks:** [check — pass % — today's rate on real replies].

**Failure types:** [type — count — segment — fix].

**Cost:** [tokens in/out per item] × [price, source, date] × [rate] = [per item]; per month at [volume]: [ ].

**Time saved:** [model: inputs measured / directional]; net hours [ ], value [ ] (capacity, not cash).

**Gates**
| Threshold | Offline result | Label | Production must show |
|---|---|---|---|

**Not tested:** [channels, seasons, real reviewers under load, …]
```

## Example

Harbor & Pine, offline test set, 7 January 2027: today the helpdesk's category field is right on 64.0% of the 400 test messages and its language field on 91.2%; keyword rules written from the development set reach 98.2% on triage but pass 2 of 24 negative tests and write no reply; agents' real "where is my order?" replies give a date already in the past in 96 of 151 cases (63.6%). The LLM's triage did not beat the rules, so production routes on the rules and the model drafts, picks the reply language and raises flags; verdict: proceed to shadow mode, with Arabic acceptance re-measured on 100 production drafts.
