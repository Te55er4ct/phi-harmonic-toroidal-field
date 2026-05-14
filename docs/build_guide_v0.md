# Build Guide — Prototype V0
## Control Toroid (Conventional Periodic Winding)

**Status:** First build  
**Purpose:** Establish baseline measurements for comparison against quasi-periodic prototypes  
**Difficulty:** Beginner  
**Estimated build time:** 3–4 hours

---

## Why Build the Control First

Every experimental result is only meaningful relative to a baseline.
Prototype V0 is that baseline.

It uses identical dimensions and materials to V1 and V2, with one difference:
conventional evenly-spaced winding. Building and measuring V0 first means
any differences observed in V1 and V2 are attributable to winding topology —
not to unknown variables in materials, dimensions, or technique.

**Do not skip the control build.**

---

## Bill of Materials

| Item | Quantity | Specification | Approx. Cost | Source |
|---|---|---|---|---|
| Toroid former V0 (printed) | 1 | PLA or PETG, R=89mm, r=55mm | ~$3–8 | Print from `cad/toroid_former_v0.stl` |
| Enameled copper wire | ~20m | 24 AWG (0.51mm) | ~$8 | Amazon, electronics suppliers |
| Nylon M8 bolt + nut | 1 set | Non-ferromagnetic | ~$1 | Hardware store |
| BNC or SMA connector | 1 | Panel mount or PCB type | ~$3 | Amazon, Mouser |
| Solder + flux | — | Electronics grade | — | On hand |
| Heat-shrink tubing | 4 pieces | 3mm diameter | ~$1 | On hand |
| Cyanoacrylate (super glue) | small amount | Thin viscosity | — | On hand |
| Small piece of cardboard | 1 | Wire management during winding | — | On hand |

**Total estimated material cost: ~$15–25**

---

## Tools Required

| Tool | Notes |
|---|---|
| 3D printer | For former — or send to print service |
| Soldering iron | 350°C tip, fine point preferred |
| Wire strippers | Set for 24 AWG |
| Multimeter | Continuity + resistance |
| Calipers | Verify printed dimensions |
| Helping hands / vise | Hold former while winding |
| Permanent marker | Mark turn positions |
| Ruler or tape measure | Measure wire length |
| Scissors | |

---

## Step 1 — Print and Verify the Former

1. Print `cad/toroid_former_v0.stl` with these settings:

   | Setting | Value |
   |---|---|
   | Material | PLA or PETG |
   | Layer height | 0.15 mm |
   | Infill | 20% (structural only — not a load-bearing part) |
   | Walls | 3 perimeters |
   | Supports | None required |
   | Orientation | Flat face down |

2. After printing, verify dimensions with calipers:

   | Dimension | Target | Tolerance |
   |---|---|---|
   | Major radius R | 89 mm | ± 0.5 mm |
   | Minor radius r | 55 mm | ± 0.5 mm |
   | Outer diameter | 288 mm | ± 1 mm |
   | Inner hole diameter | 68 mm | ± 1 mm |

3. Check the surface is smooth and free of print artifacts that could
   damage wire insulation during winding. Sand lightly if needed.

---

## Step 2 — Calculate and Prepare Wire

For a conventional winding with N = 144 turns on this toroid:

```
Circumference of tube cross-section = 2π × r = 2π × 55 = 345 mm per turn
Total wire length = 144 turns × 345 mm = ~49.7 m
Add 20% for routing and leads = ~60 m total

Cut a working length of 65 m to be safe.
```

Before cutting:
1. Measure and cut 65 m of 24 AWG enameled wire
2. Wind it loosely into a shuttle or bobbin to feed through the toroid hole
3. Leave a 20 cm tail at the start for the lead wire

---

## Step 3 — Mark Turn Positions

For a conventional (control) winding, turns are evenly spaced:

```
Angular spacing = 360° / 144 = 2.5° between turns
```

1. Using a permanent marker, make a small mark at position 0°
   on the outer equator of the toroid
2. This is your starting point — all other positions are reference only
3. You do not need to mark all 144 positions — just maintain
   consistent visual spacing as you wind

---

## Step 4 — Wind the Primary Winding

This is the meditative part. Take your time. Consistency matters more than speed.

1. Mount the toroid on the nylon bolt — this lets you rotate it freely
   while keeping it stable

2. Thread the wire end through the center hole and begin winding:
   - Pass the wire through the hole (poloidal direction)
   - Bring it over the outside of the tube
   - Back through the hole again
   - That is one turn

3. Maintain even spacing between turns — roughly 2.5° apart visually

4. Every 10 turns, place a tiny dot of super glue on the wire
   to hold position while you continue. Use sparingly.

5. Wind all 144 turns in the **clockwise** direction
   (when viewed from above)

6. Leave a 20 cm tail at the finish

**If you lose count:** use a piece of tape to mark every 10th turn as you go.

---

## Step 5 — Terminate and Solder

1. Strip 15mm of enamel from each wire end:
   - Use fine sandpaper (400 grit) or a lighter flame
   - Verify with multimeter — continuity between the two ends
   - If no continuity: enamel not fully removed — strip again

2. Tin both wire ends with solder

3. Solder to BNC or SMA connector:
   - One wire to center pin
   - Other wire to ground/shell
   - Keep leads as short as possible

4. Cover solder joints with heat-shrink

---

## Step 6 — Initial Electrical Verification

Before any RF measurement, verify basic electrical integrity:

| Test | Method | Expected Result |
|---|---|---|
| Continuity | Multimeter across connector | < 5 Ω (wire resistance) |
| No shorts to former | Multimeter, wire to former surface | Open circuit (> 1 MΩ) |
| DC resistance | Multimeter, 4-wire if available | Record value |

**Record DC resistance:** ___ Ω

Theoretical DC resistance for 60m of 24 AWG:
```
Resistance = length × resistivity = 60m × 84.2 mΩ/m ≈ 5.1 Ω
```
Measured value should be within ± 1 Ω of this. Higher means a bad
connection. Lower is not possible — recheck your calculation.

---

## Step 7 — Photograph

Take four standardized photographs and add to `photos/prototype_v0/`:

- [ ] `top_view.jpg`
- [ ] `side_0deg.jpg`
- [ ] `side_90deg.jpg`
- [ ] `isometric.jpg`

These photos become part of the permanent record.

---

## Step 8 — First Measurements

With the prototype complete and verified, proceed to measurements
following the procedures in `docs/experimental_protocol.md`.

Record all results in a copy of `docs/measurement_log_template.md`
saved as `data/prototype_v0/YYYY-MM-DD_run01_v0_control.md`.

**Key measurements to establish baseline:**

1. Impedance sweep: 100 kHz – 30 MHz
2. Record: self-resonant frequency, Q factor, inductance at 100 kHz
3. Repeat 3 times to establish repeatability

---

## Troubleshooting

| Problem | Likely Cause | Solution |
|---|---|---|
| No continuity | Enamel not stripped | Re-strip both ends with sandpaper |
| Very high resistance | Cold solder joint | Reflow with fresh solder |
| Erratic VNA trace | Loose connection | Check all connections, recalibrate |
| SRF not visible in sweep | SRF outside range | Extend sweep to 100 MHz |
| Turns not staying in place | Insufficient glue | Add more CA glue at 10-turn intervals |

---

## What to Expect

For a 144-turn toroidal inductor with R=89mm, r=55mm, 24 AWG wire:

```
Approximate inductance:    3–6 μH  (measure to confirm)
Approximate SRF:           5–15 MHz (depends on winding tightness)
Approximate Q at SRF:      50–200   (air core, 24 AWG)
```

These are rough estimates only. The actual measurements are what matter.

---

## Next Step

Once V0 is measured and documented:
→ Proceed to [prototype_v1/build_guide.md](../prototype_v1/build_guide.md)

The quasi-periodic winding build uses the same process with one
critical difference: golden-angle turn spacing instead of even spacing.

---

*"The control structure exists and will be measured identically."*
