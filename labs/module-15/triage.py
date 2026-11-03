"""Portfolio triage of Crescent Bank's pilot register (lesson 15.5), Track B.

    python triage.py                      # rules only, no AI; writes out/triage.csv
    python triage.py --llm                # + ask an LLM whether same-pattern pairs are the same task
    python triage.py --slots 3 --templates-factor 1.5

Steps, with every rule written down so the triage can be re-run each quarter on a new register:
1. Clean: one row per build (rows sharing an environment and a test set are one build; keep the row
   that went to the Model Committee).
2. Tier every build with the tier rule (lesson 15.4) from what it decides, its data and its review.
3. Record the issues: latest eval against its own threshold, owner, users, open compliance questions.
4. Cluster: the same task on the same kind of data in two units is a duplicate (merge); the same
   pattern on different content is a paved-road candidate (reuse, do not merge).
5. Decide an action per build and compute the central review load under four designs.
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))
import pandas as pd  # noqa: E402

HERE = Path(__file__).resolve().parent
ROOM = HERE / "data-room"

HIGH_AREAS = {"credit", "fraud", "aml", "hiring", "investment advice", "valuation", "market abuse", "liquidity"}
PERSONAL = {"Customer-PII", "Employee-PII", "Confidential", "Restricted"}
LOWER_IS_BETTER = ("false-accept", "factual errors", "false-negative", "mape")
# task families: the same family in two units is a candidate duplicate
FAMILIES = {
    "complaint summaries": (r"complain|תלונ", r"summar|סיכום"),
    "credit memo drafting": (r"credit memo|בקשת אשראי", r""),
    "KYC document checks": (r"kyc|הכר את הלקוח", r""),
    "conversation summaries": (r"call|chat|שיח|צ'אט", r"summar|סיכום"),
}
PATTERNS = {
    "Q&A over documents": r"faq|knowledge|procedure|questions|שאלות",
    "drafting": r"draft|letter|טיוטה|טיוטת|commentary|brief",
    "summarisation": r"summar|סיכום",
    "extraction and matching": r"extract|חילוץ|check|בדיק|match",
    "scoring and ranking": r"score|rank|forecast|triage|warning|uplift|sampling|approv|cause|דירוג|תחזית",
    "search": r"search",
}
# sim-style review effort in slots: full validation 2 per model; by tier 0.5 / 1 / 2
EFFORT = {"full": {"low": 2, "medium": 2, "high": 2}, "tiered": {"low": 0.5, "medium": 1, "high": 2}}


def read(rel):
    return pd.read_csv(ROOM / rel, dtype=str, keep_default_na=False)


def tier(r) -> str:
    if r.decision_area in HIGH_AREAS and r.decision_use != "assist":
        return "high"
    if r.data_class in PERSONAL and (r.human_review != "every output"
                                      or r.decision_use in ("informs", "decides", "answers customers")):
        return "medium"
    return "low"


def latest_eval(ev: pd.DataFrame) -> dict:
    out = {}
    for pid, g in ev.sort_values("run_date").groupby("pilot_id"):
        r = g.iloc[-1]
        ok = None
        if r.value and r.threshold:
            v, t = float(r.value), float(r.threshold)
            ok = v <= t if any(k in r.metric.lower() for k in LOWER_IS_BETTER) else v >= t
        out[pid] = (r.metric, r.value, r.threshold, ok)
    return out


def family(text: str) -> str:
    t = text.lower()
    for name, (a, b) in FAMILIES.items():
        if re.search(a, t) and (not b or re.search(b, t)):
            return name
    return ""


def pattern(text: str) -> str:
    t = text.lower()
    return next((n for n, rx in PATTERNS.items() if re.search(rx, t)), "other")


def triage(llm: bool) -> pd.DataFrame:
    reg = read("ai/pilot-register-2026-12.csv")
    left = set(read("people/staff-directory-extract.csv").query("status == 'left'").name)
    ev = latest_eval(read("ai/eval-summaries.csv"))
    reg["budget"] = reg.budget_2027_ils.astype(float)
    # 1. one row per build
    reg["copy_of"] = ""
    for (_, ts), g in reg[reg.test_set != ""].groupby(["environment", "test_set"]):
        if len(g) > 1:
            keep = g[g.submitted_to_model_committee != ""].pilot_id.iloc[0]
            for i in g.index:
                if reg.at[i, "pilot_id"] != keep:
                    reg.at[i, "copy_of"] = keep
    # 2-3. tier and evidence
    reg["tier"] = reg.apply(tier, axis=1)
    reg["eval_ok"] = reg.pilot_id.map(lambda p: ev.get(p, (None, None, None, None))[3])
    reg["issues"] = ""
    for i, r in reg.iterrows():
        f = []
        if r.eval_ok is False:
            m, v, t, _ = ev[r.pilot_id]
            f.append(f"eval below threshold ({m} {v} vs {t})")
        if r.business_owner in left:
            f.append("owner has left")
        if int(r.users_in_pilot) == 0 and r.stage != "On hold" and r.customer_facing != "Y":
            f.append("no users")
        if "compliance" in r.notes.lower() and "open" in r.notes.lower():
            f.append("open compliance question")
        if "rules engine" in r.notes.lower():
            f.append("a rules engine already does it")
        if not r.test_set and int(r.users_in_pilot) <= 2:
            f.append("no test set, almost no users")
        reg.at[i, "issues"] = "; ".join(f)
    reg["weak"] = reg.issues != ""
    # 4. clusters
    text = reg.pilot_name + " " + reg.description
    reg["family"] = text.map(family)
    reg["pattern"] = text.map(pattern)
    reg["merge_into"] = ""
    live = reg[(reg.copy_of == "") & ~reg.weak]
    for fam, g in live[live.family != ""].groupby("family"):
        if g.unit.nunique() < 2:
            continue
        # owner by evidence: passed eval, then a test set, then users
        g = g.assign(score=g.eval_ok.fillna(False).astype(int) * 100 + (g.test_set != "").astype(int) * 10
                     + g.users_in_pilot.astype(int) / 1000)
        keep = g.sort_values("score", ascending=False).pilot_id.iloc[0]
        for i in g.index:
            if reg.at[i, "pilot_id"] != keep:
                reg.at[i, "merge_into"] = keep
    if llm:
        check_pairs_with_llm(reg)
    # 5. action
    def action(r):
        if r.copy_of:
            return f"clean: same build as {r.copy_of}"
        if r.weak:
            return "stop"
        if r.merge_into:
            return f"merge into {r.merge_into}"
        if "/" in r.business_owner:
            return f"fix (one owner), then route ({r.tier})"
        if r.eval_ok is None or not r.test_set or r.baseline_measured == "N":
            return f"fix (evidence), then route ({r.tier})"
        return f"route ({r.tier})"
    reg["action"] = reg.apply(action, axis=1)
    return reg


def check_pairs_with_llm(reg: pd.DataFrame) -> None:
    from fieldkit.llm import complete
    live = reg[(reg.copy_of == "") & ~reg.weak]
    for pat, g in live.groupby("pattern"):
        rows = list(g.itertuples())
        for i, a in enumerate(rows):
            for b in rows[i + 1:]:
                if a.unit == b.unit:
                    continue
                q = (f"Two AI pilots in a bank.\nA ({a.unit}): {a.pilot_name}. {a.description}\n"
                     f"B ({b.unit}): {b.pilot_name}. {b.description}\n"
                     "Do they do the same task on the same kind of data, so one build could serve both? "
                     "Answer SAME or DIFFERENT, then one short reason.")
                ans = complete(q, max_tokens=200, system="You review AI portfolios. Be literal; same pattern is not same task.")
                print(f"[llm] {pat}: {a.pilot_id} vs {b.pilot_id}: {(ans.text.strip().splitlines() or [""])[0][:120]}")


def review_load(reg: pd.DataFrame, slots: float, tf: float) -> pd.DataFrame:
    all40 = reg[reg.copy_of == ""]
    kept = all40[all40.action.str.startswith(("route", "fix"))]
    rows = []
    for name, df, mrm, central_tiers, factor in [
        ("today: 40 builds, full validation, all to the queue", all40, "full", ("low", "medium", "high"), 1),
        ("triaged: 26 builds, full validation, all to the queue", kept, "full", ("low", "medium", "high"), 1),
        ("triaged, validation by tier, all to the queue", kept, "tiered", ("low", "medium", "high"), 1),
        ("triaged, rights by tier (only high to the queue), templates", kept, "tiered", ("high",), tf),
    ]:
        load = sum(EFFORT[mrm][t] for t in df.tier if t in central_tiers)
        rows.append([name, len(df), int((df.tier.isin(central_tiers)).sum()), load, round(load / (slots * factor), 1)])
    return pd.DataFrame(rows, columns=["design", "builds", "to central queue", "slots needed", "quarters at this capacity"])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--llm", action="store_true")
    ap.add_argument("--slots", type=float, default=3)
    ap.add_argument("--templates-factor", type=float, default=1.5)
    a = ap.parse_args()
    pd.set_option("display.width", 200)
    pd.set_option("display.max_colwidth", 70)
    reg = triage(a.llm)
    print(f"rows {len(reg)}; builds {int((reg.copy_of == '').sum())}; weak {int(reg[reg.copy_of == ''].weak.sum())}")
    print("\nTier of the 40 builds:", reg[reg.copy_of == ""].tier.value_counts().to_dict())
    print("\nActions:", reg.action.str.split(":| into| \\(").str[0].value_counts().to_dict())
    cols = ["pilot_id", "unit", "tier", "action", "issues", "budget"]
    print("\n" + reg.sort_values(["action", "pilot_id"])[cols].to_string(index=False))
    print("\nPatterns among the builds you keep (paved-road candidates):")
    kept = reg[reg.action.str.startswith(("route", "fix"))]
    print(kept.groupby("pattern").pilot_id.apply(", ".join).to_string())
    print("\nCentral review load (slots of about ten validator-days):")
    print(review_load(reg, a.slots, a.templates_factor).to_string(index=False))
    stop = reg[reg.action == "stop"].budget.sum()
    merge = reg[reg.action.str.startswith("merge")].budget.sum()
    clean = reg[reg.action.str.startswith("clean")].budget.sum()
    print(f"\n2027 unit lines released: stop ₪{stop:,.0f}; merge ₪{merge:,.0f} (before the cost of merging); "
          f"double-booked ₪{clean:,.0f}; total ₪{stop + merge + clean:,.0f}")
    out = HERE / "out"
    out.mkdir(exist_ok=True)
    reg[["pilot_id", "unit", "pilot_name", "tier", "pattern", "family", "copy_of", "merge_into", "issues",
         "action", "budget"]].to_csv(out / "triage.csv", index=False, encoding="utf-8")
    print(f"\nwritten: {out / 'triage.csv'}")


if __name__ == "__main__":
    main()
