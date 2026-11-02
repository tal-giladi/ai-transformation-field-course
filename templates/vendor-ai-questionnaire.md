# Vendor AI questionnaire

Ten sections to send to, or answer from the documents of, any vendor whose product uses AI on the organization's data: what it does by default, training, retention, location, sub-processors, humans who see the data, security, liability, model changes and exit. Use the same questionnaire for every vendor so reviews compare; answer from the vendor's own terms first and send only the questions the documents leave open. Lesson [04.3](../lessons/module-04/lesson-03.md) shows how; spreadsheet `labs/module-04/vendor-ai-questionnaire.csv` in the module 4 download ([open](../labs/module-04/vendor-ai-questionnaire.csv)).

## How to fill it

- Answer each question from the documents, with the clause. Mark each answer: stated / not stated / contradicts our policy.
- Send the vendor only what is "not stated", with a date for the reply.
- Ask for documents, not adjectives: the SOC 2 report and its period, the certificate and its scope.
- Turn every "contradicts" into a setting, a contract ask or a condition, with an owner and a date before renewal.
- End with a verdict: approve · approve with conditions · not yet, and what must happen before any data flows.

## Template

```markdown
# Vendor AI questionnaire — [vendor, product, plan] — [date]
Reviewer: [name] · Documents read: [terms vx, DPA vx, deck, console] · Renewal / signature date: [date]

| # | Question | Good answer looks like | Answer (clause) | Status |
|---|---|---|---|---|
| 1.1 | Which AI features exist, and which are on by default? | Listed; actions off and lockable | | |
| 1.2 | Can any feature send, change or delete without a person? Who can switch it on? | No, or only named admins | | |
| 2.1 | Is our input or output used to train or improve any model? Opt-in or opt-out? | No, or opt-in only | | |
| 2.2 | If "de-identified", by what method, checked by whom? | Not applicable | | |
| 3.1 | How long are prompts, outputs, logs and analytics kept? Can we change it? | Short and configurable | | |
| 3.2 | Deletion on exit: what, by when, backups? | Dated, with confirmation | | |
| 4.1 | Where is data stored and processed (countries)? | Named | | |
| 4.2 | What contract covers transfers out of our country? | DPA with transfer terms | | |
| 5.1 | Sub-processors: list, notice period, right to object, remedy | Named; ≥ 30 days; exit with refund | | |
| 6.1 | Which people (vendor or sub-processor) can see our content, why, where? | Named, limited | | |
| 7.1 | Security report or certificate: type, period or scope, sites | Current document supplied | | |
| 7.2 | Breach notification: time and channel | Without undue delay, ≤ 72 h | | |
| 8.1 | Who is responsible for outputs? Warranty, indemnity, liability cap | Proportionate | | |
| 9.1 | Will you notify us before changing the model or a feature's behaviour? How far ahead? | Yes, with time to re-test | | |
| 10.1 | Export format and deadline; deletion certificate | Standard format, tested | | |
| 10.2 | Minimum term, renewal, change of control, what happens if you close | Exit right on change of control | | |
| 10.3 | Company: founded, funding, customers in our country and languages | References we can call | | |

## Findings and asks
| Clause | Finding | Setting / contract ask / condition | Owner | Due |
|---|---|---|---|---|

## Verdict
[approve / approve with conditions / not yet] — before any data: [...] — before scale or renewal: [...]
```

## Example

Harbor & Pine — Deskly AI Assist, 17 November 2026 (excerpt):

| # | Answer (clause) | Status |
|---|---|---|
| 1.2 | Autopilot off by default; any workspace Administrator can enable it for any view (§1.2) | Contradicts policy |
| 2.1 | May use content and outputs, de-identified, to train and evaluate models; opt-out by written notice, effective 30 days after receipt (§3.2) | Contradicts policy |
| 3.1 | 30 days operational; 24 months in the analytics store (§3.4) | Contradicts policy |
| 6.1 | QualityOps Services, Philippines: human review of flagged outputs (Annex 1) | Stated — ask what is flagged |
| 9.1 | Not stated | Ask |

Verdict: approve with conditions, pilot only — opt-out confirmed and in effect, Autopilot locked, model provider named, counsel's transfer answer, DPIA signed.
