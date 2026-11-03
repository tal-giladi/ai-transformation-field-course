"""Precedent search over the research corpus, scored on 48 questions (Track B, lesson 12.5).

    python search.py                          # BM25 over all 78 documents, as the KM bank holds them
    python search.py --curated                # only documents still current after the curation sprint
    python search.py --curated --prefix       # + strip one Hebrew prefix letter (ו ה ב ל מ ש כ)
    python search.py --curated --answer       # + ask the LLM to answer from the top 5, with citations

No AI is needed for retrieval: it is plain keyword ranking, free and exact. `--answer` writes one draft
per question to runs/answers-<model>/ in the same format as drafts/, so verify_citations.py can check it.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from corpus_lib import BM25, HERE, load_corpus, read_csv, statuses

sys.path.insert(0, str(HERE.parents[1] / "common"))

SYSTEM = (HERE / "system-prompt.md").read_text(encoding="utf-8").split("```text\n", 1)[1].split("```", 1)[0]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--curated", action="store_true", help="drop documents the curation sprint marked superseded")
    ap.add_argument("--prefix", action="store_true", help="strip one Hebrew prefix letter when tokenising")
    ap.add_argument("--answer", action="store_true", help="draft an answer per question with the LLM")
    ap.add_argument("--k", type=int, default=5)
    args = ap.parse_args()

    corpus = load_corpus()
    status = statuses(curated=args.curated)
    if args.curated:
        corpus = {i: d for i, d in corpus.items() if status.get(i) == "current"}
    engine = BM25({i: d["text"] for i, d in corpus.items()}, strip_prefix=args.prefix)
    questions = read_csv(HERE / "questions.csv")
    mode = ("curated" if args.curated else "raw") + ("-prefix" if args.prefix else "")
    rows = []
    for q in questions:
        hits = engine.search(q["question"], k=args.k)
        top = [h[0] for h in hits]
        gold = q["gold_docs"].split(";")
        stale = [s for s in q["stale_docs"].split(";") if s]
        rows.append({"question_id": q["question_id"], "language": q["language"], "top": ";".join(top),
                     "gold_in_top5": int(any(g in top[:5] for g in gold)),
                     "gold_recall5": round(sum(g in top[:5] for g in gold) / len(gold), 3),
                     "first_is_gold": int(top[0] in gold),
                     "stale_in_top3": "" if not stale else int(any(s in top[:3] for s in stale))})
    out = HERE / "runs" / f"search-{mode}.csv"
    out.parent.mkdir(exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as f:
        f.write(",".join(rows[0]) + "\n")
        for r in rows:
            f.write(",".join(str(v) for v in r.values()) + "\n")

    lines = [f"# Search report: {mode}", "", f"Documents searched: {len(corpus)}. Questions: {len(rows)}.", "",
             "| Language | n | Gold in top 5 | Mean gold recall@5 | Top result is gold | Stale doc in top 3 (P3 questions) |",
             "|---|---|---|---|---|---|"]
    for lang in ("en", "he", "all"):
        sel = [r for r in rows if lang == "all" or r["language"] == lang]
        st = [r for r in sel if r["stale_in_top3"] != ""]
        lines.append(f"| {lang} | {len(sel)} | {sum(r['gold_in_top5'] for r in sel)} of {len(sel)} | "
                     f"{100 * sum(r['gold_recall5'] for r in sel) / len(sel):.1f}% | "
                     f"{sum(r['first_is_gold'] for r in sel)} of {len(sel)} | "
                     f"{sum(r['stale_in_top3'] for r in st)} of {len(st)} |")
    report = "\n".join(lines) + "\n"
    (HERE / "reports").mkdir(exist_ok=True)
    (HERE / "reports" / f"search-{mode}.md").write_text(report, encoding="utf-8")
    print(report)

    if args.answer:
        from fieldkit.llm import complete
        model_dir = None
        for q, r in zip(questions, rows):
            ctx = "\n\n".join(f"=== {i} ===\n" + "\n".join(f"¶{n} {t}" for n, t in corpus[i]["paras"].items())
                              for i in r["top"].split(";"))
            reply = complete(f"Documents:\n{ctx}\n\nQuestion ({q['language']}): {q['question']}", system=SYSTEM)
            model_dir = model_dir or HERE / "runs" / f"answers-{mode}-{reply.model}"
            model_dir.mkdir(parents=True, exist_ok=True)
            lang = "Hebrew" if q["language"] == "he" else "English"
            (model_dir / f"{q['question_id']}.md").write_text(
                f"# Answer {q['question_id']}\n\n| Field | Value |\n|---|---|\n| Language | {lang} |\n\n"
                f"**Question:** {q['question']}\n\n**Answer**\n\n{reply.text.strip()}\n", encoding="utf-8")
        print(f"Answers written to {model_dir}. Check them: python verify_citations.py --drafts {model_dir}")


if __name__ == "__main__":
    main()
