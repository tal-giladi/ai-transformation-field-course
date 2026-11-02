# Adoption dashboard spec

The definition of an honest adoption dashboard: which events count as use, who could have used the tool each week, the qualified-use rate beside the vendor's figures, how quiet non-adoption is detected, what goes to which audience, and the rules that keep the monitoring of employees lawful and proportionate. Write it before you build the first chart, and attach it to every dashboard you publish. Lesson [06.4](../lessons/module-06/lesson-04.md) shows how; the metric table is `labs/module-06/adoption-dashboard-metrics.csv` and a Track B script is `labs/module-06/adoption_dashboard.py` in the module 6 download ([metrics](../labs/module-06/adoption-dashboard-metrics.csv)).

## How to fill it

- Classify every event in the export: fires by itself, a click, trying, use. Only use counts.
- Define the qualified event, the window and the sustained-user rule so anyone can recompute them; check the threshold at two other values.
- The denominator is the opportunity-aware population per week (role and HR status), never licences.
- Define quiet non-adoption before you look, and include "still working" so leavers and absences are not counted.
- Every metric names who sees it and what it is never used for. In a small team, team-level can still identify people.
- The monitoring section is the notice employees were given: purpose, minimum data, access, never, retention, assessment, questions for counsel or the DPO.

## Template

```markdown
# Adoption dashboard spec — [pilot] — v[n], [date]
Owner: [name] · Readers: [audiences] · Source exports: [files, dates]

## Events
| Event | What fires it | Counts as use? |
|---|---|---|

## Definitions
Qualified user-[period]: [rule] · Sustained user: [rule] · Window: [why]
Opportunity-aware population: [roles], [status rule], [absence handling]
Quiet non-adoption: [was a user when] + [below threshold when] + [still working, by which signal]

## Metrics
| Metric | Layer | Definition | Numerator / denominator | Source | Window | Shown to | Never used for | Owner |
|---|---|---|---|---|---|---|---|---|

## What the export cannot answer, and where to get it
[e.g. the ticket-level adoption gate; "back to what"]

## Monitoring of employees
| Rule | Entry |
|---|---|
| Purpose | |
| Minimum data | |
| Who sees what | |
| Never | |
| Notice given (date, languages) | |
| Retention | |
| Assessment (DPIA) | |
| To counsel / DPO | |

## One-page layout
[Headline sentence · vendor view vs honest view · quiet non-adoption by queue or group · decisions asked for]
```

## Example

Harbor & Pine drafts pilot, weeks 1–8 (1 February – 28 March 2027). Qualified user-week: at least 5 `draft_inserted` events in the pilot week; `panel_opened` excluded because it fires when a ticket opens. Population: Support Agent and Senior Support Agent, active on the Monday of the week (12, then 11, then 10 as Hila goes on leave and Adi leaves). Week 8: vendor "active" 12 of 16 licences (75%); qualified 6 of 10 (60%, one on leave); sustained 7 of 10. Quiet non-adoption: 3 of 10, all moved to the WhatsApp pod on 22 February; reported as "the WhatsApp queue runs almost without drafts", with names only to the pilot lead. Per-person table deleted at gate 2 (30 September 2027); never used in performance reviews.
