"""Run the permit-FAQ pilot over a question set (lesson 11.5).

    python run_faq.py --mode search --corpus site --set test     # no AI: the website's search, top page
    python run_faq.py --mode search --corpus pack --set test     # no AI: search over the approved pack
    python run_faq.py --mode rag --corpus site --set dev --limit 10   # LLM over the website as it is
    python run_faq.py --mode rag --corpus pack --set test        # LLM over the approved pack (the design)
    python run_faq.py --mode rag --corpus pack --set negative

Writes runs/<mode>-<corpus>-<set>[-<model>].csv. Score it with score_faq.py.
The "search" mode needs only the standard library. The "rag" mode calls your LLM through
fieldkit.llm (FIELDKIT_PROVIDER, FIELDKIT_MODEL and your provider's key variable; "mock" runs free).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

from faq_lib import HERE, Search, load_corpus, read_csv, write_csv

COLS = ["question_id", "behaviour", "answer", "sources", "language", "tokens_in", "tokens_out", "error"]


def question_set(name: str) -> list[dict]:
    if name == "negative":
        rows = read_csv(HERE / "negative-tests.csv")
        for r in rows:
            r["question_id"] = r["test_id"]
        return rows
    rows = read_csv(HERE / "test-set.csv")
    if name == "track-a":
        ids = {r["question_id"] for r in read_csv(HERE / "track-a-80.csv")}
        return [r for r in rows if r["question_id"] in ids]
    return rows if name == "all" else [r for r in rows if r["split"] == name]


def system_prompt() -> str:
    text = (HERE / "system-prompt.md").read_text(encoding="utf-8")
    return re.search(r"```text\n(.*?)```", text, re.S).group(1)


def parse_json(text: str) -> dict:
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        return {"behaviour": "", "answer": text, "sources": [], "language": ""}
    try:
        return json.loads(m.group())
    except json.JSONDecodeError:
        return {"behaviour": "", "answer": text, "sources": [], "language": ""}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--mode", choices=["search", "rag"], required=True)
    ap.add_argument("--corpus", choices=["site", "pack"], required=True)
    ap.add_argument("--set", default="dev", choices=["dev", "test", "all", "negative", "track-a"])
    ap.add_argument("--k", type=int, default=4, help="documents retrieved for the LLM (rag mode)")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    docs = load_corpus(args.corpus)
    search = Search(docs)
    items = question_set(args.set)
    if args.limit:
        items = items[: args.limit]
    out, suffix = [], ""
    if args.mode == "rag":
        sys.path.insert(0, str(HERE.parents[1] / "common"))
        from fieldkit.llm import complete  # noqa: E402
        system = system_prompt()
        suffix = "-" + (os.environ.get("FIELDKIT_MODEL") or os.environ.get("FIELDKIT_PROVIDER") or "anthropic")
    for it in items:
        row = {"question_id": it["question_id"], "tokens_in": 0, "tokens_out": 0, "error": ""}
        hits = search.top(it["question"], k=args.k if args.mode == "rag" else 1)
        if args.mode == "search":
            # What a site search box gives a resident: the top page, whatever it says. It cannot refuse.
            score, doc = hits[0]
            row.update(behaviour="answer", answer=doc["body"] if score > 0 else "",
                       sources=doc["doc_id"] if score > 0 else "", language=doc["language"] if score > 0 else "")
        else:
            context = "\n\n".join(f"<document doc_id=\"{d['doc_id']}\">\n{d['body']}\n</document>" for _, d in hits)
            prompt = f"DOCUMENTS:\n{context}\n\nQUESTION:\n{it['question']}"
            try:
                reply = complete(prompt, system=system, max_tokens=800)
                data = parse_json(reply.text)
                src = data.get("sources") or []
                row.update(behaviour=str(data.get("behaviour", "")), answer=str(data.get("answer", "")),
                           sources=";".join(src) if isinstance(src, list) else str(src),
                           language=str(data.get("language", "")), tokens_in=reply.input_tokens,
                           tokens_out=reply.output_tokens)
            except Exception as exc:  # a failure is a result: keep it and go on
                row.update(behaviour="", answer="", sources="", language="", error=f"{type(exc).__name__}: {exc}")
        out.append(row)
    path = HERE / "runs" / f"{args.mode}-{args.corpus}-{args.set}{suffix}.csv"
    write_csv(path, out, COLS)
    print(f"{len(out)} questions -> {path.relative_to(HERE)}")


if __name__ == "__main__":
    main()
