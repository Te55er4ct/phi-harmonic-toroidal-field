"""
impedance_plotting.py
Quasi-Periodic Toroidal Resonance Structures
R. Wierzbicki, 2026

Processes NanoVNA measurement data and generates comparison plots
between control (V0) and quasi-periodic (V1, V2) prototypes.

Usage:
    python impedance_plotting.py --v0 data/v0/run01.s1p --v1 data/v1/run01.s1p
    python impedance_plotting.py --dir data/  (processes all .s1p files)

Dependencies:
    pip install numpy matplotlib scikit-rf pandas
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import argparse
import os
import sys
from pathlib import Path

try:
    import skrf as rf
    HAS_SKRF = True
except ImportError:
    HAS_SKRF = False
    print("Note: scikit-rf not found. Install with: pip install scikit-rf")
    print("Falling back to manual S1P parsing.")

# ── Style ──────────────────────────────────────────────────────────────────────
plt.style.use('dark_background')
COLORS = {
    'v0': '#888888',   # control — grey
    'v1': '#00aaff',   # quasi-periodic single — blue
    'v2': '#ff4466',   # counter-wound — rose
    'grid': '#1a2a1a',
    'text': '#cccccc',
}

# ── S1P Parser (fallback if scikit-rf not available) ──────────────────────────
def parse_s1p_manual(filepath):
    """
    Parse a Touchstone S1P file manually.
    Returns (frequencies_hz, s11_real, s11_imag)
    """
    frequencies = []
    s11_real = []
    s11_imag = []
    freq_unit = 1.0  # default Hz

    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('!'):
                continue
            if line.startswith('#'):
                parts = line.upper().split()
                if 'HZ' in parts:   freq_unit = 1.0
                if 'KHZ' in parts:  freq_unit = 1e3
                if 'MHZ' in parts:  freq_unit = 1e6
                if 'GHZ' in parts:  freq_unit = 1e9
                continue
            parts = line.split()
            if len(parts) >= 3:
                try:
                    frequencies.append(float(parts[0]) * freq_unit)
                    s11_real.append(float(parts[1]))
                    s11_imag.append(float(parts[2]))
                except ValueError:
                    continue

    return (np.array(frequencies),
            np.array(s11_real),
            np.array(s11_imag))


def s11_to_impedance(s11_real, s11_imag, z0=50.0):
    """Convert S11 (real+imag) to impedance Z."""
    s11 = s11_real + 1j * s11_imag
    z = z0 * (1 + s11) / (1 - s11 + 1e-12)
    return z


def find_srf(frequencies, z_magnitude):
    """Find self-resonant frequency (first impedance peak)."""
    # Find local maxima
    peaks = []
    for i in range(1, len(z_magnitude) - 1):
        if z_magnitude[i] > z_magnitude[i-1] and z_magnitude[i] > z_magnitude[i+1]:
            peaks.append((frequencies[i], z_magnitude[i]))
    if peaks:
        return sorted(peaks, key=lambda x: x[1], reverse=True)[0]
    return None


def calculate_q(frequencies, z_magnitude, srf):
    """Estimate Q factor from -3dB bandwidth around SRF."""
    if srf is None:
        return None
    srf_freq, srf_z = srf
    half_power = srf_z / np.sqrt(2)

    # Find -3dB points
    srf_idx = np.argmin(np.abs(frequencies - srf_freq))
    f_low, f_high = None, None

    for i in range(srf_idx, 0, -1):
        if z_magnitude[i] <= half_power:
            f_low = frequencies[i]
            break
    for i in range(srf_idx, len(frequencies)):
        if z_magnitude[i] <= half_power:
            f_high = frequencies[i]
            break

    if f_low and f_high and f_high > f_low:
        bw = f_high - f_low
        q = srf_freq / bw
        return q, f_low, f_high
    return None


def load_s1p(filepath):
    """Load S1P file, return frequency array and impedance array."""
    if HAS_SKRF:
        try:
            ntwk = rf.Network(filepath)
            freqs = ntwk.f
            s11 = ntwk.s[:, 0, 0]
            z0 = 50.0
            z = z0 * (1 + s11) / (1 - s11 + 1e-12)
            return freqs, z
        except Exception:
            pass

    # Fallback
    f, sr, si = parse_s1p_manual(filepath)
    z = s11_to_impedance(sr, si)
    return f, z


# ── Main Plot Functions ────────────────────────────────────────────────────────

def plot_impedance_comparison(datasets, output_path=None):
    """
    Plot impedance magnitude for multiple prototypes on same axes.

    datasets: list of dicts with keys:
        'label', 'filepath', 'color'
    """
    fig, axes = plt.subplots(2, 1, figsize=(12, 9),
                              facecolor='#0a0f0a', sharex=True)
    fig.suptitle('Impedance Comparison\nQuasi-Periodic vs Control Toroid',
                 color=COLORS['text'], fontsize=14, fontweight='bold')

    ax_mag, ax_phase = axes

    results = {}

    for ds in datasets:
        path = ds['filepath']
        if not os.path.exists(path):
            print(f"File not found: {path}")
            continue

        freqs, z = load_s1p(path)
        z_mag = np.abs(z)
        z_phase = np.angle(z, deg=True)
        freq_mhz = freqs / 1e6

        # Find SRF
        srf = find_srf(freqs, z_mag)
        q_result = calculate_q(freqs, z_mag, srf)

        # Store results
        results[ds['label']] = {
            'srf_hz': srf[0] if srf else None,
            'srf_z': srf[1] if srf else None,
            'q': q_result[0] if q_result else None,
        }

        # Plot magnitude
        ax_mag.semilogy(freq_mhz, z_mag,
                        color=ds.get('color', '#ffffff'),
                        linewidth=1.5, label=ds['label'], alpha=0.9)

        # Mark SRF
        if srf:
            ax_mag.axvline(srf[0]/1e6, color=ds.get('color', '#ffffff'),
                          linestyle='--', alpha=0.35, linewidth=0.8)
            ax_mag.annotate(f"SRF {srf[0]/1e6:.2f} MHz",
                           xy=(srf[0]/1e6, srf[1]),
                           xytext=(5, 5), textcoords='offset points',
                           color=ds.get('color', '#ffffff'),
                           fontsize=8, alpha=0.8)

        # Plot phase
        ax_phase.plot(freq_mhz, z_phase,
                     color=ds.get('color', '#ffffff'),
                     linewidth=1.2, label=ds['label'], alpha=0.85)

    # Format magnitude axis
    ax_mag.set_ylabel('|Z| (Ω)', color=COLORS['text'])
    ax_mag.set_title('Impedance Magnitude', color=COLORS['text'],
                     fontsize=11, pad=4)
    ax_mag.legend(loc='upper right', framealpha=0.3,
                  labelcolor=COLORS['text'], fontsize=10)
    ax_mag.grid(True, alpha=0.15, color=COLORS['grid'])
    ax_mag.tick_params(colors=COLORS['text'])
    ax_mag.spines[:].set_color('#334433')

    # Format phase axis
    ax_phase.set_ylabel('Phase (°)', color=COLORS['text'])
    ax_phase.set_xlabel('Frequency (MHz)', color=COLORS['text'])
    ax_phase.set_title('Impedance Phase', color=COLORS['text'],
                       fontsize=11, pad=4)
    ax_phase.axhline(0, color='#334433', linewidth=0.8, linestyle='-')
    ax_phase.grid(True, alpha=0.15, color=COLORS['grid'])
    ax_phase.tick_params(colors=COLORS['text'])
    ax_phase.spines[:].set_color('#334433')
    ax_phase.set_ylim(-95, 95)

    plt.tight_layout(rect=[0, 0, 1, 0.95])

    if output_path:
        plt.savefig(output_path, dpi=150, bbox_inches='tight',
                    facecolor='#0a0f0a')
        print(f"Saved: {output_path}")
    else:
        plt.show()

    plt.close()
    return results


def print_summary_table(results):
    """Print a formatted comparison table to console."""
    print("\n" + "="*65)
    print("MEASUREMENT SUMMARY")
    print("="*65)
    print(f"{'Prototype':<20} {'SRF (MHz)':<15} {'Peak |Z| (kΩ)':<15} {'Q':<10}")
    print("-"*65)
    for label, data in results.items():
        srf_str = f"{data['srf_hz']/1e6:.3f}" if data['srf_hz'] else "—"
        z_str = f"{data['srf_z']/1e3:.2f}" if data['srf_z'] else "—"
        q_str = f"{data['q']:.1f}" if data['q'] else "—"
        print(f"{label:<20} {srf_str:<15} {z_str:<15} {q_str:<10}")
    print("="*65)

    # Check for significant differences
    srfs = {k: v['srf_hz'] for k, v in results.items() if v['srf_hz']}
    if len(srfs) >= 2:
        vals = list(srfs.values())
        pct_diff = abs(vals[0] - vals[1]) / vals[0] * 100
        print(f"\nSRF difference: {pct_diff:.1f}%")
        if pct_diff > 5:
            print("→ Potentially significant difference — verify with repeated runs")
        else:
            print("→ Difference within typical measurement uncertainty")
    print()


# ── CLI ────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='Impedance comparison plots for quasi-periodic toroid project'
    )
    parser.add_argument('--v0', help='Path to control (V0) S1P file')
    parser.add_argument('--v1', help='Path to quasi-periodic (V1) S1P file')
    parser.add_argument('--v2', help='Path to counter-wound (V2) S1P file')
    parser.add_argument('--output', help='Output image path (PNG)',
                        default='impedance_comparison.png')
    args = parser.parse_args()

    datasets = []
    if args.v0:
        datasets.append({'label': 'V0 Control',
                        'filepath': args.v0,
                        'color': COLORS['v0']})
    if args.v1:
        datasets.append({'label': 'V1 Quasi-Periodic',
                        'filepath': args.v1,
                        'color': COLORS['v1']})
    if args.v2:
        datasets.append({'label': 'V2 Counter-Wound',
                        'filepath': args.v2,
                        'color': COLORS['v2']})

    if not datasets:
        print("No data files specified.")
        print("Usage: python impedance_plotting.py --v0 data/v0/run01.s1p "
              "--v1 data/v1/run01.s1p")
        print("\nGenerating demo plot with synthetic data...")
        datasets = generate_demo_data()

    results = plot_impedance_comparison(datasets, args.output)
    print_summary_table(results)


def generate_demo_data():
    """Generate synthetic demo data if no real files provided."""
    import tempfile

    def synthetic_s1p(filename, srf_mhz, q, label):
        freqs = np.linspace(1e5, 3e7, 1001)
        # Simple resonance model
        f0 = srf_mhz * 1e6
        z0 = 50.0
        L = 5e-6
        C = 1 / ((2 * np.pi * f0)**2 * L)
        R = f0 / q * 2 * np.pi * L

        omega = 2 * np.pi * freqs
        z = R + 1j * (omega * L - 1 / (omega * C))
        s11 = (z - z0) / (z + z0)

        with open(filename, 'w') as f:
            f.write(f"! Synthetic demo data — {label}\n")
            f.write("# MHz S RI R 50\n")
            for i, freq in enumerate(freqs):
                f.write(f"{freq/1e6:.6f} "
                       f"{s11[i].real:.6f} {s11[i].imag:.6f}\n")

    tmpdir = tempfile.mkdtemp()
    f_v0 = os.path.join(tmpdir, 'demo_v0.s1p')
    f_v1 = os.path.join(tmpdir, 'demo_v1.s1p')

    synthetic_s1p(f_v0, srf_mhz=8.2, q=85, label='V0 Control')
    synthetic_s1p(f_v1, srf_mhz=9.7, q=120, label='V1 Quasi-Periodic (demo)')

    return [
        {'label': 'V0 Control (demo)',         'filepath': f_v0, 'color': COLORS['v0']},
        {'label': 'V1 Quasi-Periodic (demo)',  'filepath': f_v1, 'color': COLORS['v1']},
    ]


if __name__ == '__main__':
    main()
