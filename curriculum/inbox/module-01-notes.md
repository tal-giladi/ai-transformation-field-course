# Module 01 — notes for the main session

Written 2026-11-02 by the module 1 agent. Nothing committed.

## Cross-module inconsistencies (shared files I may not edit)

1. **2 November 2026 is a Monday, not a Sunday.** The data room and personas say "Sunday 2 November
   2026": `labs/common/harbor-and-pine/INDEX.md` line 5, `personas/michal-coo.md` line 11,
   `personas/transcripts/michal-coo.md` line 3, and `curriculum/engagements/harbor-and-pine.md` line 23.
   Also `personas/transcripts/noa-marketing.md` line 3 says "Wednesday 5 November 2026"; 5 November is
   a Thursday. Module 1 avoids naming the weekday of 2 November and uses the correct weekdays elsewhere
   (Thu 5 Nov plan deadline, Thu 10 Dec monthly review, Thu 21 Jan pre-read, Thu 28 Jan board; first
   week = four working days, Mon 2 – Thu 5 Nov). Suggested fix: change "Sunday" to "Monday" in those
   four files and "Wednesday 5 November" to "Thursday 5 November" in the Noa transcript (or move the
   Noa meeting to Wednesday 4 November and keep the weekday). No data file depends on it.
2. **Container frequency.** `company/company-profile.md` says "roughly 2 a week"; `orders/shipments.csv`
   has 112 containers departing 27 Feb – 19 Nov 2026 (~3 a week), and the profile's own schedule
   (Vietnam and China weekly, Turkey and Italy fortnightly) also makes 3. Lesson 01.5 uses this as a
   "contradicted" claim in the first read. If it was unintended, keep it anyway (it is a good plant)
   and add it to the "Other plants" list in `curriculum/engagements/harbor-and-pine.md`.
3. **Missing transcripts for Avi and Dana.** `personas/README.md` lists no pre-run transcript for Avi
   (01.6) or Dana (01.7). I wrote them as module files: `labs/module-01/avi-it-interview-transcript.md`
   (misses: Olga's unanswered tool request; AI in software updates) and
   `labs/module-01/dana-hr-interview-transcript.md` (misses: her worry about usage monitoring). If you
   prefer them in `labs/common/harbor-and-pine/personas/transcripts/`, move them and update the
   "Transcript" column in `personas/README.md` and the two links in lessons 01.6 and 01.7.
4. **Shadow-AI user counts.** Lesson 01.6 reports ChatGPT in Customer Service as 4 distinct users
   (chatgpt.com + chat.openai.com, 160 requests) as computed by `census.py`; the writer's notes say
   "Distinct generative-AI users: Customer Service 5" (which also counts Gemini). Both are right for
   their definitions; no change needed, just don't "correct" one to the other.

## Templates

All eight M1 templates are complete drafts in `curriculum/inbox/templates/`: engagement-charter,
scope-boundary, change-request, 30-60-90-plan, access-request-pack, data-room-first-read,
shadow-ai-survey, ai-inventory. Four have spreadsheet versions in `labs/module-01/`
(`change-request-log.csv`, `data-room-first-read.csv`, `shadow-ai-census.csv`, `ai-inventory.csv`),
linked from the template pages as `../labs/module-01/<file>.csv`. With the templates copied into
`templates/`, `check-module.mjs 01` reports 0 problems (tested in a scratch copy).

## Facts I could not fully verify (also marked ⚠️ in module-01-sources.md)

- OpenAI's help, privacy and pricing pages return HTTP 403 to the fetch tool, so no OpenAI terms or
  prices are stated. Lesson 01.6 uses Google's and Anthropic's own pages for the consumer-vs-business
  point, and LinguaFlow's (fictional) DPA from the data room.
- Regulation 15 of the Data Security Regulations and the PPA's 2011 outsourcing guidance are cited
  through a 2020 law-firm guide; the gov.il text was not opened.
- Isakov Inbar (2011) via a law-firm summary; the Hebrew judgment was not opened.
- Equal Opportunities Law, section 2: an old unofficial English translation; the current Hebrew text has
  more protected grounds.
- The Commission's AI-definition guidelines: publication date opened; "not applied mechanically" from
  secondary summaries.

## For Tal to decide

- Lesson 01.1 prices an illustrative consultant Phase 0 at 22 days × ₪5,500 = ₪121,000 plus VAT, and
  says it is not a market figure. If you'd rather show a range from a real Israeli rate survey, say so
  and a later pass can source one.

## Other

- Module 1 uses no simulation (none in plan §3.3 fits lessons 01.1–01.7).
- Track B scripts (`first_read.py`, `census.py`) were run on 2026-11-02 against the data room with
  Python 3.14.3 + pandas 3.1.0 in a scratch venv; output matches the numbers in lessons 01.5 and 01.6.
  They make no LLM or network calls.
- Module time (for BUILD_PROGRESS): reading 119 min + practice 460 min + project 300 min + quizzes 30 min
  ≈ 15.2 hours.
