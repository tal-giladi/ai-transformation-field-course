"""Grant library, newsletter, vendor documents and Yossi's IT notes."""
from __future__ import annotations

from common import ROOM, fill, write_md

BOILERPLATE = """
# Boilerplate 2025 (development team's master text)

*Noa Ben-Ami, last edited February 2025. Paste from here; adapt to each funder's template.*

## About Open Hands (150 words)

Open Hands (ע"ר) was founded in 2008 by parents of children with disabilities in Kiryat Ata. Today we accompany more than 400 families across Haifa Bay and the western Galilee, Jewish and Arab, veteran Israelis and new immigrants, in Hebrew, Arabic, Russian and Amharic. A family coordinator — a qualified social worker — walks beside each family through the maze of rights, committees and services; respite weekends give parents rest; parent groups and a siblings' programme bring families together. Our approach: the family leads, we accompany; no family is turned away for language, income or diagnosis.

## The need (100 words)

Families raising a child with a disability in Israel face a fragmented system: National Insurance, the Ministry of Welfare, the Ministry of Education, health funds and local authorities each with their own forms and committees. Families who speak little Hebrew, or who live in Arab towns with fewer services, lose rights they are entitled to. Parents, mostly mothers, cut work hours or leave work.

## Outcomes we track

See the outcomes framework (2024). *(In practice each funder's report asks for different measures; we compile them by hand.)*

## Budget narrative (standard)

Staff costs are 77% of the budget. A family coordinator at 80% costs ≈ ₪186,000 a year with benefits and accompanies ≈ 70 families.
"""

TEMPLATE = """
# Adler-Haddad Family Foundation — quarterly grantee report (template)

*Template issued to grantees in 2023. Word document; English only. Submit by the 15th of the month after the quarter.*

**Section 1 — Summary of the quarter** (max. 500 words)

**Section 2 — Outputs** (table): families served; new families; contacts; home visits; rights obtained (by type); referrals made.

**Section 3 — Family outcome narratives.** *For each family served under the grant during the quarter*, a narrative of 150–250 words describing: the family's situation at the start of the quarter, the activities undertaken, the outcomes achieved, and the next steps. Please make narratives specific enough that the Foundation can understand the difference the grant made to this family.

**Section 4 — Challenges and lessons** (max. 300 words)

**Section 5 — Financial report** (attached form)

**Section 6 — Two photos** of programme activities (with consent).

*Questions: Tamar Weiss-Levi, Programme Officer.*
"""

Q3_REPORT = """
# Adler-Haddad quarterly report, Q3 2026 — extract (as submitted on 24 October 2026)

*Section 3, the first three of {{ah}} family narratives. Compiled by Shira Levin from the coordinators' drafts; reviewed by Hana Golan and Dr. Ronit Azoulay.*

**Family 1.** Noor (8) lives in Tamra with her parents and three siblings. Noor was diagnosed with cerebral palsy at birth and uses a wheelchair; her father works in construction and her mother left her job as a teacher's assistant last year to care for her. At the start of the quarter, the family's appeal against the National Insurance decision on the disabled-child benefit had been rejected. Our coordinator, Rasha, accompanied the mother to the appeals committee in Nazareth on 14 August, and the benefit was approved at 100% from July. The family also joined our Arabic-speaking parent group. Next steps: apply for an accessible transport arrangement for school; follow up on a home adaptation grant.

**Family 2.** Daniel (6), from Kiryat Bialik, has autism and severe sleep difficulties. The family immigrated from Ukraine in 2022 and the mother speaks limited Hebrew. During the quarter our coordinator Marina helped the family through the placement committee: Daniel now attends a communication class at a special-education school in the Krayot. The mother told us that for the first time she slept through the night after a respite weekend in September. Next steps: rights for the mother as a single parent; Hebrew course.

**Family 3.** Adam (9), from Shefa-'Amr, lives with Angelman syndrome. … *(narrative continues)*

*[{{rest}} further narratives follow in the original.]*
"""

FRAMEWORK = """
# Open Hands outcomes framework (2024)

*Developed with a volunteer evaluator in 2024, adopted by the board in June 2024. Not yet used in any funder report.*

| Outcome | Indicator | How we measure | Frequency |
|---|---|---|---|
| Families obtain their rights | Rights obtained per family per year (benefit, appeal, transport, aide, adaptation) | Coordinator records at each case review | Quarterly count |
| Families navigate the system with less help | Share of families who completed one process on their own after 12 months | Coordinator's 4-point rating at the annual review | Annual |
| Parents rest | Parent-reported rest after a respite weekend (1–5) | Short form after each weekend | Per weekend |
| Parents stay in work | Share of parents in paid work at intake vs after 12 months | Intake form and annual review | Annual |
| Families are less isolated | Participation in a parent group; parent-reported isolation (1–5) | Group attendance; annual survey | Annual |
| Equal access | Above indicators by language and town | Same data, split | Annual |

**Stories.** Each quarter, up to six family stories told with the family's approval of the text (consent v2, Part B), to illustrate the numbers.
"""

NEWSLETTER = """
# Open Hands newsletter — September 2026 (email to {{subs}} contacts; also on Facebook)

## "Adam's smile" — a story from Shefa-'Amr

Adam is nine. He lives in Shefa-'Amr with his parents and his two big sisters, and he goes to the special-education class at Al-Nour school. Adam lives with Angelman syndrome, a rare genetic condition: he does not speak, he walks with help, and he laughs more than anyone we know.

When Adam's family came to us in 2021, his mother, Lina, had just left her job. "I was fighting everyone," she told our coordinator. "National Insurance, the school, the health fund. I was alone." With Samah, our coordinator, the family won an appeal for Adam's disabled-child benefit, got a school aide, and in the summer Adam spent his first respite weekend with our volunteers — while his parents slept for two nights in a row for the first time in years.

**This Giving Tuesday (1 December), help us give more families like Adam's a weekend of rest.** ₪360 funds one child's place on a respite weekend.

*Photo: a child's hands holding a ball (stock image).*

*Text: Dr. Ronit Azoulay. Design: Maya Ronen.*
"""

GRANTGENIE = """
# GrantGenie — terms of service (extract) and nonprofit offer

*Saved by Noa Ben-Ami on 3 September 2026 when she signed up. GrantGenie is a fictional vendor.*

**Nonprofit Free Year.** Verified nonprofits get GrantGenie Pro free for 12 months, ending on 31 December of the year following sign-up, or on the date stated in your account. After that, your plan converts automatically to Pro at US$49 per month, billed to the card on file, unless you cancel before the conversion date.

**4. Your content.** You keep ownership of the documents you upload ("Your Content"). You grant GrantGenie a worldwide, non-exclusive, royalty-free licence to host, copy, process and analyse Your Content to provide and **improve the Services, including to train and evaluate our models**. You can opt out of model training for Your Content in Settings → Privacy (Pro and Team plans only).

**5. Data location.** Your Content is stored with our cloud providers in the United States and may be processed by our sub-processors listed on our website.

**6. Sensitive information.** Do not upload special categories of personal data (such as health information) unless you have the right to do so. You are responsible for any personal data in Your Content.

**9. Deletion.** When you close your account we delete Your Content within 90 days, except copies retained in backups or used in aggregated or de-identified training data.

**12. Governing law.** Delaware, USA.
"""

MICROSOFT = """
# Email to office@ — Microsoft 365 nonprofit subscription notice

*Forwarded by Yossi to Ronit on 15 October 2026 with "?". Paraphrased extract; the original is in English.*

**From:** Microsoft Nonprofits (no-reply)
**Received:** 16 July 2026

Your organization's Microsoft 365 Business Premium **grant** licences (10) will not renew at your next subscription renewal on **14 September 2026**, as part of changes to Microsoft's nonprofit offers announced in 2025. To keep these licences, no action is needed: they will continue at the **discounted nonprofit price** and you will be billed at renewal. To avoid charges, reduce the licence count or move users to Microsoft 365 Business Basic, which remains available as a grant for eligible nonprofits, before the renewal date. Manage licences in the Microsoft 365 admin center.

*Yossi's note on the forward:* "I thought I clicked 'keep' to keep the free ones. Galina saw the charge."
"""

YOSSI = """
# Yossi's IT notes (Google Doc "IT stuff - Open Hands", last edited 2023-05-08, a few lines added since)

- **Google Workspace for Nonprofits** — free since 2019 (applied through the Google for Nonprofits programme). I am the super admin (2FA on my phone). Ronit has the recovery codes in an envelope in the office safe? (check)
- **Gemini / Google AI** — not included for nonprofits, it's paid. (2023)
- **Microsoft** — 10 free Business Premium through the nonprofit grant, renews every September. For Office on Galina's and Ronit's computers.
- **TechSoup Israel** — gives donated software (Office, antivirus). Ask them for Windows licences next time. (2022)
- **New staff**: create Google account, add to the shared drives they need (ask Hana for Families), give a laptop.
- **When someone leaves**: (to do — write this)
- **Volunteers**: Amir adds them to the respite folder with their Gmail. The link is open "for the weekend" — we opened it in Aug 2024 when the Gmail adds didn't work at the Nahariya weekend. Close it? (added 2024)
- **Backups**: everything is in Drive. Dropbox has the old photo archive (moved to Drive May 2024; cancel Dropbox).
- **Passwords**: in my notebook and in the browser.
- Noa asked about ChatGPT Team, too expensive, she uses her own. (2026)
"""


def write(f: dict) -> None:
    lib = ROOM / "fundraising" / "grant-library"
    write_md(lib / "boilerplate-2025.md", BOILERPLATE)
    write_md(lib / "adler-haddad-quarterly-template.md", TEMPLATE)
    write_md(lib / "adler-haddad-q3-2026-report-extract.md",
             fill(Q3_REPORT, dict(ah=f["ah_families"], rest=f["ah_families"] - 3)))
    write_md(lib / "outcomes-framework-2024.md", FRAMEWORK)
    write_md(ROOM / "comms" / "newsletter-2026-09.md", fill(NEWSLETTER, dict(subs="1,630")))
    write_md(ROOM / "vendor" / "grantgenie-terms-extract.md", GRANTGENIE)
    write_md(ROOM / "vendor" / "microsoft-renewal-notice.md", MICROSOFT)
    write_md(ROOM / "it" / "yossi-it-notes.md", YOSSI)
