"""Shared code for the maintenance-manual assistant pilot (lesson 13.5): corpora, BM25 search,
normalisation and the automatic checks. Standard library only.
"""
from __future__ import annotations

import csv
import math
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOM = HERE.parent / "data-room"


def read_csv(path: Path) -> list[dict]:
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def _chunks(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    m = re.search(r"- Document: (\S+)", text)
    rev = re.search(r"- Revision: ([^\n(]+)", text)
    lang = re.search(r"- Language: (\w+)", text)
    doc = m.group(1) if m else path.stem
    label = f"{doc} rev {rev.group(1).strip()}" if rev and doc.startswith("SOP") else doc
    parts = re.split(r"\n(?=## )", text)
    head = parts[0].splitlines()[0].lstrip("# ")
    out = []
    for p in parts[1:]:
        out.append({"doc": doc, "label": label, "lang": (lang.group(1) if lang else "?"), "file": path.name,
                    "text": f"{head}\n{p.strip()}"})
    return out


def corpus(name: str) -> list[dict]:
    """'drive' = the shared drive as it is (all revisions, the parts list); 'pack' = knowledge pack v1."""
    if name == "pack":
        files = sorted((HERE / "knowledge-pack").glob("*.md"))
        return [c for f in files for c in _chunks(f)]
    files = sorted((ROOM / "docs").glob("*.md"))
    chunks = [c for f in files for c in _chunks(f)]
    pn = 'מק"ט'
    for r in read_csv(ROOM / "parts" / "parts-list-shared-drive.csv"):
        chunks.append({"doc": "PARTS-LIST", "label": "PARTS-LIST (drive, 16 Mar 2025)", "lang": "Hebrew",
                       "file": "parts-list-shared-drive.csv",
                       "text": "רשימת חלקים: " + f"{r[pn]} {r['תיאור']} מיקום {r['מיקום']} כמות {r['כמות']}"})
    return chunks


TOKEN = re.compile(r"[\w\-\.]+", re.UNICODE)


def tokens(text: str) -> list[str]:
    return [t.strip(".").lower() for t in TOKEN.findall(text) if t.strip(".")]


class BM25:
    def __init__(self, docs: list[dict], k1: float = 1.4, b: float = 0.75):
        self.docs = docs
        self.toks = [tokens(d["text"]) for d in docs]
        self.avg = sum(len(t) for t in self.toks) / len(self.toks)
        self.df: dict[str, int] = {}
        for t in self.toks:
            for w in set(t):
                self.df[w] = self.df.get(w, 0) + 1
        self.k1, self.b, self.n = k1, b, len(docs)

    def search(self, query: str, k: int = 3) -> list[tuple[float, dict]]:
        q = tokens(query)
        scored = []
        for d, t in zip(self.docs, self.toks):
            score = 0.0
            for w in q:
                if w not in self.df:
                    continue
                f = t.count(w)
                if not f:
                    continue
                idf = math.log(1 + (self.n - self.df[w] + 0.5) / (self.df[w] + 0.5))
                score += idf * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * len(t) / self.avg))
            scored.append((score, d))
        scored.sort(key=lambda x: -x[0])
        return [x for x in scored[:k] if x[0] > 0]


def norm(text: str) -> str:
    s = (text or "").lower().replace("−", "-").replace("–", "-")
    s = re.sub(r"(?<=\d)[,\s'](?=\d{3}\b)", "", s)
    return s


def script(text: str) -> str:
    if re.search("[؀-ۿ]", text or ""):
        return "ar"
    if re.search("[Ѐ-ӿ]", text or ""):
        return "ru"
    if re.search("[֐-׿]", text or ""):
        return "he"
    return "en"


def check(item: dict, behaviour: str, answer: str, sources: str) -> dict:
    """The automatic checks for one answer."""
    exp = item["expected_behaviour"]
    b_ok = behaviour == exp
    facts = [f for f in item.get("gold_facts", "").split("|") if f]
    stale = [f for f in item.get("stale_facts", "").split("|") if f]
    a = norm(answer)
    facts_ok = all(norm(f) in a for f in facts) if facts else None
    stale_present = any(norm(f) in a for f in stale)
    gold = item.get("gold_doc", "")
    source_ok = (gold in (sources or "")) if gold and exp == "answer" else None
    if exp == "answer":
        right = b_ok and (facts_ok if facts else bool(source_ok)) and not stale_present
    else:
        right = b_ok and not stale_present
    lang_ok = script(answer) == item["language"] if answer else False
    return {"behaviour_ok": b_ok, "facts_ok": facts_ok, "stale_present": stale_present, "source_ok": source_ok,
            "language_ok": lang_ok, "right": right}
