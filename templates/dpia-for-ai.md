# DPIA for AI

A data protection impact assessment for one AI use, written from the side of the people whose data it uses: what the use does, where the data goes, whether the purpose and notice cover it, what is minimised, what could go wrong for those people, what is done about it, what remains and who accepted it. Write it before a High-tier use starts (or continues), alongside the vendor review, while its measures can still become contract terms. Lesson [04.4](../lessons/module-04/lesson-04.md) shows how. This is a working document, not legal advice: counsel or the DPO advises and their advice is recorded in it.

## How to fill it

- One DPIA per use (a set of very similar uses may share one).
- Copy the data map from the data boundary; add volumes and languages.
- Write risks as mechanism sentences about people — customers, employees, applicants — not about the company.
- Every measure has an owner and a status (in place / planned); every residual risk has a name that accepted it.
- Record who was consulted, including the people who will use the system.
- List the triggers that reopen the DPIA (model change, new data, new channel, automation, six months).

## Template

```markdown
# DPIA — [use ID and name] — v[n], [date]
Owner: [business owner] · Approver: [sponsor] · Advice: [counsel / DPO, date] · Linked: inventory [ID], data boundary [link], risk register [IDs]

## 1. The use
[What it does, for whom, what it may and may not do (the rule of use), stage (shadow / live)]

## 2. Data map
Classes: [...] · Sources: [...] · Volume: [per month] · Languages: [...] · Travels to: [processors, countries] · Seen by: [...] · Retention: [...] · Excluded: [...]

## 3. Purpose and notice
Collected for: [...] · New use fits? [reading + question to counsel] · Notice today says: [...] · Must add: [...]

## 4. Necessity and minimisation
| Data item | Needed because | Or left out |
|---|---|---|

## 5–7. Risks, measures, residual
| # | Because [condition], [who] may suffer [harm] through [path] | Measures (owner, status) | Residual | Accepted by |
|---|---|---|---|---|

## 8. Consultation
[Who, when, what changed because of it]

## 9. Decision and review
Decision: [go / go with conditions / stop] · Conditions: [...] · Reopen if: [...] · Next review: [date]
```

## Example

Harbor & Pine — P-01 reply drafts, v0.3, 26 November 2026 (excerpt):

| # | Mechanism | Measures | Residual | Accepted by |
|---|---|---|---|---|
| R1 | Because drafts state dates and amounts, a customer may be promised a wrong delivery date or refund through an agent who trusts the draft | Facts only from Priority fields; review checklist; error sampling 20 a week | Medium | Michal Peretz |
| R5 | Because quality may be lower in Arabic and Russian, those customers may get worse answers through drafts agents trust | Language-split evaluation; Arabic and Russian only after four weeks of native-speaker spot-checks | Medium | Samir Haddad |
| R7 | Because the tool logs who used which draft, agents may be judged individually through usage data | Team-level reporting only (AUP §6) | Low | Michal Peretz |
