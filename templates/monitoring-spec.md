# Monitoring spec

The three documents that let an AI pilot or service run after you stop watching it daily: the logging spec (what is recorded per item, and what is deliberately not), the monitoring signals (each with an indicator, a threshold, a cadence, an owner and a response), and change control (what counts as a change, how it is tested, who approves it, how it is rolled back). Write it before launch; every stop rule in the pilot charter must appear as a trigger. Lesson [05.7](../lessons/module-05/lesson-07.md) shows how; the signals are also a spreadsheet, `labs/module-05/monitoring-signals.csv` (module 5 download). Lesson 07.6 turns the cadence into the operating rhythm.

## How to fill it

- Log what you need for four uses (gate, monitoring, incident, re-run); point to texts that already live elsewhere instead of copying them; decide retention with the DPO.
- Every signal: indicator, threshold, cadence, owner, response. A signal without a response is decoration.
- Include: sampled output review by people, eval and negative-test re-runs on every change and on vendor model notices, cost alerts, reliability, value against the counterfactual, vendor settings, shadow-tool relapse.
- Change classes: standard, major, vendor setting, emergency; each with a test, an approver, a release window and a rollback. Keep the previous version deployable.
- Put the cadence on a calendar with names.

## Template

```markdown
# Monitoring spec — [pilot or service] — v[n], [date] (owner: [ ])

## Logging
| Field | Example | Use (gate / monitoring / incident / re-run) |
|---|---|---|
Not logged, and why: [ ]. Retention: [ ] (DPO decision of [date] / question: [ ]). Readers: [ ].

## Signals
| Signal | Indicator | Threshold (trigger) | Cadence | Owner | Response | Charter stop rule |
|---|---|---|---|---|---|---|

## Change control
| Class | Examples | Test before release | Approves | Release window | Rollback |
|---|---|---|---|---|---|
| Standard | | | | | |
| Major | | | | | |
| Vendor setting | | | | | |
| Emergency | | none before; note within [ ] | | immediately | |
Current versions: prompt [ ], categories [ ], model [id, provider's earliest retirement date], API [ ].
Previous deployable: [ ].

## Calendar
| When | What | Who |
|---|---|---|
```

## Example

Harbor & Pine, 28 January 2027: one log record per drafted or held-out ticket (ticket id, channel, language, suggested and final category, flags and who cleared them, order context present, prompt version, model id, API version, tokens, cost, latency, agent action and discard reason, review seconds, holdout, sent reply id), with no message or draft text; 13 signals plus a law trigger, e.g. "discard rate per language, weekly; below 5% while acceptance is under 90%: Samir audits 20 sends"; any model, provider or API-version change is major and needs the full eval, the negative tests and a week of shadow before it is switched.
