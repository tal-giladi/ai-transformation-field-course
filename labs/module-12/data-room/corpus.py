"""The research corpus Tamar exported for the vendor proof of concept: 78 fictional documents.

Rulings (FCR-), firm memos (ARM-) and clause notes (ARP-). Every ruling is FICTIONAL.
"""
from __future__ import annotations

from datetime import date, timedelta

import textbank as tb
from common import ROOM, rng, write_csv, write_md

REASON_EN = ["This follows from the wording of the clause read as a whole and from the commercial purpose both parties knew.",
             "The parties were experienced and advised; the court will not rewrite the bargain they made.",
             "The opposite reading would make the clause meaningless in the very case it was written for."]
REASON_HE = ["כך עולה מלשון התניה כשהיא נקראת בשלמותה ומהתכלית המסחרית שהייתה ידועה לשני הצדדים.",
             "הצדדים היו מנוסים ומיוצגים; בית המשפט לא יכתוב מחדש את העסקה שעשו.",
             "הפרשנות ההפוכה הייתה מרוקנת את התניה מתוכן במקרה שלשמו נכתבה."]
OLD_DPA_EN = ("The Supplier may use Customer Data to improve its services and may transfer Customer Data to "
              "sub-processors as needed. The Supplier shall indemnify the Customer for any breach of data-protection law.")
OLD_DPA_HE = ("הספק רשאי להשתמש במידע הלקוח לשיפור שירותיו ולהעביר אותו למעבדי משנה לפי הצורך. "
              "הספק ישפה את הלקוח בגין כל הפרה של דיני הגנת המידע.")
FICTION = ("> FICTIONAL document written for the course \"AI Transformation in the Field\". No real court, case, "
           "judge, party or firm. Its statements of law were written for an exercise and are not a statement of Israeli law.")


class Doc:
    def __init__(self, doc_id, kind, title, when, topic, lang, level="", author="", group=""):
        self.id, self.kind, self.title, self.date, self.topic = doc_id, kind, title, when, topic
        self.lang, self.level, self.author, self.group = lang, level, author, group
        self.paras: list[tuple[str, str | None]] = []   # (text, proposition key)
        self.superseded_by = ""

    def add(self, text, prop=None):
        self.paras.append((text, prop))
        return len(self.paras)

    def lang_part(self, n: int, lang: str) -> str | None:
        """The text of paragraph n in one language (rulings carry Hebrew + an [EN] line)."""
        text = self.paras[n - 1][0]
        if "\n[EN] " in text:
            he, en = text.split("\n[EN] ", 1)
            return en if lang == "en" else he
        return text if self.lang == lang else None


def _ids(r, prefix, year, used):
    while True:
        n = r.randint(10, 480)
        doc_id = f"{prefix}-{year}-{n:03d}"
        if doc_id not in used:
            used.add(doc_id)
            return doc_id


def _d(r, year, lo=1, hi=12):
    return date(year, r.randint(lo, hi), r.randint(1, 28))


def build_corpus() -> list[Doc]:
    r = rng("corpus")
    used: set[str] = set()
    docs: list[Doc] = []
    authors = ["Y.D.", "S.A.", "N.F.", "A.M.", "R.B.", "D.K.", "L.W.", "K.N.", "M.B.", "F.H.", "O.L.", "I.H."]
    for ti, t in enumerate(tb.TOPICS):
        key, P, old = t["key"], t["P"], t["P3_old"]
        pk = [f"{key}:P{i}" for i in range(1, 5)]
        pold = f"{key}:P3_old"
        y_old, y2 = r.choice([2019, 2020]), r.choice([2021, 2022])
        y1, y3 = r.choice([2018, 2019, 2020, 2021, 2023]), r.choice([2022, 2023, 2024, 2025])
        parties = t["parties"]

        def ruling(year, level, pair, when):
            doc = Doc(_ids(r, "FCR", year, used), "ruling", f"{pair[0]} v. {pair[1]}", when, key, "he+en", level)
            f = r.choice([0, 1, 3] if level.startswith("trial") else [0, 1, 2, 3])
            doc.add(f"{tb.RULING_FACTS_HE[f]}\n[EN] {tb.RULING_FACTS_EN[f]}")
            return doc

        def outcome(doc):
            o = r.choice([1, 3] if doc.level.startswith("trial") else [0, 2])
            doc.add(f"{tb.OUTCOME_HE[o]}\n[EN] {tb.OUTCOME_EN[o]}")

        def reason(doc):
            k = r.randrange(3)
            doc.add(f"{REASON_HE[k]}\n[EN] {REASON_EN[k]}")

        def holding(doc, p, keyname):
            return doc.add(f"{p['he']}\n[EN] {p['en']}", keyname)

        def question(doc, p):
            doc.add(f"השאלה שלפנינו: {p['he_q']}\n[EN] The question before us: {p['en_q']}")

        r_old = ruling(y_old, "trial court (fictional)", parties[3], _d(r, y_old, 1, 9))
        question(r_old, P[2]); holding(r_old, old, pold); reason(r_old); outcome(r_old)
        r2 = ruling(y2, "appellate court (fictional)", parties[1], _d(r, y2))
        question(r2, P[2]); holding(r2, P[2], pk[2])
        r2.add(f"לפיכך אנו הופכים בנקודה זו את ההלכה שנקבעה ב-{r_old.id}.\n"
               f"[EN] We therefore reverse the holding in {r_old.id} on this point.")
        reason(r2); outcome(r2)
        r_old.superseded_by = r2.id
        r1 = ruling(y1, r.choice(["appellate court (fictional)", "trial court (fictional)"]), parties[0], _d(r, y1))
        question(r1, P[0]); holding(r1, P[0], pk[0]); reason(r1); holding(r1, P[1], pk[1]); outcome(r1)
        r3 = ruling(y3, "trial court (fictional)", parties[2], _d(r, y3))
        question(r3, P[3]); holding(r3, P[3], pk[3]); reason(r3); holding(r3, P[0], pk[0]); outcome(r3)
        docs += [r1, r2, r3, r_old]

        memo_en = t["group"] in ("Corporate", "Tech & IP")

        def memo(year, when, title_en, title_he):
            lang = "en" if (r.random() < 0.7) == memo_en else "he"
            doc = Doc(_ids(r, "ARM", year, used), "memo", title_en if lang == "en" else title_he, when, key, lang,
                      author=r.choice(authors), group=t["group"])
            return doc

        def claim(doc, p, keyname, src, para):
            c = p["en_c"] if doc.lang == "en" else p["he_c"]
            return doc.add(f"{c} [{src.id} ¶{para}]", keyname)

        def ask(doc, p):
            doc.add(("Question: " + p["en_q"]) if doc.lang == "en" else ("שאלה: " + p["he_q"]))

        def reco(doc):
            k = r.randrange(3)
            doc.add(tb.MEMO_RECO_EN[k] if doc.lang == "en" else tb.MEMO_RECO_HE[k])

        m_old = memo(y_old + 1, min(_d(r, y_old + 1, 1, 10), r2.date - timedelta(days=20)),
                     f"{t['en_name']}: research note", f"{t['he_name']}: מזכר מחקר")
        ask(m_old, P[2]); claim(m_old, old, pold, r_old, 3); reco(m_old)
        later = lambda a: a.date + timedelta(days=r.randint(60, 700))
        m1 = memo(0, later(r1), f"{t['en_name']}: what the courts enforce", f"{t['he_name']}: מה בתי המשפט אוכפים")
        m2 = memo(0, later(r2), f"{t['en_name']}: updated position", f"{t['he_name']}: עמדה מעודכנת")
        m3 = memo(0, later(r3), f"{t['en_name']}: market practice", f"{t['he_name']}: נוהג השוק")
        m4 = memo(0, max(later(r1), later(r3)), f"{t['en_name']}: client briefing", f"{t['he_name']}: תדריך ללקוח")
        m5 = memo(0, later(r3), f"{t['en_name']}: drafting checklist", f"{t['he_name']}: רשימת בדיקה לניסוח")
        for doc in (m1, m2, m3, m4, m5):   # fix ids to their real year
            used.discard(doc.id)
            doc.id = _ids(r, "ARM", min(doc.date.year, 2026), used)
            if doc.date > date(2026, 10, 20):
                doc.date = date(2026, r.randint(1, 9), r.randint(1, 28))
        ask(m1, P[0]); claim(m1, P[0], pk[0], r1, 3); claim(m1, P[1], pk[1], r1, 5); reco(m1)
        ask(m2, P[2]); claim(m2, P[2], pk[2], r2, 3)
        m2.add(f"This replaces the earlier note {m_old.id}, which relied on {r_old.id}." if m2.lang == "en"
               else f"מזכר זה מחליף את המזכר הקודם {m_old.id}, שהסתמך על {r_old.id}.")
        reco(m2)
        m_old.superseded_by = m2.id
        ask(m3, P[3]); claim(m3, P[3], pk[3], r3, 3); reco(m3)
        ask(m4, P[1]); claim(m4, P[1], pk[1], r1, 5); claim(m4, P[3], pk[3], r3, 3); reco(m4)
        ask(m5, P[0]); claim(m5, P[0], pk[0], r3, 5); reco(m5)
        docs += [m1, m2, m3, m4, m5, m_old]

        def clause(when, title, cl_en, cl_he):
            doc = Doc(_ids(r, "ARP", when.year, used), "clause note", title, when, key, "en+he",
                      author=r.choice(authors), group=t["group"])
            doc.add(cl_en); doc.add(cl_he)
            return doc

        def note(doc, p, keyname, src, para):
            doc.add(f"Drafting note: {p['en_c']} [{src.id} ¶{para}]", keyname)
            doc.add(f"הערת ניסוח: {p['he_c']} [{src.id} ¶{para}]", keyname)

        c1 = clause(later(r1) if later(r1).year <= 2026 else date(2026, 3, 1), f"{t['en_name']} — standard clause",
                    t["clause_en"], t["clause_he"])
        note(c1, P[1], pk[1], r1, 5)
        c2 = clause(min(later(r3), date(2026, 9, 1)), f"{t['en_name']} — fallback wording", t["clause_en"], t["clause_he"])
        note(c2, P[3], pk[3], r3, 3)
        if key == "data-processing":
            c3 = clause(date(2019, 6, r.randint(1, 28)), "Data-processing clause (supplier form, 2019)", OLD_DPA_EN, OLD_DPA_HE)
            note(c3, old, pold, r_old, 3)
            c3.superseded_by = c1.id
        else:
            c3 = clause(min(later(r2), date(2026, 9, 1)), f"{t['en_name']} — negotiation notes", t["clause_en"], t["clause_he"])
            note(c3, P[2], pk[2], r2, 3)
        docs += [c1, c2, c3]
    for d in docs:
        if d.date > date(2026, 10, 30):
            d.date = date(2026, 9, 15)
    return docs


def stale(doc: Doc) -> bool:
    return bool(doc.superseded_by)


def write_corpus(docs: list[Doc]) -> None:
    out = ROOM / "knowledge" / "corpus"
    rows, allmd = [], ["# Research corpus — all 78 documents in one file", "", FICTION, ""]
    for d in sorted(docs, key=lambda x: x.id):
        head = [f"# {d.id} — {d.title}", "", FICTION, "", "| Field | Value |", "|---|---|",
                f"| Document | {d.id} |", f"| Type | {d.kind} |", f"| Date | {d.date.isoformat()} |",
                f"| Topic | {d.topic} |", f"| Language | {d.lang} |"]
        if d.level:
            head.append(f"| Court | {d.level} |")
        if d.author:
            head.append(f"| Author | {d.author} ({d.group}) |")
        body = [f"¶{i} {text}" for i, (text, _) in enumerate(d.paras, 1)]
        text = "\n".join(head) + "\n\n" + "\n\n".join(body) + "\n"
        write_md(out / f"{d.id}.md", text)
        allmd += [text.replace(FICTION + "\n\n", ""), "---", ""]
        rows.append([d.id, d.kind, d.title, d.date.isoformat(), d.topic, d.lang, d.level, d.author, len(d.paras)])
    write_md(ROOM / "knowledge" / "corpus-all.md", "\n".join(allmd))
    write_csv(ROOM / "knowledge" / "corpus-index.csv",
              ["doc_id", "type", "title", "date", "topic", "language", "court", "author", "paragraphs"], rows)
