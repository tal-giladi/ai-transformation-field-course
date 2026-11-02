---
id: "01.7"
module: 1
minutes: 18
practice_minutes: 80
prerequisites: ["01.6"]
objectives:
  - "Write a counting rule for what counts as AI, and apply it to systems sold as AI, including rules engines that are not."
  - "Find AI that arrived inside SaaS feature updates and record the decisions it already shapes."
  - "Build a first AI inventory with fields, an owner for every row and an action for every row that needs one."
  - "Keep the capability inventory, the maturity view and the legal register as three separate documents linked by ID."
volatility: implementation
sources:
  - title: "EU AI Act, Recital 12 (definition of an AI system; capability to infer; exclusion of rules defined solely by natural persons)"
    url: https://artificialintelligenceact.eu/recital/12/
  - title: "European Commission — Guidelines on the definition of an AI system (6 Feb 2025)"
    url: https://digital-strategy.ec.europa.eu/en/library/commission-publishes-guidelines-ai-system-definition-facilitate-first-ai-acts-rules-application
  - title: "NIST AI RMF 1.0 Core — GOVERN 1.6 (inventory of AI systems) and GOVERN 6 (third-party AI)"
    url: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
  - title: "Google Workspace blog — Gemini included in Business and Enterprise plans (16 Jan 2025)"
    url: https://workspace.google.com/blog/product-announcements/empowering-businesses-with-AI
  - title: "Employment (Equal Opportunities) Law, 5748-1988 — unofficial English translation (ICJ)"
    url: https://www.icj.org/wp-content/uploads/2013/05/Israel-Employment-Equal-Opportunities-Law-5748-1988-eng.pdf
last_verified: "2026-11-02"
---

# 01.7 · The AI inventory from zero

Before anyone can govern AI, someone has to list it, and the list is never where people expect. Some AI was bought; more arrived silently inside software the company already pays for; some is sold as AI and isn't. In this lesson you write a counting rule, test the systems that claim to be AI, find the AI that came with feature updates, and record which decisions AI already shapes. At the end you have Harbor & Pine's first AI inventory, with an owner and an action on every row, and you know why it must stay separate from the legal register.

## The situation

It is the second week. The shadow-AI census (01.6) found the tools people chose themselves. Now you need the rest: the AI inside the systems the company runs, so that the interim rule, the approved-tools list and the risk work in module 4 have something real to stand on.

You have IT's software list (`it/saas-list.csv`, 20 applications, with columns for AI features and whether they are enabled), two configuration exports Avi copied "for the AI list" (`it/smartstock-reorder-config.md`), the HR vendor's release notes from March (`it/peoplewise-release-notes-2026-03.md`), and one odd line in the proxy log: two calls from HR to `match-ai.peoplewise.io`.

IBM's advisor course says to write the counting rule before you count, and to keep the capability inventory, the maturity assessment and the regulatory register as three separate instruments. This lesson does both with real files.

## What to do

### Step 1 — Write the counting rule first

If you don't decide what counts, the list will be either everything with "smart" in its name or only the chatbots. Write one paragraph and get the sponsor to agree to it:

> **Counting rule.** A system or feature counts as AI if it produces outputs — content, predictions,
> scores, recommendations or decisions — by inferring them from data (a learned or generative model),
> rather than only applying rules that people wrote. Count one row per tool **per use**: the same tool
> used for two purposes with different data is two rows. Record systems you checked and excluded,
> with the reason, so nobody has to check them again.

This matches where regulators draw the line. The EU AI Act names the "capability to infer" as the key characteristic of an AI system and says the definition should not cover "systems that are based on the rules defined solely by natural persons" (Recital 12). The European Commission's guidelines on the definition (6 February 2025) add that it must not be applied mechanically: each system is assessed on its characteristics. Harbor & Pine is not on the EU market, so the Act is not your legal test here — you borrow the line because it is a good one and because your clients' clients may one day ask.

### Step 2 — Test the systems sold as AI

Two Harbor & Pine add-ons are listed with "AI enabled: Yes". Open the configuration before you believe the label.

**SmartStock AI** ("Artificial intelligence that knows what you'll sell before you do"). Its settings: a reorder trigger when stock plus orders falls below *Min*; *Min* = average weekly sales over 13 weeks × (lead time + safety weeks); *Max* = Min + weekly sales × order cycle; a seasonality factor set **by hand** by Purchasing each January (Nov–Jan × 1.4, Aug–Sep × 1.2); "Demand sensing: Not licensed". Every output follows from formulas and numbers people chose. **Not AI** under the rule — record it as excluded, with the reason.

**AutoRecon** ("intelligent auto-match"): four matching rules applied in order (exact amount + date + reference; amount ± ₪1 within 3 days + name; several candidates → accountant; else unmatched). **Not AI.**

Excluding them does not mean ignoring them. SmartStock's suggestions are approved "about 80% as they are", so it shapes purchasing decisions; it belongs in the company's list of automated decisions and in any review of the purchasing process. It simply doesn't need AI governance — no model drift to monitor, no training data to question. That distinction saves your governance effort for the systems that need it.

Borderline cases get a row with "to verify" instead of a guess: RouteMaster (route optimisation; the SaaS list notes "Algorithmic optimisation, not ML (per vendor)") — conventional optimisation, excluded until the vendor says otherwise; NetGuard's URL categorisation — ask the MSP whether it is a rules list or a model; Bitdefender's "ML-based threat detection" — AI by the rule, low business impact, owned by the MSP.

### Step 3 — Find the AI that arrived with feature updates

Most AI in a mid-size company was never bought as AI. It arrived in a release note. Three ways to find it:

1. **Read the SaaS list's own columns, then distrust them.** IT recorded AI features for 13 of 20 applications, and wrote "Unknown" for Google Workspace (Gemini), Zoom (AI Companion) and Monday.com (AI assistant). Google announced on 16 January 2025 that Gemini's AI features were included in Workspace Business and Enterprise plans without a separate add-on; Harbor & Pine is on Business Standard and its admin console "not reviewed since 2024". Whether Gemini is on is a ten-minute check in the console — put Avi's name and a date on it.
2. **Read the release notes of every system that holds personal data.** PeopleWise's notes of 10 March 2026 announce "AI Candidate Match": every application and CV is scored 0–100 against the job, candidates are sorted by score, a "smart filter" hides anyone under 40, it works on Hebrew, Arabic, English and Russian CVs, and it is **enabled by default** for all existing and new jobs. CV text is sent to "our AI service", with a new sub-processor in the EU and the US. The SaaS list says PeopleWise has no AI features and AI is "No". The proxy's two calls from HR to `match-ai.peoplewise.io` say it is running.
3. **Ask the owner how the work is done now.** Not "do you use AI?" — Dana, the HR manager, would honestly say no — but "how do candidates get screened today? Walk me through the last round." This is how you learn that about fifteen seasonal warehouse workers were hired this autumn through a pipeline that hid some applicants, and that nobody in the company chose that.

### Step 4 — Record the decisions AI already shapes

For each AI row, write one sentence: **what decision or output does it shape, for whom, and who checks it?** That sentence is what turns a software list into a governance tool.

| AI in use | Decision or output it shapes | Who is affected | Human check today |
|---|---|---|---|
| PeopleWise AI Candidate Match | Which applicants a recruiter sees and calls | Job applicants | None designed; recruiter sees the sorted list |
| StoreHub AI product descriptions | Product text published on the web store | Customers | Shir (content manager) reviews new products |
| ChatGPT / LinguaFlow in Customer Service | Wording of replies sent to customers | Customers | The agent — six unedited drafts were sent (01.6) |
| MailPost AI subject lines and send times | Which marketing emails customers get, when | Customers | Unknown |
| Bitdefender ML detection | Which files and sites are blocked | Employees | MSP |

The first row is the urgent one. Israel's Employment (Equal Opportunities) Law, 5748-1988 (חוק שוויון ההזדמנויות בעבודה, התשמ"ח-1988) prohibits employers from discriminating among people seeking employment, including in acceptance for employment, on grounds that include age, religion, nationality and country of origin (section 2). A score that hides applicants, trained on other companies' hiring data and applied to CVs in four languages, is exactly the kind of system whose effect nobody at Harbor & Pine has looked at. Whether anything went wrong is a question for the company's labour lawyer, not for you. Your job is to make sure the question is asked this week, that the autumn applicant list and scores are exported before anyone changes a setting, and that the decision to switch the feature off (Dana can, under *Settings → Recruiting → AI features*) is taken by the right people.

### Step 5 — Build the inventory: fields and owners

Use the [AI inventory template](../../templates/ai-inventory.md) (spreadsheet: `labs/module-01/ai-inventory.csv` in the module download). Fields that earn their place:

- **ID**, **tool / feature**, **vendor**
- **AI under the counting rule?** yes / no / to verify — **and why**
- **How it arrived:** bought as AI · feature update · free tool · browser extension · personal subscription
- **Status:** on / off / available, not enabled / unknown
- **Business owner** (one named person) and **technical owner**
- **Departments and users**
- **Use:** what it is used for, in one line
- **Data in:** data classes (customer personal data, employee data, candidates, financial, product, none)
- **Decision or output it shapes**, **who is affected**, **human check**
- **Terms / plan**, **data location**
- **First risk view:** high / medium / low, one line why (module 4 replaces this with proper tiering)
- **Action**, **action owner**, **due**
- **Last checked**, **source** (the file or person that told you)

Every row needs a named business owner. For bought systems, the SaaS list's `business_owner` column gives it (Dana for PeopleWise, Noa for StoreHub). For shadow tools from the census, the owner is the head of the department that uses it — not IT. Avi runs the infrastructure; he does not own Customer Service's decision to draft replies with ChatGPT.

### Step 6 — Keep three instruments apart

You will be tempted to add columns until the inventory is also a maturity score and a legal register. Don't. Three documents answer three different questions for three different readers:

| Instrument | Question | Reader | Granularity |
|---|---|---|---|
| **AI inventory** (this lesson) | What AI exists, who owns it, what data and decisions it touches? | Programme, IT, owners | One row per tool per use, including excluded and unknown |
| **Maturity view** (module 2's readiness assessment) | How able is the organization to use AI well? | Sponsor, steering | A few dimensions for the whole organization |
| **Legal register** (module 4) | Which legal duties attach to which system, and are they met? | Counsel, DPO, management | Only systems in scope of a duty, with the duty and evidence |

Merge them and each gets worse: the legal register fills with "unknown" rows counsel cannot act on, and the inventory starts hiding borderline systems because listing them "creates a legal problem". Link them by the inventory ID instead. The US NIST AI Risk Management Framework makes the same point from the governance side: "mechanisms are in place to inventory AI systems" (GOVERN 1.6) is a separate outcome from managing third-party AI risk (GOVERN 6).

### Step 7 — Turn the inventory into three actions

An inventory that changes nothing is a spreadsheet. End with the three actions that matter most this month, each with an owner and a date. At Harbor & Pine the first writes itself: PeopleWise.

## Watch out

- **Trusting the "AI" label.** Vendors call rules engines AI because it sells. Open the configuration.
- **Trusting the "no AI" column.** IT's list said PeopleWise had no AI. Release notes, proxy logs and "how do you do it today?" are the checks.
- **Leaving out what you excluded.** If SmartStock isn't on the list with a reason, the next person spends a day re-checking it.
- **IT as owner of everything.** IT owns infrastructure; the department that uses a tool owns the decision to use it and the data it sends.
- **Switching off before you export.** If a feature has been deciding things, capture what it decided before you change the setting.
- **Deciding the legal question yourself.** "That's probably discrimination" and "that's fine, it's only a suggestion" are both counsel's call.
- **One inventory to rule them all.** Keep maturity and legal duties in their own documents, linked by ID.

## Your turn

### Inputs

- Data room (module download): `it/saas-list.csv`, `it/smartstock-reorder-config.md`, `it/peoplewise-release-notes-2026-03.md`, `it/proxy-log.csv` (one host), `vendors/deskly-ai-addon-terms.md` (§1), your census from 01.6 ([INDEX](../../labs/common/harbor-and-pine/INDEX.md)).
- Persona: [Dana Katz, HR manager](../../labs/common/harbor-and-pine/personas/dana-hr.md), or the [pre-run transcript](../../labs/module-01/dana-hr-interview-transcript.md); [coach prompt](../../labs/common/coach-prompt.md).
- Template: [AI inventory](../../templates/ai-inventory.md); spreadsheet `labs/module-01/ai-inventory.csv`.

### Steps

1. Write the counting rule and test SmartStock AI and AutoRecon against it.
2. Go through all 20 rows of the SaaS list: AI yes / no / to verify, with the reason.
3. Read the PeopleWise release notes and compare them with the SaaS list and the proxy log.
4. Interview Dana for 15 minutes: find out how candidates are screened today, and what she wants done. (Transcript path: note what the interviewer did not ask.)
5. Add the shadow tools from your census as rows (one per tool per use).
6. Fill the inventory: at least 15 rows including excluded and to-verify ones, each with an owner.
7. Write the decisions-shaped table (Step 4) for every AI row in use.
8. Write the three most important actions, each with owner and date, and one paragraph explaining to Michal why the legal register will be a separate document.

### Time

80 minutes.

### Done when

- [ ] The counting rule is one paragraph and says how excluded systems are recorded.
- [ ] SmartStock AI and AutoRecon are excluded with a reason taken from their configuration.
- [ ] PeopleWise is recorded as AI, on by default since March 2026, with the contradiction to the SaaS list noted.
- [ ] Every row has a named business owner; no shadow tool is owned by IT.
- [ ] Every AI row in use has the decision it shapes, who is affected and the human check.
- [ ] Three actions with owners and dates; the PeopleWise action exports the data before switching anything off and routes the legal question to counsel.
- [ ] Inventory, maturity view and legal register are described as separate documents.

<details><summary>Reference answer</summary>

**Inventory (first version, 10 November 2026).**

| ID | Tool / feature | AI? (why) | Arrived | Status | Owner | Data in | Shapes | Risk | Action |
|---|---|---|---|---|---|---|---|---|---|
| AI-01 | PeopleWise AI Candidate Match | Yes — vendor model scores CVs | Feature update, Mar 2026 | On by default (SaaS list says "No") | Dana Katz | Candidates' CVs | Which applicants are seen | High | Export autumn applicants + scores; labour lawyer; decide off/on |
| AI-02 | ChatGPT (consumer) — support replies | Yes | Free / personal | In use | Samir Haddad | Customer emails incl. personal data | Reply wording | High | Interim rule (01.6); approved tool |
| AI-03 | LinguaFlow free extension — translation | Yes | Extension, 9 machines | In use | Samir Haddad (CS); Eyal Navon, Tamar Shalev, Rebecca Morris for their teams | Screen and clipboard content | Reply and email wording | High | Interim rule; decide on Business plan (request of 2 Oct) |
| AI-04 | ChatGPT Plus / CopyGenie / Midjourney — marketing | Yes | Personal subscriptions | In use | Noa Levi | Product info, reviews | Published copy, images | Medium | Terms check; reviews without names |
| AI-05 | ChatGPT Plus — purchasing | Yes | Personal subscription | In use | Eyal Navon | Supplier emails | Supplier correspondence | Medium | Covered by approved-tool decision |
| AI-06 | Claude — finance | Yes | Personal, one month paid | In use | Ronit Avraham | Unknown, large pastes | Unknown | Medium | Conversation with Ronit |
| AI-07 | StoreHub AI product descriptions | Yes | Feature, enabled by marketing | On | Noa Levi | Product data | Web-store text | Low–medium | Keep Shir's review; record it |
| AI-08 | MailPost AI subject lines, send-time optimisation | Yes | Feature | On | Noa Levi | Customer emails, purchase history | Marketing emails | Medium | Check terms and data use |
| AI-09 | Canva Magic Write / AI images | Yes | Feature | On | Noa Levi | Marketing content | Images, text | Low | Record |
| AI-10 | Grammarly | Yes | Extension, 6 machines | In use | Each department head | Any text on screen | Wording | Medium | Terms check |
| AI-11 | Google Workspace Gemini | Yes | Included in plan (Jan 2025) | Unknown | Avi Mizrahi | Potentially all Workspace data | Unknown | To verify | Admin-console check by 17 Nov |
| AI-12 | Zoom AI Companion | Yes | Feature | Unknown | Avi Mizrahi | Meeting content | Summaries | To verify | Check settings |
| AI-13 | Monday.com AI assistant | Yes | Feature | Unknown | Yaniv Carmi | B2B leads | Unknown | To verify | Check settings |
| AI-14 | Deskly AI Assist (incl. Autopilot) | Yes | Add-on offered Oct 2026 | Available, not purchased | Samir Haddad | Tickets | Drafts; Autopilot would send replies | — | Module 4 vendor review before any trial |
| AI-15 | CloudVoice call transcription | Yes | Feature | Off | Samir Haddad | Calls | Summaries | — | Record |
| AI-16 | Bitdefender ML detection | Yes | Security tool | On | Avi Mizrahi (MSP) | Device telemetry | Blocking | Low | Record |
| AI-17 | NetGuard URL categorisation | To verify (rules list or model?) | Proxy | On | Avi Mizrahi (MSP) | Browsing | Category labels | Low | Ask MSP |
| X-01 | SmartStock AI | No — min/max formulas, manual seasonality, demand sensing not licensed | Bought 2024 "as AI" | On | Eyal Navon | Stock, POs | Reorder suggestions (~80% approved) | — | Automated-decision list, not AI governance |
| X-02 | AutoRecon | No — four ordered rules | Bought | On | Natalia Gurevich | Bank transactions | Matches | — | Same |
| X-03 | RouteMaster | No (conventional optimisation, per vendor) | Bought | On | Tamar Shalev | Addresses | Routes | — | Re-check at renewal (Feb 2027) |

**Three actions.**

1. *PeopleWise (Dana, with Michal; this week):* export all autumn-round applicants with their match scores and "hidden" status; Dana and Michal ask the company's labour lawyer how to review who was hidden and whether to re-contact anyone; decide whether to switch AI Candidate Match off until reviewed; add PeopleWise's new sub-processor to the vendor review (module 4).
2. *Interim AI rule and approved tool (Michal, 12 November; Avi and Samir to propose the tool by 30 November):* covers AI-02 to AI-06 and AI-10.
3. *Unknown features (Avi, 17 November):* check Gemini, Zoom and Monday.com settings and update AI-11 to AI-13.

**Why the legal register is separate (to Michal).** "The inventory lists everything we found, including what we excluded and what we haven't checked yet, so we never miss a system. The legal register, which counsel will help us build in module 4, lists only the systems that carry a legal duty — PeopleWise and the tools that touch customer data come first — with the duty and the evidence we meet it. If we merged them, counsel would be reading twenty rows of 'unknown', and people would start leaving borderline tools off the inventory to avoid legal attention. They share IDs, so each register row points back to its inventory row."

**What the transcript missed.** Dana was never asked how employees will feel about AI usage dashboards or monitoring; she would have said she fears the best support people will leave if they feel watched. It matters in module 6.

</details>

## References

- EU AI Act, [Recital 12](https://artificialintelligenceact.eu/recital/12/); European Commission, [guidelines on the AI system definition](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-guidelines-ai-system-definition-facilitate-first-ai-acts-rules-application) (6 February 2025).
- NIST, [AI RMF 1.0 Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) — GOVERN 1.6, GOVERN 6.
- Google Workspace, [Gemini included in Business and Enterprise plans](https://workspace.google.com/blog/product-announcements/empowering-businesses-with-AI) (16 January 2025).
- [Employment (Equal Opportunities) Law, 5748-1988](https://www.icj.org/wp-content/uploads/2013/05/Israel-Employment-Equal-Opportunities-Law-5748-1988-eng.pdf) — unofficial English translation; the Hebrew text is authoritative and has been amended since; route questions to counsel.
- The course's [laws and guidance list](../../references/laws-and-guidance.md).
- Template: [AI inventory](../../templates/ai-inventory.md). Lab: [module 1 lab README](../../labs/module-01/README.md).
- Later: module 4 adds risk tiering, the DPIA and the legal register (lessons 04.4, 04.6).
- Previous: [01.6 · The shadow-AI census](lesson-06.md). Module practical: [Walking in — Harbor & Pine](../../projects/m01-walking-in.md).
