from __future__ import annotations

import csv
from pathlib import Path

from experiments.scripts.compare_circuit_types import (
    run_measurement_only_case,
    run_superposition_case,
)


PROJECT_ROOT = Path(__file__).resolve().parents[2]

RESULTS_PATH = (
    PROJECT_ROOT
    / "experiments"
    / "results"
    / "circuit_comparison_results.csv"
)


def save_results(
    rows: list[dict[str, float | str]],
    output_path: Path,
) -> None:
    """
    Save comparison experiment results to CSV.

    Input(s)
    --------
    - rows : list[dict[str, float | str]]
        Rows to write to disk.
    - output_path : Path
        Destination CSV path.

    Output(s)
    ---------
    - return_value : None
        Writes CSV results to disk.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=[
                "circuit_type",
                "flip_probability",
                "noisy_error",
                "mitigated_error",
            ],
        )

        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    """
    Run comparison experiments and save results.

    Input(s)
    --------
    - parameter : None
        No inputs.

    Output(s)
    ---------
    - return_value : None
        Saves experiment results to CSV.
    """
    noise_levels = [0.0, 0.05, 0.1, 0.2, 0.3, 0.4]
    shots = 5000

    rows: list[dict[str, float | str]] = []

    for flip_probability in noise_levels:
        measurement = run_measurement_only_case(
            flip_probability,
            shots,
        )

        rows.append(
            {
                "circuit_type": "measurement_only",
                "flip_probability": flip_probability,
                "noisy_error": round(measurement["noisy_error"], 6),
                "mitigated_error": round(
                    measurement["mitigated_error"],
                    6,
                ),
            }
        )

        superposition = run_superposition_case(
            flip_probability,
            shots,
        )

        rows.append(
            {
                "circuit_type": "superposition",
                "flip_probability": flip_probability,
                "noisy_error": round(superposition["noisy_error"], 6),
                "mitigated_error": round(
                    superposition["mitigated_error"],
                    6,
                ),
            }
        )

    save_results(rows, RESULTS_PATH)

    print(f"Saved results to: {RESULTS_PATH}")


if __name__ == "__main__":
    main()
