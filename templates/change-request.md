# Change request

The form and the log for every request that would expand the agreed scope: a new objective, new users, new data or systems, a new deliverable, or anything that does not fit the agreed time and money. It keeps requests from disappearing and makes each addition a visible decision about what it displaces. Use it from week one, after the [scope boundary](scope-boundary.md) is acknowledged. Lesson [01.3](../lessons/module-01/lesson-03.md) shows how; a spreadsheet version of the log is `labs/module-01/change-request-log.csv` in the module 1 download ([open](../labs/module-01/change-request-log.csv)).

## How to fill it

- Log every request the day you hear it, in the requester's words. Nothing is deleted; it changes status.
- Run the five refinement questions first. A refinement is done and noted, not logged as a change.
- Fill the assessment within a week: the problem behind the request, who benefits, rough size, link to the objective and what it would displace.
- The decision belongs to the sponsor, or to the sponsor and the owner of the area if it sits outside the sponsor's line.
- Tell the requester the decision, the reason and the review date, in writing.

## Template

```markdown
## Change request CR-[nn]

| Field | Entry |
|---|---|
| Requested by, date | [name, role, date] |
| Request (their words) | "[ ]" |
| Problem behind it | [what is wrong today, for whom] |
| Who benefits | [ ] |
| Link to the objective | [direct / indirect / none — why] |
| Refinement test (5 × yes/no) | objective [ ] · users [ ] · data/systems [ ] · same deliverable [ ] · fits time and money [ ] |
| Rough size | [days, ₪, people, other teams involved] |
| What it would displace | [the work that slips if this is done] |
| Risks and dependencies | [legal review, another team's system, vendor] |
| Recommendation | [approve now / not now, review on … / no] |
| Decided by, date | [ ] |
| Decision and reason | [ ] |
| Requester told (date, how) | [ ] |
| Review date | [ ] |

## Change-request log
| ID | Date | Requester | Request | Refinement / expansion | Status | Decision | Reason | Review date |
|---|---|---|---|---|---|---|---|---|
```

Status values: logged · assessed · approved · not now · declined · done.

## Example

> **CR-05** · Noa Levi (Marketing Director), 5 Nov 2026 · "Translate the whole website into Arabic and
> Russian with AI." · Problem: Arabic- and Russian-speaking customers poorly served online · Link to
> objective: indirect; unknown how many support contacts are caused by language · Refinement test: no
> (new deliverable, new system, legal review) · Size: content for ~250 SKUs and all pages, StoreHub
> configuration, legal review of terms and privacy notice; weeks · Displaces: support-language work in
> the pilot · Recommendation: not now; measure language-related contacts in discovery · Decided by
> Michal Peretz and Yoav Ben-Ami, 10 Dec 2026: not now · Told: Noa, email 11 Dec · Review: Feb 2027.
