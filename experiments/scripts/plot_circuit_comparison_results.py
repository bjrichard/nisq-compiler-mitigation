from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt


PROJECT_ROOT = Path(__file__).resolve().parents[2]

RESULTS_PATH = (
    PROJECT_ROOT
    / "experiments"
    / "results"
    / "circuit_comparison_results.csv"
)

FIGURE_PATH = (
    PROJECT_ROOT
    / "experiments"
    / "results"
    / "circuit_comparison_plot.png"
)


def load_results(
    path: Path,
) -> list[dict[str, str]]:
    """
    Load comparison experiment results from CSV.

    Input(s)
    --------
    - path : Path
        CSV file path.

    Output(s)
    ---------
    - return_value : list[dict[str, str]]
        Loaded CSV rows.
    """
    with path.open("r") as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def extract_series(
    rows: list[dict[str, str]],
    circuit_type: str,
) -> tuple[list[float], list[float], list[float]]:
    """
    Extract plotting series for a specific circuit type.

    Input(s)
    --------
    - rows : list[dict[str, str]]
        Loaded CSV rows.
    - circuit_type : str
        Circuit category to extract.

    Output(s)
    ---------
    - return_value : tuple[list[float], list[float], list[float]]
        Flip probabilities, noisy errors, mitigated errors.
    """
    flip_probs: list[float] = []
    noisy_errors: list[float] = []
    mitigated_errors: list[float] = []

    for row in rows:
        if row["circuit_type"] != circuit_type:
            continue

        flip_probs.append(float(row["flip_probability"]))
        noisy_errors.append(float(row["noisy_error"]))
        mitigated_errors.append(float(row["mitigated_error"]))

    return flip_probs, noisy_errors, mitigated_errors


def plot_results(
    rows: list[dict[str, str]],
    output_path: Path,
) -> None:
    """
    Plot deterministic and superposition mitigation results.

    Input(s)
    --------
    - rows : list[dict[str, str]]
        Loaded experiment rows.
    - output_path : Path
        Figure output path.

    Output(s)
    ---------
    - return_value : None
        Saves plot to disk.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    (
        measurement_flip_probs,
        measurement_noisy,
        measurement_mitigated,
    ) = extract_series(rows, "measurement_only")

    (
        superposition_flip_probs,
        superposition_noisy,
        superposition_mitigated,
    ) = extract_series(rows, "superposition")

    plt.figure()

    plt.plot(
        measurement_flip_probs,
        measurement_noisy,
        marker="o",
        label="Measurement-only noisy",
    )

    plt.plot(
        measurement_flip_probs,
        measurement_mitigated,
        marker="o",
        label="Measurement-only mitigated",
    )

    plt.plot(
        superposition_flip_probs,
        superposition_noisy,
        marker="o",
        label="Superposition noisy",
    )

    plt.plot(
        superposition_flip_probs,
        superposition_mitigated,
        marker="o",
        label="Superposition mitigated",
    )

    plt.xlabel("Flip probability")
    plt.ylabel("Absolute error in P(0)")
    plt.title("Circuit Type Comparison")

    plt.legend()
    plt.grid()

    plt.savefig(output_path)
    plt.close()


def main() -> None:
    """
    Load results and generate a comparison plot.

    Input(s)
    --------
    - parameter : None
        No inputs.

    Output(s)
    ---------
    - return_value : None
        Saves plot to disk.
    """
    rows = load_results(RESULTS_PATH)

    plot_results(rows, FIGURE_PATH)

    print(f"Saved plot to: {FIGURE_PATH}")


if __name__ == "__main__":
    main()
