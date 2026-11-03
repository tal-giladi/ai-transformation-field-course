---
id: "18.5"
module: 18
minutes: 15
practice_minutes: 180
prerequisites: ["18.2", "18.3", "18.4", "01.1"]
objectives:
  - "Turn the course's templates and your own deliverables into a personal practice kit: one master version of each tool, with what you learned using it."
  - "Choose three or four engagements that show range and write each as a two-to-four-page portfolio piece, labelled honestly."
  - "Anonymise any real work so that neither the organization nor any person can be recognised, and get it signed off before it is shown."
  - "Write a one-page offer that says which engagements you can run, in phases a client can stop after, and which kit each uses."
volatility: concept
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): each course ends in a professional deliverable; capstone advisory package"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "Commercial Torts Law, 5759-1999 (חוק עוולות מסחריות), Hebrew Wikisource: ss. 5–6, trade secrets"
    url: https://he.wikisource.org/wiki/חוק_עוולות_מסחריות
  - title: "Privacy Protection Law, 5741-1981 (חוק הגנת הפרטיות), Hebrew Wikisource: s. 2(8)–(9)"
    url: https://he.wikisource.org/wiki/חוק_הגנת_הפרטיות
last_verified: "2026-11-03"
---

# 18.5 · Your practice kit and portfolio

You have run eleven engagements: Harbor & Pine as the warm-up, ten organizations, and Tzurim. Each left a deliverable set, a self-score, a comparison with an expert and a list of what you would do differently. In this lesson you turn that into two things you will use after the course: a practice kit (your own version of every tool, with what you learned using it) and a portfolio (three or four engagements written so a client or an employer can see your judgment in ten minutes). At the end you have a kit index, three master templates, two finished portfolio pieces and a one-page offer.

## The situation

The course is over when you can walk into an organization on Monday without opening it. That needs your tools in one place, in your own words, adapted by what went wrong when you used them. The [templates](../../templates/README.md) are the starting point: copy them into your own practice kit and adapt them, as their index page says.

For consulting work, or for an internal role that needs credibility, you also need to show what you can do without breaking anyone's confidence. The course's engagements help here: they are synthetic, so you can show them in full, as long as you say they are training work. Real work, if you did 18.4, needs anonymising and written sign-off. IBM's consulting certificate builds a professional deliverable at the end of each course; your portfolio does the same from a far larger set, with data, people and a pilot behind each piece.

## What to do

### Step 1 — Inventory what you have

Fill the [practice-kit index](../../labs/module-18/practice-kit/practice-kit-index.csv) (module download): one row per tool, with the source template or lesson, your version's file, which kind of organization you adapted it for, where you last used it, and **what you changed and why**. The last column is the kit's value: a template copied unchanged has taught you nothing yet.

Go through your engagements in order and pull out every place you departed from a template because it did not fit: Open Hands' one-page policy pack ([16.5](../module-16/lesson-05.md)), Lumen's agent permission map ([14.4](../module-14/lesson-04.md)), Galil Health's RFP ([10.4](../module-10/lesson-04.md)), Kinneret's readiness bar dated before the vendor's presentation ([13.4](../module-13/lesson-04.md)), the capstone's integration register ([18.2](lesson-02.md)). Each departure is a variant worth keeping.

### Step 2 — Make one master version of each tool

For each template you will use again, write a master version with a short header above the template itself:

```markdown
# Readiness assessment (my master, v3, 2027-05)
When it worked: Kinneret (bar dated before the vendor; "not yet" with a date), Tzurim.
When it failed: Northwind (I wrote the bar after the vendor demo; the sponsor saw it as moving the goalposts).
Always add: the outcome-label row; who signs the definition; a verdict per use, not per organization.
Short form (one page): Open Hands. Full form: Meridian.
Law and tools to re-check before use: Privacy Protection Law amendments; the PPA's AI guidance status; vendor terms.
```

Then the template, edited: rows you always add, wording that worked with sponsors, the questions that caught real problems. Keep two sizes where it matters — the one-page form you used when time was short, and the full form.

Beyond templates, a working kit has five more things:

| Kit item | What it holds | Built from |
|---|---|---|
| Engagement plan shapes | Twelve-week, six-week and four-week plans with phase exits and the dates that must not slip | 01.4, 16.4, 18.1 |
| Question bank by persona type | The questions that unlocked something, by role: sponsor, CFO, data steward, frontline, works committee, vendor, the person affected | Your coach feedback across all engagements |
| Bar library | Readiness bars by use type (prediction on people, document extraction, drafting assistant, agent with write access) | 02.6, 09.4, 13.4, 14.4 |
| Negative-test bank | Hand-written negative tests by use type, in the languages you work in | 05.4, 11.5, 14.5 |
| Eval harness | Your test-set spec, scoring sheet and (Track B) script, re-runnable on a new data set | 05.2–05.4, `labs/common/fieldkit` |

### Step 3 — Choose portfolio pieces that show range

Three or four pieces are enough. Choose for range, not for your best score:

- one engagement where you **recommended against** the sponsor's idea and gave them something better (for example Kinneret or the capstone);
- one where you **built and evaluated** something with real numbers (an eval report with per-language results);
- one where the hard part was **governance or authority** (Meridian's verdict, Lumen's permission map, Crescent's operating model);
- the **capstone**, because nobody told you what to find.

Each piece follows the [portfolio-piece checklist](../../labs/module-18/practice-kit/portfolio-piece-checklist.md): the situation in five lines; the two or three findings that changed the recommendation, each with its evidence type; the recommendation and the recommend-against with the money; one artifact excerpt (a readiness page, an eval table, a case front page); the gates and re-decision date; and one honest line on what you would do differently, ideally from your comparison with the expert.

### Step 4 — Label honestly

Course engagements are labelled as training work on fictional organizations, every time: "Training engagement on a synthetic organization (AI Transformation in the Field). All organizations, people and data are fictional." Never present them as client work or let a reader assume it. The label does not weaken the piece: a reader who sees a data room, a pilot with an eval and a decision record learns more about you than from a client logo.

### Step 5 — Anonymise real work, then get it signed

If you ran a real engagement (18.4), its portfolio version follows the checklist's anonymisation section: no organization name, no identifying combination of sector, size and place, no person identifiable by role, numbers changed by a stated method or replaced by synthetic ones, no screenshots, no confidential terms, no real examples of tickets or messages. Two Israeli rules make this more than courtesy: business information kept confidential for a competitive advantage can be a trade secret, and using it in breach of a contractual duty or a duty of trust is misappropriation under the Commercial Torts Law (ss. 5–6); and using information about people for a purpose other than the one it was given for, or breaching an agreed duty of confidentiality about them, is an infringement of privacy (Privacy Protection Law, s. 2(8)–(9)). The person who signed your permission letter signs the final piece in writing before anyone outside sees it.

### Step 6 — Write a one-page offer

Use [01.1](../module-01/lesson-01.md) on how engagements are sold and priced. List the engagements you can run with your kit, each as phases a client can stop after:

| Offer | Phases and exits | Kit it uses | Typical length |
|---|---|---|---|
| [e.g. AI readiness diagnostic] | [Discovery → readiness and a recommendation; exit after each] | [charter, interview bank, data profile, readiness master, findings memo] | [4 weeks] |

Say what you do not do, and to whom you route it (counsel, the DPO, security, procurement). An offer that names its boundary is easier to buy.

### Step 7 — Keep the kit alive

Version every master and date it. After each engagement, update the "when it failed" line and the question bank. Every master that touches law, prices or tools carries a "re-check before use" line, because those change: the course marks such lessons `implementation` for the same reason.

## Watch out

- **Course work presented as client work.** It is dishonest and easy to discover; label it every time.
- **A portfolio of templates.** Readers want your judgment: what you found, what you recommended against, what you would change. Templates are the kit, not the portfolio.
- **Your best score only.** Range shows more than polish. A "not yet" that held is worth more than a pilot that scored 98%.
- **"Anonymised" by renaming.** Sector, size and city together identify an organization; a role identifies a person.
- **Masters that never change.** If no "when it failed" line has changed in a year, you are not learning from your engagements.
- **Stale law in the kit.** A regulatory map from 2026 is a history document in 2028; date it and re-check.

## Your turn

### Inputs

- Your deliverables from modules 1–18, your rubric scores and your expert comparisons.
- [Practice-kit index](../../labs/module-18/practice-kit/practice-kit-index.csv) and [portfolio-piece checklist](../../labs/module-18/practice-kit/portfolio-piece-checklist.md) (module download); the [templates](../../templates/README.md).
- If you did 18.4: your permission letter and the anonymisation conditions.

### Steps

1. Fill the practice-kit index for at least 20 tools, with what you changed and why for each one you adapted.
2. Write master versions of three templates you will use most, each with the header (when it worked, when it failed, always add, sizes, re-check).
3. Build the question bank for at least five persona types from your coach feedback.
4. Write two portfolio pieces: the capstone and one other engagement chosen for range; check each against the checklist and label it.
5. Write the one-page offer with at least three engagements, their phases and exits, the kit each uses and your boundary.

### Time

180 minutes: 40 for the index, 45 for three masters, 20 for the question bank, 60 for two portfolio pieces, 15 for the offer.

### Done when

- [ ] The kit index has at least 20 rows, and every adapted tool says what you changed and why.
- [ ] Three masters have the header with a real "when it failed" line from your own engagements.
- [ ] The question bank covers at least five persona types with questions that unlocked something.
- [ ] Two portfolio pieces pass the checklist, each with an artifact excerpt and an honest "what I would do differently".
- [ ] Every course piece carries the training-engagement label; any real piece is anonymised and signed off in writing.
- [ ] The offer lists phases a client can stop after and names what you route to counsel, the DPO, security or procurement.

<details><summary>Reference answer</summary>

**Kit index (excerpt):**

| Kit item | Source | Adapted for | Last used | What I changed and why |
|---|---|---|---|---|
| Readiness assessment | 02.6 | Prediction from records | Kinneret | Added "who owns the outcome definition": a label nobody owns cannot be trained on or measured; verdict per use, not per organization |
| Engagement charter | 01.2 | Outside consultant, phased fee | Tzurim | Urgent-finding rule moved to page 1; phase exits each leave a usable document |
| Policy pack | 04.1–04.8, 16.5 | Small organization | Open Hands | One-page form kept as the default for under 50 people |
| Integration check | 07.1, 18.2 | Any | Tzurim | Register of facts added as a tab; timing trace has a "measured when" column |
| Agent permission map | 14.4 | Agents with write access | Lumen | "Last reversible moment" moved next to the action, not in a separate sheet |

**Portfolio piece (excerpt), Kinneret Plastics — "Not yet, and fund the foundation".** *Training engagement on a synthetic organization (AI Transformation in the Field). All organizations, people and data are fictional.* Situation: a 600-person, two-plant injection moulder; the owner asked for predictive maintenance with a named vendor; I was the internal lead with a day job; eleven weeks. Findings: half of unplanned hours were moulds, mostly at night (measured); 73 usable failure labels in 861 breakdowns, none of the vendor's own 30 per mode (measured); "ready" meant different events at the two plants (measured on one definition). Recommendation: night mould response for the key customer now, ₪730,000 of foundation in three stages with a stop rule, a tested multilingual manual assistant in shadow use; against: no vendor contract in 2027, re-decision January 2028. Artifact: the readiness bar, dated before the vendor's presentation, with each criterion graded. What I would do differently: I wrote the protocol with the works committee in week 6; I would start it in week 2.

**One-page offer (excerpt):** "AI readiness diagnostic — four weeks, two phases (discovery; readiness and a recommendation), exit after each; kit: charter, interview bank, data profile, readiness master, findings memo. Pilot evaluation — six weeks; kit: pilot charter with rule of use, test-set spec, negative-test bank, eval harness. Governance in week two — three weeks; kit: one-page and full policy packs, intake register. I do not give legal opinions: privacy and employment questions go to your counsel or DPO; security architecture to your security officer."

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting): a professional deliverable per course (named, not re-taught).
- [Commercial Torts Law, 5759-1999](https://he.wikisource.org/wiki/חוק_עוולות_מסחריות), ss. 5–6; [Privacy Protection Law, 5741-1981](https://he.wikisource.org/wiki/חוק_הגנת_הפרטיות), s. 2(8)–(9). Hebrew Wikisource; ask counsel before relying on them.
- [Templates](../../templates/README.md); [practice-kit index and portfolio checklist](../../labs/module-18/practice-kit/practice-kit-index.csv) (module download).
- Field kit: [01.1 · Three ways in](../module-01/lesson-01.md) (how engagements are sold and priced); [10.4](../module-10/lesson-04.md), [13.4](../module-13/lesson-04.md), [14.4](../module-14/lesson-04.md), [16.5](../module-16/lesson-05.md) (variants worth keeping); [18.2](lesson-02.md), [18.4](lesson-04.md).
- Capstone: [the project and rubric](../../projects/m18-capstone.md).
