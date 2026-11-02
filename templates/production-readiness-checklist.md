# Production-readiness checklist

The list of everything that must be true before an AI pilot touches real users, each line with evidence, an owner, a status and a due date, plus the consequence for the go-live date if it stays open. It does not move the date; it decides whether the date holds. Fill it a week before go-live and again two days before. Lesson [05.6](../lessons/module-05/lesson-06.md) shows how, with the shadow-mode and staged-release plan it belongs to.

## How to fill it

- Answer every line with evidence (a document, a test result, a date), not "yes".
- Open lines get an owner, a due date and a written consequence ("stage 1 for trained agents only", "a week later").
- The lines that are non-negotiable (privacy basis, negative tests, a tested switch, a human before anything is sent) cannot be traded for others.
- Re-run the checklist before every stage of the release, for what that stage adds.

## Template

```markdown
# Production-readiness checklist — [pilot], stage [n] — [date] (owner: [ ])

| Area | Line | Evidence | Status | Owner, due | If still open on [date] |
|---|---|---|---|---|---|
| Evidence | Eval report verdict; negative tests all pass on the production version | | | | |
| Privacy | Legal basis / counsel's answer; DPIA signed; privacy notice; marking decision | | | | |
| Data boundary | Only [fields] reach the model; [classes] masked before the call | | | | |
| Security | Least privilege (draft only / read only); keys in a vault; injection tests | | | | |
| Vendor | Terms approved (training, retention, location, sub-processors, exit) | | | | |
| Integration | Switch per segment; load rule; holdout; timeout → no output, never a guess | | | | |
| Data preconditions | [lookups, exports, mappings the stage needs] | | | | |
| Review | Source beside the output; checklists; routing by competence; spot audit staffed | | | | |
| Logging and monitoring | Logging live; signals with owners; cost alert; spending limit | | | | |
| People | Training done or booked; who uses it until then | | | | |
| Operations | Owner; support hours; incident runbook; rollback rehearsed (date, time taken) | | | | |
| Timing | Not in peak; not before a holiday or gate week; communication sent | | | | |

**Decision:** [go / go narrower: … / postpone to …], [who], [date].
```

## Example

Harbor & Pine, stage 1, first pass on 20 January 2027: four open lines (privacy notice not yet published; load rule not built; web-store lookup for WhatsApp `HP-1…` order numbers; logging and monitoring); written consequence: without the load rule and logging by 29 January, stage 1 starts for the eight trained agents only, or a week later; without the web-store lookup, WhatsApp "where is my order?" drafts stay off whatever shadow mode shows. Second pass on 29 January: all closed except the lookup; go on 1 February for email and web form, WhatsApp WISMO drafts off.
