"""Condition monitoring on K21-K23 (historian, hourly, Q4 2026) and Plant G's SCADA alarms (H2 2026).

Reading this spoils the engagement: finish module 13 first.
"""
from __future__ import annotations

from datetime import datetime, timedelta

from gen_common import ROOM, il_offset, is_working_time, machines, rng, us_utc, write_csv

UTC_DST_START = datetime(2026, 3, 27, 0, 0)   # 02:00 local +02:00
UTC_DST_END = datetime(2026, 10, 24, 23, 0)   # 02:00 local +03:00


def _local_from_utc(u: datetime) -> tuple[datetime, str]:
    off = 3 if UTC_DST_START <= u < UTC_DST_END else 2
    local = u + timedelta(hours=off)
    return local, local.strftime("%Y-%m-%dT%H:%M:%S") + f"+0{off}:00"


def write_sensors(events: list[dict]) -> dict:
    r = rng(10)
    down = {}
    for e in events:
        if e["mes"] in ("K21", "K22", "K23") and e["start"] >= datetime(2026, 9, 30):
            down.setdefault(e["mes"], []).append((e["start"], e["end"]))
    rows = []
    u = datetime(2026, 9, 30, 21, 0)  # 1 October 00:00 local
    end = datetime(2026, 12, 31, 22, 0)
    outage = (datetime(2026, 10, 19, 10, 0), datetime(2026, 10, 21, 16, 0))
    stuck = (datetime(2026, 11, 8, 6, 0), datetime(2026, 11, 17, 11, 0))
    ramp = (datetime(2026, 11, 11, 0, 0), datetime(2026, 12, 2, 3, 10))
    base = {"K21": (44.0, 168.0, 2.3, 31.5), "K22": (45.5, 172.0, 2.1, 38.0), "K23": (43.2, 160.0, 2.4, 27.0)}
    while u <= end:
        local, stamp = _local_from_utc(u)
        if not (outage[0] <= local < outage[1]):
            for mc in ("K21", "K22", "K23"):
                oil, press, vib, cyc = base[mc]
                status = "RUN" if is_working_time(local) else "IDLE"
                for s, e in down.get(mc, []):
                    if s - timedelta(minutes=59) <= local <= e:
                        status = "DOWN"
                if r.random() < 0.004:
                    continue  # dropped sample
                if status == "RUN":
                    cyc_v = round(cyc * r.uniform(0.97, 1.05), 1)
                    shots = int(3600 / cyc_v * r.uniform(0.85, 0.98))
                    oil_v = round(oil + r.gauss(0, 1.2) + (3 if 11 <= local.hour <= 16 else 0), 1)
                    press_v = round(press + r.gauss(0, 4), 0)
                    vib_v = vib + r.gauss(0, 0.15)
                    if mc == "K22" and ramp[0] <= local < ramp[1]:
                        frac = (local - ramp[0]).total_seconds() / (ramp[1] - ramp[0]).total_seconds()
                        vib_v += 5.4 * frac ** 1.6 + r.gauss(0, 0.25)
                        press_v -= round(14 * frac)
                        oil_v += round(3.5 * frac, 1)
                    if mc == "K22" and local >= ramp[1]:
                        vib_v = 1.9 + r.gauss(0, 0.12)
                    vib_v = round(max(0.3, vib_v), 2)
                elif status == "IDLE":
                    cyc_v, shots, oil_v, press_v, vib_v = "", 0, round(oil - 12 + r.gauss(0, 1), 1), 0, round(abs(r.gauss(0.2, 0.05)), 2)
                else:
                    cyc_v, shots, oil_v, press_v, vib_v = "", 0, round(oil - 6 + r.gauss(0, 2), 1), 0, round(abs(r.gauss(0.3, 0.1)), 2)
                if mc == "K21" and stuck[0] <= local < stuck[1]:
                    vib_v = 2.38
                acc = round(118 + r.gauss(0, 1.5), 1) if status == "RUN" else ""
                rows.append([stamp, mc, status, shots, cyc_v, oil_v, press_v, vib_v, acc])
        u += timedelta(hours=1)
    n = write_csv(ROOM / "sensors" / "condition-k21-k23-2026q4.csv",
                  ["timestamp", "machine", "status", "shots", "cycle_time_s", "oil_temp_c",
                   "pump_pressure_bar_p95", "motor_vib_mm_s", "accumulator_bar_min"], rows)
    return {"sensor_rows": n}


MORANDI = {"OIL_TEMP": ("A101", "Temperatura olio alta"), "HYD_PUMP": ("A114", "Pressione pompa bassa"),
           "HYD_VALVE": ("A114", "Pressione pompa bassa"), "HEATER": ("A120", "Riscaldamento zona guasto"),
           "TC": ("A131", "Termocoppia interrotta"), "GATE": ("A140", "Porta di sicurezza aperta"),
           "DRIVE": ("A152", "Errore azionamento"), "HR_HEATER": ("A160", "Allarme canale caldo"),
           "HR_TC": ("A160", "Allarme canale caldo"), "HYD_LEAK": ("A117", "Livello olio basso")}
HAIWEI = {"OIL_TEMP": ("AL-012", "OIL TEMP OVER"), "HYD_PUMP": ("AL-021", "PUMP PRESSURE LOW"),
          "HYD_VALVE": ("AL-021", "PUMP PRESSURE LOW"), "HEATER": ("AL-033", "HEATER ZONE ERR"),
          "TC": ("AL-034", "THERMOCOUPLE BREAK"), "GATE": ("AL-041", "SAFETY DOOR OPEN"),
          "DRIVE": ("AL-055", "SERVO ALARM"), "HR_HEATER": ("AL-061", "MOLD HOT RUNNER ALM"),
          "HR_TC": ("AL-061", "MOLD HOT RUNNER ALM"), "HYD_LEAK": ("AL-015", "OIL LEVEL LOW")}


def write_alarms(events: list[dict]) -> dict:
    """Plant G line SCADA: station by hall position, time MM/DD/YYYY in UTC, chattering door alarms."""
    r = rng(11)
    rows = []
    h2 = datetime(2026, 7, 1)
    for e in events:
        if e["plant"] != "G" or e["start"] < h2:
            continue
        table = MORANDI if e["maker"] == "Morandi" else HAIWEI
        if e["cause"] not in table:
            continue
        code, text = table[e["cause"]]
        t = e["start"] - timedelta(minutes=r.randint(0, 3))
        for k in range(r.choice([1, 1, 2, 3])):
            tk = t + timedelta(seconds=40 * k + r.randint(0, 30))
            ack = tk + timedelta(minutes=r.randint(1, 50)) if r.random() < 0.7 else None
            rows.append((tk, [us_utc(tk), f"PRS_{e['hall']:02d}", code, text, "HIGH" if k == 0 else "MED",
                              us_utc(ack) if ack else ""]))
    gm = [m for m in machines() if m["plant"] == "G"]
    for _ in range(1500):  # nuisance: door switches chattering, low-priority warnings
        m = r.choice(gm)
        t = h2 + timedelta(minutes=r.randrange(184 * 24 * 60))
        if not is_working_time(t):
            continue
        table = MORANDI if m["maker"] == "Morandi" else HAIWEI
        code, text = table["GATE"] if r.random() < 0.7 else (("W210", "Lubrificazione ciclo") if m["maker"] == "Morandi" else ("WN-07", "LUBE CYCLE"))
        for k in range(r.choice([1, 2, 4])):
            tk = t + timedelta(seconds=7 * k)
            rows.append((tk, [us_utc(tk), f"PRS_{m['hall']:02d}", code, text, "LOW", ""]))
    rows.sort(key=lambda x: x[0])
    n = write_csv(ROOM / "scada" / "alarms-plant-g-2026h2.csv",
                  ["Time", "Station", "Alarm", "Message", "Priority", "Ack Time"], [x[1] for x in rows])
    return {"alarm_rows": n}
