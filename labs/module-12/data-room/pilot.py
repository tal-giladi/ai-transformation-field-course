"""Pilot files: research questions with gold documents, the curation result, 40 drafts with citations."""
from __future__ import annotations

import textbank as tb
from common import PILOT, rng, write_csv, write_md
from corpus import Doc

SOURCES = {
    "general_assistant": ("A general chat assistant used by associates, who pasted documents from the bank into "
                          "the chat; collected September-October 2026 and anonymised"),
    "parshan_poc": "Parshan AI proof of concept, 2 November 2026, run on the 78 exported documents as they were (uncurated)",
}
MIX = {
    "general_assistant": {"ok": 38, "nonexistent": 18, "bad_pinpoint": 4, "misstated_neg": 5, "misstated_wrong": 5,
                          "bad_quote": 6, "superseded": 4},
    "parshan_poc": {"ok": 52, "nonexistent": 0, "bad_pinpoint": 3, "misstated_neg": 7, "misstated_wrong": 5,
                    "bad_quote": 3, "superseded": 10},
}


def props_by_key():
    out = {}
    for t in tb.TOPICS:
        for i, p in enumerate(t["P"], 1):
            out[f"{t['key']}:P{i}"] = p
        out[f"{t['key']}:P3_old"] = t["P3_old"]
    return out


def build_questions(docs: list[Doc]) -> list[dict]:
    qs, n = [], 0
    for t in tb.TOPICS:
        for i, p in enumerate(t["P"], 1):
            key = f"{t['key']}:P{i}"
            gold = sorted({d.id for d in docs if not d.superseded_by and any(k == key for _, k in d.paras)})
            stale = sorted(d.id for d in docs if d.superseded_by and d.topic == t["key"]) if i == 3 else []
            for lang in ("en", "he"):
                n += 1
                qs.append(dict(id=f"Q{n:02d}", lang=lang, text=p[f"{lang}_q"], topic=t["key"], prop=key,
                               gold=gold, stale=stale))
    return qs


def write_questions(qs) -> None:
    write_csv(PILOT / "questions.csv",
              ["question_id", "language", "question", "topic", "proposition", "gold_docs", "stale_docs"],
              [[q["id"], q["lang"], q["text"], q["topic"], q["prop"], ";".join(q["gold"]), ";".join(q["stale"])]
               for q in qs])
    write_csv(PILOT / "questions-scoring-sheet.csv",
              ["question_id", "language", "question", "gold_docs", "stale_docs", "your_top_docs",
               "gold_in_top5", "stale_in_top3", "answer_correct", "notes"],
              [[q["id"], q["lang"], q["text"], ";".join(q["gold"]), ";".join(q["stale"]), "", "", "", "", ""]
               for q in qs])
    for b in range(2):
        part = [q for q in qs if q["lang"] == ("en" if b == 0 else "he")]
        lines = [f"# Question batch {b + 1} — {'English' if b == 0 else 'Hebrew'} ({len(part)} questions)", "",
                 "Paste into a new conversation of your research assistant. Ask for each question: the answer in "
                 "two sentences, then the documents and paragraphs it relies on as [ID ¶n].", ""]
        lines += [f"{q['id']}. {q['text']}" for q in part]
        write_md(PILOT / "batches" / f"questions-{'en' if b == 0 else 'he'}.md", "\n".join(lines))


def write_curation(docs: list[Doc], km_status: dict) -> None:
    r = rng("curation")
    rows = []
    for d in sorted(docs, key=lambda x: x.id):
        if d.superseded_by:
            note = ("pre-Amendment 13 supplier form; replaced" if d.kind == "clause note"
                    else f"reversed on appeal in {d.superseded_by}" if d.kind == "ruling"
                    else f"relies on a reversed ruling; replaced by {d.superseded_by}")
            rows.append([d.id, km_status[d.id], "superseded", d.superseded_by, "T.G.", f"2026-12-{r.randint(1, 17):02d}", note])
        else:
            rows.append([d.id, km_status[d.id], "current", "", "T.G.", f"2026-12-{r.randint(1, 17):02d}", ""])
    write_csv(PILOT / "curation-2026-12.csv",
              ["doc_id", "km_status_before", "status_after_review", "superseded_by", "reviewer", "reviewed_on", "note"],
              rows)


def _quote(r, text: str, n_words=(7, 11)) -> str:
    words = text.split()
    k = min(len(words), r.randint(*n_words))
    s = r.randint(0, len(words) - k)
    return " ".join(words[s:s + k]).strip(".,;:")


def _fake_quote(r, quote: str, lang: str) -> str:
    words = quote.split()
    i = r.randint(1, max(1, len(words) - 2))
    words.insert(i, "always" if lang == "en" else "תמיד")
    return " ".join(words)


def build_drafts(docs: list[Doc], qs) -> tuple[list[list], list[list]]:
    r = rng("drafts")
    P = props_by_key()
    by_id = {d.id: d for d in docs}
    labels, sheet = [], []
    q_en = [q for q in qs if q["lang"] == "en"]
    q_he = [q for q in qs if q["lang"] == "he"]
    r.shuffle(q_en); r.shuffle(q_he)
    n = 0
    for src in ("general_assistant", "parshan_poc"):
        bag = [k for k, v in MIX[src].items() for _ in range(v)]
        r.shuffle(bag)
        for j in range(20):
            n += 1
            lang = "en" if j % 2 == 0 else "he"
            q = (q_en if lang == "en" else q_he)[j // 2 + (0 if src == "general_assistant" else 10)]
            cur = [(d, i + 1, k) for d in docs if d.topic == q["topic"] and not d.superseded_by
                   for i, (_, k) in enumerate(d.paras) if k and not k.endswith("P3_old")]
            old = [(d, i + 1, k) for d in docs if d.topic == q["topic"] and d.superseded_by
                   for i, (_, k) in enumerate(d.paras) if k and k.endswith("P3_old")]
            first = [c for c in cur if c[2] == q["prop"]]
            lines, did = [], f"D-{n:02d}"
            for c in range(1, 5):
                label = bag.pop()
                quote, detail = "", ""
                if label == "superseded":
                    d, para, k = r.choice(old)
                elif label == "bad_quote":
                    d, para, k = r.choice([x for x in cur if x[0].lang_part(x[1], lang) is not None])
                elif c == 1 and first:
                    d, para, k = r.choice(first)
                else:
                    d, para, k = r.choice(cur)
                p = P[k]
                claim = p["en_c"] if lang == "en" else p["he_c"]
                cited, pin = d.id, para
                part = d.lang_part(para, lang)
                want_quote = part is not None and (label == "bad_quote" or r.random() < 0.3)
                if label == "nonexistent":
                    while True:
                        cited = f"FCR-{r.randint(2018, 2025)}-{r.randint(10, 480):03d}"
                        if cited not in by_id:
                            break
                    pin, want_quote = r.randint(3, 6), False
                elif label == "bad_pinpoint":
                    pin, want_quote = len(d.paras) + r.randint(1, 3), False
                elif label == "misstated_neg":
                    claim, detail = (p.get("en_n") if lang == "en" else p.get("he_n")), "opposite of the paragraph"
                elif label == "misstated_wrong":
                    others = [x for x in P if x.startswith(q["topic"]) and x != k and not x.endswith("P3_old")
                              and x not in [kk for _, kk in d.paras if kk]]
                    o = P[r.choice(sorted(others))]
                    claim, detail = (o["en_c"] if lang == "en" else o["he_c"]), "a different proposition"
                if want_quote:
                    quote = _quote(r, part)
                    if label == "bad_quote":
                        quote, detail = _fake_quote(r, quote, lang), "quote not in the paragraph"
                say = (' The source says: "{}"' if lang == "en" else ' נקבע: "{}"').format(quote) if quote else ""
                lines.append(f"{c}. {claim}{say} [{cited} ¶{pin}]")
                base = "misstated" if label.startswith("misstated") else label
                exists = "n" if label == "nonexistent" else "y"
                pin_ok = "na" if label == "nonexistent" else "n" if label == "bad_pinpoint" else "y"
                q_ok = "na" if not quote else "n" if label == "bad_quote" else "y"
                current = "na" if label == "nonexistent" else "n" if label == "superseded" else "y"
                supports = ("na" if label in ("nonexistent", "bad_pinpoint") else
                            "n" if base == "misstated" else "y")
                labels.append([did, c, src, lang, cited, pin, "y" if quote else "n", base, detail, exists, pin_ok,
                               q_ok, current, supports, "pass" if label == "ok" else "fail"])
                sheet.append([did, c, lang, claim, quote, cited, pin, "", "", "", "", "", "", ""])
            head = [f"# Draft {did}", "", "| Field | Value |", "|---|---|", f"| Source | {SOURCES[src]} |",
                    f"| Language | {'English' if lang == 'en' else 'Hebrew'} |", f"| Question | {q['id']} |", "",
                    f"**Question:** {q['text']}", "", "**Answer**", ""]
            write_md(PILOT / "drafts" / f"{did}.md", "\n".join(head + lines))
    return labels, sheet


def write_drafts(labels, sheet) -> None:
    write_csv(PILOT / "citation-labels.csv",
              ["draft_id", "citation_no", "source", "language", "cited_id", "pinpoint", "has_quote", "label",
               "label_detail", "expected_exists", "expected_pinpoint_ok", "expected_quote_ok", "expected_current",
               "expected_supports", "expected_verdict"], labels)
    write_csv(PILOT / "citation-check-sheet.csv",
              ["draft_id", "citation_no", "language", "claim", "quote", "cited_id", "pinpoint", "your_exists",
               "your_pinpoint_ok", "your_quote_ok", "your_current", "your_supports", "your_verdict", "seconds"], sheet)
