# RFP for AI vendors

A request for proposal that makes AI vendors compete on evidence from your conditions, not on their demo: it fixes the criteria and weights before anyone answers, asks how every headline number was measured, requires a proof of concept on your own (synthetic or pseudonymised) data, lists the contract terms that are must-haves, and says how the answers will be scored and who decides. Use it whenever more than one vendor could supply an AI product that touches personal data, customers or clinical work, and before any demo turns into a negotiation. Lesson [10.4](../lessons/module-10/lesson-04.md) shows how; [10.5](../lessons/module-10/lesson-05.md) scores the answers.

## How to fill it

- **Lock the criteria and weights first**, with the decision makers, and date the lock. Weights are a judgement about what matters (at a clinic network: safety and privacy ×3); write them before the demos you have seen colour them. If they were set after the demos, say so.
- **Describe your conditions, not your wishes**: languages and their mix, who is in the room or on the line, noise, channels, the systems it must connect to and their versions, volumes. Vendors can only answer for your conditions if you state them.
- **For every claim you will rely on, ask the five measurement conditions**: sample, what was measured and how success was defined, the mix of tasks and languages, who measured it (independent or not), when and on which version. "Not stated" is an answer you score.
- **Make the proof of concept part of the RFP**: what data (synthetic or pseudonymised), how many items per segment, the metrics, the thresholds fixed before results, who reviews, the timeline, and that the vendor runs the same set as everyone else.
- **Separate must-have terms from nice-to-haves.** A vendor that refuses a must-have is out, however well it scores. Write a one-line reason beside each must-have; the reason is what you negotiate from.
- **Ask for documents, not adjectives**: the data-processing agreement, the sub-processor list, the security report or certificate, the safety case, the regulatory position in writing, three references in conditions like yours.
- **Say who decides what**: the steering group chooses; counsel and the DPO decide the privacy and legal questions; the clinical or business owner decides safety; procurement runs the process. The consultant designs and scores; the organization selects.
- Keep the scoring sheet as a CSV ([`rfp-scoring-sheet.csv`](../labs/module-10/rfp-scoring-sheet.csv) in the module 10 download): one row per vendor and criterion, the demo score and the evidence score side by side, and the evidence for each score.

## Template

```markdown
# Request for proposal — [product type] — [organization] — v[n], [date]
Issued by: [name, role] · Contact for questions: [one named person; no other contact with staff] · Answers due: [date, time]

## 1. Who we are and what we need
[Two paragraphs: the organization, the work the product must support, the stated goal in the sponsor's words]

## 2. Our conditions
| Condition | Our facts |
|---|---|
| Languages and mix | [e.g. Hebrew 30%, Arabic 38%, Russian 28%, other 3%; dialects] |
| People in the conversation | [e.g. relatives in about a third of visits; interpreters] |
| Setting | [rooms, noise, devices, connectivity] |
| Volumes | [items a day / month; users] |
| Systems to connect to | [system, version(s), interface available] |
| Data that would flow | [categories; special sensitivity; where it may be processed] |

## 3. How we will choose
Criteria and weights, locked on [date] by [forum]:
| Criterion | Weight | What a 5 looks like | What a 1 looks like |
|---|---|---|---|
| [Evidence (measured, independent, in conditions like ours)] | [2] | | |
| [Safety / quality of output] | [3] | | |
| [Privacy and data] | [3] | | |
| [Languages] | [2] | | |
| [Integration] | [1] | | |
| [Contract and exit] | [2] | | |
Scoring: each criterion 1–5 on the evidence in your answer and the proof of concept; the demo is not scored. Must-have terms are pass/fail.

## 4. Claims: how they were measured
For every number in your materials that you want us to rely on:
| Claim (as stated, where) | Sample (n, real or scripted) | What was measured; definition of success | Task and language mix | Who measured it | When; product version |
|---|---|---|---|---|---|

## 5. Proof of concept (part of this RFP)
Data: [n items, per segment; synthetic or pseudonymised; under NDA / DPA] · Each vendor processes: [the same set, n runs] · Metrics: [list, defined] · Thresholds (fixed before results): [list] · Review: [who, blind where possible] · Dates: [delivery, return, results] · Cost: [who pays]

## 6. Contract terms
| # | Term | Must-have? | Why | Your answer (accept / refuse / propose) |
|---|---|---|---|---|
| T1 | [No use of our data to train or improve models, de-identified included] | Yes | | |
| T2 | [Retention and deletion] | Yes | | |
| T3 | [Location of storage and processing] | Yes | | |
| T4 | [Sub-processors: list, notice, objection] | Yes | | |
| T5 | [Model changes: notice and re-test on our set] | Yes | | |
| T6 | [Safety / incident reporting, named owner] | Yes | | |
| T7 | [Exit: data return, certified deletion, transition] | Yes | | |
| T8 | [Audit rights / certification] | No | | |
| T9 | [Price for years 2–3] | No | | |

## 7. Documents to attach
[DPA · sub-processor list · security report or certificate · safety case / hazard log · regulatory position in writing · independent evaluations · three references in conditions like ours · price for three years]

## 8. Process and rules
[Timetable · single point of contact · no gifts or side meetings · answers become part of the contract · we may reject all answers · who decides: steering group; privacy and legal questions: counsel and the DPO; safety: the clinical owner]
```

## Example

Harbor & Pine — RFP for a customer-chat assistant, v1 (excerpt, written after the ChatNest read-back in [04.8](../lessons/module-04/lesson-08.md)):

**Conditions:** written contacts in Hebrew, Arabic, Russian and English (about 3,200 a month); a third about delayed orders whose promised date is wrong in the order confirmation; WhatsApp and web chat; the helpdesk and the order system (no live order-tracking feed yet). **Criteria locked 26 November:** resolution without re-contact ×3, wrong-fact rate ×3, privacy and data ×2, languages ×2, integration ×1, contract and exit ×2. **Claims:** "70% of conversations resolved" must state sample, definition (no transfer in the session vs no re-contact in 14 days), country and language mix, who measured it. **Proof of concept:** 400 past contacts, 100 per language, at least 40% delayed-order cases, after the delivery-date fix; thresholds before results: wrong-fact rate ≤ 2% in every language. **Must-haves:** no training on our conversations; a 30-day deletion; an export tested before go-live; change-of-control exit; no auto-renewal.
