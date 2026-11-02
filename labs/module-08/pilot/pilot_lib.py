"""Shared code for the Northwind agent-assist pilot (lessons 08.5 and 08.6). Not run on its own.

  - INTENTS, DECISIONS: the label sets (the same as in system-prompt.md and policy-for-pilot.md);
  - normalise_order(): "nw4311456", "#NW-4311456", "NW 4311456" -> "NW-4311456";
  - script_language(): he / ar / ru / en / am / other from the alphabet;
  - keyword_intent(): the no-LLM intent baseline;
  - text_cues(): defect, age, new immigrant, disability, legal threat, injury found by keywords;
  - decide(): the returns policy as rules on the order facts plus the cues (the pilot's decision engine);
  - template_draft(): a plain reply per decision and language (the no-LLM draft);
  - draft_checks(): automatic checks on any draft (language, banned promises, fee above the cap).
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "common"))

INTENTS = ["wismo", "return_request", "return_policy_question", "refund_status", "fee_dispute", "exchange",
           "defect_damage", "product_question", "order_change_cancel", "payment_invoice", "complaint_legal", "other"]
DECIDE_INTENTS = {"return_request", "return_policy_question", "fee_dispute", "exchange", "defect_damage"}
DECISIONS = ["refund_minus_fee", "refund_no_fee_pickup", "refund_4m_verify", "outside_window", "excluded_custom",
             "exchange_free", "status_update", "escalate_counsel", "n/a"]
LANGUAGES = ["he", "ar", "ru", "en", "am"]


def normalise_order(text: str) -> str:
    m = re.search(r"(?i)(?:nw[- ]?)?(4\d{6})", text or "")
    return f"NW-{m.group(1)}" if m else ""


def script_language(text: str) -> str:
    counts = {"he": len(re.findall(r"[֐-׿]", text)), "ar": len(re.findall(r"[؀-ۿ]", text)),
              "ru": len(re.findall(r"[Ѐ-ӿ]", text)), "am": len(re.findall(r"[ሀ-፿]", text)),
              "en": len(re.findall(r"[A-Za-z]", re.sub(r"(?i)nw-?\d+|\[name\]", "", text)))}
    best = max(counts, key=counts.get)
    return best if counts[best] else "other"


# --- keyword intent baseline (written from a reading of 100 tickets outside the 2,000) ----------------
KEYWORDS = [
    ("complaint_legal", ["רשות להגנת הצרכן ולעורך", "חברת האשראי", "سلطة حماية المستهلك ولمحامي", "адвокату",
                         "my lawyer", "disputing the charge"]),
    ("refund_status", ["לא קיבלתי את הכסף", "איפה ההחזר", "מתי יחזור הכסף", "ما رجعولي المصاري", "وين المبلغ",
                       "деньги так и не пришли", "где мой возврат", "no refund", "where is my refund", "ገንዘቤ አልተመለሰም"]),
    ("fee_dispute", ["הורידו לי", "ניכיתם", "קופון", "خصموا", "كوبون", "удержали", "купон", "voucher", "took 10%"]),
    ("exchange", ["להחליף", "أبدله", "обменять", "swap it"]),
    ("defect_damage", ["קרוע", "נשבר", "התקלפה", "חסר חלק", "פגום", "مخزوق", "انكسر", "ناقص", "дефект", "отклеилась",
                       "не хватает", "damaged", "broke", "missing", "ተቀድዶ"]),
    ("return_policy_question", ["אפשר להחזיר", "כמה זמן יש לי", "מה נכון", "بقدر أرجعه", "شو الصحيح", "можно ли вернуть",
                                "сколько дней", "как правильно", "can i return", "how long do i have", "which is it"]),
    ("return_request", ["להחזיר", "לבטל את העסקה", "לוותר", "أرجعه", "وأرجع", "вернуть", "отменить покупку",
                        "return it", "send it back", "and return the", "መመለስ"]),
    ("order_change_cancel", ["לשנות את כתובת", "לבטל את ההזמנה", "أغير عنوان", "ألغي الطلب", "изменить адрес",
                             "отменить заказ", "change the delivery address", "cancel order"]),
    ("payment_invoice", ["חשבונית", "חויבתי פעמיים", "فاتورة", "накладная", "списали дважды", "invoice", "charged twice"]),
    ("wismo", ["לא הגיע", "איפה המשלוח", "מספר מעקב", "מתי מגיע", "ما وصل", "وين الطلبية", "ma wislat", "не пришёл",
               "где мой заказ", "отслеживания", "hasn't arrived", "where is order", "tracking", "አልደረሰኝም"]),
    ("product_question", ["מתאים ל", "המשקל", "مناسب", "وزن", "подходит", "вес у", "ok for", "weigh"]),
]


def keyword_intent(message: str) -> str:
    text = (message or "").lower()
    for intent, words in KEYWORDS:
        if any(w.lower() in text for w in words):
            return intent
    return "other"


CUE_WORDS = {
    "defect": ["קרוע", "נשבר", "התקלפה", "חסר חלק", "פגום", "مخزوق", "انكسر", "ناقص", "дефект", "отклеилась",
               "не хватает", "damaged", "broke", "missing", "seam", "ተቀድዶ"],
    "legal": ["רשות להגנת הצרכן", "עורך דין", "חברת האשראי", "سلطة حماية المستهلك", "محامي", "защите прав",
              "адвокат", "consumer protection", "lawyer", "card company"],
    "injury": ["נכוויתי", "انحرقت", "обжёг", "burned"],
    "immigrant": ["עלינו לארץ", "aliyah"],
    "disability": ["נכה", "disability"],
}
AGE_RE = re.compile(r"(בן|בת) (6[5-9]|[7-9]\d)|פנסיונר|I'm (6[5-9]|[7-9]\d)|pensioner",
                    re.IGNORECASE)


def text_cues(message: str) -> set[str]:
    text = (message or "").lower()
    found = {cue for cue, words in CUE_WORDS.items() if any(w.lower() in text for w in words)}
    if AGE_RE.search(message or ""):
        found.add("age")
    return found


def lawful_fee(price: float) -> float:
    return round(min(0.05 * price, 100.0), 2)


def _date(s: str) -> date | None:
    return date.fromisoformat(s[:10]) if s else None


def add_months(d: date, m: int) -> date:
    y, mo = divmod(d.month - 1 + m, 12)
    for day in (d.day, 30, 29, 28):
        try:
            return date(d.year + y, mo + 1, day)
        except ValueError:
            continue
    raise ValueError(d)


def decide(row: dict, intent: str, cues: set[str]) -> tuple[str, float]:
    """The pilot's returns policy (policy-for-pilot.md) as rules. Returns (decision, fee in ILS)."""
    if intent == "complaint_legal":
        return "escalate_counsel", 0.0
    if intent == "refund_status":
        return "status_update", 0.0
    if intent not in DECIDE_INTENTS:
        return "n/a", 0.0
    price = float(row["item_price_ils"])
    od, dd = _date(row["order_date"]), _date(row["delivered_date"])
    late = bool(od and dd and (dd - od).days > 6)
    if intent == "defect_damage" or "defect" in cues or late:
        return "refund_no_fee_pickup", 0.0
    if row.get("custom_item") == "y":
        return "excluded_custom", 0.0
    days = int(row["days_since_delivery"] or 0)
    if intent == "exchange" and days <= 30:
        return "exchange_free", 0.0
    if days <= 14:
        return "refund_minus_fee", lawful_fee(price)
    if row["customer_segment"] in ("trail_club", "silver_trail") and days <= 30:
        return "refund_minus_fee", lawful_fee(price)
    eligible = row["customer_segment"] == "silver_trail" or cues & {"age", "immigrant", "disability"}
    ticket_day = _date(row["created_at"])
    if eligible and row["order_channel"] in ("phone", "chat_assisted") and od and ticket_day <= add_months(od, 4):
        return "refund_4m_verify", lawful_fee(price)
    return "outside_window", 0.0


# --- the no-LLM draft ------------------------------------------------------------------------------
TEMPLATES = {
    "refund_minus_fee": {
        "he": "שלום, אפשר לבטל את הרכישה. נחזיר {refund} ₪ לאמצעי התשלום (מחיר {price} ₪ פחות דמי ביטול {fee} ₪) תוך 14 יום מקבלת ההודעה. את המוצר מחזירים בנקודת איסוף; פרטים בקישור.",
        "ar": "مرحبا، بتقدر تلغي الشراء. منرجع {refund} ₪ لوسيلة الدفع (السعر {price} ₪ ناقص رسوم إلغاء {fee} ₪) خلال 14 يوم من إشعار الإلغاء.",
        "ru": "Здравствуйте! Покупку можно отменить. Вернём {refund} ₪ на средство оплаты (цена {price} ₪ минус плата за отмену {fee} ₪) в течение 14 дней с уведомления.",
        "en": "Hello, you can cancel the purchase. We will refund ₪{refund} to your payment method (price ₪{price} less a ₪{fee} cancellation fee) within 14 days of your notice."},
    "refund_no_fee_pickup": {
        "he": "שלום, מצטערים! נשלח שליח לאסוף את המוצר מהכתובת שלך ונחזיר את מלוא הסכום, {price} ₪, ללא דמי ביטול.",
        "ar": "مرحبا، منعتذر! رح نبعت مندوب ياخد المنتج من عنوانك ومنرجع كامل المبلغ {price} ₪ بدون رسوم.",
        "ru": "Здравствуйте, приносим извинения! Курьер заберёт товар по вашему адресу, вернём полную сумму {price} ₪ без платы за отмену.",
        "en": "Hello, sorry about this! A courier will collect the item from your address and we will refund the full ₪{price}, no fee."},
    "refund_4m_verify": {
        "he": "שלום, מכיוון שהרכישה נעשתה בשיחה עם נציג, ייתכן שמגיעה לך תקופת ביטול מורחבת. נא לשלוח צילום תעודה מתאימה (אזרח ותיק, נכות או תעודת עולה) ונחזיר {refund} ₪.",
        "ar": "مرحبا، لأن الشراء تم بمحادثة مع موظف، ممكن يكون إلك فترة إلغاء أطول. ابعتلنا صورة الشهادة المناسبة ومنرجع {refund} ₪.",
        "ru": "Здравствуйте! Покупка была сделана в разговоре с сотрудником, поэтому у вас может быть продлённый срок отмены. Пришлите копию подтверждающего документа, и мы вернём {refund} ₪.",
        "en": "Hello, because you bought in a conversation with one of our agents, you may have an extended cancellation period. Please send a copy of the relevant certificate and we will refund ₪{refund}."},
    "outside_window": {
        "he": "שלום, תקופת הביטול לפריט זה הסתיימה. נשמח להציע החלפה או לבדוק פתרון אחר; נציג יחזור אלייך.",
        "ar": "مرحبا، مدة الإلغاء لهاد المنتج خلصت. منقدر نقترح تبديل أو حل تاني، موظف رح يرجعلك.",
        "ru": "Здравствуйте! Срок отмены для этого товара истёк. Можем предложить обмен или другое решение; сотрудник свяжется с вами.",
        "en": "Hello, the cancellation period for this item has ended. We can offer an exchange or look at another solution; an agent will follow up."},
    "excluded_custom": {
        "he": "שלום, פריט שהוכן בהתאמה אישית אינו ניתן לביטול, אלא אם יש בו פגם. אם יש בעיה בפריט, נשמח לראות תמונה.",
        "ar": "مرحبا، المنتج المصنوع حسب الطلب ما بنلغيه إلا إذا فيه عيب. إذا في مشكلة ابعتلنا صورة.",
        "ru": "Здравствуйте! Товар, изготовленный по индивидуальному заказу, не подлежит отмене, кроме случая дефекта. Если есть проблема, пришлите фото.",
        "en": "Hello, personalised items can't be cancelled unless they are faulty. If something is wrong with it, please send us a photo."},
    "exchange_free": {
        "he": "שלום, בשמחה! נשלח את המידה החדשה ושליח יאסוף את הקיים, ללא עלות.",
        "ar": "مرحبا، أكيد! منبعت المقاس الجديد والمندوب بياخد القديم بدون تكلفة.",
        "ru": "Здравствуйте! Конечно, отправим новый размер, курьер бесплатно заберёт этот.",
        "en": "Hello, happy to help! We'll send the new size and collect the current one free of charge."},
    "status_update": {
        "he": "שלום, בדקתי את ההחזר על הזמנה {order}: סטטוס {status}. [CHECK: תאריך ההחזר הצפוי לפי ה-OMS]",
        "ar": "مرحبا، فحصت الإرجاع للطلب {order}: الحالة {status}. [CHECK: موعد الإرجاع المتوقع]",
        "ru": "Здравствуйте! Проверила возврат по заказу {order}: статус {status}. [CHECK: ожидаемая дата возврата]",
        "en": "Hello, I've checked the refund for order {order}: status {status}. [CHECK: expected refund date from the OMS]"},
}


def template_draft(decision: str, lang: str, row: dict, fee: float) -> str:
    lang = lang if lang in ("he", "ar", "ru", "en") else "he"
    if decision not in TEMPLATES:
        return ""
    price = float(row["item_price_ils"])
    return TEMPLATES[decision][lang].format(price=f"{price:g}", fee=f"{fee:g}", refund=f"{price - fee:g}",
                                            order=row.get("order_id", ""), status=row.get("return_status") or "—")


# --- checks on any draft ---------------------------------------------------------------------------
BANNED = {
    "store_credit_only": ["זיכוי לאתר בלבד", "רק בזיכוי", "كرصيد بس", "только кредитом", "store credit only"],
    "ten_percent": ["10%"],
    "thirty_days_full": ["30 יום", "30 days", "30 дней", "30 يوم"],
    "chatbot_trace": ["Certainly!", "As an AI", "כמודל שפה", "Конечно! Вот"],
}
FEE_RE = re.compile(r"(\d+(?:\.\d+)?)\s?₪|₪\s?(\d+(?:\.\d+)?)")


def draft_checks(draft: str, lang: str, decision: str, row: dict) -> dict:
    out = {"draft_language_ok": True, "banned_phrase": "", "fee_over_cap": False}
    if not draft:
        return {**out, "draft_language_ok": decision in ("n/a", "escalate_counsel")}
    want = lang if lang in ("he", "ar", "ru", "en") else "he"
    out["draft_language_ok"] = script_language(draft) == want
    for name, words in BANNED.items():
        if any(w in draft for w in words) and not (name == "thirty_days_full" and decision == "exchange_free"):
            out["banned_phrase"] = name
            break
    if decision == "refund_minus_fee":
        cap = lawful_fee(float(row["item_price_ils"]))
        price = float(row["item_price_ils"])
        amounts = [float(a or b) for a, b in FEE_RE.findall(draft)]
        small = [a for a in amounts if a < price * 0.5]
        out["fee_over_cap"] = any(a > cap + 0.01 for a in small)
    return out


# --- prompt in, JSON out ---------------------------------------------------------------------------
def order_facts(row: dict) -> str:
    return (f"Order {row['order_id']} | ordered {row['order_date']} via {row['order_channel']} | delivered "
            f"{row['delivered_date'] or 'not yet'} | item {row['item']} ({row['item_category']}), ₪{row['item_price_ils']} | "
            f"personalised: {row['custom_item']} | days since delivery: {row['days_since_delivery'] or 'n/a'} | "
            f"customer segment: {row['customer_segment']} | return status: {row['return_status'] or 'none'} | "
            f"refund method: {row['refund_method'] or 'n/a'} | fees deducted: {row['fees_deducted_ils'] or '0'} | "
            f"ticket date {row['created_at'][:10]}")


def item_prompt(row: dict) -> str:
    return f"ORDER FACTS: {order_facts(row)}\n\nCUSTOMER MESSAGE ({row['channel']}):\n{row['message']}"


def load_system_prompt() -> tuple[str, str]:
    text = (HERE / "system-prompt.md").read_text(encoding="utf-8")
    version = re.search(r"Version:\s*([\d.]+)", text).group(1)
    block = re.search(r"```text\n(.*?)```", text, re.S).group(1)
    return block.strip(), version


def parse_reply(text: str) -> dict:
    m = re.search(r"\{.*\}", text or "", re.S)
    if not m:
        return {"intent": "other", "decision": "n/a", "fee_ils": 0, "escalate": False, "cues": [], "reply_language": "",
                "draft": "", "parse_error": True}
    try:
        data = json.loads(m.group(0))
    except json.JSONDecodeError:
        return {"intent": "other", "decision": "n/a", "fee_ils": 0, "escalate": False, "cues": [], "reply_language": "",
                "draft": "", "parse_error": True}
    data.setdefault("cues", [])
    data["parse_error"] = False
    return data
