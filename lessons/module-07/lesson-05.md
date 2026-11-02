---
id: "07.5"
module: 7
minutes: 20
practice_minutes: 105
prerequisites: ["05.7", "05.5", "04.5"]
objectives:
  - "Write an AI incident runbook for one service: what counts as an incident, severity, roles, the switches from narrowest to widest, the steps, the privacy branch and the evidence to keep."
  - "Run an incident tabletop and decide, at each point, how to contain, whom to tell, what to say to customers and the public, and what changed before fixing anything."
  - "Route every reporting question to the DPO or counsel the same day, with the facts they need, instead of guessing the law."
  - "Write a blameless review whose actions change the system (sources, change control, checks), with owners and dates."
volatility: implementation
sources:
  - title: "Moffatt v. Air Canada, 2024 BCCRT 149 — summary by McCarthy Tétrault, 'Moffatt v. Air Canada: A Misrepresentation by an AI Chatbot' (February 2024)"
    url: https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot
  - title: "Amit, Pollak, Matalon & Co., 'Q&A – Reporting security breaches involving personal data in Israel' (client update, 23 May 2023): Privacy Protection (Data Security) Regulations, 5777-2017, severe security incidents"
    url: https://www.ayr.co.il/qa-reporting-security-breaches-involving-personal-data-in-israel/
  - title: "NIST SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile (April 2025)"
    url: https://csrc.nist.gov/pubs/sp/800/61/r3/final
  - title: "Google, Site Reliability Engineering, chapter 15 'Postmortem Culture: Learning from Failure'"
    url: https://sre.google/sre-book/postmortem-culture/
last_verified: "2026-11-02"
---

# 07.5 · When it goes wrong

Every AI service in production will one day say something it should not, and the damage depends less on the error than on the first four hours after someone notices it. In this lesson you write the incident runbook for Harbor & Pine's reply drafts, then live through the incident it was written for: on Monday 15 March 2027 a draft promises a refund outside policy, and by noon you learn that another one disclosed a customer's address. You run it as a tabletop (simulation or paper), compare your decisions with the runbook, and write the blameless review. At the end you have a runbook, an incident log and a review whose actions change the system.

> [!WARNING]
> This lesson is about real harm to real customers: money promised in writing, personal data disclosed, a public post. In a real incident, privacy and reporting questions go to the DPO or counsel the same day, and the decision to report, to whom and by when, is theirs. This course is not legal advice.

## The situation

The lesson has two moments. First, the last week of January 2027: the production-readiness checklist ([05.6](../module-05/lesson-06.md)) says the incident runbook must exist before the first draft is shown on Monday 1 February, and the charter's first stop rule ([05.1](../module-05/lesson-01.md)) points to it. You write it. Then the lesson steps forward to Monday 15 March 2027, 09:40, six weeks into the pilot and two and a half weeks before gate 1 ([07.2](lesson-02.md)): Noa forwards you a Facebook post with a screenshot of one of your replies.

IBM's governance courses name oversight failure (the system did what it was built to do and a person approved the wrong output), the reviewer who gets blamed for a design failure, and the escalation path with a trigger, an owner and authority. They contain no runbook and no incident. NIST's incident-response guidance (SP 800-61 Rev. 3, April 2025) frames response inside overall risk management for cybersecurity; an AI incident adds harms that are not breaches, such as a wrong promise, and causes that are not attacks, such as a changed knowledge source.

## What to do

### Step 1 — Define what counts as an incident, and how bad

People do not escalate what they cannot name. The runbook opens with the harms that make an output an incident, not a bug, and three severities, each with an example from this service:

| Severity | Definition | Example |
|---|---|---|
| S1 | Harm reached customers or the public, or personal data reached someone not entitled to it | A sent reply promises a refund outside policy; a reply quotes another customer's address |
| S2 | Harm possible and likely if nothing changes; nothing (known) sent yet | Drafts quoting an old policy appear in the queue; a negative test fails on the production prompt |
| S3 | Degraded service, no harm | Drafts time out for an hour; agents write by hand |

Harm types for this service: a commitment of money or terms the policy does not allow; personal data disclosed; a safety report (a broken chair leg, a fire risk) mishandled; offensive or discriminatory output; systematically wrong facts (dates, prices); a manipulated output (prompt injection from a customer message). An outage is S3 unless it causes one of these.

Why the promise matters: in Moffatt v. Air Canada (2024 BCCRT 149), a Canadian tribunal held the airline responsible for what its website chatbot told a customer about bereavement fares and rejected the argument that the chatbot was a separate entity responsible for its own words. Harbor & Pine's drafts are sent by a named agent, so a reply is even more plainly the company's own statement. Whether to honour a wrong promise is a business decision taken with counsel, not an IT question.

### Step 2 — Name the roles and the switches

| Role | Who | Deputy |
|---|---|---|
| Incident lead: opens the log, decides containment, sets update times | Pilot lead | Samir |
| Switch holder | Samir, pilot lead or Avi | — |
| Technical: what changed, logs, fix, re-index | Avi with the integrator | — |
| Privacy and reporting | Counsel or the DPO, through Ronit | — |
| Customers | Samir's senior agents (Olga, Lina) by phone | — |
| Public statement and leaders | Michal; Noa for the channel | Yoav for the board chair |
| Scribe | Whoever the lead names in the first minute | — |

Switches go from narrowest to widest, and the runbook says which to try first: drafts off for one category, then one channel or language, then all drafts; prompt or model back to the previous version; a knowledge source removed. The last reversible moment is the agent's send button ([05.6](../module-05/lesson-06.md)): no switch unsends a reply.

### Step 3 — Write the steps in the order you will need them

1. **Log and lead.** Open the incident log at once (time, what we know, what we decided, who decides, next update). Name one incident lead. Tell the sponsor and the owner of the affected team.
2. **Contain.** The narrowest switch that stops the harm, before looking for the cause.
3. **Escalate.** Leaders get facts, unknowns and the next update time. A possible privacy incident goes to the DPO or counsel the same day, with the facts they will ask for (below).
4. **Communicate.** Affected customers directly, by a person; keep what was written to them unless counsel says otherwise. Public statements short, true, owned by the company; never blamed on a tool or a vendor.
5. **Find and fix the cause.** Ask what changed (prompt, model, knowledge sources, settings, data) before changing anything. Fix the cause, then prove it with negative tests.
6. **Restore in stages.** What is safe first; the affected part after shadow mode, with the check that would have caught it.
7. **Review without blame.** Within five working days: timeline, cause, what worked, what did not, actions with owners and dates.

### Step 4 — Write the privacy branch, and do not write the law into it

The privacy branch tells the incident lead what to *do*, not what the law *requires*:

- Preserve the evidence: the helpdesk tickets, the pilot log rows, the vendor console's change history; no deletions until counsel says so.
- Write down which personal data went to whom, when, by which reply, and whether it can be retrieved.
- Brief counsel or the DPO the same day with those facts and the database it came from.
- Counsel decides whether it must be reported to the Privacy Protection Authority, when, and whether the person whose data was disclosed is told; the lead records the decision and its time.

The background counsel will work from: the Privacy Protection (Data Security) Regulations, 5777-2017 (תקנות הגנת הפרטיות (אבטחת מידע), התשע"ז-2017) require a database owner to report a "severe security incident" to the Authority immediately; whether an incident is severe depends on the database's security level and the scope of what happened, and the Authority may order the owner to notify affected people (as summarised by the Israeli law firm Amit, Pollak, Matalon in 2023; Amendment 13 has changed the law since, so counsel works from the current text). That is exactly why the runbook routes the question instead of answering it.

### Step 5 — Run the tabletop

A runbook nobody has rehearsed fails on the first inject. Run it as a tabletop: the scenario unfolds in injects (new information at a time), and the team decides at each one. The simulation runs Harbor & Pine's 15 March incident over four days and scores harm, time to contain, trust and documentation against a runbook:

[Simulation: Incident tabletop](../../simulations/incident-tabletop/index.html?preset=harbor)

Without the simulation, or after it with colleagues, use the paper version with the same six injects and a facilitator's sheet: `labs/module-07/incident-injects.md` (module download).

What the incident is, so you can check your log against it afterwards: on Wednesday 10 March someone added the Customer Service shared-drive folder to the drafting tool's knowledge sources, to give it the new assembly guides. The folder also held the 2023 returns policy (full refund on damage, no collection) and a 2025 export of damage claims with names and addresses. Seven drafts promising refunds outside policy were approved in under ten seconds each and sent; one draft on 12 March quoted another customer's name and street address as "a similar case". The change was made in the vendor's console, untested, with no record of approval.

### Step 6 — Decide at each inject the way the runbook says

The decisions that separate a one-day story from a week-long one, as the course story ran them:

| When | Decision | Why |
|---|---|---|
| 09:40 | Drafts off for damage and returns only, at 09:55; log open; Michal and Samir told | Narrowest switch; the rest of the queue keeps its drafts |
| 10:30 | Ask Avi what changed before touching the prompt; agree with Michal and Ronit to honour the seven written promises (about ₪21,000), call each customer, ask counsel if anything more is needed | A prompt line on top of a wrong source fixes nothing; retracting a written promise turns one story into two |
| 12:00 | Address: a possible privacy incident; logs preserved; facts to counsel by 16:00. Source: folder removed, re-indexed by 13:00, 20 negative tests overnight | Counsel decides reporting; the cause is removed and proven |
| 15:00 | Reporter: "A tool that helps our agents draft replies used an out-of-date policy document. We are contacting every affected customer and honouring what we wrote. A person reads every reply, and we have added a check." Yoav: one page, next update 09:00 | True and owned by the company; the CEO hears it before the chair does |
| Tue 09:00 | Other categories back now; damage and returns after three days in shadow mode with the source shown; a money flag: any draft mentioning a refund, credit or compensation gets a second look | Restore in stages, with the check that would have caught it |
| Thu 09:00 | Blameless review to Monday's steering group; log completed with counsel's decision | The record answers the auditor in October |

### Step 7 — Write the review without blame

Seven drafts approved in under ten seconds is a design signal, not seven careless agents: the tool had been right for six weeks, damage claims arrived at two an hour, and nothing marked a draft that promised money ([05.5](../module-05/lesson-05.md)). A blameless review looks for the contributing causes without indicting anyone, and assumes people acted reasonably on what they knew (Google's SRE book makes the same case for software outages). Its actions change the system:

- **Change control that runs, not just exists.** The monitoring spec ([05.7](../module-05/lesson-07.md)) already classed "a new data source in the context" as a major change needing tests and approval. The console let any admin add a folder. The control existed only on paper, like the "QA within 48 hours" step in the 2024 handbook. Fix: admin rights in the console reduced to Avi and the pilot lead; every source change goes through the release process with the negative tests.
- **One source library.** The tool reads only a curated folder of current documents, owned by Samir; the shared drive is never a source.
- **Negative tests for the new harm.** Twenty tests that tempt a refund or pull another customer's data, run on every change.
- **A money flag** with measured review time on flagged drafts.
- **A spot audit that can see clusters.** Twenty random replies per language per week cannot see seven damage replies in six days; add a weekly targeted sample of every flagged category.
- **Find the other copies.** Search every AI tool for the 2023 policy and the claims export. (This search finds the B2B reply helper that gate 1 deals with in [07.2](lesson-02.md).)

## Watch out

- **Fixing before containing.** Every hour spent finding the cause with drafts still on is another customer harmed. Narrowest switch first.
- **A prompt patch over a wrong source.** "Never promise refunds" makes drafts hedge while they keep quoting the old policy. Ask what changed.
- **Stating the law in the runbook.** "Report within 24 hours" written by the incident lead is a guess. Route to counsel the same day, with facts, and log the decision.
- **Blaming the vendor or the tool in public.** The change was the company's; the reply was the company's. Say so briefly.
- **Retracting a written promise in writing.** Two of the seven post your retraction. Decide with counsel; most companies honour it and fix the cause.
- **Warning letters to the agents.** The next strange draft goes unreported. The fix for a ten-second approval is the design of the check.
- **"Resolved, no further action."** Without changed controls, the next folder gets added in June.

## Your turn

### Inputs

- Your monitoring spec and change control ([05.7](../module-05/lesson-07.md)), human-review design ([05.5](../module-05/lesson-05.md)), charter stop rules ([05.1](../module-05/lesson-01.md)), risk register (module 4).
- The simulation: [Incident tabletop](../../simulations/incident-tabletop/index.html?preset=harbor). Paper version: `labs/module-07/incident-injects.md` (module download).
- Module 6 download: `labs/module-06/champions-issues-log.csv` (issue I-09 is this incident as the team logged it).
- Template: [incident runbook](../../templates/incident-runbook.md).

### Steps

1. Write the runbook for the reply drafts: incident definition and severities, roles with deputies, switches from narrowest to widest, the seven steps, the privacy branch, evidence to keep, update cadence, review deadline.
2. Run the tabletop: the simulation, or the paper version with two to five colleagues. Keep an incident log as you go.
3. Compare your log with your runbook step by step: where did you follow it, where did it not help, what was missing?
4. Write the blameless review: timeline, cause, contributing causes, what worked, what did not, actions with owners and dates.
5. Update the runbook with what the tabletop taught you.

### Time

105 minutes: 35 for the runbook, 30 for the tabletop, 15 for the comparison, 25 for the review and the runbook update.

### Done when

- [ ] The runbook defines incidents by harm, with three severities and an example of each from this service.
- [ ] Every role has a named person and a deputy; switches are ordered from narrowest to widest.
- [ ] The privacy branch says what to do and who decides, and states no legal deadline.
- [ ] In the tabletop, containment came before the search for the cause, and "what changed?" before any fix.
- [ ] The review names no person as the cause, and each action changes a control, with an owner and a date.

<details><summary>Reference answer</summary>

**Incident runbook — reply drafts (v1.0, 27 January 2027; owner: pilot lead; approved by Samir and Michal)** — excerpt.

*Incident:* any output that reached, or is about to reach, a customer and commits money or terms outside policy, discloses personal data, mishandles a safety report, is offensive, gives systematically wrong facts, or follows instructions planted in a customer message. Severities S1–S3 as in Step 1.
*Roles:* as in Step 2. *Switches:* (1) a category off; (2) a channel or language off; (3) all drafts off; (4) prompt or model to the previous version; (5) a source removed and re-indexed. All five tested in the 28 January dry run.
*Steps:* the seven in Step 3. *Updates:* to Michal and Samir every three hours on day 1, then daily; to Yoav one page by 16:00 on day 1 for any S1. *Privacy branch:* as in Step 4. *Evidence:* tickets, pilot log rows, vendor console history, screenshots of public posts, the log. *Review:* within five working days, to the next steering or review-group meeting.

**Incident log INC-01 (excerpt)**

| Time | What we know | Decision | Who |
|---|---|---|---|
| Mon 09:40 | Public post: reply promising ₪4,200 refund, keep the sofa | S1. Log opened; incident lead: pilot lead; Michal, Samir told | Pilot lead |
| 09:55 | — | Drafts off for damage and returns | Samir |
| 10:30 | 7 replies since 10 March promise refunds outside policy; all approved < 10 s | Ask Avi what changed; honour the 7 (about ₪21,000), call each today; counsel asked | Pilot lead, Michal, Ronit |
| 12:00 | Cause: CS shared-drive folder added to sources on 10 March (2023 policy, 2025 claims export with addresses); 12 March draft disclosed one customer's name and address | Possible privacy incident: logs preserved, facts to counsel by 16:00. Folder removed, re-index, 20 negative tests | Avi, Ronit |
| 15:00 | Reporter, comment by 17:00; Yoav calling | Holding statement (Step 6); one page to Yoav, next update Tue 09:00 | Michal, pilot lead |
| Tue 09:00 | 20/20 negative tests pass on re-indexed sources | Other categories on; damage and returns in shadow for three days, source shown; money flag | Samir |
| Wed | Counsel's view on reporting and on informing the customer received | Followed; decision and time recorded | Ronit |
| Fri 19 Mar | Shadow: no repeats | Damage and returns drafts back on | Samir |

**Blameless review (to the steering group, Monday 22 March).** *Cause:* an untested knowledge-source change on 10 March, made in the vendor console, which allowed any admin to add a source. *Contributing:* change control for sources existed in the spec but not in the console; the shared drive held a superseded policy and a claims export with personal data; no flag on money in drafts; a random spot audit too thin to see a cluster in one category; reviewers who had seen six weeks of correct drafts. *Worked:* containment in 15 minutes with the narrowest switch; the log from minute one; counsel briefed the same day; customers honoured and called; a short statement the company owned. *Did not:* nobody noticed for five days; the audit missed it. *Actions:* console admin rights reduced to Avi and the pilot lead (Avi, 23 March); sources only from Samir's curated library, every change through release with negative tests (pilot lead, 26 March); money flag live with measured review time (integrator, 24 March); targeted weekly sample of flagged categories (Olga, from 28 March); search all AI tools for copies of the 2023 policy and the claims export (pilot lead, 26 March; it finds the B2B reply helper, IN-08); the 2023 policy and the 2025 export removed from the shared drive (Samir with Avi, 25 March). *Adopted by the steering group on 22 March.*

</details>

## References

- Moffatt v. Air Canada, 2024 BCCRT 149, as summarised by [McCarthy Tétrault](https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot) (the company is responsible for what its chatbot tells customers).
- Privacy Protection (Data Security) Regulations, 5777-2017, severe security incidents: [Amit, Pollak, Matalon, client update of 23 May 2023](https://www.ayr.co.il/qa-reporting-security-breaches-involving-personal-data-in-israel/) (a law-firm summary that predates Amendment 13; counsel works from the current text). See also the course's [laws and guidance](../../references/laws-and-guidance.md).
- NIST, [SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), Incident Response Recommendations (April 2025); Google, [Postmortem Culture](https://sre.google/sre-book/postmortem-culture/) (blameless postmortems).
- Simulation: [Incident tabletop](../../simulations/incident-tabletop/index.html?preset=harbor).
- Template: [incident runbook](../../templates/incident-runbook.md); earlier templates: [monitoring spec](../../templates/monitoring-spec.md), [production-readiness checklist](../../templates/production-readiness-checklist.md), [risk register](../../templates/risk-register.md).
- Earlier: [05.5 · Human-in-the-loop design that actually checks](../module-05/lesson-05.md), [05.7 · Before launch](../module-05/lesson-07.md). Next: [07.6 · The operating rhythm](lesson-06.md).
