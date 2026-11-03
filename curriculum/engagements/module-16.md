# Open Hands — writer's notes for module 16 (never imported)

The ninth Stage 2 engagement and the smallest organization in the course. The learner is a **pro bono
volunteer consultant**: no fee, no authority, no budget, **40 hours over four weeks**. The stated ask is
"help us use AI, we have no budget". The hard part (16.4) is **compression**: running the whole method
in four weeks with free or very cheap tools, around sensitive data about disabled children and their
families, with one person who "does IT" one day a week. 16.5 builds a **grant-writing workflow**, a
**case-notes workflow** with an explicit data boundary, and **the whole policy pack on one page**.

The data room is built by `labs/module-16/data-room/generate.py` (seed 20261115, standard library only).
The ground truth is only in this file. Never link it from lessons. `python generate.py --facts` prints
every computed number below.

## The organization

- **Open Hands** (עמותת ידיים פתוחות (ע"ר)), an Israeli amuta founded in 2008 by three parents in Kiryat
  Ata. Office in Kiryat Ata, a satellite room in Shefa-'Amr. Supports **families raising children and
  young people (0–21) with disabilities**: family coordination by social workers (rights and services:
  National Insurance disabled-child benefit, placement committees, welfare services), parent groups
  (Hebrew, Arabic, Russian, Amharic), respite weekends run with volunteers, a siblings' programme, a
  rights hotline. Families come from Haifa Bay towns (Haifa, Kiryat Ata, Kiryat Bialik, Kiryat Motzkin,
  Acre, Shefa-'Amr, Tamra, Nesher) and the fictional town of **Kiryat Hadas** (whose municipal welfare
  department refers families under a service agreement).
- **30 people on staff (≈ 20 FTE)**, about 140 volunteers on the list (≈ 95 active), ≈ 440 active
  families, ≈ 1,130 donors. 2026 budget ₪6.12M: foundations and funds ₪2.51M, 41% (12 funders), Ministry of
  Welfare support 15%, the Kiryat Hadas service agreement 10%, individual donors 20% (Israel and an American
  Friends organization), events and other 13%. Holds a Section 46 approval and a proper-management
  certificate (2026, received June).
- **IT:** Google Workspace for Nonprofits since 2019 (free); 10 Microsoft 365 Business Premium seats from
  the old Microsoft grant (desktop Office); Zoom, Mailchimp, a website builder, a receipts system that
  reports donations to the Tax Authority's digital system (mandatory since 1 January 2026). No IT
  department: **Yossi Mizrahi**, office and operations manager, does IT one day a week; he is the only
  Workspace super-admin and his 2FA is on his personal phone.
- Domain: `openhands-amuta.org.il` (fictional).

## Who the learner is

A **pro bono volunteer consultant** matched by a (fictional) pro bono programme, *Mahut Pro Bono*.
Commitment: **40 hours over four weeks**, Sunday 15 November – Thursday 10 December 2026 (12 / 10 / 10 /
8 hours). No fee; Open Hands pays nothing; the ED may spend up to ₪3,000 a year on software without the
board; any recurring charge needs the treasurer. Reports to **Dr. Ronit Azoulay**, executive director.
Readout: the board's Zoom meeting, **Wednesday 9 December, 19:30**, a 20-minute slot. Handover to Yossi
and Ronit on Thursday 10 December.

What changes for a pro bono volunteer (16.1, pointing to 01.1): no authority and no money, so influence
comes from usefulness in week 1; no contract to protect you or them, so write a one-page charter anyway;
your hours are the scarcest resource, so every step is sized in hours; the organization's people are
stretched and some are volunteers too; you leave on a date and **nobody there can maintain anything you
build** unless Yossi can, in his one day a week; the people affected are children and families who never
asked for AI.

## Stated ask vs hidden truth

- **Stated ask (board, 27 October 2026; the chair back from a conference):** "Every nonprofit uses AI
  now. Help us use AI. We have no budget." Ronit's version on the call: "Show us how to use the free
  tools for grants and paperwork, so my social workers spend time with families, not with reports."
- **Hidden truth.** Open Hands does not have an AI *adoption* problem; it has an AI *already-in-use*
  problem with the most sensitive data it holds, and a writing workload created mostly by **one funder's
  template**.
  1. **AI is already used with family data, in personal accounts.** Two coordinators (Samah, and Marina
     per the survey) paste case notes into their personal Gemini/ChatGPT to rewrite them into the
     funder's narrative format and to translate letters to families; Noa (development) pays ChatGPT Plus
     on the organization's card and uploaded the donor sheet to segment the Giving Tuesday campaign; Noa
     also signed up for "GrantGenie" (fictional AI grant tool) with her personal email and uploaded
     past proposals and the Adler-Haddad reports; Ronit herself drafted the September newsletter story
     with ChatGPT from a coordinator's notes. Consumer accounts may be human-reviewed and kept (Gemini:
     reviewed chats up to three years).
  2. **Access control predates AI and is the real exposure.** The `Families` shared drive has 46
     accounts (11 staff who need it or not, 2 national-service volunteers, 2 former staff, 31 personal accounts incl. 23
     inactive volunteers); its `Respite 2026` sub-folder (child care sheets: medication, allergies,
     behaviour plans) has had **"anyone with the link can view"** since a respite weekend in August 2024.
     The donor sheet has 14 editors, 5 of them personal Gmail accounts (3 phone-a-thon volunteers, the treasurer, a former staff member), holds
     ID numbers for most donors (needed for the Tax Authority digital receipts since January 2026), and
     its notes column records the disability of donors' own children. Two former staff accounts are still
     active.
  3. **One funder's template drives most of the writing.** The Adler-Haddad Family Foundation (₪870,000
     a year, 34.7% of foundation income) requires a quarterly English report with a **per-family outcome
     narrative for every family served under the grant (≈ 120)**. In the report week the six coordinators
     spend ≈ 6.5 hours each on it; the development team consolidates and translates. The programme
     officer designed the template for a large grantee, finds the narratives repetitive and over-sharing,
     and would accept Open Hands' own (unused) 2024 outcomes framework plus six consented stories a
     quarter, **if asked**. Nobody has asked.
  4. **Consent does not cover what is done.** 67% of active families are on consent v1 (2019), which
     allows "anonymised information in reports to funders" but not stories, photos or newsletters. The
     September newsletter told Adam's story (rare syndrome + town + school + first name) — his mother,
     Lina Mansour (consent v1), recognised it from a neighbour. The Q3 Adler-Haddad report has first
     names, towns and diagnoses.
  5. **There is money.** "No budget" is false: Open Hands already spends or is committed to ≈ ₪4,500 a
     year on software it barely uses or should not use: the Microsoft grant ended at the September
     renewal and 10 Business Premium seats were renewed at the nonprofit price (US$660, ₪2,070, card,
     14 Oct 2026) with 3 used in the last 90 days; ChatGPT Plus on the card since March (US$20/month);
     GrantGenie converts to US$49/month on 1 January 2027 unless cancelled; Dropbox Plus nobody has used
     since 2024.
- **The honest answer (expert path):** week 1, close the exposures in an afternoon (link sharing off,
  inactive volunteers removed, `Families` restricted to the nine people who need it, which also brings
  the case database within the "no more than ten authorized users" condition for the basic security
  level — a counsel question, not the consultant's conclusion; donor sheet to four editors, ID numbers in
  a separate restricted sheet, notes column cleaned; second super-admin; ex-staff accounts suspended);
  stop personal-account use with family data the same week and give people a sanctioned alternative the
  same day (the organization's own Workspace accounts, Gemini app and NotebookLM, which come free with
  Workspace for Nonprofits under Workspace data protections). Ronit calls the programme officer about the
  template (week 2). Build two workflows on the free tools with a one-page policy pack. Cancel GrantGenie
  and Dropbox, reduce Microsoft to the 3 seats used, stop ChatGPT Plus on the card: the saving (≈ ₪4,500
  a year, of which ≈ ₪2,650 is money already being spent) pays for two nonprofit ChatGPT Business or Claude Team seats for development *if* the free tier
  turns out insufficient after three months (decision in March, not now). Consent v2 for stories,
  re-consent at the next contact, an apology to Lina's family in Arabic from Ronit. Questions to pro bono
  counsel: security level, the Kiryat Hadas agreement (holder for a public body → DPO duty?), social
  workers' confidentiality vs AI tools, the newsletter.

## Planted findings (each discoverable, never stated)

| # | Finding | Where |
|---|---|---|
| 1 | Family data in personal AI accounts | `it/staff-ai-survey-2026-10.csv` (3 "yes, with details", 4 "prefer not to say"), `finance/card-statement-2026.csv` (OpenAI), Samah, Noa, Ronit personas |
| 2 | `Respite 2026` link sharing "anyone with the link" since Aug 2024 | `it/drive-sharing-audit.csv` |
| 3 | 23 inactive volunteers still have access; 19 volunteers with access never signed confidentiality | `people/volunteers.csv` × `it/drive-sharing-audit.csv` |
| 4 | Donor sheet: 14 editors (3 personal), ID numbers on file, disability notes | `it/drive-sharing-audit.csv`, `fundraising/donors.csv` |
| 5 | Case database has 46 authorized accounts; nine need it | `it/drive-sharing-audit.csv`, `people/staff.csv` (roles) |
| 6 | Microsoft grant ended at renewal; 10 paid seats, 3 used | `finance/card-statement-2026.csv`, `it/accounts-and-licences.csv`, `vendor/microsoft-renewal-notice.md`, board minutes |
| 7 | GrantGenie: personal sign-up, content licence, auto-converts 1 Jan 2027 | `vendor/grantgenie-terms-extract.md`, `it/accounts-and-licences.csv`, card statement (US$0 authorisation) |
| 8 | One funder's template drives the writing | `fundraising/funders.csv`, `people/time-log-2026-10.csv`, `fundraising/grant-library/adler-haddad-quarterly-template.md` |
| 9 | Consent v1 does not cover stories; newsletter used a v1 family's identifiable story | `policies/consent-form-v1-2019.md`, `cases/case-register.csv`, `comms/newsletter-2026-09.md` |
| 10 | Q3 funder report over-shares (names, towns, diagnoses) | `fundraising/grant-library/adler-haddad-q3-2026-report-extract.md` |
| 11 | Privacy policy on paper only (registration number, "only coordinators access") | `policies/privacy-and-confidentiality-policy-2019.md` vs the audit |
| 12 | Volunteers' WhatsApp groups carry medication lists | `policies/volunteer-handbook-extract.md`, Etti persona |
| 13 | Kiryat Hadas agreement: Open Hands processes referral data for a public body | `policies/municipal-service-agreement-extract.md` |
| 14 | Missing baseline: one week logged, the report-crunch week; "half my week" claim | `people/time-log-2026-10.csv`, `company/board-minutes-2026-10.md` |
| 15 | IT single point of failure: one super-admin, 2FA on a personal phone; two ex-staff accounts active | `it/yossi-it-notes.md`, `it/accounts-and-licences.csv` |
| 16 | Yossi's notes on nonprofit offers are stale (TechSoup Israel, "Gemini not included") | `it/yossi-it-notes.md` (learner verifies in 16.4) |
| 17 | "Pseudonymised" case-notes export leaks identifiers in some notes | `cases/case-notes-sample.csv` |
| 18 | Own outcomes framework (2024) exists and nobody reports with it | `fundraising/grant-library/outcomes-framework-2024.md` |

## The cast (persona pack)

| Persona | Role | Type | Hidden / unlock |
|---|---|---|---|
| Dr. Ronit Azoulay | Executive director | Sponsor | Drafted the newsletter story with ChatGPT from Samah's notes; the Adler-Haddad Q3 report was 9 days late and the renewal (31 Jan) worries her; the chair pushed AI. Unlock: ask how the newsletter is written; ask which funder she fears losing |
| Noa Ben-Ami | Head of development | Secret enthusiast | ChatGPT Plus on the card; uploaded the donor sheet (with notes) to segment Giving Tuesday; GrantGenie with personal email. Unlock: ask to be shown how she prepared the Giving Tuesday segments / how she writes a proposal, not whether she uses AI |
| Samah Khatib | Senior family coordinator, Arabic desk | Frontline (social worker) | Pastes notes into personal Gemini to produce the English narratives and Arabic letters; writes reports at night; two weeks a quarter. Unlock: non-attribution + ask her to walk through the last quarterly report |
| Yossi Mizrahi | Office and operations manager, "IT" | IT, data steward | Knows about the link sharing ("for one weekend"), no offboarding, the Microsoft renewal email he clicked; only super-admin. Unlock: ask what happens when a volunteer leaves / who else can get into the admin console |
| Vladimir (Vova) Gorelik | Board treasurer | Finance, sceptic | Will fund ₪2,500 if it is one line and kills waste; had a breach at his old company; the Microsoft charge annoys him. Unlock: show money found; ask what would worry him most |
| Etti Peretz | Long-time volunteer (respite weekends) | Volunteer / receiving team | WhatsApp groups with medication lists and photos; uses her personal Gmail in Families. Unlock: ask how volunteers know what each child needs on a weekend |
| Lina Mansour | Mother of Adam (9), family since 2021 | The person affected | Recognised Adam's story; not against technology; wants to be asked and to see the text; wants letters in Arabic. Unlock: let her tell it; ask what would have made it OK |
| Tamar Weiss-Levi | Programme officer, Adler-Haddad Family Foundation | Funder | The template was designed for a large grantee; she would accept the outcomes framework + six consented stories; foundation drafting its own AI rule for grantees; noticed "ChatGPT-sounding" narratives with too much detail. Unlock: ask what she actually uses the report for |

Transcripts leave hidden: Ronit's newsletter drafting; Noa's donor-sheet upload; Samah's two weeks a
quarter (the interviewer gets "a lot of evenings" but not the count); Yossi's 2FA on his phone; Vova's
₪2,500; Etti's photos in the groups; Lina's willingness to have a story told with approval; Tamar's
foundation AI rule.

## Timeline

- Data: case register as of 12 Nov 2026; Drive sharing audit exported 12 Nov; card statement
  Jan–Oct 2026; time log Sun 4 – Thu 8 Oct 2026 (the week before the Q3 Adler-Haddad report was due on 15
  Oct; it went on 24 Oct); staff AI survey 26 Oct 2026 (22 of 30 answered; volunteers not asked).
- 27 Oct board ("help us use AI, no budget"; treasurer's ₪2,070 question). Tue 10 Nov the call. Sun 15
  Nov start (16.1). 15–19 Nov discovery (16.2; Lina 19 Nov at the Shefa-'Amr room). Week 2 (22–26 Nov)
  diagnosis and the hard part (16.3, 16.4): respite link closed Wed 18 Nov (same-day note); the afternoon fix Tue 24 Nov with Yossi; Ronit calls Tamar
  Wed 25 Nov. Week 3 (29 Nov – 3 Dec) build (16.5); Giving Tuesday 1 Dec. Hanukkah from the evening of
  Fri 4 Dec; family party Mon 7 Dec. Wed 9 Dec board readout (16.6); Thu 10 Dec handover. Adler-Haddad
  Q4 report due 15 Jan 2027; renewal proposal due 31 Jan 2027. GrantGenie converts 1 Jan 2027.
- Six months later: June 2027.

## The futures (16.6 debrief)

1. **Tools first.** The board likes a demo; Noa's GrantGenie is "free for a year", so it becomes the
   grant tool; coordinators get "use Gemini, but anonymise" with no access fix and no sanctioned account.
   January: GrantGenie converts; nobody notices until March (US$147). In April a former volunteer's
   account (still on `Families`) is phished; the child care sheets were readable by link anyway. The PPA
   receives a complaint from a parent; Open Hands cannot say who had access. The Adler-Haddad renewal is
   approved but with a condition: a data-protection review at Open Hands' cost (₪18,000). Coordinators
   stop using anything; the writing load is unchanged.
2. **Boundary first, then two workflows (the expert path).** Access fixed on 24 November; personal-account
   use stopped with the Workspace alternative the same day; Tamar agrees in December to a shorter Q4
   report (outcomes framework + six consented stories), confirmed for 2027 in the renewal. Coordinators'
   report time in the January crunch: ≈ 2 hours each instead of ≈ 6.5. The case-notes workflow is used by
   four of six coordinators by March (structure and Arabic/Russian letters, de-identified input, the
   coordinator signs); two prefer to write notes as before, which is fine. GrantGenie cancelled; Microsoft
   at 3 seats; two ChatGPT Business nonprofit seats bought in March after the free tier's limits bit for
   development (the treasurer approved one line, paid for by the savings). Consent v2 at re-contact: 71%
   of families by June. Lina agrees to a story she approved, in Arabic and English. Yossi runs a
   15-minute monthly access check.
3. **Policy only.** The board adopts a five-page AI policy drafted from a template; nothing changes in
   Drive; people keep using personal accounts "carefully"; the template conversation never happens. The
   policy is signed by every staff member and read by none. Nothing bad happens by June — which the board
   takes as proof it worked. (The exposure is unchanged; the debrief asks the learner what they would
   measure to tell future 3 from future 2.)

## Where each finding is planted (actual numbers)

Filled from `python generate.py --facts` after generation (seed 20261115). Paths relative to
`labs/module-16/data-room/`.

**Volumes.** `cases/case-register.csv` 438 families (home language he 197, ar 138, ru 62, am 27, en 14);
`people/staff.csv` 30 (19.4 FTE); `people/volunteers.csv` 142 (91 active); `fundraising/donors.csv` 1,134;
`cases/case-notes-sample.csv` 60 (he 21, ar 22, ru 6, en 11); `people/time-log-2026-10.csv` 367 entries;
`it/drive-sharing-audit.csv` 151 rows; `finance/card-statement-2026.csv` 104; `it/staff-ai-survey-2026-10.csv` 22.

1. **Shadow AI with family data.** Survey: 22 of 30 answered; 18 use AI; account among users: personal 11,
   both 4, don't know 2, work 1; pasted family information: "yes, with details" 3, "prefer not to say" 4,
   "yes, anonymised" 4, no 11. Card: OpenAI US$20 × 8 months (Mar–Oct) = ₪511.78, coded "Office supplies".
2. **Respite link.** 10 items open to "anyone with the link": the respite folder (since 2024-08-14), its 8
   care sheets, and `Volunteers/Volunteer list 2026.gsheet` (since 2025-05-07).
3. **Volunteers.** 38 volunteers have some access (31 at the top of `Families`, 37 on the respite folder);
   23 of them inactive; 21 of the 38 have no confidentiality form on file.
4. **Donor sheet.** 14 editors: 9 org accounts (incl. both national-service volunteers), 5 personal (3
   phone-a-thon volunteers, Vova's Gmail, Moshe Amar's private Gmail — former staff); plus "anyone at the
   domain with the link: editor". ID number on file 851 of 1,134 (75.0%). Notes filled 166; 37 reveal a
   child in the programme, a diagnosis, welfare or bereavement.
5. **Case database users.** `Families` shared drive: 46 accounts = 13 org (11 staff + 2 national service) +
   2 former staff + 31 personal. Roles that need case files: 9 (6 coordinators, Hana, Eli, Sveta). The Data
   Security Regulations' First Schedule item 2(2) puts a database with medical information at the basic
   level when "the number of authorized users … does not exceed ten" (PPA translation; Hebrew "אחד מאלה",
   one of these conditions). 46 → medium; 9 → arguably basic. **Counsel question**, not the consultant's call.
6. **Microsoft.** 10 Premium seats; signed in since 14 Aug: 3 (Ronit, Noa, Galina); 2 seats assigned to
   former staff; 2 never. Charge 14 Oct US$660 = ₪2,071.74. 7 unused seats = US$462 = ₪1,449 a year.
7. **GrantGenie.** Personal email; "Nonprofit Free Year" ends 31 Dec 2026 → US$49/month (₪1,844 a year);
   §4 licence to train on content; US storage; 23 documents uploaded (accounts list) incl. AH Q2/Q3 reports
   (Noa persona).
8. **The template.** Funders' estimate: report hours 570 a year, of which Adler-Haddad 360 (63.2%);
   proposals 223. Log week: Adler-Haddad 57.8 h across everyone; coordinators 37.8 h (6.3 each; Samah 7.5;
   18.7% of their 201.8 h); Hana 5, Shira 7, Noa 5.5, Ronit 2.5. With "two weeks a quarter" (Samah):
   57.8 × 2 × 4 ≈ 462 h a year against development's 360. Coordinators' direct family time in that week
   86.5 h (42.9%); case notes 28.5 h (4.8 each, 14.1%); translation 6.5 h.
9. **Consent.** v1 292 (66.7%), v2 102, missing 44; v2 with stories = y 53. Under the AH grant: 120
   families — v2 62, v1 52, missing 6. Adam = OH-F0217 (v1, Shefa-'Amr, genetic syndrome, Samah).
10. **Q3 report** narratives 1–3 name the child, age, town, diagnosis and coordinator.
14. **"Half my week".** Noa logged 21.5 of 42.0 h on funder writing (51.2%) in the crunch week; reports
    only 12.0 h (28.6%); she says a normal week is about a third.
17. **Notes leaks.** 9 planted identifiers: N001 (street + "the only Ethiopian-Israeli family"), N025
    (Arabic first name, كريم), N026 (Hebrew first name, נועם), N027 (ID + hospital), N030 (email), N042
    (school + "the only pupil"), N046 (phone), N054 (ID), N060 (full Latin name). `build/deid_check.py`
    flags 7 of 60 notes and misses N025 and N026 (native-script names). Note-writing time: mean 18.4 min
    (phone 14.0, home visit 23.2).
- **Money.** Software on the cards Jan–Oct: Mailchimp ₪2,510.74, Microsoft ₪2,071.74, Kabala ₪1,490.00, Wix
  ₪1,190.00, Zoom ₪1,029.42, OpenAI ₪511.78, Dropbox ₪385.97 = ₪9,189.65 (the "Software" category alone
  ₪8,677.87 because OpenAI is coded office supplies). Avoidable a year at ₪3.136/US$: Microsoft 7 seats
  ₪1,449 + ChatGPT Plus ₪753 + Dropbox ₪451 + GrantGenie ₪1,844 = **₪4,497** (₪2,653 current spend, ₪1,844
  future). Two ChatGPT Business nonprofit seats (US$8/user/month annual) = US$192 = ₪602 a year.
- **Donations** 2026 to 31 Oct ₪1,095,010 (2025: ₪993,670).

**Verified nonprofit offers (3 November 2026).** Google for Nonprofits: Israel eligible (amuta, amuta with
proper-management certificate, PBF etc.), verification by Goodstack; Workspace for Nonprofits no cost up to
2,000 users with the Gemini app and NotebookLM; Gemini in Gmail/Docs not in the no-cost edition; paid
editions 70–75%+ off (page updated 2026-10-26). Workspace privacy hub (updated 6 Oct 2026): no training
without permission, Gemini app chats and NotebookLM not human-reviewed (qualifying editions). Consumer
Gemini: activity used to improve services incl. training when Keep Activity is on; reviewed chats kept up to
three years. Microsoft: Business Basic grant up to 300 users with Copilot Chat; Business Premium US$5.50
/user/month annual; Copilot add-on US$25.50; Premium/E1 grants retired at first renewal on or after 1 July
2025 (secondary). OpenAI: ChatGPT Business US$8/user/month annual (US$10 monthly) via Goodstack; Enterprise
up to 75% off (Goodstack page; OpenAI help 403). Anthropic: Claude for Nonprofits (2 Dec 2025) up to 75% off
Team and Enterprise, Goodstack, excludes government, higher ed, healthcare systems. TechSoup Israel:
current partner not confirmed (2019 list: Rashi Foundation) — ⚠️ manual check.
