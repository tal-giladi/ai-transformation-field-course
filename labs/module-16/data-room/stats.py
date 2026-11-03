"""Compute the facts the documents quote and the writer's notes record (python generate.py --facts)."""
from __future__ import annotations

from collections import Counter

from people import COORDINATORS


def compute(staff, vols, fams, notes, tlog, survey, donors, card, audit, funders) -> dict:
    f = {}
    f["n_staff"] = len(staff)
    f["fte"] = round(sum(s[4] for s in staff), 1)
    f["n_vols"] = len(vols)
    f["n_vols_active"] = sum(v["active"] for v in vols)
    f["n_families"] = len(fams)
    f["n_donors"] = len(donors)
    # consent
    c = Counter(x["consent"] for x in fams)
    f["consent_v1"], f["consent_v2"], f["consent_missing"] = c["v1-2019"], c["v2-2023"], c["missing"]
    f["consent_v1_pct"] = round(100 * c["v1-2019"] / len(fams), 1)
    f["v2_stories_yes"] = sum(1 for x in fams if x["stories"] == "y")
    f["ah_families"] = sum(1 for x in fams if x["ah"] == "y")
    f["ah_v1"] = sum(1 for x in fams if x["ah"] == "y" and x["consent"] != "v2-2023")
    f["kh_referred"] = sum(1 for x in fams if x["referred"] == "Kiryat Hadas welfare")
    f["lang"] = dict(Counter(x["lang"] for x in fams))
    # Drive audit
    fam_rows = [r for r in audit if r[0] == "Shared drives/Families"]
    f["families_principals"] = len(fam_rows)
    f["families_personal"] = sum(1 for r in fam_rows if r[4] == "external personal")
    f["families_former_staff"] = sum(1 for r in fam_rows if "former" in r[4])
    vol_by_mail = {f"{v['id'].lower()}.vol@{v['domain']}": v for v in vols}
    f["families_inactive_vols"] = sum(1 for r in fam_rows if r[3] in vol_by_mail and not vol_by_mail[r[3]]["active"])
    resp = [r for r in audit if r[0].endswith("Respite (weekend care sheets)") and r[4] == "external personal"]
    f["respite_vols"] = len(resp)
    f["respite_inactive"] = sum(1 for r in resp if not vol_by_mail[r[3]]["active"])
    with_acc = {r[3] for r in fam_rows + resp if r[3] in vol_by_mail}
    f["vols_with_access"] = len(with_acc)
    f["vols_access_no_conf"] = sum(1 for m in with_acc if not vol_by_mail[m]["conf"])
    don_rows = [r for r in audit if "Donors 2026" in r[0] and r[3] != f"anyone at {r[2].split('@')[1]} with the link"]
    f["donor_editors"] = len(don_rows)
    f["donor_personal"] = sum(1 for r in don_rows if r[4] == "external personal")
    # donors
    f["donor_id_on_file"] = sum(1 for d in donors if d[5] == "y")
    f["donor_sensitive_notes"] = sum(1 for d in donors if d[17] and any(
        k in d[17] for k in ("programme", "autism", "families", "CP", "diagnosis", "welfare", "husband", "הפוגה",
                             "البرنامج")))
    f["donor_notes_any"] = sum(1 for d in donors if d[17])
    f["donors_2026"] = sum(1 for d in donors if d[11])
    f["donations_2026"] = sum(d[12] for d in donors)
    f["donations_2025"] = sum(d[10] for d in donors)
    # time log
    by = Counter()
    tot = Counter()
    for sid, _d, _t, m, act, _n in tlog:
        by[(sid, act)] += m
        tot[sid] += m
    f["ah_hours_week"] = round(sum(v for (s, a), v in by.items() if a == "funder_report_adler_haddad") / 60, 1)
    f["ah_hours_coords"] = round(sum(by[(s, "funder_report_adler_haddad")] for s in COORDINATORS) / 60, 1)
    f["ah_hours_per_coord"] = round(f["ah_hours_coords"] / len(COORDINATORS), 1)
    f["case_notes_hours_coords"] = round(sum(by[(s, "case_notes")] for s in COORDINATORS) / 60, 1)
    f["coord_hours_total"] = round(sum(tot[s] for s in COORDINATORS) / 60, 1)
    f["coord_ah_share"] = round(100 * f["ah_hours_coords"] / f["coord_hours_total"], 1)
    f["coord_direct_hours"] = round(sum(by[(s, a)] for s in COORDINATORS for a in ("family_contact", "home_visit"))
                                    / 60, 1)
    f["translation_hours"] = round(sum(by[(s, "translation_letters")] for s in COORDINATORS) / 60, 1)
    writing = ("grant_proposal", "other_funder_report", "funder_report_adler_haddad")
    f["noa_total"] = round(tot["S02"] / 60, 1)
    f["noa_writing"] = round(sum(by[("S02", a)] for a in writing) / 60, 1)
    f["noa_writing_pct"] = round(100 * f["noa_writing"] / f["noa_total"], 1)
    f["noa_reports_only_pct"] = round(100 * (by[("S02", "other_funder_report")] +
                                             by[("S02", "funder_report_adler_haddad")]) / tot["S02"], 1)
    f["samah_ah"] = round(by[("S08", "funder_report_adler_haddad")] / 60, 1)
    f["timelog_rows"] = len(tlog)
    # funders
    f["foundation_income"] = sum(x[2] for x in funders if x[1] not in ("government", "municipality"))
    f["ah_share_foundations"] = round(100 * funders[0][2] / f["foundation_income"], 1)
    f["report_hours_year"] = sum(x[9] * {"quarterly": 4, "semi-annual": 2, "annual": 1, "monthly + annual": 13,
                                         "per grant": 1}[x[4]] for x in funders)
    f["proposal_hours_year"] = sum(x[10] for x in funders)
    f["ah_report_hours_year_est"] = funders[0][9] * 4
    # survey
    f["survey_n"] = len(survey)
    f["survey_users"] = sum(1 for s in survey if s[3] != "never")
    f["survey_with_details"] = sum(1 for s in survey if s[7] == "yes, with details")
    f["survey_prefer_not"] = sum(1 for s in survey if s[7] == "prefer not to say")
    f["survey_personal"] = sum(1 for s in survey if s[5] in ("personal", "both"))
    # card
    def sumcat(pred):
        return round(sum(float(c[5]) for c in card if pred(c)), 2)
    f["openai_ils"] = sumcat(lambda c: "OPENAI" in c[1])
    f["openai_months"] = sum(1 for c in card if "OPENAI" in c[1])
    f["dropbox_ils"] = sumcat(lambda c: "DROPBOX" in c[1])
    f["msft_ils"] = sumcat(lambda c: "MSFT" in c[1])
    f["software_ils"] = sumcat(lambda c: c[7] == "Software")
    # notes sample
    f["notes_n"] = len(notes)
    f["notes_leaks"] = sum(1 for n in notes if any(k in n[7] for k in ("Yonatan", "000-", "050-", "Ha-Rimon",
                                                                       "gmail.com", "Hailemariam", "נועם", "كريم")))
    f["notes_lang"] = dict(Counter(n[4] for n in notes))
    return f
