"""Citation verification gate for research answers (Track B, lesson 12.5).

    python verify_citations.py                         # the 40 test drafts, rules only, KM status as it was
    python verify_citations.py --curated               # status from the December curation sprint
    python verify_citations.py --curated --support overlap   # + a crude keyword "support" check
    python verify_citations.py --curated --support llm # + an LLM judge for "does it say that?"
    python verify_citations.py --drafts runs/answers-curated-<model>   # check your own assistant's answers

Five checks per citation: the document exists; the paragraph exists; a quote, if any, is verbatim; the
document is current; the paragraph supports the claim. The first four are rules (free, exact). The
fifth is skipped by default (a person does it), or keyword overlap (crude, no AI), or an LLM judge through fieldkit.llm (illustrative:
your numbers depend on the model). On the test drafts the script scores itself against
citation-labels.csv.
"""
from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

from corpus_lib import HERE, lang_part, load_corpus, overlap, parse_draft, read_csv, statuses

sys.path.insert(0, str(HERE.parents[1] / "common"))

JUDGE = ("You check legal research citations. Reply with exactly one word: SUPPORTS if the paragraph states "
         "what the claim says, or NO if it does not, says something different, or says the opposite.")


def check(c: dict, corpus: dict, status: dict, support: str, threshold: float) -> dict:
    doc = corpus.get(c["cited_id"])
    res = {"exists": "y" if doc else "n", "pinpoint_ok": "na", "quote_ok": "na", "current": "na", "supports": "na"}
    if doc:
        para = doc["paras"].get(c["pinpoint"])
        res["pinpoint_ok"] = "y" if para else "n"
        res["current"] = "y" if status.get(c["cited_id"], "current") == "current" else "n"
        if para:
            text = lang_part(para, c["language"])
            if c["quote"]:
                res["quote_ok"] = "y" if " ".join(c["quote"].split()) in " ".join(para.split()) else "n"
            if support == "none":
                pass
            elif support == "llm":
                from fieldkit.llm import complete
                reply = complete(f"Paragraph:\n{para}\n\nClaim:\n{c['claim']}", system=JUDGE, max_tokens=5)
                res["supports"] = "y" if "SUPPORT" in reply.text.upper() else "n"
            else:
                res["overlap"] = overlap(c["claim"], text)
                res["supports"] = "y" if res["overlap"] >= threshold else "n"
    fails = [k for k in ("exists", "pinpoint_ok", "quote_ok", "current", "supports") if res[k] == "n"]
    res["verdict"] = "fail" if fails else "pass"
    res["reasons"] = ";".join(fails)
    return res


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--drafts", default=str(HERE / "drafts"))
    ap.add_argument("--curated", action="store_true", help="use the curation sprint's status, not the KM index")
    ap.add_argument("--support", choices=["none", "overlap", "llm"], default="none")
    ap.add_argument("--threshold", type=float, default=0.6, help="overlap share needed to count as support")
    args = ap.parse_args()

    corpus = load_corpus()
    status = statuses(curated=args.curated)
    rows = []
    for path in sorted(Path(args.drafts).glob("*.md")):
        for c in parse_draft(path):
            rows.append({"draft_id": path.stem, **c, **check(c, corpus, status, args.support, args.threshold)})
    mode = ("curated" if args.curated else "km-status") + f"-{args.support}"
    name = Path(args.drafts).name
    out = HERE / "runs" / f"verify-{name}-{mode}.csv"
    out.parent.mkdir(exist_ok=True)
    keys = ["draft_id", "no", "language", "cited_id", "pinpoint", "exists", "pinpoint_ok", "quote_ok", "current",
            "supports", "overlap", "verdict", "reasons"]
    with out.open("w", encoding="utf-8", newline="") as f:
        f.write(",".join(keys) + "\n")
        for r in rows:
            f.write(",".join(str(r.get(k, "")) for k in keys) + "\n")
    lines = [f"# Citation check: {name}, {mode}", "", f"Citations checked: {len(rows)}; failed the gate: "
             f"{sum(r['verdict'] == 'fail' for r in rows)}.", ""]
    labels_path = HERE / "citation-labels.csv"
    if name == "drafts" and labels_path.exists():
        lab = {(r["draft_id"], int(r["citation_no"])): r for r in read_csv(labels_path)}
        by = Counter()
        caught = Counter()
        for r in rows:
            L = lab[(r["draft_id"], r["no"])]
            by[(L["label"], L["source"])] += 1
            if r["verdict"] == "fail":
                caught[(L["label"], L["source"])] += 1
        lines += ["| True label | General assistant: caught | Parshan PoC: caught | Total caught |", "|---|---|---|---|"]
        for label in ("nonexistent", "bad_pinpoint", "bad_quote", "superseded", "misstated", "ok"):
            cells = []
            for src in ("general_assistant", "parshan_poc"):
                n = by[(label, src)]
                cells.append(f"{caught[(label, src)]} of {n}" if n else "—")
            tot = sum(by[(label, s)] for s in ("general_assistant", "parshan_poc"))
            tc = sum(caught[(label, s)] for s in ("general_assistant", "parshan_poc"))
            name_l = "ok (a catch here is a false alarm)" if label == "ok" else label
            lines.append(f"| {name_l} | {cells[0]} | {cells[1]} | {tc} of {tot} |")
        bad = [r for r in rows if lab[(r["draft_id"], r["no"])]["label"] != "ok"]
        good = [r for r in rows if lab[(r["draft_id"], r["no"])]["label"] == "ok"]
        missed = sum(r["verdict"] == "pass" for r in bad)
        lines += ["", f"Bad citations: {len(bad)}; caught {len(bad) - missed} "
                  f"({100 * (len(bad) - missed) / len(bad):.1f}%); missed {missed}.",
                  f"Good citations: {len(good)}; false alarms {sum(r['verdict'] == 'fail' for r in good)}.",
                  "", "Bad citations by source: " + ", ".join(
                      f"{s} {sum(1 for r in bad if lab[(r['draft_id'], r['no'])]['source'] == s)} of "
                      f"{sum(1 for r in rows if lab[(r['draft_id'], r['no'])]['source'] == s)}"
                      for s in ("general_assistant", "parshan_poc")) + "."]
    report = "\n".join(lines) + "\n"
    (HERE / "reports").mkdir(exist_ok=True)
    (HERE / "reports" / f"verify-{name}-{mode}.md").write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
