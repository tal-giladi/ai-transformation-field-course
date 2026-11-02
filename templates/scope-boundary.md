# Scope boundary

A one-page list of what the current phase includes, what it excludes and what it only reads, each line with a reason, acknowledged in writing by the people who can change it. Write it in week one, right after the engagement charter, and re-issue it whenever a change request is approved. Lesson [01.3](../lessons/module-01/lesson-03.md) shows how.

## How to fill it

- Start with the scope test: one sentence, derived from the objective, that every line answers to.
- Every line has a reason that comes from the objective or a finding, never "good idea" or "not a priority".
- Use **read-only** for things you must look at but are not yours to change (another department's system or rule).
- Every exclusion says "not now" or "no", and gives a review date where it is "not now".
- Record who acknowledged it and when. The sponsor acknowledges the whole; the owner of each area outside the sponsor's line acknowledges the lines that touch it.

## Template

```markdown
# Scope boundary — [Organization], phase [n] ([start] – [end]) — v[1.0]

**Scope test:** Phase [n] includes work that [(a) …], [(b) …] or [(c) …]. Everything else goes on the
request list with a review date.

| # | Item | In / Out / Read-only | Reason (objective or finding) | Review date |
|---|---|---|---|---|
| 1 | [ ] | [ ] | [ ] | [ ] |

**Refinement or expansion?** A request is a refinement only if all five are "yes": same objective ·
same users or customers · same data and systems · same deliverable, deeper · fits the agreed time and
money without dropping anything. Otherwise it is a change request ([change request](change-request.md)).

**Change-request route:** logged by [who] · assessed by [who] within [n] days · decided by [who] at
[which meeting] · requester told within [n] days.

**Acknowledged:**
| Who | For which lines | Date | How |
|---|---|---|---|
| [Sponsor] | All | [ ] | [email / minute] |
```

## Example

Harbor & Pine, phase 1 (2 November 2026 – 28 January 2027), excerpt:

| # | Item | Status | Reason | Review |
|---|---|---|---|---|
| 1 | Customer-service contacts: email, web form, phone | In | The objective: fewer angry customers, support cost that stops rising | — |
| 2 | Shadow AI and AI inside SaaS | In | Risk now: customer data may be in free AI tools | — |
| 5 | Delivery-date promise at checkout (StoreHub lead-time table) | Read-only | Possible driver of contacts; StoreHub belongs to marketing, changes are Noa's and Yoav's decision | — |
| 7 | Sales chatbot on the website | Out | Aims at conversion, not support contacts | Feb 2027 |
| 9 | Headcount decisions | Out | CEO with HR and the labour lawyer, not this programme | — |

Acknowledged: Michal Peretz (all lines), email 6 Nov 2026; Noa Levi (lines 5, 7), email 6 Nov 2026, Yoav Ben-Ami in copy.
