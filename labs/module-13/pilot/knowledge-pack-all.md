# Kinneret Plastics maintenance knowledge pack v1 (all documents)

22 documents, approved 2027-03-03. Upload this one file to a chat tool for Track A. Each document starts with its id, language, revision and owner.

# MAN-CHL · ArcticFlow AC-40 chiller — manual (extract)

- Document: MAN-CHL
- Language: English
- Revision: 2016 (maker)
- Owner: Maintenance manager (Vladimir Kaplan)
- In pack v1: approved 2027-03-03

## Alarms

HP1 high refrigerant pressure: clean the condenser and check the fan. FL1 low water flow: check the pump,
the strainer and that the valves to the machines are open. LT1 low water temperature: setpoint too low.

## Setpoint

Standard water setpoint for moulds: 12 °C. Do not set below 8 °C without glycol.


---

# MAN-DRY · DryMax DM-150 desiccant dryer — manual (extract)

- Document: MAN-DRY
- Language: English
- Revision: 2014 (maker)
- Owner: Maintenance manager (Vladimir Kaplan)
- In pack v1: approved 2027-03-03

## Dew point

Target dew point: −40 °C. Alarm DP-HI: dew point above −20 °C. Check the process air filter and the
regeneration heater (3.5 kW).

## Maintenance

Clean the process air filter weekly. Replace the desiccant every 3 years.

## Drying times (guide)

PA6: 4 hours at 80 °C. PC: 4 hours at 120 °C. PBT: 4 hours at 120 °C. PP and PE normally need no drying.


---

# MAN-HRC · ThermoFlow HRC-24 hot runner controller — operating manual (extract)

- Document: MAN-HRC
- Language: English
- Revision: Rev. 3, 2020 (maker)
- Owner: Maintenance manager (Vladimir Kaplan)
- In pack v1: approved 2027-03-03

## Error codes

| Code | Meaning | Action |
|---|---|---|
| E1 | Heater open circuit | Check heater resistance and cable. The zone cannot heat. |
| E2 | Heater short circuit | Switch off the zone. Check the cable and connector. |
| E3 | Thermocouple open | The zone stops heating. The operator may switch the zone to manual (% output) as a temporary measure only. |
| E4 | Thermocouple reversed | Check wiring polarity. |
| E5 | Over temperature | Zone above setpoint plus alarm band. Check the TC position and the output stage. |

## Soft start

At power-up the controller holds all zones at 100 °C for 20 minutes to dry moisture out of the heaters.
Do not skip the soft start: wet heaters can short.

## Setpoints

Never set a zone above the maximum temperature on the mould card. Typical manifold and tip settings: PP
220–240 °C, PE 210–230 °C, PA 280–290 °C. A blocked tip is not cleared by raising temperature above the
mould card maximum: check heater resistance and the thermocouple, then call the toolmaker.


---

# MAN-HW · Haiwei HW and HW-3 series — user manual (English edition, extract)

- Document: MAN-HW
- Language: English
- Revision: HW 2006; HW-3 2016 (maker)
- Owner: Maintenance manager (Vladimir Kaplan)
- In pack v1: approved 2027-03-03

## Alarm list

| Alarm | Text on screen | What to do |
|---|---|---|
| AL-012 | OIL TEMP OVER | Oil is over 55 °C. Please check cooling water open and oil cooler clean. |
| AL-015 | OIL LEVEL LOW | Please add oil ISO VG 46 after find the leak. |
| AL-021 | PUMP PRESSURE LOW | Check pump motor turning direction and suction filter. |
| AL-033 | HEATER ZONE ERR | Heater band or solid state relay is fault, please check. |
| AL-034 | THERMOCOUPLE BREAK | Thermocouple is type J, replace it. |
| AL-041 | SAFETY DOOR OPEN | Close the door. If door is closed and alarm stay, the limit switch is fault: change switch, do not short circuit it. |
| AL-055 | SERVO ALARM (HW-3 only) | Power off 1 minute and on again. If alarm come back, read the drive code and call service. |
| AL-061 | MOLD HOT RUNNER ALM | The hot runner controller sends alarm. See the hot runner controller. |

## Maintenance intervals

Hydraulic oil ISO VG 46: change every 6,000 working hours. Oil filter: every 1,500 working hours. Check ring
of the screw: inspect every 12 months or when cushion is not stable. HW series (old) machines have no
accumulator. HW-3 servo-pump machines have no accumulator.

## Heater band

Before change heater, switch off and lock main switch. Wait barrel cool down. Clamp screw torque 5 Nm.


---

# MAN-KX · Kessler KX / KX-e injection moulding machines — operation and maintenance manual (extract)

- Document: MAN-KX
- Language: English
- Revision: Ed. 2019; KX-e supplement 2024 (maker)
- Owner: Maintenance manager (Vladimir Kaplan)
- In pack v1: approved 2027-03-03

## KX alarm codes (extract)

| Code | Meaning | First action |
|---|---|---|
| E-201 | Hydraulic oil temperature high (above 55 °C) | Check cooling-water flow to the oil cooler and the cooler for fouling. Do not restart above 55 °C. |
| E-207 | Hydraulic oil level low | Stop the pump. Look for leaks before topping up (oil type: ISO VG 46 HLP). |
| E-212 | Pump pressure low | Check pump coupling and suction filter; listen for cavitation noise. |
| E-217 | Proportional valve feedback error | Check the amplifier card LED and the coil resistance (18–22 Ω). Replace the coil if out of range. |
| E-230 | Barrel heater zone deviation | Check heater band current and the zone thermocouple. |
| E-231 | Thermocouple open circuit | Replace the thermocouple (type J). |
| E-240 | Safety gate monitoring fault | The machine must not be operated. Replace the faulty gate switch. Never bridge the gate circuit. |
| E-255 | Servo drive fault | Reset once. If it repeats, check the drive fan and call Kessler service. |

## Hydraulic oil and filters

Use ISO VG 46 HLP oil. Change the oil every 8,000 operating hours or every 2 years, whichever comes first.
Change the pressure filter element every 2,000 operating hours or when the clogging indicator is red. Take
an oil sample every 4,000 operating hours; target cleanliness NAS 7 or better.

## Accumulator (KX 450 and above, all KX-e)

The hydraulic accumulator is pre-charged with nitrogen to 120 bar at 20 °C. Check the pre-charge every 6
months with the charging kit. Before any work on the hydraulic circuit or inside the clamp area, open the
accumulator discharge valve and verify 0 bar on gauge PG-3. A charged accumulator can move the clamp
with the motor switched off.

## Replacing a barrel heater band

Lock out the machine (site lockout procedure). Let the barrel cool below 50 °C. Disconnect the band at
the terminal box, not at the band. Fit the new band with the gap aligned with the old position and tighten
the clamp screw to 6 Nm. Re-tighten after the first heat-up.

## Nozzle tip

Tighten the nozzle tip hot, at processing temperature, to 85 Nm. Never tighten a cold nozzle tip.

## Clamp (toggle) lubrication

The central lubrication runs every 400 cycles. Grease the toggle pins with EP2 grease weekly. Lubrication
alarm W-12 means the lube tank is empty.

## Safety gate daily test

Every shift: open the front safety gate during a dry cycle. All movement must stop at once. Record the test
in the machine log. If any movement continues, lock out the machine and call maintenance.

## KX-e condition monitoring (2024 supplement)

The KX-e records oil temperature, pump pressure (95th percentile per hour), motor vibration (mm/s RMS) and
accumulator minimum pressure. The machine shows a yellow warning when motor vibration exceeds 4.5 mm/s for
more than one hour, and a red warning above 7.1 mm/s. Warnings are shown on the machine screen only; they
are sent to a historian only if the customer connects one.


---

# MAN-MP · Morandi MP series — maintenance manual (English translation from Italian, extract)

- Document: MAN-MP
- Language: English
- Revision: Ed. 2008 (maker)
- Owner: Maintenance manager (Vladimir Kaplan)
- In pack v1: approved 2027-03-03

## Alarms

| Alarm | Message (Italian on screen) | Meaning and action |
|---|---|---|
| A101 | Temperatura olio alta | Oil temperature above 55 °C: check cooling water and exchanger. |
| A114 | Pressione pompa bassa | Low pump pressure: check pump, valves, suction. |
| A117 | Livello olio basso | Low oil level: find the leak, then top up with ISO VG 46. |
| A120 | Riscaldamento zona guasto | Barrel heating zone fault: check heater band and fuse. |
| A131 | Termocoppia interrotta | Thermocouple open: replace (type J). |
| A140 | Porta di sicurezza aperta | Safety door open or door switch faulty. Do not bypass. |
| A152 | Errore azionamento | Drive error: reset; if repeated call service. |
| A160 | Allarme canale caldo | Hot runner alarm from the mould: see the hot runner controller. |

## Accumulator

All MP machines have a hydraulic accumulator with nitrogen pre-charge of 140 bar. Before work on the
hydraulic system, discharge the accumulator with valve V-9 and verify zero pressure on the gauge.

## Oil

ISO VG 46. Change every 5,000 hours. Filter every 1,500 hours.


---

# SOP-DRY-06 · נוהל תגובה להתראת מייבש

- Document: SOP-DRY-06
- Language: Hebrew
- Revision: A (2021-11-21)
- Owner: מנהל אחזקה
- In pack v1: approved 2027-03-03

## התראת DP-HI

נקה פילטר אוויר. אם נקודת הטל גבוהה מ-מינוס 20 מעלות יותר מ-30 דקות: עצור את המכונות שמוזנות מהמייבש בחומרים רגישים ללחות (PA, PC, PBT) והודע לראש המשמרת.
PP ו-PE לא דורשים ייבוש.


---

# SOP-ESC-07 · إجراء التصعيد في الوردية الليلية

- Document: SOP-ESC-07
- Language: Arabic
- Revision: C (2025-03-30)
- Owner: מנהלת תפעול
- Translation of the Hebrew revision C, approved 2027-03-03 by the safety officer and a native-speaking senior technician; the Hebrew text prevails

## ترتيب الاتصال

1. فني المناوبة الأول (حسب جدول المناوبات على لوحة الإعلانات في مكتب الصيانة).
2. مدير الصيانة: فقط إذا لم تصل إلى فني المناوبة خلال 15 دقيقة، أو في حدث سلامة.
3. حدث سلامة: أيضاً مسؤول السلامة يعقوب دهان.


---

# SOP-ESC-07 · נוהל הסלמה במשמרת לילה

- Document: SOP-ESC-07
- Language: Hebrew
- Revision: C (2025-03-30)
- Owner: מנהלת תפעול
- In pack v1: approved 2027-03-03

## סדר פנייה

1. טכנאי כונן בכיר (לפי לוח הכוננויות על לוח המודעות במשרד האחזקה).
2. מנהל האחזקה: רק אם לא השגת את הכונן תוך 15 דקות, או באירוע בטיחות.
3. אירוע בטיחות: גם ממונה הבטיחות, יעקב דהן.

## כלל

מכונה עם תקלת בטיחות (מגן, אינטרלוק, דליפת שמן גדולה) נשארת נעולה עד תיקון. אין להחזיר לייצור בלי בדיקת פונקציה.


---

# SOP-ESC-07 · Порядок эскалации в ночную смену

- Document: SOP-ESC-07
- Language: Russian
- Revision: C (2025-03-30)
- Owner: מנהלת תפעול
- Translation of the Hebrew revision C, approved 2027-03-03 by the safety officer and a native-speaking senior technician; the Hebrew text prevails

## Порядок звонков

1. Старший дежурный техник (по графику дежурств на доске в отделе обслуживания).
2. Начальник отдела обслуживания: только если дежурного нет 15 минут или при событии безопасности.
3. Событие безопасности: также инженер по технике безопасности Яаков Даан.


---

# SOP-GATE-08 · إجراء أعطال باب الحماية والإنترلوك

- Document: SOP-GATE-08
- Language: Arabic
- Revision: A (2022-04-03)
- Owner: ממונה בטיחות
- Translation of the Hebrew revision A, approved 2027-03-03 by the safety officer and a native-speaking senior technician; the Hebrew text prevails

## قاعدة

ممنوع تجسير أو تجاوز أو تعطيل مفتاح باب الحماية أو الإنترلوك، ولا حتى "لبضع حقنات".

## الإصلاح

الماكينة مقفلة (إجراء LOTO-01) حتى استبدال المفتاح. بعد الإصلاح: فحص وظيفي — فتح الباب أثناء دورة جافة يوقف كل حركة.


---

# SOP-GATE-08 · נוהל תקלות דלת מגן ואינטרלוק

- Document: SOP-GATE-08
- Language: Hebrew
- Revision: A (2022-04-03)
- Owner: ממונה בטיחות
- In pack v1: approved 2027-03-03

## כלל ברזל

אסור לגשר, לעקוף או לנטרל מתג דלת מגן או אינטרלוק, גם לא "לכמה זריקות".

## תיקון

המכונה נעולה (נוהל LOTO-01) עד החלפת המתג. אחרי התיקון: בדיקת פונקציה — פתיחת הדלת במחזור יבש עוצרת כל תנועה. רשום בהזמנת העבודה.


---

# SOP-GATE-08 · Порядок при неисправности защитной двери и блокировки

- Document: SOP-GATE-08
- Language: Russian
- Revision: A (2022-04-03)
- Owner: ממונה בטיחות
- Translation of the Hebrew revision A, approved 2027-03-03 by the safety officer and a native-speaking senior technician; the Hebrew text prevails

## Правило

Запрещено перемыкать, обходить или отключать выключатель защитной двери или блокировку, даже «на несколько впрысков».

## Ремонт

Машина заблокирована (LOTO-01) до замены выключателя. После ремонта: функциональная проверка — открытие двери в сухом цикле останавливает любое движение.


---

# SOP-HR-03 · إجراء الاستجابة الأولى لعطل الهوت رنر

- Document: SOP-HR-03
- Language: Arabic
- Revision: B (2024-06-02)
- Owner: מנהל כלים
- Translation of the Hebrew revision B, approved 2027-03-03 by the safety officer and a native-speaking senior technician; the Hebrew text prevails

## خطأ E3 في التيب (ثرموكبل مقطوع)

يُسمح بالاستمرار بالوضع اليدوي (نسبة مئوية) حتى 30 دقيقة فقط، بموافقة رئيس الوردية، وبشرط أن تفحص مراقبة الجودة المنتجات كل 15 دقيقة. غير ذلك: أوقف الماكينة واستدعِ قسم القوالب.

## درجات الحرارة

ممنوع رفع أي منطقة فوق الحد الأقصى في بطاقة القالب. التيب المسدود لا يُفتح برفع الحرارة.


---

# SOP-HR-03 · נוהל תגובה ראשונה לתקלת הוט ראנר

- Document: SOP-HR-03
- Language: Hebrew
- Revision: B (2024-06-02)
- Owner: מנהל כלים
- In pack v1: approved 2027-03-03

## שגיאה E3 בטיפ (תרמוקפל פתוח)

מותר להמשיך במצב ידני (אחוזים) עד 30 דקות בלבד, באישור ראש המשמרת, ובתנאי שבקרת איכות בודקת מוצרים כל 15 דקות.
אחרת: עצור את המכונה וקרא לכלים.

## טמפרטורות

אסור להעלות אף אזור מעל הטמפרטורה המקסימלית בכרטיס התבנית. טיפ סתום לא פותחים בהעלאת טמפרטורה: עצור וקרא לכלים.

## הפעלה אחרי עצירה ארוכה

אל תדלג על חימום רך (Soft start) של הבקר: 20 דקות ב-100 מעלות.


---

# SOP-HR-03 · Порядок первых действий при неисправности горячеканальной системы

- Document: SOP-HR-03
- Language: Russian
- Revision: B (2024-06-02)
- Owner: מנהל כלים
- Translation of the Hebrew revision B, approved 2027-03-03 by the safety officer and a native-speaking senior technician; the Hebrew text prevails

## Ошибка E3 на сопле (обрыв термопары)

Разрешено продолжать в ручном режиме (%) не более 30 минут, с разрешения начальника смены и при проверке деталей ОТК каждые 15 минут. Иначе: остановить машину и вызвать инструментальный участок.

## Температуры

Запрещено поднимать любую зону выше максимума из карты формы. Забитое сопло не прочищают повышением температуры.


---

# SOP-LOTO-01 · إجراء القفل والوسم (LOTO) لماكينات الحقن

- Document: SOP-LOTO-01
- Language: Arabic
- Revision: D (2023-05-14)
- Owner: ממונה בטיחות
- Translation of the Hebrew revision D, approved 2027-03-03 by the safety officer and a native-speaking senior technician; the Hebrew text prevails

## الخطوات

1. أبلغ رئيس الوردية والمشغّل أن الماكينة تتوقف للصيانة.
2. أوقف الماكينة إيقافاً عادياً (نهاية الدورة).
3. أطفئ المفتاح الرئيسي، اقفله بقفلك الشخصي وعلّق بطاقة باسمك والتاريخ.
4. أطفئ مضخة الهيدروليك.
5. السخانات مطفأة لكن الأسطوانة تبقى ساخنة: اعمل بقفازات حرارية.
6. في الماكينات التي فيها مُراكِم (Kessler KX 450 وما فوق، كل KX-e، كل Morandi): افتح صمام تفريغ المراكم وتأكد من 0 بار على مقياس الضغط. لا تكمل قبل 0 بار.
7. حرّر ضغط الهواء المضغوط من الماكينة والروبوت.
8. تجربة التشغيل: اضغط "تشغيل"، تأكد أنه لا توجد أي حركة، وارجع إلى وضع الإطفاء.
9. الآن فقط يُسمح بفتح الواقي والدخول إلى منطقة القالب.

## إزالة القفل

فقط من وضع القفل يزيله.


---

# SOP-LOTO-01 · נוהל נעילה ותיוג (LOTO) למכונות הזרקה

- Document: SOP-LOTO-01
- Language: Hebrew
- Revision: D (2023-05-14)
- Owner: ממונה בטיחות
- In pack v1: approved 2027-03-03

## מטרה

לוודא שאף אנרגיה (חשמל, הידראוליקה, אוויר, חום) לא תשתחרר בזמן עבודה בתוך המכונה או אזור התבנית.

## שלבים

1. הודע לראש המשמרת ולמפעיל שהמכונה נעצרת לתחזוקה.
2. עצור את המכונה בעצירה רגילה (סוף מחזור).
3. כבה את המפסק הראשי, נעל במנעול האישי שלך ותלה תווית עם שמך ותאריך.
4. כבה את משאבת ההידראוליקה.
5. גופי החימום כבויים אך הצילינדר נשאר חם: עבוד עם כפפות חום.
6. במכונות עם מצבר (Kessler KX 450 ומעלה, כל KX-e, כל Morandi): פתח את ברז פריקת המצבר ובדוק 0 בר במד הלחץ. אל תמשיך לפני 0 בר.
7. שחרר לחץ אוויר דחוס מהמכונה ומהרובוט.
8. ניסיון הפעלה: לחץ על התחלה, ודא שאין שום תנועה, החזר למצב כבוי.
9. רק עכשיו מותר לפתוח מגן ולהיכנס לאזור התבנית.

## הסרת נעילה

רק מי ששם את המנעול מסיר אותו. לפני הסרה: כל הכלים מחוץ למכונה, כל המגנים סגורים, ראש המשמרת עודכן.


---

# SOP-LOTO-01 · Порядок блокировки и маркировки (LOTO) термопластавтоматов

- Document: SOP-LOTO-01
- Language: Russian
- Revision: D (2023-05-14)
- Owner: ממונה בטיחות
- Translation of the Hebrew revision D, approved 2027-03-03 by the safety officer and a native-speaking senior technician; the Hebrew text prevails

## Шаги

1. Сообщить начальнику смены и оператору об остановке на обслуживание.
2. Остановить машину обычной остановкой (конец цикла).
3. Выключить главный выключатель, повесить личный замок и бирку с именем и датой.
4. Выключить гидронасос.
5. Нагреватели выключены, но цилиндр остаётся горячим: работать в термоперчатках.
6. На машинах с гидроаккумулятором (Kessler KX 450 и выше, все KX-e, все Morandi): открыть кран сброса аккумулятора и проверить 0 бар на манометре. Не продолжать до 0 бар.
7. Сбросить давление сжатого воздуха в машине и роботе.
8. Проверка пуском: нажать «старт», убедиться, что движения нет, вернуть в положение «выкл».
9. Только теперь можно открыть ограждение и входить в зону формы.

## Снятие замка

Замок снимает только тот, кто его повесил.


---

# SOP-MC-02 · נוהל החלפת תבנית

- Document: SOP-MC-02
- Language: Hebrew
- Revision: C (2024-02-11)
- Owner: מנהל כלים
- In pack v1: approved 2027-03-03

## לפני ההרמה

בדוק את משקל התבנית בכרטיס התבנית. כושר ההרמה של עגורן הגשר: 10 טון במפעל כנרת, 8 טון במפעל גליל.
אל תשתמש בעגורן שתווית הבדיקה התקופתית שלו פגה: עצור והודע לממונה הבטיחות.
נתק כבלי הוט ראנר ונשוף את קווי המים לפני ההרמה.

## בזמן ההרמה

השתמש רק בטבעות הרמה מדורגות, מוברגות עד הסוף. אסור לעמוד מתחת למטען.


---

# SOP-OIL-05 · נוהל שמן הידראולי: החלפה, מילוי ודגימה

- Document: SOP-OIL-05
- Language: Hebrew
- Revision: B (2024-01-07)
- Owner: מנהל אחזקה
- In pack v1: approved 2027-03-03

## מרווחי החלפה

Kessler (KX, KX-e): כל 8,000 שעות עבודה או שנתיים, המוקדם מביניהם. Haiwei: כל 6,000 שעות. Morandi: כל 5,000 שעות.
פילטר לחץ ב-Kessler: כל 2,000 שעות. דגימת שמן בכל המכונות: כל 4,000 שעות.

## מילוי

שמן ISO VG 46 HLP בלבד. לפני מילוי: מצא את הדליפה.


---

# SOP-PURGE-04 · נוהל ניקוי (פרג') וטיפול בפייה

- Document: SOP-PURGE-04
- Language: Hebrew
- Revision: B (2022-09-18)
- Owner: ממונה בטיחות
- In pack v1: approved 2027-03-03

## ציוד מגן

מגן פנים וכפפות חום חובה.

## ניקוי

נקה רק כשמגן הפרג' סגור. אסור לנקות לתוך התבנית. לכל היותר 3 זריקות ניקוי ברצף, ואז בדוק.
