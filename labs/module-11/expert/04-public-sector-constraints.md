# 04 · Public-sector constraints: what they mean for a resident-facing assistant

For the director-general, Thursday 7 January 2027. Head of Digital Services, after meeting the legal
adviser (21 December), the works committee (23 December) and CivicTalk (28 December). Every legal
statement below is attributed to its source or to the legal adviser's preliminary view; nothing here
is a legal opinion. Not legal advice.

## The answer first

None of the constraints forbids an assistant. Together they decide its **shape**: built and tested
inside first, for agents; content the city owns and dates; answers that cite their source and refuse
individual decisions; Arabic as good as Hebrew; a public register entry; a procurement route chosen
before any vendor gets data; and the works committee consulted before 106's work changes. A public
chatbot on 4 February fails five of the eight constraints below.

## Constraints map

| Constraint | Source (checked 2 November 2026) | What it means for us | Owner | Status |
|---|---|---|---|---|
| **Procurement** | Municipalities Ordinance s.197 (tender) and s.203 (commitments signed by mayor and treasurer); Municipalities (Tenders) Regulations, 5748-1987, regs 2, 3, 8 (amounts indexed monthly; Oct 2021: ₪145,500 and ₪710,600; exemptions incl. 3(4) sole supplier, 3(8) special expertise, 3(15) company of local authorities) | The internal test is a small purchase with price quotes (treasurer to confirm the current amount). A production assistant is a contract above the thresholds: tender, or a recorded exemption the legal adviser approves. No framework covers chatbots (catalogue, Oct 2026) | Treasurer; legal adviser | Legal adviser's note on CivicTalk sent 24 Dec |
| **The "free pilot"** | Legal adviser, preliminary view, 21 Dec; procurement procedure §5 | Free for 90 days then ₪14,500 a month for 36 months (₪522,000 + VAT) is not free; nobody with authority agreed; a supplier with our data and a head start raises equal treatment for a future tender | Legal adviser | CivicTalk told in writing that nothing is agreed; asked to delete the crawl |
| **Freedom of information** | Freedom of Information Law, 5758-1998: local authorities are public authorities (s.2); administrative guidelines that matter to the public available for inspection (s.6); 30 days, extendable (s.7) | Write everything as if published. The September answer ("no AI") must be corrected. Open: whether an assistant's answers are "guidelines" the public may rely on | Legal adviser; FOI officer | Correction sent 31 Dec |
| **Reasons for decisions** | Administrative Procedure Amendment (Decisions and Reasons) Law, 5719-1958: applies to local-authority employees; written answer within 45 days; reasons for a refusal in writing (ss. 2, 2A); burden on the authority if not (s.6) | R-07 letters ("section 3") are the opposite of a usable reason. The assistant never explains an individual decision: it routes to the department, which must give reasons | Eli Saban | Letter templates rewritten (C) |
| **Accessibility** | Equal Rights for Persons with Disabilities (Service Accessibility Adjustments) Regulations, 5773-2013, reg. 35 ff.: website at IS 5568 level AA (35A(a)); documents and forms (35A(c)); accessibility statement (35E). Kol Zchut (updated 1 Nov 2026): local authorities included; compensation up to ₪50,000 without proof of damage | Any widget is part of the site and must be accessible; CivicTalk's is self-declared. Our statement (2021) claims "all pages and documents" and is wrong (2023 audit: 22 open, 23 scanned forms) | Natalie Weiss (coordinator) | Statement corrected; widget audit a tender requirement |
| **Languages** | Basic Law: Israel as the Nation-State of the Jewish People (2018), s.4: Hebrew the state language; Arabic special status; status in practice before the law not harmed. HCJ 4112/99 Adalah v. Tel Aviv-Jaffa (2002): Arabic required on municipal signs in mixed cities | Legal adviser: he will not sign off a service "in every language" that serves Arabic speakers worse than Hebrew speakers. Gate: Arabic results within 5 points of Hebrew; Amharic routed to a person until tested | Legal adviser; Orna Ziv | Gate in the charter |
| **Wrong-advice risk** | NYC's MyCity chatbot (The Markup, 29 Mar 2024): advised businesses contrary to city law; disclaimer added; shut down Feb 2026 ("functionally unusable", The Markup, 30 Jan 2026). Moffatt v. Air Canada (2024 BCCRT 149) for "who is speaking" | A disclaimer does not make a wrong answer right. Design: answers only from the owned pack; source cited; refuses exempt-works, individual and legal questions; Moked agents first | Me; content owners | Rule of use in the charter |
| **Privacy** | Privacy Protection Law, 5741-1981 incl. Amendment 13 (in force Aug 2025); Data Security Regulations 2017; city procedure IS-07 | No personal data in the assistant's sources; the assistant does not look up anyone; logs kept on our tenant only; Ruti's platform held IDs and phone numbers | CISO (Moran Elkayam) | Ruti off 14 Dec; log exported; deletion requested from the platform |
| **Workers** | 2019 local agreement on Moked 106 (cl. 7 consultation, cl. 8 six hours' training); labour-court case law on consultation in unionised workplaces (Barnea, client update, 2015); collective agreements | Inform and consult in writing before changing agents' work; no individual monitoring by the tool; training. Layoffs and grades are the DG's to discuss, not mine | Director-general; HR | DG letter to Moshe sent 29 Dec |
| **Government guidance** | National Digital Agency, "Guide to the responsible use of AI in the public sector", v1.0, May 2026 (with the Ministry of Justice): traffic-light tracks, a blue track for controlled experiments, public transparency, end-user rules (no protected information in third-party tools) | Written for public-sector entities; not binding on us as far as I found, but the best available standard: the internal test is yellow track; a public pilot is blue track with metrics, duration and reporting | Director-general (as our "Chief AI Officer" until one is named) | Adopted for this project |

The EU AI Act does not reach a municipality serving its residents; Israel signed the Council of
Europe's Framework Convention on AI on 5 September 2024 and has not ratified it (Digital Agency guide).
NIST AI RMF is a useful checklist, nothing more here.

## Questions sent to the legal adviser (in writing, 18 December)

1. Is an internal test with model usage bought by price quotes a tender matter? *Answer 21 Dec (prelim.):
   no, if below the reg. 3(3) amount; check the current figure.*
2. What exactly did CivicTalk receive and what binds us? *Note sent 24 Dec.*
3. Must a public assistant answer in Arabic as well as Hebrew? *Prelim.: he will not sign off a
   service that serves Arabic worse.*
4. Is an assistant's answer an administrative guideline under FOI s.6? Can a resident rely on it?
   *Open; "don't design anything that assumes either answer".*
5. Can we publish a register entry, and what must it say? *Yes; comments within 5 working days.*

## Vendor claim read-back (CivicTalk, 28 December)

| Claim | Conditions | Read-back |
|---|---|---|
| "Trusted by 30 authorities" | Customers of any product (mostly forms) | Ask for chatbot customers live today, with references |
| "94% accuracy" | Not disclosed in the meeting | Not evidence until we know who wrote and scored the questions, in which languages |
| Arabic and Russian | Old pages used if they exist, else machine translation of Hebrew | On our site today: the 2023 Arabic pages win. Fails our language gate by design |
| "WCAG compliant" | Self-declared | Ask for an external audit report |
| "In the framework, no tender" | FW-21/2024 is forms and payments | Not a route for a chatbot |
| Paid PoC on our questions, ≈ ₪38,000 | Offered when asked | A fair test; but only through a procurement route, and only after our own test shows what to ask |

## The procurement route I recommend

1. **Now – February:** internal test on our Microsoft tenant; model usage through the existing cloud
   account by price quotes (treasurer); no vendor.
2. **March:** a public request for information (RFI) with our test set's design (not the questions),
   our gates and our language requirements; every supplier gets the same information.
3. **May:** a tender for a production assistant if the internal pilot passes: the eval gates as the
   specification, an accessibility audit of the widget, data residency and no training on our data,
   content ownership by the city, exit and export of everything.

## Works committee: what was agreed to put in writing (DG's letter, 29 December)

The test measures answers, not agents; no individual monitoring; six hours' paid training before any
use; the committee informed before each stage and invited to the forum item on 106; questions of
positions and grades discussed with the DG and HR, not decided by this project.
