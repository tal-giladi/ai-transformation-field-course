# Handover pack

What the receiving owner of an AI service reads to run it on a day the builder is unreachable: the service's envelope, its configuration, the evidence and how to re-run it, the operations (rhythm, runbook, contacts, contracts, costs), open items, the decisions and their reasons, the known limits and the retirement criteria. Use it whenever a service moves from a project team to operations, or from one owner to another, together with a staged transfer and acceptance tests. Lesson [07.9](../lessons/module-07/lesson-09.md) writes Harbor & Pine's.

## How to fill it

- Write for someone reading it at 22:00 during an incident: what to do, where to look, whom to call.
- Known limits go on page one.
- Each section is short and points to the document that holds the detail.
- Roles, with the current person beside them, never names alone.
- Credentials and secrets are handed over through the company's admin process, never written in the pack; the pack says who holds which rights.
- Attach the transfer plan and the acceptance tests; the pack is accepted when the tests are passed without the builder in the room.

## Template

```markdown
# Handover pack — [service] — v[N], [date]
From: [name, role] · To: [owner], [analyst] · Accepted: [date, signature]

**Known limits (read first):** [what the evidence does not cover]

## 1. What the service is (envelope)
Users · channels · languages · volume · what it may decide · what it may never do · rule of use: [link]

## 2. Configuration
Tool and plan · model id and API version · prompt version · source library version · integration (reads / writes) ·
who holds admin rights · where versions and the change log are kept

## 3. Evidence
Test sets · eval harness and how to re-run it · negative tests · baselines · last results

## 4. Operations
Operating rhythm and RACI: [link] · triggers: [link] · incident runbook: [link] ·
contacts and deputies · contracts (renewal, notice) · monthly cost and budget line

## 5. Open items
| Item | Owner | Due |
|---|---|---|

## 6. Decisions and why
| Date | Decision | Reason | Record |
|---|---|---|---|

## 7. Retirement
Criteria: [link] · decommissioning checklist: [link]

## Transfer plan and acceptance tests
| Weeks | Who runs it | Who watches |
|---|---|---|
| Acceptance test | Done on | Observed by |
|---|---|---|
```

## Example

Harbor & Pine's reply-drafts service, v1.0 of 30 June 2027, from the H2 lead to Samir Haddad (owner) and Shani Ohayon (analyst). Known limits on page one: "not yet run at peak; WhatsApp drafts on re-gate 1 July, Arabic WhatsApp the weakest segment; voice notes and photos get no draft." Configuration: prompt v1.6, source library v3 (no shared drive), console admins Avi and Shani. Acceptance tests passed without the builder: the 3 June monthly review, a prompt release through change control, a switch drill by each switch holder, the paper incident tabletop with Samir as lead, a model-notice drill, and the re-gate pack for 1 July.
