"""Policies, the client's guidelines, the vendor's documents, the KM proposal and the insurer's questionnaire.
All fictional. Parshan AI is a fictional vendor; no real product is portrayed."""
from __future__ import annotations

from common import ROOM, write_md


def write(v, nda, clients_by_code) -> None:
    for path, text in DOCS.items():
        write_md(ROOM / path, text)


DOCS = {}

DOCS["policies/it-acceptable-use-2019.md"] = """
# IT acceptable-use policy (extract)

Atlas & Rowe, version 3, approved by the management committee on 12 March 2019. Applies to partners,
associates, interns and staff.

1. Firm equipment and accounts are for firm work. Reasonable personal use is allowed.
2. Client documents are stored only in Archive. Do not save client documents on personal devices or in
   personal cloud storage (for example Dropbox, Google Drive, WeTransfer).
3. Send client documents outside the firm only by firm email or the secure file share.
4. Passwords: at least 10 characters, changed every 90 days; never shared.
5. Software: install only software approved by IT. Browser extensions need IT approval.
6. Report a lost device or a suspected data leak to IT on the same day.
7. The firm monitors internet and email traffic for security purposes.

Review date: March 2021.
"""

DOCS["policies/engagement-letter-template-2023.md"] = """
# Engagement letter — standard terms (extract)

Template ENG-STD-2023, sent with every new engagement since January 2023. Sections 1–8 (scope, team,
fees, expenses, billing, conflicts) are omitted.

**9. Confidentiality.** We keep confidential all information you give us in connection with the
engagement, subject to our professional duties and the law.

**10. Fees and time recording.** Unless agreed otherwise in writing, we charge for time spent by
lawyers and interns at our standard hourly rates, recorded in units of six minutes. We may review and
reduce time at our discretion.

**11. Technology.** We may use technology tools, including cloud services and software, in providing
the services, and may store your documents with our service providers.

**12. Retention.** We keep files for seven years after the matter closes.

**13. Governing law.** Israeli law; Tel Aviv courts.
"""

DOCS["policies/draft-ai-policy-2026.md"] = """
# DRAFT — Use of AI tools at Atlas & Rowe

Circulated by N. Friedman to the partners on 29 October 2026 for comment. Not approved.

**1. Purpose.** To let our lawyers benefit from AI tools safely and keep up with the market.

**2. Which tools.** Lawyers may use any reputable AI tool (for example ChatGPT, Claude, Gemini,
Copilot, Parshan once licensed). Paid versions are preferred.

**3. Client information.** Before entering client documents into a tool, remove the client's name and
the names of individuals. Anonymised documents may be used in any tool.

**4. Quality.** AI output should be reviewed by the lawyer where appropriate.

**5. Billing.** Time saved by AI is the firm's efficiency. On fixed-fee and capped matters it is
retained by the firm. On hourly matters, partners may bill the time a task would normally take, as the
value delivered.

**6. Training.** A one-hour introduction will be offered by the Tech & IP group.

**7. Review.** This policy will be reviewed in 2028.
"""

DOCS["clients/carmel-ocg-2026.md"] = """
# Carmel Retail Group — Outside Counsel Guidelines (extract)

Issued by the Legal Department of Carmel Retail Group Ltd to all panel firms, effective 1 October 2026.
Signed by Adv. Sigal Mizrahi, General Counsel. Sections on staffing, travel and reporting are omitted.

**4. Budgets.** Every new matter above ₪50,000 needs a written budget. Overruns are not paid without
prior written approval.

**5. Fixed prices.** We prefer fixed prices for repeat work (NDAs, supplier agreements, lease renewals,
employment documents). Panel firms will propose fixed prices for these by 30 November 2026.

**7. Use of artificial intelligence.**

7.1 Disclose to the Legal Department, before you use them on our matters, the AI tools you use for
legal work, who provides them and where our information is processed.

7.2 Do not enter Carmel information into any AI tool that may use it to train or improve models, or
that keeps it beyond the engagement, without our prior written consent.

7.3 You are responsible for verifying every authority, quotation and fact in work you send us,
whatever tool produced it.

7.4 We will not pay hourly rates for time that a reasonably efficient firm would not spend because it
would perform the task with technology. We expect the efficiency of such tools to be reflected in your
prices.

7.5 Tell us within 48 hours of any incident in which Carmel information was exposed to an AI tool
contrary to these guidelines.

**9. Panel review.** Panel membership is reviewed annually; the next review closes on 31 January 2027.
"""

DOCS["vendor/parshan-demo-deck.md"] = """
# Parshan AI — "Legal AI built for Israeli and international firms"

Slides presented to the partners of Atlas & Rowe on 8 October 2026 by Parshan's account executive,
transcribed by N. Friedman's assistant. Parshan AI Ltd. is a fictional vendor.

**Slide 2 — Why now.** "The top firms in London, New York and Tel Aviv have adopted legal AI. Clients
expect it."

**Slide 3 — Results.** "Lawyers save **6.2 hours a week**." Footnote: Parshan customer survey, 212
lawyers at 9 US and UK firms, self-reported, Q1 2026.

**Slide 4 — Zero hallucinations.** "Every answer is grounded in your own documents and cited. Our
retrieval engine eliminates hallucinations."

**Slide 5 — Your whole DMS in 48 hours.** "Connect Parshan to your document management system and every
document becomes searchable knowledge, from day one."

**Slide 6 — Languages.** English, French, German, Spanish. Hebrew: beta.

**Slide 7 — Live demo.** Twelve research questions on public US case law, in English, in Parshan's
demo environment. All twelve answered with citations in under 20 seconds.

**Slide 8 — Security.** ISO 27001, SOC 2 Type II. Hosting in the EU (Frankfurt) or the US.

**Slide 9 — Offer.** 90 seats, 24 months, US$120 per seat per month; 20% launch discount if signed by
31 December 2026. Free proof of concept on up to 100 of your documents.
"""

DOCS["vendor/parshan-order-form.md"] = """
# Parshan AI — Order Form (draft for Atlas & Rowe)

Sent by Parshan AI Ltd. on 12 October 2026. Not signed. Extract; the master subscription agreement is
incorporated by reference.

| Item | Terms |
|---|---|
| Customer | Atlas & Rowe, Advocates |
| Service | Parshan Legal (Assistant, Research, Draft, Vault) |
| Seats | 90 named users (minimum) |
| Term | 24 months from signature; renews for 12 months unless notice is given 90 days before expiry |
| Price | US$120 per seat per month, billed annually in advance; launch discount 20% if signed by 31 December 2026 |
| Set-up | US$25,000 one-off (DMS connector, onboarding) |
| Hosting | EU (Frankfurt) |

**3. Customer Data.** Parshan will not use Customer Data to train its models. Parshan's model
sub-processors may retain prompts and outputs for up to 30 days for abuse monitoring. The list of
sub-processors is on Parshan's website and may change on 14 days' notice.

**4. Usage Data.** Parshan may use aggregated and de-identified usage data and Customer feedback to
improve the Service.

**5. Indexing.** On set-up Parshan indexes the document repositories the Customer connects. Access
permissions follow the connected system where the connector supports it.

**8. Liability.** Each party's liability is limited to the fees paid in the twelve months before the
claim. Parshan is not liable for the content of outputs; the Customer is responsible for reviewing
outputs before use.

**10. Termination.** No termination for convenience during the term.
"""

DOCS["vendor/parshan-security-answers.md"] = """
# Parshan AI — answers to Atlas & Rowe's security questions

Received by IT on 20 October 2026 (questions from the firm's managed service provider). Extract.

| # | Question | Parshan's answer |
|---|---|---|
| 1 | Certifications | ISO/IEC 27001:2022; SOC 2 Type II (report under NDA) |
| 2 | Where is data stored and processed? | EU (Frankfurt). Model inference may run in the EU or the US depending on the model provider. |
| 3 | Is customer data used to train models? | No. |
| 4 | Retention by sub-processors | Up to 30 days for abuse monitoring, then deleted. |
| 5 | Does indexing respect ethical walls and DMS permissions? | Yes for iManage and NetDocuments. For other DMS, the index uses the permissions the customer configures in Parshan. |
| 6 | Which DMS does the firm use? (asked by Parshan) | "Archive" (in-house configuration). Connector: generic file connector. |
| 7 | Hebrew | Search and drafting in Hebrew are in beta; citation checking supports English. |
| 8 | Audit log | Admin can export user activity monthly. |
| 9 | Exit | Customer data deleted within 60 days of termination; export on request. |
"""

DOCS["km/km-curation-proposal-2024.md"] = """
# Proposal: reviewing the precedent bank

T. Golan, knowledge management, to the management committee, 3 June 2024. Decision of 17 June 2024:
"Deferred to the 2025 budget." Raised again in 2025 and on 22 October 2026.

**Problem.** Mikbatz holds about 1,100 documents. Most were uploaded once and never reviewed. The
status field says "current" by default. Lawyers cannot tell which precedents reflect current law and
practice; several partners keep their own folders instead.

**Proposal.** Review the most-used 300 documents (about four-fifths of all use) in six months: two
associates at 50% with me, partners signing off by group. Each document gets an owner, a review date,
a status (current, needs update, superseded) and a link to what replaced it. Afterwards, a review
cycle: every document reviewed at least every two years, or when the law changes.

**Cost.** About ₪180,000 in associate time (non-billable) plus my time. A librarian post (₪240,000 a
year) to keep it up afterwards.
"""

DOCS["risk/pi-renewal-questionnaire-2027.md"] = """
# Professional indemnity insurance — renewal questionnaire 2027 (AI section)

From the firm's insurer, received 14 October 2026; renewal date 1 February 2027; questionnaire due 15
January 2027. Section 6 of 9. The insurer is fictional.

6.1 Do lawyers or staff use generative AI tools in client work? Which tools?

6.2 Does the firm have a written policy on AI use, approved by management? Attach it.

6.3 How does the firm verify citations, quotations and authorities in AI-assisted work before it is
sent to clients or filed with a court?

6.4 Is client consent obtained before client information is used in AI tools? How is it recorded?

6.5 In the last three years, has the firm become aware of any incident in which AI-generated content
containing errors was sent to a client, a court or another party, or nearly was? Give details.

6.6 Has any client information been entered into AI tools not approved by the firm? Give details.

6.7 Are lawyers trained in the use and risks of AI tools? When was the last training?

Note from the insurer: answers to section 6 may affect terms. A material non-disclosure may affect
cover.
"""
