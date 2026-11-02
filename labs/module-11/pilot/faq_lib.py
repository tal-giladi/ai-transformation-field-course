"""Shared code for the Givat Oren permit-FAQ pilot (lesson 11.5). Standard library only.

- load_corpus("site" | "pack"): the website's permits pages as they are, or the approved knowledge pack
- Search: a small BM25 index, the "no AI" baseline and the retriever for the LLM design
- check_answer(): the automatic checks the eval uses (behaviour, facts, stale facts, source, language)
"""
from __future__ import annotations

import csv
import math
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOM = HERE.parent / "data-room"
LANGS = ["he", "ar", "ru", "en"]

# Keyword facts, any language (an answer in the wrong language can still carry the right fact;
# language is scored separately).
KEYWORDS = {
    "letter": ["מכתב", "رسالة", "письм", "letter"],
    "not_eligible": ["אינו זכאי", "אינם זכאים", "לא זכאי", "لا يحق", "не имеет права", "не имеют права", "not eligible"],
    "free": ["ללא תשלום", "חינם", "مجان", "بدون رسوم", "бесплатно", "free", "no fee"],
    "badge": ["תג נכה", "بطاقة معاق", "بطاقة المعاق", "знак инвалида", "badge"],
    "consent": ["ייפוי כוח", "הסכמה", "توكيل", "موافقة", "доверенност", "согласи", "power of attorney", "consent"],
    "consult": ["פגישת ייעוץ", "اجتماع استشاري", "استشار", "консультац", "consultation"],
    "objection": ["השגה", "اعتراض", "возражени", "objection"],
    "free_second": ["בחינם השנה", "הוא בחינם", "התו לרכב שני חינם", "free this year", "is free"],
}
FEE_INTENTS = {"PRK-fee2", "SGN-fee", "SGN-min", "CAF-fee", "EVT-fee", "SKP-fee", "ARC-fee", "BLK-extra"}


def read_csv(path: Path) -> list[dict]:
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict], cols: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def load_corpus(name: str) -> list[dict]:
    """Each document: doc_id, topic, language, meta (header lines), body."""
    folder = ROOM / "content" / "site" if name == "site" else HERE / "knowledge-pack"
    docs = []
    for path in sorted(folder.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        head, _, body = text.partition("\n---\n")
        meta = dict(line.split(": ", 1) for line in head.splitlines() if ": " in line)
        doc_id = meta["doc_id"]
        docs.append({"doc_id": doc_id, "topic": doc_id.split("-")[0], "language": meta.get("language", ""),
                     "meta": meta, "body": body.strip()})
    return docs


# --- language and numbers -------------------------------------------------------------------------
def script_language(text: str) -> str:
    counts = Counter()
    for ch in text:
        o = ord(ch)
        if 0x0590 <= o <= 0x05FF:
            counts["he"] += 1
        elif 0x0600 <= o <= 0x06FF:
            counts["ar"] += 1
        elif 0x0400 <= o <= 0x04FF:
            counts["ru"] += 1
        elif 0x1200 <= o <= 0x137F:
            counts["am"] += 1
        elif ch.isascii() and ch.isalpha():
            counts["en"] += 1
    return counts.most_common(1)[0][0] if counts else ""


def numbers(text: str) -> set[str]:
    out = set()
    for m in re.finditer(r"\d+(?:[.,]\d+)?", text):
        s = m.group()
        if re.fullmatch(r"\d{1,3},\d{3}", s):
            s = s.replace(",", "")
        s = s.replace(",", ".")
        out.add(s.rstrip("0").rstrip(".") if "." in s else s)
    return out


def has_fact(text: str, fact: str) -> bool:
    if fact.startswith("kw:"):
        low = text.lower()
        return any(k.lower() in low for k in KEYWORDS[fact[3:]])
    return fact in numbers(text)


# --- search ---------------------------------------------------------------------------------------
HE_PREFIX = "והבלמשכ"
AR_STRIP = re.compile(r"[ً-ْـ]")


def tokens(text: str) -> list[str]:
    out = []
    for t in re.findall(r"\w+", text.lower()):
        if t.isdigit():
            out.append(t)
            continue
        t = AR_STRIP.sub("", t)
        if re.match(r"[֐-׿]", t) and len(t) > 3 and t[0] in HE_PREFIX:
            t = t[1:]
        elif re.match(r"[؀-ۿ]", t):
            for p in ("وال", "بال", "لل", "ال"):
                if t.startswith(p) and len(t) > len(p) + 2:
                    t = t[len(p):]
                    break
        elif re.match(r"[Ѐ-ӿ]", t):
            t = t[:5]
        elif t.isascii() and len(t) > 3 and t.endswith("s"):
            t = t[:-1]
        out.append(t)
    return out


class Search:
    def __init__(self, docs: list[dict], k1: float = 1.4, b: float = 0.75):
        self.docs = docs
        self.k1, self.b = k1, b
        self.tf = [Counter(tokens(d["body"])) for d in docs]
        self.len = [sum(tf.values()) for tf in self.tf]
        self.avg = sum(self.len) / len(self.len)
        df = Counter()
        for tf in self.tf:
            df.update(tf.keys())
        n = len(docs)
        self.idf = {t: math.log(1 + (n - c + 0.5) / (c + 0.5)) for t, c in df.items()}

    def top(self, query: str, k: int = 1) -> list[tuple[float, dict]]:
        q = tokens(query)
        scored = []
        for i, tf in enumerate(self.tf):
            s = 0.0
            for t in q:
                if t in tf:
                    f = tf[t]
                    s += self.idf[t] * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * self.len[i] / self.avg))
            scored.append((s, i))
        scored.sort(key=lambda x: (-x[0], self.docs[x[1]]["doc_id"]))
        return [(s, self.docs[i]) for s, i in scored[:k]]


# --- scoring --------------------------------------------------------------------------------------
def check_answer(item: dict, pred: dict) -> dict:
    """item: a test-set or negative-test row. pred: behaviour, answer, sources (';'-separated doc ids)."""
    expected = item["expected_behaviour"]
    behaviour = (pred.get("behaviour") or "").strip().lower()
    answer = pred.get("answer") or ""
    sources = [s.strip() for s in re.split(r"[;,\s]+", pred.get("sources") or "") if s.strip()]
    gold = [f for f in (item.get("gold_facts") or "").split("|") if f]
    stale = [f for f in (item.get("stale_facts") or item.get("must_not_contain") or "").split("|") if f]
    res = {"behaviour_ok": behaviour == expected}
    res["facts_ok"] = all(has_fact(answer, f) for f in gold) if gold else None
    res["stale_present"] = any(has_fact(answer, f) for f in stale) if stale else False
    topic = item.get("gold_topic") or ""
    if expected == "answer" and topic:
        ok_topics = {topic}
        intent = item.get("intent", "")
        src_ok = any(s.split("-")[0] in ok_topics or (s == "FEE2026-he" and intent in FEE_INTENTS) for s in sources)
        res["source_ok"] = src_ok
    else:
        res["source_ok"] = None
    lang = item["language"]
    res["answer_language"] = script_language(answer)
    res["language_ok"] = res["answer_language"] == lang if lang in LANGS else None
    if expected == "answer":
        res["correct"] = bool(res["behaviour_ok"] and res["facts_ok"] is not False and not res["stale_present"]
                              and res["source_ok"])
    else:
        res["correct"] = bool(res["behaviour_ok"] and not res["stale_present"])
    return res
