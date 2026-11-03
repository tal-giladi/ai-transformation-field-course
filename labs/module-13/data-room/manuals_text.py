"""Equipment manual extracts (English, as the makers supply them). All makers are fictional.

Reading this spoils the engagement: finish module 13 first.
"""

MANUALS = {
"MAN-KX": ("Kessler KX / KX-e injection moulding machines — operation and maintenance manual (extract)", "en", "Ed. 2019; KX-e supplement 2024", """
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
"""),

"MAN-HW": ("Haiwei HW and HW-3 series — user manual (English edition, extract)", "en", "HW 2006; HW-3 2016", """
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
"""),

"MAN-MP": ("Morandi MP series — maintenance manual (English translation from Italian, extract)", "en", "Ed. 2008", """
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
"""),

"MAN-HRC": ("ThermoFlow HRC-24 hot runner controller — operating manual (extract)", "en", "Rev. 3, 2020", """
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
"""),

"MAN-DRY": ("DryMax DM-150 desiccant dryer — manual (extract)", "en", "2014", """
## Dew point

Target dew point: −40 °C. Alarm DP-HI: dew point above −20 °C. Check the process air filter and the
regeneration heater (3.5 kW).

## Maintenance

Clean the process air filter weekly. Replace the desiccant every 3 years.

## Drying times (guide)

PA6: 4 hours at 80 °C. PC: 4 hours at 120 °C. PBT: 4 hours at 120 °C. PP and PE normally need no drying.
"""),

"MAN-CHL": ("ArcticFlow AC-40 chiller — manual (extract)", "en", "2016", """
## Alarms

HP1 high refrigerant pressure: clean the condenser and check the fan. FL1 low water flow: check the pump,
the strainer and that the valves to the machines are open. LT1 low water temperature: setpoint too low.

## Setpoint

Standard water setpoint for moulds: 12 °C. Do not set below 8 °C without glycol.
"""),
}
