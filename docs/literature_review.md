# Literature Review & Research Precedents
## Phi-Harmonic Toroidal Field Research

---

## Introduction

This project tests a narrow, falsifiable engineering question: does
phi-proportioned toroidal coil geometry and golden-angle (137.5°) winding
distribution produce measurably different electrical and field
characteristics compared to a conventional toroid wound with the same wire
gauge, turn count, and core dimensions?

This document surveys the published work directly relevant to that question.
It deliberately excludes sources whose claims are not accepted by mainstream
physics or medicine, even where those sources historically inspired interest
in resonance-based or toroidal devices. Citing discredited or non-replicated
work as supporting evidence would misrepresent the actual evidentiary basis
for this project and invites — correctly — the "quack device" framing this
project should avoid. The honest position is: this is original instrumentation
work motivated by one narrow, real, non-replicated prior result, not a
synthesis of an established field.

---

## I. THE PRIOR RESULT THIS PROJECT EXTENDS

### Purnell, M.C., Butawan, M.B.A., Ramsey, R.D. — "Bio-field array: a
dielectrophoretic electromagnetic toroidal excitation to restore and
maintain the golden ratio in human erythrocytes" (2018)
*Physiological Reports, Vol. 6, Issue 12*
*US Patent 2017/0232253; PCT/US18/26932*

**What it is:** An IRB-approved human pilot study (n=20) using a toroidal
electromagnetic array with phi-proportioned geometry, DC-excited (2.5–3A)
through conductive rings in a hypotonic saline foot bath. Measured red
blood cell morphology and select serum chemistry before/after six
35-minute sessions over two weeks.

**Reported results:** RBC morphology shifted toward golden-ratio
proportions following treatment; reduced rouleaux (RBC stacking)
formation; decreased serum CO2 (p=0.017).

**What this does and does not establish:**
- It is the only published human trial of a phi-proportioned toroidal EM
  device that this review identified. It is real, peer-reviewed (note:
  *Physiological Reports* is a legitimate but lower-impact open-access
  journal, not a flagship physiology venue), and reports a specific,
  checkable result.
- It does **not** establish that phi geometry specifically is the active
  variable — the study used a single device with no non-phi control
  geometry. The morphological effect could be attributable to the DC
  field, the saline coupling, the toroidal topology generally, or the phi
  proportioning specifically; the design cannot distinguish between these.
- It does not generalize to AC excitation, air-core devices, or any
  outcome beyond RBC morphology and the one serum marker reported.
- As of this writing, no independent replication of this device or result
  has been published. Citation count is low and consists mostly of papers
  citing the golden-ratio-RBC theoretical background, not replications.

**This project's relationship to it:** This is a parametric extension, not
a validation. Purnell's result is the single concrete data point motivating
the question "does phi-proportioned toroidal geometry matter electromagnetically,"
applied here to a structurally different implementation (AC pulsed, air-core,
no biological subject) specifically to isolate the geometric variable Purnell's
single-device design could not isolate.

---

## II. BACKGROUND PHYSICS — TOROIDAL FIELD CONFIGURATIONS

### FLEET Project (Flying Electromagnetic Toroids) — University of
Southampton, ERC Advanced Grant

Studies the generation and propagation of toroidal electromagnetic pulses
at optical frequencies. Relevance to this project is narrow: it confirms
that toroidal (donut-topology) field configurations are legitimate,
non-trivial solutions to Maxwell's equations, studied by mainstream
academic physics with major institutional funding. It says nothing about
biological effects, golden-ratio geometry, or Hz/kHz-frequency behavior —
those are separate, untested extrapolations this project does not claim
FLEET supports.

### Zhang & Ou-Yang — golden ratio in erythrocyte morphology (2016, arXiv preprint)

A theoretical analysis proposing that healthy resting RBC geometry
approximates golden-ratio proportions. Provides the geometric premise
underlying Purnell's measurement choice (why measure RBC morphology
specifically). Note: arXiv preprints are not peer-reviewed; this is cited
as background context for why Purnell chose that outcome measure, not as
independently validated fact.

---

## III. WHAT THIS PROJECT DOES NOT CLAIM

To be explicit about scope, this project does not claim or rely on:

- Cellular-resonance disease theories (e.g., Lakhovsky's multi-wave
  oscillator and associated cancer claims). These were never
  independently replicated and are not accepted by mainstream oncology
  or biophysics. They are not part of this project's evidentiary basis.
- Orgone or bioelectric "energy" theories (e.g., Reich). The FDA obtained
  a federal injunction against related devices in the 1950s for false
  medical claims. Not part of this project's evidentiary basis.
- "Scalar wave" physics claiming superluminal propagation or Faraday-cage
  penetration (e.g., Meyl). Not accepted by mainstream physics; published
  outside mainstream physics venues. If Phase 3 testing (Faraday-cage
  transmission comparison across winding configurations) shows any
  unexpected transmission difference, that result will be reported and
  investigated as an anomaly to be explained by conventional means first
  — not interpreted as confirmation of scalar-wave theory.
- Any disease-treatment, cancer-treatment, or other health claim. This
  project's measurements are electrical and field-distribution
  characteristics (inductance, Q, SRF, field strength/geometry). It is
  not a medical device and makes no therapeutic claims.

---

## IV. OPEN QUESTIONS THIS PROJECT IS DESIGNED TO ADDRESS

1. **Does phi-proportioned toroidal geometry produce measurably different
   field distributions than a conventional toroid of identical wire,
   turns, and core dimensions?** Addressed by V1 (control) vs V2
   (phi-shell) comparison.
2. **Does golden-angle (137.5°) winding distribution produce measurably
   different standing-wave or field patterns than periodic winding, holding
   geometry constant?** Addressed by V2 vs V3 comparison.
3. **Do opposing-direction windings at 120° phase offset produce any
   measurable difference in Faraday-cage transmission compared to a
   single-winding control?** Addressed by Phase 3. This is an electrical
   engineering question (does the field couple through a grounded
   enclosure differently), framed without reference to scalar-wave theory.
4. **Can the Purnell (2018) RBC morphology result be replicated using an
   open-source implementation, and does it depend on phi geometry
   specifically (testable via the V1/V2/V3 control)?** A long-horizon
   question; any work here would need a proper IRB-equivalent protocol and
   is out of scope for current hardware-characterization phases.

None of these questions require, or benefit from, invoking cellular
resonance theory, orgone theory, or scalar wave physics to ask or answer.

---

## V. ADDENDUM — Phi-Reduction of Astronomical Periods vs. Node Series

*(Carried forward unchanged from the prior review — this section already
meets the evidentiary standard the rest of this document now follows.)*

### Background

Hans Cousto's "Cosmic Octave" method reduces a natural period to an
audible frequency by repeated octave doubling/halving. The node series
used in this project's frequency design, f(n) = 111 × φ^(n/3), uses phi
scaling instead of octave scaling. This section tests whether natural
astronomical periods, phi-reduced instead of octave-reduced, land near
frequencies already present in the node series — a series derived with no
reference to astronomy.

### Results

| Source | Octave-reduced (Hz) | Phi-reduced (Hz) | Nearest node | Δ |
|---|---|---|---|---|
| Earth sidereal day | 194.71 | 148.00 | node[2] = 152.98 | −3.26% |
| Earth solar day | 194.18 | 147.59 | node[2] = 152.98 | −3.52% |
| Earth orbital year | 136.10 | 130.11 | node[1] = 130.31 | −0.15% |
| Lunar sidereal month | 113.72 | 156.85 | node[2] = 152.98 | +2.52% |
| Lunar synodic month | 105.21 | 211.30* | node[4] = 210.85 | +0.20% |
| Schumann resonance | 125.28 | 140.50 | node[1] = 130.31 | +7.82% |

*Reduced by one additional φ-octave for direct comparison.

### Interpretation

2 of 6 independently phi-reduced periods land within 0.2% of pre-existing
node frequencies; the remaining 4 miss by 2.5–8%. This is reported as a
2-out-of-6 correspondence, not a uniform pattern. With 8 node frequencies
and 6 candidate periods, some near-coincidence is statistically expected by
chance; a rigorous treatment requires testing hit rates against a null
distribution of random period sets before treating this as more than a
suggestive observation. **No causal or physically meaningful relationship
between astronomical periods and node frequencies is claimed.**

### Sources

Fiorenza, N.A. *Planetary Parameter Comparisons*. Rev. 2.0.0, 1987.
Cousto, H. *The Cosmic Octave: Origin of Harmony*. LifeRhythm, 1988.

---

## VI. COMPLETE SOURCE LIST

| Author | Title | Year | Venue | Status |
|---|---|---|---|---|
| Purnell, Butawan, Ramsey | Bio-field array... | 2018 | *Physiological Reports* 6(12) | Peer-reviewed, n=20, not independently replicated |
| Zhang & Ou-Yang | Golden ratio in erythrocyte morphology | 2016 | arXiv preprint | Not peer-reviewed; theoretical background only |
| FLEET Project, U. Southampton | Flying Electromagnetic Toroids | 2023+ | ERC-funded research program | Mainstream physics; unrelated to bio-effects |
| Fiorenza, N.A. | Planetary Parameter Comparisons | 1987 | Self-published reference tables | Source data for Section V only |
| Cousto, H. | The Cosmic Octave | 1988 | LifeRhythm | Source data for Section V only |

---

*Literature review — revised 2026-06-25 to remove non-replicated and
discredited sources (Lakhovsky, Reich, Meyl, Hollwich, Sloan) that were
present in the prior draft. Scope narrowed to sources that are either
peer-reviewed with stated limitations, or explicitly marked as background/
theoretical context. No disease-treatment or health claims are made by
this project.*
