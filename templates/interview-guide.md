# Interview guide

The script for a 20–45 minute discovery interview that gets at how the work is really done — workflows, workarounds, numbers and the words people use — rather than a wish list for AI. Use one per person, adapted from the stakeholder map. Lesson [02.2](../lessons/module-02/lesson-02.md) shows how to run it and practise it with roleplay personas.

## How to fill it

- Before: fill the header from the stakeholder map, choose at most three things to find out, and decide the attribution rule you can actually keep.
- Ask about the last real case, not the usual case: "the last ten tickets", "last Tuesday".
- Run the same-word test on every word that will end up in a KPI or a decision ("resolved", "ready", "done", "on time", "urgent", "approved").
- Ask how every number was measured, and who measured it.
- Never pitch AI, never lead ("so the bot would help, right?"), never ask for names of colleagues.
- Within 24 hours, write the notes and mark every fact **seen** (you watched it or saw the record), **said** (the person told you) or **said by someone else** (hearsay). Send the person a read-back of what you will use.

## Template

```markdown
# Interview — [person, role] — [date, place, minutes]

From the stakeholder map: need [ ], risk [ ], knows/holds [ ]
Three things to find out: 1. [ ] 2. [ ] 3. [ ]
Attribution rule (said at the start): [e.g. "nothing quoted with your name; you see it first"]

## Opening (2 minutes)
"I'm [name], [role]. I'm trying to understand how the work really happens here — the shortcuts and the annoying parts too. I'm not assessing anyone. [Attribution rule.] You can skip any question."

## 1. The work (most of the time)
- Walk me through [last Tuesday / the last ten items], from the moment [trigger].
- Which part repeats most? Which part takes longest? What do you wait for, and from whom?
- Can you show me one? (screen, sheet, the actual item)

## 2. Numbers and how they are measured
- How many [items] a [day/week]? Where does that number come from?
- [Reported KPI] — what exactly is counted, from when to when, which channels, which days?

## 3. Same-word test
- When you say / the report says "[word]", what has happened? What does it *not* include?
- Would [other role] mean the same thing?

## 4. Workarounds and tools
- What do you do when the system/process doesn't fit? Where did you learn that?
- What tools or files of your own make this faster? (Safe framing: "I'm looking for what works.")

## 5. Exceptions and judgment
- What are the hard cases? Who decides them? What written rule do you follow, and what do you actually do?

## 6. Close (3 minutes)
- If you could change one thing that has nothing to do with AI, what would it be?
- What should I have asked and didn't? Who else should I talk to?
- Read back the three things you will use; confirm the attribution rule.

## Notes (within 24 h)
| # | Fact or quote | Seen / said / hearsay | Follow-up (file to check, person to ask) |
|---|---|---|---|
```

## Example

Samir Haddad, 10 November 2026, extract from the notes:

| # | Fact or quote | Status | Follow-up |
|---|---|---|---|
| 1 | "Most of the night queue is where-is-my-order; the macro gives the promised date, which has already passed." | said | Count the macro tag and the web-form reason in `tickets.csv` (02.4) |
| 2 | KPI "2 hours" = business hours, email only, business days; he set the definition in 2024 | said, matches KPI footnote 1 | Re-measure on all channels and days (02.4) |
| 3 | "If the customer writes again, it's a new ticket" | said | Count follow-ups by customer and order (02.5) |
| 4 | Claims decided by Rina and Samir; handbook says QA | said by someone else (Olga said the same) | Org chart, claims log decision dates (02.3) |
| 5 | "Most customers don't email at all. They WhatsApp the four service phones." | said | No export exists; the one-week hand tally of 18–22 Oct (`whatsapp-week-tally.csv`, 02.4) |
