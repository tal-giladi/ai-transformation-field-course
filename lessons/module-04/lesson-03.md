---
id: "04.3"
module: 4
minutes: 20
practice_minutes: 90
prerequisites: ["04.2"]
objectives:
  - "Review an AI vendor's terms against a ten-section questionnaire: data use for training, retention, location, sub-processors, certifications, outputs and liability, model changes and exit."
  - "Find the clauses that change a verdict in three real-shaped vendor documents and turn each into a contract ask, a setting or a condition."
  - "Write a data boundary for each approved tool: what data enters, where it travels, who sees it, how long it stays."
  - "Give each vendor a verdict (approve, approve with conditions, not yet) that names who must do what before data flows."
volatility: implementation
sources:
  - title: "Chambers Practice Guides — Data Protection & Privacy 2026: Israel (transfers abroad, onward transfers, security levels)"
    url: https://practiceguides.chambers.com/practice-guides/data-protection-privacy-2026/israel
  - title: "Legal 500 (2012) — Privacy protection in outsourcing services: the Israeli regulator's outsourcing guidelines"
    url: https://www.legal500.com/intelligence/israel/employment-and-hr/privacy-protection-in-outsourcing-services
  - title: "Amit, Pollak, Matalon & Co. — PPA manual for implementing Regulation 15 of the Data Security Regulations (September 2023), in Hebrew"
    url: https://ayr.co.il/מדריך-פעולה-ליישום-תקנה-15-לתקנות-אבטחת
  - title: "ISO — ISO/IEC 42001:2023 Artificial intelligence management system (Edition 1, published)"
    url: https://www.iso.org/standard/42001
  - title: "Bank of Israel — representative exchange rates (2 November 2026)"
    url: https://www.boi.org.il/en/economic-roles/financial-markets/exchange-rates/
last_verified: "2026-11-02"
---

# 04.3 · Vendor and tool review

Every AI tool you approve is a vendor you trust with the company's data, and the trust lives in a few clauses most people never read. In this lesson you build a vendor AI questionnaire, read three real-shaped vendor documents against it — the helpdesk's AI add-on terms, a translation tool's data processing addendum and a chatbot vendor's sales deck — and turn every clause that matters into a contract ask, an admin setting or a condition. At the end you have a verdict for each vendor and a one-page data boundary for each tool you approve.

## The situation

It is Tuesday 17 November 2026. The approved list (04.2) depends on three vendor decisions. Samir received Deskly's AI Assist terms with a quote on 14 October; Deskly is the helpdesk the module 5 pilot will most likely run in, and its renewal is on 31 January 2027. Olga's LinguaFlow Business quote has been waiting since 2 October. And Yoav wants to sign ChatNest's chatbot before its 15% discount expires on 30 November; Eitan, the account executive, meets you on 19 November (04.8).

The pilot context matters for every verdict: the module 5 pilot drafts replies for **all written support contact** — email, web form, and WhatsApp once it is routed into the helpdesk — and a person sends every reply. So whichever tool runs it will see the names, phones, addresses, order details and damage photos of most of Harbor & Pine's customers.

IBM's governance course names vendor risk (indemnity, audit rights) without giving a questionnaire, a data processing review or an exit plan. This lesson is that missing piece.

## What to do

### Step 1 — Use one questionnaire for every AI vendor

A questionnaire you reuse turns a vendor review from an essay into a comparison. Ten sections, each with what a good answer looks like and the red flag (full version in the [vendor AI questionnaire](../../templates/vendor-ai-questionnaire.md)):

| # | Section | Good answer | Red flag |
|---|---|---|---|
| 1 | **What it does and what is on by default** | Features listed; anything that acts (sends, changes records) is off and lockable | Actions any admin can switch on |
| 2 | **Data used for training** | Not used to train or improve models, or opt-in only | "De-identified" training by default, opt-out by letter |
| 3 | **Retention and deletion** | Short, configurable, deletion on exit with a date | Copies in "analytics" kept for years |
| 4 | **Location and transfers** | Named countries; a contract that covers transfers | "Our providers", unnamed regions |
| 5 | **Sub-processors** | Named list, advance notice, right to object and leave with a refund | Changes by web-page update; objecting means losing the service |
| 6 | **Humans who see our data** | Named, limited, for named reasons | Outsourced review of "flagged" content, location not in the DPA |
| 7 | **Security and certifications** | Current report or certificate with its scope and period | A logo on a slide |
| 8 | **Outputs and liability** | Vendor stands behind the service; liability proportionate | Customer "solely responsible"; cap at a few months' fees |
| 9 | **Model and feature changes** | Advance notice of model changes; ability to pin or test | Silent changes |
| 10 | **Exit and continuity** | Export format, deletion certificate, change-of-control clause, term you can leave | Long minimum term, no export, no answer on acquisition |

Section 9 is the one most questionnaires forget. When the vendor swaps the underlying model, the pilot you evaluated is no longer the system you run; module 5 (05.7) re-runs the evaluation, but only if the contract makes the vendor tell you.

For certifications, ask for the document, not the logo. A SOC 2 Type II report covers a period and a set of systems; an ISO/IEC 27001 or ISO/IEC 42001 certificate covers a scope and sites. ISO/IEC 42001:2023 is the certifiable AI management-system standard (ISO's page lists it as published, edition 1); a vendor holding it tells you it runs an AI management system, not that this feature is safe for your data.

### Step 2 — Israel first: what the law asks of you, the customer

The duties sit with Harbor & Pine as the owner of the database, not with the vendor:

- **Before engaging an outside provider** that gets access to a database, the Privacy Protection (Data Security) Regulations, 5777-2017, require the owner to look at the security risks of the engagement and to put security terms into the agreement (Regulation 15; the Privacy Protection Authority published a manual for implementing it in September 2023). The regulator's older outsourcing guidelines already expected the contract to fix the permitted purposes, forbid use beyond the service, allow audits and require deletion at the end (Legal 500's summary).
- **Data leaving Israel** falls under the Privacy Protection (Transfer of Data to Databases Abroad) Regulations, 5761-2001. Chambers' 2026 guide lists the routes: destinations whose protection is adequate (including countries the European Commission recognises as adequate and parties to Convention 108), the data subject's informed consent, or contractual safeguards; onward transfers need the controller's prior written approval.
- **Notice to customers.** Deskly's terms put this on you explicitly: the customer is responsible for notices and consents for processing end customers' data with AI Assist (§7.2). Harbor & Pine's privacy notice dates from January 2022 and says nothing about AI (04.4 handles the notice).

You don't decide which transfer route applies or whether a clause satisfies Regulation 15. You read the documents, list the facts counsel needs, and make sure no data flows before counsel answers.

### Step 3 — Read the Deskly AI Assist terms clause by clause

Open `vendors/deskly-ai-addon-terms.md`. Read it with the questionnaire beside you and note every clause that changes the verdict:

| Clause | What it says | Why it matters | Turn it into |
|---|---|---|---|
| §1.1(e), §1.2 | Autopilot sends replies to "high confidence" tickets; off by default; **any workspace Administrator** may switch it on | Breaks "a person sends every reply" with one click | Setting: Autopilot off and admin roles limited to two named people; contract: Autopilot disabled at account level |
| §2.1 | US$29 per agent seat per month for **all** agent seats, billed annually | 15 seats = US$5,220 a year, ≈ ₪19,300 at the finance planning rate of ₪3.70 per US$ (≈ ₪16,400 at the Bank of Israel rate of ₪3.136 on 2 November 2026) | Ask to license only the seats that use it |
| §3.2 | Deskly may use content and outputs, de-identified, to **train and evaluate models**; opt-out by written notice, effective **30 days** after receipt | Customer messages become training data by default | Send the opt-out now; no customer data until 30 days after Deskly confirms in writing |
| §3.4 | Prompts and outputs kept 30 days, then in an **analytics store for 24 months**; on termination deleted within 90 days, backups within a further 180 | Two years of customer messages in a store you never use | Ask to exclude AI content from analytics or cut to 90 days; record it in the DPIA |
| §4.1–4.3 | Customer "solely responsible" for reviewing outputs and for anything Autopilot sends; no warranty; liability capped at **three months'** AI fees (≈ US$1,300) | The vendor carries almost none of the risk | Accept for a pilot with a person sending; renegotiate before any scale-up |
| §5.1 | Content stored in the workspace region — **Harbor & Pine: US**; AI processing in the US and the EU | A transfer abroad already exists for tickets; AI adds new recipients | Counsel: transfer route for the AI sub-processors |
| §6.1 | Sub-processors added by updating Annex 1 on the website; objection within 15 days; sole remedy: **stop using** AI Assist | You can be moved to a new processor without a real choice | Subscribe to notifications; ask for 30 days' notice and a refund right |
| Annex 1 | Foundation-model provider "named in the trust portal, login required"; **QualityOps Services, Philippines: human review of flagged outputs** | Unnamed model; people abroad read some customer messages | Ask for the model provider's name and what gets flagged; counsel on the transfer |
| §8.1 | Co-terminous with the MSA, renewal **31 January 2027**; removable at renewal on 30 days' notice | Your leverage date is before 1 January 2027 | Negotiate the asks as part of the renewal |

Missing from the document (questionnaire sections 7, 9, 10): no security report or certification for the add-on, no notice of model changes, nothing on exporting AI data at exit. Ask.

**Verdict: approve with conditions, for the pilot only.** Conditions before any customer data: (1) the §3.2 opt-out sent and confirmed, and 30 days passed; (2) Autopilot off, admin roles limited, the setting checked monthly; (3) the model provider named and the Philippines review explained; (4) counsel's answer on the transfer routes; (5) the DPIA (04.4) signed. Before production or renewal: retention, sub-processor terms, model-change notice and liability renegotiated.

### Step 4 — Read the LinguaFlow DPA the same way

`vendors/linguaflow-translation-dpa.md` is the opposite case: most answers are good, and the work is to confirm them.

- **Scope (§1).** The DPA covers **only** LinguaFlow Business. The free extension on nine machines runs under consumer terms, with LinguaFlow as controller, texts kept up to 18 months and used for training (§1.2, §4.2). The review covers the plan you would buy, not the plan people use today.
- **Training and retention (§4.1):** not used for training; zero retention apart from 24-hour encrypted logs.
- **Location (§5):** EU (Ireland, Netherlands); UK support staff see account metadata, not texts.
- **Sub-processors (§6):** two, named; 30 days' notice; objection, then termination with a pro-rata refund.
- **Security (§7):** ISO/IEC 27001 certified; annual penetration test, summary on request; breach notice within 48 hours.
- **Exit (§8):** account data deleted within 30 days.
- **Admin (§9):** single sign-on with Google Workspace; the admin can force the extension to the Business account and block personal accounts on managed browsers.

**Verdict: approve.** Conditions are confirmations: the ISO/IEC 27001 certificate with its scope and validity date, the penetration-test summary, and the forced sign-in switched on the day the licences start. The single most useful clause is §9: it is what turns "please stop using the free extension" into a setting.

### Step 5 — Treat the ChatNest deck as an answer to nothing yet

`vendors/chatnest-sales-deck.md` is a sales document, not terms. Read it for what it reveals and what it leaves out:

- **Data:** US hosting; EU hosting only on the Enterprise plan (slide 7). No DPA, no sub-processor list, nothing on training, retention or deletion.
- **Security:** "SOC 2 Type II" as a bullet. Ask for the report and its period.
- **Term:** 12-month minimum; implementation ₪85,000; order-tracking integration "quoted separately after technical review" (slide 6).
- **Use:** the product is a customer-facing bot that answers "without an agent" — a restricted use on your list (04.2). It needs the governance committee, a risk review and a pilot before anyone signs.
- **Already a finding:** the demo was built on a catalogue file "received by email from Harbor & Pine marketing, 28 September 2026" (footnote 4) — company data sent to a vendor with no agreement in place. Product data is low class, so the harm is small; the habit is the finding.

**Verdict: not yet.** Send the questionnaire. No company data to ChatNest until there is a DPA, and no signature before the claims are checked (04.8) and a proof of concept is run on Harbor & Pine's own data.

### Step 6 — Write the data boundary for each approved tool

The verdict says *whether*; the data boundary says *what happens to the data*, on one page per tool, in words a manager and the DPO can both read. IBM's consulting course lists the boundary as one of the six parts of governance (04.7 links it there).

**Data boundary — Deskly AI Assist (pilot), draft 18 November 2026**

| Question | Answer |
|---|---|
| What data enters | Ticket text, attachments' text, customer name, email, phone, order number; WhatsApp messages once routed into Deskly; saved replies and help-centre articles |
| What must not enter | Payment details, ID numbers, health information (agents remove; Deskly's redaction setting to be checked) |
| Where it travels | Deskly workspace (US) → foundation-model provider (US, name pending) → LangBridge (Ireland) for translation → CloudCompute (US, Ireland) hosting → QualityOps (Philippines) for flagged outputs |
| Who sees inputs and outputs | Our agents and two admins; Deskly support on request; QualityOps reviewers for flagged items |
| Vendor training | Off after the §3.2 opt-out takes effect (date to record) |
| Retention | 30 days operational; 24 months analytics unless renegotiated; tickets themselves "forever — no deletion rule set" (IT's note) — a separate decision |
| Who can change it | Deskly admins (two named); sub-processor changes by Deskly with 15 days to object |
| Exit | Content deleted within 90 days of termination, backups within a further 180 |
| Our controls | Autopilot off and checked monthly; a person sends every reply; opt-out letter on file; DPIA |

## Watch out

- **Reviewing the plan you won't use.** The LinguaFlow DPA covers Business; the risk today is the free extension. Review the contract that will actually govern the data.
- **"De-identified" as a reassurance.** De-identified training is still training on your customers' messages, by the vendor's method, which you cannot check. Opt out.
- **Missing the clause that acts.** One admin switch (§1.2) turns drafting into automatic sending. Look for anything that sends, changes or deletes.
- **Treating certifications as answers.** Ask for scope, period and sites. A certificate is evidence about a management system, not about your use.
- **Letting renewal pass.** Deskly's asks have leverage before the 31 January 2027 renewal and almost none after.
- **Deciding the legal routes yourself.** Transfer conditions and Regulation 15 adequacy are counsel's call; your job is the facts and "no data until answered".
- **Vendor pressure setting the timeline.** A discount deadline is the vendor's quarter, not your risk review.

## Your turn

### Inputs

- Data room (module download): `vendors/deskly-ai-addon-terms.md`, `vendors/linguaflow-translation-dpa.md`, `vendors/chatnest-sales-deck.md`, `policies/data-retention-note.md`, `policies/privacy-notice.md`, `it/saas-list.csv` ([INDEX](../../labs/common/harbor-and-pine/INDEX.md)).
- Persona (optional): [Avi Mizrahi, IT manager](../../labs/common/harbor-and-pine/personas/avi-it-manager.md) — ask him what the Deskly admin console lets you lock; [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [vendor AI questionnaire](../../templates/vendor-ai-questionnaire.md) (spreadsheet `labs/module-04/vendor-ai-questionnaire.csv`), [data boundary](../../templates/data-boundary.md).

### Steps

1. Answer the ten questionnaire sections for Deskly AI Assist, LinguaFlow Business and ChatNest from their documents only. Mark each answer "stated", "not stated" or "contradicts our policy".
2. For Deskly, list every clause that changes the verdict and turn each into a setting, a contract ask or a condition, with an owner and a date.
3. Write the questions for counsel (transfer routes, Regulation 15, the notice duty) as one email of at most ten lines.
4. Give each vendor a verdict: approve, approve with conditions, or not yet, with what must happen before any data flows.
5. Write the data boundary for Deskly AI Assist and for LinguaFlow Business.
6. Price Deskly AI Assist for a year in ₪ and say which exchange rate you used and why.

### Time

90 minutes.

### Done when

- [ ] All three vendors are answered against the same ten sections, with gaps marked "not stated".
- [ ] You found Deskly's training default, the 24-month analytics retention, the Autopilot switch, the US region, the sub-processor remedy, the Philippines review and the liability cap.
- [ ] Each Deskly finding has a setting, ask or condition with an owner and a date before 31 December 2026.
- [ ] LinguaFlow is reviewed on the Business plan, with the free extension named as today's risk.
- [ ] ChatNest gets "not yet", with no company data until a DPA exists.
- [ ] Counsel receives facts and questions, not your legal conclusions.
- [ ] Each data boundary answers what enters, where it goes, who sees it, training, retention and exit.

<details><summary>Reference answer</summary>

**Questionnaire summary (excerpt).**

| Section | Deskly AI Assist | LinguaFlow Business | ChatNest |
|---|---|---|---|
| 1 Defaults and actions | Autopilot off; any admin can enable (§1.2) — contradicts policy | Translation only; no actions | Bot answers customers without an agent — restricted use |
| 2 Training | De-identified training unless opted out (§3.2) — contradicts | None (§4.1) | Not stated |
| 3 Retention | 30 days + 24 months analytics (§3.4) — contradicts | Zero, 24 h logs | Not stated |
| 4 Location | US workspace; AI in US and EU (§5.1) | EU; UK metadata only | US; EU on Enterprise |
| 5 Sub-processors | Annex 1; web update; objection = stop using (§6.1) | 2 named; 30 days; refund right | Not stated |
| 6 Humans | QualityOps, Philippines, flagged outputs | UK support, metadata | Not stated |
| 7 Security | Not stated for the add-on | ISO/IEC 27001; pen test; 48 h breach notice | "SOC 2 Type II" bullet |
| 8 Liability | Customer solely responsible; 3 months' fees (§4) | Not stated | Not stated |
| 9 Model changes | Not stated | Not stated | Not stated |
| 10 Exit | Delete 90 + 180 days; renewal 31 Jan 2027 | Delete in 30 days; glossary export | 12-month minimum; export not stated |

**Deskly actions.** Samir sends the §3.2 opt-out to privacy@deskly.example on 18 November, asks for written confirmation (earliest effective date 18 December); Avi turns Autopilot off at every view, limits Administrator to himself and Samir, and adds a monthly check (from 1 December); you send Deskly the questions on the model provider, QualityOps, security report, model-change notice and analytics retention (19 November); Ronit takes the renegotiation asks (seats, retention, 30-day sub-processor notice with refund, liability) into the renewal talks before 31 December.

**Email to counsel (through Ronit).** "We plan a pilot that drafts replies to customer messages inside Deskly (US) using AI sub-processors in the US, Ireland and the Philippines; a person sends every reply. Separately we will buy LinguaFlow Business (EU). Questions: (1) Which route under the transfer regulations covers each destination, and do we need anything in writing from Deskly or LinguaFlow? (2) Do Deskly's add-on terms and the MSA's DPA meet Regulation 15, or what must we add? (3) Must the privacy notice change before the pilot, and what must it say? (4) Does the human review in the Philippines change any answer? Documents attached. We will not put customer data into either tool until you answer."

**Verdicts.** Deskly: approve with conditions, pilot only (Step 3). LinguaFlow Business: approve, confirm certificate scope and switch on forced sign-in. ChatNest: not yet; questionnaire sent; no data until a DPA; claims to 04.8.

**Cost.** US$29 × 15 seats × 12 = US$5,220 ≈ ₪19,300 a year at ₪3.70/US$, the finance team's planning rate (October 2026), because Ronit's business-case template uses it; at the Bank of Israel representative rate of ₪3.136 on 2 November 2026 it would be ≈ ₪16,400. Say which one you used.

**Data boundary, LinguaFlow Business.** Enters: text of customer and supplier messages and draft replies selected for translation. Travels: LinguaFlow (Ireland, Netherlands) via EuroCloud hosting; MailRelay for account emails. Sees it: nobody at LinguaFlow (zero retention); UK support sees account metadata. Training: none. Retention: 24-hour encrypted logs. Changes: 30 days' notice, objection and refund. Exit: 30 days. Our controls: forced Business sign-in, personal accounts blocked, free extension removed.

</details>

## References

- Chambers Practice Guides, [Data Protection & Privacy 2026: Israel](https://practiceguides.chambers.com/practice-guides/data-protection-privacy-2026/israel) — transfers abroad and onward transfers (law-firm guide; the Hebrew regulations are authoritative).
- Legal 500, [Privacy protection in outsourcing services](https://www.legal500.com/intelligence/israel/employment-and-hr/privacy-protection-in-outsourcing-services) (2012) — the regulator's outsourcing guidelines; Amit, Pollak, Matalon & Co., [PPA manual on Regulation 15](https://ayr.co.il/מדריך-פעולה-ליישום-תקנה-15-לתקנות-אבטחת) (September 2023, Hebrew). Route the reading of Regulation 15 to counsel.
- ISO, [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) — the AI management-system standard.
- Bank of Israel, [representative exchange rates](https://www.boi.org.il/en/economic-roles/financial-markets/exchange-rates/) — ₪3.136 per US$ on 2 November 2026.
- Templates: [vendor AI questionnaire](../../templates/vendor-ai-questionnaire.md), [data boundary](../../templates/data-boundary.md).
- Earlier: [01.5 · Access and the first-day data-room read](../module-01/lesson-05.md) (transfer regulations, outside parties). Next: [04.4 · AI inventory, risk tiering and the DPIA](lesson-04.md). Later: [04.8 · Vendor and claim due diligence](lesson-08.md) (ChatNest's claims).
