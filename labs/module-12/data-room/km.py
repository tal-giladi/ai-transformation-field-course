"""The precedent bank index (Mikbatz): 1,180 entries, the 78 corpus documents among them."""
from __future__ import annotations

from datetime import date, timedelta

from common import ROOM, rng, write_csv
from corpus import Doc

SUBJECTS = {
    "Corporate": [("Share purchase agreement — buyer form", "SPA"), ("Shareholders' agreement — minority protections", "SHA"),
                  ("Term sheet — Series A", "VC"), ("Board resolutions pack", "governance"), ("NDA — mutual", "NDA"),
                  ("הסכם מייסדים", "founders"), ("כתב שיפוי לדירקטורים", "D&O"), ("Disclosure schedule checklist", "SPA")],
    "Litigation": [("כתב תביעה - הפרת חוזה", "pleading"), ("בקשה לסעד זמני", "injunction"), ("Expert instruction letter", "evidence"),
                   ("סיכומים - פיצוי מוסכם", "damages"), ("מכתב התראה לפני תביעה", "demand"), ("Settlement agreement", "settlement")],
    "Real estate": [("הסכם שכירות מסחרי - נוסח משכיר", "lease"), ("Construction contract — developer form", "construction"),
                    ("הסכם קומבינציה", "combination"), ("Due diligence checklist — land", "DD")],
    "Banking & finance": [("Facility agreement — senior secured", "facility"), ("שטר משכון", "security"),
                          ("Intercreditor term sheet", "intercreditor"), ("ערבות אישית - נוסח בנק", "guarantee")],
    "Tech & IP": [("SaaS agreement — customer form", "SaaS"), ("Data-processing agreement", "privacy"),
                  ("מדיניות פרטיות לאתר", "privacy"), ("Software licence — enterprise", "licence"),
                  ("IP assignment — employee", "IP"), ("Privacy notice — app", "privacy"), ("Cookie policy", "privacy")],
    "Employment": [("הסכם העסקה - עובד בכיר", "employment"), ("Non-compete and non-solicitation letter", "restrictive"),
                   ("מכתב שימוע", "hearing"), ("נוהל הגנת פרטיות עובדים", "privacy"), ("Employee monitoring policy", "privacy")],
}
TYPES = ["precedent", "template", "memo", "checklist", "ruling copy"]


def build_km(docs: list[Doc]) -> list[list]:
    r = rng("km")
    rows = []
    stale_marked = {d.id for d in docs if d.superseded_by and d.kind == "ruling"}
    marked_ok = sorted(stale_marked)[:2]                     # only two of the stale documents were ever marked
    for d in sorted(docs, key=lambda x: x.id):
        status = "superseded" if d.id in marked_ok else "current"
        reviewed = "" if r.random() < 0.6 else (d.date + timedelta(days=r.randint(30, 400))).isoformat()
        if reviewed and reviewed > "2026-10-30":
            reviewed = ""
        rows.append([d.id, d.title, {"ruling": "ruling copy", "memo": "memo", "clause note": "precedent"}[d.kind],
                     d.group or "Litigation", d.author or "", d.date.isoformat(), reviewed, status,
                     d.superseded_by if status == "superseded" else "", f"research;{d.topic}",
                     r.randint(0, 25), "yes"])
    groups = list(SUBJECTS)
    weights = [32, 22, 12, 10, 14, 10]
    n = 0
    while len(rows) < 1180:
        n += 1
        g = r.choices(groups, weights)[0]
        subj, tag = r.choice(SUBJECTS[g])
        up = date(2014, 1, 1) + timedelta(days=int(r.betavariate(2.2, 1.3) * 4680))
        if up > date(2026, 10, 25):
            up = date(2026, 10, 25) - timedelta(days=r.randint(0, 300))
        kind = r.choices(TYPES, [45, 25, 15, 10, 5])[0]
        if tag == "privacy":
            reviewed = "" if r.random() < 0.8 else (up + timedelta(days=r.randint(30, 300))).isoformat()
        else:
            reviewed = "" if r.random() < 0.62 else (up + timedelta(days=r.randint(30, 1500))).isoformat()
        if reviewed and reviewed > "2026-10-30":
            reviewed = ""
        status = r.choices(["current", "superseded", "draft"], [88, 7, 5])[0]
        uses = int(r.paretovariate(1.25) * 1.6) - 1
        if up.year < 2018:
            uses = int(uses * 0.4)
        title = f"{subj} (v{up.year % 100:02d}.{r.randint(1, 9)})"
        rows.append([f"MKB-{10000 + n * 7 + r.randint(0, 6)}", title, kind, g, "", up.isoformat(), reviewed, status,
                     "", tag, max(0, min(uses, 260)), "no"])
    return rows


def write_km(rows) -> None:
    write_csv(ROOM / "km" / "precedent-bank-index.csv",
              ["doc_id", "title", "doc_type", "practice_group", "author", "uploaded_date", "last_reviewed_date",
               "status", "superseded_by", "tags", "uses_last_12m", "in_research_export"], rows)
