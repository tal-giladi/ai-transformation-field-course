# MAN-KX · Kessler KX / KX-e injection moulding machines — operation and maintenance manual (extract)

- Document: MAN-KX
- Language: English
- Revision: Ed. 2019; KX-e supplement 2024 (maker)
- Owner: Maker (as supplied)

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
