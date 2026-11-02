---
id: "04.1"
module: 4
minutes: 16
practice_minutes: 75
prerequisites: ["01.6", "01.7"]
objectives:
  - "Write an AI acceptable-use policy of at most two pages that a support agent can apply without asking anyone."
  - "Turn the shadow-AI census and the interim rule into policy rules, each with the reason staff will hear."
  - "Test the draft against five real staff questions and fix every rule that cannot answer one."
  - "State what the company logs about AI use and why, in a way that meets Israeli limits on monitoring employees."
volatility: implementation
sources:
  - title: "EBN Law — Draft guidance from the Israeli Privacy Protection Authority on the application of the Privacy Protection Law to AI systems (May 2025): internal policies for generative AI"
    url: https://www.ebnlaw.co.il/media-center/draft-guidance-from-the-israeli-privacy-protection-authority/
  - title: "Pearl Cohen — Israel: New Draft Guidelines on the Application of Privacy Law to AI (4 May 2025)"
    url: https://www.pearlcohen.com/israel-new-draft-guidelines-on-the-application-of-privacy-law-to-ai/
  - title: "Chambers Practice Guides — Data Protection & Privacy 2026: Israel (Or-Hof Law, updated 10 March 2026): employee monitoring, Isakov tests"
    url: https://practiceguides.chambers.com/practice-guides/data-protection-privacy-2026/israel
  - title: "OpenAI Help Center — How your data is used to improve model performance (individual vs business plans)"
    url: https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance
  - title: "Google Workspace — Generative AI in Google Workspace Privacy Hub (updated 6 October 2026)"
    url: https://knowledge.workspace.google.com/admin/gemini/generative-ai-in-google-workspace-privacy-hub
  - title: "Regulation (EU) 2026/1744 (Digital Omnibus on AI), Article 1(5): Article 4 AI literacy as replaced"
    url: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202601744
last_verified: "2026-11-02"
---

# 04.1 · The AI acceptable-use policy

The interim rule you wrote in 01.6 holds the line for a few weeks; it does not tell anyone what they may do. The acceptable-use policy does. In this lesson you write Harbor & Pine's AI acceptable-use policy (AUP) in at most two pages, built from what the census actually found, test it against the questions staff really ask, and settle the one paragraph people will read most carefully: what the company logs about their AI use. At the end you have a policy Michal can sign and HR can translate.

## The situation

It is Wednesday 11 November 2026, the second week. Tomorrow Michal approves the four-line interim rule (01.6): no customer or employee personal details in unapproved AI tools, keep using AI on text without personal details, an approved tool is coming, nobody is disciplined for past use. The census found ChatGPT and a free translation extension in daily use in Customer Service, mostly for Russian and Arabic replies; paid tools on personal cards in Marketing, Purchasing and Finance; and an HR feature that ranks job applicants which nobody chose (01.7).

The company's only rule today is the 2021 IT use policy (`it/it-policy-2021.md`). It says software needs IT approval (§3), customer information may be used "only in company systems (Priority, Deskly, StoreHub, Google Workspace)" (§6), cloud services need IT and management approval (§7), and internet use is logged (§5). It never mentions AI, and its review date (June 2023) passed three years ago.

IBM's governance course says values become governable only when they turn into responsibilities, controls and evidence. An AUP is the first place that happens for staff: who may do what, with which data, and who answers for the output.

## What to do

### Step 1 — Decide what the AUP is for, and what it is not

An AUP answers one question for an employee: *may I use AI for this, with this data, in this tool?* Everything else belongs in another document of the policy pack:

| Question | Document | Lesson |
|---|---|---|
| Which tools, for which data classes? | Approved / restricted use list, tools and data classes | 04.2 |
| Is this vendor safe to buy? | Vendor AI questionnaire | 04.3 |
| What AI do we run, how risky is each use? | AI inventory with tiers, DPIA | 04.4 |
| What could go wrong and is the control working? | Risk register | 04.5 |
| Which laws apply? | Regulatory map | 04.6 |
| Who decides about new AI, how fast? | Governance charter, intake register | 04.7 |

Keep the AUP stable and short and let the lists change. If the AUP names tools, every new tool needs a policy change signed by management; if it points to the approved-tools list, IT updates the list and the policy stays put.

### Step 2 — Write rules from the census, not from a template

Each finding from 01.6 and 01.7 becomes a rule, and each rule gets its reason in one plain sentence. Staff follow rules they understand; the reason is also what lets a team lead decide a case the rule did not foresee.

| Census finding | Rule | Reason staff hear |
|---|---|---|
| Customer emails with names and phones pasted into free ChatGPT | Personal data only in tools on the approved list for that data class | Free chat tools may keep what you type and use it to train their models; the company cannot get it back |
| Free LinguaFlow extension reading every page on 9 machines | No AI browser extensions unless approved; IT removes the rest | An extension that can "read and change all your data on all websites" sees every customer screen in Deskly |
| Six replies sent with the chatbot's own preamble ("Of course! Here is a polite reply…") | You read and own every AI output before it leaves the company | The customer reads what you send; "the AI wrote it" is not an excuse to them or to us |
| CopyGenie, ChatGPT Plus, Claude Pro on personal cards | Work AI runs on company accounts, never personal ones | On a personal account the company has no contract, no admin control and no way to delete data |
| PeopleWise ranking applicants by default | No AI in decisions about people (hiring, pay, performance, discipline) without written approval | These decisions carry legal duties and affect lives; they need a review first |
| Olga asked IT for a proper translation tool on 2 October and never heard back | New tool or new use: ask through the intake form; answer within 10 working days | A rule without a fast "yes" route sends people back to their phones |

The reasons are facts you checked, not scare stories. OpenAI's help page says that for its services for individuals (Free, Plus, Pro) it "may use your content to train our models" unless the user opts out, and that by default it does not train on inputs or outputs from ChatGPT Business, Enterprise, Edu or the API. Google's Workspace privacy hub says Workspace "does not use customer data for training models without customer's prior permission or instruction". Consumer and business plans of the same product are different products; the AUP rule follows that line, and 04.2 names which plans are approved.

### Step 3 — Write it in seven short sections

Two pages is a hard limit: the people who most need the policy read it on a phone between calls. Use this order (the [acceptable-use policy template](../../templates/acceptable-use-policy.md) has it ready):

1. **Why we have this policy** — two sentences: we want people to use AI, safely.
2. **What counts as AI here** — the counting rule from 01.7 in one sentence, plus "AI features inside tools we already use count too".
3. **The rules** — at most ten, each one line plus its reason.
4. **Data: what may go where** — one line per data class, pointing to the list (04.2).
5. **Asking for a new tool or use** — the intake route and the response time (04.7).
6. **What we log, and why** — Step 5 below.
7. **Owner, review date, exceptions, and how to report a mistake.**

Israel first: the Privacy Protection Authority's draft guidance on AI (published April 2025 for comment, **still a draft** when checked on 2 November 2026) recommends, for the first time, that organizations adopt internal policies for using generative AI systems, including third-party tools, covering risks and mitigations, role-based access, permitted purposes and categories of data input, security assessment, retention and employee training (EBN Law's summary). It is not binding as a draft, but it is the clearest statement of what the regulator expects to see, and it maps one to one onto the seven sections. If the company ever has to explain itself to the PPA, a signed AUP with a data-class rule is the first document anyone will ask for.

### Step 4 — Make "you own the output" concrete

"Use AI responsibly" binds nobody. Write what the person must actually do before an AI output leaves their hands:

- **Read it all.** Check names, order numbers, dates, prices and promises against the system (Priority, Deskly, StoreHub), not against the draft.
- **Never send a promise the company has not made** — a refund, a delivery date, a discount — because the AI wrote it.
- **Remove what the AI added**: preambles, placeholders such as "[Имя клиента]" ("[Customer name]"), invented policies.
- **Nothing goes to a customer without a person pressing Send.** Automatic sending (Deskly's "Autopilot", a website bot) is a separate decision for management, not something a user switches on.

The last line matters now: Deskly's add-on terms let "any workspace Administrator" switch Autopilot on for any view (`vendors/deskly-ai-addon-terms.md` §1.2). The AUP is where "a person sends every reply" becomes a rule rather than a habit; 04.3 turns it into an admin setting.

### Step 5 — Say what you log, and stay proportionate

The proxy already logs every website (IT policy §5); the approved tools will have admin logs; module 6 will build an adoption dashboard from usage exports. Employees will ask whether the company reads their prompts. Answer before they ask.

Israeli labour case law sets the frame. The National Labour Court's *Isakov* judgment (2011) requires employer access to employees' digital assets to pass cumulative tests of legitimacy, proportionality and transparency (Chambers' 2026 Israel guide). For an AUP that means:

- **Say what is collected:** which sites are visited (proxy), which approved AI features are used and how often (admin analytics).
- **Say why:** security, licence costs, and measuring whether the tools help.
- **Say how it is reported:** by team, not by person, except in a security incident.
- **Say what is not done:** nobody reads individual prompts or conversations as routine; access to content happens only in an investigation approved by the COO with HR.
- **Bring it to employees' attention** in their language, and keep proof that you did (HR's acknowledgement).

Whether a specific monitoring step is lawful is a question for the company's labour lawyer, not for you; the policy's job is to make the practice transparent and limited enough that the question rarely comes up.

### Step 6 — Test the draft against real questions

Before Michal signs, run five questions people actually asked during the census through the draft. If the policy cannot answer one in under a minute, rewrite the rule, not the answer.

| Question (who asked) | The draft must answer |
|---|---|
| "Can I paste the customer's email if I delete the name?" (support agent) | No, unless the tool is approved for customer data: the order number, address and phone still identify the person |
| "Can I use ChatGPT to translate a supplier's price list?" (buyer) | Supplier prices are confidential business data: approved tools only |
| "Is my Grammarly OK?" (COO's assistant) | Extensions need approval; ask through intake; meanwhile only text without personal or confidential data |
| "Can I use Midjourney for a campaign image?" (marketing) | Yes, on a company account, with no customer photos or personal data in the prompt |
| "The HR system ranks candidates automatically — is that allowed?" (HR) | Not until reviewed: decisions about people need written approval |

### Step 7 — Get it signed, translated, and acknowledged

Signature: the COO (sponsor) for now; the governance charter (04.7) names the owner from then on. Translation: Hebrew, Arabic and Russian, with the English text as the master copy, and HR collects acknowledgements. Review date: six months, not two years — tools and terms change faster than the 2021 policy assumed. The AUP replaces the interim rule and updates IT policy §7 by reference; it does not rewrite the IT policy.

AI literacy is the companion to the policy, not a substitute. The EU AI Act's Article 4, as replaced by the Digital Omnibus (Regulation (EU) 2026/1744, in force since 27 July 2026), still says providers and deployers "shall take measures to support the development of AI literacy" of their staff. Whether the Act reaches Harbor & Pine at all is 04.6's question; the practical point holds anyway: a policy nobody was trained on is a policy on paper. Module 6 builds the training.

## Watch out

- **The ten-page policy.** Long policies get signed and never read. If it does not fit on two pages, the detail belongs in the lists.
- **Copying a template from the internet.** Generic rules ("use AI ethically") answer none of the five questions. Every rule should trace to a census finding.
- **A ban with no approved tool.** The census showed real needs (Russian and Arabic replies). Ban without an alternative and use moves to phones, out of every log. Ship the AUP with at least one approved tool per need, or a date.
- **Punishing past use.** The interim rule promised amnesty. A policy that starts with discipline ends the census and turns your best ally (the agent who uses AI most) into an opponent.
- **Monitoring language that frightens.** "All AI use is monitored" invites the question nobody can answer well. Say exactly what is collected, why and how it is reported.
- **Naming tools in the policy.** Then every new tool needs a management signature. Point to the list.
- **No owner and no review date.** The 2021 policy is the warning: due for review in 2023, never reviewed.

## Your turn

### Inputs

- Data room (module download): `it/it-policy-2021.md`, `vendors/linguaflow-translation-dpa.md` (the free-extension terms in §4.2), `vendors/deskly-ai-addon-terms.md` (§1.2, §4.1) ([INDEX](../../labs/common/harbor-and-pine/INDEX.md)).
- Your census, interim rule and inventory from [01.6](../module-01/lesson-06.md) and [01.7](../module-01/lesson-07.md).
- Template: [acceptable-use policy](../../templates/acceptable-use-policy.md).
- Optional: the [coach prompt](../../labs/common/coach-prompt.md) with the "Done when" list as the checklist, on your draft.

### Steps

1. List every census and inventory finding that needs a rule (at least six), with the reason in one sentence.
2. Draft the AUP in the template's seven sections. Count: it must fit on two pages (about 900 words).
3. Write section 6 (what we log) and check it against legitimacy, proportionality and transparency.
4. Run the five questions from Step 6 through your draft; write the answer the policy gives and fix the rules that fail.
5. Add the sign-off block: owner, approver, effective date, review date, languages, acknowledgement.

### Time

75 minutes.

### Done when

- [ ] The policy fits on two pages and has the seven sections.
- [ ] Every rule traces to a finding and carries its reason.
- [ ] Data rules point to the approved list (04.2) instead of naming tools in the policy.
- [ ] "You own the output" lists the checks a person makes before sending, and states that no reply reaches a customer without a person.
- [ ] The logging section says what, why, how it is reported, and what is not done.
- [ ] The five test questions are answered by the text as written.
- [ ] Owner, approver, review date (six months) and translations are named; past use is covered by the amnesty.

<details><summary>Reference answer</summary>

**Harbor & Pine — Using AI at work (v1.0, effective 22 November 2026)**

*Owner: AI and Operations Improvement lead. Approved by: Michal Peretz, COO, 19 November 2026. Review: May 2027. Master text in English; Hebrew, Arabic and Russian translations by HR. Replaces the interim AI rule of 12 November 2026 and adds to IT policy §7.*

**1. Why.** AI tools save us real time, especially on replies in Russian and Arabic, supplier emails and product copy. We want everyone to use them — in a way that keeps our customers' and colleagues' information safe and keeps us responsible for what we send.

**2. What counts as AI.** Any tool or feature that writes, translates, summarises, scores or recommends by itself, including AI features inside software we already use (Gmail, Deskly, PeopleWise, Canva). If unsure, treat it as AI.

**3. The rules.**

1. Use only tools on the **approved AI list** (link) for work, and only with the data classes the list allows for each tool. *Free and personal AI tools may keep what you type and train on it; we cannot get it back.*
2. **Company accounts only.** No work in AI tools paid with a personal card or signed in with a private account. *Without a company account we have no contract and no way to delete data.*
3. **No AI browser extensions** unless on the approved list. IT will remove the others by 30 November. *Extensions can read every page you open, including customer screens.*
4. **You own every output.** Before anything leaves the company, read all of it and check names, order numbers, dates, prices and promises against Priority, Deskly or StoreHub. Remove AI preambles and placeholders. *The customer reads what you send.*
5. **Never promise because the AI did.** No refund, date, discount or policy the company has not made.
6. **A person sends every customer reply.** Automatic sending and website bots need a management decision (governance committee). Nobody switches on auto-send features.
7. **No AI in decisions about people** — hiring, pay, performance, discipline — without written approval from the COO and HR after review. *These decisions carry legal duties.*
8. **New tool or new use? Ask** through the AI request form. You get an answer within 10 working days.
9. **Mistakes: tell us the same day** (your manager or ai@harborpine.co.il). Reporting a mistake is never a disciplinary matter; hiding one may be.

**4. Data: what may go where.** Public (website, published catalogue): any approved tool. Internal (procedures, internal notes without personal data): approved tools. Confidential business (supplier prices and terms, margins, financials, board material): approved tools marked "business data". Personal data (customers, employees, candidates — names, phones, addresses, order or claim numbers, photos): only tools marked "personal data", only for the uses listed. Highly sensitive (ID numbers, payment details, health, salaries, candidate assessments): never into an AI tool unless the governance committee approved that specific use. Unsure about a document? Use the highest class anything in it belongs to.

**5. Asking for something new.** AI request form (link) → the AI lead answers within 10 working days: yes, yes with conditions, or no with the reason. Uses that touch personal data, customers directly or decisions about people go to the governance committee, which meets monthly.

**6. What we log, and why.** The web proxy records which websites company computers visit (IT policy §5), and approved AI tools record which features each account uses and how often. We use this for security, to manage licences and to see whether the tools help. We report it by team, not by person. Nobody reads individual prompts or conversations as a routine; content is accessed only in a security or legal investigation approved by the COO together with HR, and you will be told. Proxy logs are kept 90 days.

**7. Owner, exceptions, review.** Questions: the AI lead. Exceptions: in writing, approved by the COO, recorded in the intake register. Nobody is disciplined for AI use before 12 November 2026. This policy is reviewed every six months and whenever the approved list changes a data class.

*Please confirm you have read this policy in PeopleWise by 6 December.*

**The five questions, answered by the text:** (1) deleting the name is not enough — order number and phone are still personal data → only tools marked "personal data" (rule 1, §4); (2) supplier price list → confidential business → approved tools marked "business data" (§4); (3) Grammarly → extension, not on the list → ask through the form; meanwhile only public text (rule 3, §5); (4) Midjourney on a company account, no personal data in the prompt (rules 1–2, §4) — if not yet on the list, ask; (5) PeopleWise ranking → decision about people → off until approved (rule 7).

**Words:** about 700. **What it leaves to other documents:** the tool names (04.2), the request form and committee (04.7), the vendor terms behind each "approved" (04.3).

</details>

## References

- EBN Law, [Draft guidance from the Israeli Privacy Protection Authority on AI systems](https://www.ebnlaw.co.il/media-center/draft-guidance-from-the-israeli-privacy-protection-authority/) and Pearl Cohen, [Israel: New Draft Guidelines on the Application of Privacy Law to AI](https://www.pearlcohen.com/israel-new-draft-guidelines-on-the-application-of-privacy-law-to-ai/) — the PPA's draft (April 2025; still a draft on 2 November 2026) recommends internal generative-AI use policies.
- Chambers Practice Guides, [Data Protection & Privacy 2026: Israel](https://practiceguides.chambers.com/practice-guides/data-protection-privacy-2026/israel) — the *Isakov* tests for employee monitoring. The judgment is in Hebrew; ask counsel before relying on it.
- OpenAI, [How your data is used to improve model performance](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance); Google, [Generative AI in Google Workspace Privacy Hub](https://knowledge.workspace.google.com/admin/gemini/generative-ai-in-google-workspace-privacy-hub) — consumer vs business plans, checked 2 November 2026.
- [Regulation (EU) 2026/1744](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202601744), Article 1(5) — the AI Act's Article 4 (AI literacy) as replaced.
- The course's [laws and guidance list](../../references/laws-and-guidance.md).
- Template: [acceptable-use policy](../../templates/acceptable-use-policy.md).
- Earlier: [01.6 · The shadow-AI census](../module-01/lesson-06.md) (interim rule), [01.7 · The AI inventory from zero](../module-01/lesson-07.md). Next: [04.2 · Approved tools and data classes](lesson-02.md).
