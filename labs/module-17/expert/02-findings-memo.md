# 02 · Findings memo

*To: Ofer Lavi and Dr. Ilana Shaked (same day, same words, per the protocol). From: the interim AI lead. Thursday 17 June 2027. Labels: **M** measured from Vantage's own data, **R** reported by a person, **C** claimed by a vendor or a document. An incident status note went to both on Thursday 10 June; this memo includes it.*

## The answer first

The programme is not what the board was told, and the incident is not closed. Twelve AI systems run, not seven; the route tool is used in one region of four; the savings are about an eighth of the ₪6.2M booked; the programme will cost about ₪7.5M against ₪5.2M budgeted; and between 3 May and 3 June the customs module matched 70 declarations to another importer's documents, including 7 after the vendor's fix, while customers kept opening other customers' documents through the portal after the feature that was switched off. Two systems deliver measured value and must be kept: the warehouse forecast and the route tool in the North.

## 1. The incident is open, and wider than recorded

- **Mismatches did not stop at the fix (M).** Pre-fill log: 63 declarations matched to another importer's invoice under release 4.2.0 (3–20 May) and **7 more under 4.2.1** (23 May – 3 June), all with invoice numbers without letters. 47 of the 70 were submitted to Customs (42 + 5); agents caught 23.
- **Switching off the Assist feature did not remove access (M).** Portal access log: 30 opens of 22 misattached documents by users of 12 other customers; **6 opens after 19 May**, all through the ordinary portal file page.
- **Personal data was involved (M).** Of the 22 documents opened by others, 7 are B2C manifests of Shuk Online Imports with consignees' names, street addresses and phones: **2,462 records**, 1,870 opened before 19 May and 592 after. The incident record says "none (per vendor)".
- **Customs (M).** 9 customs queries on mismatched declarations, 3 with goods held (Gefen's, 18–19 May); all 9 still "open" with the requested response dates passed (latest 29 May).
- **Early signals were closed (M).** Tickets of 6 and 11 May ("another importer's name on invoice", "wrong packing list") closed by the vendor as "data quality".
- **Legal never saw it (R, Dmitri; M, incident record "Legal: n/a").** Briefed to Yael Sharabi on Tuesday 8 June with the facts above as they were then known. Whether and what to report under the Privacy Protection Law and the Data Security Regulations, and what to tell Shuk Online, is hers and outside counsel's to decide; she has the logs.
- **Gefen (M, R).** 11 of the 70 were Gefen's declarations (7 submitted); 7 Gefen documents were attached to other importers' files and 3 were opened by others. Gefen's letter of 19 May had no written answer until 24 June.

## 2. The review step exists on paper

- Median **19 seconds** on the approval screen; 61% under 30 seconds; no field edited on 93.4% of declarations (M, May log).
- The customs team's April re-check: **28 of 400 with a material error, 7.0%** (95% interval 4.9–9.9%) — mostly tariff codes and values (M). The vendor's "99.2% accuracy" is the share of fields not edited, 99.1% in the same sample (M).
- The KPI went from 9 to 12 declarations per agent per day in March; agents' actual output stayed at about 9.2 a day because volume did not grow (M, staffing file; R, Shlomo's e-mail).
- A second AI source of tariff codes runs beside Tzir Docs: **Meches Pro "HS Suggest"**, on by default since release 9.3 (March), the source of 22.6% of May's codes (M).

## 3. Route: extended to four regions, pulled back to one

- Share of routes dispatched as the tool planned, May: North 0.68, Centre 0, South 0, Europe 0 (M). South stopped on 25 February, Centre went to planner view on 14 March, Europe was never connected (M, tickets; R, Rania).
- South late stops: 4.0% before, **8.0% with the tool**, 3.9% after the pull-back (M).
- North overrides 29% of plans; Kiryat Shmona 56%, mostly "road closed" and "military zone" in Hebrew, Arabic, Russian, Amharic and English (M). The model was trained on 2021 – June 2023 traffic (C, model card); its customer retraining needs the telematics feed, which has failed every night since 14 November (M, tickets).
- Billed: 334 seats; active in 30 days: 107 (M).

## 4. The savings are the vendor's arithmetic

| Line | Booked | Evidence | Label |
|---|---|---|---|
| Fuel and km | ₪3,100,000 | Telematics km per stop: North −4.0%, others flat (≈ ₪134,000 a year of fuel in the North) | M (directional: no control region) |
| Customs productivity | ₪1,600,000 | 31 agents before and after; overtime up in May; 2 posts frozen since January | M: no cash; capacity at most |
| CS deflection | ₪900,000 | Contacts a week 1,970 before Assist, 1,995 after; 49% of sessions handed to a person | M: none |
| Warehouse overtime | ₪600,000 | Modi'in overtime −15.1% against Ashdod (difference in differences), ≈ ₪624,000 a year incl. agency | M |
| **Total** | **₪6,200,000** | **≈ ₪760,000** | |

The vendor dashboard's ₪2.56M a year is "naive baseline km − plan km × ₪4.10", for all licensed regions; it never uses the kilometres the trucks drove (C, methodology).

## 5. Twelve systems, not seven

Register (8): Route, Docs, Assist, Kotev Assist, Ayin Drive, Nezek Vision, the quote add-in, the warehouse forecast. Outside it (4): **Mishkal Smart Match** (AP matching, an ERP module), **Meches Pro HS Suggest**, **Customer Service's e-mail triage** on n8n with the public Promptway API, paid on the CS manager's card (₪6,333 January–May, rising; 20,074 requests and 231 MB uploaded in nine weeks), and **a free online translator** customs clerks use for supplier invoices (10,416 requests, 818 MB uploaded). The Tzir value dashboard is a report, not an AI system. The **driver score** is a feature of Route used on people (R2 in the audit rules).

## 6. Licences, contracts and money

- Billed in May for zero users: Ayin Drive (₪18,000), Nezek Vision (₪22,000), the quote add-in (₪9,500) (M). Kotev Assist: 112 of 450 active (M).
- Cost centre 7700-AI: ₪7.51M actual plus forecast against ₪5.2M (+44%); Tzir Assist (₪2.09M in 2027) had no budget line (M).
- Three Tzir order forms signed 15–17 September 2026, ₪4.86M, ₪4.68M and ₪4.87M, together **₪14.41M**, each recorded as "CEO (up to ₪5M)" (M). Facts for the committee; no conclusion here.
- Region reduction under MSA 7.4: notice by **Thursday 1 July** for 1 October (M).

## 7. People

- The works committee's letter of 3 March is unanswered in writing; a driver was summoned to a hearing on the basis of the score on 24 February (cancelled the next day) (M, letter and tickets; R, Tesfaye). The committee has voted to declare a dispute if cameras or scores return without agreement (R).
- The warehouse forecast is run by one person (Lior Gabay) whose manager has left (M, directory).
- Eight AI contracts list Itai Barkan as business owner (M).

## What I did not look at, and why

The decision to report the incident and its content (counsel's); employment questions about the hearing (HR's); the approval of the order forms (the committee's); the former lead's mailbox (the board secretary is retrieving the 14 April note through the mail system).
