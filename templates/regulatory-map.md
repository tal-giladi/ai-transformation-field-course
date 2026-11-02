# Regulatory map

A one-page map of which laws, regulator guidance and standards apply to which AI use, in which role (actor), with which obligation, from which date, at which status — and the source you opened and when. It is the "legal register" kept separate from the AI inventory and linked to it by ID. Build it once the inventory is tiered, start with the home jurisdiction, and send the open questions to counsel with the facts. Lesson [04.6](../lessons/module-04/lesson-06.md) shows how; spreadsheet `labs/module-04/regulatory-map.csv` in the module 4 download ([open](../labs/module-04/regulatory-map.csv)). This is a working document, not legal advice.

## How to fill it

- One row per instrument per use (or group of uses); home jurisdiction first, then others that may reach the organization, then voluntary frameworks.
- Status: in force · in force, not yet applying · draft · proposal · voluntary · policy.
- Actor: the role the instrument gives the organization (database owner / controller, holder / processor, employer, deployer, provider).
- "Applies from" is the application date, not adoption, publication or entry into force.
- Source and date checked for every row; law-firm summaries are marked as secondary.
- For each foreign instrument, write the chain of facts that decides scope, and the triggers that would reopen it.
- End with the questions for counsel, each with its facts.

## Template

```markdown
# Regulatory map — [Organization] — v[n], [date]

| # | Instrument | Applies? (why) | Actor | Obligation | Inventory IDs | Applies from | Status | Source (checked) | Evidence owner |
|---|---|---|---|---|---|---|---|---|---|

## Scope reasoning for foreign instruments
[Instrument]: 1. [fact] → 2. [fact] → 3. [fact] → conclusion to propose: [...]
Reopen if: [...]

## Questions for counsel
1. [question] — facts: [...]
```

## Example

Harbor & Pine, 30 November 2026 (excerpt):

| # | Instrument | Applies? | Actor | Obligation | IDs | Applies from | Status | Source |
|---|---|---|---|---|---|---|---|---|
| IL-5 | Privacy Protection (Transfer of Data to Databases Abroad) Regulations, 5761-2001 | Yes | Database owner | A permitted route for each destination | P-01, AI-18, AI-11 | In force | In force | Chambers 2026 (secondary) |
| EU-3 | AI Act Art. 4 (as replaced by Reg. 2026/1744) | Arguably, via drafts sent to EU contacts | Deployer | AI-literacy measures | P-01 | 2 Feb 2025; text replaced 27 Jul 2026 | In force | EUR-Lex (2 Nov 2026) |
| EU-5 | AI Act Art. 26 + Annex III 4(a) | No — output used in Israel | Would be deployer | High-risk deployer duties | AI-01 | 2 Dec 2027 | Not yet applying | EUR-Lex Reg. 2026/1744 Art. 1(40) |
