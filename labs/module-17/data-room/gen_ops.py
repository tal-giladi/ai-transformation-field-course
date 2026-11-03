"""operations/route-daily-by-depot.csv, operations/dispatcher-overrides-2027.csv,
operations/fleet-km-fuel-monthly.csv, operations/warehouse-overtime-weekly.csv."""
from datetime import date, timedelta

from gen_common import (DEPOTS, ROUTE_NORTH_LIVE, ROUTE_ALL_REGIONS, SOUTH_PULLED_BACK,
                        CENTRE_PLANNER_ONLY, rng, write_csv, days, is_workday)

ROUTES = {"HFA": 18, "KRM": 12, "KSH": 7, "MOD": 22, "APL": 16, "PTK": 12, "ASH": 20, "BSV": 12,
          "NTV": 9, "RTM": 10}
STOPS = {"North": 14, "Centre": 18, "South": 15, "Europe": 9}
KM_PER_STOP = {"HFA": 4.3, "KRM": 6.8, "KSH": 10.4, "MOD": 3.9, "APL": 4.6, "PTK": 3.4, "ASH": 4.4,
               "BSV": 7.6, "NTV": 8.9, "RTM": 7.2}
OVERRIDE = {"HFA": 0.17, "KRM": 0.28, "KSH": 0.55, "MOD": 0.33, "APL": 0.36, "PTK": 0.31,
            "ASH": 0.44, "BSV": 0.52, "NTV": 0.61}


def works(region: str, d: date) -> bool:
    if region == "Europe":
        return d.weekday() < 5
    return is_workday(d)


def tool_share(region: str, code: str, d: date) -> tuple[float, bool]:
    """Share of routes planned in Tzir Route that day, and whether plans go to the driver app."""
    if region == "North":
        return (0.0, False) if d < ROUTE_NORTH_LIVE else (0.97, True)
    if region == "Europe" or d < ROUTE_ALL_REGIONS:
        return 0.0, False
    if region == "South":
        if d >= SOUTH_PULLED_BACK:
            return 0.0, False
        if d >= date(2027, 2, 14):
            return 0.55, True
        return 0.9, True
    # Centre
    if d >= CENTRE_PLANNER_ONLY:
        return 0.58, False
    return 0.92, True


def route_daily(over_rows: list) -> int:
    r = rng(1)
    header = ["date", "region", "depot_code", "depot", "routes", "routes_tool_planned",
              "routes_dispatched_as_planned", "routes_overridden", "stops", "km_naive_baseline",
              "km_tool_plan", "km_actual", "late_stops"]
    rows = []
    seq = 0
    for d in days(date(2026, 10, 1), date(2027, 6, 3)):
        for region, code, name in DEPOTS:
            if not works(region, d):
                continue
            routes = max(3, round(ROUTES[code] * r.uniform(0.88, 1.1) * (0.7 if d.weekday() == 4 else 1)))
            stops = round(routes * STOPS[region] * r.uniform(0.93, 1.07))
            share, app = tool_share(region, code, d)
            planned = round(routes * share)
            overridden = 0
            dispatched = 0
            if planned and app:
                o = OVERRIDE[code]
                if region == "South" and d >= date(2027, 2, 1):
                    o += 0.12
                overridden = sum(1 for _ in range(planned) if r.random() < o)
                dispatched = planned - overridden
            base = KM_PER_STOP[code] * stops
            saving = 0.058 * (dispatched / routes) if region == "North" else 0.0
            drift = 1.012 if (region == "South" and ROUTE_ALL_REGIONS <= d < SOUTH_PULLED_BACK) else 1.0
            km_actual = round(base * (1 - saving) * drift * r.uniform(0.97, 1.03))
            km_naive = km_plan = None
            if planned:
                stops_tool = stops * planned / routes
                km_naive = round(KM_PER_STOP[code] * stops_tool * 1.19 * r.uniform(0.98, 1.02))
                km_plan = round(km_naive * r.uniform(0.80, 0.84))
            late_rate = 0.04
            if region == "South" and ROUTE_ALL_REGIONS <= d < SOUTH_PULLED_BACK:
                late_rate = 0.065 + 0.0006 * (d - ROUTE_ALL_REGIONS).days
            late = sum(1 for _ in range(stops) if r.random() < late_rate)
            rows.append([d.isoformat(), region, code, name, routes, planned, dispatched, overridden,
                         stops, km_naive, km_plan, km_actual, late])
            for k in range(overridden):
                if r.random() < 0.42:
                    seq += 1
                    over_rows.append((d, region, code, k, seq))
    return write_csv("operations/route-daily-by-depot.csv", header, rows)


REASONS = {
    "ROAD_CLOSED": ["כביש 899 סגור, נסענו דרך 90", "המערכת שלחה דרך כביש סגור", "Road closed, detour via Rt 85",
                    "Дорога закрыта, объезд через 90", "الطريق مغلق، تحويلة عبر 85", "מסלול דרך כביש 232 סגור",
                    "כביש סגור ליד הגבול – עקיפה", "መንገዱ ተዘግቷል"],
    "SECURITY_RESTRICTION": ["אזור צבאי סגור לפי הנחיה", "Military zone, no entry for trucks",
                             "منطقة عسكرية مغلقة", "Маршрут через закрытую зону", "הגבלת תנועה – לא לנסוע אחרי חשכה"],
    "CUSTOMER_WINDOW": ["חלון אספקה של הלקוח 07:00-09:00", "Customer receives until 10:00 only",
                        "الزبون يستلم فقط في الصباح", "Клиент принимает только до 10:00"],
    "DRIVER_HOURS": ["נהג חורג משעות נהיגה לפי התכנון", "Plan exceeds driver hours", "Превышение часов водителя"],
    "TRAFFIC": ["עומס בצומת גולני", "Traffic at port gate 3", "פקק בכניסה לנמל"],
    "PLAN_ERROR": ["המסלול לא הגיוני, תחנה כפולה", "Plan sends truck back and forth", "تخطيط غير منطقي"],
    "DRIVER_REFUSED": ["נהג סירב לנסוע במסלול", "السائق رفض المسار"],
    "OTHER": ["", "ראה הודעה בקבוצה", "n/a"],
}
DISPATCHERS = {"North": ["F. Khatib", "S. Levi", "Y. Nassar"], "Centre": ["G. Rosen", "M. Ohayon", "D. Tsegaye"],
               "South": ["R. Haj-Yahia", "A. Elbaz", "V. Petrov"]}


def overrides(over_rows: list) -> int:
    r = rng(2)
    header = ["override_id", "date", "region", "depot_code", "route_id", "dispatcher", "reason_code",
              "reason_text", "km_tool_plan", "km_dispatched"]
    rows = []
    for d, region, code, k, seq in over_rows:
        if d < date(2027, 1, 10):
            continue
        if code == "KSH":
            weights = {"ROAD_CLOSED": 5, "SECURITY_RESTRICTION": 4, "CUSTOMER_WINDOW": 1, "OTHER": 1}
        elif region == "South":
            weights = {"ROAD_CLOSED": 4, "SECURITY_RESTRICTION": 2, "DRIVER_REFUSED": 2, "PLAN_ERROR": 2,
                       "CUSTOMER_WINDOW": 1, "OTHER": 1}
        elif region == "Centre":
            weights = {"CUSTOMER_WINDOW": 4, "PLAN_ERROR": 3, "TRAFFIC": 3, "DRIVER_HOURS": 2, "OTHER": 2}
        else:
            weights = {"ROAD_CLOSED": 3, "CUSTOMER_WINDOW": 3, "TRAFFIC": 2, "DRIVER_HOURS": 1, "OTHER": 1}
        codes = list(weights)
        rc = r.choices(codes, [weights[c] for c in codes])[0]
        text = r.choice(REASONS[rc])
        shown = "" if (rc == "OTHER" and r.random() < 0.5) else rc
        plan_km = round(KM_PER_STOP[code] * STOPS[region] * r.uniform(0.8, 1.15))
        disp_km = round(plan_km * (r.uniform(1.08, 1.35) if rc in ("ROAD_CLOSED", "SECURITY_RESTRICTION")
                                   else r.uniform(0.95, 1.12)))
        rows.append([f"OVR-{seq:05d}", d.isoformat(), region, code, f"{code}-{d:%m%d}-{k + 1:02d}",
                     r.choice(DISPATCHERS[region]), shown, text, plan_km, disp_km])
    return write_csv("operations/dispatcher-overrides-2027.csv", header, rows)


def fleet_monthly() -> int:
    r = rng(3)
    header = ["month", "region", "trucks", "km_telematics", "stops", "km_per_stop", "fuel_litres",
              "fuel_cost_ils"]
    base = {"North": (104, 6.12), "Centre": (70, 3.95), "South": (92, 5.71), "Europe": (44, 7.18)}
    rows = []
    y, m = 2025, 1
    while (y, m) <= (2027, 5):
        for region, (trucks, kps) in base.items():
            stops = round(trucks * 21 * STOPS[region] * 0.62 * r.uniform(0.95, 1.05))
            f = 1.0
            if region == "North" and (y, m) >= (2026, 12):
                f = 0.958
            elif region == "North" and (y, m) == (2026, 11):
                f = 0.985
            elif region == "South" and (y, m) in ((2027, 1), (2027, 2)):
                f = 1.016
            k = round(kps * f * r.uniform(0.985, 1.015), 2)
            km = round(stops * k)
            litres = round(km * 0.33 * r.uniform(0.98, 1.02))
            price = 7.05 + 0.02 * ((y - 2025) * 12 + m) if region != "Europe" else 6.4
            rows.append([f"{y}-{m:02d}", region, trucks, km, stops, k, litres, round(litres * price)])
        m += 1
        if m == 13:
            y, m = y + 1, 1
    return write_csv("operations/fleet-km-fuel-monthly.csv", header, rows)


def warehouse() -> int:
    r = rng(4)
    header = ["week_start", "dc", "pallets_handled", "headcount", "regular_hours", "overtime_hours",
              "agency_hours", "overtime_cost_ils", "agency_cost_ils", "labour_plan_source"]
    rows = []
    wk = date(2026, 7, 5)
    while wk <= date(2027, 5, 30):
        season = 1.0 + 0.12 * (wk.month in (9, 10, 3, 4))
        for dc, hc, ot, ag in (("Modi'in DC", 118, 690, 410), ("Ashdod DC", 96, 560, 330)):
            pallets = round(hc * 52 * season * r.uniform(0.94, 1.06))
            live = dc.startswith("Modi") and wk >= date(2027, 1, 3)
            o = ot * season * r.uniform(0.9, 1.1) * (0.86 if live else 1.0)
            a = ag * season * r.uniform(0.9, 1.1) * (0.93 if live else 1.0)
            src = "forecast model v1" if live else "spreadsheet (supervisor)"
            rows.append([wk.isoformat(), dc, pallets, hc, hc * 42, round(o), round(a), round(o) * 78, round(a) * 64, src])
        wk += timedelta(days=7)
    return write_csv("operations/warehouse-overtime-weekly.csv", header, rows)


def build() -> dict:
    over_rows: list = []
    return {
        "route-daily": route_daily(over_rows),
        "overrides": overrides(over_rows),
        "fleet-monthly": fleet_monthly(),
        "warehouse": warehouse(),
    }
