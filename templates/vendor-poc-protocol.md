# Vendor proof-of-concept protocol

The rules for testing a vendor's product on the organization's own data before signing: which data, under which agreement, which success criteria (fixed and signed before anyone sees results), what the vendor must show, what it is compared against, and what each result means for the decision. Use it whenever a claim is rated "worth testing further" or "not yet supportable". Lesson [04.8](../lessons/module-04/lesson-08.md) shows how.

## How to fill it

- Use your data and your conditions: languages, channels and the hard cases (for a support bot, the most common and the most costly contact types).
- Pseudonymise; sign a DPA with no training and a deletion date before any data moves.
- Write the success definition in your terms, the hard limits (for example a wrong-fact rate) and per-segment minimums. Both sides sign before results.
- Require an inspectable run: what the system looked up and what it answered, per case.
- Run the same test set through the alternative (your own pilot, the current process) so the decision compares like with like.
- Write the decision rule in advance: pass → next step; fail → stop or redesign.

## Template

```markdown
# Proof-of-concept protocol — [vendor, product] — v[n], [date]
Owner: [name] · Vendor contact: [name] · Signed by both sides on: [date, before data transfer]

## Purpose
Which claims this tests: [claim IDs from the read-back]

## Data
Source and period: [...] · Size and mix: [n per segment; hard cases ≥ x%] · Pseudonymisation: [method, by whom] · Agreement: [DPA, no training, deletion by date] · Prerequisites: [e.g. a process fix that must be live first]

## Success criteria (fixed before results)
| Measure | Definition | Threshold | Per segment? |
|---|---|---|---|
| [Resolved] | [e.g. no re-contact on the same order within 14 days and no wrong fact] | | |
| [Wrong-fact rate] | [date, price, policy errors per 100 answers] | [hard limit] | Yes |
| [Cost per resolved contact] | [...] | | |
| [Required behaviours] | [e.g. discloses it is a bot; hands over when asked] | All cases | |

## What the vendor must show
[Per case: inputs used, lookups, answer; access to logs]

## Comparison
[Same test set through: ...]

## Decision rule
Pass: [...] → [next step] · Fail: [...] → [stop / redesign] · Cost: [₪, credited?] · Timeline: [weeks, start condition]
```

## Example

Harbor & Pine — ChatNest (excerpt): 400 past written contacts, May–October 2026, 100 per language, at least 40% delayed-order cases, WhatsApp included once routed; pseudonymised, under a DPA with no training. Resolved = no re-contact on the same order within 14 days and no wrong fact; wrong-fact rate ≤ 2% overall and in every language; the bot discloses it is a bot in its first message. The same 400 contacts go through the drafts pilot. ₪25,000 for four weeks, credited if signed; starts after the delivery-date fix is live.
