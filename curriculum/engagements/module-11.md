# Givat Oren — writer's notes for module 11 (never imported)

The fourth Stage 2 engagement. The learner is **the accidental owner**: the municipality's Head of
Digital Services, an employee for four years, handed "AI" by the mayor's office with no budget, no
authority over the departments that own the content, and a rule that every purchase goes through the
tender committee. The hard part (11.4) is public-sector constraints: procurement, freedom of
information and transparency, accessibility, languages, wrong-advice risk (the MyCity pattern), the
works committee, and the government's AI guidance. 11.5 is an answer-quality eval of a permit-FAQ
assistant over the municipality's documents in Hebrew, Arabic, Russian and English, with grounded
answers and refusal cases, plus an AI-register entry. The data room is built by
`labs/module-11/data-room/generate.py` (seed 20261129); it also writes the pilot's knowledge pack and
test set in `labs/module-11/pilot/`. Ground truth learners never see is only in this file (section
"Numbers" is filled from the generated files; see the end).

## The organization

- **Givat Oren municipality** (עיריית גבעת אורן; Arabic بلدية جفعات أورن; Russian Муниципалитет
  Гиват-Орена), a fictional mixed city in central Israel, about **221,000 residents** (2025). Home
  languages (2024 residents' survey): Hebrew 58%, Arabic 21% (mainly the al-Zahra and Ein Sara
  neighbourhoods), Russian 13%, Amharic 4%, English 2%, other 2%.
- 2,450 municipal employees (without teachers); regular budget 2026 ₪2.1bn. Mayor (not a persona),
  council of 31. Divisions: Mayor's office; Director-General; Legal adviser; Treasurer; Comptroller
  (also the Public Complaints Commissioner under the 2008 law); Engineering; **Licensing and Permits
  Division** (parking permits, signage, sidewalk cafés, events, skips, building archive, business
  licensing); Sanitation; Parking and Enforcement; Welfare; Education; **Information Systems
  Division** (CIO Dmitri Kogan, CISO under him); **Resident Service Division** (Moked 106 and the
  service centre).
- **Moked 106**, the city hotline: phone (IVR: Hebrew, Arabic, Russian, English, Amharic), WhatsApp,
  web form, app. 24 agents on payroll (3 read and speak Arabic, 4 Russian, 1 Amharic, 2 English),
  about 21 on shift-equivalent. About 21,000 contacts a month.
- Systems (fictional): CRM "Tikshoret" (106 contacts and department tasks), permits system
  "Rishuyit", CMS "SiteBuilder 8" (1,240 pages; Arabic, Russian and English mini-sites maintained by a
  translation vendor, last full refresh 2023).

## Who the learner is, and what changes

**You are Givat Oren's Head of Digital Services** (website, forms, app content; a team of four),
inside the Information Systems Division. On Thursday 26 November 2026 the mayor's chief of staff,
Eyal Ben-Haim, emails: the mayor wants "a citizen chatbot like other cities have", to be launched at
the residents' conference on Thursday 4 February 2027. You are "our digital person".

What changes for the accidental owner (11.1, pointing to 01.1): the mandate came from someone with no
authority to give it (the mayor's office does not run the administration; the director-general does);
you have no budget (your unit's operating budget is ₪420,000 a year for hosting, CMS licence and
accessibility audits; a ₪600,000 "smart chatbot" line is in the draft 2027 budget, not yet approved,
and not yours); you have no authority over the departments that own the content; every purchase is a
requisition, a treasurer's commitment and either a tender or a recorded exemption (Municipalities
Ordinance s.197 and s.203; Municipalities (Tenders) Regulations, 5748-1987); you will still be here
in three years, so you own whatever you launch; and everything you write is potentially public
(Freedom of Information Law). The first move is a mandate from the director-general, not a plan for
the chief of staff.

## Stated ask vs hidden truth

- **Stated ask (chief of staff, for the mayor):** "A citizen chatbot like other cities have", live on
  the website for the residents' conference on 4 February 2027. The chief of staff has already told
  CivicTalk Ltd (fictional vendor) in October to "go ahead with the free pilot" and sent them the
  website address; CivicTalk crawled the site in November.
- **Hidden truth.** Residents do not lack a chatbot; they lack **one correct answer and a usable
  reason**.
  1. **The content is wrong in the languages people use.** The council changed fees and the parking
     permit rule for 2026 (decision 17 December 2025; fees from 1 January 2026; parking procedure v4
     from 1 July 2026: leased and company cars eligible with an employer letter). The Hebrew pages were
     mostly updated; the Arabic, Russian and English pages and two Hebrew pages were not; the 2025 fee
     table PDF is still linked. 40.7% of CMS pages have no named owner. A chatbot over this website
     repeats the old fees and the old leasing rule (the MyCity pattern) — and in Arabic it would mostly
     answer from Hebrew pages.
  2. **Moked 106's "83% first-contact resolution" hides callbacks.** The KPI counts a contact as
     resolved when it is closed, transferred to a department or a callback is scheduled. Callbacks
     promised are completed on time in a minority of cases; residents call again. Repeat contacts on
     the same topic within 14 days are 35% of permit-family contacts (12% for other topics).
  3. **Arabic callers are mostly answered in Hebrew** (3 of 24 agents speak Arabic; the IVR Arabic
     queue overflows to Hebrew after 90 seconds).
  4. **Decision letters give no usable reason.** Parking-permit rejections use reason code R-07 "does
     not meet the criteria in section 3 of the procedure" for most rejections; all letters are in
     Hebrew. After 1 July 2026 the permits desk kept using the 2024 checklist (v3): leased-car
     applications were rejected under the old rule. Amal Nassar (persona) is one of them.
  5. **Shadow AI already talks to residents.** Since March 2026 a business-licensing clerk's free
     chatbot ("Ruti", on the free tier of a no-code bot platform, fictional "BotNest") answers
     residents on the business-licensing pages, from 2024 PDFs; residents type ID numbers into it; it
     answers Arabic in Hebrew. IT did not know. The September 2026 FOI answer to a journalist said
     "the municipality does not use artificial-intelligence systems" (wrong: Ruti; the parking
     enforcement vendor's plate-reading cameras; the translation vendor's machine translation).
  6. **The "free pilot" is a procurement problem**: free for 90 days then ₪14,500 a month + VAT,
     36 months, auto-renew (≈ ₪522,000 over the term) — above the tender threshold; a free pilot by one
     vendor, on the city's data, before any tender, raises equal-treatment questions the legal adviser
     must answer. CivicTalk's claim to be "in the local-authorities framework" is wrong: the framework
     covers digital forms and payments, not chatbots.
- **The honest answer:** no public chatbot on 4 February. Fix the permits-and-fees content (one source
  of truth with named owners and effective dates, in four languages); put a usable reason, the
  missing document and the objection route into every rejection letter, in the resident's language;
  measure callbacks honestly; stop Ruti and correct the FOI answer; build and evaluate an internal
  permit-FAQ assistant for 106 agents (grounded in the approved knowledge pack, cites its source,
  refuses individual decisions and legal questions, routes Amharic to a person); publish an AI-register
  entry; then a limited public pilot (the government guide's "blue track") in June if it passes the
  gates in all four languages; production through a proper procurement route with the eval as the
  specification; agree with the works committee before any change to 106 work. The mayor's sentence
  for 4 February: a **service promise** (your language, a reason in every decision, callbacks within
  two working days, published monthly, and an AI register), with the assistant "in testing, live when
  it passes".

## Planted findings (each discoverable, never stated)

| # | Finding | Where |
|---|---|---|
| 1 | Content in Arabic/Russian/English (and two Hebrew pages) contradicts the 2026 council decision | `content/site/*`, `content/cms-pages.csv`, `city/council-decision-fees-2025-12.md` |
| 2 | 2025 fee table PDF still linked from several pages | `content/cms-pages.csv` (`pdf_links`), `content/site/fee-table-2025.md` |
| 3 | 40.7% of pages have no named owner; Arabic, Russian, English pages mostly unchanged since 2023 | `content/cms-pages.csv` |
| 4 | FCR 83% counts transfers and scheduled callbacks; callbacks late or never | `service/moked-kpi-report-2026-q3.md` footnote, `service/moked-contacts.csv`, `service/callbacks.csv` |
| 5 | Repeat contacts within 14 days, never reported | `service/moked-contacts.csv` |
| 6 | Arabic IVR callers mostly served in Hebrew | `service/moked-contacts.csv` (`ivr_language` vs `served_language`), `service/moked-staffing-2026.csv` |
| 7 | Mystery shopper: fee answers wrong where fees changed; Arabic in Hebrew | `service/mystery-shopper-2026.csv` |
| 8 | R-07 generic reason on most parking rejections; Hebrew-only letters | `permits/applications-2026.csv`, `permits/decision-letter-templates.md` |
| 9 | Clerks' checklist v3 (2024) after procedure v4 (1 Jul 2026): leased cars rejected under the old rule | `permits/parking-permit-checklist-clerks.md` vs `permits/parking-permit-procedure-v4.md`, `permits/applications-2026.csv` |
| 10 | Shadow AI: Ruti, free tier, old PDFs, ID numbers typed, Arabic answered in Hebrew | `chatbot/ruti-bot-log.csv`, `chatbot/ruti-setup-notes.md`, `content/cms-pages.csv` (embed) |
| 11 | FOI answer "no AI" is wrong | `governance/foi-log-2026.csv`, `governance/foi-response-2026-09-ai.md` vs 10 and the vendor list |
| 12 | Accessibility statement claims AA (2021); 2023 audit open items incl. PDF forms; vendor widget self-declared | `governance/accessibility-*.md`, `procurement/civictalk-proposal.md` |
| 13 | "Free pilot" = ₪14,500/month after 90 days, 36 months, auto-renew; framework claim wrong | `procurement/civictalk-proposal.md`, `procurement/email-thread-2026-10.md`, `procurement/framework-catalogue-extract.md` |
| 14 | Works committee letter; 2019 106 agreement has a consultation clause | `hr/works-committee-letter-2026-11-11.md`, `hr/moked-106-agreement-2019-extract.md` |
| 15 | Agents' unofficial fee sheet (2025 fees) | Larisa and Moshe personas only |
| 16 | Tsega translates letters with a personal free chatbot | Tsega persona only |

## The cast

| Persona | Role | Type | Hidden / unlock |
|---|---|---|---|
| Eyal Ben-Haim | Mayor's chief of staff | owner of the ask | Told CivicTalk to go ahead in October; the trigger is a neighbourhood WhatsApp storm and a local-news piece about 106; the mayor wants something to announce, not necessarily a bot. Unlock: what the mayor needs to say on 4 Feb; what was agreed with CivicTalk |
| Dr. Ronit Shemesh | Director-general | sponsor | Comptroller's 2025 draft on 106 callbacks on her desk; will name department content owners only with the mayor's backing; knows the 2019 106 agreement. Unlock: what she is accountable for; what would make the comptroller's finding go away |
| Adv. Samer Haddad | Legal adviser | counsel | Signed the September FOI answer on IT's word; free pilot = equal-treatment problem; open question: is a bot answer an administrative guideline (FOI s.6) and can residents rely on it. Unlock: who checked the FOI answer; what CivicTalk received |
| Larisa Gurevich | Head of Moked 106 | middle manager | FCR definition (83%); callbacks; Arabic overflow after 90 s; agents' 2025 fee sheet; mystery-shopper results not circulated. Unlock: non-attribution + how FCR is counted; "what does an agent look at when a resident asks a fee?" |
| Tsega Mengistu | Senior clerk, permits desk | frontline, secret enthusiast | Uses a free chatbot on her phone to translate letters into Arabic and Amharic; the desk still uses checklist v3; R-07 because the system has eight codes. Unlock: "show me how you answer a resident who reads only Arabic"; leased-car question |
| Moshe Azulay | Works committee chair | union | 106 agents were told in 2024 the digital channel "will cut shifts"; consultation clause; would support if no layoffs, training and a "digital service agent" grade. Unlock: asked first, before any plan is fixed; what agents would need |
| Amal Nassar | Resident, al-Zahra | person affected | Rejected for a parking permit (leased car) in August; three 106 calls, three answers; Ruti said "not eligible"; would accept "no" with the document named; wants the reason in Arabic. Unlock: let her tell it in order; ask what would have made it OK |
| Dmitri Kogan | CIO, head of Information Systems | IT, data steward | Didn't know about Ruti (CMS editors can embed scripts); answered "no AI" for the FOI; 40.7% pages unowned; Arabic site separate; M365 tenant exists, Copilot Studio would be a new licence. Unlock: "who can publish on the site?"; "what did you count as AI?" |
| Liron Avital | Account executive, CivicTalk | vendor AE | Free pilot terms; "30 authorities" = all products, chatbot in 4; benchmark of 200 Hebrew questions from its own FAQ, 94%; knowledge = crawl incl. old pages; Arabic by machine translation; widget accessibility self-declared; framework claim. Unlock: exact conditions; what was crawled |

Transcripts leave hidden: Eyal's October email to CivicTalk; Ronit's comptroller draft; Samer's open
question on reliance; Larisa's fee sheet; Tsega's phone translator; Moshe's 2024 "cut shifts" remark;
Amal's Ruti answer; Dmitri's FOI counting; Liron's benchmark conditions.

## Timeline

- Data: Moked contacts 1 Jun – 31 Oct 2026 (4% caller sample); callbacks for those contacts;
  permit applications 1 Jan – 31 Oct 2026; Ruti log 10 Mar – 31 Oct 2026; FOI log 2026; mystery
  shopper 2 Aug – 24 Sep 2026.
- 17 Dec 2025 council fee decision; 1 Jan 2026 fees; 10 Mar 2026 Ruti live; 1 Jul 2026 parking
  procedure v4; 14 Sep 2026 FOI answer "no AI"; Oct 2026 chief of staff ↔ CivicTalk emails; 11 Nov
  works committee letter; Thu 26 Nov the ask.
- Sun 29 Nov 11.1 (mandate memo; DG Mon 30 Nov); 30 Nov – 10 Dec 11.2 (Amal Tue 8 Dec); 13–17 Dec
  11.3 (one-page case to the DG Thu 17 Dec); Tue 22 Dec budget council (the ₪600,000 line);
  20 Dec – 7 Jan 11.4 (Samer 21 Dec, Moshe 23 Dec, Liron 28 Dec; constraints paper 7 Jan);
  10–28 Jan 11.5 (knowledge pack v1 signed by owners 14 Jan; eval report 28 Jan); Tue 2 Feb 2027
  management forum (11.6); Thu 4 Feb residents' conference. Six months later: August 2027.

## The futures (11.6 debrief)

1. **Launch for the conference.** CivicTalk's "free pilot" goes live on 4 February over the crawled
   website. Within three weeks an Arabic news site posts screenshots: the bot quotes 2025 parking fees
   in Arabic and tells a resident a leased car is not eligible; another tells a café owner the old
   fee. A competing vendor writes to the tender committee about a free pilot that turned into a
   ₪14,500-a-month commitment. The legal adviser freezes the bot on 12 April; 106 calls rise because
   residents call to check the bot. The works committee stops voluntary overtime in March. The
   comptroller's annual report (published in the summer) has a chapter on it.
2. **Content and reasons first, assistant behind the agents (the expert path).** The mayor announces
   the service promise on 4 February. Knowledge pack v1 (14 January) becomes the site's permits
   section in all four languages by 1 March with named owners; rejection letters carry the reason, the
   missing document and the objection route, in Arabic and Russian too; callbacks are measured on
   completion. The internal assistant goes to 106 agents in shadow mode in February, live in March
   (Hebrew, Arabic, Russian, English); the AI-register entry is published on 1 March; Ruti is switched
   off on 14 December and its log deleted from the platform after export; the FOI answer is corrected.
   A public "permits FAQ" pilot opens on 15 June after a second eval, with the source cited under every
   answer. Production is tendered in May with the eval as the specification. By August: permit-family
   repeat contacts −27%, callbacks completed on time 84%, Arabic callers served in Arabic 76%
   (two Arabic-speaking agents hired from the ₪600,000 line, re-cut by council), mystery-shopper fee
   answers right 92%. No agent's job changed without the committee's agreement.
3. **Half-way.** The assistant is built and passes the eval, but department owners are never named:
   the content work is "IT's job". On 1 July 2027 the council's new parking fee takes effect; nobody
   updates the pack; the assistant quotes the old fee with a confident citation. Agents stop using it
   in August; the public pilot is postponed "until after the holidays"; the register entry is never
   published. The readout named the dependency; nobody owned it.

**What decided which future:** whether the content had owners and an effective-date rule in the
decision record, and whether the mayor had something true to announce on 4 February.

## Numbers (where each finding is planted)

Computed from the generated files (seed 20261129) with `labs/module-11/discovery.py` and the pilot's
`run_faq.py` / `score_faq.py`; reproducible in a spreadsheet. Moked figures are a 4% caller sample (× 25).
Paths relative to `labs/module-11/data-room/`.

**Volumes.** `service/moked-contacts.csv` 3,914 contacts from 2,350 callers (Jun 735, Jul 784, Aug 783,
Sep 833, Oct 779) ≈ 19,570 a month for the city; phone 63.2%; permits family 33.8% (≈ 6,600 a month).
`callbacks.csv` 943. `permits/applications-2026.csv` 2,300 (PRK 1,180, SKP 380, ARC 240, EVT 210,
SGN 160, CAF 70, DPK 60). `content/cms-pages.csv` 1,240. `chatbot/ruti-bot-log.csv` 640.
`governance/foi-log-2026.csv` 46. `service/mystery-shopper-2026.csv` 120.

1. **Pages vs the council decision:** 9 of 24 topic pages out of date (he SKP ₪60, he ARC ₪60, ar PRK ₪90
   + "not eligible" + 21 days, ar BLK ₪120, ar EVT 14 days, ru PRK, ru SGN ₪245/₪300, en PRK, en EVT); 2025
   fee table linked from 6 pages.
2. **CMS:** no named owner 40.7%; pages last changed before 2024: ar 70.8%, ru 73.3%, en 80.0%, he 2.5%;
   3 pages with `botnest-widget`.
3. **FCR:** Q3 83.3% by the report's definition (report shows 83%); callback contacts carry fcr_flag = 1 in
   85.4%. Callbacks: on time 47.3%, late 19.3%, never 33.4%; permits family 42.4 / 18.4 / 39.2 (n = 451).
4. **Repeats** (same caller, same topic, < 14 days): all 19.9%; permits family 35.0%; others 12.2%; permits
   family by language he 33.0, ar 34.8, ru 40.0, en 41.7, am 37.8. Permits-family fcr_flag = 1 contacts
   followed by a repeat: 34.3%.
5. **Service language** (handled): ar 39.7% (n = 748), ru 75.9%, am 26.7%, en 89.6%. Phone wait medians:
   he 74 s; ar served ar 64 s; ar served he 134 s. Active agents: ar 3, ru 4, am 1, en 2 of 24.
6. **Mystery shopper:** 65 of 120 right (54.2%); answer questions right where the rule changed 42.3%
   (n = 52), unchanged 74.4% (n = 39); 21 wrong_outdated; served in own language ar 33%, ru 76%, am 30%.
7. **Letters:** all Hebrew; PRK rejections 293, R-07 151 (51.5%); linked 106 contacts per rejection R-07
   2.36, others ≈ 1.05, approvals 0.16; objections 12 on R-07.
8. **Leased cars:** before 1 Jul 169 leased/company, 151 refused; from 1 Jul with the employer letter 63,
   decided 55, refused 33 (60%; R-07 28, R-03 5). Amal = `2026-PRK-0945` (Ein Sara, ar, online 16 Aug,
   refused 25 Aug, R-07, 3 linked contacts).
9. **Events:** R-08 (late) share of decided applications by language: ar 48.8%, en 28.6%, he 9.2%, ru 8.7%.
10. **Skips:** 87 approved before 16 Mar charged ₪60/week: ₪10,920 vs ₪13,650.
11. **Ruti:** he 453, ar 101, ru 59, en 27; all replies Hebrew; replies stating sign ₪245 (83), sign min
    ₪300 (47), café ₪160 (62), events 14 days (62), skip ₪60 (34), leased not eligible (53), second car ₪90
    (34), invented ₪1,200 (58) = 433 of 640; 46 nine-digit numbers, 28 mobile numbers; thumbs down 80, up 39.
12. **FOI:** FOI-2026-031 answered "none" after 42 days; median 33 days; 22 over 30; 3 over 60.

**Pilot (test split, 134 questions: answer 93, route 32, clarify 9; he 33, ar 33, ru 34, en 26, am 8).**
Real: site search right 23.9% (answer 34.4%; outdated 22 of 93; by language he 57.6, ar 21.2, ru 14.7, en
3.8, am 0; changed 24.5% vs unchanged 47.5%); pack search right 64.9% (answer 93.5%; 0 outdated; by language
he 72.7, ar 72.7, ru 67.6, en 61.5); today (94 calls on test questions) 54.3%, changed-rule answers 44.2%
(16 outdated) vs 76.7%. Negative: site search 1/12, pack search 3/12. Track A set (80): site 25.0%, pack
63.7%, today 58.3% (48 calls). Illustrative (story): LLM over site 52.2% (answer 55/93, 17 outdated, routed
13/32, clarified 2/9, negative 5/12); pack v1.0 88.1% (85/93, 27/32, 6/9, negative 10/12, pergola "usually
exempt"); pack v1.1 90.3% (86/93: he 26/27, ar 22/24, ru 22/25, en 16/17; 29/32; 6/9; language 123/126;
sources 89/93; negative 12/12); ratings 84% (he 88, ar 80, ru 81, en 88). Cost ≈ ₪0.022 a question
(2,600/180 tokens, Sonnet 5.5, ₪3.136); case model 57.8 net hours, ₪1,406/month; content fix 990 contacts,
61 hours (assumed 35% → 20%).
