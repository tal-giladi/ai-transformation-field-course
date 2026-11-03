"""Text fragments for the Open Hands data room. All people and families are fictional."""
from __future__ import annotations

import random

TIMELOG_NOTES = {
    "family_contact": ["phone call with mother", "WhatsApp with father re committee", "call back after hotline referral",
                       "parent call: benefit appeal", "call with grandmother", "שיחה עם אמא", "مكالمة مع الأم"],
    "home_visit": ["home visit", "home visit + school", "visit, Shefa-'Amr", "visit, Kiryat Ata", "ביקור בית"],
    "travel": ["drive", "bus to visit", "נסיעה"],
    "case_notes": ["notes from visits", "update case file", "notes (evening)", "רישום", "تسجيل ملاحظات"],
    "funder_report_adler_haddad": ["AH narratives", "AH quarterly - family narratives", "AH report - rewrite in English",
                                   "AH narratives, my families", "דוח אדלר-חדאד", "AH: fix narratives Hana sent back"],
    "other_funder_report": ["report - municipal", "Ministry report numbers", "foundation report", "דוח קרן"],
    "translation_letters": ["letter to family in Arabic", "translate committee letter", "letter in Russian",
                            "Amharic letter to parents", "תרגום מכתב"],
    "team_meeting": ["team meeting", "case conference", "ישיבת צוות"],
    "admin": ["forms", "expenses", "email", "admin"],
    "meetings": ["staff meeting", "meeting with municipality", "partners meeting", "1:1"],
    "grant_proposal": ["proposal draft", "LOI", "proposal budget narrative", "rewrite boilerplate for new template"],
    "donor_comms": ["donor calls", "thank-you letters", "Giving Tuesday plan", "major donor visit prep"],
    "events": ["Hanukkah party planning", "event logistics"],
    "board": ["board prep", "treasurer call"],
    "supervision": ["supervision", "1:1 supervision"],
    "case_review": ["case review", "review complex cases"],
    "newsletter": ["newsletter", "newsletter story"],
    "other": ["misc"],
}


def timelog_note(r: random.Random, act: str) -> str:
    return r.choice(TIMELOG_NOTES.get(act, ["-"]))


SURVEY_TOOLS = {
    "family services": ["ChatGPT (free)", "Gemini (personal Google)", "Google Translate", "DeepL"],
    "development and comms": ["ChatGPT Plus", "GrantGenie", "Canva Magic Write", "Gemini (work Google)"],
    "programmes": ["ChatGPT (free)", "Canva Magic Write", "Google Translate"],
    "operations and management": ["Copilot", "ChatGPT (free)", "Gemini (work Google)"],
}
SURVEY_TASKS = {
    "family services": ["rewriting notes", "funder reports", "letters to families", "translation", "summaries"],
    "development and comms": ["proposals", "funder reports", "emails", "social posts", "summaries"],
    "programmes": ["emails", "translation", "social posts", "letters to families"],
    "operations and management": ["emails", "summaries", "board papers"],
}

FREETEXT = {
    "family services": ["The Adler-Haddad narratives. Every quarter.", "דוחות לקרנות, כל רבעון מחדש",
                        "כתיבת סיכומים אחרי ביקורי בית", "ترجمة الرسائل للعائلات والتقارير",
                        "Отчёты для фондов на английском", "Writing the same family story three times",
                        "הנרטיבים לאדלר-חדאד", "Phone tag with welfare offices"],
    "development and comms": ["Every funder wants a different template", "Reports, reports, reports",
                              "Rewriting boilerplate", "Giving Tuesday", "Finding numbers for reports"],
    "programmes": ["Volunteer scheduling", "WhatsApp groups", "Weekend care sheets", "שיבוץ מתנדבים"],
    "operations and management": ["Email", "Approvals", "Board papers", "Passwords and access requests"],
}


def survey_freetext(r: random.Random, group: str) -> str:
    return r.choice(FREETEXT[group])


DONOR_NOTES_PLAIN = ["met at 2025 gala", "prefers WhatsApp", "board member", "former volunteer", "company match",
                     "ask in December", "thank by phone", "do not call on Fridays", "American Friends",
                     "standing order since 2018", "gave in memory of father", "lawyer, pro bono contact"]
DONOR_NOTES_SENSITIVE = ["daughter in our respite programme", "son (autism) in coordination with Samah",
                         "grandson is one of our families", "parent of a child in the siblings programme",
                         "his son has CP, family since 2015", "lost husband 2024, gives in his name",
                         "her daughter's diagnosis came in 2023", "family in welfare referral, gives small monthly",
                         "בן במסגרת הפוגה", "ابنها في البرنامج"]

# Case-note building blocks (pseudonymised: [NAME] for people; some leaks are planted on purpose).
NOTE_OPEN = {
    "he": ["שיחה עם האם [NAME].", "ביקור בית אצל המשפחה.", "שיחת טלפון עם האב [NAME].", "פגישה בסניף."],
    "ar": ["مكالمة مع الأم [NAME].", "زيارة بيتية للعائلة.", "مكالمة مع الأب [NAME].", "لقاء في المكتب."],
    "ru": ["Звонок маме [NAME].", "Визит на дом.", "Разговор с отцом [NAME].", "Встреча в офисе."],
    "en": ["Call with mother [NAME].", "Home visit.", "Call with father [NAME].", "Meeting at the office."],
}
NOTE_BODY = {
    "he": ["הילד [NAME] בן {age}, ממתין לוועדת השמה. האם מותשת, לא ישנה לילות.",
           "ערעור על גמלת ילד נכה נדחה; נקבעה פגישה עם אלי (זכויות).",
           "האב עובד במשמרות; קשה להגיע לטיפולים. הוצע סוף שבוע הפוגה.",
           "האחות הגדולה מתקשה בבית הספר; הפניה לתוכנית האחים.",
           "המשפחה מקבלת ליווי ממחלקת הרווחה; תיאום עם העובדת הסוציאלית בעירייה."],
    "ar": ["الطفل [NAME] عمره {age}، ينتظر لجنة التنسيب. الأم متعبة جداً.",
           "رُفض الاستئناف على مخصصات الطفل المعاق؛ موعد مع إيلي للحقوق.",
           "الأب يعمل بورديات؛ صعوبة في الوصول للعلاجات. اقترحنا عطلة نهاية أسبوع.",
           "العائلة تتلقى مرافقة من قسم الرفاه؛ تنسيق مع العاملة الاجتماعية في البلدية."],
    "ru": ["Ребёнок [NAME], {age} лет, ждёт комиссию по распределению. Мама очень устала.",
           "Апелляция по пособию на ребёнка-инвалида отклонена; встреча с Эли (права).",
           "Отец работает посменно, трудно возить на терапии. Предложили выходные отдыха.",
           "Семья на учёте в отделе социального обеспечения; координация с муниципалитетом."],
    "en": ["The child [NAME], {age}, is waiting for the placement committee. Mother exhausted.",
           "Disabled-child benefit appeal rejected; meeting set with Eli (rights).",
           "Father works shifts; hard to get to therapies. Offered a respite weekend.",
           "Family followed by the welfare department; coordinating with the municipal social worker."],
}
NOTE_NEXT = {
    "he": ["המשך: לשלוח מכתב לוועדה עד יום ה'.", "המשך: שיחה בעוד שבועיים.", "המשך: לבדוק זכאות לסייעת."],
    "ar": ["الخطوة التالية: رسالة للجنة حتى الخميس.", "الخطوة التالية: مكالمة بعد أسبوعين."],
    "ru": ["Дальше: письмо в комиссию до четверга.", "Дальше: звонок через две недели."],
    "en": ["Next: letter to the committee by Thursday.", "Next: call again in two weeks."],
}
# Identifiers the export's pseudonymisation missed (planted in a few notes).
LEAKS = [
    ("he", "Child's name written in full: Yonatan Ben-Shushan."),
    ("he", "ת\"ז של האם נרשמה בטעות: 000-412-338."),
    ("ar", "رقم هاتف الأم: 050-000-4471."),
    ("he", "School: Ha-Rimon special-education school, Kiryat Bialik; the only pupil there on home ventilation."),
    ("ru", "Мама просила писать на её почту irina.k.home@gmail.com."),
    ("ar", "Hospital: Rambam paediatric neurology, appointment 3 Nov; ID on referral form 000-219-774."),
    ("he", "נועם חזר מאשפוז ביום שני, ההורים מבקשים דחייה של הוועדה."),
    ("ar", "كريم بدأ العلاج الطبيعي هذا الأسبوع في المركز."),
    ("am", "Grandmother [NAME] Hailemariam, Kiryat Bialik, the only Ethiopian-Israeli family on Hashoshanim St."),
]
