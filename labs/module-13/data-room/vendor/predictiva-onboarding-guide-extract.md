# Predictiva onboarding guide — data prerequisites (extract)

*Section 3 of the onboarding guide, version 4.2. Sent by Gilad Har-Even to Eli Peretz with the questionnaire.*

3.1 **Asset hierarchy.** A single register with a unique id for every asset to be monitored, matching the ids
used in maintenance records and in sensor/historian tags.

3.2 **Maintenance history.** At least 12 months of work orders per asset with the failure mode coded
(ISO 14224 or equivalent taxonomy), the start and end of downtime, and the action taken. For a failure mode
to be modelled, we need at least 30 recorded failure events of that mode across the fleet.

3.3 **Sensor data.** Time-synchronised (NTP) data in a single time reference, at 1-minute resolution or
better, with at least 3 months of history before the learning period.

3.4 **Learning period.** During the 90-day learning period the customer's reliability engineer reviews
and labels each anomaly the platform raises (true failure precursor / false alarm / unknown).

3.5 Where 3.1–3.3 are not met, Predictiva can offer a **data readiness service** (priced separately).
