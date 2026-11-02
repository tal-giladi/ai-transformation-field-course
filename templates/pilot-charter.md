# Pilot charter

The one-page agreement that turns a funded idea into a pilot that can pass, fail or be stopped: a falsifiable hypothesis, scope with reasons, thresholds copied from the business case's gates, stop rules written before they are needed, one accountable owner, and the rule of use (what the AI output may decide, who may override it, how overrides are logged). Write it before anything is built, and get it signed by the sponsor and the owner. Lesson [05.1](../lessons/module-05/lesson-01.md) shows how; the value measurement plan goes with it.

## How to fill it

- One-sentence hypothesis: change, population, effect, guardrail, the decision it feeds. Write the result that would falsify it.
- Scope as two columns, in and out; every "out" has a reason. "Sending without a person" is out unless a separate decision put it in.
- Thresholds are the business case's gate conditions, word for word, each with the instrument that measures it. Change both documents together or neither.
- Every stop rule has a trigger, an action and a named person; include harm, quality, a segment failing, economics, change and law.
- One accountable owner (a person, not a committee), then the supporting roles.
- The rule of use answers three questions: what the output may decide, who may override what, which fields log an override, and how the logs may (and may not) be used.

## Template

```markdown
# Pilot charter — [pilot name], [organization] — v[n], [date]
Signed: [sponsor], sponsor · [owner], owner

**Hypothesis.** If [who] get [the change] for [population], then [effect, number] without
[guardrail], so that [decision]. Falsified if [result].

**Scope**
| In | Out (and why) |
|---|---|
| | |

**Thresholds** (gate [n], [date])
| # | Threshold | Instrument |
|---|---|---|
| a | | |

**Stop rules**
| # | Trigger | Action | Who decides |
|---|---|---|---|
| 1 | Harm: [ ] | | |
| 2 | Quality: [ ] | | |
| 3 | Segment: [ ] | | |
| 4 | Economics: [ ] | | |
| 5 | Change: [ ] | | |
| 6 | Law: [ ] | | |
Switch: [where, held by whom, tested on (date)]

**Owner and roles.** Owner: [name]. Sponsor: [ ]. Pilot lead: [ ]. Technical: [ ]. Quality checks:
[ ]. Value numbers: [ ]. Legal / DPO: [route].

**Rule of use**
- The output may decide: [nothing alone / list]. It proposes: [ ].
- Who may override: [any user: …]; only [names] may [clear which flags / stop].
- Overrides are logged in: [fields, one click each]; reported [per segment and week]; never [used for …].
- Sentence for the team: "[An override is information, not a mistake.]"

**Value measurement plan:** [link]. **Business case:** [link, version].
```

## Example

Harbor & Pine, reply drafts, v1.0, 8 December 2026: "If support agents get an AI draft, in the customer's language, with facts from Priority and the logistics ETA, for every written contact, then the median agent time per written contact falls enough to free at least 109 hours a month at peak volume, without more wrong replies reaching customers or more repeat contacts than today, so that the November 2027 – January 2028 peak can run without the two seasonal temps." Thresholds: gate 1 (a)–(d) of ROI model v3. Rule of use: the AI decides nothing alone; any agent may change the category or rewrite or discard the draft; only Samir or Olga clear safety, legal, privacy or refund flags; three fields log every override, reported per language and week, never per agent, and not used in performance reviews.
