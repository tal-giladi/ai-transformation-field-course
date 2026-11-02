"""Meridian Mutual: a no-AI baseline extractor (lesson 09.5).

    python extract_rules.py            # writes runs/rules-baseline.csv
    python extract_rules.py --negative # the 12 negative tests (pilot/negative-tests.csv)

Keyword labels in four languages plus regular expressions, written in an afternoon the way an IT
team would. It is the "what would we get without a model?" line in the eval. It reads day/month
dates, Hebrew/English/Arabic/Russian labels and Russian-style amounts. Python's `\\d` matches any
Unicode digit, so dates and amounts written in Eastern Arabic digits (٠١٢٣...) parse by accident,
but identifiers come back in Eastern digits and do not match. It does not read Russian month
names or US month/day dates, and OCR confusions (O for 0, S for 5) break it. Those gaps are the
point: compare it with the vendor and your pilot.
"""
from __future__ import annotations

import csv
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))
sys.stdout.reconfigure(encoding="utf-8")

from fieldkit.data import data_room  # noqa: E402

ROOM = data_room("module-09") / "extraction"
OUT = Path(__file__).resolve().parent / "runs" / "rules-baseline.csv"

FIELDS = {
    "claim_form": ["policy_number", "loss_date", "claimed_amount", "vehicle_plate", "currency"],
    "garage_invoice": ["invoice_number", "invoice_date", "total_amount", "vat_amount"],
    "contractor_invoice": ["invoice_number", "invoice_date", "total_amount", "vat_amount"],
    "police_confirmation": ["report_number", "event_date"],
    "assessor_report": ["inspection_date", "assessed_amount"],
    "medical_invoice_abroad": ["service_date", "total_amount", "currency"],
    "health_receipt": ["receipt_number", "service_date", "total_amount"],
}
LABELS = {
    "loss_date": ["תאריך האירוע", "تاريخ الحادث", "Дата события", "Date of incident"],
    "invoice_date": ["תאריך:", "التاريخ:", "Дата:"],
    "event_date": ["תאריך האירוע"],
    "inspection_date": ["תאריך בדיקת הרכב"],
    "service_date": ["Date of service", "Дата приёма", "תאריך הביקור", "تاريخ الزيارة"],
    "claimed_amount": ["סכום הנזק המשוער", "قيمة الضرر التقديرية", "Предполагаемая сумма ущерба", "Amount claimed"],
    "total_amount": ["סה\"כ לתשלום", "المجموع للدفع", "Итого к оплате", "TOTAL DUE", "Итого:", "התקבל סך",
                     "المبلغ المستلم", "Получено"],
    "vat_amount": ["מע\"מ 18%", "ضريبة القيمة المضافة", "НДС 18%"],
    "assessed_amount": ["סה\"כ נזק מוערך"],
    "invoice_number": ["מספר:", "מס'", "رقم:", "№"],
    "receipt_number": ["קבלה מס'", "إيصال رقم", "Квитанция №"],
}
AMOUNT = re.compile(r"(\d{1,3}(?:[ ,]\d{3})*(?:[.,]\d{2})|\d+(?:[.,]\d{2})?)")
DATE = re.compile(r"(\d{1,2})[./](\d{1,2})[./](\d{4})")
EN_DATE = re.compile(r"(\d{1,2}) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (\d{4})")
MONTHS = {m: i for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}


def line_after(text: str, labels: list[str]) -> str | None:
    for ln in text.split("\n"):
        for lab in labels:
            if lab in ln:
                return ln.split(lab, 1)[1]
    return None


def parse_date(s: str | None) -> str:
    if not s:
        return ""
    m = DATE.search(s)
    if m:
        d, mo, y = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if mo > 12:            # cannot be day/month: try month/day
            d, mo = mo, d
        try:
            return date(y, mo, d).isoformat()
        except ValueError:
            return ""
    m = EN_DATE.search(s)
    if m:
        return date(int(m.group(3)), MONTHS[m.group(2)], int(m.group(1))).isoformat()
    return ""


def parse_amount(s: str | None) -> str:
    if not s:
        return ""
    s = s.replace("₪", " ")
    found = AMOUNT.findall(s)
    if not found:
        return ""
    raw = found[-1] if len(found) > 1 and "TOTAL" not in s else found[0]
    if re.search(r",\d{2}$", raw):                 # Russian style: 10 730,00
        raw = raw.replace(" ", "").replace(",", ".")
    else:
        raw = raw.replace(",", "").replace(" ", "")
    try:
        return f"{float(raw):.2f}"
    except ValueError:
        return ""


def extract(doc_type: str, text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for f in FIELDS[doc_type]:
        v = ""
        if f == "policy_number":
            m = re.search(r"\b(\d{2}-\d{7})\b", text)
            v = m.group(1) if m else ""
        elif f == "vehicle_plate":
            m = re.search(r"\b(\d{2}-\d{3}-\d{2})\b", text)
            v = m.group(1) if m else ""
        elif f == "report_number":
            m = re.search(r"\b(\d{6}/\d{4})\b", text)
            v = m.group(1) if m else ""
        elif f == "currency":
            m = re.search(r"\b(USD|EUR|GBP|THB|GEL|AMD)\b", text)
            v = m.group(1) if m else ""
        elif f.endswith("_date"):
            v = parse_date(line_after(text, LABELS[f]))
        elif f == "vat_amount":
            seg = line_after(text, LABELS[f])
            v = parse_amount(seg) if seg is not None else "0.00"
        elif f.endswith("_amount"):
            v = parse_amount(line_after(text, LABELS[f]))
        elif f in ("invoice_number", "receipt_number"):
            seg = line_after(text, LABELS[f])
            m = re.search(r"(\d{3,6})", seg or "")
            v = m.group(1) if m else ""
        if v:
            out[f] = v
    return out


def main() -> None:
    OUT.parent.mkdir(exist_ok=True)
    rows = []
    with open(ROOM / "documents_index.csv", encoding="utf-8") as f:
        for d in csv.DictReader(f):
            text = (ROOM / d["file"]).read_text(encoding="utf-8")
            for k, v in sorted(extract(d["doc_type"], text).items()):
                rows.append([d["doc_id"], k, v])
    with open(OUT, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["doc_id", "field", "value"])
        w.writerows(rows)
    print(f"wrote {OUT.relative_to(Path.cwd()) if OUT.is_relative_to(Path.cwd()) else OUT} ({len(rows)} values)")


if __name__ == "__main__":
    if "--negative" in sys.argv:
        from run_extraction import check_negative
        check_negative(extract)
    else:
        main()
