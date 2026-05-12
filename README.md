# Phi-Harmonic Toroidal Field Device

**Research by R. Wierzbicki · USA · 2026**

---

## Overview

This repository documents the theory, design, fabrication, and experimental research of a **phi-harmonic toroidal field device** — a precision-wound toroidal coil former constructed entirely from Fibonacci-true dimensions and phi-proportioned geometry.

The central hypothesis is that a toroidal inductor wound with three phi-harmonic coils at golden angle (137.5°) offsets, in a phi-proportioned torus (R/r = φ), produces electromagnetic field patterns that are not fully described by standard toroidal inductor theory — specifically, standing wave interference nodes at Fibonacci positions around the equator, consistent with phi-harmonic resonance theory.

---

## Device Specifications

| Parameter | Value | Significance |
|---|---|---|
| Major Radius R | 89 mm | 11th Fibonacci number |
| Minor Radius r | 55 mm | 10th Fibonacci number |
| R / r | 1.6182 | φ to 4 decimal places |
| Outer Diameter | 288 mm | 11.3 inches |
| Inner Diameter | 68 mm | 2.7 inches — wire clearance |
| Fibonacci Nodes | 8 | Golden angle spacing |
| Winding Turns | 5 | 5th Fibonacci number |
| Winding Count | 3 | Primary · Counter · Harmonic |
| Base Frequency | 111 Hz | Node 1 resonant frequency |
| Segment Count | 8 | Printed arc segments |

---

## The Three Windings

| Winding | Colour | Gauge | Direction | Offset |
|---|---|---|---|---|
| Primary | Red enamel | 18 AWG | Clockwise | 0° |
| Counter | Blue enamel | 18 AWG | Counter-CW | 120° |
| Harmonic | Green enamel | 20 AWG | φ × CW | 137.5° |

All three windings use enamelled copper magnet wire. Each winding closes back to its own node — creating three closed toroidal inductors within the same phi-geometry.

---

## Fibonacci Structure

Every dimension of this device is a Fibonacci number or direct phi-relationship:

```
1  1  2  3  5  8  13  21  34  55  89  144  233  377...
                           ↑r  ↑R
```

- R/r = 1.6182 (φ = 1.6180) — accurate to 3 decimal places
- Outer diameter = 288mm = 2 × 144 (12th Fibonacci)
- 8 segments, 5 turns, 3 windings, 8 nodes — all Fibonacci numbers

---

## The Seven Hermetic Principles — Connection to the Field

| Principle | Connection |
|---|---|
| Mentalism | The phi-spiral exists as geometric intelligence prior to matter |
| Correspondence | R/r = φ from subatomic to galactic scale |
| Vibration | Each node resonates at 111 × φ^(n/3) Hz |
| Polarity | Gold/teal amplitude poles — energy concentrates at the node between them |
| Rhythm | Toroidal circuit — perpetual self-circulating energy loop |
| Cause & Effect | The geometry IS the cause; the field IS the effect |
| Gender | Primary (projecting) and counter (receiving) are the same spiral from opposite poles |

---

## Node Frequency Map

| Node | Angle | Frequency | Cymatic Form |
|---|---|---|---|
| 1 | 0.0° | 111.00 Hz | 3-fold |
| 2 | 137.5° | 130.31 Hz | 5-fold |
| 3 | 275.0° | 152.98 Hz | 6-fold |
| 4 | 52.5° | 179.60 Hz | 5+ring |
| 5 | 190.0° | 210.85 Hz | 8-fold |
| 6 | 327.5° | 247.53 Hz | 8+ring |
| 7 | 105.0° | 290.60 Hz | 13-fold |
| 8 | 242.6° | 341.16 Hz | Complex |

---

## Theoretical Foundation

The phi-harmonic standing wave equation for the toroidal field:

```
P(t) = ( (R + r·cos(φ·t))·cos(t),  (R + r·cos(φ·t))·sin(t),  r·sin(φ·t) )
```

Standing wave membrane equation (cymatics):

```
u(r, θ, t) = sin(m·π·r/R) · cos(n·θ) · cos(ω·t)
```

Node frequency series:

```
f(n) = 111 × φ^(n/3)  Hz
```

---

## Repository Contents

```
/docs          — Technical specification PDF
/model         — FreeCAD source files and Python macros
/stl           — 3D print files (8 segments + alignment pin)
/website       — Interactive phi-harmonic field visualization (React/Three.js)
/measurements  — Experimental data (in progress)
```

---

## Theoretical Influences

- **Nikola Tesla** — 3·6·9 field symmetry and the axis of stillness
- **Viktor Schauberger** — Implosion vortex and the zone of creative stillness
- **Walter Russell** — Wave cosmogony and Still Magnetic Light
- **The Kybalion** — Seven Hermetic Principles as field laws
- **Hal Puthoff** — Zero point field theory (peer-reviewed)
- **Fibonacci / Leonardo of Pisa** — The sequence that describes living growth

---

## Research Goals

1. Measure resonant frequency response — does the device exhibit unusual Q-factors at phi-harmonic frequencies?
2. Map field distribution — does the Fibonacci node pattern produce measurable field concentration?
3. Measure impedance characteristics — do the three windings interact in unexpected ways?
4. Cymatic confirmation — do phi-harmonic drive frequencies produce geometric patterns consistent with standing wave theory?

---

## Build Log

| Date | Milestone |
|---|---|
| May 2026 | Theory complete — 13-chapter framework |
| May 2026 | 3D model initiated — FreeCAD / Fusion 360 |
| May 2026 | Repository established — public priority record |
| TBD | Print complete |
| TBD | Assembly complete |
| TBD | First measurements |

---

## License

This work is published openly for the advancement of knowledge.  
All original theory, design, and documentation © R. Wierzbicki, 2026.  
Attribution required for any derivative work.

---

*"The convergence of φ, the Fibonacci sequence, toroidal geometry, Tesla's 3·6·9,  
and zero point field theory is not accidental. They are different descriptions  
of the same underlying structure — the way energy organises itself  
when given the freedom to do so."*

— R. Wierzbicki, 2026
