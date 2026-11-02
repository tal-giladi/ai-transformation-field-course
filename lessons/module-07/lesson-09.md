---
id: "07.9"
module: 7
minutes: 20
practice_minutes: 120
prerequisites: ["07.6", "07.2", "07.8"]
objectives:
  - "Build a deliverable map of everything the engagement produced: owner after handover, where it lives, who uses it, when it is next reviewed, and whether it is living, a record or retired."
  - "Write a handover pack that lets the receiving owner run the service without you: envelope, configuration, evidence, operations, open items, decisions and known limits."
  - "Transfer by doing, with an acceptance test the receiving team passes without you in the room."
  - "Compare your Stage 1 path with the hidden truth and the futures of the choices you could have made."
volatility: concept
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera) — course 7, AI Transformation Advisory Package (integrated deliverable set); course 6 (integration across documents)"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "IBM Lead AI Transformation: Strategy, Governance & Execution Professional Certificate (Coursera) — course 6, Measure AI Value and Scaling Transformation, module 4 (launch is a handoff into operational management)"
    url: https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution
last_verified: "2026-11-02"
---

# 07.9 · Handover: so it survives you

A transformation is finished when it works the week after you leave, not the week you present it. In this lesson you hand Harbor & Pine's drafts service from the project (you) to operations (Samir's team): you map every document the engagement produced and give each an owner or a retirement, write the handover pack, transfer the work by doing it together until the team runs it alone, and check the whole set for contradictions one last time. Then you open the Stage 1 debrief: what was really going on at Harbor & Pine, and what happened in the futures where the team chose differently. At the end you have a deliverable map, a handover pack and a signed acceptance.

## The situation

April to Wednesday 30 June 2027. Gate 1 made the drafts on email and web form a service and put WhatsApp in a fix until Thursday 1 July ([07.2](lesson-02.md)); the operating rhythm runs from April ([07.6](lesson-06.md)). In May the steering committee asked you to lead the second half of 2027: roadmap v2.0 (which Ronit and Tamar will pressure-test, [07.7](lesson-07.md)) and, if its precondition is met, the B2B quotes bet. You stay at Harbor & Pine, but not on the drafts. The handover window ends on 30 June; the next morning the WhatsApp re-gate is run by Samir's team. If they need you in the room, the handover failed.

IBM's leadership course says launch is a handoff into operational management, not the end of responsibility, and that a team that disperses leaves a system nobody is watching. Its consulting capstone integrates a deliverable set into one package. It has no deliverable map and no handover document. Here you write both, and the test that proves the handover worked.

## What to do

### Step 1 — Map every deliverable, and give each an owner or an end

Eight months produced about forty documents. Some must live (they are used every week), some are records (decisions that must be findable), some are finished or retired. A [deliverable map](../../templates/deliverable-map.md) has one row per deliverable: template, version and date, kind (living / record / retired), owner after handover, where it lives, who uses it, when it is next reviewed, what it feeds. Group it the way people will look for it:

| Group | Deliverables (module) | Kind | Owner after handover |
|---|---|---|---|
| Mandate | Engagement charter, scope boundary, 30-60-90 (1) | record | Michal |
| Discovery | Findings memo, task inventory, baselines, data profile, readiness assessment (2) | record (the baselines are re-measured yearly) | Analyst |
| Portfolio | Opportunity map, scorecards, ROI model v3 and the April re-forecast, roadmap v1.1, decision-ready case (3) | ROI and roadmap living; rest record | Ronit (ROI); you (roadmap v2.0) |
| Guardrails | AUP, approved / restricted list, tools and data classes, data boundary, AI inventory, intake register, DPIA, risk register, regulatory map, governance charter (4) | living | Michal (review group); Avi (inventory, tools list); counsel through Ronit (DPIA) |
| Service | Pilot charter v1.1 and rule of use, test sets, eval harness and reports, prompt and source versions, monitoring spec, operating rhythm, incident runbook, change log (5, 7) | living | Samir; analyst |
| People | Workflow redesign, training plan and job aid, champions playbook, adoption dashboard spec, comms plan (6) | living | Samir; Dana for training of new joiners |
| Decisions | Steering packs and minutes, DR-2027-04, incident review, pressure-test log (7) | record | Michal (minutes) |
| Retired | LinguaFlow Customer Service seats; order-status macro; migrated WhatsApp quick replies | retired | Avi (30-day check done 1 June) |

The rows that matter are the ones with no owner. An orphaned living document is a control that has already stopped: the risk register nobody re-rates, the intake register nobody updates after you leave. Each living document gets a named owner who has agreed, and a next-review date in their calendar.

### Step 2 — Write the handover pack

The [handover pack](../../templates/handover-pack.md) is what the receiving owner reads to run the service on a day you are unreachable. Eight sections, short, each pointing to the document that holds the detail:

1. **What the service is: its envelope.** Who uses it (twelve agents), on which channels and languages, at what volume, with what authority (drafts only; an agent sends every reply; the rule of use), and what it may never do.
2. **Configuration.** The tool and plan, the model id and API version, the prompt and source-library versions, the integration and what it can read and write, who holds admin rights in the console (Avi and the analyst, since 23 March). Credentials are handed over through the company's admin process, never written in the pack.
3. **Evidence.** The test sets (400 email and web form; the WhatsApp set of 300), the eval harness, the negative tests, the baselines, and how to re-run them.
4. **Operations.** The operating rhythm, RACI, triggers and monthly agenda ([07.6](lesson-06.md)); the incident runbook ([07.5](lesson-05.md)); contacts with deputies; contracts with renewal and notice dates; the monthly cost and its budget line.
5. **Open items.** The WhatsApp re-gate on 1 July and what it releases (₪42,000 held); open issues from the champions' log; counsel's open questions (PeopleWise); the 13 May checkpoint result.
6. **Decisions and why.** The decision log: each decision since December in one line with its reason and a link (why drafts and not a bot; why per-segment stop rules; why the money flag).
7. **Known limits.** What the evidence does not cover: peak volume (the service has not yet run in November–January), WhatsApp voice notes and photos, follow-ups after a draft was sent, the Arabic dialect gap.
8. **Retirement.** The criteria and the decommissioning checklist.

Write it for the person who will read it at 22:00 during an incident: what to do, where to look, whom to call.

### Step 3 — Transfer by doing, and test it

Documents do not transfer competence; repetitions do. Plan the handover as four stages of the same weekly and monthly work, each with the receiving team doing more:

| Weeks | Who runs it | Who watches |
|---|---|---|
| 6–19 April | You run the rhythm; Shani (the incoming analyst) shadows every item | — |
| 20 April – 16 May | Shani runs the Sunday report, the Wednesday review and the eval re-run; you correct afterwards | You |
| 17 May – 13 June | Shani and Samir run everything, including the 3 June monthly review; you are available but not present | You, on request |
| 14–30 June | Acceptance tests (below); you are absent | — |

The acceptance tests are things the team does without you, observed and recorded:

- **Run the monthly review** (3 June): signals, decisions minuted, owners named.
- **Release a change** through change control: a prompt change with the test-set re-run and the negative tests, logged.
- **Switch drill:** switch one segment off and on, under a minute, by each of the three switch holders.
- **Incident drill:** rerun the paper tabletop ([07.5](lesson-05.md)) with Samir as incident lead and Shani as scribe.
- **Model notice drill:** given a (simulated) deprecation notice, write the migration test plan with dates.
- **Prepare the re-gate pack** for 1 July from the logs, with labels.

Samir signs the acceptance on 30 June when all six are done. What they could not do becomes a dated action, not a reason for you to stay.

### Step 4 — Run the integration check across the whole set

Before you sign the map, read the deliverables side by side one last time, question first ([integration check](../../templates/integration-check.md)). At handover the contradictions are usually between documents written months apart:

| Contradiction | Resolution |
|---|---|
| The operating rhythm costs about 27 hours a month; ROI model v3 counted about 100 hours a year | The July re-forecast nets about 220 hours a year from the capacity line (07.6) |
| The runbook names "the pilot lead" as incident lead | Renamed to the role (service analyst), deputy Samir |
| The DPIA covers email, web form and WhatsApp; the B2B reply helper (IN-08) drafts from customer emails in a separate project | DPIA addendum or the helper's merge decided at the H2 intake review |
| The charter v1.0 stop rules are per language; DR-2027-04 changed them to channel × language | Charter v1.1 issued; the old version marked superseded |
| The roadmap v1.1 still shows "chatbot re-screen 28 Oct 2027" without the condition that WhatsApp drafts pass | Roadmap v2.0 adds the condition |

### Step 5 — Leave the story, not just the files

Two things survive you better than any folder. A sentence the board can repeat: "We fixed the cause first, ran AI where it helps the team, measured it honestly, and handed it to the people who run it." And the three numbers for the board ([04.7](../module-04/lesson-07.md)), now reported by Michal: what reached production, how long decisions take, what was declined and why.

### Step 6 — The Stage 1 debrief

You have run the method end to end at Harbor & Pine. Open the debrief only after you have written your own deliverables, then score your set with the module project's rubric.

<details><summary>Harbor & Pine: the hidden truth, and what happened when the team chose differently</summary>

**What was really going on.** The CEO asked for a chatbot to replace a big part of a 14-person support team, and an AI strategy for the board. The real problem was not customer service. About 38% of support contacts were "where is my order?", caused by a delivery date the web store promised from a fixed lead-time table (Vietnam 42 days, China 38) last changed in February 2023, while containers from Vietnam and China arrived a median 11 days late from June 2026. Logistics knew the real dates and kept them in a hand-made sheet; nobody told customers, and the support team's saved reply repeated the passed date. The biggest, cheapest win was plain automation (a daily job comparing promised dates with container ETAs and writing to customers first), not AI. A chatbot would have answered those customers with the same wrong date.

Under that, three more layers. Most written contact never reached the helpdesk or the KPI report: it arrived on WhatsApp, on four shared phones, with a different order number. The support agents, led by the best of them, Olga, were already using free chatbots with customer names and addresses to write Russian and Arabic replies, because nothing approved existed; punishing her would have lost the pilot's best ally. And an HR system had started ranking job applicants by default, without anyone deciding to.

**Future A: the team followed the previous consultant's roadmap and signed ChatNest in November.** The bot went live on the website in March 2027 (WhatsApp could not be connected: there was no system). It answered "where is my order?" with the order confirmation's date, which had passed; repeat contacts rose. Measured resolution on Harbor & Pine's own contacts by May: about one in five, not 70%. The board, told "40%" in September and "on track" in January, heard in April that support cost had risen. The agents kept using free chatbots for Russian replies. Ronit added the contract to her folder next to the 2022 CRM.

**Future B: the team fixed the dates and ran the pilot, but scaled on the average at gate 1 and wrote warning letters after the incident.** The full ₪72,000 bought pre-filled drafts in April. The WhatsApp pod's non-use stayed invisible in the 73% average; the case's hours never appeared. After the warning letters, agents stopped flagging strange drafts. In June another folder was added to the sources; nobody reported the odd replies for nine days. At gate 2 in September the temps were hired again, and the board stopped believing the programme's numbers.

**Future C: the path this course took.** The date fix went live in January; "where is my order?" fell from about 44% to about 22% of written contact by March. Drafts on email and web form passed every gate condition and became a service owned by Samir. WhatsApp failed honestly at gate 1 and went into a fix with ₪30,000, not ₪72,000. The March incident was contained in 15 minutes, the customers were honoured, counsel decided the reporting question, and the review changed the system, not the people. The translation seats were decommissioned and the saving banked. The case was re-forecast down to about ₪65,000 a year in cash, said plainly. On 1 July the WhatsApp re-gate passed for Hebrew and Russian; Arabic WhatsApp drafts stayed in shadow until August. Gate 2 on 30 September approved hiring one temp for the winter, not two. Ronit now asks for gates on everything; Yoav tells the board "we replaced a vendor's number with our own". The service survived the handover.

**One more choice, briefly.** In the futures where the November census was used to discipline the agents who pasted customer data into free chatbots, Olga left in February, the Russian drafts never reached the gate, and the free-chatbot traffic in the proxy log moved to personal phones, where nobody could see it.

**The expert deliverable set** for Stage 1 is the set of reference answers in each lesson, assembled in the [module 7 project's model answer](../../projects/m07-readout.md).

</details>

## Watch out

- **Handover as a meeting.** A one-hour walkthrough and a folder link is not a handover. Transfer by doing, then test without you.
- **Orphaned living documents.** A register with no owner stopped working on the day you left. Every living document has an owner who agreed and a date in their calendar.
- **Names instead of roles.** "Ask the pilot lead" in a runbook breaks the day the pilot lead moves on. Write roles, with the current person beside them.
- **Credentials in the pack.** Access is handed over through the company's admin process; the pack says who holds rights, never the secrets.
- **Staying "just for the re-gate".** If the team needs you for the first decision, they will need you for every one. Let them run it; be reachable.
- **A handover that hides the limits.** The service has never run a peak. Say so on page one of the pack, not in an appendix.

## Your turn

### Inputs

- Your deliverables from modules 1–7 (or the reference answers in each lesson).
- Module download: `labs/module-07/deliverable-map.csv` (columns and three example rows).
- The operating rhythm ([07.6](lesson-06.md)), the decision record ([07.2](lesson-02.md)), the runbook ([07.5](lesson-05.md)), the champions' issues log (`labs/module-06/champions-issues-log.csv`, module 6 download).
- Templates: [deliverable map](../../templates/deliverable-map.md), [handover pack](../../templates/handover-pack.md), [integration check](../../templates/integration-check.md).

### Steps

1. Fill the deliverable map for every deliverable you produced; mark living, record or retired; give each living one an owner and a next-review date.
2. Write the handover pack in eight sections, each pointing to its source document.
3. Write the four-stage transfer plan and the six acceptance tests with dates.
4. Run the integration check across the set and resolve at least five contradictions.
5. Write the board sentence and confirm who reports the three numbers.
6. Open the debrief. Compare your path with the hidden truth and the three futures: at which decision were you closest to Future A or B? Then score your deliverable set with the rubric in the [module project](../../projects/m07-readout.md).

### Time

120 minutes: 30 for the map, 35 for the pack, 15 for the transfer plan and tests, 20 for the integration check, 20 for the debrief and self-scoring.

### Done when

- [ ] Every deliverable is on the map; every living one has an owner who agreed and a next-review date; retired ones are marked with the date the retirement was checked.
- [ ] The handover pack lets someone run the service at 22:00 without you, and states the service's known limits on its first page.
- [ ] The transfer plan ends with acceptance tests the team passes without you in the room.
- [ ] The integration check resolved at least five contradictions.
- [ ] You compared your path with the hidden truth and the futures, and scored your set with the rubric.

<details><summary>Reference answer</summary>

**Deliverable map (excerpt; 41 rows in full)**

| Deliverable | Kind | Owner after handover | Next review |
|---|---|---|---|
| Pilot charter v1.1 and rule of use | living | Samir | 1 Jul 2027 (re-gate) |
| Operating rhythm v1.0 | living | Samir | monthly; full review Jan 2028 |
| Incident runbook v1.1 | living | Samir (analyst keeps it current) | after every incident; drill each June |
| Test sets, eval harness, negative tests | living | Analyst | monthly re-run; WhatsApp set added 1 Jul |
| ROI model v3 + April re-forecast | living | Ronit | July re-forecast; gate 2 |
| AI inventory, tools and data classes | living | Avi | quarterly |
| Intake register | living | Michal (review group) | monthly |
| DPIA | living | Counsel through Ronit | Jan 2028, or on any new channel or source |
| Risk register | living | Michal (review group) | quarterly, tested risks only |
| Roadmap v1.1 → v2.0 | living | You (H2 lead) | v2.0 pressure-tested by Ronit and Tamar, 15 Jun |
| Findings memo, readiness assessment | record | Michal | baselines re-measured Nov 2027 |
| DR-2027-04, steering minutes, incident review | record | Michal | — |
| LinguaFlow Customer Service seats | retired | Avi | 30-day check passed 1 Jun |

**Handover pack — reply-drafts service — v1.0, 30 June 2027 (from: H2 lead; to: Samir Haddad, owner; Shani Ohayon, analyst).** *Page one, known limits:* not yet run at peak; WhatsApp drafts on re-gate 1 July (Arabic WhatsApp the weakest segment); voice notes and photos get no draft; follow-ups after a sent draft are not checked by the tool. *Envelope:* twelve agents; email and web form in he, ar, ru, en; drafts only, an agent sends every reply; never sets a date, price or amount. *Configuration:* tool and plan as approved in module 4; model id and API version in the change log, line 41; prompt v1.6; source library v3 (Samir's folder; no shared drive); console admins: Avi, Shani. *Evidence:* test set 400 (email and web form) and 300 (WhatsApp); 44 negative tests; re-run instructions in the harness README. *Operations:* 07.6 rhythm and RACI; 07.5 runbook v1.1; contacts with deputies; integrator support contract (renews 31 January); running cost about ₪4,000 a month plus tokens, Customer Service licences line. *Open items:* re-gate 1 July (₪42,000 held); issues I-05 and I-10 closed on 9 June with the WhatsApp style; PeopleWise with counsel. *Decisions and why:* 19 lines from 2 December 2026 to 1 April 2027. *Retirement:* criteria in charter v1.1; checklist from DR-2027-04.

**Transfer and acceptance:** as in Step 3. Acceptance signed by Samir on 30 June after all six tests; one dated action: Samir to run the switch drill with Avi's deputy from the managed-service provider by 15 July.

**Integration check:** the five rows in Step 4, each closed or owned.

**Board sentence:** "We fixed the cause first, ran AI where it helps the team, measured it honestly, and handed it to the people who run it." Michal reports the three numbers from the July board on.

**Debrief, typical self-assessment:** most learners find their closest call to Future B at gate 1 (reading the 73% average) or in the week-2 WhatsApp decision of 07.8, and their closest call to Future A in November, when the discount deadline made signing look urgent.

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting), courses 6 and 7 (integration across documents; the integrated advisory package); IBM, [Lead AI Transformation certificate](https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution), course 6, module 4 (launch as a handoff into operational management). Named, not re-taught.
- Templates: [deliverable map](../../templates/deliverable-map.md), [handover pack](../../templates/handover-pack.md), [integration check](../../templates/integration-check.md), [operating rhythm](../../templates/operating-rhythm.md), [incident runbook](../../templates/incident-runbook.md).
- Earlier: [07.2 · Scale, fix or stop](lesson-02.md), [07.6 · The operating rhythm](lesson-06.md), [04.7 · Governance that runs](../module-04/lesson-07.md). Next: Stage 2 begins with the first engagement, Northwind Outfitters (module 8).
- Module project: [Readout — Harbor & Pine](../../projects/m07-readout.md).
