# Risk register

The AI risk register: one row per risk, written as a mechanism, with an owner, the control and its tested status, the evidence and its date, the residual rating, the failure signal that would show the control stopped working, and the next test. Build it from a pre-mortem and starter risks, then test the controls before the ratings go to anyone. Lesson [04.5](../lessons/module-04/lesson-05.md) shows how; spreadsheet `labs/module-04/risk-register.csv` in the module 4 download ([open](../labs/module-04/risk-register.csv)).

## How to fill it

- Mechanism: "Because [condition], [who] may suffer [harm] through [path]." One owner who can change the control.
- Colours defined in words: red = harm likely next quarter or already happening; amber = possible, control not proven; green = control effective, with evidence.
- Control status: effective (runs and catches it, evidence) · designed (planned or on paper, not yet proven) · paper (described, not happening) · missing.
- Evidence is something you sampled or tested, with the date. "Asked the owner" is not evidence.
- No green without evidence; every green has a failure signal (indicator, threshold, who watches, what they do).
- Link each row to the inventory ID; red rows go to the board through the organization's existing risk reporting.

## Template

```markdown
# AI risk register — [Organization] — v[n], [date]
Colours: red = [...] · amber = [...] · green = [...]

| ID | Inventory | Mechanism | Owner | Inherent | Control (kind) | Status | Evidence (method, date) | Residual | Failure signal | Next test |
|---|---|---|---|---|---|---|---|---|---|---|

Kinds: preventive · detective · corrective
Methods: asked (not evidence) · sampled (records, logs, settings) · tested (planted error, injection, setting change)
```

## Example

Harbor & Pine, 26 November 2026 (excerpt):

| ID | Inv. | Mechanism | Owner | Control | Status | Evidence | Residual |
|---|---|---|---|---|---|---|---|
| R-01 | AI-02/03 | Because agents can still reach free chat tools and extensions, customers' messages may be kept and trained on by consumer services through copy and paste | Samir Haddad | AUP, approved tools, extensions removed, proxy host list | Designed | Sampled proxy 11–22 Oct: 160 ChatGPT requests from Customer Service; extension on 9 machines; nothing blocked | Red |
| R-05 | P-01 | Because the helpdesk's AI could be set to send replies itself, unchecked answers may reach customers through Autopilot | Avi Mizrahi | Autopilot off, two admins, monthly check | Effective once set | Console screenshot (due 1 Dec) | Amber → green with the screenshot |
