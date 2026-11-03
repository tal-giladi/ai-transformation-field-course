"""Names and free text for the Lumen SaaS data room. All people and companies are fictional."""
from __future__ import annotations

# ---------- customer company names ----------
IL_WORDS = ["Ofek", "Tavor", "Carmel", "Negev", "Arava", "Galil", "Hermon", "Yarden", "Rimon", "Dekel", "Ela",
            "Gefen", "Tamar", "Alon", "Zayit", "Hadar", "Nof", "Sela", "Keshet", "Moria", "Shikma", "Kinor",
            "Lotem", "Marom", "Savyon", "Tzuf", "Yahalom", "Orot", "Shahar", "Beit Hillel", "Nahar", "Amir",
            "Bustan", "Al-Nour", "Zaitoun", "Al-Karmel", "Kfar Yasif", "Nazareth Bay", "Rahat Star", "Sakhnin"]
EU_WORDS = ["Kypros", "Athena", "Nordlicht", "Aurora", "Delta", "Helios", "Vistula", "Danube", "Olymp", "Rhein",
            "Limassol", "Thessaly", "Baltic", "Larnaca", "Dacia", "Amstel", "Kraków", "Iasi"]
US_WORDS = ["Maple", "Lakeside", "Bayview", "Summit", "Riverbend", "Pinecrest", "Harbor", "Liberty", "Cedar",
            "Granite", "Sunset", "Prairie"]
TRADES = ["Logistics", "Retail", "Clinics", "Dental", "Engineering", "Print", "Farms", "Studio", "Bakery",
          "Restaurants", "Pharmacy", "Security", "Cleaning", "Fitness", "Hotels", "Kindergartens", "Garage",
          "Care Homes", "Laundry", "Catering", "Optics", "Packaging", "Plastics", "Vet Clinic"]
SUFFIX = {"IL": ["Ltd.", "Ltd.", "", "Group"], "CY": ["Ltd", ""], "GR": ["S.A.", ""], "DE": ["GmbH"],
          "NL": ["B.V."], "PL": ["Sp. z o.o."], "RO": ["S.R.L."], "US": ["LLC", "Inc.", ""]}
DOMAIN_TLD = {"IL": ".co.il", "CY": ".com.cy", "GR": ".gr", "DE": ".de", "NL": ".nl", "PL": ".pl", "RO": ".ro",
              "US": ".com"}

# Fixed customers that the lessons and the simulation name (all fictional).
NAMED = [
    # name, tier, country, lang, seats, billing, beta, domain
    ("Ofek Logistics", "growth", "IL", "he", 140, "annual", "y", "ofek-logistics.co.il"),
    ("Bloom Studio", "starter", "IL", "he", 6, "monthly", "y", "bloomstudio.co.il"),
    ("Shaked Clinics", "enterprise", "IL", "he", 2600, "annual", "n", "shaked-clinics.co.il"),
    ("Tavor Engineering", "growth", "IL", "ru", 46, "annual", "y", "tavor-eng.co.il"),
    ("Negev Retail Group", "enterprise", "IL", "he", 400, "annual", "n", "negevretail.co.il"),
    ("Carmel Print", "growth", "IL", "he", 54, "annual", "y", "carmelprint.co.il"),
    ("Arava Farms", "growth", "IL", "he", 38, "annual", "y", "aravafarms.co.il"),
    ("Ronen Dental", "growth", "IL", "he", 26, "monthly", "y", "ronendental.co.il"),
]

# ---------- Lumen staff (fictional) ----------
FIRST = {
    "he": ["Noa", "Yael", "Tamar", "Michal", "Shira", "Maya", "Revital", "Nurit", "Ayelet", "Hila", "Yonatan", "Itai",
           "Omer", "Eyal", "Yaron", "Gal", "Roy", "Nadav", "Ariel", "Lior", "Tal", "Dana", "Oren", "Amit", "Daniel"],
    "ar": ["Amir", "Lina", "Rami", "Fatma", "Samer", "Rana", "Ahmad", "Nour", "Khaled", "Maisa", "Yousef", "Hiba"],
    "ru": ["Andrei", "Svetlana", "Boris", "Olga", "Dmitri", "Irina", "Yulia", "Sergei", "Pavel", "Anna", "Igor"],
    "am": ["Tigist", "Yonatan", "Meseret", "Avraham", "Tsega", "Bezawit", "Dawit"],
    "en": ["David", "Rachel", "Ben", "Sarah", "Jonathan", "Emma", "Michael"],
}
LAST = {
    "he": ["Levi", "Cohen", "Mizrahi", "Peretz", "Biton", "Azoulay", "Rosenthal", "Navon", "Gal", "Dahan",
           "Friedman", "Shalev", "Klein", "Barak", "Ben-David", "Weiss", "Golan", "Ashkenazi", "Katz", "Ohana"],
    "ar": ["Haddad", "Khoury", "Abu-Ras", "Nasser", "Mansour", "Darwish", "Zoabi", "Hamdan", "Saleh"],
    "ru": ["Kogan", "Volkov", "Feldman", "Petrov", "Smirnov", "Mor", "Lerner", "Orlov", "Gurevich"],
    "am": ["Tadesse", "Mekonen", "Alemu", "Tesfaye", "Wondimu", "Gebre"],
    "en": ["Miller", "Brown", "Stone", "Harris", "Gold"],
}

# ---------- session openers by topic and language ----------
# Topics follow Lumen's intent classifier labels.
MSG = {
    "billing.invoice": {
        "he": ["למה החשבונית החודש גבוהה יותר?", "אפשר לקבל עותק של החשבונית האחרונה?", "על מה החיוב של 14 משתמשים?"],
        "en": ["Why is this month's invoice higher than last month?", "Can I get a copy of the last invoice?",
               "What is the charge for 14 seats on our invoice?"],
        "ar": ["لماذا الفاتورة هذا الشهر أعلى؟", "أريد نسخة من الفاتورة الأخيرة"],
        "ru": ["Почему счёт в этом месяце больше?", "Можно получить копию последнего счёта?"],
    },
    "billing.credit": {
        "he": ["חויבנו פעמיים על אותו משתמש", "חויבנו על עובדת שעזבה בתחילת החודש"],
        "en": ["We were charged twice for the same seat.", "You billed us for an employee who left on the 1st."],
        "ar": ["تم خصم المبلغ مرتين لنفس المستخدم"],
        "ru": ["Нам дважды выставили счёт за одного сотрудника."],
    },
    "account.plan": {
        "he": ["צריך להוסיף 3 משתמשים", "רוצים לעבור מ-Starter ל-Growth"],
        "en": ["We need to add three seats.", "How do we move from Starter to Growth?"],
        "ar": ["نحتاج إلى إضافة مستخدمين اثنين"],
        "ru": ["Нужно добавить трёх пользователей."],
    },
    "account.downgrade": {
        "he": ["אנחנו עוברים משנתי Growth לחודשי Starter. מה קורה עם החודשים ששילמנו?"],
        "en": ["We're moving from annual Growth to monthly Starter. What happens to the months we already paid?"],
        "ar": ["سننتقل من الخطة السنوية إلى الشهرية، ماذا يحدث للأشهر المدفوعة؟"],
        "ru": ["Мы переходим с годового Growth на месячный Starter. Что будет с уже оплаченными месяцами?"],
    },
    "account.2fa": {
        "he": ["אני לא מצליחה להיכנס, החלפתי טלפון", "קוד האימות לא מגיע"],
        "en": ["I changed my phone and can't sign in.", "The 2FA code never arrives."],
        "ar": ["غيرت هاتفي ولا أستطيع الدخول"],
        "ru": ["Сменил телефон и не могу войти."],
    },
    "product.howto": {
        "he": ["איך מעתיקים תבנית משמרות לשבוע הבא?", "איך מגדירים הפסקה בתשלום?", "איך מאשרים החלפת משמרת?"],
        "en": ["How do I copy a shift template to next week?", "How do I set a paid break?",
               "How do I approve a shift swap?"],
        "ar": ["كيف أنسخ جدول الورديات للأسبوع القادم؟", "كيف أضيف استراحة مدفوعة؟"],
        "ru": ["Как скопировать шаблон смен на следующую неделю?", "Как настроить оплачиваемый перерыв?"],
    },
    "product.payroll": {
        "he": ["הייצוא לשכר יוצא בלי שעות נוספות", "איך מייצאים לחילן?"],
        "en": ["The payroll export is missing overtime.", "How do I export to our payroll provider?"],
        "ar": ["تصدير الرواتب لا يتضمن الساعات الإضافية"],
        "ru": ["В выгрузке для зарплаты нет сверхурочных."],
    },
    "product.bug": {
        "he": ["האפליקציה של שעון הנוכחות קורסת באנדרואיד", "הייצוא ל-CSV נתקע ב-90%"],
        "en": ["The time-clock app crashes on Android.", "The CSV export hangs at 90%."],
        "ar": ["تطبيق الساعة يتوقف على أندرويد"],
        "ru": ["Приложение учёта времени вылетает на Android."],
    },
    "data.notifications": {
        "he": ["תמחקו הכול. אני לא רוצה יותר את המיילים האלה", "יותר מדי התראות במייל"],
        "en": ["Please delete everything. I don't want any more of these emails.", "Too many notification emails."],
        "ar": ["رسائل كثيرة جدا، أوقفوها"],
        "ru": ["Слишком много уведомлений на почту."],
    },
}

TICKET_SUBJECTS = {
    "billing.invoice": ["Invoice question", "שאלה על חשבונית", "Copy of invoice", "Счёт за ноябрь"],
    "billing.credit": ["Double charge", "חיוב כפול", "Charged for leaver", "Refund request"],
    "account.plan": ["Add seats", "שינוי חבילה", "Upgrade to Growth", "Seat count wrong"],
    "account.downgrade": ["Downgrade annual plan", "מעבר לחבילה חודשית", "Unused months on annual plan"],
    "account.2fa": ["Locked out", "לא מצליח להתחבר", "2FA reset", "Phone changed"],
    "product.howto": ["How to copy template", "איך מגדירים הפסקות", "Shift swap approval", "Как настроить"],
    "product.payroll": ["Payroll export overtime", "ייצוא לשכר", "Export format", "تصدير الرواتب"],
    "product.bug": ["App crash Android", "Export stuck", "באג בשעון נוכחות", "Sync error"],
    "data.notifications": ["Too many emails", "הסרה מדיוור", "Delete my data", "Unsubscribe"],
    "account.security": ["Admin access", "Suspicious login", "Verification"],
}
