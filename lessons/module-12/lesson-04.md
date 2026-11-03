---
id: "12.4"
module: 12
minutes: 24
practice_minutes: 150
prerequisites: ["12.3", "04.1", "04.2", "04.6", "04.8"]
objectives:
  - "Separate, for a law firm's AI use, what the rules on confidentiality and privilege say, what the Bar's ethics opinions say, what counsel's view is and what is a business decision, and route each to its owner."
  - "Explain from primary sources what the fabricated-citation cases show, and turn them into a citation check that a research answer must pass before a partner sees it."
  - "Show why time saved is not money earned in an hourly firm, and propose pricing that keeps part of the gain, tested with the client who will take the rest."
  - "Read back a legal-AI vendor's claims and contract under the conditions they were made, and write the decision paper for the second exit point."
volatility: implementation
sources:
  - title: "Rules of the Israel Bar Association (Professional Ethics), 5746-1986, rule 19 confidentiality (Hebrew Wikisource)"
    url: https://he.wikisource.org/wiki/%D7%9B%D7%9C%D7%9C%D7%99_%D7%9C%D7%A9%D7%9B%D7%AA_%D7%A2%D7%95%D7%A8%D7%9B%D7%99_%D7%94%D7%93%D7%99%D7%9F_%28%D7%90%D7%AA%D7%99%D7%A7%D7%94_%D7%9E%D7%A7%D7%A6%D7%95%D7%A2%D7%99%D7%AA%29
  - title: "Israel Bar Association Law, 5721-1961, section 90 professional privilege (Hebrew Wikisource)"
    url: https://he.wikisource.org/wiki/%D7%97%D7%95%D7%A7_%D7%9C%D7%A9%D7%9B%D7%AA_%D7%A2%D7%95%D7%A8%D7%9B%D7%99_%D7%94%D7%93%D7%99%D7%9F
  - title: "Pearl Cohen, Israeli Bar Association's ethical guidelines on using AI (National Ethics Committee, 7 May 2024)"
    url: https://www.pearlcohen.com/israeli-bar-associations-ethical-guidelines-on-using-ai/
  - title: "Calcalist, 17 September 2026: the Bar Association's ethics committee publishes an expanded, stricter opinion on AI (signed by Adv. Menachem Moshkovitz, chair)"
    url: https://www.calcalist.co.il/local_news/article/bkqvhskyfe
  - title: "Pearl Cohen, Israel Bar Association issues an expanded ethics opinion on lawyers' use of AI (29 September 2026)"
    url: https://www.pearlcohen.com/israel-bar-association-issues-an-expanded-ethics-opinion-on-lawyers-use-of-ai/
  - title: "Mata v. Avianca, Inc., 678 F. Supp. 3d 443 (S.D.N.Y. 22 June 2023), opinion and order on sanctions (copy hosted by CLLA)"
    url: https://national.clla.org/wp-content/uploads/2025/05/Mata-v-Avianca-Inc.pdf
  - title: "Ayinde v London Borough of Haringey; Al-Haroun v Qatar National Bank [2025] EWHC 1383 (Admin), Divisional Court, 6 June 2025"
    url: https://www.judiciary.uk/judgments/ayinde-v-london-borough-of-haringey-and-al-haroun-v-qatar-national-bank/
  - title: "Jerusalem Post, 24 February 2025: Supreme Court Justice Gila Canfy-Steinitz calls out a lawyer for citing AI-generated non-existent rulings"
    url: https://www.jpost.com/israel-news/article-843442
  - title: "Ynetnews: Tel Aviv District Court, class action against AIG withdrawn; five non-existent decisions cited; ₪20,000 costs"
    url: https://www.ynetnews.com/business/article/sjurpf3pgx
  - title: "Barnea Jaffa Lande, 29 March 2026: Cohen v. Ramat Gan Municipality, Adm. Appeal 63194-08-25 (22 March 2026), ₪30,000 costs for fictitious sources"
    url: https://barlaw.co.il/practice_areas/high-tech/ai-regulation/client_updates/have-you-been-using-ai-without-verifying-it-could-cost-you-ils-30000/
  - title: "Magesh et al., Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools (arXiv 2405.20362, 2024): 17%-33% hallucination rates"
    url: https://arxiv.org/abs/2405.20362
  - title: "NatLawReview on ABA Formal Opinion 512 (29 July 2024): fees, consent, boilerplate engagement terms not sufficient"
    url: https://natlawreview.com/article/american-bar-association-issues-formal-opinion-use-generative-ai-tools
  - title: "IAPP, Amendment 13 to Israel's Privacy Protection Law (in force 14 August 2025)"
    url: https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform
last_verified: "2026-11-02"
---

# 12.4 · The hard part

This is the lesson the engagement is about. A law firm cannot treat AI as a productivity tool like any other, for three reasons that pull in different directions: what it owes clients in confidence, what it owes courts in accuracy, and what it earns by the hour. In this lesson you read the confidentiality and privilege position with the firm's ethics partner, learn from the fabricated-citation cases what a check must catch, work out with the client who will take a share of any gain what pricing she would accept, read back the vendor's claims and contract, and write the decision paper for the second exit point. At the end you have a decision paper and a draft interim rule for counsel.

## The situation

Tuesday 8 to Thursday 17 December 2026; Hanukkah runs to the 12th. The committee let you continue on 3 December. You have met Orit Levinson, the general counsel and ethics partner ([persona](../../labs/module-12/personas/orit-ethics-partner.md), [transcript](../../labs/module-12/personas/transcripts/orit-ethics-partner.md)); on 8 December you meet Sigal Mizrahi, general counsel of Carmel Retail Group ([persona](../../labs/module-12/personas/sigal-client-gc.md), [transcript](../../labs/module-12/personas/transcripts/sigal-client-gc.md)). Parshan's discount expires on 31 December. Your decision paper is due on Thursday 17 December, the second exit point.

> [!IMPORTANT]
> You are not the firm's lawyer and this course is not legal advice. Every legal or ethical reading in your paper is attributed to the ethics partner or to the source she points to, and the open questions go to outside ethics counsel. Your job is to put the facts and the decisions in front of the right people.

IBM's governance course gives you the *Responsible-AI gate* and *consequence-if-wrong*; module 4 turned them into a policy pack. Here you apply both in a profession whose rules were written long before AI and are being reinterpreted now.

## What to do

### Step 1 — Confidentiality and privilege: rule, opinion, view, decision

Build a four-column table with Orit and keep the columns apart. The rules and opinions below were opened on 2 November 2026; read them yourself and let her interpret them.

| | What it says | Source | Owner |
|---|---|---|---|
| **The rule: confidentiality** | A lawyer keeps confidential anything a client, or someone on the client's behalf, brought to their knowledge, unless the client expressly agrees otherwise | Rules of the Israel Bar Association (Professional Ethics) (כללי לשכת עורכי הדין (אתיקה מקצועית), התשמ"ו-1986), [rule 19](https://he.wikisource.org/wiki/%D7%9B%D7%9C%D7%9C%D7%99_%D7%9C%D7%A9%D7%9B%D7%AA_%D7%A2%D7%95%D7%A8%D7%9B%D7%99_%D7%94%D7%93%D7%99%D7%9F_%28%D7%90%D7%AA%D7%99%D7%A7%D7%94_%D7%9E%D7%A7%D7%A6%D7%95%D7%A2%D7%99%D7%AA%29) | Orit |
| **The rule: privilege** | Documents and communications exchanged between client and lawyer, connected to the service, are not disclosed in proceedings, investigations or searches unless the client waives | Israel Bar Association Law (חוק לשכת עורכי הדין, התשכ"א-1961), [section 90](https://he.wikisource.org/wiki/%D7%97%D7%95%D7%A7_%D7%9C%D7%A9%D7%9B%D7%AA_%D7%A2%D7%95%D7%A8%D7%9B%D7%99_%D7%94%D7%93%D7%99%D7%9F) | Orit |
| **The profession's opinion, 2024** | Verify AI output; avoid personal or sensitive client information in AI systems; written consent before client information goes into open systems; prefer closed systems | National Ethics Committee guidance, 7 May 2024, as summarised by [Pearl Cohen](https://www.pearlcohen.com/israeli-bar-associations-ethical-guidelines-on-using-ai/) | Orit |
| **The profession's opinion, 2026** | Full personal responsibility; verify every output; no restricted information in open, unsecured platforms, and simple anonymisation is not enough; explicit, informed consent in advance, and a general clause in a retainer or power of attorney is not enough; closed platforms still need a risk review and access limits; AI agents only for defined, reversible, supervised technical steps; tell the client when AI use bears on the fee or expenses | Expanded opinion, September 2026, as reported by [Calcalist](https://www.calcalist.co.il/local_news/article/bkqvhskyfe) (17 September) and [Pearl Cohen](https://www.pearlcohen.com/israel-bar-association-issues-an-expanded-ethics-opinion-on-lawyers-use-of-ai/) | Orit and outside ethics counsel |
| **Personal data** | Client documents carry personal data; Amendment 13 to the Privacy Protection Law raised the stakes from 14 August 2025 | [IAPP](https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform) | Privacy owner (Orit) |
| **Business decisions** | Which tool, which clients first, what consent process, what to tell the insurer | — | Management committee, partners |

The full text of the 2026 opinion is on the Bar Association's site in Hebrew; the summaries above are secondary. Ask Orit for the text and read it with her.

Then put the firm's facts against the table: consumer AI use by at least 52 lawyers, 27 of them uploading files; a client-confidential draft SPA uploaded on 3 September and closed without telling the client; an engagement-letter clause 11 ("we may use technology tools") written for cloud storage in 2023; four clients whose guidelines carry AI terms, Carmel's the strictest (disclose, consent, verify, no hourly for time technology would save, 48-hour incident notice). You do not say any of this is a breach. You say it is the firm's starting point, and that no platform purchase changes it: as the 2026 opinion is reported, a closed platform still needs consent, a risk review and access limits.

### Step 2 — What the fabricated-citation cases show

Read the primary sources, not the headlines:

- **Mata v. Avianca** (S.D.N.Y., 22 June 2023, Judge P. Kevin Castel). Lawyers filed an affirmation citing six opinions that did not exist, produced by ChatGPT, and stood by them after the court questioned them. The court found subjective bad faith and imposed a US$5,000 penalty, plus letters to the client and to each judge falsely named as an author. The court said there is nothing inherently improper in using a reliable AI tool, but that existing rules give lawyers a "gatekeeping role" ([opinion](https://national.clla.org/wp-content/uploads/2025/05/Mata-v-Avianca-Inc.pdf)).
- **Ayinde v Haringey; Al-Haroun v Qatar National Bank** (High Court of England and Wales, Divisional Court, 6 June 2025). In one case a barrister cited five cases that did not exist; in the other a solicitor relied on research his own client had done without checking the authorities. The court said practical and effective measures must now be taken by those with leadership responsibilities, naming heads of chambers and **managing partners** ([judgment](https://www.judiciary.uk/judgments/ayinde-v-london-borough-of-haringey-and-al-haroun-v-qatar-national-bank/)). That sentence is addressed to Yoav's job.
- **Israel.** In February 2025 Supreme Court Justice Gila Canfy-Steinitz rejected a petition whose lawyer cited rulings that did not exist and warned lawyers against relying on AI without checking ([Jerusalem Post](https://www.jpost.com/israel-news/article-843442), 24 February 2025). The Tel Aviv District Court ordered ₪20,000 costs against a plaintiff who withdrew a class action against AIG after his lawyer cited five decisions the judge said do not exist ([Ynetnews](https://www.ynetnews.com/business/article/sjurpf3pgx)). On 22 March 2026 the Supreme Court ordered the Ramat Gan municipality to pay ₪30,000 in exceptional costs for relying on a non-existent ministry circular and misdescribed rulings (Adm. Appeal 63194-08-25, reported by [Barnea](https://barlaw.co.il/practice_areas/high-tech/ai-regulation/client_updates/have-you-been-using-ai-without-verifying-it-could-cost-you-ils-30000/)). Read the judgments themselves before citing them in a client document.
- **Grounded tools still err.** Stanford researchers found the leading legal research tools built on retrieval produced hallucinations between 17% and 33% of the time on their benchmark (Magesh et al., [2024](https://arxiv.org/abs/2405.20362)). "Grounded in your documents" is a design, not a guarantee.

What these cases have in common is the failure mode in the firm's own October memo: an invented authority, a real one that no longer says what it is cited for, and a supervisor who signs because it looks right. Turn that into a **citation gate**, five checks that a research answer must pass before it reaches a partner:

1. The cited document exists in the corpus.
2. The cited paragraph exists.
3. Any quotation is word for word in that paragraph.
4. The document is current (not reversed, replaced or withdrawn).
5. The paragraph says what the sentence claims.

The first four are rules a script or a spreadsheet can run. The fifth is judgement. You will build and measure all five in 12.5.

### Step 3 — The billable hour, with the client in the room

In 12.3 you showed that on hourly work a saved hour is a lost fee and that clients re-price faster work. Now test pricing with the person who will take her share. Interview Sigal (roleplay or transcript). Ask what her board needs, not whether 15% is fair. What you learn shapes the recommendation:

- She wants **fixed prices for repeat work** (supplier agreements, leases, employment documents), a **quarterly subscription** for routine advice, and hourly only for disputes and deals; she would accept a package about 10% below this year's spend on that work if it is predictable.
- Her conditions for consenting to AI on Carmel matters: an enterprise tool that does not train on Carmel data and deletes it; being told which; every citation verified and documented; any problem heard from the firm, not from a court.

Three pricing moves follow, each with an owner:

| Move | What it does | Owner |
|---|---|---|
| Fixed prices for repeat work, set before the hours fall | The firm keeps part of the gain (the NDA history: ₪1,422 an hour instead of ₪860) | Eli and the group partners |
| Hourly kept for disputes and deals, with AI disclosed where it bears on the fee | Meets the client's guideline and the 2026 opinion's disclosure point | Orit (wording), partners |
| Reject the draft policy's "bill the time a task would normally take" | It bills time not spent; it goes to outside ethics counsel | Orit |

US clients will quote ABA Formal Opinion 512 (29 July 2024): lawyers may not bill for time they did not spend or for learning a tool, efficiencies should reach the client through fees, and boilerplate engagement terms are not informed consent ([NatLawReview summary](https://natlawreview.com/article/american-bar-association-issues-formal-opinion-use-generative-ai-tools)). It binds no Israeli lawyer; it tells you what international clients expect.

### Step 4 — Read back the vendor, then the contract

Use the [claim read-back](../../templates/claim-read-back.md) and the [vendor AI questionnaire](../../templates/vendor-ai-questionnaire.md) from [04.3](../module-04/lesson-03.md) and [04.8](../module-04/lesson-08.md):

| Claim | Under what conditions | What would change your view |
|---|---|---|
| "Lawyers save 6.2 hours a week" | Self-reported survey, 212 lawyers, 9 US and UK firms, Q1 2026 | Time measured on the firm's own work |
| "Zero hallucinations" | Demo: 12 English questions on US case law in the vendor's environment | Its own PoC on the firm's 78 documents: 28 of 80 citations fail a basic check (10 stale, 12 misstated) |
| "Your whole DMS in 48 hours" | Permissions follow the DMS only for iManage and NetDocuments; the firm's DMS is not one | An index limited to curated, permissioned collections |
| Hebrew | Beta; citation checking in English only | Tested on Hebrew questions |

Then the order form: §3 sub-processors may keep prompts and outputs up to 30 days and change on 14 days' notice; §4 lets the vendor use "aggregated and de-identified usage data and Customer feedback to improve the Service" (the very clause the firm's own data-processing memos warn about); §8 caps liability at 12 months' fees and excludes the content of outputs; §10 allows no termination for convenience during 24 months. Changes to ask for before any signature: 30 seats and 12 months, termination for convenience, §4 narrowed, a sub-processor list with a right to object, indexing limited to curated collections, a higher cap for confidentiality breaches. And the method for choosing, from module 10: an RFP with a proof of concept on the firm's curated corpus, in Hebrew and English, scored on the gate.

[Simulation: Vendor RFP](../../simulations/vendor-rfp/index.html?preset=generic)

The generic scenario is not a legal-AI tender; use it to practise scoring on evidence after the "demo conditions" reveal, which is exactly what Parshan's demo needs.

### Step 5 — The interim rule and the decision paper

Draft an interim rule for Orit to mark up (two pages; [acceptable-use policy](../../templates/acceptable-use-policy.md) and [approved / restricted use list](../../templates/approved-restricted-use-list.md) from [04.1](../module-04/lesson-01.md) and [04.2](../module-04/lesson-02.md)): no client information in any AI tool except the approved enterprise one, under a written agreement with no training and deletion; consumer accounts on firm work end; every authority checked through the gate before a partner signs; incidents to the ethics partner within a day; consent by matter class, starting with the four clients with AI terms.

Then the [decision-ready case](../../templates/decision-ready-case.md) for 17 December: approve the interim rule to counsel, one enterprise assistant, curation, the two-group pilot with the gate, a fixed-price proposal for Carmel; decline signing Parshan in December. Say what a no means, and what the 31 December discount is worth against a two-year, 90-seat commitment that has not been tested on the firm's material.

## Watch out

- **Saying "privileged" or "breach".** You report facts and route them. The ethics partner and outside ethics counsel interpret rule 19, section 90 and the Bar's opinions.
- **Foreign cases as Israeli law.** Mata and Ayinde bind no Israeli court. They show the failure mode and, in Ayinde, who is expected to act. Israeli courts have now said the same in their own decisions.
- **"Anonymised, so it's fine."** As reported, the 2026 opinion treats anonymisation as insufficient on its own; a deal can be recognised from its terms.
- **"The platform solves confidentiality."** A closed platform still needs consent, a risk review and access limits, and a whole-DMS index that ignores ethical walls creates a new problem.
- **Negotiating for the firm.** In Sigal's interview you learn; Yoav and Eli negotiate. Report her words exactly.
- **Letting the discount decide.** A two-year, 90-seat commitment that has not been tested on the firm's own documents is not made cheaper by 20%.

## Your turn

### Inputs

- Data room (module download): `policies/engagement-letter-template-2023.md`, `policies/draft-ai-policy-2026.md`, `policies/it-acceptable-use-2019.md`, `clients/carmel-ocg-2026.md`, `clients/clients.csv`, `it/dlp-alerts-2026.csv`, `risk/ethics-log-2026.csv`, `risk/pi-renewal-questionnaire-2027.md`, `vendor/parshan-demo-deck.md`, `vendor/parshan-order-form.md`, `vendor/parshan-security-answers.md`, `research/memo-non-compete-draft-v2.md`.
- Personas: [Orit](../../labs/module-12/personas/orit-ethics-partner.md), [Sigal](../../labs/module-12/personas/sigal-client-gc.md), [Noa](../../labs/module-12/personas/noa-tech-partner.md), with transcripts in `labs/module-12/personas/transcripts/`; [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [regulatory map](../../templates/regulatory-map.md), [acceptable-use policy](../../templates/acceptable-use-policy.md), [approved / restricted use list](../../templates/approved-restricted-use-list.md), [claim read-back](../../templates/claim-read-back.md), [vendor AI questionnaire](../../templates/vendor-ai-questionnaire.md), [risk register](../../templates/risk-register.md), [decision-ready case](../../templates/decision-ready-case.md).

### Steps

1. Build the four-column table (rule, opinion, view, decision) with Orit, from the sources; list the open questions for outside ethics counsel.
2. Write one paragraph per case (Mata, Ayinde, the three Israeli decisions) from the primary or reported source: what happened, what the court said, what it means for the gate.
3. Interview Sigal; write her needs and conditions in her words, and three pricing moves with owners.
4. Read back the vendor's four claims and list the contract changes.
5. Draft the interim rule (two pages) for Orit.
6. Write the decision paper for 17 December.

### Time

150 minutes: 35 for the ethics table with Orit, 25 for the cases, 25 for Sigal and pricing, 25 for the vendor, 20 for the interim rule, 20 for the decision paper.

### Done when

- [ ] Every legal or ethical statement is attributed to a source or to the ethics partner; none is in your voice.
- [ ] The citation gate's five checks are written, and each case is tied to the check it shows.
- [ ] Pricing is tested with the client: her needs, her conditions for consent and three pricing moves with owners.
- [ ] The vendor read-back states each claim's conditions and what would change your view; contract changes are listed.
- [ ] The interim rule covers tools, client information, verification, incidents and consent, and goes to counsel, not to the partners directly.
- [ ] The decision paper asks one decision and declines the December signature with its evidence.

<details><summary>Reference answer</summary>

The full paper is `labs/module-12/expert/04-decision-paper.md`. Its core:

**Ethics table:** rule 19 (confidentiality unless the client expressly agrees otherwise) and section 90 (privilege in proceedings unless waived), read by Orit; the 2024 guidance and the 2026 expanded opinion (verify everything, no restricted information in open systems, informed consent with a general retainer clause not enough, closed platforms still need risk review and access limits, agents supervised, disclosure where AI bears on fees), read by Orit with outside ethics counsel. Open questions for outside counsel: must the client of the 3 September upload be told; is clause 11 consent (Orit's view: unlikely); may the draft policy's billing clause stand; what to answer the insurer at 6.5 and 6.6.

**Cases and the gate:** Mata (six invented opinions; US$5,000; letters to the client and judges) → checks 1–2; Ayinde (invented cases; a solicitor relying on a client's research; leaders including managing partners must take practical measures) → the gate as a firm rule, owned by the managing partner; Israel 2025–2026 (non-existent rulings criticised; ₪20,000 costs in the AIG withdrawal; ₪30,000 against Ramat Gan) → checks 1, 4 and 5; Stanford's 17–33% → grounding does not remove check 5.

**Sigal:** fixed prices for repeat work, a quarterly advice subscription, hourly for disputes and deals; a package about 10% below 2026 spend is defensible; consent if the tool is enterprise-grade without training, she is told which, citations are verified and documented, and incidents come from the firm.

**Vendor:** 6.2 h self-reported elsewhere; "zero hallucinations" vs 28 of 80 PoC citations failing (none invented); whole-DMS index without the firm's walls; Hebrew beta. Contract: 30 seats, 12 months, termination for convenience, §4 narrowed, sub-processor objection, curated collections only, higher cap for confidentiality.

**Decision asked (17 December):** approve the interim rule to counsel (18 December), one enterprise assistant from January, curation (78 research documents by 31 December, top 300 by the end of February), the two-group pilot with the gate (evaluated by 7 January), a Carmel fixed-price proposal by 15 January; decline signing Parshan in December; RFP with a corpus PoC for a June decision.

**What the transcripts' interviewers missed:** Orit was never asked about insurance (the questionnaire asks about near misses, due 15 January) and was not told of the near miss; Sigal was never asked who else she is talking to (a rival firm is already doing 30 supplier agreements at fixed prices).

</details>

## References

- Rules and opinions: Rules of the Israel Bar Association (Professional Ethics), 5746-1986, [rule 19](https://he.wikisource.org/wiki/%D7%9B%D7%9C%D7%9C%D7%99_%D7%9C%D7%A9%D7%9B%D7%AA_%D7%A2%D7%95%D7%A8%D7%9B%D7%99_%D7%94%D7%93%D7%99%D7%9F_%28%D7%90%D7%AA%D7%99%D7%A7%D7%94_%D7%9E%D7%A7%D7%A6%D7%95%D7%A2%D7%99%D7%AA%29); Israel Bar Association Law, 5721-1961, [section 90](https://he.wikisource.org/wiki/%D7%97%D7%95%D7%A7_%D7%9C%D7%A9%D7%9B%D7%AA_%D7%A2%D7%95%D7%A8%D7%9B%D7%99_%D7%94%D7%93%D7%99%D7%9F); the ethics committee's [May 2024 guidance](https://www.pearlcohen.com/israeli-bar-associations-ethical-guidelines-on-using-ai/) and [September 2026 expanded opinion](https://www.calcalist.co.il/local_news/article/bkqvhskyfe) ([Pearl Cohen summary](https://www.pearlcohen.com/israel-bar-association-issues-an-expanded-ethics-opinion-on-lawyers-use-of-ai/)); [Amendment 13](https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform).
- Cases: [Mata v. Avianca](https://national.clla.org/wp-content/uploads/2025/05/Mata-v-Avianca-Inc.pdf); [Ayinde and Al-Haroun](https://www.judiciary.uk/judgments/ayinde-v-london-borough-of-haringey-and-al-haroun-v-qatar-national-bank/); the Supreme Court, February 2025 ([Jerusalem Post](https://www.jpost.com/israel-news/article-843442)); the AIG class action ([Ynetnews](https://www.ynetnews.com/business/article/sjurpf3pgx)); Cohen v. Ramat Gan Municipality ([Barnea](https://barlaw.co.il/practice_areas/high-tech/ai-regulation/client_updates/have-you-been-using-ai-without-verifying-it-could-cost-you-ils-30000/)).
- Research and US context: [Magesh et al., 2024](https://arxiv.org/abs/2405.20362); [ABA Formal Opinion 512](https://natlawreview.com/article/american-bar-association-issues-formal-opinion-use-generative-ai-tools) (summary).
- Field kit: [04.1 · The AI acceptable-use policy](../module-04/lesson-01.md), [04.2 · Approved tools and data classes](../module-04/lesson-02.md), [04.3 · Vendor and tool review](../module-04/lesson-03.md), [04.6 · Which law applies to you](../module-04/lesson-06.md), [04.8 · Vendor and claim due diligence](../module-04/lesson-08.md); the RFP method: [10.4](../module-10/lesson-04.md).
- Templates: [regulatory map](../../templates/regulatory-map.md), [acceptable-use policy](../../templates/acceptable-use-policy.md), [approved / restricted use list](../../templates/approved-restricted-use-list.md), [claim read-back](../../templates/claim-read-back.md), [vendor AI questionnaire](../../templates/vendor-ai-questionnaire.md), [risk register](../../templates/risk-register.md), [decision-ready case](../../templates/decision-ready-case.md).
- Simulation: [Vendor RFP](../../simulations/vendor-rfp/index.html?preset=generic) (generic scenario).
- Earlier: [12.3 · Diagnosis](lesson-03.md). Next: [12.5 · Build: precedent search with a citation gate](lesson-05.md).
