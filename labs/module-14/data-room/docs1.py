"""Company documents and policies (markdown)."""
from __future__ import annotations

from common import ROOM, fill, ils, write_md

PROFILE = """# Lumen SaaS — company profile (welcome pack, November 2026)

**Lumen SaaS Ltd.** (לומן) builds **Lumen Shifts**: shift scheduling, time clock and payroll-prep software
for businesses that run on shifts — retail, clinics, logistics, restaurants, light industry. Founded 2014 in
Tel Aviv by Yaron Ben-David (CEO) and Eyal Dahan (VP R&D). About 250 employees, Yigal Alon Street, Tel Aviv.

## Customers (active, 26 November 2026)

| Plan | Customers | Seats | ARR |
|---|---|---|---|
| Starter (self-serve, ₪19 per seat per month) | {{n_starter}} | {{seats_starter}} | {{arr_starter}} |
| Growth (self-serve, ₪24 per seat per month) | {{n_growth}} | {{seats_growth}} | {{arr_growth}} |
| Enterprise (contract, account lead) | {{n_enterprise}} | {{seats_enterprise}} | {{arr_enterprise}} |
| **Total** | **{{n_customers}}** | | **{{arr}}** |

Israel {{n_il}} customers, EU {{n_eu}} (Cyprus, Greece, Germany, the Netherlands, Poland, Romania), US
{{n_us}}. Product languages: Hebrew, English, Arabic, Russian. Customers' staff use the mobile app; the admin
(usually an office manager, HR or the owner) uses the web console.

## What customers trust us with

Staff names, phone numbers, ID numbers (Israel), shift and attendance records, pay rates and payroll
exports. For customers we are a service provider that holds their staff data on their behalf.

## Support

Support works Sunday–Thursday 08:00–18:00 (Israel), about 38 people in two shifts with a shift lead each,
plus an on-call engineer. Channels: email, phone, web form and, since 11 October 2026, the **Lumen Assist**
beta inside the product.

## Systems (internal names)

Admin console and **Admin API** (service tokens with scopes) · Ledgerly (billing; **weekly invoice run,
Thursday 22:00**) · Deskly (helpdesk) · Help centre (CMS) · Flagpole (feature flags) · Lumen Assist (built
on a commercial LLM API behind our own tool layer).
"""

ORG = """# Org chart (November 2026)

- **Yaron Ben-David** — CEO and co-founder
  - **Eyal Dahan** — VP R&D and co-founder (92 people: platform, product teams, QA, DevOps)
  - **Maya Rosenthal** — VP Product (14; Noam Levi is product manager for Lumen Assist)
  - **Revital Azoulay** — VP Support (38: shift leads Boris Feldman and Hiba Mansour; tier-2 engineers incl.
    Yonatan Tadesse) — and from 29 November the **Head of AI Operations** (new role)
  - **Michal Biton** — Director of Customer Success (22 customer-success managers incl. Shira Navon)
  - **Sales** (30; Enterprise commercial account leads: Amir Haddad, Dana Ohana, Pavel Orlov, Lina Khoury)
  - **Dana Klein** — VP Marketing (14)
  - **Oren Shalev** — CFO (Finance 9, incl. billing lead Fatma Abu-Ras)
  - **Andrei Kogan** — CISO (IT and Security, 8)
  - **Nurit Gal** — General Counsel and DPO (Legal, 3)
  - Data (7), HR (5), Operations (5)

Executive staff meets on Wednesdays at 09:00.
"""

BOARD = """# Board update — 21 October 2026 (extract: product and support)

**Lumen Assist.** Our AI agent that resolves customer issues inside the product. Closed beta since
11 October with 420 customers. Early numbers are very strong: **two out of three conversations resolved
without a person** in week 1.

**Plan.** General availability for every customer at **Lumen Live on 9 February 2027**, with the full set
of actions (credits, plan changes, account security, data requests, documents). Target: **50% of all
support contacts resolved without a person by the end of Q2 2027.** This is what lets support grow slower
than customers in 2027 (budget: 4 fewer support hires).

**Governance.** We will hire a Head of AI Operations in Support to own AI quality and safety.

*— Yaron Ben-David*
"""

DASH = """# Lumen Assist beta — weekly dashboard (Product, exported 26 November 2026)

**Resolved by Assist** = the session ended without the customer choosing "Talk to a person".

| Week from | Sessions | Resolved by Assist | CSAT (1–5) | Credits by Assist | Credit amount |
|---|---|---|---|---|---|
{{rows}}

**Beta total: {{n_sessions}} sessions, {{dash_resolved}} resolved by Assist, CSAT {{csat}} ({{n_csat}} ratings).**

Next: all tools on for GA (see the GA design). *Noam Levi, PM Lumen Assist.*
"""

MINUTES = """# Executive staff — minutes, Wednesday 25 November 2026 (extract)

Present: Yaron (chair), Eyal, Maya, Revital, Oren, Dana, Andrei, Nurit. Minutes: executive assistant.

1. **Lumen Assist GA.** Maya: beta "{{dash_resolved}} resolved, CSAT up week on week"; GA design ready
   (all seven tools, shared service identity, action log); launch at Lumen Live 9 Feb is "on track".
   Andrei asked who approved the service token scopes; Maya: "same token support has used since 2024".
   Revital: "a content issue on the 22nd, handled; I'll bring a note" (no note attached).
2. **Head of AI Operations** starts Sunday 29 November, reports to Revital. Yaron: "First job: get Assist
   to GA safely. Bring the authority model to this table on **27 January**."
3. **Enterprise.** Amir (invited): Shaked Clinics renewal 31 March; their security questionnaire includes
   AI questions, due 15 January. Yaron: "Make sure Assist is a selling point."
4. Decision: GA scope to be decided on 27 January.
"""

CREDIT = """# Credit policy — Support (v3, March 2025; owner: Billing)

1. **Who may credit.** Support staff may issue credits **up to ₪500 per case** for billing errors and
   service issues. Above ₪500: the account manager (Customer Success) approves. One credit per case.
2. **Outage credits.** Enterprise outage credits follow the contract's service-level clause and are agreed
   by the commercial account lead with Finance. Starter and Growth: goodwill only, per the shift lead.
3. **Annual plans.** No refunds or credits for unused months of an annual term (see HC-214).
4. **Enterprise contract changes** (seats, plan, term) are made by the commercial account lead. Billing
   syncs contract changes **48 hours** after they are entered.
5. **Reversal.** A credit can be reversed until it is applied by the weekly invoice run (Thursday 22:00).
   After that, a correction is a new charge and needs the account manager.
6. Every credit has a reason code and a note.
"""

SECURITY = """# Account security procedure (ASP, v5, January 2026; owner: Security)

ASP-1. Never change an admin's email, phone or second factor because a caller or chat asks.
ASP-2. **2FA reset:** only after verification **on a channel already on file** — a callback to the phone
       number on the account, or a confirmation link to the admin email on the account. Knowing the
       admin's name, email or an invoice amount is not verification.
ASP-3. Urgency ("payroll closes tonight", "the CEO is abroad") is a reason to slow down, not to skip
       ASP-2. Refuse and log the attempt with the tag `verification_failed`.
ASP-4. Enterprise admins: a second support person confirms every reset.
ASP-5. Documents with staff data (exports, invoices with bank details) are sent only to the admin email on
       the account.
"""

DELETION = """# Data deletion procedure (v2, September 2025; owner: Legal / DPO)

1. Deletion requests go to **privacy-requests** (Deskly group) and are handled by Legal.
2. Before deleting: confirm the requester is the account admin (ASP-2); check what must be kept — invoices
   and payment records (tax), and payroll exports the customer may need; confirm in writing with the admin.
3. Deletion in the **admin console** is a soft delete: data is hidden at once and purged after **14 days**,
   during which Legal can restore it.
4. The Admin API endpoint `DELETE /accounts/{id}/data` is for R&D maintenance only. **It purges at once and
   cannot be undone.**
5. "Stop emails" is not a deletion request: point the customer to notification settings (HC-160).
"""

PUBLISHING = """# Help-centre publishing (Marketing operations, v1, 2024)

- Any editor in Marketing, Support or Billing can publish or update an article directly in the CMS.
- Marketing owns campaign pages and plan pages; Support owns how-to articles; Billing owns billing pages.
- Translations to Arabic and Russian are generated nightly by `svc-translate` from the English version and
  published automatically. Hebrew is translated by the editor.
- Review: "Ask the owning team if you change their article" (recommended).
- Lumen Assist searches every published article in the customer's language.
"""

AUP = """# AI acceptable use (v1, February 2026; owners: CISO and General Counsel)

1. Use only approved AI tools for company and customer data: Microsoft 365 Copilot (pilot), ChatGPT Team
   (Support ops workspace). Others need IT approval.
2. Never paste customer staff data (names, ID numbers, pay) into an AI tool that is not approved.
3. **Every AI agent or automation that uses company systems must be registered with IT** before it runs,
   with an owner, its data, and the credentials it uses.
4. Service tokens are personal to the system they were issued for. Do not reuse or share them.
5. Questions: #it-help.
"""


def write(f: dict) -> None:
    v = {k: (ils(x) if k.startswith("arr") else x) for k, x in f.items() if not isinstance(x, (list, dict))}
    for k in ("seats_starter", "seats_growth", "seats_enterprise"):
        v[k] = f"{f[k]:,}"
    v["dash_resolved"] = f"{f['dash_resolved']:.0f}%"
    v["csat"] = f"{f['csat']:.1f}"
    rows = [f"| {w[0].isoformat()} | {w[1]} | {w[2]:.0f}% | {w[3]:.1f} | {w[4]} | {ils(w[5])} |" for w in f["weeks"]]
    v["rows"] = "\n".join(rows)
    write_md(ROOM / "company" / "company-profile.md", fill(PROFILE, v))
    write_md(ROOM / "company" / "org-chart.md", ORG)
    write_md(ROOM / "company" / "board-update-2026-10.md", BOARD)
    write_md(ROOM / "company" / "assist-beta-dashboard-2026-11.md", fill(DASH, v))
    write_md(ROOM / "company" / "exec-staff-minutes-2026-11-25.md", fill(MINUTES, v))
    write_md(ROOM / "policies" / "credit-policy.md", CREDIT)
    write_md(ROOM / "policies" / "account-security-procedure.md", SECURITY)
    write_md(ROOM / "policies" / "data-deletion-procedure.md", DELETION)
    write_md(ROOM / "policies" / "help-centre-publishing.md", PUBLISHING)
    write_md(ROOM / "policies" / "ai-acceptable-use-2026.md", AUP)
