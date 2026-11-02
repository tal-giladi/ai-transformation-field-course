# Task inventory

The list of the tasks a team actually does, one row per task, each with its trigger, volume, time, error rate, variation and the judgment it needs, and whether the process around it can be walked on paper. It is what turns interviews and observation into candidates you can compare. Lesson [02.3](../lessons/module-02/lesson-03.md) shows how to build it from a process walk; a spreadsheet version is `labs/module-02/task-inventory.csv` in the module 2 download ([open](../labs/module-02/task-inventory.csv)).

## How to fill it

- One row per task as the worker does it ("find the real delivery date for a late order"), not per system or per job title.
- **Volume, time, error**: a number and its source (export, tally, observation, said). Leave it blank and write "not measured" rather than guess; a blank is a finding.
- **Variation**: how different the cases are (low: one script fits nearly all; high: every case is different).
- **Judgment**: rule (a written rule decides), pattern (experience recognises it), or judgment (weighing values, money or risk). This later decides between plain automation, AI and leaving it alone (03.2).
- **Walkable on paper?** Yes only if you can write the steps, an owner per step, the trigger and the volume. "No" means the task is not yet a candidate: map it first.
- **Paper vs practice**: where the written procedure and what people do differ.

## Template

```markdown
# Task inventory — [team] — [date], by [name]

| ID | Task (verb + object) | Who | Trigger | Volume / month (source) | Time per item (source) | Error or rework (source) | Variation | Judgment | Languages | Systems and files touched | Walkable on paper? | Paper vs practice | Evidence: seen / said |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
```

## Example

Harbor & Pine Customer Service, 19 November 2026 (excerpt):

| ID | Task | Who | Trigger | Volume / month | Time per item | Error or rework | Variation | Judgment | Walkable? | Paper vs practice |
|---|---|---|---|---|---|---|---|---|---|---|
| CS-01 | Answer "where is my order?" | 12 agents | Customer writes (WhatsApp, email, form) or calls | ~1,200 WhatsApp (tally: 276 in one week × 52/12) + ~130 helpdesk (macro tag, lower bound) + ~170 calls (IVR option 1) | 5–15 min WhatsApp (estimate); up to 2 h waiting for logistics (Olga, seen) | 23% of resolved tickets with an order come back within 14 days (export) | Low | Rule (date lookup) | Yes | Handbook: send the macro with the order date. Practice: best agents skip it and email logistics@ |
| CS-07 | Decide a damage claim | Rina, Samir | Photos arrive | ~25 claims (claims log) | Not measured | Outcome missing on 32% (claims log) | High | Judgment | No: decision step undocumented | Handbook: QA reviews in 48 h. Practice: no QA role since 2023; median 8 days |
