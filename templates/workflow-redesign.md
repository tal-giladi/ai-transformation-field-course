# Workflow redesign

The step-by-step record of how a team's work changes when an AI output enters it: every step of today's process marked keep, change, remove or new, the old paths switched off with a date and an owner, the handoffs and decision rights, where the freed hours go, and who is affected. Write it before go-live, with the people who do the work, and sign it with the owner and the sponsor. Lesson [06.1](../lessons/module-06/lesson-01.md) shows how; a spreadsheet version of the step table is `labs/module-06/workflow-redesign.csv` in the module 6 download ([open](../labs/module-06/workflow-redesign.csv)).

## How to fill it

- Start from evidence of what people do (observation, exports, tallies), not from the handbook. One table per workflow; three workflows usually cover most of the work.
- Mark every step: **keep** (still needed), **change** (done differently), **remove** (pointless now — and switched off), **new** (added by the pilot). Each mark has a reason.
- Every "remove" gets a switch-off date and a named owner. "Agents should prefer the new way" is not a removal.
- Name the receiving teams: anyone outside the pilot who gains a duty (keeping a field current, answering escalations).
- Write where the freed hours go, in order, with an owner and the number that will show it, and what they are not for.

## Template

```markdown
# Workflow redesign — [team, workflow] — v[n], [date]
Owner: [name] · Sponsor: [name] · Written with: [names]

## Steps — [workflow name]
| # | Today (who, tool) | Evidence | Mark | With the AI output | Reason |
|---|---|---|---|---|---|

## Where the AI output appears
[Inside which screen, at which moment, one click or automatic, what facts sit beside it, channel differences]

## Handoffs and decision rights
| Handoff | From → to | What changes | Who decides |
|---|---|---|---|

## Old paths switched off
| Old path | Switched off (date) | Owner | Why it must go | Checked on (date) |
|---|---|---|---|---|

## Where the freed hours go
| Order | Period | Destination | Owner | Indicator |
|---|---|---|---|---|
Not for: [what the hours are not used for, in approved wording]

## Change impact by role
| Role | What changes on [date] | What they need | Risk if ignored |
|---|---|---|---|

## Document changes
[Handbook / procedure sections, owner, date, languages]

## Dry run
[Date, who, what hesitated, what changed]

Signed: [owner], [sponsor], [date]
```

## Example

Harbor & Pine Customer Service, written WISMO contact, v1.0, 18 January 2027 (excerpt):

| # | Today | Mark | With drafts (from 1 February) | Reason |
|---|---|---|---|---|
| 4 | Delay-apology macro with the date from the order | Remove | Deleted from Deskly on 1 Feb (Samir) | It sends a date that has passed |
| 5 | Email logistics@ and wait | Change | Only if the ETA is blank or older than 7 days | Logistics keeps the ETA field current by 10:00 daily (Tamar's team) |
| 7 | — | New | Insert, edit, send; mark used / edited / discarded | Rule of use; gate-1 data |

Freed hours: (1) Feb–Apr, WhatsApp first response and Russian/Arabic waits, Samir, median first response per channel and language; (2) May–Oct, Friday rota and claim backlog; (3) peak 2027, replaces the two seasonal temps if gate 2 confirms it, Michal. Not a reduction of the permanent team.
