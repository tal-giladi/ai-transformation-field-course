"""Policies, consent forms, the volunteer handbook and the municipal service agreement."""
from __future__ import annotations

from common import ROOM, write_md

PRIVACY = """
# Privacy and confidentiality policy

*Open Hands (ע"ר). Approved by the board on 12 March 2019. Next review: March 2020.*

## 1. Purpose

Families trust us with the most private parts of their lives. This policy sets out how we protect the information they give us, as required by the Privacy Protection Law, 5741-1981, and the professional ethics of social work.

## 2. Our database

Open Hands keeps one database of family information, registered with the Registrar of Databases (registration no. 700418562). The database owner is the amuta; the person responsible is the executive director.

## 3. Who may see family information

- Only the family coordinators and the head of family services have access to family files.
- The executive director may see family files when needed for management.
- Volunteers receive only the information needed for a respite weekend (allergies, medication, how to calm the child), on paper, and return it at the end of the weekend.
- Interns and national-service volunteers do not have access to family files.

## 4. How we keep information

- Family files are kept on Google Drive, protected by passwords.
- Paper files are kept in a locked cabinet in the Kiryat Ata office.
- Every staff member and volunteer signs a confidentiality form before starting.

## 5. Sharing

No information about a family is shared outside Open Hands without the family's written consent, except as required by law (for example a report to welfare services about a child at risk) or to obtain the family's rights on its behalf.

## 6. Reports and publicity

Reports to funders contain only anonymised information. Stories in our publications are told only with the family's consent.

## 7. Questions

Questions to the executive director.
"""

CONSENT_V1 = """
# Consent form — version 1 (2019)

*Signed at intake from 2019 until February 2023. Hebrew original; English translation for funders.*

**הסכמה לקבלת ליווי ושיתוף מידע / Consent to support and to sharing information**

I, the undersigned, parent / guardian of ____________, ask Open Hands (ע"ר) to accompany our family, and agree that:

1. Open Hands will collect and keep information about our family and our child, including information about health, development and the services we receive, for the purpose of accompanying us.
2. Open Hands may contact, on our behalf, National Insurance, the Ministry of Welfare, the Ministry of Education, the local authority, health providers and therapists, and share with them the information needed to obtain our rights and services.
3. Open Hands may use anonymised information about our family in reports to funders and to the authorities.
4. I may withdraw this consent at any time by notice to the family coordinator.

Signature ____________ Date ____________

*(The form has no section on stories, photos, the newsletter, social media or digital tools.)*
"""

CONSENT_V2 = """
# Consent form — version 2 (March 2023)

*Signed at intake since March 2023. Hebrew, Arabic, Russian and Amharic versions. English translation.*

**Part A — Support and rights** (required)

1. Open Hands will collect and keep information about our family and our child, including health, development and services, for the purpose of accompanying us.
2. Open Hands may contact, on our behalf, National Insurance, government ministries, the local authority, health providers and therapists, and share with them what is needed to obtain our rights.
3. Open Hands keeps information in cloud services (for example Google Drive) protected by access control. Open Hands does not sell information and does not give it to anyone for advertising.
4. Open Hands may use anonymised and aggregated information (numbers, outcomes) in reports to funders and authorities.

**Part B — Stories and photos** (optional; tick each one)

- [ ] Open Hands may tell our family's story to funders and donors, **after we have read and approved the text**. The story will not include our full names, our town, our child's school or anything that identifies us, unless we agree in writing.
- [ ] Open Hands may use photos of our child in which his or her face can be seen.
- [ ] I agree that the above may appear in the newsletter and on social media.

I may withdraw any consent at any time by notice to the family coordinator.

Signature ____________ Date ____________
"""

HANDBOOK = """
# Volunteer handbook — respite weekends (extract)

*Liat Ohana and Amir Saleh, edition 2022, reprinted 2025.*

## Before the weekend

- Amir opens a **WhatsApp group** for each weekend: the volunteers, the counsellor in charge and Amir. Use your own phone; there are no work phones.
- The **care sheet** for each child (allergies, medication and times, how to calm him or her, what he or she loves) is in the shared folder. The link is pinned in the WhatsApp group. Read it before you arrive.
- If you cannot open the folder, ask Amir to add your Gmail.

## During the weekend

- Medication changes and anything unusual go in the WhatsApp group immediately, with the child's name, so the counsellor sees it.
- You may share photos of the activities in the group so parents (who are added on Saturday afternoon) can see their children are happy.

## After the weekend

- Delete photos from your phone after the parents have received them.
- Leave the group after the weekend. (Amir closes it after a week.)

## Confidentiality

Everything you learn about the families stays with you. Sign the confidentiality form with Liat before your first weekend.
"""

AGREEMENT = """
# Service agreement — Kiryat Hadas municipality and Open Hands (extract)

*Agreement no. KH-WEL-2024-031, signed 4 January 2024, for 2024–2027 with yearly renewal. Clauses relevant to information. Kiryat Hadas is a fictional town.*

**1. Definitions.** "The Municipality" — the Kiryat Hadas municipality, through its Department of Social Services. "The Contractor" — Open Hands (ע"ר). "Referred family" — a family the Department refers to the Contractor on a referral form.

**3. The service.** The Contractor will provide family coordination to referred families with a child with a disability, up to 70 families at a time, and report monthly.

**7. Information.**

7.1 The Department will send the Contractor, for each referred family, a referral form containing identifying details, the family's composition, the child's disability and the welfare services the family receives.

7.2 The Contractor will use the information solely for the purpose of providing the service under this agreement, will keep it confidential, and will not transfer it to any third party without the Municipality's prior written approval, except to the authorities for the purpose of obtaining the family's rights.

7.3 The Contractor will keep the information in accordance with the Privacy Protection Law, 5741-1981, and the regulations under it, including the Privacy Protection (Data Security) Regulations, 5777-2017, and will allow the Municipality to audit its compliance.

7.4 The Contractor will report every security incident involving referred families' information to the Department within 24 hours.

7.5 On the end of the agreement the Contractor will return or delete the information as the Municipality instructs.

**9. Reporting.** By the 5th of each month: an Excel form with the number of contacts per referred family (by family id), the services obtained, and open issues.

*Signed for the Municipality: Director of Social Services; Treasurer. For the Contractor: Dr. Ronit Azoulay; Avi Shalev.*
"""


def write(f: dict) -> None:
    write_md(ROOM / "policies" / "privacy-and-confidentiality-policy-2019.md", PRIVACY)
    write_md(ROOM / "policies" / "consent-form-v1-2019.md", CONSENT_V1)
    write_md(ROOM / "policies" / "consent-form-v2-2023.md", CONSENT_V2)
    write_md(ROOM / "policies" / "volunteer-handbook-extract.md", HANDBOOK)
    write_md(ROOM / "policies" / "municipal-service-agreement-extract.md", AGREEMENT)
