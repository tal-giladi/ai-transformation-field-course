# Champions playbook

The written rules for a champions network during an AI rollout: what champions do and never do, who they are and why, their protected time and its cost, the issues log and the weekly huddle, office hours, back-ups, and when the launch structure ends. Write it before go-live and give a copy to every champion and their manager. Lesson [06.3](../lessons/module-06/lesson-03.md) shows how; Harbor & Pine's issues log for weeks 1–8 is `labs/module-06/champions-issues-log.csv` in the module 6 download ([open](../labs/module-06/champions-issues-log.csv)).

## How to fill it

- Three jobs (help on real work, collect issues with examples, carry decisions back) and three "never" lines (report individuals, change the tool's settings or prompts, take decisions reserved to others). Write the "never" lines before anyone asks.
- Choose one champion per working group (language, shift, site), respected for the work by colleagues; not only enthusiasts; asked privately with the right to say no.
- Time in the rota, covered, priced as a running cost of the pilot.
- Every issue gets a decision within two huddles and a line in the message back to the team.
- Office hours record topics, never names.

## Template

```markdown
# Champions playbook — [pilot] — v[n], [date]
Owner: [name] · Approved: [manager]

## Purpose
Champions: (1) [help on real work] (2) [issues with examples in the log] (3) [decisions back to the team]
Champions never: (1) report who uses the tool and who does not (2) change prompts or settings (3) [decisions reserved to others]

## Champions
| Name | Group | Why | Time a week | From – to | Back-up |
|---|---|---|---|---|---|
Next round: [names]

## Cost
[hours × rate = ₪; whose budget]

## Issues log
Fields: id, date, by, group, channel, category, what went wrong, example, how often, decision, change ref, owner, status, closed, told the team

## Huddle
[Day, time, length, who; agenda: new issues, top three by frequency and harm, a decision each, three lines to the team]

## Office hours
[Day, time, place, who; what is recorded: topics, not names]

## Load and back-ups
| Role held | Person | Back-up |
|---|---|---|

## End of the launch structure
[Date and decision: rotate / shrink / end]
```

## Example

Harbor & Pine, v1.0, 31 January 2027 (excerpt). Champions: Olga (Russian, also English), Lina (Arabic), Shani (Hebrew), two hours a week each from 8 February to 1 April, 48 hours ≈ ₪6,240 at ₪130 an hour, a running cost of the pilot. Huddle Sundays 12:30, 20 minutes. Office hours Tuesdays 13:00–13:45, live tickets, topics recorded. Issue I-02 (3 February, Olga): ETA blank, so the draft repeats the passed checkout date; T-50240; decision: prompt change PC-02, test set re-run 9 February, released 10 February; told the team in the huddle note of 14 February and job aid v1.1. Olga and Samir are Deskly admins from before the pilot: settings changes only through the pilot lead and change control.
