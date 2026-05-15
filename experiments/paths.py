from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXPERIMENTS_DIR = PROJECT_ROOT / "experiments"
RESULTS_DIR = EXPERIMENTS_DIR / "results"


NOISE_SWEEP_RESULTS_PATH = RESULTS_DIR / "noise_sweep_results.csv"
NOISE_SWEEP_PLOT_PATH = RESULTS_DIR / "noise_sweep_plot.png"

CIRCUIT_COMPARISON_RESULTS_PATH = RESULTS_DIR / "circuit_comparison_results.csv"
CIRCUIT_COMPARISON_PLOT_PATH = RESULTS_DIR / "circuit_comparison_plot.png"
