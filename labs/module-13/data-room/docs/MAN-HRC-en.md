# MAN-HRC · ThermoFlow HRC-24 hot runner controller — operating manual (extract)

- Document: MAN-HRC
- Language: English
- Revision: Rev. 3, 2020 (maker)
- Owner: Maker (as supplied)

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
