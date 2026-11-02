# AI intake register

The single list of every AI build, purchase and request — from a form, an email, an expense claim or a vendor's release note — with its owner, where it runs, the data it touches, what else does the same job, its tier and route, the decision and how many days the decision took. It is how governance stays fast enough that people use it, and the source of two of the three numbers the board sees. Start it the day the acceptable-use policy is published. Lesson [04.7](../lessons/module-04/lesson-07.md) shows how; spreadsheet `labs/module-04/ai-intake-register.csv` in the module 4 download ([open](../labs/module-04/ai-intake-register.csv)).

## How to fill it

- Record everything, including items found rather than requested (expenses, release notes, proxy logs), with the date you found them.
- Fill "overlaps" before deciding: other requests or approved tools that do the same job.
- Tier with the inventory's rule; route: fast-track · review group · portfolio gate (money or scale) · not AI (normal process).
- Days to decision = calendar days from received to decided. Report the median and name the slowest.
- A decline or "not yet" always has a reason the requester can read.

## Template

```markdown
# AI intake register — [Organization]

| ID | Received | Source | Requester | What (one line) | Business owner | Runs in (tool, plan) | Data class | Overlaps | Tier | Route | Status | Decision | Decided | Days | Reason / conditions |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Routes: fast-track · review group · portfolio gate · not AI (normal process)
Status: received · in review · decided · implemented
```

## Example

Harbor & Pine (excerpt):

| ID | Received | Requester | What | Runs in | Data | Overlaps | Tier | Route | Decision | Days |
|---|---|---|---|---|---|---|---|---|---|---|
| IN-01 | 2 Oct 2026 | Olga (via Samir) | Translation of messages and replies | LinguaFlow Business | D | Deskly Translate, Gemini | Medium | New vendor | Approved with conditions, 19 Nov | 48 |
| IN-04 | 18 Nov 2026 | Noa | Product copy, moved to a company account | CopyGenie | P | Gemini, StoreHub AI | Medium | Fast-track | Approved for P and I, 25 Nov | 7 |
| IN-08 | 17 Nov 2026 | Samir | WhatsApp into the helpdesk | Deskly WhatsApp channel | D | — | Not AI | Normal IT change | Routed, 17 Nov | 0 |
