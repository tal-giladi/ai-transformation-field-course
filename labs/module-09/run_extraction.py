"""Meridian Mutual: run your extraction pilot over the intake documents (lesson 09.5, Track B).

    python run_extraction.py --split dev            # the 40 development documents (iterate here)
    python run_extraction.py --split test           # the 200 test documents, once, with your final prompt
    python run_extraction.py --split all --limit 10 # a quick look
    python run_extraction.py --negative             # the 12 negative tests in pilot/negative-tests.csv

The provider and model come from FIELDKIT_PROVIDER / FIELDKIT_MODEL (see labs/common/README.md);
FIELDKIT_PROVIDER=mock runs the pipeline for free and returns nothing useful. Replies are cached,
so a re-run with the same prompt and model costs nothing. Writes runs/llm-<model>-<split>.csv in
the format score_extraction.py reads, plus a token and cost line per document.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))
sys.stdout.reconfigure(encoding="utf-8")

from fieldkit.cost import PRICES, token_cost  # noqa: E402
from fieldkit.data import data_room  # noqa: E402
from fieldkit.llm import complete  # noqa: E402

HERE = Path(__file__).resolve().parent
ROOM = data_room("module-09") / "extraction"
FIELDS = {
    "claim_form": ["policy_number", "loss_date", "claimed_amount", "vehicle_plate", "currency"],
    "garage_invoice": ["invoice_number", "invoice_date", "total_amount", "vat_amount"],
    "contractor_invoice": ["invoice_number", "invoice_date", "total_amount", "vat_amount"],
    "police_confirmation": ["report_number", "event_date"],
    "assessor_report": ["inspection_date", "assessed_amount"],
    "medical_invoice_abroad": ["service_date", "total_amount", "currency"],
    "health_receipt": ["receipt_number", "service_date", "total_amount"],
}
HINTS = {
    "vehicle_plate": "only on motor claim forms",
    "currency": "only if the document states an amount in a foreign currency",
    "loss_date": "the date of the event, not the signature date",
    "event_date": "the date of the event, not the date the complaint was filed",
    "inspection_date": "the date the assessor inspected the vehicle",
}


def system_prompt() -> str:
    text = (HERE / "pilot" / "system-prompt.md").read_text(encoding="utf-8")
    return text.split("\n---\n")[1].strip()


def split_ids(split: str) -> list[str]:
    with open(HERE / "pilot" / "splits.csv", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return [r["doc_id"] for r in rows if split == "all" or r["split"] == split]


def ask(doc_type: str, text: str) -> str:
    wanted = ", ".join(f"{f} ({HINTS[f]})" if f in HINTS else f for f in FIELDS[doc_type])
    return (f"Document type: {doc_type}\nFields: {wanted}\n\n"
            f"<document>\n{text}\n</document>\n\nReturn one JSON object with exactly these keys.")


def parse(reply: str) -> dict:
    m = re.search(r"\{.*\}", reply, re.S)
    if not m:
        return {}
    try:
        data = json.loads(m.group(0))
    except json.JSONDecodeError:
        return {}
    return data if isinstance(data, dict) else {}


def check_negative(extract) -> None:
    """Run every negative test with extract(doc_type, text) -> dict and print pass/fail."""
    with open(HERE / "pilot" / "negative-tests.csv", encoding="utf-8") as f:
        tests = list(csv.DictReader(f))
    cache: dict[str, dict] = {}
    passed = 0
    for t in tests:
        if t["file"] not in cache:
            cache[t["file"]] = extract(t["doc_type"], (HERE / "pilot" / t["file"]).read_text(encoding="utf-8"))
        out = {k: v for k, v in cache[t["file"]].items() if v not in (None, "", "null")}
        allowed = set(FIELDS[t["doc_type"]])
        if t["field"] == "(any extra field)":
            extra = sorted(set(out) - allowed)
            ok = not extra
            got = ", ".join(extra) or "none"
        else:
            got = out.get(t["field"])
            exp = t["expected"]
            if exp == "null":
                ok = got is None
            elif not t["field"].endswith("_amount"):
                ok = str(got).strip() == exp      # dates and identifiers: exact, Western digits
            else:
                try:
                    ok = got is not None and f"{float(str(got).replace(',', '')):.2f}" == f"{float(exp):.2f}"
                except ValueError:
                    ok = str(got).strip() == exp
        passed += ok
        print(f"{t['test_id']} {t['field']:18s} expected {t['expected']:12s} got {str(got):14s} {'PASS' if ok else 'FAIL'}")
    print(f"negative tests passed: {passed} of {len(tests)}")


def llm_extract(doc_type: str, text: str) -> dict:
    return parse(complete(ask(doc_type, text), system=system_prompt(), max_tokens=300).text)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", default="dev", choices=["dev", "test", "all"])
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--negative", action="store_true")
    a = ap.parse_args()
    if a.negative:
        check_negative(llm_extract)
        return
    model = os.environ.get("FIELDKIT_MODEL") or ("mock" if os.environ.get("FIELDKIT_PROVIDER") == "mock" else "claude-opus-5-5")
    ids = split_ids(a.split)
    with open(ROOM / "documents_index.csv", encoding="utf-8") as f:
        index = {r["doc_id"]: r for r in csv.DictReader(f)}
    if a.limit:
        ids = ids[: a.limit]
    sys_p = system_prompt()
    rows, usage = [], []
    for i, doc_id in enumerate(ids, 1):
        d = index[doc_id]
        text = (ROOM / d["file"]).read_text(encoding="utf-8")
        reply = complete(ask(d["doc_type"], text), system=sys_p, max_tokens=300)
        data = parse(reply.text)
        for k, v in data.items():
            if v not in (None, ""):
                rows.append([doc_id, k, str(v)])
        usage.append((doc_id, reply.input_tokens, reply.output_tokens, reply.cached))
        print(f"{i:3d}/{len(ids)} {doc_id} {d['doc_type']:22s} {d['doc_language']} -> {len(data)} fields"
              f"{' (cached)' if reply.cached else ''}")
    safe = re.sub(r"[^A-Za-z0-9.-]+", "-", model)
    out = HERE / "runs" / f"llm-{safe}-{a.split}.csv"
    out.parent.mkdir(exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["doc_id", "field", "value"])
        w.writerows(rows)
    tin = sum(u[1] for u in usage)
    tout = sum(u[2] for u in usage)
    line = f"tokens in {tin:,}, out {tout:,} for {len(usage)} documents"
    if model in PRICES:
        line += f"; list-price cost US${token_cost(tin, tout, model):.4f} (US${token_cost(tin, tout, model) / max(1, len(usage)):.5f} a document)"
    print(line)
    print(f"wrote {out.relative_to(HERE).as_posix()} -> now run: python score_extraction.py {out.relative_to(HERE).as_posix()}")


if __name__ == "__main__":
    main()
