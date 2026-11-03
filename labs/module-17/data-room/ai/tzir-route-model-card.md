# Tzir Route — model card (vendor document, version 3.4, October 2026)

**What it does.** Builds daily delivery routes for a depot: sequence of stops, assignment to trucks, expected arrival windows. Plans go to the planner console and, when the dispatcher releases them, to the driver app.

**Model.** Gradient-boosted travel-time model per road segment and hour, plus a vehicle-routing solver.

**Training data.** GPS traces of 1,140 commercial fleets in Israel, **January 2021 to June 2023**; public road network (OpenStreetMap snapshot, July 2023); historical delivery windows.

**Customer adaptation.** "Customer-specific fine-tuning runs quarterly from the customer's telematics feed once the feed has been validated."

**Driver score.** Optional feature: a 0–100 score per driver from harsh braking, idling, deviation from plan and phone handling events. "Intended for coaching. Not designed for disciplinary decisions."

**Known limitations.** Road closures not present in the network snapshot must be entered by the customer in the console; travel-time estimates assume traffic patterns similar to the training period.

**Baseline for savings.** The value dashboard compares the optimised plan with a naive shortest-path sequence of the same stops (see dashboard documentation).
