"""Shared code for the module 5 pilot scripts (lessons 05.2-05.4). Not run on its own.

What is here, so each script stays short:
  - the category and flag lists (the same as in system-prompt.md and categories.md);
  - pseudonymise(): replaces names, e-mail addresses, phone, ID and card numbers before any text
    goes to a model;
  - normalise_order(): turns "so26…", "SO-26…", "#005101", "26005101" into "SO26005101";
  - order_context(): the facts the date fix knows about an order, as one line for the prompt;
  - script_language(): Hebrew / Arabic / Russian / English / other by the alphabet used;
  - keyword_classify(): the no-LLM baseline that every LLM run is compared with;
  - load_system_prompt(), item_message(), parse_reply(): the prompt in and the JSON out;
  - draft_checks(): automatic checks on a draft (language, dates, leaks, chatbot traces).
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "common"))

CATEGORIES = ["wismo", "reschedule", "damage", "assembly", "returns", "invoice", "b2b_quote",
              "product_question", "complaint", "spam", "other"]
FLAGS = ["safety", "legal_threat", "refund_exception", "personal_data", "privacy_request", "angry",
         "unsupported_language", "prompt_injection", "no_order_number"]
LANGUAGES = ["he", "ar", "ru", "en"]
ESCALATION_FLAGS = {"safety", "legal_threat", "refund_exception", "privacy_request", "angry"}

# Customs, warehouse and booking time between a container's latest ETA and delivery to the customer
# (the date-fix rule in lesson 03.2: "latest ETA + about 7 days").
DAYS_AFTER_ETA = 7


# --- Pseudonymisation --------------------------------------------------------------------------------
EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+(\.[\w-]+)+")
PHONE_RE = re.compile(r"(?<!\d)(?:\+?972[- ]?|0)(?:5\d|[2-489]|7\d)[- ]?\d{3}[- ]?\d{4}(?!\d)")
CARD_RE = re.compile(r"(?<!\d)(?:\d{4}[ -]?){3}\d{4}(?!\d)")
ID_RE = re.compile(r"(?<![\dA-Za-z])\d{9}(?!\d)")
# A street, a house number and a city, as customers write a delivery address ("הרצל 104, Rishon LeZion").
ADDRESS_RE = re.compile(r"(?:[^\W\d_][\w\"'׳-]* ){1,3}\d{1,4},\s?[A-Z][A-Za-z']+(?:[ -][A-Z][A-Za-z']+)*")


def pseudonymise(text: str, names: list[str] | tuple = ()) -> tuple[str, dict]:
    """Replace personal details with placeholders (names, e-mails, phones, ID and card numbers, street addresses). Returns (text, counts of what was replaced).

    `names` are the sender's name as the helpdesk has it; the full name and each part of three or
    more letters are replaced wherever they appear (signatures, "my name is…").
    Order numbers are kept: the pilot needs them to look the order up.
    """
    counts = {"email": 0, "phone": 0, "card": 0, "id": 0, "address": 0, "name": 0, "name_second_pass": 0}
    text = text or ""

    def sub(pattern, token, key, s):
        new, n = pattern.subn(token, s)
        counts[key] += n
        return new

    text = sub(EMAIL_RE, "[EMAIL]", "email", text)
    text = sub(CARD_RE, "[CARD]", "card", text)
    text = sub(PHONE_RE, "[PHONE]", "phone", text)
    text = sub(ID_RE, "[ID]", "id", text)
    text = sub(ADDRESS_RE, "[ADDRESS]", "address", text)
    parts: list[str] = []
    for name in names:
        name = (name or "").strip()
        if not name:
            continue
        parts.append(name)
        parts += [p for p in re.split(r"\s+", name) if len(p) >= 3]
    for part in sorted(set(parts), key=len, reverse=True):
        pattern = re.compile(r"(?<!\w)" + re.escape(part) + r"(?!\w)")
        text = sub(pattern, "[NAME]", "name", text)
    # Second pass: the helpdesk often has the name in one alphabet and the signature or greeting in
    # another ("Osnat Golan" vs "אסנת גולן"). Catch the two words before a phone number and the word
    # after a greeting.
    text = sub(SIGNATURE_RE, "[NAME] [PHONE]", "name_second_pass", text)
    text = sub(GREETING_RE, r"\1 [NAME]", "name_second_pass", text)
    text = re.sub(r"\[NAME\](\s+\[NAME\])+", "[NAME]", text)
    return text, counts


SIGNATURE_RE = re.compile(r"(?<![\w\]])[^\W\d_]{2,}\s+[^\W\d_]{2,}\s+\[PHONE\]")
GREETING_RE = re.compile(r"^(שלום|היי|Здравствуйте,|Добрый день,|مرحبا|Hi|Hello|Dear)\s+(?!\[|רב\b|Sir\b|team\b|there\b)[^\W\d_]{2,}(?=\s?[,!.،])", re.M)


# --- Orders ------------------------------------------------------------------------------------------
ORDER_RE = re.compile(r"(?i)(?:\bSO[- ]?26\d{6}\b|#\s?0\d{5}\b|\b26\d{6}\b)")


def normalise_order(raw: str) -> str:
    """'so26005101', 'SO-26005101', '#005101', '26005101' -> 'SO26005101'; '' if no order number."""
    raw = (raw or "").strip()
    if not raw:
        return ""
    digits = re.sub(r"\D", "", raw)
    if len(digits) == 8 and digits.startswith("26"):
        return "SO" + digits
    if len(digits) == 6:
        return "SO26" + digits
    return ""


def find_order(text: str) -> str:
    m = ORDER_RE.search(text or "")
    return normalise_order(m.group(0)) if m else ""


def _d(value) -> date | None:
    if value is None or value != value or value == "":  # None, NaN, ''
        return None
    if hasattr(value, "date"):
        return value.date()
    return date.fromisoformat(str(value)[:10])


def order_context(order: dict | None, shipment: dict | None, received: date) -> dict:
    """What the date fix knows about an order on the day the message arrived.

    Returns a dict with the prompt line and the dates the draft checks need:
    {"line", "promised", "expected", "delivered"}. Reconstructed as if the date fix (live from
    January 2027) had been running: expected = the container's latest ETA + 7 days, never earlier
    than the promise.
    """
    if not order:
        return {"line": "none", "promised": None, "expected": None, "delivered": None}
    promised = _d(order.get("promised_delivery_date"))
    actual = _d(order.get("actual_delivery_date"))
    fmt = lambda d: d.strftime("%d/%m/%Y")  # noqa: E731
    bits = [f"order {order['order_id']}", str(order.get("item_description", "")),
            f"supplier country {order.get('supplier_country', '')}"]
    if promised:
        bits.append(f"promised by {fmt(promised)}")
    if actual and actual <= received:
        bits.append(f"delivered on {fmt(actual)}")
        return {"line": " · ".join(bits), "promised": promised, "expected": None, "delivered": actual}
    expected = None
    if shipment:
        eta = _d(shipment.get("eta_latest_date")) or _d(shipment.get("eta_original_date"))
        arrived = _d(shipment.get("arrival_date"))
        if arrived and arrived <= received:
            bits.append("container arrived at port, delivery being scheduled")
            expected = max(promised or received, received + timedelta(days=3))
        elif eta:
            expected = eta + timedelta(days=DAYS_AFTER_ETA)
            if promised and expected < promised:
                expected = promised
    elif promised:
        expected = promised
    bits.append("not delivered yet")
    if expected:
        bits.append(f"expected delivery {fmt(expected)} (updated by logistics)")
    return {"line": " · ".join(bits), "promised": promised, "expected": expected, "delivered": None}


# --- Language by alphabet -----------------------------------------------------------------------------
SCRIPTS = {
    "he": re.compile(r"[֐-׿]"),
    "ar": re.compile(r"[؀-ۿ]"),
    "ru": re.compile(r"[Ѐ-ӿ]"),
    "en": re.compile(r"[A-Za-z]"),
}
OTHER_SCRIPT = re.compile(r"[ሀ-፿԰-֏Ⴀ-ჿ一-鿿]")  # Ethiopic, Armenian, Georgian, CJK
FRENCH_HINT = re.compile(r"(?i)\b(bonjour|merci|je|voudrais|est-ce|canapé|livraison|où)\b")
STRIP_FOR_LANG = re.compile(r"\[[A-Z_]+(?::[^\]]*)?\]|Harbor & Pine|SO26\d{6}|[A-Z]{2,}-[A-Z]{3}-\d+")


def script_language(text: str) -> str:
    """The language a message is written in, judged by its alphabet: he, ar, ru, en, other or ''."""
    text = STRIP_FOR_LANG.sub(" ", text or "")
    counts = {k: len(p.findall(text)) for k, p in SCRIPTS.items()}
    other = len(OTHER_SCRIPT.findall(text))
    best = max(counts, key=counts.get)
    if other > counts[best]:
        return "other"
    if counts[best] == 0:
        return ""
    return best


# --- The keyword baseline (no LLM) --------------------------------------------------------------------
# Written from the 200-message dev set only. Order matters: the first rule that matches wins.
KEYWORDS: list[tuple[str, list[str]]] = [
    ("spam", ["first page of google", "seo", "free audit", "manufacturer of", "moq", "catalog",
              "overdue", "pay today", "mailbox full", "unsubscribe", "loan", "הלוואה", "הלוואות",
              "לחץ כאן", "bitcoin", "winner", "verify your"]),
    ("b2b_quote", ["quote", "הצעת מחיר", "הצעות מחיר", "коммерческое предложение", "عرض سعر",
                   "hotel", "מלון", "guest house", "procurement", "רכש,", "כיסאות משרדיים",
                   "משרדים", "municipality"]),
    ("assembly", ["assembl", "הרכבה", "מרכיבים", "להרכיב", "מרכיב", "сборк", "сборщик", "собрать",
                  "تركيب", "الفني", "instructions", "הוראות"]),
    ("other", ["warranty", "guarantee", "אחריות", "гаранти", "كفالة", "קו\"ח", "resume", "cv",
               "שעות הפתיחה", "opening hours", "часы работы"]),
    ("damage", ["damage", "broken", "torn", "shattered", "scratch", "crack", "dent", "photos of the",
                "נזק", "שבור", "נשבר", "קרוע", "סדק", "שריטה", "פגום", "תמונות", "תביעה",
                "сломан", "сломал", "поврежд", "царапин", "трещин", "порван", "разбит", "фото",
                "مكسور", "انكسر", "خربان", "مخدوش", "شق", "صور"]),
    ("returns", ["return", "refund", "cancel", "החזרה", "להחזיר", "החזר", "זיכוי", "ביטלתי", "לבטל",
                 "ביטול", "возврат", "вернуть", "отменить заказ", "отмен", "ارجاع", "ارجع", "رجع",
                 "الغاء", "بلغي", "مصاري"]),
    ("invoice", ["invoice", "receipt", "חשבונית", " קבלה", "чек", "счёт", "счет", "فاتورة", "ايصال",
                 "charged", "חיוב", "חייבו"]),
    ("reschedule", ["another day", "different day", "reschedule", "postpone", "להזיז", "לדחות",
                    "יום אחר", "אפשר רק אחרי", "перенести", "другой день", "نأجل", "يوم ثاني",
                    "نغير موعد"]),
    ("complaint", ["unacceptable", "rude", "terrible service", "compensation", "nobody came",
                   "לא מקובל", "גסי רוח", "מזעזע", "פיצוי", "אף אחד לא הגיע", "שירות גרוע",
                   "безобраз", "грубо", "компенсац", "никто не приехал", "ужасн",
                   "مش محترمين", "تعويض", "ما حدا اجا", "خدمة سيئة", "هيك بتعاملوا"]),
    ("spam", ["partnership opportunity", "book a call", "influencer"]),
    ("product_question", ["dimension", "colour", "color", "in stock", "מידות", "צבע אחר", "במלאי",
                          "בתצוגה", "משלוח לאילת", "размер", "другом цвете", "в наличии", "قياسات",
                          "لون ثاني", "متوفر", "מגיע גם"]),
    ("wismo", ["where is my order", "when will", "arrive", "delivery date", "still waiting",
               "on time", "on track", "my order", "איפה ההזמנה", "מתי מגיע", "מתי תגיע", "מחכה",
               "המשלוח", "ההזמנה", "עדיין בזמן", "סטטוס", "מתי זה מגיע", "где мой", "когда",
               "доставк", "жду", "заказ", "реальную дату", "وين", "متى", "الطلبية", "الطلب",
               "التوصيل", "بستنى", "بوصل", "يوصل"]),
    ("product_question", ["size", "showroom", "צבע", "цвет", "لون", "المعرض", "משלוח ל"]),
]


def keyword_classify(subject: str, body: str) -> str:
    """Category by the first matching keyword list; 'other' when nothing matches."""
    text = f"{subject or ''}\n{body or ''}".lower()
    for category, words in KEYWORDS:
        if any(w in text for w in words):
            return category
    return "other"


# --- Prompt in, JSON out -----------------------------------------------------------------------------
def load_system_prompt(path: Path = HERE / "system-prompt.md") -> tuple[str, str]:
    """The first ```text block of system-prompt.md and its version (from the H1)."""
    md = path.read_text(encoding="utf-8")
    block = re.search(r"```text\n(.*?)\n```", md, re.S)
    version = re.search(r"\(v([\d.]+)\)", md.splitlines()[0])
    if not block:
        raise ValueError(f"No ```text block in {path}")
    return block.group(1), (version.group(1) if version else "?")


def item_message(row: dict) -> str:
    """One test item in the INPUT format the system prompt describes."""
    atts = int(row.get("attachments_count") or 0)
    return (f"ITEM: {row['item_id']}\nCHANNEL: {row.get('channel') or 'email'}\n"
            f"RECEIVED: {str(row.get('received_date') or '')[:10]}\nSUBJECT: {row.get('subject') or ''}\n"
            f"ATTACHMENTS: {f'{atts} file(s)' if atts else 'none'}\n"
            f"ORDER CONTEXT: {row.get('order_context') or 'none'}\n"
            f"MESSAGE:\n<<<\n{row.get('message') or ''}\n>>>")


def parse_reply(text: str) -> dict:
    """Read the model's JSON. A reply that is not JSON is kept and counted as a format failure."""
    text = (text or "").strip()
    m = re.search(r"\{.*\}", text, re.S)
    if m:
        try:
            data = json.loads(m.group(0))
            flags = data.get("flags") or []
            if isinstance(flags, str):
                flags = [f.strip() for f in flags.split(",") if f.strip()]
            return {"label": str(data.get("category", "")).strip().lower(),
                    "language": str(data.get("language", "")).strip().lower(),
                    "reply_language": str(data.get("reply_language", "")).strip().lower(),
                    "flags": ";".join(sorted({str(f).strip().lower() for f in flags})),
                    "draft": str(data.get("draft", "")),
                    "note_to_agent": str(data.get("note_to_agent", "")),
                    "format_ok": True}
        except json.JSONDecodeError:
            pass
    word = text.lower().strip(" .\"'")
    return {"label": word if word in CATEGORIES else "format_error", "language": "",
            "reply_language": "", "flags": "", "draft": "", "note_to_agent": "", "format_ok": False}


# --- Automatic checks on a draft ----------------------------------------------------------------------
CHATBOT_TRACES = re.compile(
    r"(?i)(certainly!|here'?s a (polite|draft|reply)|as an ai|i'?m an ai|language model|"
    r"конечно!|вот (вежлив|вариант|ответ)|بالتأكيد|إليك|הנה טיוטה|בטח! הנה|\*\*|^#)", re.M)
UNFILLED = re.compile(r"\[(?!FIRST_NAME\]|AGENT_NAME\]|CHECK:)[^\]]{2,40}\]")


def _date_tokens(d: date) -> list[re.Pattern]:
    return [re.compile(rf"(?<!\d)0?{d.day}\s?[./-]\s?0?{d.month}(?!\d)")]


def draft_checks(draft: str, *, expected_reply_language: str, category: str, promised=None,
                 expected=None, must: str = "", must_not: str = "") -> dict:
    """Checks a machine can make on one draft. They do not replace a person reading it (05.4)."""
    draft = draft or ""
    out = {}
    if expected_reply_language in ("none", "") or category == "spam":
        out["no_draft_ok"] = draft.strip() == ""
    else:
        out["has_draft"] = draft.strip() != ""
        out["language_ok"] = script_language(draft) == expected_reply_language
    out["no_chatbot_trace"] = not CHATBOT_TRACES.search(draft)
    out["no_unfilled_placeholder"] = not UNFILLED.search(draft)
    out["no_personal_numbers"] = not (CARD_RE.search(draft) or ID_RE.search(draft) or PHONE_RE.search(draft))
    if category == "wismo" and draft:
        if expected:
            out["quotes_expected_date"] = any(p.search(draft) for p in _date_tokens(expected))
        if promised and expected and promised != expected:
            out["no_stale_promised_date"] = not any(p.search(draft) for p in _date_tokens(promised))
    if must:
        out["must"] = all(re.search(p, draft, re.I) for p in must.split(" ;; ") if p)
    if must_not:
        out["must_not"] = not any(re.search(p, draft, re.I) for p in must_not.split(" ;; ") if p)
    return out
