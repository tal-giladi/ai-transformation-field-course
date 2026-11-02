---
id: "04.4"
module: 4
minutes: 20
practice_minutes: 110
prerequisites: ["04.3", "01.7"]
objectives:
  - "Tier every AI inventory row High, Medium or Low with a rule written as checkable conditions, and record the reason and any override."
  - "Decide from written triggers which uses need a DPIA, and route the legal reading to counsel."
  - "Write a DPIA for an AI use that assesses risks to the people whose data it uses, with measures, residual risk, owner and review triggers."
  - "Find what the organization's privacy notice must say before the use starts."
volatility: implementation
sources:
  - title: "EBN Law — PPA draft AI guidance (April 2025): privacy impact assessments recommended; transparency about AI processing"
    url: https://www.ebnlaw.co.il/media-center/draft-guidance-from-the-israeli-privacy-protection-authority/
  - title: "Pearl Cohen — Israel: New Draft Guidelines on the Application of Privacy Law to AI (4 May 2025)"
    url: https://www.pearlcohen.com/israel-new-draft-guidelines-on-the-application-of-privacy-law-to-ai/
  - title: "Chambers Practice Guides — Data Protection & Privacy 2026: Israel (notice of collection after Amendment 13; security levels; risk assessments)"
    url: https://practiceguides.chambers.com/practice-guides/data-protection-privacy-2026/israel
  - title: "GDPR, Regulation (EU) 2016/679, Article 35 (data protection impact assessment) — EUR-Lex"
    url: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679
  - title: "Regulation (EU) 2026/1744, Article 1(13): AI Act Article 27(4)–(5) as replaced (FRIA may cross-refer to the DPIA)"
    url: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202601744
  - title: "Barnea Jaffa Lande — Final PPA position statement on the obligation to appoint a DPO (22 July 2026)"
    url: https://barlaw.co.il/practice_areas/regulation/privacy-law/client_updates/position-statement-on-the-obligation-to-appoint-a-dpo-not-a-change-in-the-law-but-a-change-in-the-rules-of-the-game/
last_verified: "2026-11-02"
---

# 04.4 · AI inventory, risk tiering and the DPIA

The inventory from 01.7 says what AI exists; it does not yet say which rows deserve most of your attention. In this lesson you tier every row with a rule anyone can re-apply, decide which uses need a data protection impact assessment (DPIA), and write one for the use that matters most at Harbor & Pine: the drafts pilot that will read most customers' messages. At the end you have a tiered inventory, a DPIA you could hand to counsel, and the list of what the privacy notice must say before the pilot starts.

## The situation

It is Monday 23 November 2026. The inventory has 17 AI rows and three excluded ones, each with a "first risk view" you wrote in a hurry (01.7). Since then the portfolio work (module 3) chose the reply-drafts pilot: from February 2027 it will draft replies for all written support contact — email, the web form, and WhatsApp once it is routed into the helpdesk — and a person will send every reply. The vendor review (04.3) approved LinguaFlow Business and put conditions on Deskly AI Assist, which will probably run the pilot. Yoav still wants ChatNest.

IBM's governance and consulting courses say to classify by checkable conditions, not by feel, and to classify twice: by consequence and by authority (what the system may do without a person). This lesson turns that into a rule and applies it to every row.

## What to do

### Step 1 — Write the tier rule as checkable conditions

A tier you can argue about is not a tier. Write conditions someone else can check from the inventory and get the same answer. Harbor & Pine's rule:

| Tier | Any of these conditions | What the tier requires |
|---|---|---|
| **High** | H1 decides about or ranks people (hiring, pay, credit, access to a service) · H2 acts or sends without a person, where a wrong output costs someone money, rights or safety · H3 highly sensitive data (class S) · H4 personal data (class D) of more than 1,000 people or contacts a month, sent to new recipients | DPIA before use; governance committee approval; risk-register rows with tested controls; named owner; monitoring |
| **Medium** | M1 personal data (class D) · M2 output reaches customers or the public · M3 confidential business data in an outside tool | On the approved list with its condition; vendor review and data boundary; one risk-register row |
| **Low** | None of the above | Inventory row; reviewed once a year |

The conditions combine the two readings IBM asks for. H1 and H3 are about **consequence** (who can be harmed, how badly); H2 is about **authority** (whether a person stands between the output and the world). The data classes are the ones you defined in 04.2.

Two rules keep the tiers honest. **Tier the use, not the tool:** Gemini summarising meeting notes and Gemini drafting customer replies are two rows. And **overrides are allowed only in writing:** if the committee decides a row the rule calls High is really Medium, the reason goes in the row, with a name and a date.

### Step 2 — Apply it to the inventory

Add five columns to the inventory: the facts the rule needs (highest data class, decides about people, acts without a person and the harm if wrong, reaches outside, volume and new recipients), then the tier and the reason. The spreadsheet `labs/module-04/ai-inventory-tiering.csv` in the module download has 14 rows filled with those facts; apply the rule by hand, or with the script (Track B, below).

Harbor & Pine, 23 November 2026:

| ID | Use | Tier | Why |
|---|---|---|---|
| P-01 | Reply drafts for all written contact (pilot, in Deskly AI Assist) | **High** | H4: about 3,200 written contacts a month (630 WhatsApp conversations in the tallied week plus 570 helpdesk tickets in October), new recipients in the US, Ireland and the Philippines |
| AI-01 | PeopleWise AI Candidate Match | **High** | H1 ranks and hides applicants; H3 candidate data |
| AI-19 | ChatNest customer chatbot (proposed) | **High** | H2 answers customers without a person (a wrong delivery date or refund costs money); H4 |
| AI-18 | LinguaFlow Business translation | Medium | M1, M2; about 800 contacts a month, under the scale line |
| AI-11 | Gemini in Workspace, drafting and summaries | Medium | M1, M2 |
| AI-08 | MailPost subject lines and send times | Medium | M1, M2; it acts without a person, but a badly timed newsletter costs nobody money, so not H2 |
| AI-07, AI-04 | Product descriptions, marketing copy | Medium | M2: published text (wrong dimensions reach customers) |
| AI-06 | Claude (personal) in Finance | Medium | M3: finance data in an outside tool; use unknown |
| AI-02, AI-03, AI-10 | ChatGPT consumer, free LinguaFlow, Grammarly | Medium | M1, M2; stopped or being removed — the tier says how bad it was, the list says it is not allowed |
| AI-12 | Zoom AI Companion | Medium | M1 if switched on; to verify |
| AI-16 | Bitdefender ML detection | Low | No condition |

Three things the tiering teaches. The pilot everyone thinks of as "safe because a person sends" is High, because of what it reads and where that goes, not because of what it decides. The HR feature nobody chose is the other High row. And Medium is crowded: that is fine, because Medium's controls (approved list, data boundary, one risk row) are cheap and mostly done.

### Step 3 — Decide where a DPIA is needed

A DPIA is a structured look at a use **from the side of the people whose data it uses**: what happens to their data, what could go wrong for them, what you do about it, and who accepted what is left.

Israel first. In the sources checked for this lesson, Israeli law sets no general DPIA duty like the GDPR's for a company like Harbor & Pine (counsel confirms); three instruments still point the same way:

- The Privacy Protection Authority's **draft** AI guidance (April 2025, still a draft on 2 November 2026) recommends privacy impact assessments as a risk tool for AI (EBN Law: "recommends (but does not require)"; Pearl Cohen: organizations "should conduct" DPIAs).
- The Privacy Protection (Data Security) Regulations, 5777-2017, require risk assessments for databases at the medium and high security levels (Chambers' 2026 guide). Which level Harbor & Pine's customer databases are at is a question for counsel (04.2).
- Amendment 13 to the Privacy Protection Law expanded the notice owed to people when their data is collected (Step 5). A DPIA is where you find out whether the current notice still covers what you are about to do.

For comparison, the GDPR makes a DPIA mandatory where processing "in particular using new technologies" is "likely to result in a high risk to the rights and freedoms of natural persons" (Article 35(1)), and always for systematic evaluation with significant effects, large-scale special categories and large-scale public monitoring (Article 35(3)). The EU AI Act asks certain deployers of high-risk systems for a separate fundamental-rights impact assessment; since the Digital Omnibus (Regulation (EU) 2026/1744) it may cross-refer to the DPIA (Article 27(4) as replaced). Whether either reaches Harbor & Pine is 04.6's question. The criteria are still the best test available, so borrow them.

Harbor & Pine's DPIA triggers (any one means "write a DPIA before the use starts or continues"):

1. Decisions about people (H1).
2. Highly sensitive data (class S).
3. New technology on personal data at scale (class D, more than 1,000 people or contacts a month).
4. Personal data going to new recipients at scale, including abroad.
5. A new purpose for data collected for something else.
6. Systematic monitoring of people, including employees (module 6's usage dashboard will need this test).

Result: **P-01 needs a DPIA now** (triggers 3, 4, 5). **AI-01 PeopleWise** needs one before it is ever switched back on (1, 2); it stays off while counsel reviews (01.7). **AI-19 ChatNest** needs one before any pilot (3, 4, and H2). MailPost, Grammarly and Zoom have unknown volumes: find out before deciding.

Who signs? Amendment 13 requires certain organizations to appoint a data protection officer; the Privacy Protection Authority published its final position statement on that duty in July 2026, covering public bodies, data trading, and organizations whose core business includes ongoing and systematic monitoring or large-scale processing of sensitive data (Barnea Jaffa Lande, 22 July 2026). Whether Harbor & Pine falls inside is counsel's call. Until there is a DPO, the DPIA is owned by the business owner (Samir for P-01), approved by Michal, with counsel's advice recorded in it.

### Step 4 — Write the DPIA in nine sections

Use the [DPIA for AI template](../../templates/dpia-for-ai.md). The sections, with what makes each one useful rather than ceremonial:

1. **The use in one paragraph** — what it does, for whom, what it may and may not do. Copy the rule of use, not the vendor's marketing.
2. **Data map** — classes, sources, volumes, where it travels, who sees it, retention. Your data boundary (04.3) is most of this.
3. **Purpose and notice** — what the data was collected for, whether the new use fits, what the privacy notice says and must say.
4. **Necessity and minimisation** — why each data item is needed; what you leave out.
5. **Risks to people** — written as mechanism sentences: "Because [condition], [person] may suffer [harm] through [path]." People, not the company: customers, employees, applicants.
6. **Measures** — preventive, detective, corrective; each with an owner and a status (in place / planned).
7. **Residual risk** — after measures, per risk, with who accepted it.
8. **Consultation** — who was asked: the team that will use it, IT, counsel; the people affected where possible.
9. **Decision and review triggers** — go / go with conditions / stop; what reopens the DPIA.

The risks section is where DPIAs usually fail: a list of categories ("privacy", "accuracy") instead of mechanisms. A mechanism names a path you can put a control on.

### Step 5 — Check the privacy notice against the use

Harbor & Pine's notice (`policies/privacy-notice.md`, last updated 1 January 2022) says messages are used "to answer your questions and complaints", shared with "service providers that host or operate our systems", and kept "for as long as we need it". It says nothing about AI, about which countries, or about the 24 months Deskly keeps AI analytics.

After Amendment 13, a notice of collection must cover, among other things, the purposes, the controller's identity, the recipients and why data is disclosed to them, whether providing the data is legally required and what happens if the person refuses, and the rights of access and correction (Chambers' 2026 summary of section 11). The PPA's draft AI guidance adds that organizations should explain the purposes and methods of AI processing and tell people when they are interacting with a bot. P-01 is not a bot — a person sends every reply — but the notice should still say that messages are processed with AI tools by named kinds of providers, abroad.

Write the gap list and the proposed wording for counsel; do not publish a new notice yourself. Deskly's terms already put this duty on Harbor & Pine (§7.2).

## Watch out

- **Tiering by tool.** Gemini for meeting notes and Gemini for customer replies are different risks. Tier uses.
- **"A human sends it, so it's low risk."** The reviewer limits what goes out; it does not change what the system reads, keeps and sends abroad. P-01 is High on data alone.
- **Tier inflation.** If everything is High, nothing is. Keep the conditions narrow and record overrides with a reason.
- **A DPIA about the company.** "Reputational risk" and "regulatory fines" are the company's risks. The DPIA asks what happens to the customer, the agent, the applicant.
- **Writing the DPIA after the contract.** Its measures (opt-out, retention, notice) are contract asks; after signature they are wishes.
- **Signing it yourself.** You draft. The business owner owns it, the sponsor approves, counsel advises, and a DPO signs if one is appointed.
- **Forgetting the employees.** Agents' work in the tool is logged; usage dashboards (module 6) are monitoring. They are data subjects too.

## Your turn

### Inputs

- Data room (module download): `it/saas-list.csv`, `it/peoplewise-release-notes-2026-03.md`, `policies/privacy-notice.md`, `policies/data-retention-note.md`, `vendors/deskly-ai-addon-terms.md`, `support/whatsapp-week-tally.csv`, `support/tickets.csv` ([INDEX](../../labs/common/harbor-and-pine/INDEX.md)).
- Your inventory (01.7), approved list (04.2), vendor review and data boundaries (04.3).
- Spreadsheet: `labs/module-04/ai-inventory-tiering.csv`; Track B script `labs/module-04/tier_inventory.py` ([lab README](../../labs/module-04/README.md)).
- Templates: [AI inventory](../../templates/ai-inventory.md), [DPIA for AI](../../templates/dpia-for-ai.md).

### Steps

1. Write your tier rule (or adopt Step 1's) and the DPIA triggers.
2. Add the rule's facts to every inventory row and assign tiers, with the reason and any override.
3. List which rows need a DPIA, which need facts first, and which need none.
4. Write the DPIA for P-01: all nine sections, at least six risks as mechanism sentences, each with measures, owner and residual rating.
5. Write the privacy-notice gap list and the questions for counsel.

**Track B (Python).** From `labs/module-04/`, run `python tier_inventory.py`. Change one fact (for example set P-01's `new_recipients` to `n`, as if the pilot ran on a tool already holding the data) and run it again. Python is worth it here because the inventory is re-tiered every quarter and after every vendor change; a script applies the rule identically each time and shows which fact moved a row.

### Time

110 minutes (the DPIA is most of it).

### Done when

- [ ] The tier rule fits in one table and every condition can be checked from inventory columns.
- [ ] Every row has a tier and a reason; overrides have a name, date and reason.
- [ ] P-01 is High, with the reason, even though a person sends every reply.
- [ ] DPIA needs are decided from triggers, including "facts first" where the volume is unknown.
- [ ] The DPIA's risks are mechanism sentences about people, including the agents.
- [ ] Every measure has an owner and a status; every residual risk has an accepter.
- [ ] The notice gap list compares the 2022 notice to the use and goes to counsel as questions.

<details><summary>Reference answer</summary>

**Tiers:** as in Step 2 (3 High, 10 Medium, 1 Low across the 14 rows in the spreadsheet; the script prints the same). DPIA: P-01 now; AI-01 before any re-enable; AI-19 before any pilot; volumes first for AI-08, AI-10, AI-12.

**DPIA — P-01 Reply drafts (draft v0.3, 26 November 2026). Owner: Samir Haddad. Approver: Michal Peretz. Advice: company counsel (via Ronit). No DPO appointed (question with counsel).**

1. *The use.* For every written support contact (email, web form; WhatsApp once routed into Deskly), the tool proposes a category and a reply draft in the customer's language from the message, the customer's order status and the help-centre articles. An agent reads, edits and sends. The tool cannot send, refund, change orders or see payment data. Stage 1 (February–March 2027) runs in shadow: drafts are produced and compared, nothing generated is sent.
2. *Data map.* Class D: names, emails, phones, addresses, order numbers, message text, damage photos; about 3,200 contacts a month, in Hebrew (about 60%), Arabic, English and Russian. Travels: Deskly (US) → model provider (US, name pending) → LangBridge (Ireland) → QualityOps (Philippines, flagged items). Retention: 30 days operational, 24 months analytics (negotiating), tickets "forever" today. Not included: payment details, ID numbers, health information.
3. *Purpose and notice.* Collected "to answer your questions and complaints" (notice §2); drafting answers fits that purpose in the plain reading — counsel to confirm. Vendor model training is a different purpose: excluded by the §3.2 opt-out. The notice does not mention AI processing or overseas recipients (Step 5).
4. *Minimisation.* The draft needs the current message, the order's status and promised and actual dates, and the help-centre articles. It does not need the customer's history of other tickets, phone number or full address: exclude them from the prompt. Test set for module 5: pseudonymised.
5–7. *Risks, measures, residual.*

| # | Mechanism | Measures (owner, status) | Residual (accepted by) |
|---|---|---|---|
| R1 | Because drafts state dates and amounts, a customer may be promised a wrong delivery date or refund through an agent who trusts the draft | Facts only from Priority fields, not generated; review checklist; no promise wording allowed in drafts (Samir, planned); error sampling 20 a week (you, planned) | Medium (Michal) |
| R2 | Because the tool reads many customers' data, one customer may receive another's details through a draft built from the wrong ticket or order | Order lookup by ticket's requester only; agent checks name and order (Samir, planned); tested in module 5 negative tests | Low–Medium (Michal) |
| R3 | Because Deskly keeps AI content 24 months in the US, customers' messages may be exposed or reused far beyond the reply's need | Opt-out of training (Samir, sent 18 Nov); retention renegotiation (Ronit, by 31 Dec); counsel on transfer route | Medium until renegotiated (Michal) |
| R4 | Because flagged outputs are read by reviewers in the Philippines, customers' messages may be seen by people they never expected | Ask Deskly what is flagged and the contract terms (you, 19 Nov); notice update | Open — decide after Deskly answers |
| R5 | Because quality may be lower in Arabic and Russian, those customers may get worse or wrong answers through drafts agents trust | Language-split evaluation (module 5); Hebrew and English first, Arabic and Russian after four weeks of native-speaker spot-checks | Medium (Samir) |
| R6 | Because a customer message can contain instructions, a planted instruction may put a false promise or another customer's data into a draft | No actions or sending; agent review; injection tests in the test set (04.5) | Medium (Avi) |
| R7 | Because the tool logs who used which draft, agents may be judged individually through usage data used as performance monitoring | AUP §6: team-level reporting, no routine reading; dashboard DPIA test in module 6 (Michal, HR) | Low (Michal) |
| R8 | Because WhatsApp messages and photos sit on four shared phones today, routing them into Deskly moves them to a system with access control — and to the AI path | Routing project with retention rule; phones wiped after migration (Avi, Samir) | Low after migration |

8. *Consultation.* Samir and two agents (Olga for Russian, an Arabic-speaking colleague) on 24 November; Avi on settings; counsel's written advice pending.
9. *Decision and triggers.* Go with conditions for stage 1 (shadow) once: opt-out confirmed, Autopilot locked, counsel's answer on transfers and notice, test set pseudonymised. Reopen if: the model provider changes; WhatsApp routing goes live; anyone proposes auto-send; scope extends to new data (claims, quotes); six months pass.

**Notice gaps (to counsel).** (1) AI processing of messages is not mentioned; (2) recipients abroad are described only as "some of which store information on servers outside Israel" — enough?; (3) retention is "as long as we need it" — Deskly's 24 months and "forever" tickets need a rule; (4) privacy@ goes to IT — who is the contact? Proposed sentence: "We use service providers, including AI tools, to help our team read and answer your messages; a member of our team reviews and sends every reply. These providers may process your messages in the United States and the European Union."

</details>

## References

- EBN Law, [PPA draft guidance on AI systems](https://www.ebnlaw.co.il/media-center/draft-guidance-from-the-israeli-privacy-protection-authority/) and Pearl Cohen, [Israel: New Draft Guidelines on AI](https://www.pearlcohen.com/israel-new-draft-guidelines-on-the-application-of-privacy-law-to-ai/) — impact assessments and AI transparency (draft, April 2025).
- Chambers Practice Guides, [Data Protection & Privacy 2026: Israel](https://practiceguides.chambers.com/practice-guides/data-protection-privacy-2026/israel) — notice of collection after Amendment 13, security levels, risk assessments.
- Barnea Jaffa Lande, [Position statement on the obligation to appoint a DPO](https://barlaw.co.il/practice_areas/regulation/privacy-law/client_updates/position-statement-on-the-obligation-to-appoint-a-dpo-not-a-change-in-the-law-but-a-change-in-the-rules-of-the-game/) (22 July 2026).
- GDPR [Article 35](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679); [Regulation (EU) 2026/1744](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202601744), Article 1(13) — the fundamental-rights impact assessment may cross-refer to a DPIA.
- Templates: [AI inventory](../../templates/ai-inventory.md), [DPIA for AI](../../templates/dpia-for-ai.md). Lab: [module 4 lab README](../../labs/module-04/README.md).
- Previous: [04.3 · Vendor and tool review](lesson-03.md). Next: [04.5 · Risk register from zero](lesson-05.md). Later: module 5 builds the pilot's test set and human review (05.2, 05.5).
