# Pressure-test log

The findings log of a pre-failure reading of a plan: what breaks, for whom and when; the evidence; whether the assumption is wrong (false today) or the dependency fragile (true today, may change); the test or trial that settles it; the disposition; the owner. Use it on any roadmap, business case or rollout plan before money is committed against it, and ask someone who did not write the plan to do it. Lesson [07.7](../lessons/module-07/lesson-07.md) pressure-tests the roadmap a consultancy wrote for Harbor & Pine. Spreadsheet version: `labs/module-07/pressure-test-log.csv` (module 7 download).

## How to fill it

- List the plan's promises with their dates first.
- Set a failure date and write failure stories alone, before discussing them.
- Every finding points at a file, a number or a person, never a category.
- Wrong: correct it or remove what rests on it. Fragile: fallback, trigger, re-sequence or remove the dependency.
- Load-test every control the plan relies on, with arithmetic (time, volume, independence).
- Name the smallest trial that settles each arguable finding.
- Dispositions: correct, re-sequence, add a fallback, de-scope, defer, remove. Sort by consequence.
- Say what survives. Give the log to the sponsor first, with one decision and a date.

## Template

```markdown
# Pressure-test log — [plan, author, date] — [date of test]
Reviewer: [name, not the plan's author] · For: [sponsor] · Failure date assumed: [date]

## Promises
| # | The plan promises | By |
|---|---|---|

## Findings (sorted by consequence)
| # | What breaks, for whom, when | Evidence | Wrong / fragile | Load test or trial | Disposition | Owner | Due |
|---|---|---|---|---|---|---|---|

## What survives
[Items of the plan that pass the test, one line each]

## Cover note
[The most likely failure, in one sentence] · [what to decide, by when] · [what survives] ·
[who should pressure-test the reviewer's own plan]
```

## Example

Harbor & Pine, 24 November 2026, the previous consultant's roadmap. Finding 1: "The chatbot answers 'where is my order?' with the passed promised date; customers write again; from go-live (February 2027)." Evidence: 38% of tickets are WISMO; Vietnam and China orders arrive a median 11 days late; the vendor's footnote says order tracking needs integration. Type: wrong (the 70% does not hold for this business). Trial: a two-week dry run of the date fix, then a proof of concept on own data. Disposition: re-sequence (date fix first; chatbot to a re-screen). Finding 13: "The vendor's 15% discount ends on 30 November": fragile; take the deadline out of the decision. Decision asked: do not sign ChatNest by 30 November.
