"""Run the maintenance-manual assistant (or the no-AI search baseline) over a question set (lesson 13.5).

    python run_manual.py --mode search --corpus drive --set test    # no AI: the shared drive as it is
    python run_manual.py --mode search --corpus pack --set test     # no AI: knowledge pack v1
    python run_manual.py --mode rag --corpus pack --set dev --limit 10
    python run_manual.py --mode rag --corpus pack --set test
    python run_manual.py --mode rag --corpus pack --set negative
    python run_manual.py --mode rag --corpus drive --set test       # the "just point it at the drive" design

search: returns the best-matching passage as the answer (always behaviour "answer").
rag:    sends the system prompt v1.0 and the WHOLE corpus (it is small) with each question through
        fieldkit.llm (provider and model from FIELDKIT_PROVIDER / FIELDKIT_MODEL; cached).
Writes runs/<mode>-<corpus>-<set>[-<model>].csv.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys

from manual_lib import HERE, BM25, corpus, read_csv

sys.path.insert(0, str(HERE.parents[1] / "common"))


def system_prompt() -> str:
    text = (HERE / "system-prompt.md").read_text(encoding="utf-8")
    return re.search(r"```text\n(.*?)```", text, re.S).group(1)


def items(which: str) -> list[dict]:
    if which == "negative":
        return [{"qid": r["nid"], "language": r["language"], "question": r["prompt"]}
                for r in read_csv(HERE / "negative-tests.csv")]
    if which == "track-a":
        ids = {r["qid"] for r in read_csv(HERE / "track-a-60.csv")}
        return [r for r in read_csv(HERE / "test-set.csv") if r["qid"] in ids]
    return [r for r in read_csv(HERE / "test-set.csv") if r["split"] == which]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--mode", choices=["search", "rag"], required=True)
    ap.add_argument("--corpus", choices=["drive", "pack"], required=True)
    ap.add_argument("--set", choices=["dev", "test", "track-a", "negative"], required=True)
    ap.add_argument("--limit", type=int)
    a = ap.parse_args()
    docs = corpus(a.corpus)
    qs = items(a.set)[: a.limit] if a.limit else items(a.set)
    out, model = [], "search"
    if a.mode == "search":
        bm = BM25(docs)
        for q in qs:
            hits = bm.search(q["question"], k=1)
            if hits:
                d = hits[0][1]
                out.append([q["qid"], "answer", d["text"].replace("\n", " "), d["label"], 0, 0])
            else:
                out.append([q["qid"], "answer", "", "", 0, 0])
    else:
        from fieldkit.llm import complete
        system = system_prompt()
        knowledge = "\n\n".join(f"<document source=\"{d['label']}\" language=\"{d['lang']}\">\n{d['text']}\n</document>"
                                for d in docs)
        for q in qs:
            prompt = (f"KNOWLEDGE PACK\n{knowledge}\n\nQUESTION (id {q['qid']}):\n{q['question']}\n\n"
                      "Reply with the JSON object only.")
            reply = complete(prompt, system=system, max_tokens=600)
            model = reply.model
            try:
                obj = json.loads(re.search(r"\{.*\}", reply.text, re.S).group(0))
            except (AttributeError, ValueError):
                obj = {"behaviour": "answer", "answer": reply.text, "sources": []}
            src = obj.get("sources", [])
            out.append([q["qid"], obj.get("behaviour", "answer"), str(obj.get("answer", "")).replace("\n", " "),
                        "; ".join(src) if isinstance(src, list) else str(src), reply.input_tokens, reply.output_tokens])
            print(f"{q['qid']}: {obj.get('behaviour')}", flush=True)
    suffix = "" if a.mode == "search" else f"-{model}"
    path = HERE / "runs" / f"{a.mode}-{a.corpus}-{a.set}{suffix}.csv"
    path.parent.mkdir(exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["qid", "behaviour", "answer", "sources", "input_tokens", "output_tokens"])
        w.writerows(out)
    print(f"wrote {path.relative_to(HERE)} ({len(out)} rows)")


if __name__ == "__main__":
    main()
