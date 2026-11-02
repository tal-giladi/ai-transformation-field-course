# AI acceptable-use policy

The short policy that tells every employee whether they may use AI for a task, with which data, in which tool, and what they must check before an output leaves the company. Write it in week two, from what the shadow-AI census found, and keep it to two pages: the tool names live in the approved list, not here. Lesson [04.1](../lessons/module-04/lesson-01.md) shows how.

## How to fill it

- Start from the census: every rule should trace to something people actually do, with the reason they will hear.
- At most ten rules, one line each plus a one-sentence reason.
- Point to the approved / restricted use list and the data classes instead of naming tools.
- Say exactly what is logged about AI use, why, how it is reported and what is not done.
- Test the draft against five real staff questions before it is signed; fix the rules that cannot answer them.
- Name an owner and a review date no more than six months away. Translate into the languages staff work in.

## Template

```markdown
# [Organization] — Using AI at work (v[n], effective [date])

Owner: [role] · Approved by: [name, role, date] · Review: [date, ≤ 6 months] · Languages: [list; master text]
Replaces: [interim rule, date] · Relation to other policies: [e.g. adds to IT policy §x]

## 1. Why
[Two sentences: we want people to use AI; safely, and we stay responsible for what we send.]

## 2. What counts as AI
[The counting rule in one sentence, including AI features inside software we already use.]

## 3. The rules
1. [Rule] — *[reason in one sentence]*
2. [Company accounts only] — *[reason]*
3. [Extensions] — *[reason]*
4. [You own every output: the checks before anything leaves the company] — *[reason]*
5. [No promises the company has not made] — *[reason]*
6. [A person sends every customer-facing output unless management decided otherwise] — *[reason]*
7. [No AI in decisions about people without written approval] — *[reason]*
8. [New tool or use: ask through intake; answer within [n] working days]
9. [Mistakes: report the same day; reporting is never a disciplinary matter]

## 4. Data: what may go where
Public: [...] · Internal: [...] · Confidential business: [...] · Personal: [...] · Highly sensitive: [...]
Unsure? Use the highest class anything in it belongs to. → Approved list: [link]

## 5. Asking for something new
[Form or address] → [who answers] within [n] working days → [what goes to the review group]

## 6. What we log, and why
Collected: [...] · Why: [...] · Reported: [by team / not by person, except ...] · Not done: [routine reading of prompts] · Content accessed only: [when, approved by whom, employee told] · Kept for: [...]

## 7. Owner, exceptions, review
Questions: [...] · Exceptions: [in writing, approved by ..., recorded in the intake register] · Amnesty: [use before date] · Review: [...]

Acknowledgement: [how and by when employees confirm they read it]
```

## Example

Harbor & Pine, v1.0, effective 22 November 2026 (excerpt):

> **3.4 You own every output.** Before anything leaves the company, read all of it and check names, order
> numbers, dates, prices and promises against Priority, Deskly or StoreHub. Remove AI preambles and
> placeholders. *The customer reads what you send.*
>
> **6. What we log, and why.** The web proxy records which websites company computers visit, and approved
> AI tools record which features each account uses and how often. We use this for security, licences and
> to see whether the tools help. We report it by team, not by person. Nobody reads individual prompts or
> conversations as a routine; content is accessed only in a security or legal investigation approved by
> the COO together with HR, and you will be told. Proxy logs are kept 90 days.
