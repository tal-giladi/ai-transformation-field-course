# Human-review design

One page that shows a human check is a working control and not a sentence: who reviews what, what they see beside the AI output, what to check per case type, the capacity screen at peak with the hours it needs and who gives them, the rule for when the queue is too long, who may discard, flag or stop, how reviewers are routed by competence, how their flags lead somewhere, who is accountable when a wrong output gets through, and how AI-drafted outputs are marked. Write it before any AI output reaches a reviewer in production. Lesson [05.5](../lessons/module-05/lesson-05.md) shows how; the oversight-under-load simulation tests the design.

## How to fill it

- Test the check against four conditions: information, authority, time, competence. Any "no" needs a fix in the design.
- Capacity screen at peak and on the busiest day: items × minutes of a real check ÷ 60 = reviewer-hours needed; compare with hours someone has actually given, and with the business case's review line.
- One design answer to each reason reviewers stop checking: flags that go nowhere (feedback loop), load (a load rule), a usually-right tool (point verification where errors cluster).
- Accountability: the four questions asked before any finding about a person.
- Marking: always inside; outside decided with counsel and written down.

## Template

```markdown
# Human-review design — [pilot] — v[n], [date] (owner: [ ]; author: [ ])

| Part | Design |
|---|---|
| What is reviewed, by whom | |
| What the reviewer sees beside the output | |
| What to check, per case type | |
| Capacity screen at peak | [items/day] × [min per real check] = [h/day] ([busiest day: ]); available [h/day, given by]; business case line [h/month] |
| Load rule | [when the queue exceeds …, then …] |
| Authority | [discard / edit / flag / clear flags / stop: who] |
| Competence | [routing by language or skill; training; certification] |
| Feedback loop | [where flags go; when reviewers hear what changed] |
| Spot audit | [who re-reads what, how many, how often] |
| Accountability | Before any finding about a person: information? time? authority? competence? A "no" is a design failure, fixed by [owner] |
| Marking, inside | [fields on every item] |
| Marking, outside | [what customers are told]; question to counsel: [ ] |
```

## Example

Harbor & Pine, reply drafts, 14 January 2027: about 90 drafts a day at peak (112 on Sunday); a real check takes about 3 minutes without the order data on screen and about 2 with it, so the source-beside-the-draft panel moved into the first integration sprint, because it is what makes the business case's 64 review hours a month true; Arabic drafts are routed only to Lina, Rami, Ahmad or Samir, Russian to Olga, Yana or Sergei; when drafts waiting exceed the hours left that day, new tickets get triage only; only Samir or Olga clear safety, legal, privacy or refund flags.
