"""Lessons 10.2 and 10.3 (Track B): the discovery numbers from Galil Health's data room, the same way every time.

    python discovery.py

Prints:
  - the visit-language mix two ways (Notara's "visit language" field vs the appointment system's preferred language);
  - language match between doctor and patient, who interprets, and what a mismatch does to documentation time;
  - documentation minutes per doctor-day (note time from the 8% visit sample x full visit counts) vs the survey;
  - notes signed within 24 hours, by language match;
  - shadow-AI signals (survey tools and comments, firewall summary);
  - the 2025 dictation trial week by week and the documentation incidents;
  - the steering group's demo-day scores, weighted.
No network, no API key.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "common"))

import pandas as pd

from fieldkit.data import data_room, load

room = data_room("module-10")
v = load(room / "notara" / "visits-sample.csv")
dd = load(room / "notara" / "doctor-days.csv")
cl = load(room / "people" / "clinicians.csv")
sv = load(room / "people" / "clinician-survey-2026-10.csv")
px = load(room / "it" / "proxy-ai-summary-2026-10.csv")
tr = load(room / "notara" / "mednote-dictation-trial-2025.csv")
inc = load(room / "quality" / "patient-safety-incidents.csv")
sc = load(room / "vendors" / "demo-day-scorecards.csv")


def share(s: pd.Series) -> str:
    return ", ".join(f"{k} {100 * x:.1f}%" for k, x in s.value_counts(normalize=True).items())


print(f"== Visits in the sample: {len(v):,} (an 8% random sample of doctor visits, 1 Sep - 31 Oct 2026)")
print("Notara 'visit_language':       ", share(v["visit_language"]))
print("Appointment 'patient_pref_language':", share(v["patient_pref_language"]))

# Language match: does the doctor speak the patient's preferred language?
langs = cl.set_index("clinician_id")["languages"].str.split(";")
v["doctor_speaks"] = [p in langs[c] for p, c in zip(v["patient_pref_language"], v["clinician_id"])]
mm = v[~v["doctor_speaks"]]
print(f"\n== Language mismatch: {len(mm):,} of {len(v):,} visits ({100 * len(mm) / len(v):.1f}%)")
print("Interpreter in mismatch visits:", share(mm["interpreter"].fillna("(blank)")))
print("relative_present field blank:", f"{100 * v['relative_present'].isna().mean():.1f}%")

v["note_min"] = v["note_active_sec"] / 60
v["after_min"] = v["after_hours_sec"] / 60
grp = v.assign(group=v["doctor_speaks"].map({True: "doctor speaks the language", False: "mismatch"}))
print("\n== Documentation per visit by language match (minutes)")
print(grp.groupby("group").agg(visits=("visit_id", "size"), note_median=("note_min", "median"),
                               note_mean=("note_min", "mean"), after_hours_share=("after_hours_sec", lambda s: (s > 0).mean()),
                               after_mean=("after_min", "mean")).round(2).to_string())
print("\nNote minutes (median) by preferred language, doctor speaks it:")
print(v[v["doctor_speaks"]].groupby("patient_pref_language")["note_min"].median().round(2).to_string())

# Documentation per doctor-day: mean minutes per visit (in hours + after hours) x visits that day.
per_doc = v.groupby("clinician_id").agg(note=("note_min", "mean"), after=("after_min", "mean"))
dd2 = dd.join(per_doc, on="clinician_id")
dd2["doc_minutes"] = dd2["visits"] * (dd2["note"] + dd2["after"])
dd2["after_minutes"] = dd2["visits"] * dd2["after"]
print("\n== Documentation minutes per doctor-day (estimate)")
print(f"Visits per doctor-day: median {dd['visits'].median():.0f}, mean {dd['visits'].mean():.1f}; doctor-days {len(dd):,}")
print(f"Documentation per doctor-day: median {dd2['doc_minutes'].median():.0f} min, p75 {dd2['doc_minutes'].quantile(.75):.0f}, "
      f"of which after hours: median {dd2['after_minutes'].median():.0f} min")
print(f"Per visit overall: note median {v['note_min'].median():.2f} min, mean {v['note_min'].mean():.2f}; "
      f"after-hours share {100 * (v['after_hours_sec'] > 0).mean():.1f}%")
docs = sv[sv["role"] == "doctor"]
print(f"Survey (self-reported, doctors n={len(docs)}): median {docs['documentation_minutes_per_day'].median():.0f} min a day; "
      f"evenings finishing notes median {docs['evenings_finishing_notes_per_week'].median():.0f} a week")
nur = sv[sv["role"] == "nurse"]
print(f"Survey nurses n={len(nur)}: interpreting minutes a day median {nur['interpreting_minutes_per_day'].median():.0f}")
print(f"Survey response: {len(sv)} of {len(cl)} clinicians ({len(docs)} of {(cl['role'] == 'doctor').sum()} doctors)")

v["signed_24h"] = (v["note_signed_at"] - v["note_opened_at"]) <= pd.Timedelta(hours=24)
print("\n== Notes signed within 24 hours:", f"{100 * v['signed_24h'].mean():.1f}%",
      "| match", f"{100 * v[v['doctor_speaks']]['signed_24h'].mean():.1f}%",
      "| mismatch", f"{100 * v[~v['doctor_speaks']]['signed_24h'].mean():.1f}%")

print("\n== Shadow-AI signals")
print("Survey 'tools_used_for_notes':", sv["tools_used_for_notes"].value_counts().to_dict())
pat = re.compile(r"טלפון|אפליקציה|GPT|телефон|приложени|ИИ|تطبيق|هاتف|app|phone", re.I)
hits = sv[sv["comment"].fillna("").str.contains(pat)]
print(f"Comments mentioning a phone, an app or an AI tool: {len(hits)}")
stt = px[px["category"] == "AI audio transcription"]
print("Consumer speech-to-text on guest Wi-Fi, upload MB over 4 weeks by clinic:")
print(stt.groupby("clinic_id")["upload_mb"].sum().sort_values(ascending=False).round(0).to_string())
print("Clinics with ChatGPT on the clinic network:", sorted(px[px["application"] == "ChatGPT"]["clinic_id"].unique()))

print("\n== 2025 MedNote dictation trial: doctors dictating at least 10% of their visits, by week")
tr["user"] = tr["notes_dictated"] >= 0.1 * tr["visits"]
print(tr.groupby("trial_week")["user"].sum().to_string())
print("\nDocumentation incidents:")
print(inc[inc["category"] == "documentation"][["incident_id", "reported_date", "clinic_id", "severity", "description_en"]].to_string(index=False))

print("\n== Demo-day scores (mean of 9 raters; weights 2/3/3/2/1/2)")
W = {"evidence": 2, "safety": 3, "privacy": 3, "languages": 2, "integration": 1, "contract": 2}
m = sc.pivot_table(index="vendor", columns="criterion", values="score_1to5", aggfunc="mean")
m["weighted"] = sum(m[c].round(0) * w for c, w in W.items()) / sum(W.values())
print(m.round(2).sort_values("weighted", ascending=False).to_string())
print("(weighted uses each criterion's mean rounded to the nearest whole score, as the steering group recorded them)")
