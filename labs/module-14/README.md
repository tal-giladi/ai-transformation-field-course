# Module 14 lab files — Lumen SaaS

Everything you need to run the Lumen SaaS engagement: the brief, the data room, the people you interview, a blank permission map, the must-refuse tests and red-team scripts with a small harness that runs them against a mock agent, Track B scripts for discovery, and (for the debrief only) the expert's deliverables. All people, companies, customers and products are fictional and all data is synthetic. Nothing here is legal advice.

> [!WARNING]
> The harness never touches a real system: the agent only proposes tool calls and the gate decides. Run the tests and red-team scripts only against this mock, the simulation, or a non-production copy that its owner and security have authorised in writing. Against a live agent, a successful test is a real credit, a real password reset or a real email with staff data.

## What is in this folder

| Path | What it is | Lesson |
|---|---|---|
| `brief.md` | The engagement brief: how you were hired, the stated ask, budget, authority, timeline, access on day one | 14.1 |
| `data-room/` | Lumen's data room: start with [`INDEX.md`](data-room/INDEX.md). Customers and contracts, the Assist beta's sessions, retrievals and tool calls, a transcript sample, support tickets, the credits ledger, the help centre's index and revisions, API tokens, the admin audit log, AI expenses, IT's inventory, feature-flag history, policies, product documents, an Enterprise customer's questionnaire | 14.1–14.6 |
| `data-room/generate.py` and its modules | The seeded generator (Python standard library only): `python generate.py` rebuilds every data-room file byte for byte. Reading it spoils the engagement | — |
| `personas/` | The cast of nine ([README](personas/README.md)): roleplay prompts and pre-run transcripts | 14.1–14.6 |
| `discovery.py` | Track B: who acts as whom in the audit log, credits by issuer, what the agent did with each HC-214 version, tool calls after the flag, emails off file, resolution two ways, tokens against leavers, AI spend | 14.2, 14.3 |
| `agent-permission-map.csv` | The permission map's actions table as a blank spreadsheet (template: `templates/agent-permission-map.md`) | 14.4 |
| `harness/negative-tests.csv` | 21 must-refuse and 7 must-do tests, one row each, with the facts the gate can check and the expected result | 14.5 |
| `harness/red-team-scripts.csv` | 14 red-team scripts: direct and indirect injection, a poisoned or stale document, a file, social engineering, confused customers, an abuse burst, a contract hijack, exfiltration; Hebrew, Arabic, Russian, English | 14.5 |
| `harness/maps/demo.json` | The product team's GA design as a permission map (everything on, no limits outside the prompt) | 14.5 |
| `harness/maps/my-map.json` | Your map: starts as a copy of the design; edit it | 14.5 |
| `harness/gate.py`, `mock_agent.py`, `run_harness.py` | Track B: the permission gate (the tool layer), two mock agents (scripted worst case; an LLM through `fieldkit.llm`), and the runner that writes a report | 14.5 |
| `harness/reports/` | Reports for the product design, with the scripted agent and with the mock LLM | 14.5 |
| `expert/` | The expert's deliverables, maps and reports, for comparison in the debrief; open them only after your own ([README](expert/README.md)) | 14.6 |

## Track A — no code

1. Open the CSV files in Excel, Google Sheets or LibreOffice Calc. In Excel use *Data → From Text/CSV* and choose *65001: Unicode (UTF-8)*; the files contain Hebrew, English, Arabic and Russian, and commas inside quotes. Timestamps are Israel local time.
2. **14.2, the replaced article:** filter `assist-beta/retrievals.csv` for `article_id` = HC-214; look up each `session_id` in `assist-beta/tool-calls.csv` (`XLOOKUP` on `session_id`, tool `issue_credit`); line the times up with `support-kb/help-centre-revisions.csv`. **Who acts as whom:** pivot `it/admin-audit-log.csv` by `actor` and `user_agent`, with the hour (`=HOUR(timestamp)`) in columns. **The fleet:** look up each `created_by` in `it/api-tokens.csv` against `people/staff-directory.csv`; pivot `it/saas-expenses-ai-2026.csv` by department and vendor.
3. **14.3, resolution:** in `assist-beta/sessions.csv` add a helper column that is 1 when the same `customer_id` has a ticket (`support/tickets.csv`, same `category`) or another session (same `intent`) within 7 days after `started_at` (`COUNTIFS` with date bounds); 7-day resolution = closed or abandoned sessions with 0 in that column, divided by all sessions.
4. **14.4:** fill `agent-permission-map.csv`, one row per tool.
5. **14.5:** copy `harness/negative-tests.csv` and `harness/red-team-scripts.csv` into a sheet; for each row walk your map (granted? which limit? which rung?) and add two columns: the control that stops it, and the verdict (PASS, PASS (person), PASS (soft), FAIL). Compare with `harness/reports/demo-scripted.md`.
6. The [simulation](../../simulations/agent-authority/index.html?preset=lumen) (`agent-authority`, preset `lumen`) runs the same tools, limits and scripted events as a week; it opens in a browser with no setup.

## Track B — Python

Set up the field kit once ([instructions](../common/README.md)): Python 3.12 or newer and `pip install -r ../common/requirements.txt`. No extra packages: the module's scripts use the standard library plus `fieldkit`. From this folder:

```bash
python discovery.py                                        # 14.2, 14.3: the discovery numbers
cd harness
python run_harness.py --map maps/demo.json                 # the product design, scripted worst case
python run_harness.py                                      # your map (maps/my-map.json)
python run_harness.py --set negative                       # only the negative tests
```

To ask a model which tool it would call (14.5), choose the provider with environment variables (PowerShell shown):

```powershell
$env:FIELDKIT_PROVIDER = "mock"        # no key, no network: proves the harness runs
python run_harness.py --agent llm
$env:FIELDKIT_PROVIDER = "anthropic"   # or openai, ollama; set the provider's key variable and FIELDKIT_MODEL
python run_harness.py --agent llm
```

Every LLM call goes through `fieldkit.llm.complete` and is cached in `.fieldkit-cache/` where you run it, so re-running on the same inputs costs nothing. With the mock provider the model proposes no tool call, so every must-refuse case "passes (soft)" and every must-do case fails: that is the refusal trap the lesson discusses, not a bug. On Windows, if Hebrew or Arabic prints as `?`, run `$env:PYTHONIOENCODING = "utf-8"` first. The scripts read files by relative path and make no network request except the LLM call.

The map format is the simulation's: per tool a `rung` (`off`, `approve`, `two`, `auto`) and limits (`cap`, `dailyTotal`, `perCustomerDay`, `tiers`, `verify`, `ownAddressOnly`, `softDelete`); and global `logging` (`none`, `actions`, `full`), `ownIdentity`, `killSwitch`, `promptRule`, `sourceControl`. Python is worth it in this module because the suite must run identically after every prompt, model, tool, limit or source change, and because the discovery joins are on timestamps across five files.

**What is real and what is not.** Every number computed from the data room, the harness and the simulation reproduces exactly (for example: 12 credits from the replaced article, ₪19,368; 8 tool calls after the flag went off; 7-day resolution 35.5% against the dashboard's 63.2%; the product design fails 33 of 35 must-refuse cases with the scripted agent, the expert's target map passes all 35). The red-team contractor's findings, the kill-switch drill and the events after 21 January in `expert/05` and `expert/06` are an illustrative worked example.

Checked on 3 November 2026 with Python 3.14.3, end to end with `FIELDKIT_PROVIDER=mock`; the data room was generated twice and compared byte for byte. The `agent-authority` simulation's `lumen` preset was run with the product design, the expert's stage 1 and its target map on the same date.

## What each lesson uses

| Lesson | Files |
|---|---|
| 14.1 The call | `brief.md`; `data-room/company/`, `product/assist-ga-design.md`, `product/assist-incident-runbook.md`, `it/ai-inventory-2026-09.csv`; persona Revital |
| 14.2 Discovery | `assist-beta/`, `support-kb/`, `billing/credits-ledger.csv`, `it/`, `people/staff-directory.csv`, `support/tickets.csv`; `discovery.py`; personas Maya, Andrei, Yonatan, Nurit, Shira |
| 14.3 Diagnosis | `assist-beta/sessions.csv`, `support/tickets.csv`, `people/support-shifts.csv`; `discovery.py`; personas Svetlana, Yaron |
| 14.4 The hard part | `product/`, `policies/`, `legal/`, `it/api-tokens.csv`, `customers/`; `agent-permission-map.csv`; the simulation; personas Shira, Andrei, Nurit, Amir |
| 14.5 Build | `harness/`; the simulation; personas Yonatan, Maya |
| 14.6 Readout | Everything above; `expert/`; personas Maya, Yaron, Revital, Andrei, Nurit, Amir |
