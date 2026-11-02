# Incident runbook

What the team does when an AI service causes or nearly causes harm: what counts as an incident and how bad, who leads, which switches to pull in which order, the steps from logging to review, the privacy branch that routes reporting questions to counsel, and the evidence to keep. Write it before the first output reaches a customer, rehearse it with a tabletop, and update it after every incident. Lesson [07.5](../lessons/module-07/lesson-05.md) writes Harbor & Pine's and runs the tabletop.

## How to fill it

- Define incidents by harm, not by technology, with three severities and an example of each from this service.
- Name roles as well as people, each with a deputy.
- Order switches from narrowest to widest; test each one before go-live.
- The privacy branch says what to do and who decides. It never states a legal deadline: that is counsel's or the DPO's call.
- Customers hear from a person; public statements are short, true and owned by the company.
- "What changed?" (prompt, model, sources, settings, data) comes before any fix.
- The review is blameless, and its actions change controls, with owners and dates.

## Template

```markdown
# Incident runbook — [service] — v[N], [date]
Owner: [role, person] · Approved by: [names] · Rehearsed: [date, tabletop]

## 1. What counts as an incident
Harms: [list for this service]
| Severity | Definition | Example from this service |
|---|---|---|
| S1 | Harm reached people, or personal data reached someone not entitled to it | |
| S2 | Harm likely if nothing changes; nothing known sent | |
| S3 | Degraded service, no harm | |

## 2. Roles
| Role | Who | Deputy |
|---|---|---|
| Incident lead | | |
| Switch holders | | |
| Technical (what changed, fix) | | |
| Privacy and reporting (counsel / DPO) | | |
| Customers | | |
| Leaders and public statement | | |
| Scribe | | |

## 3. Switches, narrowest first
1. [one category] 2. [one channel or language] 3. [all] 4. [prompt / model to previous version] 5. [source removed]
Last reversible moment: [e.g. the send button]. No switch undoes what was sent.

## 4. Steps
1. Log and lead · 2. Contain · 3. Escalate · 4. Communicate · 5. Find what changed, then fix ·
6. Restore in stages · 7. Blameless review within [n] working days

## 5. Privacy branch
Preserve evidence · write down which data went to whom · brief [counsel / DPO] the same day with the facts ·
they decide reporting and informing the person · record their decision and its time

## 6. Updates
[To whom, how often, format] · [one page to the CEO for any S1 by …]

## 7. Evidence to keep
[Tickets, logs, console change history, screenshots, the incident log]

## 8. Ready-made texts
Holding statement: [text] · Customer call script: [text] · Leader page: what happened, how many, contained?, unknowns, decisions, next update

## Incident log
| Time | What we know | Decision | Who |
|---|---|---|---|
```

## Example

Harbor & Pine's reply drafts, v1.0 of 27 January 2027. S1 example: "a sent reply promises a refund outside policy; a reply quotes another customer's address." First switch: damage and returns drafts off. On 15 March 2027 the log reads: 09:40 public post, S1, lead named; 09:55 damage and returns drafts off; 12:00 cause found (an untested knowledge-source change on 10 March), possible privacy incident, facts to counsel by 16:00; Tuesday, other categories back, damage and returns after three days in shadow mode with a money flag. Review actions: console admin rights reduced; sources only from a curated library; negative tests on every source change.
