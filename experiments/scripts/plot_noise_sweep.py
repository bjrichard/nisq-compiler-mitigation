from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt


PROJECT_ROOT = Path(__file__).resolve().parents[2]
RESULTS_PATH = PROJECT_ROOT / "experiments" / "results" / "noise_sweep_results.csv"
FIGURE_PATH = PROJECT_ROOT / "experiments" / "results" / "noise_sweep_plot.png"


def load_results(path: Path) -> tuple[list[float], list[float], list[float]]:
    """
    Load noise sweep results from CSV.

    Returns:
        flip probabilities, noisy errors, mitigated errors
    """
    flip_probs: list[float] = []
    noisy_errors: list[float] = []
    mitigated_errors: list[float] = []

    with path.open("r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            flip_probs.append(float(row["flip_probability"]))
            noisy_errors.append(float(row["noisy_error"]))
            mitigated_errors.append(float(row["mitigated_error"]))

    return flip_probs, noisy_errors, mitigated_errors


def plot_results(
    flip_probs: list[float],
    noisy_errors: list[float],
    mitigated_errors: list[float],
    output_path: Path,
) -> None:
    """
    Plot noisy vs mitigated error.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure()

    plt.plot(flip_probs, noisy_errors, marker="o", label="Noisy error")
    plt.plot(flip_probs, mitigated_errors, marker="o", label="Mitigated error")

    plt.xlabel("Flip probability")
    plt.ylabel("Absolute error in P(0)")
    plt.title("Readout Error Mitigation Performance")

    plt.legend()
    plt.grid()

    plt.savefig(output_path)
    plt.close()


def main() -> None:
    flip_probs, noisy_errors, mitigated_errors = load_results(RESULTS_PATH)

    plot_results(
        flip_probs,
        noisy_errors,
        mitigated_errors,
        FIGURE_PATH,
    )

    print(f"Plot saved to: {FIGURE_PATH}")


if __name__ == "__main__":
    main()
