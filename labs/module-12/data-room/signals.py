"""Proxy log, AI-use survey, DLP alerts, software expenses, ethics log, renewals log."""
from __future__ import annotations

from datetime import date

import textbank as tb
from common import ROOM, rng, workdays, write_csv

DOMAINS = {"chatgpt.com": "genai_chat", "claude.ai": "genai_chat", "gemini.google.com": "genai_chat",
           "copilot.microsoft.com": "genai_chat", "perplexity.ai": "genai_search",
           "notebooklm.google.com": "genai_chat", "deepl.com": "genai_translate",
           "translate.google.com": "genai_translate"}


def build_proxy(lawyers) -> list[list]:
    r = rng("proxy")
    days = workdays(date(2026, 9, 1), date(2026, 10, 31))
    assoc = [l for l in lawyers if l["role"] == "associate"]
    partners = [l for l in lawyers if l["role"] != "associate"]
    forced_a = {"L063", "L058"} | {l["id"] for l in assoc if l["group"] == "Tech & IP"}
    others = [l["id"] for l in assoc if l["id"] not in forced_a and l["id"] != "L041"]
    users_a = sorted(forced_a | set(r.sample(others, 43 - len(forced_a))))
    users_p = ["L003", "L005", "L006", "L008", "L010", "L015", "L016", "L022", "L026"]
    staff = [(f"S{100 + i}", "Secretariat" if i < 8 else "Finance") for i in range(1, 12)]
    dept = {l["id"]: l["group"] for l in lawyers}
    uploaders = set(users_p[:3]) | {"L063", "L058"} | {l["id"] for l in assoc if l["group"] == "Tech & IP"}
    rest = [u for u in users_a if u not in uploaders]
    uploaders |= set(r.sample(rest, 31 - len(uploaders) - 2))   # two staff uploaders added below
    rows = []
    profiles = []
    for u in users_a + users_p:
        heavy = u in ("L003", "L063") or dept[u] == "Tech & IP"
        profiles.append((u, dept[u], 0.55 if heavy else r.uniform(0.08, 0.35), u in uploaders))
    for s, dep in staff:
        profiles.append((s, dep, r.uniform(0.05, 0.25), s in ("S101", "S104")))
    for u, dep, p, up in profiles:
        prefs = (["chatgpt.com"] * 6 + ["claude.ai"] * 2 + ["gemini.google.com"] * 2 + ["perplexity.ai", "copilot.microsoft.com",
                 "notebooklm.google.com"] + ["deepl.com"] * 2 + ["translate.google.com"] * 2)
        if u.startswith("S"):
            prefs = ["translate.google.com"] * 4 + ["deepl.com"] * 2 + ["chatgpt.com"] * 2
        if u == "L063":
            prefs = ["chatgpt.com"] * 4 + ["deepl.com"] * 3 + ["translate.google.com"] * 2
        for d in days:
            if r.random() > p:
                continue
            for dom in sorted(set(r.sample(prefs, r.choice([1, 1, 2])))):
                req = r.randint(3, 45)
                files = r.choices([0, 1, 2, 3], [5, 3, 1, 1])[0] if up and r.random() < 0.5 else 0
                mb_up = round(req * 0.004 + files * r.uniform(0.08, 1.6), 2)
                h1 = r.randint(8, 17)
                h2 = min(23, h1 + r.randint(0, 5))
                rows.append([d.isoformat(), u, dep, dom, DOMAINS[dom], req, mb_up, round(req * 0.03 + r.uniform(0, 0.4), 2),
                             files, f"{h1:02d}:{r.randint(0, 59):02d}", f"{h2:02d}:{r.randint(0, 59):02d}",
                             "allowed (monitor only)"])
    # fixed events
    rows.append(["2026-09-03", "L058", "Corporate", "chatgpt.com", "genai_chat", 22, 1.37, 0.71, 1, "10:12", "11:40",
                 "warned (user proceeded)"])
    rows.append(["2026-10-19", "L063", "Corporate", "chatgpt.com", "genai_chat", 61, 0.42, 2.11, 2, "21:05", "23:52",
                 "allowed (monitor only)"])
    rows.sort(key=lambda x: (x[0], x[1], x[3]))
    return rows


def build_survey() -> list[list]:
    r = rng("survey")
    rows = []
    bands = ["partner"] * 12 + ["senior_associate"] * 14 + ["junior_associate"] * 21
    r.shuffle(bands)
    groups = ["Corporate", "Litigation", "Real estate", "Banking & finance", "Tech & IP", "Employment"]
    freq_w = {"partner": [6, 3, 2, 1], "senior_associate": [4, 5, 4, 1], "junior_associate": [6, 6, 7, 2]}
    for i, band in enumerate(bands, 1):
        freq = r.choices(["never", "occasionally", "weekly", "daily"], freq_w[band])[0]
        if freq == "never":
            client, uses, tools = "no", "", ""
        else:
            client = r.choices(["no", "only_anonymised", "yes"], [12, 4, 0.7])[0]
            uses = ";".join(sorted(set(r.sample(["emails", "translation", "summaries", "research", "first drafts"],
                                                r.randint(1, 3)))))
            tools = ";".join(sorted(set(r.sample(["ChatGPT", "Gemini", "Claude", "DeepL", "Copilot"], r.randint(1, 2)))))
        lang, comment = r.choice(tb.SURVEY_COMMENTS)
        rows.append([f"R{i:02d}", f"2026-10-{r.randint(5, 16):02d}", band, r.choice(groups), freq, uses, tools, client,
                     r.choice(["yes", "yes", "maybe", "no"]), comment])
    return rows


DLP = [
    ["2026-01-14", "S103", "email", "personal webmail", "Outbound to personal address", "Fwd: invoice batch Jan.pdf", "low", "allowed", "IT", "Personal admin forward; reminded"],
    ["2026-02-22", "L071", "usb", "USB storage", "Removable media copy", "trial_bundle_vol2.pdf", "medium", "blocked", "IT", "Approved exception for court bundle"],
    ["2026-03-09", "L033", "web", "wetransfer.com", "File share to unapproved cloud", "valuation_model_v3.xlsx", "medium", "warned (user proceeded)", "IT", "Sent to client at client's request"],
    ["2026-04-27", "S106", "web", "translate.google.com", "Client document marker", "letter_to_[client].docx", "medium", "warned (user proceeded)", "IT", "Reminded; no further action"],
    ["2026-05-11", "L044", "email", "personal webmail", "Outbound to personal address", "draft_opinion_he.docx", "medium", "allowed", "L004", "Associate working from home; reminded of VPN"],
    ["2026-06-02", "L063", "web", "deepl.com", "Client document marker", "SHA_[client]_RU_EN.docx", "medium", "warned (user proceeded)", "IT", "User reminded of policy"],
    ["2026-06-30", "L080", "web", "dropbox.com", "File share to unapproved cloud", "lease_comparison.xlsx", "low", "warned (user proceeded)", "IT", "No client data"],
    ["2026-07-21", "L029", "usb", "USB storage", "Removable media copy", "closing_set_final.zip", "medium", "blocked", "IT", "Use secure share instead"],
    ["2026-08-12", "L077", "web", "chatgpt.com", "Personal data pattern (ID numbers)", "employee_list.xlsx", "high", "blocked", "IT", "Blocked by pattern rule"],
    ["2026-09-03", "L058", "web", "chatgpt.com", "Client document marker (CLIENT-CONFIDENTIAL footer)", "SPA_[client]_draft_v7.docx", "high", "warned (user proceeded)", "L004", "Spoke to associate. Chat history deleted by user. No further action."],
    ["2026-09-24", "S109", "email", "personal webmail", "Outbound to personal address", "payroll_sep.pdf", "high", "blocked", "IT", "Finance clerk; HR informed"],
    ["2026-10-06", "L048", "web", "claude.ai", "Client document marker", "witness_statement_draft.docx", "high", "warned (user proceeded)", "", "Open"],
    ["2026-10-20", "L086", "web", "gemini.google.com", "Client document marker", "term_sheet_[client].pdf", "high", "warned (user proceeded)", "", "Open"],
    ["2026-10-28", "L039", "web", "perplexity.ai", "Client document marker", "pleading_v2.docx", "medium", "warned (user proceeded)", "", "Open"],
]


def build_expenses(lawyers) -> list[list]:
    r = rng("expenses")
    rows = []
    tech = ["L003"] + [l["id"] for l in lawyers if l["group"] == "Tech & IP" and l["role"] == "associate"][:5]
    others = [l["id"] for l in lawyers if l["group"] not in ("Tech & IP",)]
    for m in range(1, 11):
        for u in tech:
            if u != "L003" and m == 1 and r.random() < 0.3:
                continue
            rows.append([f"2026-{m:02d}-{r.randint(2, 6):02d}", u, "Tech & IP", "OpenAI *ChatGPT Plus",
                         "Software subscription (monthly)", round(r.uniform(70, 76), 2), "software", "L003"])
        for _ in range(r.randint(2, 4)):
            u = r.choice(others)
            v, desc, amt = r.choice([("Zoom", "Video meetings (monthly)", 58), ("Adobe Acrobat Pro", "PDF editing (monthly)", 89),
                                     ("LinkedIn Premium", "Business development", 140), ("Dropbox Plus", "File storage", 45),
                                     ("Grammarly Premium", "English editing (monthly)", 45), ("Zoom", "Video meetings (monthly)", 58)])
            rows.append([f"2026-{m:02d}-{r.randint(2, 27):02d}", u, next(l["group"] for l in lawyers if l["id"] == u), v, desc,
                         round(amt * r.uniform(0.95, 1.05), 2), "software", "finance"])
    rows.sort()
    return rows


ETHICS = [
    ["2026-01-19", "Real estate", "conflict", "New buyer client vs existing developer client", "closed"],
    ["2026-02-03", "Corporate", "ai-tools", "Associate asks if ChatGPT may be used to polish English of a client email; answered: no client details", "closed"],
    ["2026-03-15", "Litigation", "privilege", "Expert's draft report shared with client's insurer; privilege view", "closed"],
    ["2026-04-08", "Corporate", "ai-tools", "Associate asks whether a free tool may translate a Russian shareholders' agreement; answered: not without client consent", "closed"],
    ["2026-05-21", "Employment", "confidentiality", "Former client's HR files requested by new client", "closed"],
    ["2026-06-02", "Corporate", "ai-tools", "DLP warning: DeepL upload of shareholders' agreement; reminded", "closed"],
    ["2026-07-12", "Tech & IP", "fees", "Fixed-fee package overrun; can extra hours be billed? Answered: not without agreement", "closed"],
    ["2026-08-30", "Banking & finance", "conflict", "Lender and borrower group companies", "closed"],
    ["2026-09-03", "Corporate", "ai-tools", "DLP: draft SPA uploaded to consumer AI tool; client not informed; outside ethics counsel asked whether disclosure is required", "open - awaiting outside ethics counsel"],
    ["2026-09-17", "All", "ai-tools", "Bar Association ethics committee published expanded AI opinion; firm policy needed", "open"],
    ["2026-10-02", "Corporate", "client-terms", "Carmel outside-counsel guidelines received: AI disclosure and consent clause; no firm policy to answer it", "open"],
    ["2026-10-14", "All", "insurance", "PI insurer renewal questionnaire includes AI controls section; due 15 Jan 2027", "open"],
    ["2026-10-23", "Tech & IP", "ai-tools", "Partner asks whether 'time saved by AI' may be billed as value under fixed fee (draft AI policy)", "open"],
]

RENEWALS = [
    ["2025-01-15", "C-003", "Banking & finance", "rate review", "rate freeze for 2025", "budget pressure", "freeze agreed", 0.0],
    ["2025-02-10", "C-005", "Corporate", "rate review", "standard 4% increase", "firm proposal", "accepted", 4.0],
    ["2025-03-02", "C-022", "Corporate", "panel renewal", "5% discount on hourly rates", "volume", "3% discount", -3.0],
    ["2025-04-20", "C-011", "Real estate", "rate review", "standard 4% increase", "firm proposal", "accepted", 4.0],
    ["2025-06-12", "C-019", "Litigation", "panel renewal", "capped fees for all new claims", "predictability", "caps on claims under ₪500k", 0.0],
    ["2025-09-01", "C-026", "Employment", "retainer review", "retainer cut from ₪30,000 to ₪25,000 a month", "fewer queries", "₪27,000 a month", -10.0],
    ["2025-11-20", "C-014", "Corporate", "annual renewal", "fixed price ₪900 per NDA from 2026", "turnaround now under one day; templates automated", "₪1,150 per NDA from 1 Jan 2026", None],
    ["2025-12-10", "C-041", "Employment", "retainer review", "10% off retainer", "your employment templates are automated now", "6% off", -6.0],
    ["2026-01-05", "C-007", "Litigation", "rate review", "standard 4% increase", "firm proposal", "accepted 2%", 2.0],
    ["2026-02-16", "C-009", "Tech & IP", "fixed-fee package review", "seed-round package from ₪38,000 to ₪30,000", "faster turnaround seen in 2025; competitor quotes", "₪35,000", -7.9],
    ["2026-03-30", "C-040", "Corporate", "panel renewal", "blended rate cap", "budget", "blended cap ₪1,150 per hour", -5.0],
    ["2026-05-18", "C-002", "Real estate", "rate review", "standard 4% increase", "firm proposal", "accepted", 4.0],
    ["2026-06-07", "C-012", "Banking & finance", "rate review", "fixed fee per facility agreement", "predictability", "under discussion", None],
    ["2026-07-01", "C-022", "Corporate", "panel renewal", "disclose AI use; 5% discount", "AI expected to reduce cost", "disclosure clause agreed; 2% discount", -2.0],
    ["2026-09-14", "C-031", "Litigation", "panel tender", "panel of two firms for 2027-2029", "competitor offered fixed fees about 30% lower with AI-assisted document review", "lost", -100.0],
    ["2026-10-29", "C-014", "All", "renewal 2027 (call from GC to managing partner)", "15% off all hourly rates from 2027", "OCG 1 Oct 2026; 'your efficiency should reach us'", "open", None],
]


def write_signals(lawyers, clients_by_code) -> None:
    write_csv(ROOM / "it" / "proxy-ai-domains-2026-09-10.csv",
              ["date", "user_id", "department", "domain", "category", "requests", "mb_up", "mb_down",
               "file_uploads", "first_request", "last_request", "policy_action"], build_proxy(lawyers))
    write_csv(ROOM / "surveys" / "ai-use-survey-2026-10.csv",
              ["response_id", "submitted_date", "role_band", "practice_group", "ai_use_frequency", "used_for",
               "tools", "client_information_in_ai", "would_use_firm_tool", "comment"], build_survey())
    write_csv(ROOM / "it" / "dlp-alerts-2026.csv",
              ["alert_date", "user_id", "channel", "destination", "rule", "file_name", "severity", "action",
               "closed_by", "closure_note"], DLP)
    write_csv(ROOM / "finance" / "expense-claims-software-2026.csv",
              ["claim_date", "employee_id", "practice_group", "vendor", "description", "amount_ils", "category",
               "approved_by"], build_expenses(lawyers))
    write_csv(ROOM / "risk" / "ethics-log-2026.csv",
              ["logged_date", "from_group", "topic", "summary", "status"], ETHICS)
    rows = []
    for d, c, g, kind, asked, reason, outcome, pct in RENEWALS:
        fees = clients_by_code.get(c)
        rows.append([d, c, g, kind, asked, reason, outcome, "" if pct is None else pct,
                     fees[5] if fees else ""])
    write_csv(ROOM / "clients" / "renewals-and-rate-negotiations.csv",
              ["date", "client_code", "practice_group", "event", "client_asked", "reason_given", "outcome",
               "change_pct", "client_fees_2025_ils"], rows)
