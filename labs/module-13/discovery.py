"""Kinneret Plastics: the discovery and baseline numbers (lessons 13.2 and 13.3).

    python discovery.py            # everything
    python discovery.py downtime   # one section: downtime, mttr, workorders, pm, night, parts, assets,
                                   # sensors, scrap, safety

Reads the data room by relative path; no network. Prints what it found, with numerators and denominators.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))

import pandas as pd  # noqa: E402

from fieldkit.data import data_room, load  # noqa: E402

ROOM = data_room("module-13")
MACHINE = ("MECH", "ELEC", "HYD")
PLANNED = ("PM", "SETUP", "NO_ORDER")


def pct(a, b) -> str:
    return f"{100 * a / b:.1f}% ({a} of {b})" if b else "n/a"


def downtime() -> pd.DataFrame:
    dt = load(ROOM / "production" / "downtime-events-2026.csv")
    un = dt[~dt.reason_code.isin(PLANNED)].copy()
    un["group"] = un.reason_code.map(lambda c: "machine" if c in MACHINE else c.lower())
    print("\n== Unplanned downtime 2026 by reason (ProdTrack), hours ==")
    t = un.pivot_table(index="group", columns="plant", values="duration_min", aggfunc="sum").fillna(0) / 60
    t["total"] = t.sum(axis=1)
    t["share_%"] = 100 * t["total"] / t["total"].sum()
    print(t.round(0).sort_values("total", ascending=False).to_string())
    print("\nMean duration (h) of MOULD stops by shift:")
    print((un[un.reason_code == "MOULD"].groupby("shift").duration_min.mean() / 60).round(1).to_string())
    print("\nMean duration (h) of machine stops (MECH/ELEC/HYD) by shift:")
    print((un[un.reason_code.isin(MACHINE)].groupby("shift").duration_min.mean() / 60).round(1).to_string())
    print(f"\nWAIT_TECH stops at night: {pct(int(((un.reason_code == 'WAIT_TECH') & (un['shift'] == 'night')).sum()), int((un.reason_code == 'WAIT_TECH').sum()))}")
    return dt


def g_crosswalk() -> dict:
    """Plant G hall number -> MES machine, matched on the serial number (not on the number)."""
    gl = pd.read_csv(ROOM / "assets" / "asset-list-plant-g.csv", dtype=str, keep_default_na=False)
    mes = pd.read_csv(ROOM / "assets" / "mes-machines.csv", dtype=str, keep_default_na=False)
    by_serial = dict(zip(mes.serial, mes.machine))
    return {int(r["מס' מכונה"]): by_serial[r["מס' סידורי"]] for _, r in gl.iterrows()
            if r["מס' מכונה"].isdigit()}


def g_log() -> pd.DataFrame:
    g = pd.read_csv(ROOM / "maintenance" / "maintenance-log-plant-g-2026.csv", dtype=str, keep_default_na=False)
    g["hall"] = g["מכונה"].map(lambda s: int(re.findall(r"\d+", s)[0]))
    g["call"] = pd.to_datetime(g["תאריך"] + " " + g["שעת קריאה"], format="%d/%m/%Y %H:%M")

    def ready(row):
        s = row["מוכן ב-"]
        if not s:
            return pd.NaT
        if " " in s:
            d, t = s.split(" ")
            r = pd.to_datetime(f"{d}/{row['call'].year} {t}", format="%d/%m/%Y %H:%M")
            return r if r >= row["call"] else r + pd.DateOffset(years=1)
        return pd.to_datetime(row["תאריך"] + " " + s, format="%d/%m/%Y %H:%M")
    g["ready"] = g.apply(ready, axis=1)
    return g


def mttr(dt: pd.DataFrame) -> None:
    print("\n== MTTR: the same word at two plants ==")
    maint = ("MECH", "ELEC", "HYD", "MOULD", "WAIT_TECH")
    k = dt[(dt.plant == "K") & dt.reason_code.isin(maint)]
    print(f"Plant K, ProdTrack stop -> restart: {k.duration_min.mean() / 60:.1f} h (n = {len(k)})")
    g = g_log()
    rep = g[(g["תקלה"] != "טיפול מונע חודשי") & g.ready.notna()]
    print(f"Plant G, log call -> 'ready': {((rep.ready - rep.call).dt.total_seconds() / 3600).mean():.1f} h (n = {len(rep)})")
    gm = dt[(dt.plant == "G") & dt.reason_code.isin(maint)]
    print(f"Plant G, ProdTrack stop -> restart: {gm.duration_min.mean() / 60:.1f} h (n = {len(gm)})")
    cw = g_crosswalk()
    moved = {h: m for h, m in cw.items() if m != f"G{h:02d}"}
    print(f"Hall numbers that are not the MES number: {moved}")
    ev = gm.copy()
    ev["start_local"] = ev.start_at.dt.tz_localize(None)
    ev["end_local"] = ev.end_at.dt.tz_localize(None)
    gaps, matched = [], 0
    for _, row in rep.iterrows():
        m = cw.get(row["hall"])
        c = ev[(ev.machine == m) & ((ev.start_local - row.call).abs() <= pd.Timedelta(minutes=30))]
        if len(c):
            matched += 1
            gaps.append((c.end_local.iloc[0] - row.ready).total_seconds() / 60)
    s = pd.Series(gaps)
    print(f"Log rows matched to a ProdTrack stop (machine via crosswalk, start within 30 min): {pct(matched, len(rep))}")
    print(f"'Ready' -> production restarted: median {s.median():.0f} min, mean {s.mean():.0f} min; "
          f"restart after 'ready' in {pct(int((s > 0).sum()), len(s))}")


def workorders() -> pd.DataFrame:
    wo = load(ROOM / "maintenance" / "work-orders-plant-k-2026.csv")
    bd = wo[wo.wo_type == "BD"].copy()
    print("\n== Plant K breakdown work orders (MaintPro) ==")
    code = bd.failure_code.fillna("").astype(str).str.replace(".0", "", regex=False)
    print(f"Breakdown WOs: {len(bd)}; failure code blank {pct(int((code == '').sum()), len(bd))}; "
          f"'99' {pct(int((code == '99').sum()), len(bd))}; another code {pct(int(((code != '') & (code != '99')).sum()), len(bd))}")
    bd["month"] = bd.requested_at.dt.month
    coded = bd.assign(c=(code != "") & (code != "99")).groupby("month").c.mean() * 100
    print("Coded (not blank, not 99) by month, %: " + ", ".join(f"{m}: {v:.0f}" for m, v in coded.items()))
    vague = bd.action_text.fillna("").str.strip().str.lower().isin(
        ["תוקן", "תוקן.", "בוצע", "done", "ok", "טופל", "fixed", "تم", "сделано", "סודר"])
    print(f"Action text is only 'fixed/done': {pct(int(vague.sum()), len(bd))}")
    print(f"Action text mentions the notebook or Vladi: {pct(int(bd.action_text.fillna('').str.contains('מחברת|ולדי').sum()), len(bd))}")
    nf = bd.action_text.fillna("").str.contains("לא נמצא|לא היה במדף|לא קיים|مش بالرف")
    print(f"Action text says the part was not where the list said: {int(nf.sum())}")
    print(f"downtime_min blank or 0: {pct(int((bd.downtime_min.isna() | (bd.downtime_min == 0)).sum()), len(bd))}; "
          f"started_at blank: {pct(int(bd.started_at.isna().sum()), len(bd))}")
    t = bd.completed_at
    mins = t.dt.hour * 60 + t.dt.minute
    near_end = mins.apply(lambda m: any(0 <= e - m <= 15 for e in (405, 885, 1365)))
    planner = bd.closed_by == "svetlana.p"
    print(f"Completed in the 15 minutes before a shift change: {pct(int(near_end.sum()), len(bd))}; "
          f"closed by the planner (Thursday afternoons): {pct(int(planner.sum()), len(bd))}")
    lang = bd.problem_text.fillna("").map(lambda s: "ar" if re.search("[؀-ۿ]", s) else
                                          "ru" if re.search("[Ѐ-ӿ]", s) else
                                          "he" if re.search("[֐-׿]", s) else "en")
    print("Problem text script: " + ", ".join(f"{k} {v}" for k, v in lang.value_counts().items()))
    return wo


def pm(wo: pd.DataFrame, dt: pd.DataFrame) -> None:
    print("\n== Preventive maintenance ==")
    p = wo[wo.wo_type == "PM"]
    closed = p.status == "סגור"
    print(f"PM compliance as reported (closed / scheduled): {pct(int(closed.sum()), len(p))}")
    bulk = p[(p.closed_by == "svetlana.p") & p.labour_min.isna()]
    print(f"PM WOs closed by the planner with no labour time: {len(bulk)} on "
          f"{sorted(bulk.completed_at.dt.strftime('%Y-%m-%d').unique())}, machines "
          f"{sorted(bulk.asset_id.unique())}")
    real = p[closed & p.labour_min.notna()]
    print(f"PM compliance counting only PMs with labour recorded: {pct(len(real), len(p))}")
    ids = {a.replace("KN-IM-", "K") for a in bulk.asset_id.unique()}
    m = dt[(dt.plant == "K") & dt.reason_code.isin(MACHINE)].copy()
    m["period"] = m.start_at.dt.month.map(lambda x: "Oct-Dec" if x >= 10 else "Jan-Sep")
    m["group"] = m.machine.map(lambda x: "deferred six" if x in ids else "other twenty")
    n = m.groupby(["group", "period"]).size().unstack()
    n["Jan-Sep"] = n["Jan-Sep"] / 9
    n["Oct-Dec"] = n["Oct-Dec"] / 3
    n = n.div(pd.Series({"deferred six": len(ids), "other twenty": 26 - len(ids)}), axis=0)
    print("Machine stops (MECH/ELEC/HYD) per machine per month:\n" + n.round(2).to_string())


def night() -> None:
    nc = pd.read_csv(ROOM / "maintenance" / "night-calls-2026.csv", dtype=str)
    for c in ("minutes_to_reach", "minutes_on_phone", "machine_waiting_min"):
        nc[c] = nc[c].astype(int)
    weeks = (pd.to_datetime(nc.date).max() - pd.to_datetime("2026-03-01")).days / 7
    print("\n== Night calls to the maintenance manager (Mar-Dec 2026) ==")
    print(f"Calls: {len(nc)} (~{len(nc) / weeks:.1f} a week); machine waiting median {nc.machine_waiting_min.median():.0f} min, "
          f"total {nc.machine_waiting_min.sum() / 60:.0f} h; solved by phone {pct(int((nc.solved_by_phone == 'כן').sum()), len(nc))}; "
          f"came in {int((nc.came_in == 'כן').sum())}")
    print("Topics:\n" + nc.topic.value_counts().to_string())
    print("By technician:\n" + nc.technician_id.value_counts().to_string())


def parts() -> None:
    rep = pd.read_csv(ROOM / "parts" / "parts-list-shared-drive.csv", dtype=str, keep_default_na=False)
    erp = pd.read_csv(ROOM / "parts" / "erp-parts-2026-12-31.csv", dtype=str, keep_default_na=False)
    e = erp.set_index("part_number")
    sup = rep['מק"ט'].map(lambda p: e.loc[p, "status"] == "superseded" if p in e.index else False)
    active = rep[~sup]
    bins = active.apply(lambda r: r["מיקום"] == e.loc[r['מק"ט'], "bin_plant_k"], axis=1)
    print("\n== Parts list on the drive vs ERP ==")
    print(f"Replica rows: {len(rep)}; superseded in ERP: {pct(int(sup.sum()), len(rep))}; "
          f"bin equal to ERP among the rest: {pct(int(bins.sum()), len(active))}")
    print(f"ERP Plant G parts (none in the replica): {int((erp.bin_plant_g != '').sum())}")


def assets() -> None:
    k = load(ROOM / "assets" / "asset-register-plant-k.csv")
    imm = k[k["class"] == "IMM"]
    print("\n== Asset registers ==")
    print(f"Plant K machines with a MES code in the CMMS register: {pct(int(imm.mes_code.notna().sum()), len(imm))}")
    print(f"Criticality filled: {int(k.criticality.notna().sum())} of {len(k)}; moulds in the CMMS: 0; moulds in the tooling list: "
          f"{len(load(ROOM / 'assets' / 'mould-list.csv'))}")
    ml = load(ROOM / "assets" / "mould-list.csv")
    sc = ml.shot_counter.astype(str)
    print(f"Moulds with a numeric shot count: {pct(int(sc.str.isdigit().sum()), len(ml))}; last service blank "
          f"{pct(int(ml.last_service.isna().sum()), len(ml))}")


def sensors() -> None:
    s = pd.read_csv(ROOM / "sensors" / "condition-k21-k23-2026q4.csv", dtype={"timestamp": str})
    print("\n== Condition monitoring ==")
    print(f"Machines with sensor data: {s.machine.nunique()} of 40; rows {len(s)}; first {s.timestamp.min()}")
    s["t"] = pd.to_datetime(s.timestamp, utc=True)
    for m, g in s.groupby("machine"):
        gaps = g.t.sort_values().diff().dt.total_seconds().div(3600)
        run = g[g.status == "RUN"]
        stuck = run.motor_vib_mm_s.round(2).value_counts().iloc[0]
        print(f"{m}: hours missing {int((gaps[gaps > 1] - 1).sum())}; most frequent RUN vibration value repeated {stuck} times")
    k22 = s[(s.machine == "K22") & (s.status == "RUN")].set_index("t").motor_vib_mm_s
    weekly = k22.resample("W").mean().round(2)
    print("K22 weekly mean vibration (RUN hours):\n" + weekly.to_string())
    local = s.timestamp.str[:19]
    print(f"Rows whose local time repeats if the UTC offset is dropped (25 October): "
          f"{int(s.assign(l=local).duplicated(['l', 'machine']).sum())}")


def scrap() -> None:
    sc = load(ROOM / "production" / "scrap-weekly-2026.csv")
    print("\n== Quality scrap ==")
    print(f"Scrap with a defect code: {pct(int(sc.scrap_total.sum() - sc.uncoded.sum()), int(sc.scrap_total.sum()))}")


def safety() -> None:
    ex = load(ROOM / "safety" / "periodic-examinations-register.csv")
    due = pd.to_datetime(ex.next_due.astype(str))
    late = ex[due < pd.Timestamp("2027-01-10")]
    print("\n== Periodic examinations (as of 10 January 2027) ==")
    print(late[["item", "plant", "description", "last_examination", "next_due", "status"]].to_string(index=False))


SECTIONS = ["downtime", "mttr", "workorders", "pm", "night", "parts", "assets", "sensors", "scrap", "safety"]

if __name__ == "__main__":
    want = sys.argv[1:] or SECTIONS
    dt = downtime() if {"downtime", "mttr", "pm"} & set(want) else None
    if "mttr" in want:
        mttr(dt)
    wo = workorders() if {"workorders", "pm"} & set(want) else None
    if "pm" in want:
        pm(wo, dt)
    for name in ("night", "parts", "assets", "sensors", "scrap", "safety"):
        if name in want:
            globals()[name]()
