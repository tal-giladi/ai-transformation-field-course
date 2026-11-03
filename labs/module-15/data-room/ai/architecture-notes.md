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
