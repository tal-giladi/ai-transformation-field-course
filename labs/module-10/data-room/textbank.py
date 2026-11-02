"""Text used by generate.py (Galil Health data room). Fictional organization, people and vendors.

Reading this file spoils the engagement: finish module 10 first.
"""

# ---------------------------------------------------------------- survey free text
# (language, text, kind) kind: tool = mentions a tool they already use; other = burden or concern
SURVEY_TEXT = [
    ("he", "אני מקליטה את השיחה בטלפון ומבקשת סיכום, זה חוסך לי חצי שעה בערב", "tool"),
    ("ru", "Записываю приём на телефон, приложение делает выжимку по-русски, потом перевожу в Notara.", "tool"),
    ("ru", "Без приложения на телефоне я бы сидела до десяти вечера.", "tool"),
    ("ar", "أستعمل تطبيق تسجيل على هاتفي الخاص ثم أنسخ الملخص إلى الملف", "tool"),
    ("he", "צ'אט GPT עוזר לי לתרגם מכתבים מרוסית לעברית", "tool"),
    ("he", "יש אפליקציה שכולם במרפאה משתמשים בה, למה לא לשלם עליה רשמית?", "tool"),
    ("en", "I already use an AI note app on my own phone. Works well in Hebrew, less in Arabic.", "tool"),
    ("ar", "زميل علمني على تطبيق يلخص الزيارة، لكن لا أعرف أين تذهب التسجيلات", "tool"),
    ("he", "מקליט רק כשהמטופל מסכים בעל פה", "tool"),
    ("ru", "Пользуюсь ИИ для писем в больницу, экономит время.", "tool"),
    ("he", "ההכתבה של MedNote ב-2025 הייתה סיוט, היום יש כלים טובים יותר בחינם", "tool"),
    ("ru", "Коллеги в Кармиэле показали мне приложение, теперь записываю почти все приёмы.", "tool"),
    ("he", "הכי קשה זה ביקורים עם בני משפחה שמדברים כולם ביחד", "other"),
    ("he", "אני לא רוצה שיקליטו אותי ושזה יגיע לתלונות", "other"),
    ("ar", "المرضى كبار السن لن يوافقوا على التسجيل إذا لم نشرح لهم بالعربية", "other"),
    ("ar", "أكتب الملاحظات بالعبرية بعد زيارة بالعربية، هذا يأخذ وقتاً مضاعفاً", "other"),
    ("ru", "Главное — чтобы не путались лекарства.", "other"),
    ("ru", "Пожилые пациенты приходят с детьми, и все говорят одновременно.", "other"),
    ("he", "יותר זמן מול המטופל ופחות מול המסך", "other"),
    ("he", "מי יבדוק את הסיכום? אני. אז מה חסכנו?", "other"),
    ("en", "Please make sure whatever we buy works with the old Notara in Tiberias.", "other"),
    ("he", "בצפת עדיין גרסה ישנה של Notara, כל עדכון לוקח חודשים", "other"),
    ("ar", "أحتاج وقتاً أطول مع المريض، وليس أداة جديدة فقط", "other"),
    ("he", "האחיות מתרגמות ואף אחד לא סופר את זה", "other"),
    ("ru", "Хорошо бы, если бы врач смотрел на пациента, а не в экран.", "other"),
    ("he", "שעתיים ביום על תיעוד, לפחות", "other"),
    ("he", "עובדת מהבית בערבים כדי לסגור רשומות", "other"),
    ("en", "Happy to pilot anything that handles Arabic properly.", "other"),
    ("ar", "لا أثق بالأرقام التي يعرضها البائعون", "other"),
    ("he", "לא ברור לי מה קורה להקלטה אחרי זה", "other"),
    ("en", "Nurses translate half my afternoon list. Nobody counts that.", "other"),
    ("ar", "التمريض يترجم للأطباء الجدد طوال اليوم", "other"),
    ("he", "תנו לנו לנסות לפני שקונים לכולם", "other"),
    ("ru", "Не хочу, чтобы записи использовали для проверки врачей.", "other"),
]

# ---------------------------------------------------------------- patient-safety incidents
# Fixed incidents: (id, date, clinic, category, severity, description_he, description_en)
FIXED_INCIDENTS = [
    ("IN-2025-031", "2025-03-24", "GH-NOF", "documentation", "near_miss",
     "בהכתבה נרשם 'מטפורמין הופסק' במקום 'מטופרולול הופסק'. הרוקחת זיהתה לפני ניפוק.",
     "Dictated note recorded 'metformin stopped' instead of 'metoprolol stopped'. The pharmacist caught it before dispensing."),
    ("IN-2025-044", "2025-04-15", "GH-NAH", "documentation", "no_harm",
     "בת המטופלת אמרה בביקור שהאם הפסיקה אליקוויס; לא הופיע בסיכום שהוכתב. נרשם NSAID; זוהה ע\"י רופא המשפחה למחרת.",
     "The patient's daughter said in the visit that her mother had stopped Eliquis; it was not in the dictated summary. An NSAID was prescribed; the family doctor caught it the next day."),
    ("IN-2026-019", "2026-04-02", "GH-MAJ", "communication", "minor",
     "מטופלת דוברת ערבית נבדקה ע\"י רופא מחליף ללא מתורגמן; הוראות המינון הובנו לא נכון.",
     "An Arabic-speaking patient was seen by a substitute doctor without an interpreter; the dosing instructions were misunderstood."),
    ("IN-2026-052", "2026-09-17", "GH-KRM", "documentation", "near_miss",
     "אלרגיה לפניצילין שדווחה ע\"י בן המטופלת (ברוסית) לא הופיעה ברשומה. הרופאה ציינה שהסיכום 'מהטלפון' השמיט אותה. אחות זיהתה לפני מתן מרשם.",
     "A penicillin allergy reported by the patient's son (in Russian) was missing from the record. The doctor said the summary 'from the phone' had left it out. A nurse caught it before a prescription was issued."),
]

# Generic incident templates: (category, severity choices, he, en)
GENERIC_INCIDENTS = [
    ("fall", ["no_harm", "minor"], "נפילה של מטופל בחדר ההמתנה", "Patient fall in the waiting room"),
    ("lab", ["near_miss", "no_harm"], "תוצאת מעבדה חריגה לא נצפתה במשך שבוע", "Abnormal lab result not seen for a week"),
    ("referral", ["no_harm", "minor"], "הפניה לקרדיולוג לא נשלחה", "Cardiology referral not sent"),
    ("identification", ["near_miss"], "מדבקה עם שם מטופל אחר על מבחנה", "Another patient's label on a sample tube"),
    ("medication", ["near_miss", "no_harm", "minor"], "מינון שגוי במרשם, תוקן ע\"י הרוקח", "Wrong dose on a prescription, corrected by the pharmacist"),
    ("vaccine", ["near_miss"], "תקלה בקירור חיסונים במשך הלילה", "Vaccine fridge temperature excursion overnight"),
    ("aggression", ["no_harm", "minor"], "אלימות מילולית כלפי מזכירה", "Verbal aggression towards a receptionist"),
    ("communication", ["no_harm", "minor"], "מטופל לא קיבל הודעה על ביטול תור", "Patient not told about a cancelled appointment"),
    ("documentation", ["no_harm"], "רשומה נפתחה על שם מטופל שגוי ותוקנה", "Record opened under the wrong patient and corrected"),
    ("equipment", ["no_harm"], "מכשיר א.ק.ג. לא תקין, בדיקה נדחתה", "ECG machine faulty, test postponed"),
]

# ---------------------------------------------------------------- PoC sample visits (poc/sample-notes.md)
SAMPLE_NOTES = """# PoC sample visits and notes

Three of the 90 synthetic visits, with the script excerpt that carries the hard fact, the fact list the
reviewers checked against, and each vendor's note for the same passage (run 1). Scripts and notes are
synthetic; actors played every role. English glosses in *italics* were added by the reviewers.

## P-38 · Arabic · primary care, Majd al-Krum scenario · daughter present · air conditioner

Script excerpt:

> **الابنة:** دكتور، أمي وقفت حبة الضغط من أسبوعين لأنها كانت تدوخ.
> *Daughter: Doctor, my mother stopped the blood-pressure pill two weeks ago because she was dizzy.*
> **المريضة:** بس الحبة الصغيرة، الثانية بوخدها.
> *Patient: Only the small pill, I still take the other one.*

Facts the note must carry (3 of 11): amlodipine stopped two weeks ago by the patient; reason: dizziness;
ramipril continued.

| Vendor | The note's medication line (run 1) | Reviewer |
|---|---|---|
| ScribeWave | "Medications: continues antihypertensives. Dizziness reported." | Omission: the stopped drug is missing; "continues" is wrong for one of two |
| Kol Refua | No output: the service returned an empty note for Arabic audio | Not scored |
| MedNote for Notara | "תרופות: לחץ דם ... [לא ברור]" *Medications: blood pressure ... [unclear]* | Omission: stop, reason and continued drug all missing |
| Rishma Health | "Amlodipine: stopped by patient ~2 weeks ago due to dizziness (reported by daughter) ⚠ confirm. Ramipril: continues." | Correct; the unsure marker asked the doctor to confirm |

## P-71 · Russian · cardiology, Tiberias scenario · son present · corridor noise

Script excerpt:

> **Сын:** У мамы аллергия на пенициллин, в больнице была сыпь.
> *Son: Mum is allergic to penicillin, she had a rash in hospital.*
> **Пациентка:** Да, и на йод тоже, кажется.
> *Patient: Yes, and to iodine too, I think.*

Facts (2 of 12): penicillin allergy (rash, hospital); possible iodine allergy (uncertain).

| Vendor | Allergy line (run 1) | Reviewer |
|---|---|---|
| ScribeWave | "Allergies: penicillin (rash)." | Iodine uncertainty dropped (minor) |
| Kol Refua | "אלרגיות: לא ידוע" *Allergies: unknown* | Omission: penicillin allergy missing |
| MedNote for Notara | "אלרגיה: פניצילין" *Allergy: penicillin* | Iodine dropped (minor) |
| Rishma Health | "Allergies: penicillin (rash, per son); iodine — patient unsure ⚠ confirm." | Correct |

## P-07 · Hebrew · primary care, Safed scenario · patient alone · quiet room

Script excerpt:

> **מטופל:** אני לוקח אליקוויס פעמיים ביום, ולפעמים אדוויל לגב.
> *Patient: I take Eliquis twice a day, and sometimes Advil for my back.*

Facts (2 of 9): apixaban twice daily; occasional ibuprofen (an interaction the doctor addresses).

| Vendor | Medication line (run 1) | Reviewer |
|---|---|---|
| ScribeWave | "Apixaban 5 mg BID. Ibuprofen PRN for back pain." | Invented a dose (5 mg was never said) |
| Kol Refua | "אליקוויס פעמיים ביום; אדוויל לפי הצורך לגב." | Correct |
| MedNote for Notara | "אליקוויס פעמיים ביום." | Omission: ibuprofen missing (the interaction) |
| Rishma Health | "Apixaban twice daily. Ibuprofen occasionally for back pain — interaction discussed." | Correct |
"""
