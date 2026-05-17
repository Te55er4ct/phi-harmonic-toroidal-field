# Measurement Log Template
**Prototype:** [V0 / V1 / V2 / V3]
**Run number:** [01, 02, 03...]
**Date:** YYYY-MM-DD
**Operator:** [name]

## Conditions
- Temperature: __ °C (±2)
- Humidity: __ % RH
- Calibration verified: [ ] Yes (S11 load = __ dB)
- Warm-up time: __ minutes

## DC Verification
| Winding | Expected R (Ω) | Measured R (Ω) | Pass/Fail |
|---------|----------------|----------------|------------|
| Primary | __ | __ | [ ] |
| Counter | __ | __ | [ ] |
| Harmonic | __ | __ | [ ] |

Inter-winding shorts: [ ] None (all pairs > 1 MΩ)

## Measurement Set A — Impedance Sweep
| Parameter | Value | Notes |
|-----------|-------|-------|
| SRF (MHz) | __ | |
| Q at SRF | __ | |
| L at 100 kHz (μH) | __ | |
| C_dist (pF) | __ | |

File: `data/prototype_v0/YYYY-MM-DD_run01_impedance_primary.csv`

## Measurement Set B — Coupling (if V3)
| Pair | k | M (μH) |
|------|---|---|
| P→C | __ | __ |
| P→H | __ | __ |
| C→H | __ | __ |

## Thermal (if measured)
| Drive power (W) | ΔT (°C) | Max temp (°C) |
|----------------|---------|----------------|
| __ | __ | __ |

## Deviations from Protocol
[Describe any differences from experimental_protocol.md]

## Signature
[Name / initials]
