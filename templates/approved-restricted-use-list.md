# Approved / restricted use list

The list the acceptable-use policy points to: AI uses staff may go ahead with, sorted into three tiers of control, and the restricted uses that need the review group — or that nobody may do. Rows are tasks people recognise ("draft a customer reply"), not tool names. Publish it with the policy and update it whenever the intake register approves something. Lesson [04.2](../lessons/module-04/lesson-02.md) shows how; spreadsheet `labs/module-04/approved-restricted-use-list.csv` in the module 4 download ([open](../labs/module-04/approved-restricted-use-list.csv)).

## How to fill it

- Tier 1 — go ahead: approved tool, allowed data class, user checks the output.
- Tier 2 — go ahead within the listed use: personal or confidential business data, for the stated purpose and condition.
- Tier 3 — ask first: new tool, new data class, output reaching customers without a person, decisions about people, automated actions.
- Restricted: say why and who may lift it ("nobody" is allowed).
- Add the eight questions staff ask most, each answered in one line from the list.
- Date every version; one person maintains it.

## Template

```markdown
# Approved / restricted AI use list — [Organization] — v[n], [date]
Maintained by: [name] · Settings checked by: [name] · Tier 3 and restricted changes: [review group]

## Approved uses
| ID | Use | Tier | Tool(s) and plan | Data classes | Condition | Owner |
|---|---|---|---|---|---|---|

## Restricted uses
| ID | Restricted use | Why | Who may lift it |
|---|---|---|---|

## Questions people ask
| Question | Answer (one line) |
|---|---|

## Changes in this version
- [date] [change] [decided by, intake ID]
```

## Example

Harbor & Pine, v1, 18 November 2026 (excerpt):

| ID | Use | Tier | Tool | Data | Condition | Owner |
|---|---|---|---|---|---|---|
| U-02 | Draft and translate a customer reply | 2 | Gemini (Workspace), LinguaFlow Business | D | Only the customer's message; a person checks names, dates, prices, promises and sends | Samir Haddad |
| U-04 | Product and campaign copy | 1 | CopyGenie (company account), Gemini | P | Dimensions and materials checked against the catalogue | Noa Levi |

| ID | Restricted use | Why | Who may lift it |
|---|---|---|---|
| R-01 | AI output sent to customers without a person | Wrong promises at volume | Review group after a pilot and risk review |
| R-02 | Ranking or filtering applicants or employees | Legal duties; livelihoods | COO and HR after counsel's review |

| Question | Answer |
|---|---|
| "Is a supplier record sensitive?" | Prices are B; the rep's name and mobile are D; the record counts as D — approved business tools yes, free tools no |
