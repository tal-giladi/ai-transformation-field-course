# Atlas & Rowe — writer's notes for module 12 (never imported)

The fifth Stage 2 engagement. The learner is an **outside consultant to the managing partner** of a
90-lawyer Israeli commercial law firm whose partners are split over buying a legal-AI platform. The
hard part is threefold: confidentiality and privilege, fabricated citations, and the billable hour
(time saved is not money earned; clients take their share at renewal). The data room is in
`labs/module-12/data-room/` (built by `generate.py`, seed 20261115, standard library only); the pilot
files are in `labs/module-12/pilot/` (also written by `generate.py`). Never link this file from lessons.

## The firm

- **Atlas & Rowe, Advocates** (אטלס אנד רואו, עורכי דין), founded 1994 by Avraham Atlas (d. 2017) and
  David Rowe (London-trained, retired 2020). Offices on Menachem Begin Road, Tel Aviv. 90 lawyers: 26
  partners (16 equity, 10 salaried) and 64 associates; 11 interns; about 50 staff (secretaries,
  finance 6, IT 2 plus a managed service provider, KM 1 after the librarian left in March 2026).
- Practice groups: Corporate & M&A, International desk (inside Corporate; US/UK/EU investors; English
  work product, some Russian), Commercial litigation, Real estate, Banking & finance, Employment,
  Tech & IP. Hebrew and English work product; Arabic and Russian among lawyers and clients.
- 2025 fees billed ₪151.1M; worked value ₪174.4M; realisation 87%. Billing mix by fees: hourly 52%,
  fixed fee 19%, capped 16%, monthly retainer 12%. Associates' billable target 1,850 h; actual 2025
  average 1,552; 2026 annualised 1,490 (81%; 1 of 64 at target: spare capacity, no backlog).
- Partner compensation: modified lockstep, 70% points by seniority, 30% "contribution" of which half is
  personal billed hours. Partners whose hours fall lose points — the quiet reason the partnership is split.
- Systems (fictional): DMS "Archive"; time and billing "TimeLedger"; precedent bank "Mikbatz" (מקבץ)
  inside the DMS; email and Office; a web proxy with DLP from the managed service provider.
- Clients are codes in the data room. Carmel Retail Group (C-014, ₪6.1M in 2025, fourth largest) is
  named; Ofek Insurance (C-031, ₪3.8M in 2025) is the litigation panel lost to a tender on 14 September
  2026 (named only by Shmuel's persona).

## Who the learner is

Yoav Dagan (managing partner) hired the learner as an **outside consultant**, reporting to him; the
"steering group" is the firm's management committee (Yoav, Shmuel Atlas, Noa Friedman, Orit Levinson,
Eli Ben-Hamo, Tamar Golan for KM questions). Eight and a half weeks, Sunday 15 November 2026 – Thursday
14 January 2027 (the partners' meeting votes on the AI budget that evening). Fixed fee in three
exitable phases: ₪64,000 diagnose (to Thursday 3 December; exit), ₪96,000 decide and build (to
Thursday 7 January; exit after the decision paper on Thursday 17 December), ₪20,000 readout (to 14
January). ₪180,000 + VAT; pilot tooling up to ₪40,000.

What is new for an outsider in a law firm (12.1): the consultant is not a lawyer and may not see
client files; everything is under a confidentiality undertaking, the data room is pseudonymised
(clients as codes except Carmel, which consented to be named and interviewed), and the precedent
corpus is the firm's own knowledge with client identifiers removed. Partners are owners, not
employees: there is no CEO to decide; the vote is the decision. The consultant must never give legal
or ethics advice to lawyers: Orit (GC and ethics partner) and outside ethics counsel own those.

## Stated ask vs hidden truth

- **Stated ask:** "Everyone wants Harvey/CoCounsel; partners are split." Concretely: Noa Friedman's
  October proposal to sign Parshan AI (fictional Israeli-UK legal-AI vendor) for all 90 lawyers, 24
  months, US$120 per seat per month, 20% launch discount if signed by 31 December 2026, US$25,000
  set-up. Her slide: "6.2 hours a week per lawyer × 90 × 44 weeks × ₪950 = ₪23.3M a year of capacity
  for ₪0.4M." Shmuel Atlas opposes ("it invents cases; our clients pay for judgement"). Vote deferred
  to 14 January; Yoav hires the consultant to "tell the partners what to buy".
- **Hidden truth.** The question is not which platform.
  1. **AI is already in the firm's client work, uncontrolled.** 43 of 64 associates and 9 partners hit
     consumer AI sites in September–October; 27 lawyers uploaded 171 files; a draft share-purchase agreement
     went into a consumer tool (DLP alert, 3 September), handled quietly. Noa's team has had personal
     ChatGPT Plus accounts reimbursed as "software" since 2024. The firm's survey (self-reported)
     shows far less. The engagement-letter clause ("we may use technology tools") is the kind of
     general clause the Bar's 2026 ethics opinion says is not enough for consent.
  2. **A fabricated citation already nearly reached a client.** In October a junior associate's memo
     (written at night with a free chatbot) cited a ruling that does not exist in the firm's corpus and
     misstated another; the supervising partner — Shmuel, the sceptic — wrote "good, send to the
     client"; the senior associate Karim caught it the next morning. Nobody reported it.
  3. **The billable hour.** On hourly work (54% of fees), saved hours become lost revenue unless they
     are resold, and associates are at ≈ 80% of target with no backlog. Research is hidden: it is
     coded as drafting because partners write off "RES" lines; the true research share of associate
     time is ≈ 4× what the codes say (25.2% vs 6.2%), and most of the AI-relevant time sits in write-offs and in
     fixed-fee and capped matters, where saving time is margin. **Clients already take their share:**
     after the 2025 NDA template automation cut turnaround from ≈ 3 days to under 1, Carmel moved NDAs
     to a fixed price per document at renewal and that revenue fell by about a third; Carmel's new
     outside-counsel guidelines (1 October 2026) require disclosure and consent for AI and refuse to
     pay hourly for work "a reasonably efficient firm would perform with technology"; its GC asked
     Yoav for 15% off at the January renewal. He has not told the partners.
  4. **The knowledge base is stale.** Mikbatz: 1,180 documents, 71% never reviewed;
     "current" status unreliable; precedents not updated for Amendment 13; memos that rely on rulings
     later reversed. A precedent-search tool over it retrieves the stale answer confidently. The
     vendor wants to index the whole DMS, which crosses ethical walls (Tamar flagged it; no answer).
- **The honest answer:** do not sign a 90-seat licence by 31 December. Put an interim AI rule and one
  approved enterprise tool in place now (no consumer tools on client material, client consent per
  matter class, verification duty); fund a six-week curation sprint of the most-used precedents;
  pilot a precedent-search assistant **over the curated corpus only**, with a citation-verification
  gate (exists, pinpoint exists, quote verbatim, current, supports the claim) in two groups (Tech &
  IP fixed-fee work, litigation research); change pricing where the firm keeps the gain (fixed fees
  and a Carmel contract package instead of 15% off hourly); revisit the platform by RFP with a proof
  of concept on the firm's corpus at a June 2027 gate. Revised ROI includes the customer's share.

## Planted findings (each discoverable, never stated)

| # | Finding | Where |
|---|---|---|
| 1 | Shadow AI far above self-report; file uploads; partners too | `it/proxy-ai-domains-2026-09-10.csv` + `people/lawyers.csv` vs `surveys/ai-use-survey-2026-10.csv` |
| 2 | Client document uploaded to a consumer tool; closed quietly | `it/dlp-alerts-2026.csv`, `risk/ethics-log-2026.csv` (Orit persona for detail) |
| 3 | Personal ChatGPT Plus reimbursed as "software" in Tech & IP | `finance/expense-claims-software-2026.csv` |
| 4 | Near-miss fabricated citation approved by a partner | `research/memo-M-2026-0412-v2.md` (comments), corpus; Karim persona |
| 5 | Research hidden in drafting codes; RES lines written off | `billing/time-entries-2026-q3.csv` |
| 6 | Spare associate capacity: saved hours cannot be resold | `people/lawyers.csv`, time entries |
| 7 | Gains sit in fixed-fee/capped matters and write-offs; Noa's fixed fees overrun | `billing/matters.csv`, time entries |
| 8 | Customer's share: NDA automation → fixed price at renewal → revenue down | `clients/carmel-nda-workstream.csv`, `clients/renewals-and-rate-negotiations.csv` |
| 9 | Client OCG: disclosure, consent, no hourly for tech-avoidable work | `clients/carmel-ocg-2026.md` |
| 10 | Engagement-letter clause too general for consent | `policies/engagement-letter-template-2023.md` vs Bar opinion (12.4) |
| 11 | Noa's draft AI policy allows "anonymised" client data in any tool, no verification rule | `policies/draft-ai-policy-2026.md` |
| 12 | Vendor claims: 6.2 h/week from a survey of US firms; "zero hallucinations"; Hebrew beta; whole-DMS indexing; sub-processor retention | `vendor/parshan-*.md` |
| 13 | ROI slide copies the vendor number and treats hours as revenue | `firm/partners-meeting-2026-10-minutes.md` |
| 14 | KM: stale status; superseded documents marked current; pre-Amendment 13 privacy precedents | `km/precedent-bank-index.csv`, `knowledge/corpus/` |
| 15 | Lost tender to a fixed-fee, AI-assisted competitor (litigation) | `clients/renewals-and-rate-negotiations.csv`; Shmuel persona |
| 16 | PI insurer asks about AI controls at the February renewal | `risk/pi-renewal-questionnaire-2027.md` |

## The cast (persona pack)

| Persona | Role | Type | Hidden / unlock |
|---|---|---|---|
| Yoav Dagan | Managing partner | Sponsor | Told Parshan "probably in"; Carmel's 15% call not shared; comp model is why partners split. Unlock: commitments made; what clients say about price; how partners are paid |
| Shmuel Atlas | Founding partner, litigation | Sceptic | Lost Ofek tender to fixed-fee AI-assisted rival; writes off RES lines himself; approved the memo with the fake citation (does not know it was AI). Unlock: lost pitches; how he reviews bills; how research memos are checked |
| Noa Friedman | Partner, Tech & IP | Secret enthusiast | Team on reimbursed ChatGPT Plus since 2024, uploads term sheets; 6.2 h from the vendor; fixed fees overrun. Unlock: no names + "what do you use today"; source of 6.2; fixed-fee performance |
| Karim Nassar | Senior associate, litigation | Frontline | Caught the fake citation; uses an assistant on his phone with anonymised facts; RES coded as DRF. Unlock: no names + "has anyone found an AI error"; how research time is recorded |
| Yana Petrenko | Junior associate, Corporate & International | Frontline, junior | Wrote the memo at 23:40 with a free chatbot; translates Russian investor documents in free tools; fears losing the work she learns from. Unlock: safety, workload at night, how she checks sources |
| Tamar Golan | Head of Knowledge Management | Data steward | ~40 wrong-but-"current" precedents; vendor's whole-DMS index crosses ethical walls; can curate top 300 in six weeks. Unlock: an example from the index; access and walls; what she needs |
| Eli Ben-Hamo | Finance director (CFO) | Finance | NDA revenue fell after automation; no backlog; modelled Parshan as cost only. Unlock: what happened after 2025 automation; more work than hours?; ask for his model |
| Orit Levinson | General counsel and ethics partner | Counsel | DLP incident, client not told, outside ethics view pending; engagement letter clause; PI insurer question. Unlock: incidents; engagement letter; insurance |
| Sigal Mizrahi | GC, Carmel Retail Group (client) | Person affected / commercial pressure | 15% is an opening; wants fixed prices and a subscription; testing a rival firm; would consent under conditions. Unlock: what a good deal is; who else; what she needs to consent |

Transcripts leave hidden: Yoav's comp-model reason; Shmuel's approval of the memo; Noa's fixed-fee
overruns; Karim's phone use; Yana's Russian translations; Tamar's capacity offer; Eli's Parshan model;
Orit's insurer question; Sigal's rival firm.

## Timeline

- Data: time entries 1 Jul – 30 Sep 2026 (three groups); matters and fees 2025 – Oct 2026; proxy log
  1 Sep – 31 Oct 2026; DLP alerts and expenses 2026; NDA workstream Jan 2024 – Oct 2026; KM index
  uploads 2014–2026.
- 2025 Mar–Jun NDA and employment-agreement template automation. 1 Jan 2026 Carmel renewal (NDA
  fixed price). 3 Sep 2026 DLP alert. 14 Sep Ofek tender lost. 1 Oct Carmel OCG. 8 Oct Parshan demo.
  20 Oct memo near-miss (draft 19 Oct 23:40). 22 Oct partners' meeting (vote deferred). 29 Oct Sigal's
  call to Yoav.
- Tue 3 Nov the call; Sun 15 Nov start (12.1); 16–26 Nov discovery (12.2); Thu 3 Dec phase-1 readout
  (12.3; exit point); 4–12 Dec Hanukkah; 8–15 Dec hard part (12.4), decision paper Thu 17 Dec (exit);
  20 Dec – 7 Jan build and eval (12.5); 31 Dec Parshan discount expires; Mon 11 Jan rehearsal with
  Yoav and Shmuel; Tue 12 Jan management committee; Thu 14 Jan partners' meeting (12.6); 31 Jan
  Carmel renewal; Feb 2027 PI insurance renewal. Six months later: July 2027.

## The futures (12.6 debrief)

1. **Sign everything.** Partners vote 15–11 to sign Parshan before the discount. Usage: 70% log in in
   February, 22% weekly by May (associates keep their own tools for drafting). A research answer citing
   a superseded non-compete ruling reaches an employment client; corrected before filing. Carmel
   renewal at 12% off hourly; two more clients ask for the same. Billed hours in research-heavy matters
   fall 9%; partners' points fall; the comp fight returns in June. Year-1 cash ≈ −₪3.1M against doing nothing (model column A).
2. **Curate, control, re-price, then choose (the expert path).** Interim rule and one enterprise tool
   in January; consumer AI traffic down 80% by March; consent added by matter class; Carmel signs a
   fixed-price contract package (12 contract types, quarterly subscription) instead of 15% off;
   curation sprint finishes 300 precedents; pilot in Tech & IP and litigation: 0 unverified citations
   sent, Noa's fixed-fee overruns down from 34% to 12%; June RFP with a corpus PoC picks a platform
   for 30 seats. Year-1 cash about break-even against doing nothing (model column B), and a pricing model that keeps part of the gain.
3. **Ban it.** Shmuel's motion passes: no AI until "the market settles". Proxy traffic drops for two
   weeks, then moves to phones. Ofek-type tenders keep being lost on price; three associates leave for
   a firm with tools; a second near-miss is found by the other side's counsel in a court filing.

## Where each finding is planted (actual numbers)

Computed from the generated files (seed 20261115) with `discovery.py`, `roi_model.py`,
`pilot/search.py` and `pilot/verify_citations.py`; all reproducible in a spreadsheet. Paths relative to
`labs/module-12/`.

**Volumes.** lawyers 90; matters 562; time entries 5,218 (40 lawyers: Litigation 21, Tech & IP 10,
International desk 9); clients with fees 140; proxy rows 864 (63 users); DLP 14; expenses 86; survey
47; KM index 1,180; corpus 78 (24 rulings, 36 memos, 18 clause notes); questions 48 (24 en, 24 he);
drafts 40 with 160 citations.

1. **Shadow AI.** Proxy: 52 lawyers (43 of 64 associates, 9 of 26 partners) + 11 staff; 27 lawyers
   uploaded 171 files (174 with staff). Survey: weekly or daily 28% (13 of 47), "no client
   information" 89% (42), "only anonymised" 5, nobody "yes". Office/VPN only; phones invisible (Karim).
2. **DLP 3 Sep 2026**, L058 (Corporate associate), chatgpt.com, CLIENT-CONFIDENTIAL draft SPA, warned,
   user proceeded; closed by L004 "no further action"; ethics log 3 Sep: client not informed, outside
   ethics counsel asked, open. Three more client-marker alerts in October still open.
3. **Expenses.** 58 "OpenAI *ChatGPT Plus" claims, ₪4,225, 6 people in Tech & IP, approved by L003.
4. **Near miss.** `data-room/research/memo-non-compete-draft-v2.md`: point 1 cites FCR-2020-460
   (reversed by FCR-2022-390); point 2 cites FCR-2022-318 (does not exist); point 3 says the opposite of
   FCR-2021-124 ¶5; point 4 correct (FCR-2025-049 ¶3). Last saved 19 Oct 23:40; proxy L063 on
   chatgpt.com 19 Oct until 23:52 with 2 uploads (inference, not proof). S.A.: "send to the client today".
5. **Research hidden.** Associates: research by narrative 25.2% of hours vs 6.2% coded RES (partners
   5.1% vs 3.7%). Written off on non-fixed matters: RES lines 40.0%, research hidden in DRF/REV 12.0%,
   everything else 4.3%. RES lines on Shmuel's matters are written off far more often.
6. **Capacity.** Associates 2026 annualised 1,490 = 81% of 1,850; 1 of 64 at target.
7. **Where research sits.** Research hours by billing type: hourly 56.8%, fixed 24.0%, capped 14.5%,
   retainer 4.7%; 80.4% of research on non-fixed matters is billed. Fixed fees 2025, worked value over
   fee: Tech & IP +38.1% (others 1–10%); realisation Tech & IP 76% vs firm 87%.
8. **Customer's share.** NDAs: 2024 461 NDAs, ₪943,250, ₪2,046 each, 2.38 h each, ₪860/h; 2025 507,
   ₪567,210 (automation Mar–Jun, still hourly); 2026 Jan–Oct 452 at ₪1,150 fixed = ₪519,800 (≈ ₪624k
   annualised, −34% vs 2024 while volume +18%); hours per NDA 0.81; fees per hour ₪1,422 (+65% vs 2024).
   Renewals log: C-014 Nov 2025 asked ₪900, settled ₪1,150; C-041 "your templates are automated" −6%;
   C-009 "faster turnaround" −7.9%; C-031 tender lost (competitor fixed fees ~30% lower with AI review);
   C-014 29 Oct 2026 15% off hourly, open. Carmel hourly fees 2025 ₪4.33M (15% = ₪0.65M).
9. **OCG.** Carmel 7.1–7.5 (disclose, consent for training/retention tools, verify, no hourly for
   tech-avoidable time, 48 h incident notice); four clients with AI clauses (C-014; C-003 consent;
   C-007 prohibited unless approved; C-022 disclose).
10. **Engagement letter** clause 11 "technology tools": general; the Bar's September 2026 opinion (per
    Calcalist) says a general clause in a retainer or power of attorney is not enough for consent.
11. **Draft policy**: anonymised data in any tool; review "where appropriate"; bill "the time a task
    would normally take" on hourly matters (billing for time not spent).
12. **Vendor**: 6.2 h from a self-reported survey of 212 lawyers at 9 US/UK firms; demo of 12 English
    questions on US case law; "zero hallucinations"; Hebrew beta, citation checking English only;
    whole-DMS indexing; Archive is not a supported connector → permissions configured in Parshan
    (ethical walls); sub-processor retention 30 days; §4 usage data "to improve the Service" (the
    corpus's own data-processing P1); liability cap 12 months' fees; no termination for convenience.
    PoC drafts: 28 of 80 citations bad (0 nonexistent, 10 superseded, 12 misstated, 3 bad pinpoint, 3
    bad quote) vs the general assistant's 42 of 80.
13. **Slide**: 6.2 × 90 × 44 × ₪950 = ₪23,324,400, hours treated as revenue.
14. **KM**: 71% never reviewed; 8% reviewed in the last two years; 105 privacy documents "current" and
    not reviewed since 14 Aug 2025; top 300 documents = 86% of uses; 25% unused. Corpus: 13 documents
    superseded (6 rulings reversed on appeal, 6 memos relying on them, 1 pre-Amendment 13 clause); the
    KM index marks only 2 of them.
15. **Lost tender**: C-031, 14 Sep 2026, ₪3.8M fees in 2025.
16. **Insurer**: questionnaire 6.1–6.7 due 15 Jan 2027; 6.5 asks about near misses (the memo).

**Pilot (real, reproducible).** Search, BM25 over 78 documents: gold in top 5 for 48 of 48; mean gold
recall@5 71.7%; top result gold 39 of 48; a stale document in the top 3 for 12 of 12 questions about
reversed points. Curated (65 documents): top result gold 48 of 48; stale 0 of 12; recall@5 74.1% (en
78.1%, he 70.1%). Hebrew prefix stripping: no gain (73.6%). Citation gate on 160 citations (70 bad):
rules with the KM status catch 36 of 70 (51.4%; superseded 2 of 14); rules with the curated status
catch 48 of 70 (68.6%), 0 false alarms; the 22 misstated citations need a reader; keyword overlap
catches 68 of 70 but raises 48 false alarms on 90 good citations. LLM-judge figures in 12.5 are an
illustrative worked example.

**ROI (`roi_model.py`, year 1).** Research hours ≈ 25,746 a year (directional). Saving 30% net of
verification (assumed). 0 (do nothing): Carmel's 15% conceded, −₪0.65M. A (90 seats, adoption 60%):
4,634 h saved, fees lost ₪2.42M, capacity 1,666 h, Carmel −₪0.65M, control −₪0.24M, tools −₪0.40M:
−₪3.71M; vs doing nothing −₪3.06M. B (two groups, adoption 80%, about a third of research, half the
pilot's hourly research moved to fixed prices): 2,163 h saved, fees lost ₪0.56M, Carmel package
−₪0.43M, control −₪0.42M, tools −₪0.11M, Tech & IP packages +₪0.83M (half of the ₪1.67M overrun cut,
assumed): −₪0.69M; vs doing nothing −₪41k, with 1,470 freed hours.

**Futures, with the model.** Future 1 ≈ the A column (−₪3.1M against doing nothing in 2027, before
other clients follow Carmel). Future 2 ≈ B (about break-even in 2027 against doing nothing, a pricing
model that keeps part of the gain, a curated base and a June gate). Future 3 ≈ doing nothing plus the
tender losses and the second near miss.
