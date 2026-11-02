# Data profile

A one-page check of whether a dataset can carry a named AI use: is it complete, labelled, unique, current, representative and joinable, where did it come from, and may it be used for this purpose. Fill one per dataset per use case, before anyone builds anything on it. Lesson [02.5](../lessons/module-02/lesson-05.md) shows how; a spreadsheet version is `labs/module-02/data-profile.csv` in the module 2 download ([open](../labs/module-02/data-profile.csv)).

## How to fill it

- Name the **use** first ("triage and draft replies for support emails"). A dataset is fit or unfit *for something*; the same file can pass for one use and fail for another.
- Profile only the fields the use needs. Every percentage names its numerator and denominator.
- **Label**: was the outcome the AI would learn from or be judged against ever recorded, consistently, by someone who knew? If not, the verdict is "not yet" and the fix is an outcome-recording routine with an owner and a start date.
- **Currency**: who publishes this copy, how often, and how often is it read? A copy read more often than it is refreshed is stale.
- **Chain of custody**: origin → purpose it was collected for → whether that purpose covers this use → where access is enforced → who owns it today. A chain that ends at "the system" instead of a person is broken.
- **Permission** is not your decision. Write what the privacy notice and contracts say, mark the question, and route it to counsel or the DPO.

## Template

```markdown
# Data profile — [dataset] for [named use] — [date], by [name]

## 1. Identity
File / system: [ ] · Produced by (system / person): [ ] · Provenance: system export / hand-kept / vendor / narrative
Period: [ ] · Rows: [ ] · Owner today (a person): [ ] · Refreshed: [cadence] · Read by the use: [cadence]

## 2. Fitness for the use
| Check | Result (numerator / denominator) | Pass / fix / fail | Note |
|---|---|---|---|
| Completeness of the fields the use needs | | | |
| Label: outcome recorded? by whom? how consistently? | | | |
| Duplicates (rule used) | | | |
| Currency (stale copies, last update) | | | |
| Representativeness (period, languages, channels, seasons) | | | |
| Joinability (keys to other data; formats) | | | |
| Definitions (what each status/category really means) | | | |

## 3. Chain of custody and permission
| Link | Answer | Evidence |
|---|---|---|
| Origin | | |
| Collected for (privacy notice, contract) | | |
| Does that purpose cover this use? | Question for counsel / DPO: [ ] | |
| Personal data fields; special sensitivity? | | |
| Where stored (in Israel / abroad), who can access | | |
| Where access is enforced (system, folder, nobody) | | |
| Accountable person today | | |

## 4. Verdict
Usable now / usable after [fix, owner, date] / not yet: [one sentence]. What would change it: [ ]
```

## Example

Harbor & Pine, `claims/damage-claims-log.csv` for "suggest a decision on damage claims", 24 November 2026 (excerpt):

| Check | Result | Verdict |
|---|---|---|
| Label: decision recorded? | Blank for 48 of 149 claims (32.2%); 31.4% even among claims opened by 30 September, so not just recent ones | Fail |
| Definitions | Three values: approved 55, partly approved 28, rejected 18; no reason field | Fix |
| Currency | One person's Google Sheet, also downloaded by Finance each quarter (two copies) | Fix |
| Permission | Customer names and phone numbers in every row, on the shared drive; privacy notice lists "handle returns and claims" — using past decisions to train or prompt a model is a question for counsel | Route |

**Verdict:** not yet for decision suggestions. What would change it: Rina records a decision and a reason for every claim for eight weeks (owner Samir, from 1 December), names and phones removed from the working copy.
