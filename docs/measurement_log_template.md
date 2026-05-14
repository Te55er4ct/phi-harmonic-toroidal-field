# Measurement Log Template
## Quasi-Periodic Toroidal Resonance Structures

**Copy this file for each measurement session.**  
**Rename to:** `YYYY-MM-DD_run##_[prototype].md`  
**Example:** `2026-06-15_run01_v0_control.md`

---

## Session Metadata

| Field | Value |
|---|---|
| Date | YYYY-MM-DD |
| Run number | ## |
| Operator | |
| Prototype | V0 (control) / V1 / V2 |
| Location | |
| Ambient temperature | ___ °C |
| Ambient humidity | ___ % |

---

## Instrument Configuration

| Instrument | Model | Firmware/SW version | Serial / ID |
|---|---|---|---|
| VNA | | | |
| LCR meter | | | |
| Multimeter | | | |
| Oscilloscope | | | |
| Function generator | | | |

**VNA calibration:**
- [ ] SOLT calibration performed this session
- [ ] Calibration verified (open / short / load)
- Calibration plane: ___
- Cal kit used: ___

---

## Prototype Physical Inspection

- [ ] DC resistance verified (no open circuits)
- [ ] Inter-winding isolation verified (no shorts)
- [ ] Photographs taken (add to photos/ folder)
- [ ] Visual inspection — any damage or anomalies noted below

**Notes:**

---

## DC Resistance

| Winding | Measured Ω | Expected Ω | Pass/Fail |
|---|---|---|---|
| Primary | | | |
| Counter | | | |
| Harmonic | | | |
| Primary → Counter (isolation) | | > 1 MΩ | |
| Primary → Harmonic (isolation) | | > 1 MΩ | |
| Counter → Harmonic (isolation) | | > 1 MΩ | |

---

## Measurement Set A — Impedance Sweep

### A1 — Primary Winding

VNA sweep: 100 kHz to 30 MHz, ___ points, ___ × averaging

| Parameter | Value | Unit | Notes |
|---|---|---|---|
| Low-frequency inductance (100 kHz) | | μH | |
| Self-resonant frequency (1st) | | MHz | |
| Self-resonant frequency (2nd) | | MHz | if present |
| Self-resonant frequency (3rd) | | MHz | if present |
| Q factor at 1st SRF | | | |
| −3 dB bandwidth at 1st SRF | | kHz | |
| Estimated distributed capacitance | | pF | C = 1/(4π²f²L) |
| Peak impedance at SRF | | kΩ | |

Raw data file: `data/[prototype]/[date]_run##_impedance_primary.s1p`

**Observations:**

---

### A2 — Counter Winding

| Parameter | Value | Unit | Notes |
|---|---|---|---|
| Low-frequency inductance (100 kHz) | | μH | |
| Self-resonant frequency (1st) | | MHz | |
| Q factor at 1st SRF | | | |
| −3 dB bandwidth | | kHz | |
| Estimated distributed capacitance | | pF | |

Raw data file: `data/[prototype]/[date]_run##_impedance_counter.s1p`

**Observations:**

---

### A3 — Harmonic Winding

| Parameter | Value | Unit | Notes |
|---|---|---|---|
| Low-frequency inductance (100 kHz) | | μH | |
| Self-resonant frequency (1st) | | MHz | |
| Q factor at 1st SRF | | | |
| −3 dB bandwidth | | kHz | |
| Estimated distributed capacitance | | pF | |

Raw data file: `data/[prototype]/[date]_run##_impedance_harmonic.s1p`

**Observations:**

---

## Measurement Set B — Coupling Coefficients

### B1 — Primary to Counter

| Parameter | Value | Unit |
|---|---|---|
| Mutual inductance M | | μH |
| Coupling coefficient k | | dimensionless |
| k = M / √(L_primary · L_counter) | | |

Raw data file: `data/[prototype]/[date]_run##_coupling_p-c.s2p`

### B2 — Primary to Harmonic

| Parameter | Value | Unit |
|---|---|---|
| Mutual inductance M | | μH |
| Coupling coefficient k | | dimensionless |

Raw data file: `data/[prototype]/[date]_run##_coupling_p-h.s2p`

### B3 — Counter to Harmonic

| Parameter | Value | Unit |
|---|---|---|
| Mutual inductance M | | μH |
| Coupling coefficient k | | dimensionless |

Raw data file: `data/[prototype]/[date]_run##_coupling_c-h.s2p`

---

## Measurement Set C — Harmonic Spectrum (if performed)

Drive conditions:
- Drive winding: Primary
- Drive frequency: ___ Hz
- Drive amplitude: ___ Vpp
- Load winding: Counter / Harmonic

| Harmonic | Frequency (Hz) | Amplitude (mV) | Relative to fundamental (dB) |
|---|---|---|---|
| Fundamental (1st) | | | 0 dB (reference) |
| 2nd harmonic | | | |
| 3rd harmonic | | | |
| 5th harmonic | | | |
| 7th harmonic | | | |
| THD | | | % |

**Observations:**

---

## Measurement Set D — Thermal (if performed)

Drive conditions:
- Drive winding: ___
- Drive frequency: ___ Hz
- Drive amplitude: ___ Vpp
- Duration before measurement: 10 min

| Measurement point | Temperature (°C) | Notes |
|---|---|---|
| Point 1 (0° position) | | |
| Point 2 (90° position) | | |
| Point 3 (180° position) | | |
| Point 4 (270° position) | | |
| Ambient | | |
| Max delta T | | |

---

## Comparison Summary (fill in after control + experimental both measured)

| Parameter | V0 Control | V1 Quasi-Periodic | Difference | Significant? |
|---|---|---|---|---|
| Primary SRF (MHz) | | | | Y/N |
| Primary Q | | | | Y/N |
| Primary −3dB BW (kHz) | | | | Y/N |
| Primary C_dist (pF) | | | | Y/N |
| k (primary-counter) | | | | Y/N |
| k (primary-harmonic) | | | | Y/N |

**Significance threshold:** difference > 3× measurement uncertainty, reproducible ≥ 3 runs.

---

## General Observations and Anomalies

*Anything unexpected, unusual, or worth investigating further:*

---

## Next Steps

- [ ] Repeat this run to verify reproducibility
- [ ] 
- [ ] 

---

## Files Generated This Session

```
data/[prototype]/
  [date]_run##_impedance_primary.s1p
  [date]_run##_impedance_counter.s1p
  [date]_run##_impedance_harmonic.s1p
  [date]_run##_coupling_p-c.s2p
  [date]_run##_coupling_p-h.s2p
  [date]_run##_coupling_c-h.s2p
  [date]_run##_notes.md          ← this file
photos/[prototype]/
  [date]_top.jpg
  [date]_side_0deg.jpg
  [date]_side_90deg.jpg
  [date]_isometric.jpg
```

---

*See also: [experimental_protocol.md](experimental_protocol.md)*
