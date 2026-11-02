# Approved tools and data classes

Two tables that decide what data may go into which AI tool: the organization's data classes with its own examples, and a tools × classes matrix built from each tool's terms (training, retention, contract, location). Build it after the acceptable-use policy and before publishing the approved / restricted use list, and re-check a row whenever a vendor changes its terms. Lesson [04.2](../lessons/module-04/lesson-02.md) shows how; the spreadsheet version is `labs/module-04/tools-and-data-classes.csv` in the module 4 download ([open](../labs/module-04/tools-and-data-classes.csv)).

## How to fill it

- Write five classes with at least three examples each from the organization's own files and screens.
- Add the two rules: the highest class in a record wins; identifiers (order numbers, phones, addresses) are personal data.
- For each tool, record the plan and account type, then training, retention, contract and location, with the source and the date you checked. "Unknown" is an answer; it means "No" until found out.
- In the matrix, write Yes, Yes for listed uses (with the condition) or No, and the reason.
- A class D or S cell is never Yes for a tool that trains on input by default or has no company contract.

## Template

```markdown
# Tools and data classes — [Organization] — v[n], [date]

## Data classes
| Class | What it is | Our examples |
|---|---|---|
| P — Public | | |
| I — Internal | | |
| B — Confidential business | | |
| D — Personal data | | |
| S — Highly sensitive | | |
Rules: highest class wins · identifiers are personal data · [legal sensitivity question routed to: ...]

## Tool facts
| Tool | Plan / account | Training on our input | Retention | Contract (DPA?) | Location | Source | Checked |
|---|---|---|---|---|---|---|---|

## Matrix
| Tool | P | I | B | D | S | Notes / conditions |
|---|---|---|---|---|---|---|
```

## Example

Harbor & Pine, 18 November 2026 (excerpt):

| Tool | P | I | B | D | S | Notes |
|---|---|---|---|---|---|---|
| Personal or free AI tools | Yes | No | No | No | No | Consumer terms; may train on input |
| Gemini in Workspace (company accounts) | Yes | Yes | Yes | Listed uses | No | After retention set to 90 days and settings confirmed |
| LinguaFlow Business | Yes | Yes | Yes | Listed uses (translation) | No | DPA: no training, zero retention, EU |
| Deskly AI Assist | — | — | — | Pending vendor review | No | Trains on de-identified content unless opted out (§3.2) |
