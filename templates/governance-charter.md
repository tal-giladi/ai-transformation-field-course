# Governance charter

The one document that says how AI is governed in the organization, in six parts — approved uses, restricted uses, data boundary, risk evidence, monitoring, escalation — plus the terms of reference of a small review group with written decision rights, a cadence, and the three numbers reported to the board. It points to the policy pack's other documents instead of repeating them. Write it once the pack's pieces exist; review it every six months. Lesson [04.7](../lessons/module-04/lesson-07.md) shows how.

## How to fill it

- Two pages: a short frame, the six parts each pointing to its document, the terms of reference.
- Decision rights say who decides each kind of item and within what time; most items are decided outside the meeting.
- Any member may stop a use on a threshold or policy breach; the group confirms or lifts it.
- Spending follows the organization's existing approval thresholds; the portfolio gate is only for money or scale.
- Link to the existing risk process and the board instead of building a parallel one.

## Template

```markdown
# AI governance charter — [Organization] — v[n], [date]
Owner: [role] · Approved by: [name, date] · Review: [date]

## Purpose and scope
[Two sentences.] Scope: all AI under the counting rule, including features inside bought software.

## The six parts
1. Approved uses → [approved list, tiers 1–2]
2. Restricted uses → [restricted list, tier 3]
3. Data boundary → [data boundaries per tool]
4. Risk evidence → [tier rule, DPIAs, risk register, regulatory map]
5. Monitoring → [failure signals: indicator · threshold · watcher · response]
6. Escalation → trigger → owner acts (same day) → secretary informs chair → chair decides continue / restrict / stop → recorded

## Review group — terms of reference
Chair (decides without consensus): [...] · Members: [...] · Secretary: [...] · On call: [counsel] · Quorum: [...]

| Decision | Who decides | Time limit |
|---|---|---|
| Tier 1–2 use with an approved tool | | |
| New tool for Medium uses | | |
| High-tier and restricted uses | | |
| Stop a use | Any member, immediately | |
| Spending | [existing finance thresholds] | |

## Cadence
Weekly intake triage · Monthly review group · Quarterly census and re-tiering · Six-monthly policy review · Board: [when]

## Reporting to the board
1. Reached production · 2. Median days to decision (slowest named) · 3. Declined or not yet, and why
Link to existing risk reporting: [how red risks reach the board]
```

## Example

Harbor & Pine, 30 November 2026 (excerpt):

| Decision | Who decides | Time limit |
|---|---|---|
| New Tier 1–2 use with a tool already approved for that data class | AI lead, recorded in the intake register | 10 working days |
| High-tier uses, restricted uses, lifting a restriction | Review group (chair Michal Peretz decides without consensus) | Next meeting, or 5 working days by email |
| Stopping a use on a threshold or policy breach | Any member, immediately | Immediately |
| Spending | Up to ₪50,000 department head and CFO; ₪50,000–150,000 CEO; above ₪150,000 over three years the board | As finance sets |
