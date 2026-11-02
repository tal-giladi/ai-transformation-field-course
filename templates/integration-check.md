# Integration check

A log of the contradictions between deliverables that are each sound on their own: one document needs true what another denies or omits. Use it before a steering pack goes out, before a handover, and in every engagement readout (NN.6) and the capstone (18.2): read the documents side by side, question first, and trace every claim's timing to the readiness assessment and the roadmap, and every human control to its cost line and the people who staff it. Lessons [07.1](../lessons/module-07/lesson-01.md) and [07.9](../lessons/module-07/lesson-09.md) run it on Harbor & Pine. Spreadsheet version: `labs/module-07/integration-check.csv` (module 7 download).

## How to fill it

- Start from what the decision-makers will rely on (numbers, dates, scope, controls), not from the documents' order.
- For each item, read every document that mentions it; log any two that disagree.
- Say which one is right now, and whether the contradiction changes a decision.
- A contradiction that changes a decision is disclosed to the sponsor and put to the forum as its own line; it is never fixed quietly.
- Trace every human control (a review step, a spot check, an on-call line) to a person and a cost line.
- Trace every claim's timing (when a benefit lands) to readiness and the roadmap.

## Template

```markdown
# Integration check — [package] — [date]
Documents read: [list with versions]

| ID | What is relied on | Document A says | Document B says | Right now | Changes a decision? | Resolution | Owner | Due | Status |
|---|---|---|---|---|---|---|---|---|---|

## Control trace
| Human control | Person | Hours | Cost line in the model | Gap |
|---|---|---|---|---|

## Timing trace
| Claim | Lands when (case) | Readiness allows from | Roadmap schedules | Gap |
|---|---|---|---|---|
```

## Example

Harbor & Pine, 14 January 2027, before the steering pack: "IC-01 · language order of the drafts · roadmap v1.0: Russian and Arabic four weeks after Hebrew and English · charter, eval and training plan: all four from 1 February · charter is right · changes a decision: yes · put to the committee as roadmap v1.1." Control trace at handover, 30 June 2027: "operating rhythm, about 27 hours a month · ROI model v3 counted about 100 hours a year · gap about 220 hours a year, netted from the capacity benefit in the July re-forecast."
