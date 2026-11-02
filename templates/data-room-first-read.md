# Data-room first read

A record of your first read of an organization's data room: every file and where it came from, what is missing, and every number in the narrative documents sorted into verified, contradicted, claim to test or unverifiable. Do it on day one or two of every engagement, before you quote any number to anyone. Lesson [01.5](../lessons/module-01/lesson-05.md) shows how; a spreadsheet version of the claims register is `labs/module-01/data-room-first-read.csv` in the module 1 download ([open](../labs/module-01/data-room-first-read.csv)).

## How to fill it

- Inventory first, analysis later: one line per file.
- Provenance is one of: system export · hand-kept file · narrative document · vendor document · written for you.
- For every claim write who said it, where and when (actor, source, date) before you judge it.
- Use only four statuses. "Verified" means an export gives the same number by the same definition; two documents repeating each other are one source.
- Every "claim to test" names the lesson or step where you will test it.

## Template

```markdown
# Data-room first read — [Organization] — [date], by [name]

## 1. What is here
| File | What it is | Produced by (system / person) | Period | Rows or pages | Owner | Provenance |
|---|---|---|---|---|---|---|

## 2. What is missing
| Missing item | Why it matters | Who would have it | Requested on | Status |
|---|---|---|---|---|

## 3. Claims register
| # | Claim (exact words or number) | Who | Where | When | Status | Checked against / how to test | Note |
|---|---|---|---|---|---|---|---|

Statuses: verified · contradicted · claim to test (say where) · unverifiable (say who has an interest)

## 4. Summary for the sponsor (five lines)
- Can rely on: [ ]
- Can't rely on yet: [ ]
- Contradictions found: [ ]
- Asked for: [ ]
- Open questions: [ ]
```

## Example

Harbor & Pine, 3 November 2026, claims register excerpt:

| # | Claim | Who | Where | When | Status | Checked against |
|---|---|---|---|---|---|---|
| 1 | Q3 tickets handled: 1,360 | Samir, Finance BI | KPI report | 6 Oct 2026 | Verified | `tickets.csv`: 425 + 448 + 487 |
| 2 | Average first response 2.0 h | Samir, Finance BI | KPI report | 6 Oct 2026 | Claim to test (02.4) | Footnote: business hours, email only, business days, mean |
| 3 | Containers roughly 2 a week | HR welcome pack | Company profile | Aug 2026 | Contradicted | `shipments.csv`: 112 departures in ~38 weeks ≈ 3 a week |
| 4 | Cut support cost by 40% | CEO | Board minutes | 24 Sep 2026 | Unverifiable | No basis given; a director asked |
