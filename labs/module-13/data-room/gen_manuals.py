"""The maintenance shared drive as it is (data-room/docs/) and knowledge pack v1 (pilot/knowledge-pack/).

Reading this spoils the engagement: finish module 13 first.
"""
from __future__ import annotations

from gen_common import PILOT, ROOM, rng, write_csv, write_text
from manuals_text import MANUALS
from sops_text import SOPS_CURRENT, SOPS_STALE, SOPS_TRANSLATED

PACK_APPROVED = "2027-03-03"
LANG_NAME = {"he": "Hebrew", "ar": "Arabic", "ru": "Russian", "en": "English"}


def _doc(doc_id: str, title: str, lang: str, rev: str, date: str, owner: str, body: str, extra: str = "") -> str:
    head = (f"# {doc_id} · {title}\n\n"
            f"- Document: {doc_id}\n- Language: {LANG_NAME[lang]}\n- Revision: {rev} ({date})\n- Owner: {owner}\n")
    return head + extra + "\n" + body.strip() + "\n"


def write_drive() -> dict:
    """data-room/docs/: what a technician finds on \\\\kp-fs01\\maintenance today."""
    files = []
    for doc_id, (title, lang, ed, body) in MANUALS.items():
        name = f"{doc_id}-{lang}.md"
        write_text(ROOM / "docs" / name, _doc(doc_id, title, lang, ed, "maker", "Maker (as supplied)", body))
        files.append((name, doc_id, title, lang, ed, "maker"))
    for doc_id, (title, lang, rev, date, owner, body) in SOPS_CURRENT.items():
        name = f"{doc_id}-{lang}-rev{rev}.md"
        write_text(ROOM / "docs" / name, _doc(doc_id, title, lang, rev, date, owner, body))
        files.append((name, doc_id, title, lang, rev, date))
    for (doc_id, lang, rev), (title, date, body) in SOPS_STALE.items():
        name = f"{doc_id}-{lang}-rev{rev}.md"
        write_text(ROOM / "docs" / name, _doc(doc_id, title, lang, rev, date, "—", body))
        files.append((name, doc_id, title, lang, rev, date))
    return {"drive_docs": len(files), "_files": files}


def write_drive_listing(files: list[tuple]) -> dict:
    """A directory listing of the shared drive (what IT exported on request)."""
    r = rng(12)
    rows = []
    folder = {"MAN": "manuals", "SOP": "procedures"}
    for name, doc_id, title, lang, rev, date in files:
        sub = folder[doc_id.split("-")[0]]
        modified = date if len(str(date)) == 10 else "2019-06-03"
        rows.append([f"\\\\kp-fs01\\maintenance\\{sub}\\{name.replace('.md', '.pdf')}", doc_id, lang, rev, modified,
                     r.randint(180, 4200), "docs/" + name])
    extra = [
        ("parts\\רשימת חלקים - מעודכן.xlsx", "", "he", "", "2025-03-16", 412, "parts/parts-list-shared-drive.csv"),
        ("parts\\old\\רשימת חלקים 2022.xlsx", "", "he", "", "2022-11-02", 380, ""),
        ("procedures\\translations\\LOTO_arabic.pdf", "SOP-LOTO-01", "ar", "B", "2019-02-03", 96, "docs/SOP-LOTO-01-ar-revB.md"),
        ("procedures\\translations\\LOTO_russian.doc", "SOP-LOTO-01", "ru", "A", "2016-09-01", 54, "docs/SOP-LOTO-01-ru-revA.md"),
        ("procedures\\oil\\נוהל שמן ישן.pdf", "SOP-OIL-05", "he", "A", "2017-03-12", 88, "docs/SOP-OIL-05-he-revA.md"),
        ("manuals\\haiwei\\HW_service_bulletin_2014.pdf", "", "en", "", "2014-05-20", 210, ""),
        ("manuals\\morandi\\Manuale_MP_italiano.pdf", "", "it", "", "2008-01-15", 18400, ""),
        ("photos\\K07 הידראוליקה 2021\\", "", "", "", "2021-08-09", 52000, ""),
        ("vladi\\לוח כוננויות 2026.xlsx", "", "he", "", "2026-12-28", 44, ""),
        ("vladi\\סיכום תקלות 2015.xls", "", "he", "", "2016-01-10", 120, ""),
    ]
    for path, doc_id, lang, rev, mod, kb, room in extra:
        rows.append([f"\\\\kp-fs01\\maintenance\\{path}", doc_id, lang, rev, mod, kb, room])
    rows.sort(key=lambda x: x[0])
    n = write_csv(ROOM / "maintenance" / "shared-drive-listing.csv",
                  ["path", "doc_id", "language", "revision", "last_modified", "size_kb", "copy_in_data_room"], rows)
    return {"drive_listing": n}


def write_pack() -> dict:
    """Knowledge pack v1: current revisions only, approved translations, each with owner and revision."""
    pack = []
    for doc_id, (title, lang, ed, body) in MANUALS.items():
        pack.append((f"{doc_id}-{lang}", _doc(doc_id, title, lang, ed, "maker", "Maintenance manager (Vladimir Kaplan)",
                                                body, f"- In pack v1: approved {PACK_APPROVED}\n")))
    for doc_id, (title, lang, rev, date, owner, body) in SOPS_CURRENT.items():
        pack.append((f"{doc_id}-{lang}", _doc(doc_id, title, lang, rev, date, owner, body,
                                                f"- In pack v1: approved {PACK_APPROVED}\n")))
    for (doc_id, lang), (title, body) in SOPS_TRANSLATED.items():
        rev, date, owner = SOPS_CURRENT[doc_id][2], SOPS_CURRENT[doc_id][3], SOPS_CURRENT[doc_id][4]
        extra = (f"- Translation of the Hebrew revision {rev}, approved {PACK_APPROVED} by the safety officer "
                 f"and a native-speaking senior technician; the Hebrew text prevails\n")
        pack.append((f"{doc_id}-{lang}", _doc(doc_id, title, lang, rev, date, owner, body, extra)))
    pack.sort(key=lambda x: x[0])
    for name, text in pack:
        write_text(PILOT / "knowledge-pack" / f"{name}.md", text)
    allp = ("# Kinneret Plastics maintenance knowledge pack v1 (all documents)\n\n"
            f"{len(pack)} documents, approved {PACK_APPROVED}. Upload this one file to a chat tool for Track A. "
            "Each document starts with its id, language, revision and owner.\n\n")
    allp += "\n\n---\n\n".join(text for _, text in pack)
    write_text(PILOT / "knowledge-pack-all.md", allp)
    return {"pack_docs": len(pack)}
