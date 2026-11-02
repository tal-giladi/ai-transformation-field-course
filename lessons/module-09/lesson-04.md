---
id: "09.4"
module: 9
minutes: 22
practice_minutes: 150
prerequisites: ["09.3", "01.7", "04.4", "04.6", "04.8"]
objectives:
  - "Classify AI and AI-like systems in a regulated insurer by impact, whatever the vendor calls them, and decide which laws reach them."
  - "Write gate questions before reading the evidence, and rate each gate pass, flag or block with the evidence."
  - "Run an outcome test across groups on claims data, choosing which attributes are legitimate to test and reading ratios with their intervals."
  - "Write a deployment verdict per system, with enforceable conditions, the interim action already taken, a correction to the record and the dissent."
volatility: implementation
sources:
  - title: "Inter-ministerial team, Artificial intelligence in the financial sector — final report (December 2025): risk-based approach; explainability; human involvement; bias and discrimination incl. the Prohibition of Discrimination Law s. 3(a), 3(a1), 3(d)(1) and outcome testing for proxies; responsibility"
    url: https://www.boi.org.il/media/rh0bejl4/aireport.pdf
  - title: "EBN Law, summary of the final report on AI in the financial sector (December 2025)"
    url: https://www.ebnlaw.co.il/he/media-center/ai-finance-sector/
  - title: "Capital Market, Insurance and Savings Supervisor — circular 2016-9-9 (5 July 2016), s. 3, s. 8, annex s. 6 (investigation reports)"
    url: https://www.gov.il/BlobFolder/dynamiccollectorresultitem/regulation-1101/he/regulation_h_2016-9-9.pdf
  - title: "Chambers Practice Guides, Data Protection & Privacy 2026: Israel (Or-Hof Law, updated 10 March 2026): data of special sensitivity; DPO; security levels; transfers; PPA AI guidance still draft"
    url: https://practiceguides.chambers.com/practice-guides/data-protection-privacy-2026/israel
  - title: "Pearl Cohen, Israel: New Draft Guidelines on the Application of Privacy Law to AI (4 May 2025)"
    url: https://www.pearlcohen.com/israel-new-draft-guidelines-on-the-application-of-privacy-law-to-ai/
  - title: "EU AI Act, Article 2 (scope) and Annex III point 5 (AI Act Explorer)"
    url: https://artificialintelligenceact.eu/annex/3/
  - title: "AI Act Explorer — Digital Omnibus on AI, Regulation (EU) 2026/1744 (Annex III high-risk obligations from 2 December 2027)"
    url: https://artificialintelligenceact.eu/ai-act-explorer/digital-omnibus/
  - title: "29 CFR 1607.4(D), the four-fifths rule (US Uniform Guidelines; origin of the 0.80 screen)"
    url: https://www.law.cornell.edu/cfr/text/29/1607.4
  - title: "IBM Lead AI Transformation (Coursera) — course 4, AI Governance, Risk, and Responsible Deployment (pass / flag / block; ship / ship with conditions / wait)"
    url: https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution
last_verified: "2026-11-02"
---

# 09.4 · The hard part: a regulated deployment verdict

The risk committee meets on 15 December and must decide about two systems that have been live since September and a pilot that would extend them. In this lesson you classify both systems by what they do to claimants, decide which laws reach them, write the gate questions before you read the evidence, run an outcome test across groups on four months of motor claims, and rate every gate pass, flag or block. At the end you have a deployment verdict the committee can sign: one verdict per system, enforceable conditions, the interim action already taken, a correction to the record and the dissent.

## The situation

Monday 30 November – Tuesday 8 December 2026 (the pre-read is due on the 8th). Fraud Insight's
auto-referral has been off since 22 November. Ilana accepted the case in 09.3 but still wants Smart
Intake extended to home claims for the storms. The CRO, Michael Ohana, agreed to put the June
correction on page one if you bring the facts.

IBM's governance course gives you the vocabulary: a gate question that can be answered "no"; pass,
flag or block; ship, ship with conditions or wait; conditions that bind only with a metric, a limit, an
owner and someone who can stop it; 0.80 as an internal screen, not a legal safe harbour. In IBM's
exercise three gates are pre-written and the disparity measure is handed to you. Here you write the
gates, choose the groups, compute the measure from the data and find the mechanism.

> [!WARNING]
> This lesson works with real-shaped claims data about people's language and place of residence.
> Use only the pseudonymised extracts in the data room. In a real organization, any outcome test on
> claimants' attributes needs the DPO's approval for that purpose, and conclusions about
> discrimination law are for counsel, not for you.

## What to do

### Step 1 — Classify each system by what it does, not what it is called

Start from the counting rule in [01.7](../module-01/lesson-07.md) and Meridian's own policy. Open
`vendor/fraud-insight-config-export.csv`: Fraud Insight is fourteen rules, each adding a fixed number of
points, with two thresholds (35 for an amber badge, 50 for automatic routing to the SIU with payment
held). There is no learning. Under your counting rule it is **not AI**. Under the policy's definition
("infers from the input how to generate outputs") a narrow reading excludes it too. Michael admits he
is tempted to read it that way: it would keep it off the agenda.

Classify by impact instead:

| | Smart Intake | Fraud Insight |
|---|---|---|
| What it does | Pre-fills fields from documents; a handler confirms each | Holds payment and routes to the SIU at 50+ points; no person in between |
| AI under the counting rule? | Yes | No: weighted rules |
| High-impact under the policy (rule 2: "makes or materially supports a decision about a customer's claim")? | Yes, lower tier: it supports amounts that are paid | **Yes**: it decides who is investigated and whose payment waits |
| Risk factors the inter-ministerial report uses: decides or assists; effect on rights; volume; data sensitivity | Assists; ≈ 14,000 motor claims a year at two centres; health data in some documents | Decides the hold; ≈ 18,600 motor claims a year; uses language and area |
| Tier | Medium | High |

The sentence that settles it, for the committee: *the Prohibition of Discrimination Law applies to how
Meridian provides insurance whatever technology it uses, so a spreadsheet that did what Fraud Insight
does would be gated the same way.* Add an action: amend the policy so that "automated decision rules"
with the same impact are in scope by name.

### Step 2 — Decide which laws reach the systems

Write a short [regulatory map](../../templates/regulatory-map.md) as in [04.6](../module-04/lesson-06.md),
Israel first. What each instrument asks *here*, and what you route to counsel:

| Instrument | What it asks here |
|---|---|
| Supervisor's circular 2016-9-9 on clarification and settlement of claims (binding) | Good faith, transparency and fairness (s. 3); the documents list at first contact; a notice within 30 days of having all documents; and when a decision relies on an investigation report, the claimant is told its main findings (annex s. 6(c)). Question for counsel: does an automatic payment hold need a continued-clarification notice with reasons? |
| Prohibition of Discrimination in Products, Services and Entry into Places of Entertainment and Public Places Law, 5761-2000 (חוק איסור הפליה במוצרים, בשירותים ובכניסה למקומות בידור ולמקומות ציבוריים) | As quoted in the inter-ministerial report: no discrimination in providing a public service, which the law defines to include insurance, on grounds including nationality, country of origin, religion, age (s. 3(a)) and place of residence (s. 3(a1)); an exception where the distinction is required by the nature of the service (s. 3(d)(1)). Question for the General Counsel: exposure from F08 and F09, and whether anything is "required by the nature" of fraud detection. |
| CMISA consolidated circular: risk management (including model risk) and the outsourcing chapter | Risks identified and managed; outsourcing does not transfer the institution's responsibility. The vendor's liability cap (agreement 12.1) does not change that. |
| Inter-ministerial report on AI in the financial sector (December 2025) | Recommendations, not binding: tiers by risk; general and specific explainability for significant decisions; human involvement for high-impact decisions; outcome testing because proxies hide inside neutral-looking rules; responsibility stays with the institution. Use it as the committee's benchmark, labelled as such. |
| Privacy Protection Law, 5741-1981 (חוק הגנת הפרטיות) with Amendment 13; Data Security Regulations, 5777-2017; transfer regulations | Health data is of special sensitivity; purpose limitation; a processor agreement; transfers to the EU are allowed, the contract and what is sent are the questions. Smart Intake copies diagnoses into a notes field and processes documents in Frankfurt (Annex C). The Privacy Protection Authority's AI guidance is a draft (April 2025). |
| EU AI Act (Regulation 2024/1689 as amended by 2026/1744) | **Decided: not applicable.** Meridian has no EU establishment and sells to Israeli residents; the outputs are used in Israel (Article 2(1)). Claims handling is not in Annex III; point 5(b) expressly excludes fraud detection from credit scoring; 5(c) covers only risk assessment and pricing in life and health insurance (Annex III obligations apply from 2 December 2027). Write the reasoning down and when to re-check: if Meridian ever prices health cover for EU residents with AI. |

[Dr. Rana Haj-Yahia](../../labs/module-09/personas/rana-dpo.md), the DPO, owns the privacy rows; ask her
before you write them. [Michael Ohana](../../labs/module-09/personas/michael-cro.md) owns the format.

### Step 3 — Write the gate questions before you read the evidence

A gate question turns a principle into an evidence question that can be answered "no" or "not
documented". Write them, date them and send them to Michael before you score anything. If you already
looked at some evidence (you did: the pivot in 09.2), say so in the paper.

| Gate | Evidence question |
|---|---|
| G1 Inventory | Is it in the AI inventory, with a named accountable owner? |
| G2 Approval | Was it approved by the committee before production, as rule 3.2 requires? |
| G3 Accuracy | Has it been tested on Meridian's own documents or claims, against verified outcomes? |
| G4 Outcomes across groups | Are outcomes comparable across the groups we can legitimately test, with intervals? |
| G5 Explanation | Can a handler tell the claimant the main reasons for what happened to their claim? |
| G6 Human oversight | Is there a person with the information, time and authority to override it, and evidence that they do? |
| G7 Privacy | DPIA done; data minimised; processor and transfer terms reviewed? |
| G8 Vendor terms | Change control, liability, data use, exit? |
| G9 Monitoring and stop | A metric, a limit, an owner and someone who can switch it off? |

[Tamar Weiss](../../labs/module-09/personas/tamar-internal-audit.md) from internal audit will not
approve your paper, but she will tell you what evidence she would ask for behind each gate: keep an
evidence file she could re-run.

### Step 4 — Run the outcome test

An outcome test compares what happened to comparable claims in different groups. It does not need to
know how the system works, which is why the inter-ministerial report recommends it for proxies that
hide inside neutral-looking rules.

**Choose the groups, and write why each is legitimate.**

| Attribute | Recorded? | Test with it? | Use it as an input? |
|---|---|---|---|
| Language of correspondence | Yes, for service | Yes: closest available signal of national origin | Never |
| Postal area | Yes | Yes: place of residence is itself a protected ground | Never |
| Region | Yes | Yes | Only with a documented reason |
| Age band | Yes (missing for 28% of agents' claims) | Yes: a protected ground in services, often legitimate in pricing | Only where required by the nature of the product |
| Ethnicity, religion | No | **Never infer them** from names, areas or anything else | Never |
| Gender | Not on these claims | State the gap; do not infer it | — |

The DPO approved using these fields for this test (policy rule 3.2 requires a test of outcomes across
groups, so the purpose is documented).

**Measure.** The adverse outcome is an SIU referral (it holds payment). Data: every motor claim
registered 1 July – 31 October 2026, the period before go-live is a natural comparison. With
`python bias_test.py` (or a pivot table with the Wilson interval formula from the lab README):

| Group | Before 6 Sep (handlers) | After 6 Sep (Fraud Insight) | Ratio to reference, after |
|---|---|---|---|
| Hebrew (reference) | 3.4% of 2,065 | 5.4% of 1,697 (95% interval 4.4–6.6%) | 1.00 |
| Arabic | 3.2% of 538 | **21.0% of 453 (17.5–25.0%)** | **3.87** |
| Russian | 4.0% of 301 | 3.8% of 261 | 0.71 |
| Amharic | 3.6% of 28 | 6.5% of 31 | n too small to read |
| Postal area not on the list (reference) | 3.4% of 2,591 | 5.3% of 2,179 | 1.00 |
| Postal area on the "risk areas" list | 3.8% of 423 | **25.9% of 343 (21.6–30.8%)** | **4.92** |
| North vs Center | 3.9% vs 3.1% | 13.5% vs 6.6% | 2.04 |
| Age 18–24 vs 35–44 | 3.7% vs 4.2% | 10.6% vs 8.0% | 1.32, intervals overlap |

Three things to read before you write a sentence:

1. **The screen.** A referral is adverse, so a group *above* 1.25× the reference (the four-fifths
   rule turned around) with non-overlapping intervals is a finding. The four-fifths rule comes from US
   employment guidelines (29 CFR 1607.4(D)), which themselves say small numbers need care; in Israel it
   is an internal screen, not a legal test.
2. **The counterfactual.** Before go-live, handlers referred Arabic- and Hebrew-speaking claimants at
   the same rate. The disparity arrived with the system.
3. **The mechanism.** `python bias_test.py --factors`: F08 "interpreter required" (+10) fires on 90.3%
   of Arabic claims and 0% of Hebrew; F09 "risk area" (+15) on 68.4% and 1.6%. Without the two, Arabic
   auto-referrals fall from 65 to 4, Hebrew from 33 to 31. F05 "non-network garage" fires on 41.5% of
   Arabic claims and 20.6% of Hebrew: an indirect proxy to review, not to remove blindly.

What you cannot measure yet: whether the score finds fraud. Its back-test (AUC 0.81) used the SUSPECT
flag, i.e. past referrals, as the label (release notes, footnote 2): it measures how well the score
imitates referrals. Of 23 closed auto-referrals, 2 were confirmed fraud; 84 are still open
(`--outcomes`). Ask [Gil Navon](../../labs/module-09/personas/gil-kalanit-vendor.md), the vendor's account
executive, to read back each claim ([04.8](../module-04/lesson-08.md)): where the weights came from,
what "fraud-flagged" means, whether Meridian can change the configuration today.

For Smart Intake the outcome is a correct field. From 09.5's eval on 200 test documents: Arabic 62.2%,
Hebrew 88.6%, mostly Eastern Arabic digits and the old Haifa scanner.

### Step 5 — Write the explanation a claimant could use

The inter-ministerial report separates general explainability (how a system works, for the regulator
and the institution) from specific explanation (why this decision, for the customer), and asks for the
specific kind where a decision is significant and adverse. The claims circular already expects the
main findings of an investigation report when a decision relies on one. Samira was told "the system
flagged your file". Test G5 by writing the sentence a handler could have said:

> "Your claim was routed to our investigations unit automatically because of a score that, among
> other things, added points for your language of correspondence and your postal area. We have
> stopped using those factors. The review found nothing, and you were paid on 29 October."

If you cannot write that sentence without embarrassment, the gate blocks.

### Step 6 — Rate the gates

Rate each gate with the evidence in one line. A block on any gate rules out both ship verdicts.

| Gate | Smart Intake | Fraud Insight |
|---|---|---|
| G1 Inventory | Flag (added now) | Flag (added now) |
| G2 Approval | Block (resolved by this decision) | Block |
| G3 Accuracy | Flag: 82.1% of fields vs the vendor's 97.4% (lab conditions) | Block: never validated on confirmed outcomes |
| G4 Outcomes | Flag: Arabic 62.2% vs Hebrew 88.6% | Block: 3.87× and 4.92× through proxy factors |
| G5 Explanation | Pass: a person confirms the values | Block |
| G6 Oversight | Flag: 37 wrong values at confidence ≥ 0.80 are not highlighted | Block: no person before the hold |
| G7 Privacy | Block until diagnoses stop going into the notes field | Flag: no DPIA |
| G8 Vendor terms | Flag: on by default (7.3); data use (9.2); liability cap | Flag |
| G9 Monitoring and stop | Flag | Block |

### Step 7 — Write the verdict

One verdict per system, in IBM's terms, then conditions that bind (the [decision record](../../templates/decision-record.md)
fields: metric, warning, hard limit, cadence, owner, who can stop it, what happens). Then four things
committees often miss:

- **The interim action already taken** (22 November), for ratification.
- **The correction to the record**: the June statement has not been true since 6 September. Put it on
  page one, with the date it stopped being true.
- **The dissent**, by name and reason: Ilana wants Smart Intake on home claims for the storms.
- **The cost of delay, stated honestly**: no measured fraud saving is lost, because none was shown;
  the vendor's discount expires.

## Watch out

- **"It's not AI, so it's out of scope."** Classify by impact. The law does not care what the vendor
  calls it.
- **Inferring ethnicity.** Never infer protected traits from names or areas to "improve" the test. Use
  what is recorded for a service reason, say what is missing.
- **Treating 0.80 as a legal safe harbour.** It is an internal screen with a US origin; intervals and
  sample sizes matter more than the threshold.
- **Writing the criteria after the results.** Date them; say what you had already seen.
- **"We will monitor."** A condition without a limit, an owner and a stop authority binds nothing.
- **One verdict for everything.** The two systems have different risks; the pilot is a third decision.
- **Legal conclusions in your voice.** Quote the instrument, name the question, route it to counsel.
- **Forgetting the claimant.** The chair will ask what Samira was told. Have the sentence ready.

## Your turn

### Inputs

- Data room (module download): `claims/motor_claims_2026-07_to_10.csv`, `vendor/fraud-insight-config-export.csv`,
  `vendor/risk-areas-v3.csv`, `vendor/kalanit-claims-9.4-release-notes.md`, `vendor/kalanit-agreement-excerpt.md`,
  `siu/siu_case_log.csv`, `complaints/complaints_log_2026.csv`, `policies/ai-policy-2026.md`,
  `governance/risk-committee-minutes-2026-06-15.md`, `governance/ai-inventory-2026-06.csv`.
- Personas: [Michael Ohana](../../labs/module-09/personas/michael-cro.md), [Rana Haj-Yahia](../../labs/module-09/personas/rana-dpo.md),
  [Gil Navon](../../labs/module-09/personas/gil-kalanit-vendor.md), [Tamar Weiss](../../labs/module-09/personas/tamar-internal-audit.md);
  transcripts in the module download; [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [regulatory map](../../templates/regulatory-map.md), [ai inventory](../../templates/ai-inventory.md),
  [risk register](../../templates/risk-register.md), [DPIA for AI](../../templates/dpia-for-ai.md),
  [claim read-back](../../templates/claim-read-back.md), [decision record](../../templates/decision-record.md).

### Steps

1. Classify both systems (Step 1 table) and write the one sentence that settles "is it AI?".
2. Write the regulatory map, Israel first, with the EU AI Act decision and its reasoning; list the
   questions for the General Counsel and the DPO. Interview Rana.
3. Write and date the gate questions; interview Michael about the format and Tamar about the evidence.
4. Run the outcome test by language, postal area, region and age band, before and after 6 September,
   with intervals; find the mechanism in the factors. Interview Gil and read back his three claims.
5. Write the explanation sentence for Samira.
6. Rate every gate for both systems.
7. Write the verdict: page one with the correction and the decisions requested; verdicts with
   conditions; dissent; cost of delay; evidence file.

**Track B (Python).** `python bias_test.py` (by `--by claimant_lang|region|risk_area|age|channel`),
`--factors` and `--outcomes`. Python is worth it here because the committee, the auditor and the
vendor will each want to re-run the test, and Wilson intervals and factor counts over 5,536 claims are
error-prone by hand. Track A: a pivot of `siu_referred` by group and period; the README gives the
interval formula.

### Time

150 minutes: 25 for classification and the map, 20 for the gates, 45 for the outcome test, 20 for the
interviews, 40 for the verdict.

### Done when

- [ ] Both systems classified by impact; the "is it AI?" question answered in one sentence.
- [ ] The regulatory map is Israel first, and says why the EU AI Act does not apply and when to re-check.
- [ ] Gate questions are dated and answerable "no".
- [ ] The outcome test reports n, rates, intervals and the before/after comparison, and names the factors that cause the gap.
- [ ] No protected trait was inferred; missing attributes are stated.
- [ ] One verdict per system and one for the pilot; every condition has a limit, an owner and a stop authority.
- [ ] Page one corrects the June statement; the interim action is up for ratification; the dissent is written.

<details><summary>Reference answer</summary>

Full version: `labs/module-09/expert/04-deployment-verdict.md` (module download). Page one:

> **0. Correction to the record.** On 15 June 2026 management stated that no AI system makes or
> materially supports decisions on claims. Since 6 September 2026 that has not been true. Kalanit Claims
> 9.4 went live with two modules switched on by default: Smart Intake (pre-fills claim fields from
> documents) and Fraud Insight (scores every motor claim; at 50 or more it routes the claim to the SIU
> and holds payment). The committee's action 6.1 ("assessment to the committee before use") was not
> done. Both are added to the inventory today (AI-05, AI-06).
>
> **1. Decisions requested.** (1) Ratify the interim change of 22 November: auto-referral off; F08, F09
> and F13 disabled; score visible to the SIU as a review aid only, with written reasons for any
> referral. (2) Fraud Insight: **wait** (blocked) until re-validated on confirmed outcomes and
> re-tested across groups; no extension to home claims; no Fraud Insight Pro. (3) Smart Intake:
> **wait** on any extension; the current motor use continues only while its conditions are met
> (diagnoses no longer copied by 31 December, or it is switched off). (4) The winter pilot as
> proposed: **wait**; an offline extraction pilot now and shadow mode after the peak instead.

**Outcome test (extract).** Arabic 21.0% of 453 vs Hebrew 5.4% of 1,697 after go-live (3.87×); risk-area
postal codes 25.9% vs 5.3% (4.92×); before go-live 3.2% vs 3.4%. Mechanism: F08 on 90.3% of Arabic
claims, F09 on 68.4%; without them Arabic auto-referrals 65 → 4. Effectiveness unknown: back-test label
= referrals; 2 of 23 closed auto-referrals confirmed.

**Classification sentence.** "Fraud Insight is not AI by our counting rule, and it does not matter: it
holds payments and decides who is investigated, and the anti-discrimination law applies whatever
technology we use."

**A condition that binds (Smart Intake).** No health data in notes: weekly sample of 50; any
diagnosis after 31 December → switched off; owner CIO product owner; the DPO can stop it.

**EU AI Act.** Not applicable: no EU establishment, Israeli customers, outputs used in Israel (Art.
2(1)); claims and fraud detection not in Annex III (5(b) excludes fraud detection; 5(c) is life and
health pricing, from 2 December 2027). Re-check if Meridian prices health cover for EU residents.

**Dissent.** The COO would extend Smart Intake to home claims for the storm season; not followed:
with Smart Intake keying 3.5 + checking 3.3 minutes vs 6.7 without, it saves no time, and home claims
add health data and Arabic invoices it reads worst.

</details>

## References

- Inter-ministerial team, [AI in the financial sector, final report](https://www.boi.org.il/media/rh0bejl4/aireport.pdf) (December 2025, Hebrew): chapters on explainability, human involvement, bias and discrimination (quoting the Prohibition of Discrimination Law), responsibility, insurance; [EBN Law summary](https://www.ebnlaw.co.il/he/media-center/ai-finance-sector/). Recommendations, not binding.
- Supervisor, [circular 2016-9-9](https://www.gov.il/BlobFolder/dynamiccollectorresultitem/regulation-1101/he/regulation_h_2016-9-9.pdf) (Hebrew), s. 3, s. 8 and annex s. 6.
- Chambers, [Data Protection & Privacy 2026: Israel](https://practiceguides.chambers.com/practice-guides/data-protection-privacy-2026/israel); Pearl Cohen on the [PPA's draft AI guidance](https://www.pearlcohen.com/israel-new-draft-guidelines-on-the-application-of-privacy-law-to-ai/).
- EU: [AI Act Annex III](https://artificialintelligenceact.eu/annex/3/), [Article 2](https://artificialintelligenceact.eu/article/2/), [Digital Omnibus](https://artificialintelligenceact.eu/ai-act-explorer/digital-omnibus/). US: [29 CFR 1607.4(D)](https://www.law.cornell.edu/cfr/text/29/1607.4) (four-fifths rule).
- IBM, [Lead AI Transformation certificate](https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution), course 4 (pass / flag / block; ship / ship with conditions / wait; named, not re-taught).
- Field kit: [01.7 · The AI inventory from zero](../module-01/lesson-07.md), [04.4 · AI inventory, risk tiering and the DPIA](../module-04/lesson-04.md), [04.6 · Which law applies to you](../module-04/lesson-06.md), [04.8 · Vendor and claim due diligence](../module-04/lesson-08.md), [07.2 · Scale, fix or stop](../module-07/lesson-02.md).
- Templates: [regulatory map](../../templates/regulatory-map.md), [DPIA for AI](../../templates/dpia-for-ai.md), [claim read-back](../../templates/claim-read-back.md), [decision record](../../templates/decision-record.md).
- Next: [09.5 · Build and decide: the extraction pilot](lesson-05.md).
