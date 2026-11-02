# Stakeholder map

The one-page list of everyone who can shape, block, absorb or be affected by the AI program, written before the first interview: for each, what they need to call it a win and what they risk, in two sentences, what they know or hold, and when and how you will talk to them. Lesson [02.1](../lessons/module-02/lesson-01.md) shows how to build it; a spreadsheet version is `labs/module-02/stakeholder-map.csv` in the module 2 download ([open](../labs/module-02/stakeholder-map.csv)).

## How to fill it

- Start from the org chart and the systems list, then add the people the work touches that the org chart does not show: the receiving team, the person who keeps the hand-made file, the customer.
- **Two-sentence test**: sentence 1 is what this person needs to call the program a win; sentence 2 is what they risk or fear. If you cannot write both, you have not understood them yet: mark the row "to learn" and ask.
- **Knows / holds**: the fact, file or system only they can give you. This sets the interview order.
- **Influence** on the decision (high / medium / low) and **stance now** (supports / neutral / opposes / unknown), each with the evidence for it ("said in the board minutes", "assumed").
- **Protection**: what this person risks by talking to you, and the attribution rule you will offer.
- Review it after every interview. Stances move.

## Template

```markdown
# Stakeholder map — [organization, program] — [date], by [name]

| # | Name, role | Type | Needs to call it a win (sentence 1) | Risks or fears (sentence 2) | Knows / holds | Influence | Stance now (evidence) | Protection and attribution | Interview: when, who introduces, what to find out |
|---|---|---|---|---|---|---|---|---|---|

Types: sponsor · executive · finance · IT/security · legal/DPO · middle manager · frontline · receiving team · data steward · process owner · affected person · vendor · board

## Interview order and why
1. [ ]

## Open questions (rows marked "to learn")
- [ ]
```

## Example

Harbor & Pine, 5 November 2026 (excerpt):

| # | Name, role | Type | Needs (win) | Risks (fear) | Knows / holds | Influence | Stance now | Protection | Interview |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Michal Peretz, COO | Sponsor | Customers stop being angry about deliveries, with a result Yoav can show the board on 28 Jan. | Being seen to slow down the CEO's bot. | Operations budget; why she hired you | High | Supports (01.2) | — | Weekly Thursday check-in |
| 4 | Samir Haddad, CS manager | Middle manager | A team that is not drowning and is recognised for its work. | Five or six of his people cut against the "40%". | The KPI definitions; the queue; the macro | Medium | Unknown, likely guarded (CEO's 40% is public) | No attribution; he sees the write-up first | Week 2, first; introduced by Michal |
| 7 | Tamar Shalev, logistics | Receiving team, data steward | Customer Service off her team's back. | Another sheet to feed by hand; blamed for late ships. | The container ETA sheet (`logistics-eta-tracking.csv`) | Medium | Unknown | Tell her what you will do with her sheet | Week 2, after Samir |
| 12 | Customers waiting for delivery | Affected person | A true date, before they have to ask. | A bot that repeats a wrong date faster. | Their own messages (tickets, WhatsApp) | Low directly, high on revenue | — | Their data stays in approved systems | Read 50 messages; no contact |
