# Access request pack

One page per dataset or system you need, written so that the data owner can approve it in five minutes: what, why, in what form, who approves, where it will live, until when, and whether counsel needs to look. Use it in your first week for everything the data room lacks, and again whenever a later lesson needs new data. Lesson [01.5](../lessons/module-01/lesson-05.md) shows how. This template does not replace legal advice: the "legal check" line is there so the right person decides before data moves.

## How to fill it

- Ask for the minimum: the fields your question needs, a bounded period, no personal details you don't need.
- Ask for an export, read-only. Avoid admin logins.
- Keep pseudonymised data pseudonymised.
- The approver is the system's business owner; your sponsor countersigns; IT or the owner's team executes.
- Give a deletion or return date before you are asked.
- Fill the legal-check line whenever personal data, an outside party (you, if you are a consultant) or a service outside the country is involved.

## Template

```markdown
# Access request AR-[nn] — [dataset or system]

| Field | Entry |
|---|---|
| Requested by, date | [name, role, date] |
| Dataset / system | [ ] |
| Fields | [list; mark any personal fields and why each is needed] |
| Period | [from – to] |
| Purpose (one sentence) | [the question it answers] |
| Used in deliverable | [e.g. findings memo, 1 Dec] |
| Form | [CSV export / report / screenshots; read-only] |
| Pseudonymisation | [what is removed or replaced, by whom] |
| Approver (data owner) | [name, role] |
| Countersigned by (sponsor) | [name, role] |
| Executed by | [IT / owner's team / vendor] |
| Stored where; who can see it | [folder, named people] |
| Deleted or returned by | [date] |
| Legal check | [not needed because … / needed: purpose · outside party · transfer abroad · employees' data → routed to … on …] |
| Status | [sent / approved / partly / refused — reason / received on …] |

## Request log
| AR | Dataset | Owner | Sent | Status | Received | Deletion date |
|---|---|---|---|---|---|---|
```

## Example

> **AR-03 — StoreHub order export** · requested 3 Nov 2026 · Fields: order number, created date,
> promised delivery date shown at checkout, SKU, supplier country, delivery date, status — no names,
> addresses, phones or payment data · Period: 15 Mar – 31 Oct 2026 · Purpose: compare the date promised
> at checkout with ERP orders and container arrivals · Used in: findings memo, 1 Dec · Form: CSV,
> read-only · Approver: Noa Levi (StoreHub owner) · Countersigned: Michal Peretz · Executed by: Lior
> Friedman (e-commerce) · Stored: programme folder, my access only · Deleted by: 31 Jan 2027 · Legal
> check: not needed with no personal fields; if order numbers can be linked to customers, ask counsel
> through Ronit Avraham · Status: sent 3 Nov.
