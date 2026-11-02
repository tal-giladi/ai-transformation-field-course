# PoC sample visits and notes

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
