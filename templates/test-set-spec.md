# Test-set spec

One page that says what an evaluation was measured on, and therefore what its numbers can and cannot prove: the decision the test set supports, the population and its known limits, size and confidence, the split between development and test, how the ground truth was labelled and how well labellers agreed, the facts added, what was removed or transformed before any text reached a model, the negative tests, and the rules for changing it. Write it when you freeze the test set, and attach it to every eval report that uses it. Lesson [05.2](../lessons/module-05/lesson-02.md) shows how.

## How to fill it

- Start from the decision (a gate threshold) and size the set from it; give the confidence interval per segment that the decision depends on.
- Write the population's limits plainly: channels, seasons, process changes not in the data.
- Development set for tuning, test set scored once per version; fixed seed; stratified by the segments you report.
- Labelling: written rules, two independent labellers, agreement and kappa, an adjudicator, a change log.
- Removed or transformed: columns dropped, pseudonymisation with counts, how the residue was checked, what stays (and why), where it is stored, when it is deleted.
- Negative tests: kinds, count, pass mark (all), when they are re-run.

## Template

```markdown
# Test-set spec — [pilot] — v[n], [date] (owner: [ ]; labels adjudicated by [ ])

| Item | Entry |
|---|---|
| Decision it supports | |
| Population | [unit, source, period, sampling] |
| Known limits | [what it does not represent; where that is tested instead] |
| Size and split | [test n / dev n]; stratified by [ ]; seed [ ]; script [ ] |
| What it can prove | [interval overall and per segment]; top-up plan |
| Ground truth | [fields: category, language, expected facts …] |
| Labelling | [rules doc vN]; [labellers]; agreement [ ]%, kappa [ ]; adjudication [ ] |
| Removed or transformed | [columns]; [pseudonymised: what, counts]; [residue check]; [kept and why] |
| Not used | [sources and why] |
| Negative tests | [n, kinds]; pass mark all; re-run [when] |
| Storage and deletion | [where, who can read, when deleted] |
| Change rule | [labels change only through …; new version for every change] |
```

## Example

Harbor & Pine, v1.0, 18 December 2026: 400 test / 200 development messages from the 600 full-text support emails of May–October 2026, stratified by language × category with seed 20261215 (test: Hebrew 239, Arabic 50, Russian 58, English 53; WISMO 151); per-language interval about ±11 points, so Arabic and Russian are topped up to 100 rated drafts each in production; order context for 260 test items, an expected delivery date for 163; names (840 + 53 in a second pass), phones (205) and street addresses (21) pseudonymised, order numbers kept; known limits: no WhatsApp, no peak season, before the date fix; 24 negative tests, pass mark all.
