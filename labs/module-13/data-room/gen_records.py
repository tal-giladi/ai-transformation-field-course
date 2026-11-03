"""Assets, moulds, parts, the statutory examination register and quality's weekly scrap.

Reading this spoils the engagement: finish module 13 first.
"""
from __future__ import annotations

from datetime import date, datetime, timedelta

from gen_common import ROOM, machines, rng, write_csv

PART_FAMILIES = {  # cause -> (prefix, Hebrew description, how many numbers)
    "HYD_PUMP": ("HP-BRG", "ערכת מיסבים משאבה", 8), "HYD_VALVE": ("HV-COIL", "סליל שסתום", 10),
    "HYD_LEAK": ("HH", "צינור לחץ גבוה", 24), "OIL_TEMP": ("WV", "ברז מים מחליף חום", 5),
    "HEATER": ("HB", "גוף חימום צילינדר", 26), "TC": ("TCJ", "תרמוקפל J", 9),
    "CONTACTOR": ("CT", "מגען", 12), "DRIVE": ("DRV-FAN", "מאוורר דרייבר", 6),
    "CHECK_RING": ("CR-SET", "סט טבעת חוזרת", 14), "CLAMP": ("TG-PIN", "פין טוגל", 8),
    "EJECTOR": ("EJ-SEN", "חיישן מפלט", 5), "GATE": ("SG-SW", "מתג בטיחות דלת", 6),
    "ROBOT": ("RB-VAC", "כוס וואקום", 10),
}
OTHER_FAMILIES = [("FLT-HYD", "פילטר שמן הידראולי", 6), ("FLT-AIR", "פילטר אוויר", 6), ("OR", "או-רינג", 40),
                  ("BRG", "מיסב", 20), ("FUSE", "נתיך", 15), ("LMP", "נורת סימון", 8), ("SNS-PRX", "חיישן קרבה", 12),
                  ("DRY-HTR", "גוף חימום רגנרציה מייבש", 4), ("DRY-FLT", "פילטר מייבש", 6), ("TC-HR", "תרמוקפל הוט ראנר", 8)]
REPLICA_DATE = date(2025, 3, 16)


def parts() -> tuple[list[dict], dict]:
    """The live ERP catalogue and, per cause, the part numbers a technician would take from the replica."""
    r = rng(6)
    catalogue = []
    fams = [(p, d, n, c) for c, (p, d, n) in PART_FAMILIES.items()] + [(p, d, n, "") for p, d, n in OTHER_FAMILIES]
    for prefix, desc, n, cause in fams:
        for i in range(1, n + 1):
            pn = f"{prefix}-{10 + i * 3:03d}"
            catalogue.append({"pn": pn, "desc": f"{desc} {i}", "cause": cause, "plant": "K",
                              "old_bin": f"{r.choice('ABCDE')}-{r.randint(1, 24)}-{r.randint(1, 5)}",
                              "bin": f"K1-{r.choice('ABCDEFG')}{r.randint(1, 30):02d}-{r.randint(1, 6):02d}",
                              "qty": r.randint(0, 14), "old_qty": r.randint(0, 14), "superseded": None,
                              "unit": "יח'", "price": r.choice([45, 80, 120, 260, 480, 950, 2400, 6800])})
    for p in catalogue:  # 2025-26 supersessions: the replica keeps the old number
        if r.random() < 0.19:
            p["superseded"] = p["pn"] + "B"
    for p in catalogue:  # the bin the WhatsApp group could not find
        if p["pn"] == "HV-COIL-028":
            p.update(old_bin="B-7-2", bin="K1-D14-02", superseded=None)
    g_parts = []
    for prefix, desc, n in [("G-MOR-HB", "גוף חימום מורנדי", 14), ("G-MOR-SEAL", "ערכת אטמים מורנדי", 10),
                            ("G-MOR-VLV", "שסתום מורנדי", 8), ("G-HW-TC", "תרמוקפל הייוויי", 6)]:
        for i in range(1, n + 1):
            g_parts.append({"pn": f"{prefix}-{i:02d}", "desc": f"{desc} {i}", "cause": "", "plant": "G",
                            "bin": f"G1-{r.choice('ABC')}{r.randint(1, 12):02d}", "qty": r.randint(0, 8),
                            "superseded": None, "unit": "יח'", "price": r.choice([120, 260, 480, 950])})
    by_cause = {}
    for p in catalogue:
        if p["cause"]:
            by_cause.setdefault(p["cause"], []).append(p["pn"])
    return catalogue + g_parts, by_cause


def write_parts(catalogue: list[dict]) -> dict:
    r = rng(7)
    erp, replica = [], []
    for p in catalogue:
        if p["superseded"]:
            erp.append([p["pn"], p["desc"], "superseded", p["superseded"], "", "", 0, 0, p["unit"], p["price"]])
            erp.append([p["superseded"], p["desc"] + " (חדש)", "active", "", p["bin"] if p["plant"] == "K" else "",
                        "", p["qty"] if p["plant"] == "K" else 0, 0, p["unit"], int(p["price"] * 1.08)])
        else:
            erp.append([p["pn"], p["desc"], "active", "", p["bin"] if p["plant"] == "K" else "",
                        p["bin"] if p["plant"] == "G" else "", p["qty"] if p["plant"] == "K" else 0,
                        p["qty"] if p["plant"] == "G" else 0, p["unit"], p["price"]])
        if p["plant"] == "K":
            replica.append([p["pn"], p["desc"], p["old_bin"], p["old_qty"], p["unit"],
                            r.choice(["", "", "", "להזמין", "חלופי בארון ולדי"])])
    erp.sort(key=lambda x: x[0])
    replica.sort(key=lambda x: x[0])
    n1 = write_csv(ROOM / "parts" / "erp-parts-2026-12-31.csv",
                   ["part_number", "description", "status", "superseded_by", "bin_plant_k", "bin_plant_g",
                    "on_hand_k", "on_hand_g", "uom", "std_cost_ils"], erp)
    n2 = write_csv(ROOM / "parts" / "parts-list-shared-drive.csv",
                   ["מק\"ט", "תיאור", "מיקום", "כמות", "יחידה", "הערות"], replica)
    sup = sum(1 for p in catalogue if p["plant"] == "K" and p["superseded"])
    return {"erp_rows": n1, "replica_rows": n2, "replica_superseded": sup}


def write_assets() -> dict:
    r = rng(8)
    ms = machines()
    rows = []
    with_mes = {"K01", "K02", "K03", "K09", "K10", "K21", "K22", "K23", "K15"}
    for m in [x for x in ms if x["plant"] == "K"]:
        rows.append([m["cmms"], f"מכונת הזרקה {m['maker']} {m['model']}", "IMM", m["maker"], m["model"],
                     m["serial"], m["year"], m["tonnage"],
                     f"אולם {'A' if m['hall'] <= 13 else 'B'} / {m['hall']}", m["mes"] if m["mes"] in with_mes else "",
                     "כן" if m["cm"] else "", "", "פעיל"])
    aux = [("KN-DR-%02d" % i, "מייבש DryMax DM-150", "DRYER", "DryMax", "DM-150", 2012 + i) for i in range(1, 7)]
    aux += [("KN-CH-%02d" % i, "צ'ילר ArcticFlow AC-40", "CHILLER", "ArcticFlow", "AC-40", 2015 + i) for i in range(1, 4)]
    aux += [("KN-CP-%02d" % i, "מדחס + מכל אוויר 2000 ל'", "COMPRESSOR", "AirTec", "AT-55", 2011 + 5 * i) for i in range(1, 3)]
    aux += [("KN-CR-%02d" % i, "עגורן גשר 10 טון", "CRANE", "Galil Cranes", "GB-10", 2009 + i) for i in range(1, 3)]
    aux += [("KN-RB-%02d" % i, "רובוט שליפה", "ROBOT", "Pickfast", "PF-3", 2016 + i % 6) for i in range(1, 15)]
    for a in aux:
        rows.append([a[0], a[1], a[2], a[3], a[4], "", a[5], "", "", "", "", "", "פעיל"])
    n1 = write_csv(ROOM / "assets" / "asset-register-plant-k.csv",
                   ["asset_id", "description", "class", "maker", "model", "serial", "year", "tonnage",
                    "location", "mes_code", "condition_monitoring", "criticality", "status"], rows)
    g_rows = []
    gm = sorted([x for x in ms if x["plant"] == "G"], key=lambda x: x["hall"])
    for m in gm:
        g_rows.append([m["hall"], m["maker"], m["model"].split()[0], m["year"], m["tonnage"], m["serial"],
                       r.choice(["", "", "מצבר שוחזר 2022", "בורג הוחלף 2021", ""])])
    for name, note in (("עגורן 1", "עגורן גשר 8 טון, אולם 1"), ("עגורן 2", "עגורן גשר 8 טון, אולם 2 - החלפות תבניות"),
                       ("מדחס 1", "מכל 1500 ל'"), ("צ'ילר 1", ""), ("מייבש 1-4", "")):
        g_rows.append([name, "", "", "", "", "", note])
    n2 = write_csv(ROOM / "assets" / "asset-list-plant-g.csv",
                   ["מס' מכונה", "יצרן", "דגם", "שנה", "טונאז'", "מס' סידורי", "הערות"], g_rows)
    mes_rows = [[m["plant"], m["mes"], f"{m['maker']} {m['model']}" + (f" #{m['mes'][1:]}" if m["plant"] == "G" else ""),
                 m["tonnage"], m["serial"], "2025-03-02" if m["plant"] == "K" else "2025-06-15"] for m in ms]
    n3 = write_csv(ROOM / "assets" / "mes-machines.csv",
                   ["plant", "machine", "description", "tonnage", "serial", "in_prodtrack_since"], mes_rows)
    moulds = []
    customers = [("Arava Home Appliances", 0.3), ("Galil Dairies", 0.2), ("Yarden Beverages", 0.25),
                 ("Kinneret own crates", 0.1), ("Other", 0.15)]
    ks = [m["mes"] for m in ms]
    for i in range(1, 232):
        cust = r.choices([c for c, _ in customers], [w for _, w in customers])[0]
        plant = "G" if i % 3 == 0 else "K"
        hot = "Y" if cust in ("Galil Dairies", "Yarden Beverages") or r.random() < 0.35 else "N"
        counter = r.choice(["", "", "", "ידני", str(r.randint(200, 4000) * 1000)])
        last = "" if r.random() < 0.62 else (date(2025, 1, 1) + timedelta(days=r.randint(0, 720))).isoformat()
        on = r.choice(ks) if r.random() < 0.17 else ""
        moulds.append([f"TM-{1000 + i}", plant, cust, f"part-{r.randint(100, 999)}", r.choice([1, 2, 4, 8, 16, 32, 48]),
                       hot, on, counter, last])
    n4 = write_csv(ROOM / "assets" / "mould-list.csv",
                   ["mould_id", "plant", "customer", "part", "cavities", "hot_runner", "on_machine",
                    "shot_counter", "last_service"], moulds)
    return {"assets_k": n1, "assets_g": n2, "mes_machines": n3, "moulds": n4}


def write_exam_register() -> dict:
    rows = [
        ["KN-CR-01", "K", "עגורן גשר 10 ט'", "פקודת הבטיחות בעבודה ס' 81 (מכונת הרמה)", "14", "2026-04-14", "י. ברק, בודק מוסמך", "T-2026-118", "2027-06-14", "בתוקף"],
        ["KN-CR-02", "K", "עגורן גשר 10 ט'", "פקודת הבטיחות בעבודה ס' 81 (מכונת הרמה)", "14", "2026-04-14", "י. ברק, בודק מוסמך", "T-2026-119", "2027-06-14", "בתוקף"],
        ["KN-CP-01", "K", "מכל אוויר 2000 ל'", "פקודת הבטיחות בעבודה ס' 115 (קולט אוויר)", "26", "2026-02-09", "א. סלים, בודק דוודים מוסמך", "P-2026-031", "2028-04-09", "בתוקף"],
        ["KN-CP-02", "K", "מכל אוויר 2000 ל'", "פקודת הבטיחות בעבודה ס' 115 (קולט אוויר)", "26", "2026-02-09", "א. סלים, בודק דוודים מוסמך", "P-2026-032", "2028-04-09", "בתוקף"],
        ["KN-FL-01", "K", "מלגזה 3 ט'", "פקודת הבטיחות בעבודה ס' 81 (מכונת הרמה)", "14", "2026-01-20", "י. ברק, בודק מוסמך", "T-2026-012", "2027-03-20", "בתוקף"],
        ["KN-FL-02", "K", "מלגזה 3 ט'", "פקודת הבטיחות בעבודה ס' 81 (מכונת הרמה)", "14", "2026-01-20", "י. ברק, בודק מוסמך", "T-2026-013", "2027-03-20", "בתוקף"],
        ["עגורן 1", "G", "עגורן גשר 8 ט'", "פקודת הבטיחות בעבודה ס' 81", "14", "2026-09-07", "ר. חורי, בודק מוסמך", "GL-2026-44", "2027-11-07", "בתוקף"],
        ["עגורן 2", "G", "עגורן גשר 8 ט' (החלפות תבניות)", "פקודת הבטיחות בעבודה ס' 81", "14", "2025-08-11", "ר. חורי, בודק מוסמך", "GL-2025-37", "2026-10-11", "בתוקף"],
        ["מדחס 1", "G", "מכל אוויר 1500 ל'", "פקודת הבטיחות בעבודה ס' 115", "26", "2025-05-19", "ר. חורי, בודק דוודים מוסמך", "GL-2025-21", "2027-07-19", "בתוקף"],
        ["מלגזה G1", "G", "מלגזה 2.5 ט'", "פקודת הבטיחות בעבודה ס' 81", "14", "2026-03-02", "ר. חורי, בודק מוסמך", "GL-2026-09", "2027-05-02", "בתוקף"],
    ]
    n = write_csv(ROOM / "safety" / "periodic-examinations-register.csv",
                  ["item", "plant", "description", "basis", "interval_months", "last_examination",
                   "examiner", "report_ref", "next_due", "status"], rows)
    return {"exam_rows": n}


def write_scrap(events: list[dict]) -> dict:
    """Quality's weekly scrap per machine (Arava requires defect codes): drift shows before some stops."""
    r = rng(9)
    rows = []
    week1 = date(2025, 12, 29)  # ISO week 1 of 2026 starts Monday 29 December 2025
    by_machine = {}
    for e in events:
        by_machine.setdefault(e["mes"], []).append(e)
    for m in machines():
        evs = by_machine.get(m["mes"], [])
        for w in range(52):
            ws = week1 + timedelta(days=7 * w)
            we = ws + timedelta(days=7)
            produced = int(r.gauss(42000 if m["tonnage"] < 300 else 18000, 3000))
            base = r.uniform(0.008, 0.016)
            short = int(produced * base * 0.3)
            flash = int(produced * base * 0.25)
            splay = int(produced * base * 0.1)
            for e in evs:
                d = e["start"].date()
                lead = (d - ws).days
                if e["cause"] in ("CHECK_RING", "HYD_VALVE", "HYD_PUMP", "HEATER") and 0 <= lead < 14:
                    short += int(produced * r.uniform(0.006, 0.02))
                if e["cause"] in ("HR_HEATER", "HR_TC") and 0 <= lead < 10:
                    short += int(produced * r.uniform(0.004, 0.012))
                if e["cause"] in ("MOULD_DAMAGE", "CLAMP") and 0 <= lead < 10:
                    flash += int(produced * r.uniform(0.005, 0.015))
                if e["cause"] in ("DRYER", "WET_MAT") and ws <= d < we:
                    splay += int(produced * r.uniform(0.004, 0.01))
            burn = int(produced * base * 0.08)
            cont = int(produced * base * 0.12)
            dim = int(produced * base * 0.1)
            other = int(produced * base * 0.05)
            coded = short + flash + splay + burn + cont + dim + other
            uncoded = int(coded * r.uniform(0.0, 0.04))
            rows.append([m["plant"], m["mes"], f"2026-W{w + 1:02d}", ws.isoformat(), produced, coded + uncoded,
                         short, flash, splay, burn, cont, dim, other, uncoded])
    n = write_csv(ROOM / "production" / "scrap-weekly-2026.csv",
                  ["plant", "machine", "iso_week", "week_start", "parts_produced", "scrap_total", "short_shot",
                   "flash", "splay", "burn", "contamination", "dimensional", "other", "uncoded"], rows)
    return {"scrap_rows": n}
