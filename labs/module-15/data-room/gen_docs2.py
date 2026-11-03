"""governance/*.md, ai/architecture-notes.md, branches/branch-managers-forum-2026-11-minutes.md."""
from gen_common import write_md

POLICY = """
# AI policy, version 1 (מדיניות בינה מלאכותית) — approved by the Management Committee, 22 June 2025

Owner: COO. Review: yearly.

1. **Definition.** An AI system is any system that uses machine learning, a statistical model trained
   on data, or a generative model (including large language models). Every AI use at Crescent is a
   *model* under the bank's model risk management policy.
2. **Approval before use.** No AI system may be used with real data before full independent
   validation by Model Risk Management and approval by the Model Committee. Full validation applies to
   every AI system, whatever its use.
3. **Pilots.** A pilot may run in the AI sandbox with synthetic or masked data. Real customer data in a
   pilot needs written approval of the DPO for that pilot. Customer-facing pilots need the Model
   Committee's approval before any customer sees an output.
4. **Register.** Every AI pilot is registered with the COO office within 5 working days of its start.
5. **Committee.** The Model Committee meets monthly. It reviews all AI pilots every quarter.
6. **Public tools.** Customer data and confidential data must not be entered into public AI tools.
   Public generative AI services are blocked on the bank's network.
7. **Vendors.** AI supplied by a vendor is subject to this policy and to the outsourcing procedure.
8. **Exceptions.** Only the CRO may approve an exception, in writing, for a limited time.
"""

MINUTES = """
# Model Committee — 2026 minutes (AI items only, extract)

Chair: Dr. Irina Kogan (CRO). Members: Yonatan Bar (MRM), Nir Ashkenazi (CIO), Adv. Lina Nassar (CCO),
the unit head for each item. Secretary: MRM.

**18 February 2026.** RET-03 Branch staff FAQ assistant (submitted October 2025): deferred pending full
validation; MRM capacity for AI in Q1 is used by the Directive 369 phase-in. The unit asked whether
staff may keep using it in the meantime; the chair noted that the pilot runs in the sandbox.

**22 April 2026.** CRD-02 Fraud alert triage and CRD-03 Dispute letter drafts: deferred pending full
validation. CRD-03 to stay on hold. The Head of Cards asked for a faster route for letters a person
reviews before sending; the chair answered that the policy makes no distinction.

**17 June 2026.** MTG-01 Mortgage document extraction, CMP-01 KYC document checks: deferred pending
full validation. MRM reported that 3 AI review slots a quarter are the most it can give in 2026–2027.

**16 September 2026.** CORP-01 Credit memo assistant, CRD-01 Complaint summaries — Cards, CC-01 Call
summaries: deferred pending full validation. CRK-01 Early-warning signals: validation started 6
September. The CIO asked for a priority order across units; the committee asked the COO office for a
list of all AI pilots.

**25 November 2026.** OPS-01 Bank-wide assistant: validation started (scope: "the assistant as a
model"). DIG-01 Customer chatbot: returned, documentation incomplete. HR-01 CV screening: returned,
documentation incomplete; MRM noted the selection-rate result. The COO informed the committee of the
board's decision on the AI CoE. Decisions in 2026 on AI items: approved 0, declined 0.
"""

WORKPLAN = """
# Model Risk Management — work plan 2027 (extract)

Owner: Yonatan Bar, Head of MRM. Approved by the CRO, 10 December 2026.

**People.** Head of MRM and two validators (Ma'ayan Levi, Oleg Shapiro). One validator position
requested for 2027; not in the budget.

**Capacity.** We plan in *review slots*: one slot is about ten validator-days in a quarter. The unit
has about 12 slots a quarter.

| Use of slots (per quarter, 2027) | Slots |
|---|---:|
| Directive 369 phase-in: existing non-material models (deadline 21 February 2027 under circular 2792; 61 not yet compliant on 31 December 2026) | 6 |
| Annual reviews of material models | 3 |
| AI models (Model Committee queue) | 3 |
| **Total** | **12** |

**AI.** Under the AI policy every AI system needs full validation: 2 slots each. At 3 slots a quarter
we validate 1.5 AI systems a quarter. On 31 December 2026 the AI queue has 19 submissions (2 in
validation). After 21 February the phase-in slots move to annual reviews, not to AI, unless the
validator position is approved.

**Risks.** Key-person risk: three people, no backup for market-risk models. External validation
support is possible (about ₪350,000 for six months) but not budgeted.
"""

SURVEY = """
# Banking Supervision Department — AI-governance survey 2026: Crescent's answers (extract)

Prepared by the Compliance Division (regulatory liaison) with the COO office; approved by the CCO and
the CRO; submitted 2026. Extract of the questions about inventory and use.

| # | Question (summary) | Crescent's answer |
|---|---|---|
| 3.1 | Does the bank maintain a central inventory of AI applications, with an owner and a risk level for each? | Yes. The AI pilot list maintained by the COO office lists every AI application with its business owner and risk level. |
| 3.2 | Are AI applications subject to model risk management? | Yes. Every AI application is a model under the bank's policy and is validated in full by MRM and approved by the Model Committee before use. |
| 3.4 | Is AI used in customer-facing processes? | No AI application is in production with customers. |
| 4.2 | How does the bank control the use of public generative AI tools? | Public generative AI services are blocked on the bank's network; the AI policy prohibits entering customer data. |
| 5.1 | Is vendor-supplied AI identified? | Vendor AI is reviewed through the outsourcing procedure and the Model Committee. |
"""

ARCH = """
# IT architecture review — notes on AI pilots (extract), December 2026

Author: IT Architecture (for the AI CoE handover). One entry per pilot that IT reviewed; other pilots
were not reviewed by IT.

**OPS-01 Tzofen Assist (tenant `tzofen-tenant-01`).** SaaS assistant, Israel region. Seats assigned
by HR group. Includes the *agent studio*: units can build assistants on their own documents; each
studio assistant uses a retrieval index inside the tenant (indexes today: `OPS-procedures`,
`CC-knowledge`). Users of a studio assistant must hold a Tzofen seat. If the tenant is not renewed,
the indexes and the studio assistants are deleted 30 days after the end of the subscription.

**OPS-02 Procedure assistant.** Built in the Tzofen agent studio on index `OPS-procedures` (1,240
procedure sections, Hebrew). No separate licence: covered by the OPS-01 seats. 118 back-office users.

**CC-02 Agent knowledge assistant.** Built in the Tzofen agent studio on index `CC-knowledge`
(knowledge base + procedures). No separate licence: covered by the OPS-01 seats. 110 agents in the
pilot; the plan is all 420 agents in 2027.

**RET-03 Branch staff FAQ.** Retrieval over the procedures library with the Ananim sandbox LLM API
(`nimbus-sbx-ret`). Branch staff reach it from branch PCs through the sandbox portal. The sandbox
terms (PR-2025-099) say "pilots only, no production use".

**CC-01 Call summaries.** Kolelet AI transcribes and summarises calls (Hebrew, Arabic, Russian). Since
August 2026 a Kesher 360 macro written by Digital Channels copies the summary into the customer's
Kesher note when the agent closes the call. The macro is owned by Digital Channels.

**DIG-02 Chat transcript summaries.** Bahir Labs API summarises agent chats and writes the summary
to the customer record in Kesher.

**CRD-01 Complaint summaries — Cards.** Bahir Labs API (contract PR-2025-131), Cards tenant
`cleartext-crd`. Input: complaint text, dispute history. Output: summary, root-cause tag, monthly
themes.

**RET-01 Smart complaint summary.** Mishov Analytics SaaS (tenant `mishov-ret-tenant`). Input:
complaint text from all channels exported nightly from Kesher. Output: summary per complaint, themes.

**MTG-01 Mortgage document extraction.** Rishum Docs tenant `docai-mtg-sbx`; users: Mortgages
underwriting and the back office.

**TRS-01 Daily market summaries.** Environment `trs-llm-sbx` (Ananim API); one daily job at 07:10
produces one note, distributed by email list.

**DIG-01 Customer chatbot.** Sichon AI platform. A/B test live on 2% of web visitors since 3 November
2026 (Digital's decision).

**IT capex 2027.** Line 7700-31 "AI landing zone" (hosting, identity, logging and monitoring for AI
workloads in the bank's cloud tenant): ₪1.1M approved, no project started.
"""

FORUM = """
# Branch managers' forum, northern region — minutes, 19 November 2026 (extract)

Present: 14 branch managers, the regional manager, the branch digital lead.

1. **Branch FAQ assistant.** Managers said it is "the tool we use most after the core system": fees,
   standing orders, powers of attorney, forms. Haifa Hadar (Olga Petrenko): a customer was quoted
   the old account-management fee on 10 November; the fee table in the library had not been updated
   after the November price change. The digital lead updated it on 26 November.
2. **Letters in Arabic and Russian.** Several branches asked for help drafting customer letters in
   Arabic and Russian; the regional manager will pass the request to the AI CoE (REQ in the intake).
3. **Tzofen seats.** Branch staff received Tzofen seats on 1 December; no training date yet.
"""


def build() -> dict:
    write_md("governance/ai-policy-v1-2025.md", POLICY)
    write_md("governance/model-committee-minutes-2026.md", MINUTES)
    write_md("governance/mrm-workplan-2027.md", WORKPLAN)
    write_md("governance/bsd-ai-survey-response-2026-extract.md", SURVEY)
    write_md("ai/architecture-notes.md", ARCH)
    write_md("branches/branch-managers-forum-2026-11-minutes.md", FORUM)
    return {"governance_docs": 6}
