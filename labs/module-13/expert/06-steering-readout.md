# 06 · Readout for the management meeting, decision record and handover

Management meeting, Tuesday 23 March 2027, 10:00–11:00. Pre-read sent Thursday 18 March. Chair: Amnon Shaked. Present: Dalia Mizrahi, Orit Navon, Eli Peretz, Vladimir Kaplan, Rotem Levi, Michal Aharon, the operations-excellence manager; Khalil Mansour for item 4.

## Front page

**One sentence:** Kinneret loses deliveries because stops last too long — half of the lost hours are moulds, mostly at night — and because nobody records what failed; so we fix the night response for Arava now, build the records that any AI needs this year, give the night technicians a tested assistant in their language, and decide on predictive maintenance in January 2028 on our own data.

**Recommendation, in parts (owner, date):**

1. Arava plan: night mould response, shot counters on 60 hot-runner moulds, the six machines' PMs restored, QA cover for first-article approval at night (Fadi Khoury, Rotem Levi, Vladimir Kaplan; from 1 April). Target OTIF 92% in Q3, 95% in Q4.
2. Foundation: common asset register incl. moulds (30 April); recording at the machine in three languages (Plant K 30 April, Plant G 30 June); live parts view (31 March); sensors on the eight worst machines (30 September) (Vladimir Kaplan, Avi Malka, Boaz Tal).
3. Manual-assistant pilot: shadow on the night shift from 4 April, live after the joint committee's review (operations excellence; pack owners Vladimir Kaplan and Yaakov Dahan).
4. The protocol with the works committee signed before any change on the floor (Michal Aharon, Khalil Mansour; 31 March).
5. Release ₪730,000 of line 7400-210 in three stages with the stop rule (Orit Navon).

**Recommend-against, with evidence:** no contract with Predictiva in 2027, no letter of intent, no cameras. Usable failure labels: 73 of 861 breakdowns, none of the 30 per mode the vendor itself requires (measured). The platform covers machine faults, 24% of our lost hours; moulds, 46%, are outside it (measured). At the vendor's own best figure it returns about ₪257k a year against ₪343k a year of cost (directional).

**What a "no" to this means:** the Arava plan of 31 March contains no measure for night mould stops, and the January 2028 decision will meet the same records as this one.

## Integration check (three contradictions fixed before the pre-read)

- The case said recording live at Plant G "by 30 April"; the protocol says nothing changes before the joint committee meets, which Khalil set for 6 April at Plant G. Fixed to 30 June everywhere.
- A draft of item 3 showed "₪14,000 a year saved" from night calls. Removed: 64 hours of machine waiting are capacity at best, and not the reason for the assistant.
- The register entry for the assistant said logs "anonymous"; the tool's admin console stores the user's login. Changed to "stored without user id after export; 90 days" and a setting request to IT, before shadow use.

## Rehearsal of the hardest finding (Sunday 21 March, Amnon alone)

The hardest finding: **no Predictiva this year, and the "first plastics reference" conversation set a deadline that is not ours.** First attempt opened with the data-quality table; Amnon heard "your factory is a mess" and said he would ask Gilad to "just start at Galil". Second attempt opened with his own question from 12 January ("Arava back to 95%"), then the night mould hours and Tigist's short-shot story, then "Predictiva would watch the quarter that is machines; here is what would make it worth buying in January". He asked: "So what do I tell Gilad?" — the moment he owned it. Agreed: Amnon tells Gilad himself that Kinneret will run a proof of concept in January 2028 on its own data, on Kinneret's protocol.

## Decision record (23 March)

| # | Decision | Owner | Date |
|---|---|---|---|
| 1 | Arava plan items approved; sent to Arava 30 March | Dalia Mizrahi | 30 March |
| 2 | Foundation approved, stages 1–3, ₪730,000 from line 7400-210; stop rule: < 50% of breakdown WOs with a failure mode on 30 June | Orit Navon | Gates 30 April, 30 June, 31 December |
| 3 | Assistant: shadow from 4 April; live after joint committee review; stop on any safety-route failure | Operations excellence | 4 April; review 6 May |
| 4 | Protocol with the works committee: no individual performance reports, no discipline from the records, no cameras, Arabic and Russian recording, paid training | Michal Aharon | Signed by 31 March |
| 5 | Predictiva: declined for 2027; proof-of-concept protocol written by October; re-decision January 2028 | Amnon Shaked | January 2028 |
| 6 | KPI deck: one MTTR definition (stop to restart) for both plants from April | Operations excellence | April deck |

**Dissent, in the dissenter's words:** Eli Peretz: "Galil could have started in April and been the first. We will be ready in January." Recorded; Plant G is the first site for the 2028 proof of concept if its records meet the bar.

## Handover (by 30 June)

- **Business owner:** Dalia Mizrahi. **Technical owners:** Vladimir Kaplan (register, recording, pack), Boaz Tal (historian, tablets, assistant tool), Yaakov Dahan (safety documents in the pack and their translations).
- **Successor for the maintenance knowledge:** a senior technician named by Vladimir to co-own the pack and the failure-mode list from June (his 2028 retirement is the reason).
- **The kit:** `readiness_audit.py` and `discovery.py` re-run monthly by Lina Haddad; the test set, gates and scorer re-run after every pack change; the protocol and its six-month review; the 2028 decision criteria (04, section 1).
- **I stop owning** the assistant on 30 June and the foundation on 31 December.
