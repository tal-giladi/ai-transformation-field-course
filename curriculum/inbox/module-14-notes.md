# Module 14 — notes for the main session (Lumen SaaS)

## To merge

- Template `agent-permission-map` drafted in `curriculum/inbox/templates/agent-permission-map.md` (build-spec format, Harbor & Pine example). Its spreadsheet version is `labs/module-14/agent-permission-map.csv`, linked from the template as `../labs/module-14/agent-permission-map.csv`. Lessons 14.4, 14.5, the project and `labs/module-14/expert/04-permission-map.md` link to `templates/agent-permission-map.md` (the only links the checker reports as broken).
- Glossary: `curriculum/glossary-inbox/module-14.md` (16 terms).
- `templates/README.md` will need a line for the new template (M14).
- `_sidebar.md`: Module 14 — Lumen SaaS, lessons 14.1–14.6 with these titles: The call · Discovery · Diagnosis · The hard part: agent authority · Build: tests, red team and staged autonomy · Readout and debrief; then the module quiz.
- `references/laws-and-guidance.md`: suggest adding OWASP Top 10 for LLM Applications 2025 and the OWASP Top 10 for Agentic Applications 2026 under standards (see the sources inbox).

## The agent-authority preset (`lumen`): what the module matches and what I would change

The engagement matches the preset exactly: seven tools and their ids; the product team's demo set-up (`startConfig`); the expert config (credits ₪300 / ₪2,000 a day / 1 per customer a day, Starter and Growth; plan changes one approver, Starter and Growth; 2FA after verification; delete not granted with soft delete; email to the address on file; full trace, own identity, kill switch, prompt rule, source control); invoice run Thursday 22:00; 48-hour contract sync; 14-day soft delete; 30 approvals a day (two shift leads × 30 minutes in `people/support-shifts.csv`); 12 minutes a handoff; the replaced article "Downgrades and refunds" on a Monday; 11 days to discovery with no agent log; the staged plan (weeks 1–2 on approval, then credits alone). The expert's harness maps (`labs/module-14/expert/maps/stage-1.json`, `stage-2.json`) use the preset's config format, and stage 2 is the preset's `expert.config` verbatim. Simulation results quoted in 14.4–14.6 were produced by running `model.js` with the preset (demo: ₪6,450 lost, 24,436 records, 33 unrecovered harms; expert: nothing lost, 3 handed off, 30 approvals, 196 minutes; stage 1: 103 approvals, 5 rubber-stamped, 333 minutes).

Suggested preset edits (I did not touch `simulations/`):

1. **`outageCredit.why`** says "The agent may credit up to ₪500". In the data room ₪500 is the limit for support *people* (`policies/credit-policy.md`), and the agent's cap in the expert map is ₪300. Suggest: "Support staff may credit up to ₪500 and the agent up to ₪300; above ₪500 the account manager decides, because outage credits are in the contract."
2. **`reset2fa` in `expert.config`** has no `tiers` limit, so verified Enterprise resets execute alone. In the engagement Enterprise is excluded from the launch entirely. Harmless in the sim (the only Enterprise reset event is unverified), but adding `tiers: ['starter', 'growth']` would match the lesson. If changed, the validator's "expert loses nothing" check should still pass.
3. The sim's stale-article credits (₪1,100 / ₪1,300 / ₪900, Tavor / Carmel / Arava) are a model week; the data room's real beta incident has 12 credits with exact amounts (Tavor ₪1,104, Carmel ₪1,296, Arava ₪912 among them). Lessons say the simulation is "a scripted week" and quote the data room for the incident. No change needed; noted so nobody "fixes" one to match the other.

## Shared helper issue (labs/common, not mine to edit)

- `fieldkit.data.load()` parses every `*_at` / `*_date` / `timestamp` column with `utc=True` and converts to Asia/Jerusalem. Naive timestamps that are already Israel local time (all of module 14's, and probably other data rooms') shift by +2 or +3 hours. Module 14's scripts use the standard library `csv` and `data_room()` only, and the INDEX warns about it. Suggest: treat naive timestamps as Asia/Jerusalem (`tz_localize`) instead of UTC. Worth checking modules that compute hours of day with `load()`.

## Facts I could not verify (⚠️)

- Israeli statutes and the PPA draft AI guidance were read through the Chambers 2026 guide (secondary); Hebrew texts not opened.
- The OWASP Agentic Top 10 names come from OWASP's launch post; the resource page did not render the list and the PDF was not opened.
- The Replit incident is cited "as reported" from the AI Incident Database.
- NIST AI 600-1: publication page only; lessons cite it generally.
- EU AI Act articles via AI Act Explorer, not EUR-Lex.

## For Tal to decide

- Nothing blocking. One judgement call: the expert's reports and maps live in `labs/module-14/expert/` (downloadable, as in modules 8–12). The hidden truth and the futures are only in lesson 14.6 `<details>`.

## Not changed

- No file of module 13 or any shared file was touched. `curriculum/status/module-14.log` has lessons 01–06 and `module done`.
