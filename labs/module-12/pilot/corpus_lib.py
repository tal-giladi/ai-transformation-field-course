"""Shared code for the precedent-search pilot: load the corpus, tokenise, search, parse citations.

Standard library only. The corpus is in ../data-room/knowledge/corpus/ (78 fictional documents).
"""
from __future__ import annotations

import csv
import math
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOM = HERE.parent / "data-room"
CORPUS = ROOM / "knowledge" / "corpus"
PARA = re.compile(r"^¶(\d+) (.*?)(?=^¶\d+ |\Z)", re.S | re.M)
CITE = re.compile(r"^\s*(\d+)\.\s+(.*?)\s*\[([A-Z]{3}-\d{4}-\d{3}) ¶(\d+)\]\s*$")
QUOTE = re.compile(r'(?: The source says: | נקבע: )"(.+?)"')
TOKEN = re.compile(r"[a-z0-9֐-׿]+")
HE_PREFIX = "והבלמשכ"
STOP = set("the a an of to in and or is are be by for on it its as at that this with not if from any which "
           "של את על עם או אם כי לא הוא היא זה זו גם רק אך".split())


def read_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def load_corpus() -> dict[str, dict]:
    """doc_id -> {"title", "text", "paras": {n: text}}."""
    docs = {}
    for p in sorted(CORPUS.glob("*.md")):
        raw = p.read_text(encoding="utf-8")
        title = raw.splitlines()[0].lstrip("# ").strip()
        body = raw[raw.index("\n¶1 ") + 1:] if "\n¶1 " in raw else ""
        paras = {int(m.group(1)): m.group(2).strip() for m in PARA.finditer(body)}
        docs[p.stem] = {"title": title, "text": title + "\n" + "\n".join(paras.values()), "paras": paras}
    return docs


def statuses(curated: bool) -> dict[str, str]:
    """Document status: from the KM index (before curation) or from the December curation sprint."""
    if curated:
        return {r["doc_id"]: r["status_after_review"] for r in read_csv(HERE / "curation-2026-12.csv")}
    return {r["doc_id"]: r["status"] for r in read_csv(ROOM / "km" / "precedent-bank-index.csv")
            if r["in_research_export"] == "yes"}


def tokens(text: str, strip_prefix: bool = False) -> list[str]:
    out = []
    for t in TOKEN.findall(text.lower()):
        if t in STOP:
            continue
        if strip_prefix and len(t) > 3 and t[0] in HE_PREFIX:
            t = t[1:]
        out.append(t)
    return out


class BM25:
    def __init__(self, docs: dict[str, str], strip_prefix=False, k1=1.4, b=0.75):
        self.strip, self.k1, self.b = strip_prefix, k1, b
        self.ids = list(docs)
        self.tf = [Counter(tokens(docs[i], strip_prefix)) for i in self.ids]
        self.len = [sum(c.values()) for c in self.tf]
        self.avg = sum(self.len) / len(self.len)
        df = Counter(t for c in self.tf for t in c)
        n = len(self.ids)
        self.idf = {t: math.log(1 + (n - d + 0.5) / (d + 0.5)) for t, d in df.items()}

    def search(self, query: str, k: int = 5) -> list[tuple[str, float]]:
        q = tokens(query, self.strip)
        scores = []
        for i, tf in enumerate(self.tf):
            s = 0.0
            for t in q:
                if t in tf:
                    f = tf[t]
                    s += self.idf[t] * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * self.len[i] / self.avg))
            scores.append((self.ids[i], round(s, 4)))
        scores.sort(key=lambda x: (-x[1], x[0]))
        return scores[:k]


def lang_part(text: str, lang: str) -> str:
    """Rulings carry Hebrew and an [EN] line; return the part in the draft's language."""
    if "\n[EN] " in text:
        he, en = text.split("\n[EN] ", 1)
        return en if lang == "en" else he
    return text


def parse_draft(path: Path) -> list[dict]:
    """Numbered answer lines ending in [ID ¶n]; an optional quoted passage."""
    out = []
    lang = "he" if "| Language | Hebrew |" in path.read_text(encoding="utf-8") else "en"
    for line in path.read_text(encoding="utf-8").splitlines():
        m = CITE.match(line)
        if not m:
            continue
        body = m.group(2)
        q = QUOTE.search(body)
        claim = QUOTE.sub("", body).strip()
        out.append({"no": int(m.group(1)), "claim": claim, "quote": q.group(1) if q else "",
                    "cited_id": m.group(3), "pinpoint": int(m.group(4)), "language": lang})
    return out


def overlap(claim: str, paragraph: str) -> float:
    """Share of the claim's content words found in the paragraph (a crude, no-AI support check)."""
    c = set(tokens(claim, True))
    p = set(tokens(paragraph, True))
    return round(len(c & p) / len(c), 3) if c else 0.0
