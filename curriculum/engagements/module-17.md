# Vantage Logistics — writer's notes for module 17 (never imported)

The tenth and last engagement, and the only **rescue**. The learner is an **interim AI lead hired by
the board for 30 days**, reporting to the chair of the board's audit committee and to the CEO, in a
1,200-person Israeli logistics and freight-forwarding company whose AI programme has just lost its
lead, has an open AI incident, a cost overrun and a board that no longer believes its numbers. The
hard part (17.4) is a turnaround: an inherited failing programme, an open incident, an overrun and
broken trust with the board and the operations teams. The build-or-decide (17.5) is a **stop/keep
audit of everything running** (Track B genuinely helps: it joins contracts, invoices, licence usage,
tickets and evidence), the **closure of the open incident** (runbook, root cause, notifications routed
to counsel) and the decisions that cannot wait for the board. 17.6 is the **30-day board brief**.
The data room is `labs/module-17/data-room/` (built by `generate.py`, seed 20270606).

No engagement preset exists in `simulations/`; lessons link the generic ones that fit
(`incident-tabletop?preset=harbor` in 17.5, `roi-defender?preset=harbor` in 17.3,
`risk-register-tester?preset=harbor` in 17.4, `steering-committee?preset=harbor` in 17.6) and say
they are Harbor & Pine's. A `vantage` preset for `incident-tabletop` and `steering-committee` is
proposed in `curriculum/inbox/module-17-notes.md`.

## The company

- **Vantage Logistics Ltd.** (ואנטג' לוגיסטיקה בע"מ), fictional. Founded 1988 in Haifa as a customs
  brokerage; trucking from 1996, warehousing from 2004; listed on the Tel Aviv Stock Exchange since
  2011; head office in Petah Tikva. Revenue 2026 ₪1.04bn. About 1,200 staff in **four regions**:
  North (Haifa port, Karmiel, Kiryat Shmona; ~330), Centre (Modi'in distribution centre, the airport
  logistics park, Petah Tikva; ~420 incl. HQ functions), South (Ashdod port, Be'er Sheva, Netivot;
  ~290) and Europe (Vantage Europe B.V., Rotterdam: forwarding office and a small trucking unit; ~60).
  Head office ~100. Staff and drivers speak Hebrew, Arabic, Russian, Amharic, English; Europe Dutch
  and English. Customers are importers, exporters and retailers; customs declarations are filed by
  Vantage's licensed customs agents at three customs houses (Haifa, Ashdod, Ben Gurion airport).
- **Systems** (fictional): ERP "Mishkal ERP" (finance, AP); customs-brokerage software "Meches Pro";
  telematics "Mabat Fleet" (GPS, km, fuel) in every truck; the AI platform **Tzir AI Ltd.** (fictional
  Israeli vendor) with three modules — **Tzir Route** (route optimisation, planner console, driver app
  with a "driver score"), **Tzir Docs** (reads supplier invoices and packing lists, proposes tariff
  codes, values and origin, pre-fills the import declaration in Meches Pro for a customs agent to
  review), **Tzir Assist** (customer-portal assistant: shipment status and, from 20 April 2027, "my
  documents"). Others: **Kotev Assist** (enterprise assistant, 450 seats), **Ayin Drive** (in-cab
  camera with fatigue/distraction detection, 60 cabs in the South), **Nezek Vision** (damage-photo
  assessment, warehouse POC), a quote-pricing add-in, the in-house warehouse demand and labour
  forecast (Modi'in DC), AP invoice matching inside Mishkal ERP, "HS Suggest" inside Meches Pro
  (turned on by default in release 9.3, March 2027). Shadow: the customer-service email triage built
  by the CS team lead on n8n with the public **Promptway** LLM API (fictional) paid on her card; customs
  clerks using a free online translator for Chinese invoices.
- All vendor names except n8n are fictional and were searched on 3 November 2026 (Tzir AI, Kotev
  Assist, Ayin Drive, Mishkal ERP, Meches Pro, Mabat Fleet, Promptway, Gefen Medical Distribution: no
  company found). "Vantage Logistics" is the plan's name; unrelated firms with that name exist in
  Vietnam and Canada (none in Israel); the data room and brief say the company is fictional.

## Who the learner is, and what changes

**Interim AI lead (ראש/ת תוכנית AI בפועל), 30 days, contracted by the board** on the audit committee's
proposal (board special session Thu 3 June 2027). Starts **Sunday 6 June 2027**. Reports to **Dr.
Ilana Shaked**, external director and chair of the audit committee, *and* to **Ofer Lavi**, CEO. Fee
₪96,000 for the 30 days (board-approved); an incident-support budget of up to ₪120,000 (CEO approves).
Entry role (17.1, pointing to 01.1): a hybrid of outside consultant and accidental owner — outsider
with an executive's in-tray; **two principals whose interests may diverge** (the chair wants an
independent account; the CEO wants the programme fixed and his numbers to survive); a fixed end date
(you leave; nothing may depend on you); an incident already open that you inherit; a team of one
data scientist and one analyst whose manager has just resigned. Differs from every earlier entry:
the first move is a **written reporting protocol** with both principals (who hears what first, what
goes to the committee directly, what is routed to counsel), signed before discovery.

## Stated ask vs hidden truth

- **Stated ask (board minute of 3 June 2027):** "The last AI lead left; the board wants answers in 30
  days." The minute lists the board's questions: what AI is running, what it costs, what it has
  delivered, what happened in the May incident and whether it is closed, and whether to continue.
  The CEO's addition: "and a plan to get the savings back on track".
- **Hidden truth.**
  1. **The incident is not closed, and it is bigger than the record says.** INC-27-0518-01 is marked
     "contained" (22 May) with "personal data: none (per vendor)". The data shows mismatches continued
     after the vendor's hotfix (4.2.1, 21 May) for numeric-only invoice numbers; exposed portal
     documents included B2C manifests of a parcel consolidator (Shuk Online) with ~1,870 individuals'
     names, addresses and phones, opened by users of other customers; and some declarations were
     submitted to Customs with another importer's values. The privacy branch was never triggered: the
     general counsel (also privacy officer) was never sent the incident. Nobody has asked counsel or
     the licensed customs agent in charge about correcting declarations.
  2. **The "review step" exists only on paper.** Tzir Docs' "99.2% accuracy" is "fields accepted
     without edit"; customs agents approve pre-fills in batches (median review ~14 seconds at peak,
     against a KPI of declarations per agent per day). The customs compliance team's April QA re-check
     of 400 pre-filled declarations found a material error in about 7% — reported to the COO, never
     to the board.
  3. **The CEO was warned.** On 14 April the former lead wrote to the CEO recommending a pause of
     batch approval and a measured review; the CEO replied "not before the board's Q2 numbers". The
     memo is not in the data room: the handover note mentions "my 14/4 note to Ofer on Docs review";
     the former lead tells it on the phone if asked the right question; the CEO tells it only when
     shown the handover line.
  4. **The tool extended to four regions was pulled back (the plan's planted finding).** Tzir Route
     went North in November 2026 and to all four regions on 10 January 2027. South pulled it back on
     25 February (routes onto closed roads, late deliveries, drivers' refusal after the driver score
     was used in a disciplinary hearing); Centre went to "planner view only" in March; Europe was
     never integrated. The March board deck and the vendor dashboard still say "4 regions live, 310
     drivers": the dashboard counts licensed seats. The COO asked South to "keep South in the
     numbers until the board".
  5. **The route model is trained on pre-war traffic.** The model card: trained on 2021-01 to 2023-06
     GPS traces; "quarterly retraining from the customer's telematics feed". The Mabat feed has failed
     every night since 14 November 2026 (HTTP 401 after a credential change); no retraining happened.
     Overrides in the North concentrate on routes to the Upper Galilee and the Golan, with reasons
     like "road closed", "military zone", "detour".
  6. **The savings are the vendor's arithmetic.** The board was told ₪6.2M a year; ₪6.2M is booked
     as savings in the 2027 budget. Fuel ₪3.1M comes from the Tzir value dashboard (tool plan vs a
     "naive shortest-path baseline", × the vendor's default ₪/km, all licensed regions). Telematics
     show km per stop down ~4% in the North only; flat elsewhere. Customs ₪1.6M ("8 FTE freed"): no
     headcount moved, overtime up after the incident. CS deflection ₪0.9M: tickets unchanged, 41% of
     assistant sessions end with "talk to a person". Warehouse ₪0.6M: the only real one (overtime
     down ~14% at Modi'in against Ashdod DC). Defensible: about ₪0.76M.
  7. **The overrun is partly a commitment nobody approved.** Three Tzir order forms signed 15–17
     September 2026 under one master agreement, each just below the ₪5M per-contract line above
     which the delegation of authority requires the board: ₪14.4M together over 36 months. Not your
     finding to judge: you put the facts to the audit committee chair and counsel.
  8. **Licences nobody uses.** Route: 310 driver seats billed, ~96 active (North). Kotev Assist: 450
     seats, ~112 active in 30 days. Ayin Drive billed after the pilot paused (8 March). Nezek Vision
     billed after its POC ended (28 February). The quote add-in paused since February.
  9. **The works committee will declare a dispute if cameras return.** Letter of 3 March: in-cab
     cameras and the driver score introduced without the consultation the collective agreement's
     technology clause requires; a driver was summoned to a hearing using the score. Drivers in the
     North like the live-traffic part of the app; the committee would agree to route planning without
     individual scores.
  10. **AI outside every list:** AP matching (embedded), HS Suggest (vendor release, on by default,
      a second tariff-code source beside Tzir Docs), the n8n + Promptway email triage with customer
      emails in prompts, the free translator for supplier invoices.
  11. **A key customer is about to leave.** Gefen Medical Distribution (~₪9.4M a year; tender in
      September) found another importer's invoice in its portal on 18 May; three of its shipments
      were held at Haifa Port after customs queries on value; its own invoices (pricing) were seen by
      another importer; its counsel is asking.
  12. **Real value exists and must not be thrown out with the rest:** the warehouse forecast (the
      data scientist's in-house model; owner gap now that the lead left), AP matching, Route in the
      North (with retraining and without the driver score).
- **The honest answer (expert):** close the incident properly before anything else (contain the
  post-fix mismatches by pausing Docs auto-match on numeric invoice keys and adding a consignee
  cross-check; full scope from the logs; general counsel briefed on day 2 with the facts for the
  privacy and customs questions; Gefen and Shuk Online told by people with facts; vendor RCA
  rejected and rewritten); stop/keep audit with criteria fixed before the list — **stop** Ayin Drive,
  the driver score, Nezek Vision, the quote add-in, Assist's documents feature, Route outside the
  North (reduction notice by Thursday 1 July for the 1 October anniversary), Kotev seats cut to 150;
  **keep** the forecast (with an owner), AP matching, Route North (fix the feed, retrain on
  post-2023 data, no individual scores); **keep under conditions** Tzir Docs (consignee check,
  measured review time, 5% QA sample, a 90-day gate); **bring in** the n8n triage and the translator
  through an approved route; **turn off** HS Suggest until evaluated. Restate savings to what is
  measured (~₪0.6M) and the 2027 AI cost forecast with the stops. Board brief: what runs, what it
  costs, what it delivered, the incident, what stops, what continues, the governance facts for the
  audit committee (the April memo, the order forms) stated as facts with their sources and routed to
  the committee and counsel, and a permanent owner by a date. Deliver the hardest finding to the CEO
  first, then the chair, as agreed in the reporting protocol.

## Timeline

| Date | What |
|---|---|
| Sep 2026 (15–17) | Three Tzir order forms signed under MSA-TZ-2026 |
| 14 Nov 2026 | Mabat telematics export to Tzir starts failing nightly (HTTP 401) |
| Nov 2026 | Tzir Route live in the North |
| Sun 10 Jan 2027 | Tzir Route extended to all four regions |
| 1 Feb 2027 | Tzir Docs live at Haifa and Ashdod customs houses (airport from 1 April) |
| 24 Feb 2027 | A South driver summoned to a hearing using the driver score |
| Thu 25 Feb 2027 | Rania pulls Route back in the South |
| 28 Feb 2027 | Nezek Vision POC ends (billing continues) |
| Wed 3 Mar 2027 | Works committee letter |
| 8 Mar 2027 | Ayin Drive paused (billing continues) |
| Mar 2027 | Centre to planner view only; Meches Pro 9.3 turns HS Suggest on |
| 15 Mar 2027 | Tzir Assist live (status); documents feature from 20 April |
| Thu 25 Mar 2027 | Board: the former lead's deck ("7 systems, 4 regions, ₪6.2M, 0 incidents") |
| Apr 2027 | Customs QA re-check of 400 pre-fills (to the COO) |
| Wed 14 Apr 2027 | Former lead's memo to the CEO (not in the data room) |
| Sun 2 May 2027 | Tzir Docs 4.2 pushed without notice |
| Tue 18 May 2027 | Gefen finds another importer's invoice; customs query; INC-27-0518-01 opened |
| Wed 19 May | Assist documents feature switched off by IT; Gefen's email |
| Fri 21 May | Hotfix 4.2.1 |
| Sat 22 May | Ticket set to "contained" |
| Thu 27 May | Former lead resigns; handover note |
| Fri 28 May | Tzir RCA ("customer data quality") |
| Thu 3 Jun | Board special session: 30 days; interim lead appointed |
| **Sun 6 Jun** | You start (17.1) |
| 6–17 Jun | Discovery (17.2); findings to both principals Thu 17 Jun |
| Sun 20 Jun | Diagnosis and case (17.3) |
| Thu 24 Jun | Turnaround plan with both principals (17.4) |
| **Thu 1 Jul** | Last working day for the Tzir region-reduction notice (90 days before 1 Oct); audit committee pre-read |
| **Mon 5 Jul** | Board: the 30-day brief (17.6); your contract ends Tue 6 Jul |
| Jan 2028 | Six months later (the futures) |

## Planted findings (each discoverable, never stated)

Paths relative to `labs/module-17/data-room/`.

| # | Finding | Where |
|---|---|---|
| 1 | Route extended to four regions and pulled back; still "4 regions live" in the deck and dashboard | `operations/route-daily-by-depot.csv` (`routes_tool_planned` by region over time), `it/licence-usage-2027-05.csv`, `company/board-deck-ai-programme-2027-03-25.md`, `vendor/tzir-value-dashboard-2027-05.md`, `correspondence/` (COO email) |
| 2 | Route model trained on pre-war traffic; retraining never ran (feed broken since 14 Nov) | `ai/tzir-route-model-card.md`, `incident/it-tickets-ai.csv` (Mabat 401s), `operations/dispatcher-overrides-2027.csv` (reasons) |
| 3 | Savings computed by the vendor against a naive baseline | `vendor/tzir-value-dashboard-2027-05.md`, `operations/route-daily-by-depot.csv` (`km_naive_baseline` vs `km_actual`), `operations/fleet-km-fuel-monthly.csv` |
| 4 | Customs-document AI with an unreviewed error rate; review only on paper | `customs/declarations-prefill-2027-05.csv` (`review_seconds`, `fields_edited`), `customs/qa-sample-2027-04.csv`, `ai/ai-register-2027-03.csv` ("agent reviews every declaration"), the KPI in `company/` |
| 5 | Incident wider than recorded: post-fix mismatches, personal data in exposed documents, declarations submitted with another importer's values | `customs/declarations-prefill-2027-05.csv` (`doc_owner_customer` ≠ `customer_code`, `model_version`), `portal/document-access-log-2027-05.csv`, `portal/document-index-2027-05.csv`, `customs/customs-queries-2027.csv`, vs `incident/INC-27-0518-01-record.md` |
| 6 | Vendor RCA blames the customer; release notes show the unannounced normaliser change; MSA requires notice of material changes | `incident/tzir-rca-2027-05-28.md`, `incident/tzir-release-notes-4.2.md`, `vendor/tzir-msa-extract.md` |
| 7 | Invoices for licences nobody uses | `finance/ap-invoices-ai.csv` vs `it/licence-usage-2027-05.csv`; Nezek and Ayin billed after end/pause |
| 8 | Three order forms each below the ₪5M board line, ₪14.4M together | `vendor/contracts-ai.csv`, `vendor/tzir-order-forms.md`, `company/delegation-of-authority-extract.md` |
| 9 | The departed lead's deck vs reality ("7 systems, 4 regions, ₪6.2M, 0 incidents") | deck vs everything above; tickets before 25 March |
| 10 | Union grievance over driver monitoring; score used in a hearing | `people/works-committee-letter-2027-03-03.md`, `people/collective-agreement-extract.md`, tickets |
| 11 | AI outside the register (embedded, vendor release, shadow) | `finance/card-and-expense-ai-2027.csv`, `it/proxy-ai-hosts-2027-q2.csv`, `it/licence-usage-2027-05.csv`, tickets (Meches 9.3) |
| 12 | Cost overrun: budget ₪5.2M with Assist "funded from savings"; forecast ₪7.51M | `company/budget-2027-ai-and-savings.md`, `finance/ai-programme-cost-2027.csv` |
| 13 | Real value: forecast and AP matching; owner gap | `operations/warehouse-overtime-weekly.csv`, `ai/forecast-backtest-2027-04.md`, `people/staff-directory-extract.csv` |
| 14 | The region-reduction notice date (1 July) before the board | `vendor/tzir-msa-extract.md`, `vendor/contracts-ai.csv` |
| 15 | The key customer at risk (tender in September) | `customers/key-accounts.csv`, `customers/gefen-email-2027-05-19.md` |
| 16 | The April memo to the CEO | only: handover note line + Itai (phone) + Ofer (when shown the line) |

## The cast (persona pack, 9)

| Persona | Role | Type | Hidden / unlock |
|---|---|---|---|
| Dr. Ilana Shaked | External director, chair of the audit committee | Board member, principal | The external auditor asked in the Q1 review for evidence of the ₪6.2M booked savings; that is why "30 days". She has heard "something about contracts" from the internal auditor's draft plan. Unlock: ask why 30 days; agree the reporting protocol before asking for anything |
| Ofer Lavi | CEO | CEO, principal | Received the 14 April memo and said "not before the Q2 numbers"; asked for the order forms to be "kept under the line"; wants "a plan to get the savings back". Unlock: show the handover note's line and ask what the 14/4 note said; ask how the order forms were approved |
| Svetlana Morozov | CFO | CFO / finance | Booked the vendor's savings at the CEO's instruction; her note "subject to validation" was dropped from the board version; flagged the 450 Kotev seats in March. Unlock: ask how the savings line was computed and who removed the note; show telematics fuel |
| Rania Haj-Yahia | Regional operations manager, South | Middle manager who pulled the tool back | Pulled Route back on 25 Feb after routes onto closed roads and late deliveries; her deputy used the driver score in a hearing and she stopped it; the COO asked her to keep South "in the numbers". Unlock: no-blame framing and "what happened on the day you switched it off" |
| Tesfaye Worku | Driver, drivers' representative on the works committee | Works committee | Committee will declare a dispute if cameras return without agreement; drivers in the North like live traffic; would sign for route planning without individual scores, with retention limits and no disciplinary use. Unlock: ask what drivers would keep, and commit to consultation before any change |
| Dmitri Volkov | Head of IT & Information Security, incident lead | IT / security | Saw more mismatches after the hotfix but the vendor and the CEO wanted it closed; never told legal because the vendor said "no PII"; suspects the B2C manifests. Unlock: ask for the logs after 21 May and what was in the exposed documents |
| Yaniv Sasson | VP Customer Success, Tzir AI | Vendor | 4.2 was a platform release; the vendor does not consider the normaliser "material"; the dashboard baseline is naive; Tzir never built the Europe connector; will offer a "free 12-month four-region extension" to avoid the reduction notice. Unlock: ask for the release notes, the change-notice clause and the baseline definition |
| Itai Barkan | Former head of AI (one phone call) | Former owner | The 14 April memo and the reply; the order forms split at the CEO's request. Unlock: one call only; ask what he warned about, to whom and when; he will not volunteer blame |
| Orit Ben-Shushan | VP Supply Chain, Gefen Medical Distribution | Affected customer | Has a competitor's offer; tender in September; Gefen's invoices (pricing) were seen by another importer; Gefen's counsel is asking. Unlock: tell her the truth with facts, then ask what she needs to stay |

Transcripts leave hidden: Ilana's external-auditor question; Ofer's memo; Svetlana's dropped note; Rania's COO email; Tesfaye's terms; Dmitri's post-fix mismatches; Yaniv's free-extension offer; Itai's order-form split; Orit's competitor offer.

## The futures (17.6 debrief, six months later, January 2028)

1. **Blame the vendor, keep the savings.** Tzir terminated "for cause" in July without the cure
   period; incident closed as the vendor's fault, counsel never asked about the manifests; a new AI
   lead hired to "restore the savings". By January: Tzir's claim for the remaining term in
   arbitration; customs asked about a further batch of declarations; Gefen moved its imports after the
   September tender; Shuk Online learned of the exposure from a customer and complained; the booked
   savings written down in the Q3 report after the auditor's question; the new lead resigned in
   December.
2. **Switch it all off.** The board stopped every AI system on 5 July, including the forecast and AP
   matching. Customs agents fully manual (overtime +22%); Modi'in overtime back up; the Tzir fees
   still payable (no reduction notice sent); the n8n triage kept running, out of sight; the works
   committee satisfied; Gefen stayed on a 10% discount; in January the board asked why competitors'
   AI was "working" and Vantage's was not.
3. **Stop/keep with conditions (the expert path).** Notice served 1 July; stops executed; Kotev cut;
   Docs back on 28 June with the consignee check and a 5% QA sample; counsel decided the privacy and
   customs steps (in the story: the Authority notified, Shuk Online informed, the affected
   declarations corrected through the licensed agent); a works-committee agreement in September;
   the feed fixed and Route retrained; Gefen renewed with a quarterly QA report; savings restated; the
   audit committee commissioned internal audit on contract approvals and the board amended the
   delegation of authority to aggregate contracts with one vendor; a permanent head of AI in October.

What decided it: whether the incident was closed on facts before the programme was judged, and
whether "stop" and "keep" were decided per system on evidence rather than for the programme as a
whole.

## Where each finding is planted (actual numbers)

Computed from the generated files (seed 20270606) with `labs/module-17/discovery.py` and `audit.py`;
reproducible in a spreadsheet. Paths relative to `labs/module-17/data-room/`. Data room 1.8 MB
including the generator; `python generate.py` run twice gives identical files.

1. **Regions.** Share of routes dispatched as planned, by month: North 0.55 (Nov 2026), 0.68–0.72
   (Dec–Jun); South 0.35 (Jan), 0.25 (Feb), 0 from 25 Feb; Centre 0.45 (Jan), 0.60 (Feb), 0.25 (Mar),
   0 from Apr (planner view from 14 Mar); Europe 0 throughout. South late stops 4.0% / 8.0% / 3.9%.
   Seats billed 334 (310 drivers + 24 planners), active 107 (North 96 + 6; Centre 5 planners).
   Deck and dashboard: "4 regions, 310 drivers".
2. **Pre-war model.** Model card: trained Jan 2021 – Jun 2023. Mabat digest tickets weekly from
   14 Nov 2026 (HTTP 401; credentials rotated 13 Nov). North overrides 29% (HFA 17%, KRM 30%,
   KSH 56%); override reasons in North: ROAD_CLOSED 142, SECURITY_RESTRICTION 58; 994 override rows,
   42 uncoded, 30 distinct texts.
3. **Savings.** Dashboard: 10,046 routes optimised, 179,178 km "saved", ₪734,630 to date,
   ₪2.56M annualised. Telematics km per stop Dec–May vs Nov–Apr: North −4.0%, Centre −0.2%, South
   −0.1%, Europe +0.8%; North fuel ≈ ₪3.33M a year → ≈ ₪134,000. Warehouse: Modi'in overtime
   712.8 → 608.9 h/week, Ashdod 580.6 → 583.9; DiD −15.1%; ≈ ₪624,000 a year incl. agency. CS
   contacts 1,970 → 1,995 a week; Assist sessions handed to a person 49% of 2,135. Customs 31 agents
   throughout, 2 posts frozen from Jan, output ≈ 9.2 a day, KPI 9 → 12 from March, overtime 702 h in
   May. Defensible ≈ ₪0.76M of ₪6.2M.
4. **Review.** May log 5,635 declarations: median 19 s on the approval screen, 61% under 30 s, 93.4%
   with no field edited; HS source Tzir 69.2%, Meches HS Suggest 22.6%, agent 8.2%. QA April: 28/400
   = 7.0% material (CI 4.9–9.9%): HS 12, value 7, origin 5, quantity 3, consignee 1; fields accepted
   without edit 99.1%.
5. **Incident.** 70 mismatches: 63 under 4.2.0 (3–20 May; 42 submitted), 7 under 4.2.1 (23 May –
   3 Jun; 5 submitted); 23 returned by agents; 21 declaring customers, 24 document owners; owner C1022
   on 16; C1007 declaring 11 (7 submitted), C1007 documents elsewhere 7. Portal: 30 cross-customer
   opens of 22 documents by 12 customers; 6 after 19 May (portal file page); 7 Shuk Online manifests
   opened, 2,462 records (1,870 before 19 May); 3 Gefen invoices opened by others (C1141, C1073,
   C1172); Gefen opened Shuk Online's invoice on 18 May. Customs queries: 9 on mismatched
   declarations (3 Gefen, held, received 18–19 May), all open past requested dates (latest 29 May).
   Early tickets 6 and 11 May closed as "data quality". Vendor RCA counts 42.
6. **Vendor change.** Release notes 2 May; MSA 4.3 (14 days' notice); ticket "notice received same day".
7. **Licences.** May invoices with zero users: Ayin ₪18,000, Nezek ₪22,000, quote ₪9,500; Kotev 112/450.
   Billed after use stopped, Mar–May: ₪148,500.
8. **Order forms.** ₪4.86M + ₪4.68M + ₪4.87M = ₪14.41M, signed 15–17 Sep 2026, each "CEO (up to ₪5M)".
9. **Deck vs reality.** Ten minor-incident tickets before 25 March (6 Route, 3 Ayin, 1 Assist) plus the
   23 Feb driver-score data request.
10. **Works committee.** Letter 3 Mar; ticket 23 Feb; clause 14.
11. **Outside the register.** Smart Match, HS Suggest; Promptway card ₪6,333 Jan–May (US$188.40 →
    US$604.35 a month); proxy (9 weeks) api.promptway.ai 20,074 requests / 230,868 KB from CS;
    translate.freedocs.net 10,416 requests / 817,705 KB from customs; blocked chat attempts from
    Operations and Sales.
12. **Overrun.** Budget ₪5,200,000; actual + forecast ₪7,510,868 (+₪2,310,868, +44%): Assist
    ₪2,090,000 unbudgeted; pilots +₪232,500; incident and interim ₪216,000; AI team −₪228,998;
    cloud +₪1,366.
13. **Real value.** Forecast MAPE 18.4% → 11.2%; Lior Gabay sole operator; 8 contracts owned by I. Barkan.
14. **Notice.** 1 Oct anniversary − 90 days = Sat 3 Jul → Thu 1 Jul.
15. **Customer.** Gefen ₪9.4M, tender Sep 2027; e-mail 19 May.

**Audit (`audit.py`).** 19 lines: stop 7, keep 5, reduce 2, register 2, bring in 2, retire 1. May
cost ₪452,250 a month; savings once in effect ₪120,540 a month; inside 2027 ₪340,620; 2027 forecast
₪7,510,868 → ₪7,170,248; 2028 run-rate ₪4,864,520. Fees to the end of the Tzir terms from July 2027
≈ ₪10.0M; Tzir fees ≈ ₪4.32M a year.

**Differences from the first draft of these notes (the numbers above win):** overrun +44% (not
~₪7.9M); Assist hand-over 49% (not 41%); exposed records 2,462 incl. 592 after the fix; defensible
savings ≈ ₪0.76M (warehouse ₪0.62M); Gefen's shipments held at Haifa Port; the futures' 2028
run-rate is ₪4.86M; customs KPI 9 → 12 a day (not 38 → 55).
