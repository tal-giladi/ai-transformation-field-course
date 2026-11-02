# Findings memo

The short memo that closes discovery: the question you were asked, your answer in the first three sentences, three to six findings each with its evidence and consequence, what you do not know yet, and the decisions you need. People believe it because every number traces to a file or a person and nothing is stated more strongly than its source. Lesson [02.7](../lessons/module-02/lesson-07.md) shows how to write one and how to check a draft an AI assistant wrote.

## How to fill it

- **Answer first.** The first paragraph answers the sponsor's question in their words. No background before it.
- **One finding = one claim + evidence + consequence.** Claim in one sentence; evidence with file, number, denominator and date; status (verified / reported); consequence in time, money or risk for the decision at hand.
- **Translate twice** where governance is involved: once as an obligation ("customer data leaves approved systems"), once as an operating consequence ("and the fastest Russian replies depend on it").
- **Say what you don't know** and how you will find out. Say what you looked for and did not find.
- **No people blamed, no individuals named** for workarounds. Findings are about the work.
- If an AI assistant drafted any part, check every number, citation and definition against the source and keep the check log in the appendix.

## Template

```markdown
# Findings memo — [question] — [date]

To: [sponsor] · Cc: [ ] · From: [ ] · Status: [draft / final] · Pages: 2 max + appendix

## Answer
[Three sentences: the answer to the question, the one number that carries it, what you recommend deciding.]

## Findings
### 1. [Claim in one sentence]
Evidence: [file / interview, number, n, date] — [verified / reported]
Consequence: [time, money, risk; for whom]

### 2. …

## What we don't know yet
- [Gap] — how we will find out, by when

## What we looked for and did not find
- [ ]

## Decisions needed
| Decision | Options | Recommendation | By whom, by when |
|---|---|---|---|

## Appendix: sources and method; AI use and check log
| Statement in the draft | Source checked | Result (kept / corrected / removed) |
|---|---|---|
```

## Example

Harbor & Pine, to Michal Peretz, 1 December 2026 (excerpt):

> **Answer.** Customers are angry mainly because the delivery date we promise at checkout is never
> updated when a container is late, and the support team spends much of its time answering that one
> question by hand. Between 31% and 38% of helpdesk tickets and 44% of WhatsApp conversations in a tallied week
> ask "where is my order?". I recommend fixing the promise first, with a daily delay notice that needs no
> AI, and preparing an AI draft-reply pilot for the remaining questions from February.
>
> **1. The promised date is a fixed number of days, set in 2023.** Evidence: `storehub-delivery-settings.csv`
> (Vietnam 42 days, China 38, last changed 14 Feb 2023); Vietnam and China orders promised from June were
> delivered a median 11 days late (n = 1,106, `orders.csv`) — verified. Consequence: every late container
> produces a wave of contacts 10–15 days after its original ETA.
