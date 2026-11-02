# Agentic opportunity frame

A one-page frame for one candidate workflow: the steps as they run today, what simplification removes, what does each remaining step (plain automation, generation, an agent or a person), who builds it, what it connects to with which permissions, who checks it, and the upkeep it creates. Write it for each large candidate after the opportunity map and before the fast screen, so that the screen and the cost estimate are about a real design. Lesson [03.2](../lessons/module-03/lesson-02.md) shows how.

## How to fill it

- Map today's workflow from the data: every step has an owner, a system, a trigger and, where possible, a file that shows it.
- Simplify before choosing technology: list the steps that should not exist, and pick one system of record for every fact.
- Decide per step. Facts (prices, dates, stock, policy terms) always come from a system, never from a model.
- Permissions are explicit: read, write a draft, send or change. Anything that acts on a customer or on money without a person needs a reason.
- Write why it is or is not an agent, and what would change that answer.
- Residue and upkeep have a named owner and an estimate in hours.

## Template

```markdown
# Agentic opportunity frame — [candidate] — [organization] — [date]

**Outcome the change serves:** [one sentence, in the sponsor's words]

## 1. Today
| # | Step | Who / system | Trigger | Evidence (file or person) |
|---|---|---|---|---|

## 2. Simplify
- Steps removed or made unnecessary, and by what: [ ]
- System of record for each fact: [fact → system], checked against [ ]

## 3. New workflow, step by step
| # | Step | Kind (plain automation / generation / agent / person) | Why | Fails how, and who notices |
|---|---|---|---|---|

## 4. Build and run
- Builder: [who], estimate [days or ₪], how sure: [quote / estimate / guess]
- Connections and permissions: [system → read / write draft / send / change]
- Checks: [who checks which output, how often; dry run or shadow period]
- Upkeep and residue: [what people must keep doing so it works, who, hours a month]

## 5. Agent or not
[Why not an agent / why an agent: does the order of steps depend on what each finds? are actions
reversible or held for a person? does every decision point have an owner? What would change the answer.]

## 6. One sentence for the sponsor
[ ]
```

## Example

Harbor & Pine, the promised-date fix, 19 November 2026 (excerpt):

| # | New step | Kind | Why |
|---|---|---|---|
| a | Correct the web store's lead-time table | Person (Noa decides), one-off setting | A business decision about what to promise |
| b | Daily: latest container ETA + about 7 days vs the promised date | Plain automation | A written rule |
| c | Email the customer the new date from four fixed texts (Hebrew, Arabic, Russian, English) | Plain automation | Same message for everyone except date and order number |
| d | Exceptions list to Tamar | Plain automation, read by a person | The judgment is in fixing the sheet |

Builder: Avi with the IT service provider or the Priority partner, about a week (Tamar's estimate). Permissions: Priority orders read, revised-date field write; ETA sheet read; email send from a no-reply address with the four texts only. Checks: two-week dry run to an internal mailbox Samir reads; Tamar's daily list. Residue: Tamar keeps the sheet in a fixed format, about an hour a week. **Agent or not:** plain automation, no AI; nothing here chooses its next step.
