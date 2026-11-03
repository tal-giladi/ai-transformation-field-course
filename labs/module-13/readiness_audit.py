"""Kinneret Plastics: the data-readiness audit of the maintenance records (lesson 13.5).

    python readiness_audit.py                 # the whole audit, no AI
    python readiness_audit.py --llm 40        # also ask an LLM to code 40 uncoded work orders (fieldkit.llm)
    python readiness_audit.py --out report.md # write the tables to a markdown file as well

Re-run it every month on new exports: the numbers are the foundation's progress measure. Reads the data
room by relative path; the only network call is the optional LLM step.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))

import pandas as pd  # noqa: E402

from fieldkit.data import data_room, load  # noqa: E402

ROOM = data_room("module-13")
OUT: list[str] = []

# Keyword rules: free text -> component class (Hebrew, Arabic, Russian, English, as technicians write)
RULES = [
    ("hot runner", r"הוט ראנר|חם רץ|טיפ|\bHR\b|HRC|هوت رنر|تيب|горячеканал|\bГК\b|сопло|hot runner"),
    ("mould water", r"מים מהתבנית|מים בקביטי|צינור מים לתבנית|מים על המוצר|مي .*القالب|تسريب مي|течь воды|вода в полости|water leak from mould"),
    ("mould pin/damage", r"פין|פלאש|ברר|תבנית נפגעה|دبوس|بن مكسور|فلاش|القالب انضرب|выталкиватель в форме|облой|ejector pin|flash"),
    ("pump", r"משאבה|مضخة|насос|pump"),
    ("valve", r"שסתום|סגירה איטית|פתיחת תבנית|הזרקה לא יציבה|بروبور|ولف|سكّر بطيء|فتح القالب|клапан|медленное закрытие|valve|slow clamp"),
    ("hydraulic leak", r"דליפ|שמן על הרצפה|צינור שמן|تسريب زيت|زيت على الأرض|бيسرب|течь масла|шланг|oil leak|hose"),
    ("oil temperature", r"טמפ' שמן|שמן חם|حرارة الزيت|انذار حرارة زيت|температура масла|перегрев масла|oil temp"),
    ("heater", r"גוף חימום|אזור .* לא|לא מתחמם|טמפ' צילינדר|سخان|المنطقة .* لا تسخن|الاسطوانة|нагреват|не греет|тэн|heater|not heating"),
    ("thermocouple", r"תרמוקפל|TC|קריאת טמפ'|ثرموكبل|قراءة الحرارة|термопар|скачет температура|thermocouple"),
    ("contactor/power", r"מנוע לא עולה|פחת|מגען|الموتور|فصل كهرباء|мотор не|автомат|motor won't"),
    ("drive", r"דרייבר|סרוו|ממיר|سيرفو|درايفر|сервопривод|частотник|servo|drive fault"),
    ("screw/check ring", r"כרית|בורג חוזר|short shot קבוע|الكوشن|البرغي|подушка|шнек|cushion"),
    ("toggle/clamp", r"טוגל|כוח סגירה|חריקה|التوغل|قوة الإغلاق|колен|усилие смыкания|toggle|clamp force"),
    ("machine ejector", r"פלט לא חוזר|מפלט מכונה|الإجكتور ما برجع|выталкиватель не|machine ejector"),
    ("safety gate", r"דלת|אינטרלוק|מתג בטיחות|الباب|انترلوك|مفتاح أمان|двер|блокировка|safety gate"),
    ("robot", r"רובוט|גריפר|الروبوت|робот|robot"),
    ("dryer/material", r"מייבש|נקודת טל|חומר|כסיפות|בועות|النشافة|مادة رطبة|فضة|сушилк|точка росы|сырой|dryer|splay"),
]
MOULD = {"hot runner", "mould water", "mould pin/damage"}


def say(text: str = "") -> None:
    print(text)
    OUT.append(text)


def pct(a, b) -> str:
    return f"{100 * a / b:.1f}% ({a}/{b})" if b else "n/a"


def classify(text: str) -> str:
    for name, pattern in RULES:
        if re.search(pattern, text or "", flags=re.IGNORECASE):
            return name
    return "(unclassified)"


def crosswalk_g() -> dict:
    gl = pd.read_csv(ROOM / "assets" / "asset-list-plant-g.csv", dtype=str, keep_default_na=False)
    mes = pd.read_csv(ROOM / "assets" / "mes-machines.csv", dtype=str, keep_default_na=False)
    by_serial = dict(zip(mes.serial, mes.machine))
    return {int(r["מס' מכונה"]): by_serial[r["מס' סידורי"]] for _, r in gl.iterrows() if r["מס' מכונה"].isdigit()}


def labels(dt: pd.DataFrame, wo: pd.DataFrame) -> pd.DataFrame:
    say("\n## 1. Outcome labels: can a breakdown be counted as a failure of a known mode?\n")
    bd = wo[wo.wo_type == "BD"].copy()
    code = bd.failure_code.fillna("").astype(str).str.replace(".0", "", regex=False)
    bd["coded"] = (code != "") & (code != "99") & (code != "92")
    bd["code"] = code
    bd["machine"] = bd.asset_id.str.replace("KN-IM-", "K", regex=False)
    stops = dt[(dt.plant == "K") & ~dt.reason_code.isin(["PM", "SETUP", "NO_ORDER", "QA_HOLD"])]
    matched = []
    for _, row in bd.iterrows():
        c = stops[(stops.machine == row.machine) & ((stops.start_at - row.requested_at).abs() <= pd.Timedelta(minutes=15))]
        matched.append(len(c) > 0)
    bd["matched"] = matched
    bd["usable"] = bd.coded & bd.matched
    say(f"- Plant K breakdown work orders 2026: {len(bd)}")
    say(f"- with a component code (not blank, not 99, not 92 'mould'): {pct(int(bd.coded.sum()), len(bd))}")
    say(f"- matched to a ProdTrack stop on the same machine within 15 min: {pct(int(bd.matched.sum()), len(bd))}")
    say(f"- **usable as a label (coded and matched): {pct(int(bd.usable.sum()), len(bd))}**")
    per = bd[bd.usable].code.value_counts()
    say(f"- codes with at least 30 usable events in 2026 (the vendor's minimum per failure mode): "
        f"{', '.join(per[per >= 30].index) or 'none'}; largest: {per.index[0]} ({per.iloc[0]})")
    say("- Plant G: the log has no failure-code column at all: 0 usable labels.")
    return bd


def backcode(bd: pd.DataFrame, g: pd.DataFrame) -> None:
    say("\n## 2. What the free text can still tell (keyword back-coding, component class only)\n")
    bd = bd.copy()
    bd["cls"] = (bd.problem_text.fillna("") + " " + bd.action_text.fillna("")).map(classify)
    gr = g[g["תקלה"] != "טיפול מונע חודשי"].copy()
    gr["cls"] = (gr["תקלה"] + " " + gr["טיפול"]).map(classify)
    for name, d in (("Plant K work orders", bd), ("Plant G log", gr)):
        cl = d.cls != "(unclassified)"
        mould = d.cls.isin(MOULD)
        say(f"- {name}: classified {pct(int(cl.sum()), len(d))}; of which mould-side {pct(int(mould.sum()), int(cl.sum()))}")
    both = pd.concat([bd.cls, gr.cls]).value_counts()
    say("\n| Component class (both plants) | Events 2026 |\n|---|---|")
    for k, v in both.items():
        say(f"| {k} | {v} |")
    say("\nA class is a component, not a failure mode (worn, leaking, seized, burnt) and not a cause. "
        "It is enough for a Pareto and for PM planning; it is not a label for prediction.")


def clocks(dt: pd.DataFrame) -> None:
    say("\n## 3. Three clocks\n")
    al = pd.read_csv(ROOM / "scada" / "alarms-plant-g-2026h2.csv", dtype=str, keep_default_na=False)
    first = al.Time.str[:2].astype(int)
    second = al.Time.str[3:5].astype(int)
    say(f"- SCADA `Time` values whose first field is above 12 (so it cannot be a day-first date): "
        f"{int((first > 12).sum())}; whose second field is above 12 (cannot be month-first): {int((second > 12).sum())} "
        f"of {len(al)} → the export is month-first (MM/DD/YYYY)")
    say(f"- ambiguous dates (both fields ≤ 12): {pct(int(((first <= 12) & (second <= 12)).sum()), len(al))}")
    cw = {f"PRS_{h:02d}": m for h, m in crosswalk_g().items()}
    hi = al[al.Priority == "HIGH"].copy()
    hi["naive"] = pd.to_datetime(hi.Time, format="%m/%d/%Y %H:%M:%S")
    hi["machine"] = hi.Station.map(cw)
    g = dt[(dt.plant == "G")].copy()
    g["utc"] = g.start_at.dt.tz_convert("UTC").dt.tz_localize(None)
    g["local"] = g.start_at.dt.tz_localize(None)
    for label, col in (("read as local time", "local"), ("read as UTC", "utc")):
        ok = 0
        for _, a in hi.iterrows():
            c = g[(g.machine == a.machine) & ((g[col] - a.naive).abs() <= pd.Timedelta(minutes=10))]
            ok += len(c) > 0
        say(f"- HIGH alarms matched to a ProdTrack stop within 10 min, {label}: {pct(ok, len(hi))}")
    hi["hallno"] = hi.Station.str[4:].astype(int)
    wrong = hi.Station.map(lambda s: f"G{int(s[4:]):02d}") != hi.machine
    say(f"- HIGH alarms from stations whose number is not the MES number: {pct(int(wrong.sum()), len(hi))}")


def assets(dt: pd.DataFrame, wo: pd.DataFrame, g: pd.DataFrame) -> None:
    say("\n## 4. One asset, three names\n")
    k = load(ROOM / "assets" / "asset-register-plant-k.csv")
    imm = k[k["class"] == "IMM"]
    say(f"- Plant K register rows with a MES code: {pct(int(imm.mes_code.notna().sum()), len(imm))}")
    say(f"- Plant G hall numbers that differ from the MES number: "
        f"{sum(1 for h, m in crosswalk_g().items() if m != f'G{h:02d}')} of 14 (matched on serial numbers)")
    say(f"- Plant K breakdown WOs logged against a machine for a mould problem (class mould, asset a machine): see section 2; "
        f"moulds have no asset id in MaintPro (231 moulds in tooling's list)")


def sensors(dt: pd.DataFrame) -> None:
    say("\n## 5. Sensor data\n")
    s = pd.read_csv(ROOM / "sensors" / "condition-k21-k23-2026q4.csv", dtype={"timestamp": str})
    s["t"] = pd.to_datetime(s.timestamp, utc=True)
    say(f"- machines with condition monitoring: {s.machine.nunique()} of 40, from {s.t.min().date()} ({s.t.dt.date.nunique()} days)")
    fails = dt[dt.machine.isin(["K21", "K22", "K23"]) & dt.reason_code.isin(["MECH", "ELEC", "HYD"])
               & (dt.start_at >= pd.Timestamp("2026-10-01", tz="Asia/Jerusalem"))]
    say(f"- machine stops on those machines inside the sensor window: {len(fails)} "
        f"({', '.join(fails.machine + ' ' + fails.start_at.dt.strftime('%d %b') + ' ' + fails.reason_code)})")
    run = s[s.status == "RUN"]
    for m, d in run.groupby("machine"):
        top = d.motor_vib_mm_s.value_counts()
        say(f"- {m}: vibration value {top.index[0]} repeated in {top.iloc[0]} RUN hours"
            + (" (flat line: stuck channel)" if top.iloc[0] > 100 else ""))
    k22 = run[run.machine == "K22"].set_index("t").motor_vib_mm_s
    over = k22[k22 > 4.5]
    if len(over):
        say(f"- K22 first RUN hour above the maker's 4.5 mm/s yellow threshold: {over.index[0]} "
            f"({(pd.Timestamp('2026-12-02 01:10', tz='UTC') - over.index[0]).days} days before the 2 December pump failure)")


def verdicts() -> None:
    say("\n## 6. Verdict per dataset and use\n")
    say("| Dataset | Predictive maintenance (train/test a model) | Pareto, PM planning, CAPA | Manual assistant |\n|---|---|---|---|")
    say("| Plant K work orders | Not yet: labels too few, durations not measurable | Usable after back-coding (component class) | Not needed |")
    say("| Plant G log | Not yet: no codes, 'ready' ≠ restart, hall numbers | Usable after crosswalk | Not needed |")
    say("| ProdTrack downtime | Not yet: reason chosen by operator, no WO link | Usable now (with the WAIT_TECH caveat) | Not needed |")
    say("| Sensors K21–K23 | Not yet: 3 machines, 3 months, 1 failure, a stuck channel | Usable now for a threshold alarm | Not needed |")
    say("| Plant G SCADA alarms | Not yet: UTC and month-first, hall numbers | Usable after conversion | Not needed |")
    say("| Parts list on the drive | Not usable: replace with the ERP | Not usable | Must be excluded |")
    say("| Manuals and SOPs on the drive | — | — | Usable after curation (current revisions, approved translations) |")


def llm_sample(bd: pd.DataFrame, n: int) -> None:
    from fieldkit.cost import token_cost
    from fieldkit.llm import complete
    codes = pd.read_csv(ROOM / "maintenance" / "failure-codes.csv", dtype=str)
    menu = "\n".join(f"{r.code}: {r.description_en}" for r in codes.itertuples())
    sample = bd[~bd.coded].sample(n=min(n, int((~bd.coded).sum())), random_state=13)
    system = ("You code maintenance work orders from an injection-moulding plant. Text may be Hebrew, Arabic, "
              "Russian or English. Choose the single best code from the list, or UNKNOWN if the text does not say "
              "what failed. Never guess a code from the machine type alone. Reply with JSON: "
              '{"code": "...", "confidence": "high|low", "reason": "..."}')
    agree = unknown = tin = tout = 0
    rule_to_code = {"pump": "H01", "valve": "H02", "hydraulic leak": "H03", "oil temperature": "H04", "heater": "E01",
                    "thermocouple": "E02", "contactor/power": "E03", "drive": "E04", "screw/check ring": "M01",
                    "toggle/clamp": "M02", "machine ejector": "M03", "safety gate": "S01", "robot": "R01",
                    "hot runner": "92", "mould water": "92", "mould pin/damage": "92", "dryer/material": "A01"}
    model = None
    for _, row in sample.iterrows():
        prompt = f"Codes:\n{menu}\n\nProblem: {row.problem_text}\nAction: {row.action_text}"
        reply = complete(prompt, system=system, max_tokens=200)
        model = reply.model
        tin += reply.input_tokens
        tout += reply.output_tokens
        try:
            got = json.loads(re.search(r"\{.*\}", reply.text, re.S).group(0)).get("code", "UNKNOWN")
        except (AttributeError, ValueError):
            got = "UNKNOWN"
        unknown += got == "UNKNOWN"
        rule = rule_to_code.get(classify(f"{row.problem_text} {row.action_text}"), "UNKNOWN")
        agree += got == rule
    say(f"\n## 7. LLM coding of {len(sample)} uncoded work orders ({model})\n")
    say(f"- agrees with the keyword class: {pct(agree, len(sample))}; UNKNOWN: {pct(unknown, len(sample))}")
    try:
        say(f"- tokens in/out {tin}/{tout}; cost US${token_cost(tin, tout, model):.4f}")
    except KeyError:
        say(f"- tokens in/out {tin}/{tout} (no price for {model} in fieldkit.cost.PRICES)")
    say("- The LLM can read four languages and abbreviations; it cannot recover what nobody wrote down. "
        "Check a sample by hand with the maintenance manager before any count is used.")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--llm", type=int, default=0, help="code N uncoded work orders with an LLM")
    ap.add_argument("--out", help="also write the report to this markdown file")
    a = ap.parse_args()
    say("# Data-readiness audit — Kinneret Plastics maintenance records (2026 exports)")
    dt = load(ROOM / "production" / "downtime-events-2026.csv")
    wo = load(ROOM / "maintenance" / "work-orders-plant-k-2026.csv")
    g = pd.read_csv(ROOM / "maintenance" / "maintenance-log-plant-g-2026.csv", dtype=str, keep_default_na=False)
    bd = labels(dt, wo)
    backcode(bd, g)
    clocks(dt)
    assets(dt, wo, g)
    sensors(dt)
    verdicts()
    if a.llm:
        llm_sample(bd, a.llm)
    if a.out:
        Path(a.out).write_text("\n".join(OUT) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
