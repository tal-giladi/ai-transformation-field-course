# Kalanit Claims 9.4 — release notes for Meridian Mutual

*Kalanit Systems Ltd., 10 August 2026. Sent to: CIO office, Kalanit product owner (Noam Segal).
Production deployment: Sunday 6 September 2026. Fictional vendor.*

## Highlights

- **Regulatory reporting:** updated claims data fields for the Supervisor's reporting formats.
- **New intake screens:** single-page registration, duplicate check on policy and loss date.
- **Smart Intake (AI-powered document capture)** — NEW.
- **Fraud Insight (AI-driven fraud scoring)** — NEW, included in your maintenance plan.
- Performance: search 40% faster.

## Smart Intake

Reads uploaded and scanned documents (claim forms, invoices, police confirmations, assessor reports,
medical invoices) and pre-fills claim fields for the handler to confirm. Supports Hebrew, Arabic,
Russian and English.

- **97.4% field-level accuracy**¹
- Pre-filled fields are shown with a confidence score; fields below 0.80 are highlighted.
- Free-text notes: relevant text from the document (for example diagnosis on medical invoices) is
  copied to the claim's notes field to save typing.
- Processing: documents are sent to Kalanit's cloud capture service (public cloud, EU region,
  Frankfurt; see sub-processors, Annex C of the agreement) and the result is returned to Kalanit Claims.

**Default configuration for Meridian:** enabled for motor claims at the Haifa and Ramat Gan claims
centres from go-live ("early adopter" sites). Other lines and centres: on request.

¹ *Internal benchmark: 500 typed Hebrew motor claim forms scanned at 300 dpi, Kalanit lab, March 2026.*

## Fraud Insight

Scores every new claim from 0 to 100 with Kalanit's fraud factor library and routes high-risk claims
to the SIU.

- **Identified 78% of fraud-flagged claims at a 10% referral rate (AUC 0.81) in back-testing on
  Meridian's 2024–2025 motor claims**²
- Configurable factors and weights; delivered with the **Israel Market Template 2026.2**.
- Bands: *review* (amber badge for the handler) and *refer* (automatic routing to the SIU queue;
  payment approval is held until the SIU releases the claim).
- Explainability: the factors that fired are listed on the SIU screen.

**Default configuration for Meridian:** enabled for all motor claims from go-live, with the Israel
Market Template thresholds (review 35, refer 50). Home and other lines: on request.

² *Back-test on claims registered 1 January 2024 – 31 December 2025, where "fraud-flagged" means
the claim carries the SUSPECT flag in Kalanit.*

## Fraud Insight Pro (licensed separately)

Network analytics across claimants, garages and phone numbers; image forensics for photos;
consortium data. Ask your account executive.

## Opt-out

As in the maintenance agreement (section 7.3): new functionality is delivered enabled with Kalanit's
recommended configuration unless the customer opts out in writing within 30 days of these notes.
