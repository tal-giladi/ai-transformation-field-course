"""it/proxy-ai-hosts-2027-q2.csv and incident/it-tickets-ai.csv."""
from datetime import date, timedelta

from gen_common import MABAT_FEED_BROKEN, rng, write_csv

HOSTS = [
    # department, host, category, action, base requests a week, base upload KB a week
    ("Customer Service", "api.promptway.ai", "uncategorised", "allowed", 1900, 23000),
    ("Customer Service", "app.kotev.ai", "Sanctioned - AI assistant", "allowed", 640, 3100),
    ("Customs - Haifa", "translate.freedocs.net", "Translation", "allowed", 520, 41000),
    ("Customs - Ashdod", "translate.freedocs.net", "Translation", "allowed", 610, 48000),
    ("Customs - Haifa", "app.kotev.ai", "Sanctioned - AI assistant", "allowed", 60, 300),
    ("Operations - Centre", "chat.promptway.ai", "Generative AI - public", "blocked", 140, 0),
    ("Operations - South", "chat.promptway.ai", "Generative AI - public", "blocked", 95, 0),
    ("Sales", "app.kotev.ai", "Sanctioned - AI assistant", "allowed", 410, 1900),
    ("Sales", "chat.promptway.ai", "Generative AI - public", "blocked", 70, 0),
    ("Finance", "app.kotev.ai", "Sanctioned - AI assistant", "allowed", 380, 2600),
    ("HQ", "app.kotev.ai", "Sanctioned - AI assistant", "allowed", 520, 2900),
    ("Operations - North", "route.tzir.ai", "Sanctioned - business application", "allowed", 2600, 900),
    ("Customs - Ashdod", "docs.tzir.ai", "Sanctioned - business application", "allowed", 3300, 210000),
    ("Customs - Haifa", "docs.tzir.ai", "Sanctioned - business application", "allowed", 3100, 196000),
]


def proxy() -> int:
    r = rng(40)
    header = ["week_start", "department", "host", "category", "action", "requests", "upload_kb"]
    rows = []
    wk = date(2027, 4, 4)
    while wk <= date(2027, 5, 30):
        for dept, host, cat, act, req, up in HOSTS:
            g = 1.0 + (0.04 * ((wk - date(2027, 4, 4)).days // 7) if host == "api.promptway.ai" else 0)
            q = round(req * g * r.uniform(0.85, 1.15))
            rows.append([wk.isoformat(), dept, host, cat, act, q, round(up * g * r.uniform(0.85, 1.15)) if up else 0])
        wk += timedelta(days=7)
    return write_csv("it/proxy-ai-hosts-2027-q2.csv", header, rows)


T = []  # (opened, system, category, priority, summary, status, closed, assignee, linked)


def t(opened, system, cat, prio, summary, status, closed, who, link=""):
    T.append([opened, system, cat, prio, summary, status, closed, who, link])


def tickets() -> int:
    T.clear()
    r = rng(41)
    wk = MABAT_FEED_BROKEN
    while wk <= date(2027, 6, 3):
        end = wk + timedelta(days=6)
        t(wk.isoformat(), "Mabat Fleet > Tzir Route", "integration", "P4",
          "Nightly telematics export to Tzir failed 7/7 nights: HTTP 401 Unauthorized (auto-digest)",
          "closed - duplicate", end.isoformat(), "auto")
        wk += timedelta(days=7)
    t("2026-11-13", "Mabat Fleet", "change", "P3", "Rotate Mabat API credentials (annual security policy)",
      "closed", "2026-11-13", "D. Volkov")
    t("2026-11-22", "Tzir Route", "request", "P3", "Retraining data: confirm telematics feed to vendor", "closed",
      "2026-11-24", "I. Barkan", "")
    for d, txt in (("2027-01-17", "מסלול בדרום עובר בכביש סגור – הנהג חזר"), ("2027-01-26", "Route plan uses road closed by army order near Netivot"),
                   ("2027-02-03", "אפליקציית נהג: מסלול דרך אזור סגור, נהג סירב"), ("2027-02-11", "South: plans ignore delivery windows, 9 late"),
                   ("2027-02-19", "Driver app crashes on old phones (South)"), ("2027-01-31", "KSH routes via Rt 899 – closed")):
        t(d, "Tzir Route", "incident - minor", "P3", txt, "closed - workaround (dispatcher override)", d, "Tzir support")
    t("2027-02-23", "Tzir Route", "data request", "P3",
      "Export of driver score history for driver #4471 (requested by deputy ops manager South, for hearing 24/2)",
      "done", "2027-02-24", "BI team")
    t("2027-02-25", "Tzir Route", "change", "P2", "South region: stop sending plans to driver app (R. Haj-Yahia)",
      "done", "2027-02-25", "Tzir support")
    t("2027-03-14", "Tzir Route", "change", "P3", "Centre: planner view only, no driver dispatch (G. Rosen)",
      "done", "2027-03-14", "Tzir support")
    t("2027-02-08", "Tzir Route", "request", "P4", "Europe connector to Rotterdam TMS - status?", "open", "", "I. Barkan")
    for d, txt in (("2027-01-21", "Ayin Drive false fatigue alerts at night"), ("2027-02-07", "Ayin camera offline x6 cabs"),
                   ("2027-02-16", "Drivers covering Ayin cameras with tape")):
        t(d, "Ayin Drive", "incident - minor", "P3", txt, "closed", d, "M. Azulay")
    t("2027-03-08", "Ayin Drive", "change", "P2", "Pause Ayin Drive pending works committee (COO)", "done", "2027-03-08", "D. Volkov")
    t("2027-03-01", "Nezek Vision", "request", "P4", "POC ended 28/2 - disable vendor accounts and stop billing?", "open", "", "I. Barkan")
    t("2027-03-09", "Meches Pro", "change", "P3",
      "Release 9.3 installed. Release notes: 'HS Suggest (AI) enabled by default'. No action.", "closed", "2027-03-09", "IT apps")
    t("2027-03-15", "Kotev Assist", "query", "P4", "Finance: 450 seats billed, how many used?", "closed - answered", "2027-03-20", "IT apps")
    for d, txt in (("2027-03-22", "Tzir Assist gave customer a wrong ETA (vessel delayed)"), ("2027-03-29", "Assistant answered in Hebrew to a Russian question"),
                   ("2027-04-12", "Assistant promised delivery 'tomorrow' - customs not released"), ("2027-04-27", "Assistant quoted storage fee from old tariff")):
        t(d, "Tzir Assist", "incident - minor", "P3", txt, "closed", d, "Tzir support")
    t("2027-04-20", "Tzir Assist", "change", "P3", "Enable 'my documents' feature (file attachments) for all customers", "done", "2027-04-20", "Tzir support")
    t("2027-05-02", "Tzir Docs", "change", "P4", "Vendor maintenance window: platform release 4.2 (notice received same day)", "closed", "2027-05-02", "auto")
    t("2027-05-06", "Tzir Docs", "incident - minor", "P3", "Prefill shows another importer's name on invoice (Ashdod)",
      "closed - data quality (supplier invoice no. duplicated)", "2027-05-07", "Tzir support")
    t("2027-05-11", "Tzir Docs", "incident - minor", "P3", "Pre-fill attached wrong packing list (LCL, Haifa)",
      "closed - data quality", "2027-05-12", "Tzir support")
    inc = "INC-27-0518-01"
    t("2027-05-18", "Tzir Docs / Tzir Assist", "incident - major", "P1",
      "Customer (C1007) sees another importer's invoice in portal; customs query on value", "contained", "2027-05-22",
      "D. Volkov", inc)
    t("2027-05-19", "Tzir Assist", "change", "P1", "Disable 'my documents' feature in Tzir Assist", "done", "2027-05-19", "D. Volkov", inc)
    t("2027-05-21", "Tzir Docs", "change", "P1", "Vendor hotfix 4.2.1 deployed (invoice key normaliser)", "done", "2027-05-21", "Tzir support", inc)
    t("2027-05-24", "Tzir Docs", "incident - minor", "P3", "Agent reports prefill from another customer's invoice (numeric invoice no.)",
      "closed - known issue fixed in 4.2.1", "2027-05-25", "Tzir support", inc)
    t("2027-05-30", "Tzir Docs", "incident - minor", "P3", "Mismatch again, Haifa, LCL", "open", "", "Tzir support", "")
    t("2027-05-27", "AI programme", "request", "P3", "Remove I. Barkan access; reassign owner of AI systems", "open", "", "IT apps")
    noise = [("Kotev Assist", "request", "Access request"), ("Kotev Assist", "request", "Licence for new employee"),
             ("Tzir Route", "request", "Add new driver to app (North)"), ("Tzir Route", "request", "Reset driver PIN"),
             ("Tzir Docs", "request", "New agent user (Ashdod)"), ("Mishkal ERP", "incident - minor", "Smart Match suggests wrong PO"),
             ("Tzir Assist", "request", "Customer cannot log in to portal")]
    d = date(2026, 10, 4)
    while d <= date(2027, 6, 2):
        if r.random() < 0.38:
            s, c, txt = r.choice(noise)
            t(d.isoformat(), s, c, "P4", txt, "closed", (d + timedelta(days=r.randint(0, 3))).isoformat(), "IT service desk")
        d += timedelta(days=1)
    T.sort(key=lambda x: x[0])
    rows = [[f"IT-{26000 + i * 3}"] + x for i, x in enumerate(T)]
    header = ["ticket_id", "opened", "system", "category", "priority", "summary", "status", "closed", "assignee",
              "linked_incident"]
    return write_csv("incident/it-tickets-ai.csv", header, rows)


def build() -> dict:
    return {"proxy": proxy(), "tickets": tickets()}
