# Phi-Scaled Resonant Toroidal Research Platform
### *The Wierzbicki Phenomenon Omnivortex Device*
**Experimental Research · Ryan R. Wierzbicki · USA · 2026**

---

## Overview

This repository documents the design, fabrication, and experimental evaluation of a phi-proportioned toroidal field platform employing non-periodic winding geometry, Fibonacci-derived dimensional relationships, and multi-coil harmonic coupling at golden-angle offsets.

The platform investigates whether recursively phi-scaled toroidal structures and quasi-periodic winding distributions exhibit measurable differences in electromagnetic field organisation, resonance behaviour, harmonic distribution, and field coherence — compared to conventional toroidal architectures.

This project extends one specific, narrow, published result: Purnell et al.
(2018, *Physiological Reports*) reported that a phi-proportioned toroidal
electromagnetic array shifted human red blood cell morphology toward
golden-ratio proportions in a small (n=20), single-device, non-replicated
pilot study. That study used DC excitation through a conductive saline bath
and had no non-phi control geometry, so it cannot distinguish whether phi
geometry specifically — versus toroidal topology generally, the DC field, or
the saline coupling — is the active variable. This platform's three-version
comparative design (V1/V2/V3) exists to isolate that variable using an AC,
air-core implementation. See `docs/literature_review.md` for the full
evidentiary basis and explicit scope limits.

Cymatics (Jenny, 1967–74) motivates the node-frequency predictions tested in
Phase 2 — this is a citable, real body of acoustic-physics work, not a
biological claim. No claims of overunity performance, violation of
established physical law, or therapeutic/disease-treatment efficacy are
made. The purpose of this platform is experimental investigation of
measurable electromagnetic phenomena — inductance, Q, resonant frequency,
field distribution — produced by phi-harmonic geometry.

---

## Research Objectives

The platform is designed to investigate the following specific questions:

1. Do phi-proportioned toroidal geometries (R/r = φ) produce measurably different field distributions compared to non-phi toroidal geometries with identical winding configurations?

2. Do quasi-periodic winding offsets at the golden angle (137.5°) produce measurably different standing-wave node distributions compared to evenly periodic winding arrangements?

3. Do three mutually coupled windings in phi-harmonic phase relationships produce emergent field phenomena not predicted by analysis of each winding in isolation?

4. Does the combination of opposing primary and counter windings produce any measurable difference in Faraday-cage transmission compared to a single-winding control? (Framed as an electrical engineering question; see `docs/literature_review.md` §III for why this is not framed in terms of scalar-wave theory.)

5. Are Fibonacci node positions — predicted by the phi-spiral winding geometry — measurably associated with field concentration or standing-wave formation?

6. Do phi-harmonic driving frequencies (f(n) = 111 × φ^(n/3) Hz) produce resonant behaviour distinct from non-harmonic driving frequencies in this geometry?

---

## Theoretical Foundation

### The Motivating Result

Purnell et al. (2018, *Physiological Reports*) reported that a
phi-proportioned toroidal electromagnetic array shifted human red blood
cell morphology toward golden-ratio proportions in a small (n=20),
single-device, non-replicated pilot study using DC excitation through a
saline bath. The study had no non-phi control geometry, so it cannot
isolate whether phi geometry, toroidal topology generally, the DC field,
or the saline coupling produced the effect. This platform's V1/V2/V3
comparative design exists to isolate that variable with an AC, air-core
implementation. Full evidentiary basis and scope limits: `docs/literature_review.md`.

### Faraday-Cage Transmission Test

The V3 winding architecture (opposing primary/counter windings, 120° phase
offset) will be compared against V1/V2 single-winding controls for any
measurable difference in transmission through a grounded Faraday enclosure.
This is framed as an electrical engineering measurement, not as a test of
scalar-wave theory — see `docs/literature_review.md` §III for why that
framework is explicitly not part of this project's evidentiary basis. Any
unexpected result will be investigated via conventional EM coupling
mechanisms first.

### Cymatic Field Organisation

Jenny (1967–1974) demonstrated that specific driving frequencies produce reproducible geometric standing-wave patterns in physical media. The phi-harmonic node frequency series (111 × φ^(n/3) Hz) is predicted to produce distinct cymatic patterns corresponding to Fibonacci symmetry orders (3-fold, 5-fold, 8-fold, 13-fold) at successive node positions around the torus equator. This prediction is directly testable.

### Phi Geometry as Organisational Principle

The golden ratio φ = (1+√5)/2 = 1.6180... appears as a growth ratio throughout biological systems — phyllotaxis, vascular branching, neural architecture — because it maximises spatial coverage without self-overlap. The hypothesis under investigation is that a toroidal field structure proportioned to φ is geometrically congruent with biological field structures in a way that conventional integer-ratio geometries are not.

---

## Experimental Design

### Three-Version Comparative Framework

| Version | Label | Geometry | Winding | Variable Under Test |
|---|---|---|---|---|
| V1 | Control | Standard (R=80mm, r=45mm) | Poloidal standard | Baseline |
| V2 | Phi-Shell | Phi-proportioned (R=89mm, r=55mm) | Poloidal standard | Phi geometry alone |
| V3 | Omnivortex | Phi-proportioned (R=89mm, r=55mm) | Three phi-spiral windings | Phi geometry + phi winding |

This design enables isolation of the geometric effect (V1 vs V2), the winding effect (V2 vs V3), and the combined effect (V1 vs V3).

### Device Specifications

| Parameter | V1 Control | V2 Phi-Shell | V3 Omnivortex |
|---|---|---|---|
| Major Radius R | 80 mm | 89 mm (F11) | 89 mm (F11) |
| Minor Radius r | 45 mm | 55 mm (F10) | 55 mm (F10) |
| R / r | 1.778 | 1.618 (φ) | 1.618 (φ) |
| Outer Diameter | 250 mm | 288 mm | 288 mm |
| Winding type | Poloidal | Poloidal | Phi-spiral |
| Winding count | 1 | 1 | 3 |
| Turn count | 50 | 50 | 5 per winding |

---

## V3 Omnivortex Winding Architecture

| Winding | Colour | Gauge | Direction | Phase Offset |
|---|---|---|---|---|
| Primary | Red enamel | 18 AWG | Clockwise | 0° |
| Counter | Blue enamel | 18 AWG | Counter-clockwise | 120° |
| Harmonic | Green enamel | 20 AWG | Phi-rate advance | 137.5° (golden angle) |

Each winding closes at its own node contact — creating three closed toroidal inductors within the same phi-proportioned geometry. The harmonic winding advances at the golden angle per major turn (minor turns = major turns × φ = 8.09).

---

## Fibonacci Node Geometry

| Node | Angle | Predicted Frequency | Predicted Cymatic Form |
|---|---|---|---|
| 1 | 0.0° | 111.00 Hz | 3-fold symmetry |
| 2 | 137.5° | 130.31 Hz | 5-fold symmetry |
| 3 | 275.0° | 152.98 Hz | 6-fold symmetry |
| 4 | 52.5° | 179.60 Hz | 5-fold + ring |
| 5 | 190.0° | 210.85 Hz | 8-fold symmetry |
| 6 | 327.5° | 247.53 Hz | 8-fold + ring |
| 7 | 105.0° | 290.60 Hz | 13-fold symmetry |
| 8 | 242.6° | 341.16 Hz | Complex composite |

Node frequency series: **f(n) = 111 × φ^(n/3) Hz**

---

## Mathematical Framework

**Toroidal parametric surface:**

    P(t) = ( (R + r·cos(φ·t))·cos(t),  (R + r·cos(φ·t))·sin(t),  r·sin(φ·t) )

**Node frequency series:**

    f(n) = 111 × φ^(n/3)  Hz,   n = 0, 1, 2, ... 7

**Golden angle:**

    GA = 360 / φ² = 137.5077...°

**Standing-wave membrane model:**

    u(r, θ, t) = sin(m·π·r/R) · cos(n·θ) · cos(ω·t)

**Fibonacci dimensional relationships:**

    R = 89 mm = F(11),   r = 55 mm = F(10),   R/r = 1.6182 ≈ φ

---

## Measurement Protocol

### Phase 1 — Electromagnetic Characterisation
Instruments: LCR meter, oscilloscope, function generator, NanoVNA

- Inductance and Q factor comparison across V1, V2, V3
- Resonance frequency mapping and harmonic spectrum analysis
- Impedance sweep 1 Hz – 10 MHz
- Phase relationships between V3 windings

### Phase 2 — Field Distribution Mapping
Instruments: Gaussmeter, Arduino sweep driver

- Near-field magnetic flux mapping at predicted node positions
- Standing-wave node detection using particle medium
- Cymatic pattern documentation at each node frequency

### Phase 3 — Faraday-Cage Transmission Test
Instruments: Paired coil sets, oscilloscope, Faraday cage

- Faraday cage transmission test: V1 vs V2 vs V3
- Phase velocity measurement
- Any anomalous result investigated via conventional EM coupling mechanisms
  before any other interpretation

### Phase 4 — Biological Response Investigation

*Phase 4 investigations will be conducted within applicable regulatory
frameworks (IRB-equivalent oversight required for any biological subject)
and will not involve therapeutic claims. This phase is a long-horizon,
not-yet-scoped extension and is not a current commitment.*

- Replication attempt of Purnell (2018) RBC morphology measurement,
  parametrized across V1/V2/V3 to test whether phi geometry specifically
  is the active variable

---

## Driver Circuit

| Parameter | Value |
|---|---|
| Driver | 2 × L298N H-bridge + Arduino Nano |
| Supply voltage | 12V DC regulated |
| Series resistance | 1.5Ω 10W per winding |
| Peak current | ~7A per winding |
| Frequency range | 1 Hz – 100 kHz |
| Drive modes | In-phase / Anti-phase / Phase-offset / Sequential |

---

## Fabrication

All structural components are 3D-printed in PETG from parametrically generated STL files produced by `TorusGenerator.java` — a pure-Java parametric STL generator operating directly from mathematical definitions.

| Parameter | Value |
|---|---|
| Material | PETG |
| Segments | 8 per torus (45° arc each) |
| Layer height | 0.20 mm |
| Infill | Honeycomb 30% |
| Wall perimeters | 4 |
| Supports | None required |

---

## Historical Precedents

| Researcher | Year | Contribution |
|---|---|---|
| Nikola Tesla | 1898 | High-frequency electromagnetic therapeutic effects |
| Georges Lakhovsky | 1925 | Cellular LC oscillation theory; MWO clinical trials |
| Hans Jenny | 1967–74 | Cymatic standing-wave geometry at discrete frequencies |
| Herbert Fröhlich | 1968 | Quantum coherence in biological systems |
| Konstantin Meyl | 2001 | Scalar longitudinal wave theory and experimental replication |
| Thomas Valone | 2003 | Bioelectromagnetic healing: historical record and biophysical rationale |

---

## Current Status

| Date | Milestone |
|---|---|
| May 2026 | Theoretical framework complete |
| May 2026 | Parametric geometry and Java STL generator complete |
| May 2026 | Driver circuit specification complete |
| May 2026 | Repository established — public priority record |
| May 2026 | Documentation complete. Awaiting first print. |
| May 23, 2026 | First segment printed — V1 control |
| May 23, 2026 | OpenSCAD geometry validated — slits, pegs, sockets |
| May 23, 2026 | Bambu Lab A1 Mini operational |
| May 24, 2026 | Toroidal segment peg/socket alignment validated procedurally |
| May 24, 2026 | 45° segmented toroid architecture finalized for V1 testing 
| TBD | Phase 1 electromagnetic characterisation |
| TBD | Phase 2 field distribution mapping |
| TBD | Phase 3 scalar component investigation |
| TBD | Phase 4 biological response investigation |

---

## Research Position

This project investigates unconventional resonant geometries and winding architectures within experimental electromagnetic research. All measurements will employ appropriate instruments, documented procedures, and comparative baselines.

**This project does not claim:**
- Perpetual motion or overunity performance
- Violation of conservation of energy or Maxwell's equations
- Confirmed anomalous physics prior to experimental verification
- Therapeutic efficacy in the absence of controlled experimental data

**This project does claim:**
- Original parametric design of a phi-proportioned three-winding toroidal field platform
- Rigorous three-version experimental design for variable isolation
- Public priority record established May 2026
- Open research for collaborative independent verification

---

## License

Open research publication for collaborative experimentation and independent verification.  
All original theory, design, and documentation © R. Wierzbicki, 2026.  
Attribution required for derivative work and published results.

---

*"The convergence of φ, the Fibonacci sequence, toroidal geometry, Tesla's 3·6·9,  
and a century of bioelectromagnetic research is not accidental.  
They are different descriptions of the same underlying structure —  
the way energy organises itself when given the freedom to do so."*

— R. Wierzbicki, 2026
