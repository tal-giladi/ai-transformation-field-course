# Operating rhythm

How a running AI service is owned and watched once the project team has moved on: one accountable owner, a RACI for the recurring tasks and the switches, a calendar with the hours each item costs, triggers that send a named person to act, a fixed monthly agenda, and the criteria for retiring it. Write it when a pilot becomes a service, before the builders leave. Lesson [07.6](../lessons/module-07/lesson-06.md) writes Harbor & Pine's. Spreadsheet version: `labs/module-07/operating-rhythm.csv` (module 7 download).

## How to fill it

- One accountable owner who holds the switch; a committee governs above them, it does not own the service.
- RACI lines are things people actually do; include the switch, source and prompt changes, model notices and retirement. One A per line.
- Every recurring item has a day, a person and hours; total the hours and compare them with the business case.
- Triggers and cadence are separate tables. A trigger names who is told, who may act, how fast and the response.
- Report adoption by team or queue, never by person.
- Write the retirement criteria now, as checkable conditions.

## Template

```markdown
# Operating rhythm — [service] — v[N], [date]
Accountable owner: [name] · Analyst: [name] · Technical owner: [name]

## Roles
| Role | Who | Owns |
|---|---|---|

## RACI
| Activity | [Owner] | [Analyst] | [Technical] | [Reviewers] | [Finance] | [Governance forum] | [Investment forum] |
|---|---|---|---|---|---|---|---|
| Switch off (segment / all) | | | | | | | |
| Prompt change | | | | | | | |
| Knowledge-source change | | | | | | | |
| Model or provider change | | | | | | | |
| Sampled output review | | | | | | | |
| Eval re-run and negative tests | | | | | | | |
| Incident lead | | | | | | | |
| Value numbers | | | | | | | |
| Vendor settings and admin rights | | | | | | | |
| Licences and leavers | | | | | | | |
| Retirement decision | | | | | | | |

## Calendar
| Cadence | When | What | Who | Hours a month |
|---|---|---|---|---|
| **Total** | | | | |
Hours in the business case: [n] · Difference: [n] · Told to finance on: [date]

## Triggers
| Trigger (threshold) | Told | May act | How fast | Response |
|---|---|---|---|---|

## Monthly review agenda ([n] minutes)
1. Signals vs thresholds · 2. Incidents, near misses, open actions · 3. Changes released and proposed ·
4. Value · 5. Adoption by queue · 6. Vendor and model notices, contract dates · 7. Decisions, minuted
First review: [date] · Minutes go to: [forum] on [date]

## Retirement criteria
- [Checkable condition] — decided by [forum]; executed with the decommissioning checklist
```

## Example

Harbor & Pine's reply-drafts service, v1.0 of 4 April 2027: owner Samir Haddad (holds the switch); analyst the pilot lead until 30 June, then Shani Ohayon with four protected hours a week. The calendar totals about 27 hours a month against about 100 hours a year in ROI model v3; the difference (about 220 hours a year) is netted from the capacity benefit in the July re-forecast. Trigger: "acceptance below 60% two weeks running in one channel × language → that segment off, same week, Samir." First monthly review Thursday 6 May 2027. Retirement criterion: "minutes saved per contact against the holdout below 1 for two quarters."
