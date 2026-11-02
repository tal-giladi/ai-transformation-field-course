# Module 05 — sources cited

All opened on 2026-11-02 unless marked.

## Israel

| Source | URL | Used in | What it supports |
|---|---|---|---|
| WIPO Lex, Protection of Privacy Law, 5741-1981 (unofficial English, 2014; Hebrew controlling) | https://www.wipo.int/wipolex/en/text/347462 | 05.2 | Section 2(9): use of information for a purpose other than the one prescribed is an infringement; section 8(b): database information used only for its purposes |
| Pearl Cohen, "Major amendment to Israeli privacy law set to take effect" (3 Aug 2025) | https://www.pearlcohen.com/major-amendment-to-israeli-privacy-law-set-to-take-effect/ | 05.2 | Amendment 13 effective 14 August (2025); broader definitions; registration limited; DPO duty; administrative fines |
| Pearl Cohen, "Israel: New Draft Guidelines on the Application of Privacy Law to AI" (4 May 2025) | https://www.pearlcohen.com/israel-new-draft-guidelines-on-the-application-of-privacy-law-to-ai/ | 05.2, 05.5 | PPA draft: notify individuals when interacting with a bot; explain purposes and methods of AI processing; DPIAs; generative-AI use policies. Still a draft; gov.il original not opened ⚠️ manual check |
| Shibolet & Co., article on the PPA's guide to regulation 10(d) of the Data Security Regulations (guide dated 29 Sep 2024; article 30 Sep 2024; Hebrew) | https://www.shibolet.com/מדריך-פעולה-של-הרשות-להגנת-הפרטיות-ליי/ | 05.7 | Medium/high security databases: document access by users and code components (identity, time, component, access type, scope, allowed/denied); keep logs at least 24 months. Law-firm summary; the PPA's own guide on gov.il not opened ⚠️ manual check |

## EU

| Source | URL | Used in | What it supports |
|---|---|---|---|
| AI Act Explorer, Article 50 | https://artificialintelligenceact.eu/article/50/ | 05.5 | 50(4): deployers disclose AI-generated text published to inform the public on matters of public interest, except where human review/editorial control and editorial responsibility; Article 50 applies from 2 Aug 2026. Consistent with `references/laws-and-guidance.md` (Digital Omnibus keeps Article 50's date; grace period for 50(2) only). EUR-Lex text not re-opened ⚠️ manual check |

## Standards and security

| Source | URL | Used in | What it supports |
|---|---|---|---|
| NIST, AI 600-1 Generative AI Profile (26 Jul 2024) | https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence | 05.2, 05.4, 05.6, 05.7 | Publication page only (title, number, date, voluntary companion profile to AI RMF). Lessons cite it generally for pre-deployment testing and monitoring; no specific action number quoted |
| OWASP GenAI Security Project, LLM01:2025 Prompt Injection | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ | 05.3, 05.6 | Direct and indirect injection; no fool-proof prevention; mitigations: constrain behaviour, separate untrusted content, least privilege, human approval for privileged operations, adversarial testing |

## Vendors and tools (checked 2026-11-02)

| Source | URL | Used in | What it supports |
|---|---|---|---|
| Claude pricing | https://claude.com/pricing | 05.3, 05.4 | Opus 5.5 $4/$20, Sonnet 5.5 $2/$10, Haiku 5.5 $0.10/$0.50 (≤100K tokens) per MTok; "Save 50% with batch processing"; Team and Enterprise include Projects |
| Anthropic, Models overview | https://platform.claude.com/docs/en/about-claude/models/overview | 05.3, 05.4, 05.7 | Model IDs; "Every Claude model ID is a pinned snapshot"; Batch API 50% off |
| Anthropic, Model deprecations | https://platform.claude.com/docs/en/about-claude/model-deprecations | 05.7 | At least 60 days' notice before retirement of publicly released models; requests to retired models fail; Sonnet 4.5 deprecated 30 Sep 2026, retires 30 Nov 2026; Sonnet 5.5 not sooner than 28 Sep 2027; `temperature`/`top_p`/`top_k` removed in API version 2026-10-21 |
| Anthropic, Commercial Terms of Service | https://www.anthropic.com/legal/commercial-terms | 05.3 | "Anthropic may not train models on Customer Content from Services"; business customers; consumer offerings under separate terms |
| Claude Help Center, What are projects? | https://support.claude.com/en/articles/9517075-what-are-projects | 05.3 | Project instructions and knowledge; projects on all plans (free: 5); RAG on paid plans |
| Google Gemini Help, Gems | https://support.google.com/gemini/answer/15146780?hl=en | 05.3 | Gems with instructions and knowledge files; appear in the Workspace side panel; personal-account Gems moving to "skills" from Nov 2026 |
| Microsoft Learn, Copilot Studio overview (updated 27 Oct 2026) | https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio | 05.3 | Agents with instructions and knowledge; evaluations with test sets and graders |
| OpenAI, ChatGPT Business data and projects pages | https://openai.com/business-data/ ; https://help.openai.com/en/articles/10169521-projects-in-chatgpt | 05.3 | Both returned HTTP 403. The lesson names ChatGPT projects/custom GPTs only as options and tells learners to confirm data terms themselves ⚠️ manual check |

## Public cases

| Source | URL | Used in | What it supports |
|---|---|---|---|
| Evans Hudson LLP summary of *Moffatt v. Air Canada*, 2024 BCCRT 149 | https://ehlaw.ca/?p=22062 | 05.2 (by reference to 03.3) | Chatbot said retroactive bereavement fares were allowed; negligent misrepresentation; CA$650.88. Tribunal page not opened (403 in module 3) ⚠️ manual check |

## IBM (named, not re-taught)

| Source | URL | Used in |
|---|---|---|
| IBM Enterprise AI Transformation and Consulting (Coursera) — course list confirmed | https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting | 05.1, 05.4, 05.5 |
| IBM Lead AI Transformation: Strategy, Governance & Execution (Coursera) — course list confirmed | https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution | 05.1, 05.5, 05.6, 05.7 |

## For references/laws-and-guidance.md

- Add: Privacy Protection (Data Security) Regulations — PPA guide to regulation 10(d) (logs and documentation files, 29 Sep 2024): documentation of access, 24-month retention for medium/high security. Source above (law-firm summary) ⚠️ verify on gov.il.
