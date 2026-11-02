# Readiness assessment

A written, dated judgment of whether the organization around a proposed AI use is ready for it: the work, the data, the owners, the people, the governance, the measurement and the technology. Every finding carries its evidence, its date, its status (verified, reported or contradicted), its consequence for the decision and an owner, and the assessment ends in a verdict per use case: proceed, phase or not yet, with what would change it. Lesson [02.6](../lessons/module-02/lesson-06.md) shows how; a spreadsheet version of the findings log is `labs/module-02/readiness-assessment.csv` in the module 2 download ([open](../labs/module-02/readiness-assessment.csv)).

## How to fill it

- Name the use cases first. Readiness is for something; the verdict can differ per use case.
- State the **bar** for each dimension in one line before you look at the evidence ("every reply that reaches a customer is checked by a named agent").
- One finding per row: observation + consequence. "Outcome missing for 32% of claims" is an observation; "so claims cannot train or test a decision aid until outcomes are recorded" is the finding.
- **Status**: *verified* (you checked it against data you hold or saw it yourself), *reported* (someone says so; not checked), *contradicted* (data you hold says otherwise). Never write a claim stronger than its source.
- **Date** every finding: the organization changes, and so does the bar.
- Every verified gap gets an owner and a date; every reported item gets a verification task.
- The verdict must be allowed to be "not yet". Say what evidence would change it.

## Template

```markdown
# Readiness assessment — [organization] — [date], by [name]

Use cases assessed: A. [ ] · B. [ ] · C. [ ]
Sources: [interviews n, exports profiled, documents read, observation hours]

## 1. Dimensions and bar
| Dimension | The bar for these use cases (one line) |
|---|---|
| Work and process | |
| Data | |
| Ownership | |
| People and adoption | |
| Governance, privacy and legal | |
| Measurement | |
| Technology and security | |

## 2. Findings log
| ID | Dimension | Finding (observation → consequence) | Evidence (source) | Status | Date | Use cases affected | Owner | Action and due date |
|---|---|---|---|---|---|---|---|---|

## 3. Verdict per use case
| Use case | Verdict: proceed / phase / not yet | Turns on (finding IDs) | What would change it | Next review |
|---|---|---|---|---|

## 4. What we did not check
- [ ]
```

## Example

Harbor & Pine, 26 November 2026 (excerpt):

| ID | Dimension | Finding | Evidence | Status | Date | Owner | Action |
|---|---|---|---|---|---|---|---|
| R-03 | Measurement | "First response 2.0 h" is the mean of working hours on Q3 email tickets received Sun–Thu; all tickets on a wall clock: median 6.1 h → the board's baseline is not the customer's wait | `tickets.csv` (n = 2,319); KPI report footnote 1 | Contradicted (as a headline) | 18 Nov | Samir | Publish both definitions from December |
| R-05 | Data | Most written contacts are on four WhatsApp phones; no export exists, one hand tally (630 in a week) → no baseline or test set for the main channel | `whatsapp-week-tally.csv`; Samir | Verified (tally exists); volume reported | 20 Nov | Avi, Samir | Decide channel strategy before any pilot on WhatsApp |

| Use case | Verdict | What would change it |
|---|---|---|
| Proactive delay notice (no AI) | Proceed | — |
| Draft replies for email and web form, human sends | Phase: shadow mode from February | AI-use rule issued; approved tool; four weeks of reply samples labelled |
| Customer-facing chatbot | Not yet | Delay notice live and measured for a quarter; the vendor's deflection shown on Harbor & Pine's own data |
