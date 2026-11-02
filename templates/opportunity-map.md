# Opportunity map

The full list of places where the work could change, each restated as one workflow step with an owner, a measured volume and a benefit in one unit, and placed as automate, assist, augment or leave alone. Build it after discovery and before any screening or scoring, from three feeds (requests, tools already in use, leadership goals) plus your own findings. Lesson [03.1](../lessons/module-03/lesson-01.md) shows how; the spreadsheet version is `labs/module-03/opportunity-map.csv` in the module 3 download ([open](../labs/module-03/opportunity-map.csv)).

## How to fill it

- One row per candidate, including the ones you expect to drop (tools already in use, vendor offers, systems that only claim to be AI).
- Restate every request as: workflow step, owner, volume a month, minutes each, what changes, one benefit unit. If the step or the owner is unknown, mark it "not yet a candidate" and write the question that would make it one.
- Every figure has a source and a status: **M** measured (you counted it), **R** reported (someone told you), **C** claimed (proposer or vendor).
- Mode: **automate** (no person per item), **assist** (a person decides and sends each item), **augment** (a person gains a capability they did not have), **leave alone** (not worth it, not ready, not AI, or a governance decision).
- Oversight need: report → review; predict → show uncertainty; decide or act on a person → approval gate.
- The ledger line is never blank: who checks, corrects, escalates or waits because of this change.
- Do not score here. Scoring needs locked criteria (lesson 03.4).

## Template

```markdown
# Opportunity map — [Organization] — [date]

Feeds used: requests ([sources]) · already in use ([census / inventory date]) · top-down goals
([documents]) · discovery ([findings memo date])

| # | Candidate, restated (step + change) | Feed | Owner | Volume a month (source, M/R/C) | Minutes each (source, M/R/C) | Benefit unit | Mode | Reason for the mode | Oversight need | Ledger line | Not yet a candidate? (question) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [ ] | [request / in use / top-down / discovery] | [ ] | [ ] | [ ] | [hours / ₪ / errors / days] | [automate / assist / augment / leave alone] | [ ] | [review / show uncertainty / approval gate / none] | [ ] | [ ] |

## Workload behind the biggest driver
[The driver] across all channels, [month]: [channel 1 volume × minutes] + [channel 2 …] = [hours a
month] = [people at 182 hours a month]. Source: [files].

## What the map already shows
[Three to five sentences: which candidates need no AI, which depend on others, which are governance
decisions, which fail a basic question before scoring.]
```

## Example

Harbor & Pine, 19 November 2026, three of fifteen rows:

| # | Candidate | Feed | Owner | Volume a month | Mode | Ledger line |
|---|---|---|---|---|---|---|
| 1 | Compare each open order's promised date with the container's latest ETA daily; email the customer a new date; correct the web store's lead-time table | Discovery | Tamar, Noa | about 210 orders on slipped containers (M, `orders.csv` + `shipments.csv`) | Automate — rules, no AI | Logistics keeps the ETA sheet clean, about 1 hour a week (R) |
| 3 | Draft replies to written contacts in the customer's language; an agent edits and sends every one | Requests + in use (free ChatGPT) | Samir | about 3,200 once WhatsApp is routed in (M + R) | Assist | About 2 minutes of agent checking per draft; native-speaker spot-check |
| 7 | Approve or reject damage claims from photos | Request (CFO) | Rina | about 25 (M) | Not yet a candidate: decision blank for 32% of claims | Rina records every outcome first |

WISMO workload, October 2026: 268 tickets × 8 min + 1,180 WhatsApp × 10 min + 201 calls × 4.3 min ≈ 247 hours a month, about 1.4 people.
