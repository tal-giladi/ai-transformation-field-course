---
id: "04.2"
module: 4
minutes: 18
practice_minutes: 80
prerequisites: ["04.1"]
objectives:
  - "Define five data classes with examples from the organization's own files, and a rule for mixed records."
  - "Decide which data class may go into which tool from each tool's terms, and record the reason and the condition."
  - "Write an approved / restricted use list in three tiers of control, with uses rather than tool names as rows."
  - "Answer the questions staff actually ask (\"is a supplier record sensitive?\") in one line each from the list."
volatility: implementation
sources:
  - title: "OpenAI — Enterprise privacy at OpenAI (updated 8 January 2026)"
    url: https://openai.com/enterprise-privacy/
  - title: "OpenAI Help Center — How your data is used to improve model performance"
    url: https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance
  - title: "Google Workspace — Generative AI in Google Workspace Privacy Hub (updated 6 October 2026)"
    url: https://knowledge.workspace.google.com/admin/gemini/generative-ai-in-google-workspace-privacy-hub
  - title: "Chambers Practice Guides — Data Protection & Privacy 2026: Israel (data of special sensitivity, security levels, transfers abroad)"
    url: https://practiceguides.chambers.com/practice-guides/data-protection-privacy-2026/israel
  - title: "EBN Law — PPA draft AI guidance: permitted purposes and categories of data input"
    url: https://www.ebnlaw.co.il/media-center/draft-guidance-from-the-israeli-privacy-protection-authority/
  - title: "Bank of Israel — representative exchange rates (2 November 2026)"
    url: https://www.boi.org.il/en/economic-roles/financial-markets/exchange-rates/
last_verified: "2026-11-02"
---

# 04.2 · Approved tools and data classes

The acceptable-use policy says "personal data only in tools approved for it". This lesson makes that sentence usable: five data classes with Harbor & Pine examples, a decision for each tool and class taken from the tool's own terms, and an approved / restricted use list in three tiers of control. You finish by answering the questions staff actually ask — "is a supplier record sensitive?", "can I paste an order number without the name?" — in one line each. At the end you have the list the policy points to.

## The situation

It is Monday 16 November 2026. Michal signs the acceptable-use policy (04.1) on Thursday, and rule 1 points to a list that does not exist yet. The census (01.6) gave you the demand: support agents translating and drafting replies in Russian and Arabic, buyers writing to suppliers in English and Chinese, marketing writing product copy, one person in Finance pasting large blocks into a chatbot. The inventory (01.7) gave you the supply: AI features already paid for inside Google Workspace, StoreHub, MailPost and Canva, a helpdesk add-on on offer, and Olga's request of 2 October for LinguaFlow Business with its data processing addendum attached.

IBM's consulting course calls this tiered control: not every use needs the same review, so sort uses by what they touch and let the low tier run without asking. Here you build the tiers.

## What to do

### Step 1 — Define five data classes with the company's own examples

Classes written in the abstract ("confidential", "restricted") get applied by guesswork. Write each with examples people will recognise from their own screens:

| Class | What it is | Harbor & Pine examples |
|---|---|---|
| **P — Public** | Already published or meant to be | Product pages, published catalogue and prices, help-centre articles, the privacy notice |
| **I — Internal** | Company information with no personal data whose leak would embarrass, not harm | The support handbook, process notes, internal templates, aggregated ticket counts |
| **B — Confidential business** | Information that would harm the company if a competitor or supplier saw it | Supplier prices and terms, purchase costs, margins, finance summary, board minutes, unpublished prices |
| **D — Personal data** | Anything about an identifiable person: customer, employee, candidate, supplier contact | Customer emails and WhatsApp messages, names, phones, addresses, order and claim numbers, damage photos of someone's home, B2B buyers' contact details, a supplier's sales rep |
| **S — Highly sensitive** | Personal data whose misuse causes serious harm, or that the law treats specially | ID numbers, payment details, health information, salaries and HR files, candidates' CVs and scores, anything about a person's finances |

Two rules make the classes work:

- **Highest class wins.** A document or record takes the highest class of anything in it. The damage-claims log has customer names and phones → D, even though most columns are product codes.
- **An identifier is personal data.** Deleting the name does not make a customer email anonymous: the order number, phone or address still points to one person in Priority. Treat it as D unless the text has been checked and stripped of every identifier — which, for a support email, is rarely worth the effort.

Israel first: the Privacy Protection Law, 5741-1981 (חוק הגנת הפרטיות, התשמ"א-1981), as amended by Amendment 13, uses its own term, "information of special sensitivity", and the Privacy Protection (Data Security) Regulations, 5777-2017, set a database's security level partly by whether it holds such data (Chambers' 2026 Israel guide: databases with data of special sensitivity are at least at the medium level). Your class S is an operating label, not the legal definition. Which Harbor & Pine databases hold legally sensitive data, and at which security level, is a question for counsel; write the question down (it goes into the DPIA in 04.4) and keep S strict meanwhile.

### Step 2 — Read each tool's terms for four facts

For each candidate tool, the decision depends on four facts you can find in its terms or admin console. Write them down with the source and the date you checked:

1. **Training:** does the vendor use what we type to train or improve its models? By default, or only if we opt in?
2. **Retention:** how long are prompts and outputs kept, and can our admin change it?
3. **Contract:** is there a company account with a data processing agreement, or is each user a consumer?
4. **Location:** where is the data processed and stored? (Israel's Transfer of Data to Databases Abroad Regulations apply to anything leaving Israel — 01.5.)

Harbor & Pine, checked 2 November 2026:

| Tool | Training | Retention | Contract | Location | Source |
|---|---|---|---|---|---|
| ChatGPT Free / Plus (personal) | May train on content unless the user opts out | Per user settings | Consumer terms, each user | US | OpenAI help page |
| ChatGPT Business (not bought) | Not by default | Admin controls on Enterprise | Business terms | Check at purchase | OpenAI enterprise privacy page |
| Gemini in Google Workspace (company accounts) | Not without the customer's prior permission | Admin sets 90 days to indefinite | Prompts are customer data under the Cloud Data Processing Addendum | As for Workspace; Avi to confirm | Google privacy hub |
| LinguaFlow free extension | Texts kept up to 18 months, used for training | — | Consumer terms; LinguaFlow is the controller | — | DPA §1.2, §4.2 |
| LinguaFlow Business (quoted) | No | Zero retention, 24-hour encrypted logs | DPA, LinguaFlow as processor | EU (Ireland, Netherlands) | DPA §2, §4.1, §5 |
| Deskly AI Assist (offered) | Trains on de-identified content unless opted out | 30 days, then 24 months in analytics | Add-on to the existing MSA and DPA | US workspace; AI in US and EU; human review in the Philippines | Add-on terms §3.2, §3.4, §5.1, Annex 1 |
| CopyGenie Pro (personal card) | Unknown | Unknown | Personal account | Unknown | Ask Noa for the terms |

Three things to notice. The same product can sit in two rows (ChatGPT, LinguaFlow): the plan decides, not the brand. A tool already in the company's contracts (Workspace) may be the cheapest safe option, once someone checks the admin settings. And Deskly — the obvious home for the pilot — is the hardest case: its terms allow training unless you opt out in writing, which is 04.3's job.

### Step 3 — Fill the tools-and-classes matrix

Now decide, for each tool and class: **Yes**, **Yes for listed uses** (with the condition), or **No**. Write the reason in the cell's note. The rule of thumb: a tool may hold a class only if training is off, retention is limited, there is a company contract, and the location question has gone to counsel.

| Tool | P | I | B | D | S |
|---|---|---|---|---|---|
| Personal or free AI tools (any) | Yes | No | No | No | No |
| Gemini in Workspace (company accounts) | Yes | Yes | Yes | Yes for listed uses, once Avi has set retention to 90 days and confirmed the feature settings | No |
| LinguaFlow Business (when bought, extension forced to Business account) | Yes | Yes | Yes | Yes for listed uses (translation of messages and replies) | No |
| Deskly AI Assist | — | — | — | Pending vendor review (04.3) | No |
| CopyGenie (company account) | Yes | Yes | No until terms reviewed | No | No |
| StoreHub, MailPost, Canva AI features | Yes | Yes | Within the existing contract's data | As today, no new data | No |

The free row says "No" for Internal on purpose: the cost of one more rule ("internal is fine in free tools") is higher than the benefit, and the census showed people do not separate internal from personal under time pressure.

### Step 4 — Write the approved / restricted use list in three tiers

Staff think in tasks, not in tools and classes. Turn the matrix into a list of **uses**, sorted into three tiers of control:

- **Tier 1 — Go ahead.** Approved tool, data class allowed, output checked by the user. No one to ask.
- **Tier 2 — Go ahead within the listed use.** Personal or confidential business data, in the tool and for the purpose listed, with the condition stated (for example "a person sends every reply"). Team leads know their team uses it.
- **Tier 3 — Ask first.** Anything new: a new tool, a new data class, output that reaches customers without a person, decisions about people, automated actions. Goes through intake (04.7).

And a fourth list nobody may cross without the governance committee: **restricted uses**.

| Use | Tier | Tool(s) | Condition |
|---|---|---|---|
| Rewrite or translate text with no personal or confidential data | 1 | Any approved tool | Check the output |
| Draft and translate a customer reply (email, web form, WhatsApp) | 2 | Gemini in Workspace; LinguaFlow Business | Minimum needed of the customer's message; a person checks and sends |
| Translate and draft supplier emails, including prices | 2 | Gemini in Workspace; LinguaFlow Business | Company account |
| Product copy and campaign text | 1 | CopyGenie (company account), Gemini | No customer reviews with names |
| Summarise internal documents and meeting notes | 1–2 | Gemini in Workspace | Board and finance material: Tier 2, Finance only |
| Any use of the helpdesk's AI add-on | 3 | Deskly AI Assist | After 04.3 and the DPIA (04.4) |

| Restricted use | Why | Who may lift it |
|---|---|---|
| Sending AI output to customers without a person (auto-send, bots) | Wrong promises go out at volume | Governance committee after a pilot and risk review |
| AI ranking, filtering or scoring applicants or employees | Legal duties; affects people's livelihoods | COO and HR after counsel's review |
| Customer, employee or candidate data in personal or free tools | No contract, training, retention | Nobody |
| Uploading whole datasets (claims log, ticket exports, customer lists) into any chat tool | Mass exposure for a one-off question | Governance committee, case by case |
| Class S data in any AI tool | Highest harm | Governance committee with counsel |
| AI-generated statements of policy, refunds or legal positions to customers | Binding the company to something it never decided | Not allowed; the policy owner writes these |

The Privacy Protection Authority's draft AI guidance (April 2025, still a draft) suggests exactly this content for an internal policy: permitted purposes and categories of data input, role-based access, and limits on reusing inputs for training (EBN Law's summary).

### Step 5 — Answer the questions staff actually ask

Every list generates questions. Answer the common ones on the same page, in one line, pointing to the class or the tier:

| Question | Answer |
|---|---|
| "Is a supplier record sensitive?" | It has two parts: the supplier's prices and terms are **B** (approved business tools); the sales rep's name, mobile and email are **D**. The whole record counts as D. Gemini and LinguaFlow Business: yes. Free tools: no. |
| "Can I paste an order number without the name?" | No — an order number identifies the customer in Priority. It is D. |
| "Can I put a damage photo into Gemini to describe the damage?" | A photo of someone's home is D. Only in the listed use (drafting the reply), with a person sending. |
| "A hotel's procurement manager in Cyprus emailed us — same rules?" | Yes, D. Their contact details are personal data wherever they live (04.6 looks at the EU side). |
| "Can I use free ChatGPT for a supplier email if I remove the prices?" | If nothing in it is B or D, it is Tier 1 — but only in an approved tool. Free tools get public text only. |
| "Ronit's team wants to summarise the finance summary." | B, Tier 2, Gemini on a company account, Finance only. |
| "Can I ask AI which claims to approve?" | No — that is a decision with money and a customer on the other end; it is not on the list. Ask through intake. |
| "Grammarly is on my laptop — keep it?" | Not on the list: extensions need approval. Ask through intake; IT removes unapproved ones by 30 November. |

### Step 6 — Price the change and run the transition

The list changes what people do on Sunday morning. Plan the switch:

- **Buy what the list relies on.** LinguaFlow Business for 15 seats is €2,160 a year (`vendors/linguaflow-translation-dpa.md` §10), about ₪7,600 at the Bank of Israel representative rate of ₪3.5168 per euro on 2 November 2026. Over three years that is about ₪22,800, under ₪50,000: the department head and the CFO approve (`company/finance-summary.md`). Gemini comes with the Workspace plan; the cost is Avi's hour in the admin console.
- **Remove what it forbids.** IT removes the free LinguaFlow extension, "ChatGPT Sidebar" and unapproved Grammarly installs by 30 November and forces the LinguaFlow extension to sign in to the Business account on managed browsers (DPA §9 allows it).
- **Move personal subscriptions to company accounts** (CopyGenie, Midjourney) or end them; stop reimbursing personal AI plans from 1 December.
- **Name the maintainer.** You own the list; Avi checks each new entry's admin settings; the governance committee (04.7) approves Tier 3 and restricted-use changes. Date every version.

## Watch out

- **Classes nobody can apply.** "Confidential" without examples becomes "whatever I think". Use the company's own files as examples.
- **The anonymisation myth.** Deleting a name rarely anonymises a support message. Treat it as personal data.
- **Approving brands instead of plans.** ChatGPT Free and ChatGPT Business are different contracts. Write the plan and the account type in every row.
- **Approving from the vendor's marketing page.** Approve from the terms and the admin settings, with the date you checked.
- **A list without a way to say yes.** If Tier 3 requests wait seven weeks (Olga's did), Tier 1 becomes "whatever works on my phone".
- **Forgetting the transition.** A list that leaves the free extension installed on nine machines has changed nothing.

## Your turn

### Inputs

- Data room (module download): `vendors/linguaflow-translation-dpa.md`, `vendors/deskly-ai-addon-terms.md`, `it/saas-list.csv`, `it/expenses.csv`, `it/browser-extensions.csv`, `policies/privacy-notice.md`, `catalog/products.csv` ([INDEX](../../labs/common/harbor-and-pine/INDEX.md)).
- Your AUP from [04.1](lesson-01.md), census and inventory from [01.6](../module-01/lesson-06.md) and [01.7](../module-01/lesson-07.md).
- Templates: [tools and data classes](../../templates/tools-and-data-classes.md), [approved / restricted use list](../../templates/approved-restricted-use-list.md); spreadsheets `labs/module-04/tools-and-data-classes.csv` and `labs/module-04/approved-restricted-use-list.csv` in the module download ([lab README](../../labs/module-04/README.md)).

### Steps

1. Write the five classes with at least three Harbor & Pine examples each, and the two rules (highest class wins; identifiers are personal data).
2. For at least six tools, record training, retention, contract and location with source and date. For tools whose terms are not in the data room, check the vendor's current page and write the date — or mark "unknown, ask".
3. Fill the tools × classes matrix with Yes / Yes for listed uses / No and a reason.
4. Write the use list: at least six uses in tiers 1–3 and at least five restricted uses, each with who may lift it.
5. Answer eight staff questions in one line each, including "is a supplier record sensitive?".
6. Write the transition: what is bought, removed and moved, by whom, by when, with the cost in ₪ and the exchange rate you used.

### Time

80 minutes.

### Done when

- [ ] Every class has company examples; the mixed-record rule and the identifier rule are written.
- [ ] Every tool row names the plan and account type and cites its terms with a date.
- [ ] No class D or S cell says Yes for a tool that trains on input by default or has no company contract.
- [ ] The use list is written in tasks staff recognise, in three tiers, with conditions.
- [ ] Restricted uses include auto-sending to customers and AI decisions about people.
- [ ] Eight questions are answered in one line each from the list, without "it depends".
- [ ] The transition removes the free extension and personal subscriptions, with dates and owners.

<details><summary>Reference answer</summary>

**Tools × classes (v1, 18 November 2026).** As in Step 3, with these notes: Gemini in Workspace — D only after Avi (1) confirms which Gemini features are on in the admin console, (2) sets Gemini conversation retention to 90 days and (3) records it; counsel asked whether the Workspace data location needs anything under the transfer regulations (the same question applies to Gmail already). LinguaFlow Business — D for translation only; counsel to confirm the EU processing location meets the transfer regulations. Deskly AI Assist — pending 04.3; the default "train on de-identified content unless opted out" rules it out for D until the opt-out is confirmed. CopyGenie — P and I only until Noa supplies the business terms.

**Use list (excerpt).**

| ID | Use | Tier | Tool | Data | Condition | Owner |
|---|---|---|---|---|---|---|
| U-01 | Rewrite, shorten or translate text without personal or confidential data | 1 | Any approved | P, I | User checks | Everyone |
| U-02 | Draft and translate a customer reply | 2 | Gemini (Workspace), LinguaFlow Business | D | Paste only the customer's message, not the history; a person checks names, dates, prices, promises and sends | Samir |
| U-03 | Supplier emails, including prices, in English and Chinese | 2 | Gemini, LinguaFlow Business | B, D | Company account | Eyal |
| U-04 | Product and campaign copy | 1 | CopyGenie (company), Gemini | P | No reviews with names; dimensions and materials checked against `products.csv` | Noa |
| U-05 | Summarise internal documents and meetings | 1 | Gemini | I | — | Everyone |
| U-06 | Summarise finance and board material | 2 | Gemini | B | Finance team only | Ronit |
| U-07 | Helpdesk AI add-on (triage, drafts) | 3 | Deskly AI Assist | D | After vendor review and DPIA | Samir |

**Restricted:** R-01 auto-send to customers; R-02 ranking or filtering applicants or employees (PeopleWise AI Candidate Match stays off); R-03 D or S data in personal or free tools; R-04 whole datasets in chat tools; R-05 S data in any AI tool; R-06 AI-written policy, refund or legal statements to customers.

**Eight answers:** as in Step 5.

**Transition.** Buy LinguaFlow Business, 15 seats, €2,160 a year (≈ ₪7,600 at ₪3.5168/€, Bank of Israel, 2 November 2026) — Samir and Ronit approve (under ₪50,000 over three years), Avi orders by 24 November. Avi removes the free LinguaFlow extension (9 machines), ChatGPT Sidebar (2) and Grammarly (6) by 30 November, forces LinguaFlow sign-in to the Business account, sets Gemini retention. Noa moves CopyGenie to a company card or stops; Finance stops reimbursing personal AI plans from 1 December (₪2,372 reimbursed so far in 2026). You publish the list with the AUP on 22 November and answer questions in the first two weeks.

**What changed from the interim rule:** agents now have two approved tools for the task they were doing in free ChatGPT, so the rule has a "yes" route.

</details>

## References

- OpenAI, [Enterprise privacy](https://openai.com/enterprise-privacy/) and [How your data is used to improve model performance](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance); Google, [Generative AI in Google Workspace Privacy Hub](https://knowledge.workspace.google.com/admin/gemini/generative-ai-in-google-workspace-privacy-hub) — all checked 2 November 2026.
- Chambers Practice Guides, [Data Protection & Privacy 2026: Israel](https://practiceguides.chambers.com/practice-guides/data-protection-privacy-2026/israel) — data of special sensitivity and security levels (a law-firm guide; the Hebrew law and regulations are authoritative).
- EBN Law, [PPA draft guidance on AI systems](https://www.ebnlaw.co.il/media-center/draft-guidance-from-the-israeli-privacy-protection-authority/) — permitted purposes and data categories in internal AI policies (draft).
- Bank of Israel, [representative exchange rates](https://www.boi.org.il/en/economic-roles/financial-markets/exchange-rates/) — ₪3.5168 per euro on 2 November 2026.
- Templates: [tools and data classes](../../templates/tools-and-data-classes.md), [approved / restricted use list](../../templates/approved-restricted-use-list.md).
- Previous: [04.1 · The AI acceptable-use policy](lesson-01.md). Next: [04.3 · Vendor and tool review](lesson-03.md).
