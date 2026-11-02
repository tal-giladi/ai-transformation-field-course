"""Text fragments for the Harbor & Pine generator: names, customer emails, agent replies.

Everything here is fictional. Customer messages are written the way real customers write: short,
sometimes angry, with typos, mixed languages and personal details in the signature. Placeholders in
{braces} are filled by generate.py.

Languages: he = Hebrew, ar = Arabic (Palestinian/Israeli colloquial), ru = Russian, en = English.
"""

# --------------------------------------------------------------------------------------------
# Names: (Latin spelling, native spelling, gender). Staff use the Latin spelling; customers sign
# emails with the native spelling.
# --------------------------------------------------------------------------------------------
HE_FIRST = [
    ("Yossi", "יוסי", "m"), ("Moshe", "משה", "m"), ("David", "דוד", "m"), ("Eli", "אלי", "m"),
    ("Itai", "איתי", "m"), ("Noam", "נועם", "m"), ("Omer", "עומר", "m"), ("Lior", "ליאור", "m"),
    ("Ido", "עידו", "m"), ("Amit", "עמית", "m"), ("Nir", "ניר", "m"), ("Erez", "ארז", "m"),
    ("Oren", "אורן", "m"), ("Tomer", "תומר", "m"), ("Guy", "גיא", "m"), ("Yaniv", "יניב", "m"),
    ("Eyal", "אייל", "m"), ("Ofer", "עופר", "m"), ("Ronen", "רונן", "m"), ("Asaf", "אסף", "m"),
    ("Shira", "שירה", "f"), ("Maya", "מאיה", "f"), ("Yael", "יעל", "f"), ("Keren", "קרן", "f"),
    ("Efrat", "אפרת", "f"), ("Sivan", "סיון", "f"), ("Dafna", "דפנה", "f"), ("Orly", "אורלי", "f"),
    ("Liat", "ליאת", "f"), ("Hadas", "הדס", "f"), ("Inbal", "ענבל", "f"), ("Ruti", "רותי", "f"),
    ("Galit", "גלית", "f"), ("Anat", "ענת", "f"), ("Limor", "לימור", "f"), ("Osnat", "אסנת", "f"),
    ("Tigist", "טיגיסט", "f"), ("Abebe", "אבבה", "m"), ("Almaz", "אלמז", "f"), ("Worku", "וורקו", "m"),
]
HE_LAST = [
    ("Cohen", "כהן"), ("Levi", "לוי"), ("Mizrahi", "מזרחי"), ("Biton", "ביטון"), ("Dahan", "דהן"),
    ("Friedman", "פרידמן"), ("Azoulay", "אזולאי"), ("Malka", "מלכה"), ("Ohayon", "אוחיון"),
    ("Shapiro", "שפירא"), ("Golan", "גולן"), ("Ben-David", "בן דוד"), ("Amar", "עמר"),
    ("Gabay", "גבאי"), ("Sasson", "ששון"), ("Weiss", "וייס"), ("Segal", "סגל"), ("Barak", "ברק"),
    ("Navon", "נבון"), ("Elbaz", "אלבז"), ("Rosen", "רוזן"), ("Harel", "הראל"), ("Carmi", "כרמי"),
    ("Yosef", "יוסף"), ("Hazan", "חזן"), ("Tesfaye", "טספאי"), ("Mekonen", "מקונן"), ("Vaknin", "וקנין"),
]
AR_FIRST = [
    ("Ahmad", "أحمد", "m"), ("Mahmoud", "محمود", "m"), ("Yousef", "يوسف", "m"), ("Omar", "عمر", "m"),
    ("Khaled", "خالد", "m"), ("Fadi", "فادي", "m"), ("Wassim", "وسيم", "m"), ("Jamal", "جمال", "m"),
    ("Muhammad", "محمد", "m"), ("Bilal", "بلال", "m"), ("Nadia", "نادية", "f"), ("Rania", "رانيا", "f"),
    ("Hiba", "هبة", "f"), ("Maysa", "ميساء", "f"), ("Amal", "أمل", "f"), ("Reem", "ريم", "f"),
    ("Haneen", "حنين", "f"), ("Suha", "سهى", "f"), ("Samah", "سماح", "f"), ("Rasha", "رشا", "f"),
]
AR_LAST = [
    ("Khoury", "خوري"), ("Nasser", "ناصر"), ("Abu-Saleh", "أبو صالح"), ("Mansour", "منصور"),
    ("Darwish", "درويش"), ("Zoabi", "زعبي"), ("Hamdan", "حمدان"), ("Badir", "بدير"),
    ("Shehadeh", "شحادة"), ("Masarwa", "مصاروة"), ("Kiwan", "كيوان"), ("Saliba", "صليبا"),
    ("Jabareen", "جبارين"), ("Agbaria", "اغبارية"), ("Halabi", "حلبي"),
]
RU_FIRST = [
    ("Natalia", "Наталья", "f"), ("Irina", "Ирина", "f"), ("Svetlana", "Светлана", "f"),
    ("Ksenia", "Ксения", "f"), ("Marina", "Марина", "f"), ("Anna", "Анна", "f"), ("Yulia", "Юлия", "f"),
    ("Elena", "Елена", "f"), ("Tatiana", "Татьяна", "f"), ("Larisa", "Лариса", "f"),
    ("Dmitri", "Дмитрий", "m"), ("Alex", "Алекс", "m"), ("Vladimir", "Владимир", "m"),
    ("Pavel", "Павел", "m"), ("Boris", "Борис", "m"), ("Artem", "Артём", "m"), ("Mikhail", "Михаил", "m"),
    ("Leonid", "Леонид", "m"), ("Roman", "Роман", "m"), ("Evgeni", "Евгений", "m"),
]
# Russian surnames: (Latin, Cyrillic, has a feminine -a form)
RU_LAST = [
    ("Ivanov", "Иванов", True), ("Volkov", "Волков", True), ("Orlov", "Орлов", True),
    ("Fedorov", "Фёдоров", True), ("Zaitsev", "Зайцев", True), ("Smirnov", "Смирнов", True),
    ("Belov", "Белов", True), ("Kogan", "Коган", False), ("Rabinovich", "Рабинович", False),
    ("Gurevich", "Гуревич", False), ("Kaplan", "Каплан", False), ("Lerner", "Лернер", False),
    ("Shevchenko", "Шевченко", False), ("Melnik", "Мельник", False),
]
EN_FIRST = [
    ("Daniel", "m"), ("Rachel", "f"), ("Jonathan", "m"), ("Sarah", "f"), ("Ethan", "m"),
    ("Rebecca", "f"), ("Michael", "m"), ("Hannah", "f"), ("Benjamin", "m"), ("Leah", "f"),
    ("Aaron", "m"), ("Naomi", "f"), ("Josh", "m"), ("Emily", "f"),
]
EN_LAST = ["Miller", "Green", "Goldberg", "Stein", "Adler", "Brooks", "Fischer", "Klein", "Baker",
           "Morris", "Wolf", "Hart", "Sterling", "Price"]

STREETS_HE = ["הרצל", "ז'בוטינסקי", "רוטשילד", "ויצמן", "בן גוריון", "העצמאות", "הנשיא", "סוקולוב",
              "אחד העם", "הגפן", "הזית", "האלון", "רמב\"ם", "ביאליק"]
STREETS_EN = ["Herzl St", "Jabotinsky St", "Weizmann St", "HaNasi Blvd", "Ben Gurion Blvd",
              "Sokolov St", "HaGefen St"]

# --------------------------------------------------------------------------------------------
# Customer emails. Keys are the TRUE category (the answer key), not the helpdesk category.
# Each language has several templates; generate.py picks one and fills it.
# --------------------------------------------------------------------------------------------
BODIES = {
    "wismo": {
        "he": [
            "שלום,\nהזמנתי {product} ב-{order_date} (הזמנה {order}) ונאמר לי שהמשלוח יגיע עד {promised}. התאריך עבר ואף אחד לא חזר אליי.\nאיפה ההזמנה???",
            "היי, רציתי לברר מה הסטטוס של הזמנה {order}. באתר כתוב 'בטיפול' כבר כמה שבועות. אנחנו נכנסים לדירה חדשה וחייבים לדעת מתי זה מגיע",
            "שלום רב,\nביום {order_date} רכשתי באתר {product}. הובטח משלוח עד {promised}. עד היום לא קיבלתי שום עדכון, לא SMS ולא מייל. אשמח לתשובה מתי צפוי המשלוח.\nתודה",
            "מתי מגיעה ההזמנה?? מספר {order}",
            "ערב טוב, ההזמנה שלי {order} הייתה אמורה להגיע השבוע. אפשר לדעת מה קורה איתה? לקחתי יום חופש מהעבודה בשביל זה",
            "שלום. אני מחכה ל{product} כבר יותר מחודש וחצי. בטלפון אי אפשר להשיג אף אחד, מחכים 20 דק'. מה קורה עם ההזמנה {order}?",
            "הי, יש עדכון לגבי המשלוח? הזמנה {order}. תודה מראש",
        ],
        "ru": [
            "Здравствуйте!\nЯ заказала у вас {product} {order_date}, номер заказа {order}. Обещали доставку до {promised}. Срок прошёл, никто не звонит и не пишет. Где мой заказ?",
            "Добрый день. Подскажите пожалуйста статус заказа {order}. Ждём уже больше месяца, на сайте ничего не меняется.",
            "Здравствуйте, когда будет доставка? Заказ {order}. Спасибо",
            "Добрый вечер. Мы купили {product} в шоуруме, сказали привезут до {promised}. Уже прошло, никакой информации. Пожалуйста ответьте на русском, иврит плохо понимаю.",
        ],
        "ar": [
            "مرحبا،\nطلبت {product} بتاريخ {order_date}، رقم الطلب {order}، وحكولي التوصيل لغاية {promised}. التاريخ مر وما حدا حكى معي. وين الطلبية؟",
            "السلام عليكم، بدي اعرف شو صار بالطلب رقم {order}. صار الي اكثر من شهر بستنى",
            "مساء الخير، متى بوصل الطلب؟ {order}",
            "مرحبا، اشترينا {product} من المعرض بحيفا وحكولي بوصل قبل {promised}. لليوم ما في اي خبر. بترجاكم ردو علي",
        ],
        "en": [
            "Hi,\nI ordered a {product} on {order_date} (order {order}). The website said delivery by {promised}. That date has passed and I haven't heard anything. Can you tell me when it will arrive?",
            "Hello, any update on order {order}? Still waiting. Thanks",
            "Hi there, we're still waiting for our {product}. Order {order}, promised for {promised}. Could someone give me an actual date please?",
        ],
    },
    "wismo_early": {
        "he": [
            "שלום, הזמנתי {product} לפני כמה שבועות. רק רציתי לוודא שהמשלוח עדיין בזמן ל-{promised}? יש לנו אירוע משפחתי",
            "היי, אפשר לדעת אם ההזמנה {order} יוצאת בזמן? תודה",
        ],
        "ru": ["Добрый вечер! Хотела уточнить, доставка {product} будет вовремя, до {promised}? Нам важно, переезжаем."],
        "ar": ["مرحبا، بدي اتأكد انه {product} رح يوصل بالموعد قبل {promised}؟ عنا عرس بالعيلة"],
        "en": ["Hi there, just checking the {product} is still on track for {promised}? We're moving that week."],
    },
    "wismo_followup": {
        "he": [
            "שוב אני. פניתי אליכם לפני כמה ימים ואמרו לי שההזמנה תגיע עד {promised}. היא לא הגיעה. אני מבקש לדבר עם מנהל.",
            "זו כבר הפנייה השלישית שלי בנושא הזמנה {order}. אם לא אקבל תאריך אמיתי עד מחר אני מבטלת את ההזמנה ופונה לחברת האשראי.",
            "קיבלתי ממכם תשובה שההזמנה 'בדרך'. בדרך מאיפה? כבר עברו 10 ימים. {order}",
            "שלום, עניתם לי שהכל בסדר וסגרתם את הפנייה. שום דבר לא בסדר, המוצר לא הגיע!! הזמנה {order}",
        ],
        "ru": [
            "Пишу второй раз! Мне ответили что заказ {order} будет до {promised}. Его нет. Сколько можно ждать?",
            "Это уже третье обращение. Если не получу реальную дату, буду отменять заказ.",
        ],
        "ar": [
            "هاي ثاني مرة بكتبلكم. قلتولي الطلب بوصل لغاية {promised} وما وصل. بدي احكي مع المدير.",
            "للمرة الثالثة بسأل عن الطلب {order}. اذا ما في موعد واضح بدي ألغي الطلب.",
        ],
        "en": [
            "Following up again on order {order}. I was told it would arrive by {promised}. It hasn't. I need a real date please.",
            "This is my third email. If I don't get a firm delivery date I will cancel and dispute the charge.",
        ],
    },
    "damage": {
        "he": [
            "שלום, קיבלנו היום את {product} והוא הגיע פגום - {detail}. מצרפת תמונות. מה עושים עכשיו?",
            "המשלוח הגיע היום. בפתיחת הקרטון ראינו ש{detail}. המובילים כבר הלכו. מבקש החלפה. הזמנה {order}",
            "שלום רב, {product} שהזמנו (הזמנה {order}) הגיע עם נזק: {detail}. שילמנו הרבה כסף ואנחנו מאוד מאוכזבים. מבקשים פתרון מהיר.\nכתובת למסירה: {address}",
        ],
        "ru": [
            "Здравствуйте, сегодня привезли {product}, при распаковке обнаружили повреждение: {detail}. Фото прилагаю. Прошу заменить. Заказ {order}",
            "Добрый день! Доставили заказ {order}, но {detail}. Что делать? Грузчики уже уехали.",
        ],
        "ar": [
            "مرحبا، وصلتني {product} اليوم وفيها ضرر: {detail}. بعتتلكم صور. شو الحل؟ رقم الطلب {order}",
            "السلام عليكم، الطلب {order} وصل مكسور. {detail}. بدنا تبديل بأسرع وقت",
        ],
        "en": [
            "Hi, our {product} was delivered today and it's damaged ({detail}). Photos attached. Please advise on a replacement. Order {order}",
            "Hello, order {order} arrived but {detail}. The delivery guys left before we opened the box. What now?",
        ],
    },
    "damage_followup": {
        "he": ["שלחתי תמונות של הנזק לפני שבוע ולא קיבלתי שום תשובה. מה עם ההחלפה? הזמנה {order}",
               "שלום, מה קורה עם התביעה שלי? אמרו לי שתחזרו אליי תוך כמה ימים. {order}"],
        "ru": ["Неделю назад отправила фото повреждения, ответа нет. Когда будет замена? Заказ {order}"],
        "ar": ["بعتت صور الضرر من اسبوع وما حدا رد. شو صار بالتبديل؟ {order}"],
        "en": ["I sent photos of the damage a week ago and heard nothing back. What's happening with the replacement? Order {order}"],
    },
    "assembly": {
        "he": [
            "קיבלנו את {product} אבל אין הוראות הרכבה בקופסה. איך מרכיבים? יש סרטון?",
            "שלום, חסר בורג/חלק מס' 7 בערכת ההרכבה של {product}. אפשר לשלוח?",
            "הזמנו הרכבה עם המשלוח (הזמנה {order}) והמרכיב לא הגיע. מתי הוא מגיע?",
        ],
        "ru": ["Здравствуйте, в коробке с {product} нет инструкции по сборке. Можно прислать? Заказ {order}",
               "Сборщик не пришёл, хотя мы заказывали сборку. Заказ {order}. Когда придёт?"],
        "ar": ["مرحبا، ما في تعليمات تركيب مع {product}. كيف بنركبها؟",
               "طلبنا تركيب مع التوصيل والفني ما اجا. الطلب {order}"],
        "en": ["Hi, the {product} arrived without assembly instructions. Is there a PDF or video?",
               "We paid for assembly with order {order} but the technician never showed up. When is he coming?"],
    },
    "assembly_followup": {
        "he": ["שוב לגבי ההרכבה, אף אחד לא הגיע גם היום. {order}"],
        "ru": ["Опять пишу насчёт сборки, никто так и не пришёл. {order}"],
        "ar": ["مرة ثانية بخصوص التركيب، ولا حدا اجا. {order}"],
        "en": ["Still no technician. Order {order}."],
    },
    "returns": {
        "he": [
            "אני רוצה להחזיר את {product}, הצבע לא מתאים לסלון. איך עושים החזרה ומתי אקבל זיכוי?",
            "שלום, ביטלתי את ההזמנה {order} לפני שבועיים ועדיין לא קיבלתי את הכסף בחזרה לאשראי.",
        ],
        "ru": ["Хочу вернуть {product}, не подошёл по размеру. Как оформить возврат? Заказ {order}"],
        "ar": ["بدي ارجع {product} لانه الحجم مش مناسب. كيف بعمل ارجاع؟ الطلب {order}"],
        "en": ["I'd like to return the {product}, it doesn't fit the space. How do I arrange a pickup and refund? Order {order}"],
    },
    "returns_followup": {
        "he": ["עדיין לא קיבלתי זיכוי. כבר עברו 14 יום. {order}"],
        "ru": ["Деньги так и не вернули. {order}"],
        "ar": ["لسا ما رجعولي المصاري. {order}"],
        "en": ["Still no refund on my card. Order {order}."],
    },
    "invoice": {
        "he": ["שלום, לא קיבלתי חשבונית מס על הזמנה {order}. אפשר לשלוח למייל הזה?",
               "חויבתי פעמיים באשראי על אותה הזמנה ({order}). נא לבדוק ולזכות",
               "צריך חשבונית על שם החברה, ח.פ. 51-xxxxxx. הזמנה {order}"],
        "ru": ["Добрый день, не получили чек/счёт за заказ {order}. Пришлите пожалуйста."],
        "ar": ["مرحبا، ما وصلتني فاتورة للطلب {order}. ممكن تبعتوها؟"],
        "en": ["Hi, could you send the tax invoice for order {order}? Our accountant needs it."],
    },
    "invoice_followup": {
        "he": ["עדיין לא קיבלתי את החשבונית. {order}"],
        "ru": ["Счёт так и не пришёл. {order}"],
        "ar": ["لسا ما وصلت الفاتورة. {order}"],
        "en": ["Still waiting for the invoice for {order}."],
    },
    "b2b_quote": {
        "he": [
            "שלום,\nאנו {org} ומעוניינים בהצעת מחיר ל-{n} כיסאות ו-{m} שולחנות לחדר האוכל. נבקש מחירים וזמני אספקה עד {date2}.\nבברכה,\n{native_name}, רכש",
            "היי, אנחנו משפצים קומה במשרדים ({org}). צריכים {n} כיסאות משרדיים ו-{m} שולחנות עבודה. אפשר הצעת מחיר + זמן אספקה?",
        ],
        "ru": ["Здравствуйте, мы {org}. Нужно коммерческое предложение на {n} стульев и {m} столов. Сроки поставки?"],
        "ar": ["مرحبا، نحن {org}. بدنا عرض سعر ل-{n} كرسي و-{m} طاولة. شو مدة التوريد؟"],
        "en": [
            "Dear Harbor & Pine team,\nWe are {org} and are refurbishing our lobby and restaurant. Could you quote {n} dining chairs and {m} tables, delivery before {date2}? Please include lead times.\nKind regards,\n{name}\nProcurement",
        ],
    },
    "product_question": {
        "he": ["האם {product} מגיע גם בצבע אחר? ומה זמן האספקה?",
               "שלום, מה המידות המדויקות של {product}? יעבור בדלת של 80 ס\"מ?",
               "יש לכם את {product} בתצוגה בסניף חיפה? רוצה לבוא לראות",
               "כמה זמן לוקח משלוח לאילת?"],
        "ru": ["Здравствуйте, {product} есть в другом цвете? Сколько ждать доставку?",
               "Какие точные размеры у {product}? Пройдёт в дверь 80 см?"],
        "ar": ["مرحبا، {product} في منه لون ثاني؟ وقديش مدة التوصيل؟",
               "شو قياسات {product} بالزبط؟"],
        "en": ["Is the {product} available in another finish? What's the delivery time?",
               "What are the exact dimensions of the {product}? Will it fit through an 80 cm door?"],
    },
    "complaint": {
        "he": ["המובילים היו גסי רוח והשאירו את הקרטון בכניסה לבניין, קומה 4 בלי מעלית. לא מקובל!",
               "חיכינו כל היום למשלוח ואף אחד לא הגיע ולא התקשר. הזמנה {order}. אני רוצה פיצוי.",
               "השירות שלכם פשוט מזעזע. אי אפשר להשיג אף אחד בטלפון ובמייל עונים תשובות אוטומטיות."],
        "ru": ["Грузчики были очень грубые и оставили коробки у подъезда. Это безобразие. Заказ {order}"],
        "ar": ["العمال كانوا مش محترمين وتركوا الكرتونة تحت البناية. هيك بتعاملوا الزباين؟ {order}"],
        "en": ["We waited at home all day and nobody came or called. Order {order}. This is unacceptable."],
    },
    "complaint_followup": {
        "he": ["לא קיבלתי שום התייחסות לתלונה שלי. {order}"],
        "ru": ["На мою жалобу никто не ответил. {order}"],
        "ar": ["ما حدا رد على الشكوى تبعتي. {order}"],
        "en": ["No response to my complaint. {order}"],
    },
    "reschedule": {
        "he": ["אפשר להזיז את המשלוח ליום אחר? לא נהיה בבית ביום חמישי. הזמנה {order}",
               "קיבלתי SMS על תיאום משלוח. אפשר רק אחרי 16:00? {order}\nכתובת: {address}"],
        "ru": ["Можно перенести доставку на другой день? Заказ {order}"],
        "ar": ["ممكن نأجل التوصيل ليوم ثاني؟ الطلب {order}"],
        "en": ["Can we move the delivery to next week? Order {order}"],
    },
    "other": {
        "he": ["הרגל של הכורסה נשברה אחרי שנה וחצי. יש אחריות?",
               "שלום, אני רוצה לשנות כתובת למשלוח. הכתובת החדשה: {address}",
               "מה שעות הפתיחה של התצוגה בתל אביב בחול המועד?",
               "שלום, ראיתי שאתם מחפשים עובדים למחסן בראשון. למי שולחים קו\"ח?",
               "אפשר לקבל את הקטלוג החדש במייל?"],
        "ru": ["Здравствуйте, сломалась ножка кресла через год. Это гарантия?",
               "Какие часы работы шоурума в Хайфе?"],
        "ar": ["مرحبا، رجل الكرسي انكسرت بعد سنة. في كفالة؟",
               "شو ساعات الدوام بالمعرض بحيفا؟"],
        "en": ["Hi, one leg of our armchair broke after a year. Is that covered by warranty?",
               "What are the showroom opening hours in Tel Aviv?"],
    },
    "spam": {
        "en": ["Hello,\nWe can get your website on the FIRST PAGE of Google in 7 days!!! Reply for a free audit.\nBest, Mark | SEO Growth Experts",
               "Dear Sir/Madam, we are a leading manufacturer of office chairs in Foshan with 15 years experience. Attached is our catalog. MOQ 50 pcs. Best price guaranteed.",
               "Your mailbox storage is 99% full. Click here to verify your account and avoid suspension.",
               "Partnership opportunity: increase your sales 300% with our AI-powered influencer platform. Book a call: calendly link",
               "Invoice #INV-88213 overdue - please see attached document and pay today."],
        "he": ["הלוואות עד 50,000 ש\"ח ללא בטחונות! לחץ כאן", "מבצע מיוחד על שילוט ודפוס לעסקים - 30% הנחה"],
    },
}

# Extra details for damage messages.
DAMAGE_DETAILS = {
    "he": ["יש סדק ברגל השמאלית", "הזכוכית של השולחן מנופצת", "הבד קרוע בצד", "חסרים ברגים וחלק מהמסגרת עקום",
           "יש שריטה עמוקה לאורך כל המשטח", "דלת הארון שבורה בציר"],
    "ru": ["трещина на ножке", "стекло разбито", "порвана ткань сбоку", "глубокая царапина на столешнице",
           "сломана дверца шкафа"],
    "ar": ["في شق بالرجل", "الزجاج مكسور", "القماش مقطوع من الجنب", "في خدش كبير على الطاولة", "باب الخزانة مكسور"],
    "en": ["one leg is cracked", "the glass top is shattered", "the fabric is torn on one side",
           "there's a deep scratch across the top", "a wardrobe door is broken at the hinge"],
}

# Signatures: customers often include their phone number and address (personal data).
SIGNATURES = {
    "he": ["\n\n{native_name}\n{phone}", "\n\nתודה,\n{native_name}", "\n\nנשלח מה-iPhone שלי", "\n\n{native_name} {phone}", ""],
    "ru": ["\n\nС уважением,\n{native_name}\nтел. {phone}", "\n\n{native_name}", "\n\nОтправлено с iPhone", ""],
    "ar": ["\n\n{native_name}\n{phone}", "\n\nمع الشكر\n{native_name}", ""],
    "en": ["\n\nBest,\n{name}\n{phone}", "\n\nThanks,\n{name}", "\n\nSent from my iPhone", ""],
}

# Free-text subjects customers type in email (web-form subjects come from the form's dropdown).
SUBJECTS = {
    "wismo": {"he": ["איפה ההזמנה שלי??", "הזמנה {order}", "סטטוס הזמנה", "משלוח", "Re: ההזמנה שלך התקבלה", "עיכוב במשלוח", "מתי מגיע?"],
              "ru": ["Заказ {order}", "Доставка", "Где мой заказ", "Re: ההזמנה שלך התקבלה"],
              "ar": ["الطلب {order}", "وين الطلبية", "Re: ההזמנה שלך התקבלה", "توصيل"],
              "en": ["Order {order}", "Delivery status", "Where is my order?", "Re: Your order is confirmed"]},
    "damage": {"he": ["מוצר פגום", "הגיע שבור!!", "נזק במשלוח - הזמנה {order}", "תמונות"],
               "ru": ["Повреждение", "Брак", "Заказ {order} повреждён"],
               "ar": ["ضرر", "الطلب وصل مكسور"],
               "en": ["Damaged item", "Order {order} arrived damaged", "Photos"]},
    "assembly": {"he": ["הרכבה", "הוראות הרכבה", "חסר חלק"], "ru": ["Сборка", "Инструкция"],
                 "ar": ["تركيب"], "en": ["Assembly", "Missing part", "Assembly instructions"]},
    "returns": {"he": ["החזרה", "ביטול עסקה", "זיכוי"], "ru": ["Возврат"], "ar": ["ارجاع"], "en": ["Return", "Refund"]},
    "invoice": {"he": ["חשבונית", "חיוב כפול", "חשבונית מס"], "ru": ["Счёт"], "ar": ["فاتورة"], "en": ["Invoice", "Tax invoice"]},
    "b2b_quote": {"he": ["בקשה להצעת מחיר", "הצעת מחיר - {org}"], "ru": ["Запрос цены"], "ar": ["عرض سعر"],
                  "en": ["Request for quotation", "RFQ - {org}", "Quote request"]},
    "product_question": {"he": ["שאלה על מוצר", "מידות", "צבעים", ""], "ru": ["Вопрос", ""], "ar": ["سؤال", ""],
                         "en": ["Question", "Product question", ""]},
    "complaint": {"he": ["תלונה", "שירות גרוע", "לא מקובל"], "ru": ["Жалоба"], "ar": ["شكوى"], "en": ["Complaint", "Very disappointed"]},
    "reschedule": {"he": ["תיאום משלוח", "שינוי מועד"], "ru": ["Перенос доставки"], "ar": ["تأجيل التوصيل"], "en": ["Reschedule delivery"]},
    "other": {"he": ["שאלה", "אחריות", "שעות פתיחה", "פנייה", ""], "ru": ["Вопрос", "Гарантия"], "ar": ["سؤال", "كفالة"],
              "en": ["Question", "Warranty", "Hello"]},
    "spam": {"en": ["Rank #1 on Google", "Office chairs factory direct", "Mailbox full - action required",
                    "Partnership", "Overdue invoice"], "he": ["הלוואה מהירה", "מבצע לעסקים"]},
}

# The web form has a dropdown "reason". Customers pick what they think fits.
WEBFORM_REASONS = {
    "he": {"status": "סטטוס הזמנה", "damage": "מוצר פגום", "assembly": "הרכבה", "returns": "החזרות וביטולים",
           "invoice": "חשבוניות", "b2b": "לקוחות עסקיים", "other": "אחר"},
    "en": {"status": "Order status", "damage": "Damaged item", "assembly": "Assembly", "returns": "Returns",
           "invoice": "Invoices", "b2b": "Business customers", "other": "Other"},
}
WEBFORM_SUBJECT = {"he": "פנייה מטופס צור קשר - {reason}", "en": "Contact form: {reason}"}

# --------------------------------------------------------------------------------------------
# Agent replies. "wismo_macro" is the saved reply (macro) most agents use; it repeats the date the
# web store promised. "wismo_checked" is what an agent writes after asking logistics.
# --------------------------------------------------------------------------------------------
REPLIES = {
    "wismo_macro": {
        "he": "שלום {first},\nתודה על פנייתך ועל הסבלנות. ההזמנה שלך ({order}) נמצאת בתהליך אספקה מהספק. מועד האספקה המשוער הוא {promised}. במידה ויהיה שינוי נעדכן אותך.\nבברכה,\n{agent}\nשירות לקוחות Harbor & Pine",
        "ru": "Здравствуйте, {first}!\nСпасибо за обращение. Ваш заказ {order} находится в процессе поставки. Ориентировочная дата доставки: {promised}. Если что-то изменится, мы сообщим.\nС уважением,\n{agent}\nСлужба поддержки Harbor & Pine",
        "ar": "مرحبا {first}،\nشكرا على تواصلك. طلبك {order} في مرحلة التوريد من المورد. موعد التوصيل المتوقع {promised}. اذا في اي تغيير منبلغك.\nمع الاحترام،\n{agent}\nخدمة الزبائن Harbor & Pine",
        "en": "Hi {first},\nThank you for your patience. Your order {order} is on its way from our supplier. The estimated delivery date is {promised}. We will let you know if anything changes.\nBest regards,\n{agent}\nHarbor & Pine Customer Care",
    },
    "wismo_checked": {
        "he": "שלום {first},\nבדקתי מול מחלקת הלוגיסטיקה. המכולה עם ההזמנה שלך התעכבה בדרך וצפויה להגיע לנמל ב-{eta}. לאחר שחרור מהמכס ניצור איתך קשר לתיאום משלוח. מתנצלים מאוד על העיכוב.\n{agent}",
        "ru": "Здравствуйте, {first}!\nЯ уточнила в логистике: контейнер с вашим заказом задержался в пути, ожидаемое прибытие в порт {eta}. После растаможки мы позвоним, чтобы согласовать доставку. Приносим извинения за задержку.\n{agent}",
        "ar": "مرحبا {first}،\nفحصت مع قسم اللوجستيكا. الحاوية اللي فيها طلبك تأخرت بالطريق ومتوقع توصل الميناء بتاريخ {eta}. بعد الجمارك منتواصل معك لتنسيق التوصيل. بنعتذر عن التأخير.\n{agent}",
        "en": "Hi {first},\nI checked with our logistics team. The container with your order was delayed at sea and is now expected at the port on {eta}. Once it clears customs we will call you to book delivery. We're sorry for the delay.\n{agent}",
    },
    "damage": {
        "he": "שלום {first},\nמצטערים לשמוע. פתחנו עבורך תביעת נזק מס' {claim}. נא לשלוח תמונות של הנזק ושל מדבקת הקרטון אם עוד לא שלחת. נחזור אליך לאחר בדיקה.\n{agent}\nשירות לקוחות Harbor & Pine",
        "ru": "Здравствуйте, {first}. Очень жаль. Мы открыли заявку на повреждение № {claim}. Пришлите, пожалуйста, фото повреждения и наклейки на коробке. Мы свяжемся с вами после проверки.\n{agent}",
        "ar": "مرحبا {first}، منأسف. فتحنا طلب ضرر رقم {claim}. بترجاك تبعت صور للضرر وللملصق على الكرتونة. منرجعلك بعد الفحص.\n{agent}",
        "en": "Hi {first}, we're sorry to hear that. We have opened damage claim {claim}. Please send photos of the damage and of the label on the box if you haven't already. We'll get back to you after review.\n{agent}",
    },
    "assembly": {
        "he": "שלום {first},\nמצורף קישור להוראות ההרכבה (PDF) וסרטון. אם חסר חלק, נא לציין את מספר החלק ונשלח בדואר. לתיאום מרכיב: 03-9xx-xxxx שלוחה 3.\n{agent}",
        "ru": "Здравствуйте, {first}! Отправляю ссылку на инструкцию по сборке. Если не хватает детали, напишите её номер, мы вышлем.\n{agent}",
        "ar": "مرحبا {first}، مرفق رابط لتعليمات التركيب. اذا في قطعة ناقصة ابعتلنا رقمها ومنبعتها.\n{agent}",
        "en": "Hi {first}, here is the link to the assembly guide (PDF and video). If a part is missing, send us its number and we'll post it.\n{agent}",
    },
    "returns": {
        "he": "שלום {first},\nבהתאם למדיניות ההחזרות ניתן להחזיר מוצר תוך 14 יום במצבו המקורי. דמי איסוף 250 ש\"ח. הזיכוי יבוצע תוך 14 ימי עסקים מקבלת המוצר במחסן.\n{agent}",
        "ru": "Здравствуйте, {first}. Возврат возможен в течение 14 дней в оригинальном состоянии. Стоимость вывоза 250 ₪. Деньги вернутся в течение 14 рабочих дней после получения товара на складе.\n{agent}",
        "ar": "مرحبا {first}، حسب سياسة الارجاع ممكن ترجع المنتج خلال 14 يوم بحالته الاصلية. رسوم الاستلام 250 شيكل. المبلغ برجع خلال 14 يوم عمل.\n{agent}",
        "en": "Hi {first}, you can return an item within 14 days in its original condition. Pickup costs ₪250. The refund is made within 14 business days after the item reaches our warehouse.\n{agent}",
    },
    "invoice": {
        "he": "שלום {first}, החשבונית נשלחה שוב למייל זה. אם לא התקבלה, נא לבדוק בתיקיית הספאם.\n{agent}",
        "ru": "Здравствуйте, {first}. Счёт отправлен повторно на этот адрес.\n{agent}",
        "ar": "مرحبا {first}، بعتنالك الفاتورة مرة ثانية على هاد الايميل.\n{agent}",
        "en": "Hi {first}, we've re-sent the invoice to this address. Please check your spam folder too.\n{agent}",
    },
    "b2b_quote": {
        "he": "שלום {first}, תודה על הפנייה. העברתי את הבקשה למחלקת המכירות העסקיות, נציג יחזור אליך תוך 2 ימי עסקים.\n{agent}",
        "ru": "Здравствуйте! Запрос передан в отдел корпоративных продаж, с вами свяжутся в течение 2 рабочих дней.\n{agent}",
        "ar": "مرحبا، حولنا طلبك لقسم المبيعات للشركات وراح يتواصلوا معك خلال يومين عمل.\n{agent}",
        "en": "Hi {first}, thanks for reaching out. I've passed your request to our business sales team; they will contact you within 2 business days.\n{agent}",
    },
    "product_question": {
        "he": "שלום {first}, המוצר זמין בצבעים המופיעים באתר. זמן אספקה משוער מופיע בעמוד המוצר בעת ההזמנה. מוזמנים לתצוגה בתל אביב או בחיפה.\n{agent}",
        "ru": "Здравствуйте, {first}! Доступные цвета указаны на сайте, срок доставки показан при оформлении заказа.\n{agent}",
        "ar": "مرحبا {first}، الالوان المتوفرة موجودة بالموقع، ومدة التوصيل بتظهر وقت الطلب.\n{agent}",
        "en": "Hi {first}, the available finishes are listed on the product page, and the delivery estimate is shown at checkout. You're welcome to visit our showrooms in Tel Aviv or Haifa.\n{agent}",
    },
    "complaint": {
        "he": "שלום {first}, אנו מתנצלים על החוויה. העברנו את הפנייה למנהל השירות לבדיקה מול חברת ההובלה.\n{agent}",
        "ru": "Здравствуйте, {first}. Приносим извинения. Ваше обращение передано руководителю службы поддержки.\n{agent}",
        "ar": "مرحبا {first}، منعتذر عن هالتجربة. حولنا الشكوى لمدير الخدمة.\n{agent}",
        "en": "Hi {first}, we apologise. Your complaint has been passed to our customer service manager.\n{agent}",
    },
    "reschedule": {
        "he": "שלום {first}, עדכנו את מועד המשלוח. תקבל/י SMS עם חלון הגעה יום לפני.\n{agent}",
        "ru": "Здравствуйте, {first}. Дата доставки изменена, накануне придёт SMS.\n{agent}",
        "ar": "مرحبا {first}، غيرنا موعد التوصيل، رح توصلك رسالة قبل بيوم.\n{agent}",
        "en": "Hi {first}, we've changed your delivery date. You'll get a text with the time window the day before.\n{agent}",
    },
    "other": {
        "he": "שלום {first}, תודה על פנייתך. {agent}",
        "ru": "Здравствуйте, {first}! Спасибо за обращение. {agent}",
        "ar": "مرحبا {first}، شكرا على تواصلك. {agent}",
        "en": "Hi {first}, thanks for getting in touch. {agent}",
    },
}

# What an agent pastes back when they forget to delete the chatbot's preamble.
AI_PREAMBLES = {
    "ru": ["Конечно! Вот вежливый и профессиональный ответ клиенту на русском языке:\n\n",
           "Вот улучшенная версия вашего ответа:\n\n"],
    "ar": ["بالتأكيد! إليك رداً مهذباً ومهنياً على العميل:\n\n"],
    "en": ["Certainly! Here's a polite, professional reply you can send:\n\n"],
    "he": ["בטח! הנה תשובה מנומסת ומקצועית ללקוח:\n\n"],
}
AI_PLACEHOLDER_NAME = {"ru": "[Имя клиента]", "en": "[Customer Name]", "ar": "[اسم العميل]", "he": "[שם הלקוח]"}

# Duplicates: what a customer adds when they send the same message again.
RESEND_PREFIX = {
    "he": ["שולחת שוב כי לא קיבלתי אישור\n\n", "", "(שלחתי גם בטופס באתר)\n\n"],
    "ru": ["Отправляю повторно\n\n", ""],
    "ar": ["ببعتها مرة ثانية\n\n", ""],
    "en": ["Sending again in case the first one didn't go through\n\n", ""],
}

# How agents sign their replies in each language (otherwise their first name in Latin letters).
AGENT_SIGN = {
    "Olga Petrenko": {"he": "אולגה", "ru": "Ольга"}, "Yana Kogan": {"he": "יאנה", "ru": "Яна"},
    "Sergei Novikov": {"he": "סרגיי", "ru": "Сергей"}, "Lina Khoury": {"he": "לינה", "ar": "لينا"},
    "Rami Nasser": {"he": "ראמי", "ar": "رامي"}, "Ahmad Jabareen": {"he": "אחמד", "ar": "أحمد"},
    "Samir Haddad": {"he": "סמיר", "ar": "سمير"}, "Hila Dahan": {"he": "הילה"}, "Moran Biton": {"he": "מורן"},
    "Adi Golan": {"he": "עדי"}, "Shani Ohayon": {"he": "שני"}, "Tigist Mekonen": {"he": "טיגיסט"},
    "Daniel Shaw": {"he": "דניאל"}, "Rina Azoulay": {"he": "רינה, תביעות"},
}
