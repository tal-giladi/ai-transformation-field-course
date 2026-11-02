# Build spec for module writers

You write ONE module (or one data room, or a set of simulations) of "AI Transformation in the Field".
The main session gave you the unit; do only that unit.

## Before you write: read, in this order

1. `C:\Users\TalGiladi\OneDrive\repos\tals-academy\docs\new-course-instructions.md`. It is binding and wins over everything here.
2. `curriculum/plan.md`, all of it. Most important: §1 (purpose, relation to IBM), §3 (design, engagement contents, lesson shape, simulations), §4 (sources, Israel first), §5 (two tracks), §6 (your module's lessons), §7 (lesson format), §8 (templates).
3. This file.
4. `curriculum/research/ibm-gap-map.md` and `curriculum/research/ibm-consulting-gap-map.md` (which gap your lessons fill, and IBM vocabulary to name in one line, never re-teach). Open the per-course notes in `curriculum/research/ibm-content/` and `ibm-consulting/` only for the topics your module covers. IBM content is copyrighted: use the ideas, never copy wording or exercises.
5. `labs/common/README.md` (the field kit: Python helpers, persona format, coach prompt) and, for modules 1–7, `labs/common/harbor-and-pine/INDEX.md` (which data-room file serves which lesson).
6. `references/laws-and-guidance.md` (the shared, dated list of laws, regulator guidance and standards; start from it, re-open the sources you cite, and report changes in your sources inbox).
7. `templates/README.md` and the finished modules before yours, to match tone and re-use their templates instead of re-teaching.

## Hard limits for agents

- **Do not spawn sub-agents. Work sequentially.** Tal's rule: never more than 2 agents running in total.
- **Shared files are off-limits.** Never edit `_sidebar.md`, `README.md`, `glossary.md`, `templates/`, `references/`, `labs/common/`, `simulations/common/`, `BUILD_PROGRESS.md`, `curriculum/plan.md`, this file, or another module's files. Write additions to your inboxes (below).
- **Never commit or push.** The main session does that.
- Work only inside `C:\Users\TalGiladi\OneDrive\repos\course-creator\ai-transformation-field-course`. Never edit the Academy repo.
- Finish one lesson completely (`.md` + `.quiz.yaml`) before starting the next, then append `lesson-MM done` to `curriculum/status/module-NN.log`. Append `module done` at the end. If the log already lists a lesson as done, skip it (a previous run wrote it).

## What you produce for module NN

**Lessons.** Every lesson in plan §6 for your module, with those ids (titles may be polished):

- `lessons/module-NN/lesson-MM.md`
- `lessons/module-NN/lesson-MM.quiz.yaml` (4–5 questions)

**Module quiz.**

- `assessments/module-NN-quiz.md`: a short intro (what it covers, 10 questions, pass mark 70%), a "Revisit by topic" list linking every lesson, and a link to the module project. No questions, no answers, never an "Answers" heading.
- `assessments/module-NN-quiz.quiz.yaml`: 10 scenario questions.

**Project.** `projects/mNN-<slug>.md` with the slug from the table below. It is the module's larger practical piece (plan §6 "Module practical", or for engagements the full deliverable set). It contains: the brief; the deliverables, each with the template it uses; the steps; a self-assessment rubric table (criterion · what "strong" looks like · what "weak" looks like); and a model answer or expert deliverable set in `<details><summary>Model answer</summary>…</details>` (for engagements: link to the expert deliverables in the lab folder).

| Module | Project slug | Module | Project slug |
|---|---|---|---|
| 01 | `m01-walking-in` | 10 | `m10-galil-health` |
| 02 | `m02-discovery` | 11 | `m11-givat-oren` |
| 03 | `m03-portfolio` | 12 | `m12-atlas-and-rowe` |
| 04 | `m04-policy-pack` | 13 | `m13-kinneret-plastics` |
| 05 | `m05-pilot` | 14 | `m14-lumen-saas` |
| 06 | `m06-adoption` | 15 | `m15-crescent-bank` |
| 07 | `m07-readout` | 16 | `m16-open-hands` |
| 08 | `m08-northwind-outfitters` | 17 | `m17-vantage-logistics` |
| 09 | `m09-meridian-mutual` | 18 | `m18-capstone` |

**Labs.** `labs/module-NN/README.md` always: what is in the folder, what each lesson uses, how to open it with no code (Track A) and with Python (Track B). Modules 1–7 use the shared Harbor & Pine data room in `labs/common/harbor-and-pine/` (do not edit it; if you need a file it lacks, put the request in your notes inbox and work around it). Module-specific extras (a worked spreadsheet, a flawed document to critique, Track B scripts) go in `labs/module-NN/`.

**Engagement modules (08–17) also produce, before any lesson:**

- `labs/module-NN/brief.md`: the engagement brief (how you were brought in, by whom, stated ask, budget in ₪, timeline, who you report to, what access you have on day one).
- `labs/module-NN/data-room/`: `INDEX.md` (every file, what it is, which lesson uses it — never which findings are planted), `generate.py` (seeded, Python standard library only, `python generate.py` rebuilds every data file byte-for-byte), and the generated files, committed (Track A learners cannot run Python). Real-shaped: the column names, codes, free-text style and messiness of a real export. A few hundred to a few thousand rows per table; keep the whole folder under 3 MB. Documents (policies, contracts, vendor sheets, KPI reports, minutes, emails) are markdown or CSV. Plant the findings from plan §6 plus your own (bad data, a missing baseline, shadow AI, a step that exists only on paper); each must be discoverable from the data, never stated outright.
- `labs/module-NN/personas/`: `README.md` (the cast: name, role, one line each, which lesson interviews whom), one file per persona in the format of `labs/common/persona-format.md` (6–9 personas, types from plan §3.1), and `transcripts/<persona>.md` pre-run interviews for learners who will not roleplay (a decent but imperfect interviewer; 15–30 exchanges; leaves at least one hidden fact undiscovered).
- `labs/module-NN/expert/`: the expert's deliverables, used in the NN.6 debrief for comparison.
- `curriculum/engagements/module-NN.md` (writer's notes, never imported): the hidden truth, every planted finding and where it is planted, the persona unlocks, the two or three futures. The hidden truth reaches learners only in lesson NN.6 inside `<details>`, never in the labs folder (it is downloadable).

Lesson shape for engagements: plan §3.2 (NN.1 The call … NN.6 Readout and debrief). Each lesson points to the field-kit lesson and template it applies instead of re-teaching (`../module-02/lesson-02.md`, `../../templates/interview-guide.md`).

**Inboxes.** The main session merges these into the shared files:

- `curriculum/glossary-inbox/module-NN.md`: one term per line, `- **Term** — Meaning in one sentence (lesson NN.M).` Only terms the course uses in a specific sense.
- `curriculum/inbox/templates/<name>.md`: complete drafts of templates your lessons need, with the file names from the table below (another module may already have published one: re-use it, don't redraft). A lesson links to the future path `../../templates/<name>.md`.
- `curriculum/inbox/module-NN-sources.md`: every law, regulator guidance, standard and public case you cited, with the URL you opened and the date. Mark anything you could not open `(⚠️ manual check)`.
- `curriculum/inbox/module-NN-notes.md`: anything else for the main session (a fact you could not verify, a request for a Harbor & Pine file, a cross-module inconsistency, something Tal must decide).

**Check.** Run `node curriculum/tools/check-module.mjs NN` from the course root until it reports `0 problems`. Links to templates still in your inbox and to simulations not built yet count as broken; ignore only those and list them in your report.

## Template file names (use exactly these)

| Owner | Templates |
|---|---|
| M1 | `engagement-charter`, `scope-boundary`, `change-request`, `30-60-90-plan`, `access-request-pack`, `data-room-first-read`, `shadow-ai-survey`, `ai-inventory` |
| M2 | `stakeholder-map`, `interview-guide`, `task-inventory`, `data-profile`, `readiness-assessment`, `findings-memo` |
| M3 | `opportunity-map`, `agentic-opportunity-frame`, `use-case-scorecard`, `scoring-workshop-script`, `alignment-session-agenda`, `roi-model`, `roadmap`, `decision-ready-case` |
| M4 | `acceptable-use-policy`, `approved-restricted-use-list`, `tools-and-data-classes`, `data-boundary`, `vendor-ai-questionnaire`, `claim-read-back`, `vendor-poc-protocol`, `ai-intake-register`, `dpia-for-ai`, `risk-register`, `regulatory-map`, `governance-charter` |
| M5 | `pilot-charter`, `value-measurement-plan`, `test-set-spec`, `eval-report`, `human-review-design`, `monitoring-spec`, `production-readiness-checklist` |
| M6 | `workflow-redesign`, `training-session-plan`, `champions-playbook`, `adoption-dashboard-spec`, `comms-plan` |
| M7 | `steering-pack`, `decision-record`, `pressure-test-log`, `incident-runbook`, `operating-rhythm`, `phase-1-plan`, `deliverable-map`, `handover-pack`, `integration-check` |
| M10 | `rfp-for-ai-vendors` |
| M14 | `agent-permission-map` |

A template is a markdown page: H1 = its name, one plain paragraph on when to use it, `## How to fill it` (short), then the template itself (headings, tables, `[placeholders]`), then `## Example` with a short filled excerpt from Harbor & Pine. Spreadsheet-shaped templates also get a CSV in `labs/module-NN/` linked from the page.

## Lesson format

Front-matter exactly as the instructions §4 show. Then the H1 `# NN.M · Title`, then one plain intro paragraph (what you will do in this lesson and what you will have at the end).

- `objectives`: 2–4, quoted, measurable ("Write…", "Decide…", "Measure…").
- `minutes`: reading time, usually 12–20. `practice_minutes`: the honest time of "Your turn", usually 30–120.
- `volatility`: `implementation` for anything with tools, prices, models, law dates; else `concept`.
- `sources`: every law, standard, guidance, price, tool feature and public case the lesson relies on. Only URLs you opened (WebFetch) at writing time. gov.il and some Israeli sites block bots: if you cannot open a URL you are sure of, you may cite it and note `(⚠️ manual check)` in your sources inbox. `last_verified`: the date you checked.

The five `##` sections, in this order, in every lesson (the checker enforces them):

1. `## The situation` — where you are in the engagement, what just happened, why this step now. Name an IBM idea in one line when the lesson builds on it ("IBM calls this the capacity screen; here you build it.").
2. `## What to do` — the method, step by step (`###` per step), with a worked example on the organization's real data-room files. This is the core of the lesson: concrete enough that the learner could do it in a real organization on Monday.
3. `## Watch out` — the common mistakes and how to recover from each (short; this is where "what fails" lives).
4. `## Your turn` — the task, with `###` subsections exactly: `### Inputs` (data-room files, persona, template, all linked), `### Steps`, `### Time`, `### Done when` (checkable criteria), then a `<details><summary>Reference answer</summary>…</details>` block with a real model answer (the actual numbers, the actual memo excerpt), not a description of one. Track B steps, where the lesson has them, go in `### Steps` under a `**Track B (Python)**` paragraph that says why Python is worth it here.
5. `## References` — bulleted, the sources from the front-matter plus links to related lessons, templates and simulations.

Rules inside lessons:

- **Israel first.** Organizations are Israeli. Israeli law and regulators are the primary layer (Privacy Protection Law 5741-1981 incl. Amendment 13, Privacy Protection (Data Security) Regulations 5777-2017, Privacy Protection Authority guidance, government AI policy, sector regulators, labour law and works committees). Give an Israeli law's Hebrew name once, then English. EU (GDPR, AI Act) second where it reaches the organization; US and standards (NIST AI RMF, NIST AI 600-1, ISO/IEC 42001) last. Never state a legal requirement without a source; this course is not legal advice, and lessons say when to route a question to counsel or the DPO.
- **Money** in ₪ (NIS), with a US$ figure only where a vendor prices in dollars. Say the exchange rate and date used.
- **Tools.** Tool-agnostic. Where a lab needs a tool, name current options (Microsoft 365 Copilot / Copilot Studio, ChatGPT Enterprise/Business, Claude for Work, Gemini for Workspace, n8n/Zapier/Make) and say what was checked when. Prices, model names, plan names and features change: verify each against the vendor's page at writing time.
- **People and companies.** All organizations and people are fictional, with names that reflect Israel's workforce (Hebrew, Arabic, Russian, Amharic, English names). Real companies appear only as vendors, as public case files (plan §4, verified), or in a source.
- **Languages.** The data rooms contain Hebrew, Arabic, Russian and English text where the organization would have it; evals test those languages. Lesson prose is English; quote non-English data with an English gloss.
- **Roleplays.** A lesson that uses a persona links the persona file, tells the learner what to find out, and links `../../labs/common/coach-prompt.md` for feedback; the pre-run transcript is the no-roleplay path.
- **Simulations.** Link on its own line: `[Simulation: Pilot economics](../../simulations/pilot-economics/index.html?preset=harbor)`. Use the names in plan §3.3. Each lesson must work without the simulation.
- **Safety.** Anything that can harm people, systems or data (a live agent with write access, real customer data, a production change) opens with `> [!WARNING]`. Labs use the synthetic data rooms; the optional real engagement (18.4) gets `> [!CAUTION]` on permission and confidentiality.
- **Links.** Relative only. A link into `labs/module-NN/` or `labs/common/` downloads the module zip (that is fine: say "in the module download"). No `#/` or `?id=` links.
- Allowed HTML: only `<details>`, `<summary>`, `<kbd>`, `<sub>`, `<sup>`, `<br>`. Mermaid diagrams are welcome.
- Length: aim for 1,500–3,000 words per lesson; the worked example and the reference answer carry the weight.

## Quizzes (lesson and module)

Instructions §5 are binding. In short:

- Exactly 4 options, one correct, `correct` 0–3, spread across positions in every file (no file with all answers in one or two positions), an `explanation` that teaches.
- No "all/none of the above". The correct option is not the longest or the most hedged; all four similar in length and tone.
- Questions are realistic decisions in an engagement, not recall: "The sponsor wants the pilot live in two weeks and the test set has 40 items. What do you do first?"
- Use `>-` scalars for every text field. Parse every file (the checker does).

## Python (Track B)

Python 3.12+. Import the shared helpers from `labs/common/fieldkit/` (see `labs/common/README.md`); do not copy them into your lab. Any extra dependency must be pinned in your lab's `requirements.txt` and justified in the README. Scripts read the data-room files by relative path, never need network access except the LLM call, and print what they found. An LLM call always goes through `fieldkit.llm` so the learner can pick a provider. Never put a key in a file; read it from the environment.

## Final report (under 200 words)

The files you wrote; lesson count; the checker result; template and simulation links waiting; any ⚠️ facts you could not verify; anything Tal must decide; the module time estimate (sum of minutes + practice_minutes + project time + 30 min quizzes, in hours).
