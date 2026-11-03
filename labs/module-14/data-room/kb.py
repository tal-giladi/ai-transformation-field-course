"""Help centre: article index, revision history and the HC-214 versions."""
from __future__ import annotations

from common import ROOM, rng, write_csv, write_md

ARTICLES = [
    ("HC-101", "Copy a shift template to another week", "Support"), ("HC-102", "Set up paid and unpaid breaks", "Support"),
    ("HC-104", "Approve or reject a shift swap", "Support"), ("HC-107", "Time clock: geofencing and kiosks", "Support"),
    ("HC-110", "Overtime rules by country", "Support"), ("HC-112", "Publish a schedule and notify staff", "Support"),
    ("HC-140", "Payroll export: formats and fields", "Support"), ("HC-141", "Payroll export to Israeli payroll providers",
                                                                "Support"),
    ("HC-143", "Why overtime is missing from an export", "Support"), ("HC-150", "Known issues: mobile apps", "R&D"),
    ("HC-151", "Report a bug", "Support"), ("HC-160", "Notification settings for admins and staff", "Support"),
    ("HC-161", "Unsubscribe from product emails", "Marketing"), ("HC-201", "Read your invoice", "Billing"),
    ("HC-202", "Download invoices and receipts", "Billing"), ("HC-203", "Billing errors and credits", "Billing"),
    ("HC-205", "How seats are counted", "Billing"), ("HC-210", "Plans: Starter, Growth and Enterprise", "Marketing"),
    ("HC-211", "Change your plan", "Billing"), ("HC-214", "Downgrades and refunds", "Billing"),
    ("HC-230", "Two-step verification (2FA)", "Security"), ("HC-231", "Locked out of your account", "Security"),
    ("HC-240", "Delete your account and data", "Legal"), ("HC-241", "Privacy and your staff's data", "Legal"),
]
LANGS = ["en", "he", "ar", "ru"]
EDITORS = {"Support": "boris.feldman", "Billing": "fatma.abu-ras", "Marketing": "maisa.hamdan", "Security": "andrei.kogan",
           "Legal": "nurit.gal", "R&D": "noam.levi"}

V4_EN = """# Downgrades and refunds (HC-214) — version 4

*Published 2 November 2025 by Billing. Applies to all plans.*

## Monthly plans

You can move to a smaller plan or remove seats at any time. The change applies from your next invoice.
We don't refund the current month.

## Annual plans

You can downgrade an annual plan, but the change takes effect **at the end of your current annual term**.
Until then you keep your current plan and seats. **We don't refund or credit unused months of an annual
plan.** If you need to remove seats because staff left, contact support: we can review seat counts once a
quarter.

## Enterprise

Changes to Enterprise plans follow your contract. Talk to your account lead.

## Credits

Credits for billing errors are covered in [Billing errors and credits](HC-203).
"""

V5_EN = """# Switch plans, keep your value (HC-214)

*Campaign draft — Q4 "Right-size your plan". Do not publish before legal and billing review.*

Moving to a plan that fits your team better? **We've got you.** From November, when you switch from an
annual plan to a monthly plan, we'll **credit one month's fee for your unused months** straight to your
account — no forms, no waiting.

- Switch any time from **Settings → Plan**.
- Your credit appears on your next invoice.
- Questions? Ask Lumen Assist — it can apply your credit for you.

*Terms: annual plans with at least three unused months. Offer may change.*
"""

V5_RU = """# Смените тариф и сохраните выгоду (HC-214)

*Черновик кампании — 4-й квартал. Не публиковать до проверки юристами и биллингом.*

Переходите на тариф, который лучше подходит вашей команде? При переходе с годового тарифа на месячный мы
**зачислим на ваш счёт плату за один месяц** за неиспользованные месяцы — без форм и ожидания.

- Сменить тариф можно в **Настройки → Тариф**.
- Кредит появится в следующем счёте.
- Вопросы? Спросите Lumen Assist — он может начислить кредит сам.

*Условия: годовые тарифы, осталось не меньше трёх месяцев.*

*(English gloss added by the exporter: the page promises one month's fee as credit when switching from an
annual to a monthly plan, and says Lumen Assist can apply it.)*
"""


def write_kb() -> None:
    r = rng("kb")
    idx, rev = [], []
    for aid, title, team in ARTICLES:
        for lang in LANGS:
            n = r.randint(1, 4)
            year = 2021 + r.randint(0, 3)
            for k in range(1, n + 1):
                when = f"{min(2026, year + k - 1)}-{r.randint(1, 12):02d}-{r.randint(1, 28):02d} {r.randint(8, 18):02d}:{r.randint(0, 59):02d}"
                if lang == "en":
                    who, note = EDITORS[team], r.choice(["update", "screenshots", "wording", "new UI", "fix link"])
                else:
                    who, note = ("svc-translate" if when >= "2025-06" else EDITORS[team]), f"translation from en v{k}"
                if aid != "HC-214":
                    rev.append([aid, lang, k, when + ":00", who, team if who != "svc-translate" else "Marketing", note])
            if aid != "HC-214":
                idx.append([aid, lang, title, team, n, "published", "yes"])
    hist = [
        ("en", 1, "2021-03-14 10:02:00", "fatma.abu-ras", "Billing", "first version"),
        ("en", 2, "2023-01-08 11:40:00", "fatma.abu-ras", "Billing", "annual plans section"),
        ("en", 3, "2025-01-05 09:15:00", "fatma.abu-ras", "Billing", "Enterprise wording"),
        ("en", 4, "2025-11-02 14:30:00", "fatma.abu-ras", "Billing", "seat review once a quarter"),
        ("he", 4, "2025-11-02 15:05:00", "fatma.abu-ras", "Billing", "translation from en v4"),
        ("ar", 4, "2025-11-03 03:00:00", "svc-translate", "Marketing", "translation from en v4"),
        ("ru", 4, "2025-11-03 03:00:00", "svc-translate", "Marketing", "translation from en v4"),
        ("en", 5, "2026-11-09 16:40:00", "maisa.hamdan", "Marketing", "Q4 right-size campaign"),
        ("he", 5, "2026-11-09 16:52:00", "maisa.hamdan", "Marketing", "Q4 right-size campaign"),
        ("ar", 5, "2026-11-10 03:00:00", "svc-translate", "Marketing", "translation from en v5"),
        ("ru", 5, "2026-11-10 03:00:00", "svc-translate", "Marketing", "translation from en v5"),
        ("en", 6, "2026-11-22 14:05:00", "yonatan.tadesse", "Support", "restore v4 text"),
        ("he", 6, "2026-11-22 14:09:00", "yonatan.tadesse", "Support", "restore v4 text"),
    ]
    for lang, k, when, who, team, note in hist:
        rev.append(["HC-214", lang, k, when, who, team, note])
    for lang in LANGS:
        cur = 6 if lang in ("en", "he") else 5
        idx.append(["HC-214", lang, "Downgrades and refunds", "Billing", cur, "published", "yes"])
    idx.sort(key=lambda x: (x[0], LANGS.index(x[1])))
    rev.sort(key=lambda x: (x[0], LANGS.index(x[1]), x[2]))
    write_csv(ROOM / "support-kb" / "help-centre-articles.csv",
              ["article_id", "language", "title", "owner_team", "current_revision", "status", "searchable_by_assist"], idx)
    write_csv(ROOM / "support-kb" / "help-centre-revisions.csv",
              ["article_id", "language", "revision", "published_at", "published_by", "team", "change_note"], rev)
    write_md(ROOM / "support-kb" / "articles" / "HC-214-en-v4.md", V4_EN)
    write_md(ROOM / "support-kb" / "articles" / "HC-214-en-v5.md", V5_EN)
    write_md(ROOM / "support-kb" / "articles" / "HC-214-ru-current.md", V5_RU)
