---
id: "04.6"
module: 4
minutes: 20
practice_minutes: 90
prerequisites: ["04.4"]
objectives:
  - "Build a one-page regulatory map for an organization's AI inventory: instrument, whether it applies and why, the organization's role (actor), the obligation, the date it applies, its status and the source checked."
  - "Decide whether the GDPR and the EU AI Act reach an Israeli company with a few EU business customers, and show the reasoning step by step."
  - "Separate binding law, draft guidance and voluntary frameworks, and say for each what it asks of whom."
  - "Write the questions that go to counsel, with the facts that decide them."
volatility: implementation
sources:
  - title: "Regulation (EU) 2026/1744 (Digital Omnibus on AI), OJ L, 24.7.2026 — EUR-Lex"
    url: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202601744
  - title: "Regulation (EU) 2024/1689 (AI Act), OJ L, 12.7.2024 — EUR-Lex (Articles 2, 3, 4, 26, 50, 113, Annex III)"
    url: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689
  - title: "GDPR, Regulation (EU) 2016/679 — EUR-Lex (Article 3)"
    url: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679
  - title: "GDPR Recital 23 (offering goods or services to data subjects in the Union)"
    url: https://gdpr-info.eu/recitals/no-23/
  - title: "European Parliament Legislative Observatory — 2025/0360(COD) Digital Omnibus (GDPR amendments): awaiting committee decision"
    url: https://oeil.secure.europarl.europa.eu/oeil/en/procedure-file?reference=2025/0360(COD)
  - title: "European Commission — Adequacy decisions (Israel listed)"
    url: https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en
  - title: "Pearl Cohen — New privacy regulations in Israel govern data transfers from the EEA (30 May 2023)"
    url: https://www.pearlcohen.com/new-privacy-regulations-in-israel-govern-data-transfers-from-the-eea/
  - title: "Pearl Cohen — Major amendment to Israeli privacy law set to take effect (14 August 2025)"
    url: https://www.pearlcohen.com/major-amendment-to-israeli-privacy-law-set-to-take-effect/
  - title: "Barnea Jaffa Lande — Final PPA position statement on the obligation to appoint a DPO (22 July 2026)"
    url: https://barlaw.co.il/practice_areas/regulation/privacy-law/client_updates/position-statement-on-the-obligation-to-appoint-a-dpo-not-a-change-in-the-law-but-a-change-in-the-rules-of-the-game/
  - title: "Digital Policy Alert — PPA Directive No. 1/2024 on the responsibilities of the board of directors (12 September 2024)"
    url: https://digitalpolicyalert.org/event/22531-published-privacy-protection-authority-directive-no-12024-outlining-the-responsibilities-of-the-board-of-directors
  - title: "Chambers Practice Guides — Data Protection & Privacy 2026: Israel (updated 10 March 2026)"
    url: https://practiceguides.chambers.com/practice-guides/data-protection-privacy-2026/israel
  - title: "Ministry of Innovation, Science and Technology — Israel's Policy on Artificial Intelligence Regulation and Ethics (17 December 2023)"
    url: https://www.gov.il/en/pages/ai_2023
  - title: "NIST — AI Risk Management Framework"
    url: https://www.nist.gov/itl/ai-risk-management-framework
  - title: "ISO — ISO/IEC 42001:2023"
    url: https://www.iso.org/standard/42001
last_verified: "2026-11-02"
---

# 04.6 · Which law applies to you

"Are we compliant with the AI rules?" has no answer until you know which rules, for which system, in which role, from which date. In this lesson you build a one-page regulatory map for Harbor & Pine's AI inventory: Israeli law first, then the EU instruments that might reach a company with a handful of EU hotel customers, then the voluntary frameworks. Every row names the company's role (the actor), the obligation, the date it applies and the source you opened. At the end you have the map, a reasoned answer to "does the EU matter for us?", and the questions for counsel.

## The situation

It is Sunday 29 November 2026. The tiered inventory (04.4) has three High uses and the DPIA has a list of questions for counsel. Yoav has heard at a conference that "the EU AI Act applies to everyone who uses AI" and asks whether Harbor & Pine needs an EU compliance project before the board meeting on 28 January.

One fact matters for that question, and it is not in the data room's exports: when you asked Yaniv Carmi (B2B Sales) who the company's business customers are, he said three of them are hotel groups headquartered in Cyprus and Greece that buy furniture for their hotels in Eilat and Tel Aviv. Orders ship to the Israeli hotels and are invoiced in shekels; the groups' procurement managers in Nicosia and Athens email the B2B team, and sometimes the support address. Harbor & Pine sells and delivers only in Israel.

IBM's governance course teaches the claim card for one system under one law: the actor–source–date check. Here you do it for the whole inventory, starting with Israel.

## What to do

### Step 1 — Fix the unit: one row per instrument per use

A regulatory map is not a list of laws. Each row says: **this instrument** applies (or not, and why) **to this use**, in **this role**, with **this obligation**, from **this date**, at **this status**, according to **this source checked on this date**, and **this person** owns the evidence. Use the inventory IDs from 04.4 so the map, the inventory and the risk register link up (01.7: keep them as three documents linked by ID).

Three distinctions keep the map honest:

- **Status:** in force · in force but not yet applying · draft · proposal · voluntary. A draft guidance and a statute are different rows, even when they say similar things.
- **Actor:** the role the instrument gives Harbor & Pine — database owner (controller) or holder (processor) under Israeli privacy law; employer; deployer or provider under the AI Act. Buying a tool usually makes you the deployer; the vendor is the provider.
- **Dates:** adoption, publication, entry into force and application are different. The map records the date the obligation **applies**.

### Step 2 — Map Israel first

Harbor & Pine is an Israeli company processing Israelis' data in Israel and abroad. Israel has no AI-specific statute for a retailer: the government's AI policy (Ministry of Innovation, Science and Technology with the Ministry of Justice, 17 December 2023) recommends sector-specific regulators, a risk-based approach and "soft" regulation rather than one AI law. So the binding layer is privacy, data security, employment and labour law, applied to AI uses:

| # | Instrument | Harbor & Pine's role | What it asks (for AI uses) | Rows | Applies from | Status |
|---|---|---|---|---|---|---|
| IL-1 | Privacy Protection Law, 5741-1981, as amended by Amendment 13 | Database owner (controller); Deskly, LinguaFlow, Google as holders | Purpose limits; notice of collection with purposes, recipients and rights (s. 11); data subject rights; PPA fines | P-01, AI-01, AI-11, AI-18, AI-19 | Amendment 13 in force 14 August 2025 | In force |
| IL-2 | Same law, s. 17B1(a): duty to appoint a DPO | Possibly none — counsel decides | Public bodies, data trading, core business of ongoing systematic monitoring or large-scale sensitive data; PPA's final position statement July 2026 | Company | 14 August 2025 | In force; scope by counsel |
| IL-3 | PPA Directive 1/2024 on the board's responsibilities | Board, where processing personal data is core or high-risk | Board oversight of privacy and data-security compliance | Company | Published 12 September 2024 | Regulator directive; scope by counsel |
| IL-4 | Privacy Protection (Data Security) Regulations, 5777-2017 | Database owner | Security level per database; database definitions document; risk assessments for medium and high levels; Regulation 15 on outside providers; incident notification | P-01, AI-18, AI-11 | 8 May 2018 | In force |
| IL-5 | Privacy Protection (Transfer of Data to Databases Abroad) Regulations, 5761-2001 | Database owner transferring | A permitted route for each destination (adequate protection, consent or contractual safeguards); onward transfers with approval | P-01 (US, Ireland, Philippines), AI-18 (EU), AI-11, AI-19 (US) | In force | In force |
| IL-6 | Privacy Protection Regulations (information transferred to Israel from the EEA), 2023 | Database owner receiving EEA data | For personal data received from the EEA (not sent directly by the person): deletion, minimisation, accuracy, notice within one month | B2B hotel contacts (Step 4) | 7 August 2023, phased to 1 January 2025 | In force |
| IL-7 | Employment (Equal Opportunities) Law, 5748-1988 | Employer | No discrimination among job seekers, including in acceptance for employment | AI-01 | In force | In force |
| IL-8 | Labour case law on monitoring (*Isakov*, National Labour Court, 2011) | Employer | Legitimacy, proportionality, transparency for access to employees' digital activity | AUP §6; module 6 dashboard | 2011 | Case law |
| IL-9 | PPA draft guidance on AI systems (April 2025) | Database owner using AI | Legal basis, transparency including bot disclosure, impact assessments, generative-AI use policy, AI security | All AI uses with personal data | — | **Draft** (still a draft on 2 November 2026) |
| IL-10 | Government AI policy (December 2023) | — | Principles; sector regulators lead | — | — | Policy, not law |

Sources: Pearl Cohen (Amendment 13 effective 14 August 2025); Barnea Jaffa Lande (the final DPO position statement, 22 July 2026); Digital Policy Alert (Directive 1/2024); Chambers' 2026 Israel guide (notice items, security levels, transfers, the *Isakov* tests); Pearl Cohen (the EEA regulations, 2023); gov.il (the AI policy). Law-firm summaries are leads to the Hebrew text, not substitutes: mark them as such and let counsel confirm.

### Step 3 — Test whether the GDPR reaches the company

Work through the GDPR's territorial scope as a chain of facts, not a feeling:

1. **Establishment in the EU (Article 3(1))?** No office, staff or representative in the EU. → Not through 3(1).
2. **Offering goods or services to data subjects in the Union (Article 3(2)(a))?** Recital 23 says the question is whether the company "envisages offering goods or services to data subjects in the Union"; mere accessibility of a website is not enough, while a language or currency of a Member State with the possibility of ordering in it, or mentioning customers in the Union, can show it. Harbor & Pine prices in shekels, sells in Hebrew and English, delivers only in Israel, and the hotel groups buy for hotels in Israel. → No sign of targeting.
3. **Monitoring behaviour in the Union (Article 3(2)(b))?** No tracking of people in the EU. → No.

**Conclusion to propose:** the GDPR most likely does not apply directly to Harbor & Pine's processing of the hotel groups' contacts; counsel confirms. Two practical effects remain: the hotel groups, as EU controllers, may ask for contract terms when they send personal data to Harbor & Pine, and the European Commission lists Israel among the countries with an adequacy decision, which makes that easy. The separate Digital Omnibus proposal that would amend the GDPR (procedure 2025/0360(COD)) was still awaiting a committee decision in the European Parliament when checked; do not plan on it.

**And Israel's own EEA rule.** The 2023 regulations on information transferred to Israel from the EEA apply to personal data Harbor & Pine receives from the EEA, except data the person sends directly. A procurement manager's own email is sent directly; a list of hotel staff or guests sent by the group is not. Record the B2B contacts as IL-6's scope and ask counsel what that means for the notice and retention.

### Step 4 — Test whether the AI Act reaches the company

Same method, on the official text (EUR-Lex, checked 2 November 2026):

1. **Who is in scope (Article 2(1))?** Providers placing systems on the EU market; deployers established in the EU; and "providers and deployers of AI systems that have their place of establishment or are located in a third country, where the output produced by the AI system is used in the Union" (point (c)).
2. **What role?** A deployer is anyone "using an AI system under its authority" in a professional activity (Article 3(4)). Harbor & Pine would deploy the drafting tool; Deskly or the model provider is the provider. ChatNest would be the provider of its bot.
3. **Is output used in the Union?** A draft reply sent to a procurement manager in Nicosia is arguably output used in the Union. For every other row (Israeli customers, Israeli applicants, internal use) the output is used in Israel. → At most P-01 and AI-19, for EU contacts only. Counsel confirms.
4. **Which obligations would that trigger, and when?**

| Obligation | Actor | Harbor & Pine? | Applies from |
|---|---|---|---|
| Article 4 AI literacy: "take measures to support the development of AI literacy" of staff (as replaced by Regulation (EU) 2026/1744) | Providers and deployers | Yes, if in scope; met by the AUP and module 6's training, recorded | 2 February 2025 (Chapters I–II); the replaced text since 27 July 2026 |
| Article 5 prohibited practices; new points (ba)–(bb) on non-consensual intimate and child sexual abuse material | All | Not relevant to these uses | 2 February 2025; new points 2 December 2026 |
| Article 50(1): tell people they are interacting with an AI system | **Provider** | No for P-01 (a person sends); for AI-19 it is ChatNest's duty — put it in the contract | 2 August 2026 |
| Article 50(2): machine-readable marking of generated content | Provider | No (Harbor & Pine is not a provider); systems already on the market have until 2 December 2026 | 2 August 2026 / 2 December 2026 |
| Article 50(3)–(4): emotion recognition, deep fakes, text published to inform the public on matters of public interest | Deployer | Not triggered: private replies to customers are none of these | 2 August 2026 |
| Article 26 deployer duties for high-risk systems (Annex III, e.g. point 4(a), recruitment and filtering of applications) | Deployer | AI-01 PeopleWise is that kind of system, but its output is used in Israel → out of scope | **2 December 2027** for Annex III systems (Article 113 as amended); 2 August 2028 for Annex I systems |

The Digital Omnibus on AI, Regulation (EU) 2026/1744 of 8 July 2026, was published in the Official Journal on 24 July 2026 and entered into force on the third day after, 27 July 2026. It moved the Annex III high-risk obligations to 2 December 2027 and the Annex I ones to 2 August 2028, set 2 December 2026 for the new prohibitions and for Article 50(2) compliance by systems already on the market, and replaced Article 4. The general application date of the AI Act, 2 August 2026, is unchanged.

**Conclusion to propose to Yoav:** no EU compliance project. Record the reasoning on the map; keep one cheap measure (an AI-literacy record, which module 6's training produces anyway); put the Article 50(1) duty and EU-contact handling in any chatbot contract; and write the **triggers that reopen the question**: selling or delivering to the EU; pricing in euros or a site in an EU language; an office or staff in the EU; a customer-facing bot reachable by EU contacts; any AI that evaluates people in the EU.

### Step 5 — Put the voluntary frameworks in their place

IBM's consulting course says three instruments answer three different questions; ask which one the client means. NIST AI RMF 1.0 (voluntary, January 2023, under revision when checked) and its Generative AI Profile (NIST AI 600-1, July 2024) answer "how should we think about AI risk?" — you used them as vocabulary in 04.5. ISO/IEC 42001:2023 answers "can we prove a management system?" — a certifiable standard that a 120-person importer does not need now, but worth asking vendors about (04.3). The law answers "what must we do, by when?" None presumes the others. The US has no row: Harbor & Pine does not sell there.

### Step 6 — Write the questions for counsel and the owners

Close the map with what only counsel can answer and who holds the evidence for each row. Send facts, not conclusions:

1. Does s. 17B1(a) require us to appoint a DPO, given the PPA's final position statement (July 2026)?
2. Does Directive 1/2024 apply to our board? If not, we propose to brief the board on the policy pack anyway.
3. Which transfer route covers Deskly (US, plus Ireland and the Philippines for AI) and LinguaFlow (EU)?
4. What must the privacy notice say before the pilot (notice gaps from 04.4)?
5. Confirm that the GDPR does not apply to our B2B hotel contacts, and what the 2023 EEA regulations require for data the hotel groups send us.
6. Confirm our reading that the AI Act reaches us, if at all, only through drafts sent to EU contacts, and that Article 4 is the only obligation that follows.

## Watch out

- **"The EU AI Act applies to everyone."** It applies to defined actors with defined connections to the EU. Walk Article 2 with the facts.
- **Mixing up dates.** Entry into force is not application. The Omnibus entered into force on 27 July 2026 but moved high-risk obligations to December 2027 and August 2028.
- **Treating drafts as law, or ignoring them.** The PPA's AI guidance is a draft: follow it as the regulator's expectation, label it a draft.
- **A list of laws instead of a map.** Without the actor, the use and the date, nobody can act on a row.
- **Secondary sources as the authority.** Law-firm summaries are how you find the provision; the text (and counsel) are how you rely on it.
- **Forgetting Israel's own EU-related rule.** The EEA regulations are Israeli law; they matter more to Harbor & Pine than the GDPR does.
- **Answering the legal question yourself.** You narrow it, with facts, so counsel's hour is spent on the decision.

## Your turn

### Inputs

- Your tiered inventory and DPIA (04.4), the vendor findings (04.3).
- Data room (module download): `orders/orders.csv` (B2B ship-to cities), `policies/privacy-notice.md`, `it/peoplewise-release-notes-2026-03.md`, `vendors/deskly-ai-addon-terms.md` §5, `vendors/chatnest-sales-deck.md` slide 7 ([INDEX](../../labs/common/harbor-and-pine/INDEX.md)).
- The fact from Yaniv in "The situation" (three EU hotel groups buying for their Israeli hotels).
- The course's [laws and guidance list](../../references/laws-and-guidance.md) as a starting point; open each source yourself.
- Template: [regulatory map](../../templates/regulatory-map.md); spreadsheet `labs/module-04/regulatory-map.csv` ([lab README](../../labs/module-04/README.md)).

### Steps

1. List the instruments to test: at least eight Israeli, two EU, two voluntary.
2. For each, fill one row per relevant use: applies or not (and why), actor, obligation, rows affected, applies-from date, status, source and the date you checked it, evidence owner.
3. Write the GDPR chain (Step 3) and the AI Act chain (Step 4) for the EU hotel customers, each as numbered facts leading to a conclusion.
4. Open the AI Act and the Omnibus on EUR-Lex and check every date you wrote. Note anything that changed since 2 November 2026.
5. Write the triggers that would reopen the EU question.
6. Write the questions for counsel (at most eight) with the facts attached.

### Time

90 minutes.

### Done when

- [ ] Every row names the instrument, actor, obligation, inventory IDs, applies-from date, status, source and date checked.
- [ ] Drafts, proposals and voluntary frameworks are labelled as such.
- [ ] The GDPR chain checks establishment, targeting (with Recital 23's indicators) and monitoring, and mentions Israel's 2023 EEA regulations.
- [ ] The AI Act chain checks Article 2(1)(c), the deployer role, where output is used, and names each obligation with its date.
- [ ] Dates for the AI Act match EUR-Lex, including the Omnibus changes (2 December 2027, 2 August 2028, 2 December 2026, 27 July 2026).
- [ ] The answer to Yoav is one paragraph with a recommendation and reopening triggers.
- [ ] Legal conclusions are proposed to counsel, not asserted.

<details><summary>Reference answer</summary>

**Map (excerpt, 30 November 2026).** IL-1 to IL-10 as in Step 2, plus:

| # | Instrument | Applies? | Actor | Obligation | Rows | Applies from | Status | Source (checked) | Evidence owner |
|---|---|---|---|---|---|---|---|---|---|
| EU-1 | GDPR | Most likely not (no establishment, no targeting, no monitoring) — counsel to confirm | — (EU hotel groups are controllers for their own data) | Contract terms if the groups ask | B2B contacts | — | In force | EUR-Lex Art. 3; Recital 23 (2 Nov 2026) | Yaniv |
| EU-2 | GDPR amendments (Digital Omnibus proposal) | No effect | — | — | — | — | Proposal, awaiting committee decision | OEIL 2025/0360(COD) (2 Nov 2026) | You |
| EU-3 | AI Act Art. 4 | Arguably, via drafts to EU contacts | Deployer | AI-literacy measures for staff | P-01 | 2 Feb 2025; text replaced 27 Jul 2026 | In force | EUR-Lex 2024/1689, 2026/1744 (2 Nov 2026) | Dana (training records) |
| EU-4 | AI Act Art. 50(1) | Not for P-01; ChatNest's duty for AI-19 | Provider | Disclose AI interaction | AI-19 | 2 Aug 2026 | Applies | EUR-Lex | Contract clause: Ronit |
| EU-5 | AI Act Art. 26 + Annex III 4(a) | No — output used in Israel | Would be deployer | Deployer duties for high-risk | AI-01 | 2 Dec 2027 | In force, not yet applying | EUR-Lex 2026/1744 Art. 1(40) | Dana |
| ST-1 | NIST AI RMF 1.0 + AI 600-1 | Voluntary | — | Vocabulary for the risk register | All | — | Voluntary; RMF under revision | nist.gov (2 Nov 2026) | You |
| ST-2 | ISO/IEC 42001:2023 | Not now | — | Ask vendors for certificates and scope | AI-14, AI-19 | — | Published standard | iso.org (2 Nov 2026) | Avi |

**Answer to Yoav.** "No EU compliance project is needed. We sell and deliver only in Israel, in shekels, so the GDPR does not reach us directly, and the AI Act could touch us only through AI-drafted replies to the three hotel groups' managers in Cyprus and Greece — which would require only that our staff are trained on AI, which module 6 does anyway. Counsel is confirming both readings. The legal work that matters is Israeli: the privacy notice, the transfer route for Deskly and the DPO question. We reopen the EU question if we start selling to the EU, price in euros, open an office there, or put a chatbot where EU contacts can reach it."

**Dates checked on EUR-Lex.** Omnibus: Regulation (EU) 2026/1744 of 8 July 2026, OJ 24 July 2026, in force 27 July 2026. Annex III high-risk: 2 December 2027. Annex I: 2 August 2028. New Article 5 points and Article 50(2) for systems already on the market: 2 December 2026. Articles 102–110: 27 July 2026. AI Act general application: 2 August 2026; Chapters I–II: 2 February 2025.

</details>

## References

- EUR-Lex: [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689) (AI Act) and [Regulation (EU) 2026/1744](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202601744) (Digital Omnibus on AI), both opened 2 November 2026; [GDPR](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679) Article 3 and [Recital 23](https://gdpr-info.eu/recitals/no-23/).
- European Parliament, [Legislative Observatory 2025/0360(COD)](https://oeil.secure.europarl.europa.eu/oeil/en/procedure-file?reference=2025/0360(COD)); European Commission, [adequacy decisions](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en).
- Israel: Pearl Cohen on [Amendment 13](https://www.pearlcohen.com/major-amendment-to-israeli-privacy-law-set-to-take-effect/) and on the [2023 EEA regulations](https://www.pearlcohen.com/new-privacy-regulations-in-israel-govern-data-transfers-from-the-eea/); Barnea Jaffa Lande on the [final DPO position statement](https://barlaw.co.il/practice_areas/regulation/privacy-law/client_updates/position-statement-on-the-obligation-to-appoint-a-dpo-not-a-change-in-the-law-but-a-change-in-the-rules-of-the-game/); Digital Policy Alert on [Directive 1/2024](https://digitalpolicyalert.org/event/22531-published-privacy-protection-authority-directive-no-12024-outlining-the-responsibilities-of-the-board-of-directors); Chambers, [Data Protection & Privacy 2026: Israel](https://practiceguides.chambers.com/practice-guides/data-protection-privacy-2026/israel); [Israel's Policy on AI Regulation and Ethics](https://www.gov.il/en/pages/ai_2023) (December 2023).
- NIST, [AI RMF](https://www.nist.gov/itl/ai-risk-management-framework); ISO, [ISO/IEC 42001](https://www.iso.org/standard/42001).
- The course's [laws and guidance list](../../references/laws-and-guidance.md). Template: [regulatory map](../../templates/regulatory-map.md).
- Previous: [04.5 · Risk register from zero](lesson-05.md). Next: [04.7 · Governance that runs](lesson-07.md). Later: engagements 9–12 and 15 add sector regulators.
