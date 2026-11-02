# AI inventory

The list of every AI system and feature in the organization — bought, built, switched on by a vendor update, or brought in by staff — with what it is used for, the data it touches, the decisions it shapes, a named owner and the next action. It also lists what you checked and excluded, so nobody checks it twice. Build the first version in week two from the SaaS list, the shadow-AI census and release notes; keep it up to date every quarter. Lesson [01.7](../lessons/module-01/lesson-07.md) shows how; the spreadsheet version is `labs/module-01/ai-inventory.csv` in the module 1 download ([open](../labs/module-01/ai-inventory.csv)). Module 4 adds risk tiering and links it to the legal register.

## How to fill it

Module 4 adds risk-tier columns (data class, decisions about people, acting without a person, harm if wrong, tier and reason, DPIA); the spreadsheet `labs/module-04/ai-inventory-tiering.csv` has them.

- Write the counting rule at the top and apply it to every candidate. One row per tool **per use**.
- Record excluded and "to verify" systems with the reason.
- Every row has one named business owner: the head of the team that uses it, not IT by default.
- "Shapes" is one sentence: what decision or output, for whom, and who checks it.
- The first risk view is a placeholder (high / medium / low with one reason) until module 4's tiering.
- Keep maturity scores and legal duties out of this document; link to them by ID.

## Template

```markdown
# AI inventory — [Organization] — v[n], [date]

**Counting rule:** A system or feature counts as AI if it produces outputs — content, predictions, scores,
recommendations or decisions — by inferring them from data (a learned or generative model), rather
than only applying rules that people wrote. One row per tool per use. Excluded and unverified systems
are listed with the reason.

| ID | Tool / feature | Vendor | AI? (yes / no / to verify) | Why | How it arrived | Status | Business owner | Technical owner | Departments / users | Use | Data in | Shapes (decision or output) | Who is affected | Human check | Terms / plan | Data location | First risk view | Action | Action owner | Due | Last checked | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

How it arrived: bought as AI · feature update · free tool · browser extension · personal subscription · built in-house
Status: on · off · available, not enabled · unknown

## Top actions this month
| # | Action | Owner | Due |
|---|---|---|---|

## Linked documents
- Maturity view: [link] · Legal register: [link] (rows linked by inventory ID)
```

## Example

Harbor & Pine, first version, 10 November 2026 (excerpt):

| ID | Tool / feature | AI? | Why | How it arrived | Status | Owner | Shapes | Human check | Action |
|---|---|---|---|---|---|---|---|---|---|
| AI-01 | PeopleWise AI Candidate Match | Yes | Vendor model scores CVs 0–100 | Feature update, March 2026 | On by default (IT list said "No") | Dana Katz | Which applicants recruiters see; hides scores under 40 | None designed | Export autumn applicants and scores; labour lawyer; decide off/on |
| AI-07 | StoreHub AI product descriptions | Yes | Generated text | Feature, enabled by marketing | On | Noa Levi | Product text on the web store | Content manager reviews | Record the review step |
| X-01 | SmartStock AI | No | Min/max formulas, manual seasonality, "demand sensing" not licensed | Bought 2024 as "AI" | On | Eyal Navon | Reorder suggestions, ~80% approved as is | Buyer approves | Automated-decision list, not AI governance |
| AI-11 | Google Workspace Gemini | Yes | Generative features included in the plan since Jan 2025 | Included in plan | Unknown | Avi Mizrahi | Unknown | — | Admin-console check by 17 Nov |
