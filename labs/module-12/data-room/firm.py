"""People, matters, clients, the Carmel NDA workstream and the renewals log."""
from __future__ import annotations

from datetime import date

import textbank as tb
from common import ROOM, r10, rng, write_csv

GROUPS = ["Corporate", "Litigation", "Real estate", "Banking & finance", "Tech & IP", "Employment"]

PARTNERS = [  # id, name, role, group, desk, year admitted, languages
    ("L001", "Yoav Dagan", "equity_partner", "Corporate", "", 1995, "he,en"),
    ("L002", "Shmuel Atlas", "equity_partner", "Litigation", "", 1984, "he,en"),
    ("L003", "Noa Friedman", "equity_partner", "Tech & IP", "", 2007, "he,en"),
    ("L004", "Orit Levinson", "equity_partner", "Employment", "", 1998, "he,en,fr"),
    ("L005", "David Kessler", "equity_partner", "Corporate", "International", 1999, "en,he"),
    ("L006", "Leah Weinberg", "equity_partner", "Corporate", "International", 2003, "en,he"),
    ("L007", "Gadi Ohana", "equity_partner", "Corporate", "", 2005, "he,en"),
    ("L008", "Rachel Adler", "salaried_partner", "Corporate", "International", 2011, "en,he"),
    ("L009", "Tal Segal", "salaried_partner", "Corporate", "", 2012, "he,en"),
    ("L010", "Avi Mor", "equity_partner", "Litigation", "", 2000, "he,en"),
    ("L011", "Ronit Bar-Lev", "equity_partner", "Litigation", "", 2004, "he,en"),
    ("L012", "Samer Khatib", "salaried_partner", "Litigation", "", 2010, "ar,he,en"),
    ("L013", "Inbal Harel", "salaried_partner", "Litigation", "", 2012, "he,en"),
    ("L014", "Elad Peretz", "salaried_partner", "Litigation", "", 2013, "he,en"),
    ("L015", "Michal Ben-Ami", "salaried_partner", "Tech & IP", "", 2012, "he,en"),
    ("L016", "Jonathan Green", "salaried_partner", "Tech & IP", "", 2013, "en,he"),
    ("L017", "Moshe Azoulay", "equity_partner", "Real estate", "", 1997, "he,en,fr"),
    ("L018", "Hani Mansour", "equity_partner", "Real estate", "", 2002, "ar,he,en"),
    ("L019", "Keren Shapira", "equity_partner", "Real estate", "", 2006, "he,en"),
    ("L020", "Dmitri Volkov", "salaried_partner", "Real estate", "", 2011, "ru,he,en"),
    ("L021", "Elena Sokolova", "equity_partner", "Banking & finance", "", 2001, "ru,he,en"),
    ("L022", "Uri Peleg", "equity_partner", "Banking & finance", "", 2003, "he,en"),
    ("L023", "Nizar Hamdan", "salaried_partner", "Banking & finance", "", 2012, "ar,he,en"),
    ("L024", "Fadi Haddad", "equity_partner", "Employment", "", 2004, "ar,he,en"),
    ("L025", "Sharon Levi", "equity_partner", "Employment", "", 2006, "he,en"),
    ("L026", "Polina Gurevich", "salaried_partner", "Employment", "", 2014, "ru,he,en"),
]
ASSOC_GROUPS = (["Corporate"] * 16 + ["Litigation"] * 15 + ["Tech & IP"] * 7 + ["Real estate"] * 9
                + ["Banking & finance"] * 8 + ["Employment"] * 9)
FIXED_ASSOC = {"L041": ("Karim Nassar", "Litigation", "", 2019, "ar,he,en"),
               "L063": ("Yana Petrenko", "Corporate", "International", 2024, "ru,he,en")}
GROUP_REV_2025 = {"Corporate": 46.0e6, "Litigation": 34.0e6, "Real estate": 22.0e6,
                  "Banking & finance": 18.0e6, "Tech & IP": 14.0e6, "Employment": 18.4e6}
GROUP_2026_FACTOR = {"Corporate": 0.75, "Litigation": 0.70, "Real estate": 0.74,
                     "Banking & finance": 0.75, "Tech & IP": 0.78, "Employment": 0.75}
TYPE_SHARE = {"Corporate": (0.55, 0.20, 0.15, 0.10), "Litigation": (0.72, 0.20, 0.05, 0.03),
              "Real estate": (0.35, 0.15, 0.40, 0.10), "Banking & finance": (0.65, 0.20, 0.05, 0.10),
              "Tech & IP": (0.20, 0.05, 0.66, 0.09), "Employment": (0.40, 0.05, 0.10, 0.45)}
TYPES = ("hourly", "capped", "fixed", "retainer")
MATTER_COUNT = {"Corporate": 150, "Litigation": 130, "Real estate": 80, "Banking & finance": 60,
                "Tech & IP": 70, "Employment": 70}
SECTORS = ["retail", "insurance", "banking", "technology", "real estate", "manufacturing", "health",
           "energy", "food", "logistics", "investment fund", "telecom", "public company", "family office"]


def build_lawyers() -> list[dict]:
    r = rng("lawyers")
    out = []
    for lid, name, role, group, desk, year, langs in PARTNERS:
        target = 700 if lid == "L001" else 1000 if lid == "L004" else 1400 if role == "equity_partner" else 1600
        base = {"L001": 610, "L004": 880}.get(lid, r.gauss(target * 0.92, 90))
        rate = r10(r.uniform(1900, 2400) if role == "equity_partner" else r.uniform(1450, 1750))
        out.append(dict(id=lid, name=name, role=role, group=group, desk=desk, year=year, langs=langs,
                        target=target, h2025=round(base), rate=rate))
    groups = ASSOC_GROUPS[:]
    r.shuffle(groups)
    forced = {"L041": "Litigation", "L063": "Corporate", "L058": "Corporate"}
    locked = [int(x[1:]) - 27 for x in forced]
    for fixed_id, want in forced.items():
        i = int(fixed_id[1:]) - 27
        if groups[i] != want:
            j = next(k for k, g in enumerate(groups) if g == want and k not in locked)
            groups[i], groups[j] = groups[j], groups[i]
    used = {p[1] for p in PARTNERS}
    origins = ["he"] * 60 + ["ar"] * 15 + ["ru"] * 15 + ["am"] * 4 + ["en"] * 6
    intl_left = 5
    for k in range(64):
        lid = f"L{27 + k:03d}"
        if lid in FIXED_ASSOC:
            name, group, desk, year, langs = FIXED_ASSOC[lid]
        else:
            group = groups[k]
            while True:
                o = r.choice(origins)
                name = f"{r.choice(tb.FIRST[o])} {r.choice(tb.LAST[o])}"
                if name not in used:
                    break
            langs = ",".join(dict.fromkeys([o if o != "en" else "en", "he", "en"]))
            desk = ""
            if group == "Corporate" and lid != "L058" and intl_left > 0 and r.random() < 0.45:
                desk, intl_left = "International", intl_left - 1
            year = r.choice(range(2016, 2026))
        used.add(name)
        rate = min(1250, 650 + 70 * (2026 - year))
        h = r.gauss(1540, 130)
        out.append(dict(id=lid, name=name, role="associate", group=group, desk=desk, year=year, langs=langs,
                        target=1850, h2025=round(h), rate=r10(rate)))
    # make sure the International desk has six associates
    intl = [l for l in out if l["role"] == "associate" and l["desk"] == "International"]
    for l in out:
        if len(intl) >= 6:
            break
        if l["role"] == "associate" and l["group"] == "Corporate" and not l["desk"] and l["id"] != "L058":
            l["desk"] = "International"
            intl.append(l)
    return out


def build_clients() -> list[dict]:
    r = rng("clients")
    out = []
    for i in range(1, 161):
        code = f"C-{i:03d}"
        out.append(dict(code=code, name="Carmel Retail Group Ltd" if code == "C-014" else f"[client {code}]",
                        sector="retail" if code == "C-014" else "insurance" if code in ("C-007", "C-031") else
                        "banking" if code == "C-003" else "investment fund" if code == "C-022" else r.choice(SECTORS),
                        since=r.choice(range(1996, 2026)) if code != "C-014" else 2009,
                        weight=(1 / (i ** 0.7)) * r.uniform(0.6, 1.4)))
    return out


def build_nda() -> list[dict]:
    """Carmel NDA workstream, Jan 2024 - Oct 2026: automation from mid-2025, fixed price from Jan 2026."""
    r = rng("nda")
    rows = []
    ramp_t = {3: 2.2, 4: 1.6, 5: 1.2, 6: 1.0}
    ramp_h = {3: 1.8, 4: 1.4, 5: 1.1, 6: 1.0}
    for y in (2024, 2025, 2026):
        for m in range(1, 13):
            if y == 2026 and m > 10:
                break
            n = max(20, round(r.gauss({2024: 38, 2025: 42, 2026: 46}[y], 4)))
            if y == 2024 or (y == 2025 and m <= 2):
                t, h = r.gauss(3.1, 0.25), r.gauss(2.4, 0.12)
            elif y == 2025 and m in ramp_t:
                t, h = ramp_t[m] + r.gauss(0, 0.1), ramp_h[m] + r.gauss(0, 0.05)
            else:
                t, h = r.gauss(0.8, 0.08), r.gauss(0.85 if y == 2025 else 0.8, 0.05)
            hours = round(n * h, 1)
            rate = {2024: 860, 2025: 890, 2026: 920}[y]
            if y == 2026:
                basis, fees = "fixed ₪1,150 per NDA", n * 1150
            else:
                basis, fees = f"hourly (blended ₪{rate})", r10(hours * rate)
            rows.append(dict(month=f"{y}-{m:02d}", n=n, t=round(t, 1), hours=hours, basis=basis, fees=fees,
                             per=round(fees / n), eff=round(fees / hours)))
    return rows


def build_matters(lawyers, clients, nda) -> list[dict]:
    r = rng("matters")
    partners = {g: [l["id"] for l in lawyers if l["group"] == g and l["role"] != "associate"] for g in GROUPS}
    weights = [c["weight"] for c in clients]
    codes = [c["code"] for c in clients]
    matters, seq = [], 100
    carmel_plan = ["Corporate"] * 6 + ["Employment"] * 3 + ["Litigation"] * 2 + ["Real estate"] * 2
    ofek_plan = ["Litigation"] * 6
    for g in GROUPS:
        for i in range(MATTER_COUNT[g]):
            seq += 1
            client = r.choices(codes, weights)[0]
            while client in ("C-014", "C-031"):
                client = r.choices(codes, weights)[0]
            opened = r.choices([2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026], [2, 3, 4, 6, 9, 14, 20, 12])[0]
            closed_2025 = opened <= 2025 and r.random() < 0.3
            mtype = r.choices(TYPES, TYPE_SHARE[g])[0]
            matters.append(dict(id=f"M-{opened}-{seq:04d}", client=client, group=g,
                                desk="International" if g == "Corporate" and r.random() < 0.3 else "",
                                partner=r.choice(partners[g]), type=mtype, opened=opened,
                                has25=opened <= 2025, has26=not closed_2025,
                                w25=r.lognormvariate(0, 0.9), w26=r.lognormvariate(0, 0.9)))
    # Carmel and the lost Ofek panel: assign some matters to them
    for plan, code in ((carmel_plan, "C-014"), (ofek_plan, "C-031")):
        for g in plan:
            cand = [m for m in matters if m["group"] == g and m["client"] not in ("C-014", "C-031")
                    and m["has25"] and m["type"] in ("hourly", "capped", "retainer")]
            m = cand[int(r.random() * len(cand))]
            m["client"], m["w25"] = code, m["w25"] * 2.5
            if code == "C-031":
                m["has26"], m["w26"] = True, m["w26"] * 0.3
    # The two NDA matters (hourly 2024-2025, fixed per document 2026): values come from the workstream
    nda25 = sum(x["fees"] for x in nda if x["month"].startswith("2025"))
    nda26 = sum(x["fees"] for x in nda if x["month"].startswith("2026") and x["month"] <= "2026-09")
    h25 = sum(x["hours"] for x in nda if x["month"].startswith("2025"))
    h26 = sum(x["hours"] for x in nda if x["month"].startswith("2026") and x["month"] <= "2026-09")
    matters.append(dict(id="M-2024-0091", client="C-014", group="Corporate", desk="", partner="L007", type="hourly",
                        opened=2024, has25=True, has26=False, fixed25=nda25, worked25=r10(h25 * 890 / 0.97),
                        note="NDA programme 2024-2025 (closed 31 Dec 2025)"))
    matters.append(dict(id="M-2026-0007", client="C-014", group="Corporate", desk="", partner="L007", type="fixed",
                        opened=2026, has25=False, has26=True, fixed26=nda26, worked26=r10(h26 * 920),
                        note="NDA programme 2026: ₪1,150 per NDA"))
    # scale 2025 per (group, type) cell; Carmel scaled first to ₪6.1M in total
    carmel = [m for m in matters if m["client"] == "C-014" and "fixed25" not in m and m["has25"]]
    cw = sum(m["w25"] for m in carmel)
    for m in carmel:
        m["b25"] = (6.1e6 - nda25) * m["w25"] / cw
    for g in GROUPS:
        for t, share in zip(TYPES, TYPE_SHARE[g]):
            cell = [m for m in matters if m["group"] == g and m["type"] == t and m["has25"]]
            fixed_part = sum(m.get("b25", 0) + m.get("fixed25", 0) for m in cell)
            rest = [m for m in cell if "b25" not in m and "fixed25" not in m]
            target = GROUP_REV_2025[g] * share - fixed_part
            w = sum(m["w25"] for m in rest) or 1
            for m in rest:
                m["b25"] = target * m["w25"] / w
            cell26 = [m for m in matters if m["group"] == g and m["type"] == t and m["has26"] and "fixed26" not in m]
            w = sum(m["w26"] for m in cell26) or 1
            t26 = GROUP_REV_2025[g] * share * GROUP_2026_FACTOR[g]
            for m in cell26:
                m["b26"] = t26 * m["w26"] / w
    for m in matters:
        if "fixed25" in m:
            m["b25"] = m["fixed25"]
        if "fixed26" in m:
            m["b26"] = m["fixed26"]
        for yr in ("25", "26"):
            b = m.get("b" + yr)
            if b is None:
                continue
            if "worked" + yr in m:
                worked = m["worked" + yr]
            else:
                real = {"hourly": r.gauss(0.88 if m["group"] == "Litigation" else 0.92, 0.035),
                        "capped": r.gauss(0.79, 0.05), "retainer": r.gauss(0.86, 0.04),
                        "fixed": r.gauss(0.745 if m["group"] == "Tech & IP" else 0.95, 0.05)}[m["type"]]
                worked = b / max(0.5, min(1.15, real))
            m["b" + yr], m["wv" + yr] = r10(b), r10(worked)
        m["terms"] = m.get("note") or {"hourly": "hourly, firm rates",
                                       "capped": f"capped at ₪{r10(m.get('b25', m.get('b26', 0)) * 1.05):,}",
                                       "fixed": f"fixed fee ₪{r10(m.get('b25', m.get('b26', 0))):,}",
                                       "retainer": "monthly retainer"}[m["type"]]
    return matters


def write_firm(lawyers, clients, matters, nda) -> dict:
    write_csv(ROOM / "people" / "lawyers.csv",
              ["lawyer_id", "name", "role", "practice_group", "desk", "year_admitted", "languages",
               "billable_target_h", "billable_2025_h", "billable_2026_jan_sep_h", "standard_rate_ils"],
              [[l["id"], l["name"], l["role"], l["group"], l["desk"], l["year"], l["langs"], l["target"],
                l["h2025"], l["h2026"], l["rate"]] for l in lawyers])
    fees = {}
    for m in matters:
        f = fees.setdefault(m["client"], [0, 0])
        f[0] += m.get("b25", 0)
        f[1] += m.get("b26", 0)
    r = rng("clients-out")
    ocg = {"C-014": ("yes", "disclose+consent+no_hourly_for_tech_avoidable"), "C-003": ("yes", "consent"),
           "C-007": ("yes", "prohibited_unless_approved_in_writing"), "C-022": ("yes", "disclose"),
           "C-005": ("yes", "none"), "C-011": ("yes", "none"), "C-019": ("yes", "none"), "C-026": ("yes", "none"),
           "C-040": ("yes", "none")}
    rows = []
    for c in clients:
        f25, f26 = fees.get(c["code"], [0, 0])
        if not f25 and not f26:
            continue
        f24 = r10(f25 * r.uniform(0.85, 1.12)) if c["since"] < 2025 else 0
        o = ocg.get(c["code"], ("no", ""))
        renewal = "2027-01-31" if c["code"] == "C-014" else (r.choice(["2027-01-01", "2027-03-31", "2027-06-30", ""])
                                                            if o[0] == "yes" else "")
        rows.append([c["code"], c["name"], c["sector"], c["since"], f24, r10(f25), r10(f26), o[0], o[1], renewal])
    write_csv(ROOM / "clients" / "clients.csv",
              ["client_code", "client_name", "sector", "client_since", "fees_2024_ils", "fees_2025_ils",
               "fees_2026_jan_sep_ils", "outside_counsel_guidelines", "ocg_ai_clause", "next_renewal"], rows)
    write_csv(ROOM / "billing" / "matters.csv",
              ["matter_id", "client_code", "practice_group", "desk", "responsible_partner", "billing_type",
               "fee_terms", "opened_year", "status", "worked_value_2025_ils", "billed_2025_ils",
               "worked_value_2026_jan_sep_ils", "billed_2026_jan_sep_ils"],
              [[m["id"], m["client"], m["group"], m["desk"], m["partner"], m["type"], m["terms"], m["opened"],
                "open" if m["has26"] else "closed", m.get("wv25", ""), m.get("b25", ""), m.get("wv26", ""),
                m.get("b26", "")] for m in sorted(matters, key=lambda x: x["id"])])
    write_csv(ROOM / "clients" / "carmel-nda-workstream.csv",
              ["month", "ndas_completed", "median_turnaround_days", "hours_recorded", "pricing_basis",
               "fees_billed_ils", "fee_per_nda_ils", "fees_per_hour_ils"],
              [[x["month"], x["n"], x["t"], x["hours"], x["basis"], x["fees"], x["per"], x["eff"]] for x in nda])
    return {c[0]: c for c in rows}
