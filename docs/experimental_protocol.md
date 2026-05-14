# Experimental Protocol
## Quasi-Periodic Toroidal Resonance Structures

**Version:** 1.0  
**Status:** Active  
**Last updated:** May 2026

---

## Purpose

This document defines standard measurement procedures for comparing
quasi-periodic toroidal winding geometries against conventional periodic
baselines. All measurements must be performed consistently across all
prototypes to enable valid comparison.

Deviations from this protocol must be noted in the measurement log.

---

## Equipment

### Minimum Configuration

| Instrument | Purpose | Example Models |
|---|---|---|
| Vector network analyzer (VNA) | Impedance sweep, S-parameters | NanoVNA-H4, LiteVNA 64 |
| LCR meter | Low-frequency L/C/R | DE-5000, VICTOR 4090C |
| Multimeter | DC resistance, continuity | Any ≥ 4.5 digit |
| Calibration kit | SOLT calibration | Matched to VNA connector type |
| Non-ferromagnetic mount | Fixture for toroid under test | Nylon bolt + 3D-printed stand |

### Extended Configuration (later phases)

| Instrument | Purpose |
|---|---|
| Oscilloscope ≥ 100 MHz | Time-domain waveform capture |
| Function generator | Controlled drive signal |
| Current probe | Non-invasive current measurement |
| IR sensor or thermal camera | Thermal loss comparison |
| Small pickup coil | Near-field spatial mapping |

---

## Calibration Procedure

Perform before every measurement session without exception.

1. Allow VNA to warm up for ≥ 10 minutes
2. Perform full SOLT calibration **at the measurement plane**
   — at the point where the device under test (DUT) connects,
   not at the far end of the cable
3. Verify calibration with known reference:
   - Open: |S11| ≈ 0 dB, phase ≈ 180°
   - Short: |S11| ≈ 0 dB, phase ≈ 0°
   - Load (50Ω): |S11| ≈ −40 dB or lower
4. Record calibration state in measurement log
5. **Do not move cables** between calibration and measurement

---

## Prototype Preparation

Before any electrical measurement:

1. Verify DC resistance of each winding with multimeter
   - Record value — establishes wire integrity
   - Compare against calculated value for wire gauge and length
2. Verify no inter-winding shorts (resistance between winding pairs should be open)
3. Verify no winding-to-former shorts (if using ferrite core)
4. Photograph prototype from four standardized angles:
   - Top view
   - Side view (0°)
   - Side view (90°)
   - Isometric
5. Record ambient temperature and humidity in measurement log

---

## Measurement Set A — Impedance Sweep (Primary)

This is the core dataset. Perform on every prototype.

### Setup

- Connect one winding terminal to VNA port 1 (S11 reflection)
- Leave all other windings open-circuit (floating, not grounded)
- Frequency range: 100 kHz to 30 MHz
  (adjust if self-resonant frequency falls outside this range)
- Sweep points: minimum 401, recommend 1001
- Averaging: 4× minimum
- IF bandwidth: 100 Hz or lower for clean trace

### Measurements to Record

| Parameter | Unit | Notes |
|---|---|---|
| \|Z\| vs. frequency | Ω | Impedance magnitude |
| Phase vs. frequency | degrees | |
| Rs vs. frequency | Ω | Series resistance component |
| Xs vs. frequency | Ω | Series reactance component |
| S11 magnitude | dB | Reflection coefficient |
| S11 phase | degrees | |

### Derived Parameters

Calculate and record:

- **Self-resonant frequency (SRF)** — frequency of first impedance peak
- **Second and third resonances** — if present within sweep range
- **Q factor at SRF**: Q = f_SRF / BW_−3dB
  where BW_−3dB is the −3 dB bandwidth around the resonance peak
- **Low-frequency inductance** — measured at 100 kHz (below SRF)
- **Distributed capacitance** — estimated from SRF and L:
  C_dist = 1 / ((2π · f_SRF)² · L)

### Perform For Each Winding Separately

Repeat Measurement Set A for:
- [ ] Primary winding alone (others floating)
- [ ] Counter winding alone (others floating)
- [ ] Harmonic winding alone (others floating)

---

## Measurement Set B — Coupling Coefficient

Measures inductive coupling between winding pairs.

### Setup

- Connect primary to VNA port 1
- Connect secondary (counter or harmonic) to VNA port 2
- All unused windings floating
- Two-port S-parameter measurement (S11, S21, S12, S22)
- Frequency range: 100 kHz to 10 MHz

### Derived Parameters

- **Mutual inductance M** — from S21 at low frequency
- **Coupling coefficient k** = M / √(L1 · L2)
- **Coupling frequency response** — |S21| vs. frequency

### Perform For Each Pair

- [ ] Primary → Counter
- [ ] Primary → Harmonic
- [ ] Counter → Harmonic

---

## Measurement Set C — Harmonic Spectrum Under Drive

Measures harmonic content when the device is actively driven.

### Setup

- Drive primary winding with function generator
- Drive frequency: start at 1 kHz, sweep to 100 kHz
- Drive amplitude: 1 Vpp (low level — avoid core saturation)
- Monitor output across secondary winding with oscilloscope
- Record FFT spectrum from oscilloscope

### Measurements to Record

- Fundamental amplitude at output
- 2nd, 3rd, 5th, 7th harmonic amplitudes
- Total harmonic distortion (THD) if measurable
- Resonance response under drive vs. impedance sweep results

---

## Measurement Set D — Thermal Behavior

Compares thermal loss between control and quasi-periodic prototypes.

### Setup

- Drive at identical power levels
- Allow 10 minutes for thermal stabilization
- Measure surface temperature with IR thermometer or thermal camera
- Record at 4 standardized measurement points around toroid

### Note

Thermal differences, if present, indicate loss mechanism differences —
not efficiency gains. Any thermal data is loss characterization only.

---

## Comparative Protocol

The experiment has no value without a valid control.

### Control Structure (Prototype V0)

- Conventional periodic winding
- Identical toroid dimensions: R = 89 mm, r = 55 mm
- Identical wire gauge and total wire length
- Identical turn count
- Evenly spaced turns (360° / N spacing)

### Comparison Rules

1. Both prototypes measured on the same instrument
2. Both measurements taken within the same session where possible
3. Same calibration used for both
4. Same ambient conditions (temperature, humidity)
5. Both measurements repeated minimum 3 times; report mean ± std dev

### What Constitutes a Meaningful Difference

A difference is considered potentially significant if:

- It exceeds 3× the measurement uncertainty
- It is reproducible across ≥ 3 independent measurement runs
- It is present on both impedance sweep AND another measurement set

A single anomalous reading is not a result. Reproducibility is everything.

---

## Data Storage

All measurement data stored in `/data/` following naming convention:

```
data/
  prototype_v0/
    YYYY-MM-DD_run01_impedance_primary.csv
    YYYY-MM-DD_run01_coupling_p-c.csv
    YYYY-MM-DD_run01_notes.md
  prototype_v1/
    YYYY-MM-DD_run01_impedance_primary.csv
    ...
```

Raw VNA data exported as CSV or S2P (Touchstone format).
Never modify raw data files — create processed copies for analysis.

---

## Instrumentation Notes

### NanoVNA / LiteVNA Specific

- Use NanoVNA-saver software for PC-based sweep capture
- Export as S1P (one-port) or S2P (two-port) Touchstone format
- Perform calibration with the included SOLT cal kit
- Minimum 201 points; 1001 points recommended for SRF characterization

### LCR Meter Specific

- Measure inductance at 1 kHz, 10 kHz, and 100 kHz
- Record all three — frequency dependence reveals distributed effects
- Use 4-wire (Kelvin) connection if available to exclude lead resistance

---

## Safety Notes

- All measurements are low-voltage, low-power — no significant hazard
- Avoid driving windings at high power near SRF without current limiting
- Ferrite cores can chip — handle carefully, wear eye protection when cutting

---

*"We don't know what we'll find. That's the point."*

*See also: [hypothesis.md](hypothesis.md) · [measurement_log_template.md](measurement_log_template.md) · [geometry.md](geometry.md)*
