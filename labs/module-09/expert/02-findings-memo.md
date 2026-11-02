# Findings memo — AI in claims

*Head of AI Transformation to Ilana Bar-Lev (COO), Thursday 19 November 2026. cc Michael Ohana (CRO)
for item 3. Template: [findings memo](../../../templates/findings-memo.md). Evidence labels:
**verified** (I measured it in the data or saw the document), **reported** (someone told me),
**inferred**.*

## Answer first

Claims are slow because documents are requested in rounds, not because intake is typed. The fraud
score that went live with Kalanit 9.4 refers Arabic-speaking claimants to investigation four times as
often as Hebrew-speaking ones, through two factors that stand in for nationality and place of
residence; it should stop referring automatically **now**, before the committee. The winter pilot as
proposed would scale both problems into the peak.

## Findings

**1. The claimant waits about a month; the dashboard shows 10.5 days.** *(verified)* From the reported
date to the last indemnity payment, median **32 days** (n=696 claims paid in 2026, 1-in-40 sample). The
dashboard's 10.5 days is the last segment only (file complete → decision) and excludes SIU claims.
Kalanit's registered → closed median is 41.1 days. Internal audit raised the KPI definition in 2025
*(reported, Yusuf)*.

**2. The wait is in the document chase.** *(verified)* Median segments: intake 2.5 days, first
request 1.1, **document chase 12.8 (mean 18.5)**, file complete → decision 8.3, decision → payment 1.6.
45.2% of claims need a second round, 14.1% a third. Median wait: one round 24 days, two 41, three or
more 60. **45.4%** of documents requested in round 2 or later were on the standard day-one list, and
the complete list went out on the day of the report for only **5.6%** of claims (manual 3.2 says same
day). Yusuf: "one complete list, the first day, in the claimant's language" *(reported)*.

**3. Fraud Insight refers by language and area.** *(verified)* Every motor claim, July–October 2026
(5,536): before 6 September, SIU referral 3.2% Arabic vs 3.4% Hebrew; after, **21.0% vs 5.4%** (95%
intervals 17.5–25.0% and 4.4–6.6%). Postal areas on the vendor's "risk areas" list: 25.9% vs 5.3%.
Two factors explain it: F08 "interpreter required" fires on 90.3% of Arabic claims and F09 "risk area"
on 68.4%; without them, Arabic auto-referrals would fall from 65 to 4. Auto-referral holds payment. The
claimant whose complaint I followed (CL-2026-026307) was referred with a score of 60 (threshold 50):
three of her five factors were her garage, her language and her postal area; 44 days to payment; told "the
system flagged your file" *(reported, the claimant)*.

**4. The fraud numbers measure suspicion.** *(verified)* The vendor's back-test label is the SUSPECT
flag, i.e. an SIU referral. Of closed handler referrals since July 2025, 12.6% were confirmed fraud
(174 of 1,385). "Fraud prevented" ₪6.77M YTD splits into confirmed fraud ₪2.34M, no finding ₪2.90M
(deductibles, partial payments) and claimant withdrew ₪1.54M (111 people). The ₪20M is the vendor's
"10% of claims paid" with no source; Natalia's range for leakage is ₪3–6M *(reported)*.

**5. Smart Intake saves no time and works worst for Arabic documents.** *(verified)* Time study: 3.5
keying + 3.3 checking minutes with Smart Intake vs 6.7 keying without. On Kalanit's own batch run of
240 documents: 81.7% of fields right (Arabic 59.6%, Hebrew 88.4%); a rules script with no AI gets
86.0%. It copies diagnoses into the notes field (45 documents) and processes documents in Frankfurt;
the DPO had not been told *(reported)*.

**6. AI already in use outside the inventory.** *(verified)* The two 9.4 modules (live since 6
September; not in the June inventory; committee action 6.1 "assessment before use" not done) and
handlers translating foreign documents with personal ChatGPT/Gemini accounts (12 handler notes in the
CRM sample, May–October).

**7. The pilot window is the peak.** *(verified)* January ≈ 5,100 claims vs ≈ 2,500 in summer; intake
lag 5.6 days median in January 2026 vs 1.5–1.6; handling time on the dashboard 13.8–14.6 days in
February–March. Team leads have no review capacity in December–February *(reported, Yusuf)*.

## What this means

- The biggest lever on the claimant's wait needs no AI: a complete documents list on day one.
- Fraud Insight is a high-impact use under the AI policy, live without approval, with a discrimination
  risk that the law does not excuse because a vendor configured it.
- The proposal's targets rest on two numbers that do not measure what they claim (10.5 days, ₪20M).

## Interim recommendation (urgent, before 15 December)

> Ilana, today, by change request (free, any day; agreement 7.3): switch off Fraud Insight's
> **auto-referral** for motor claims and disable factors **F08** and **F09**; keep the score visible to
> the SIU as a review aid only, with written reasons for any referral (manual 6.1). Release the
> payment hold on the 84 open auto-referred cases unless a handler records concrete grounds. Michael
> agrees this goes to the committee as an interim decision already taken. Ask Kalanit to stop copying
> diagnoses into the notes field. Nothing else changes before 15 December.

## Next

Baselines and the one-page case on 26 November; the verdict pre-read on 8 December.
