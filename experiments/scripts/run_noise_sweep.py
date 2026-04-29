from __future__ import annotations

import csv
from pathlib import Path

from experiments.scripts.run_readout_mitigation_demo import (
    build_single_qubit_measurement_circuit,
    normalize_counts,
    sample_noisy_counts,
)
from qc_compiler.mitigation import (
    confusion_matrix_from_model,
    mitigate_single_qubit_counts,
)
from qc_compiler.noise import MeasurementNoiseModel


PROJECT_ROOT = Path(__file__).resolve().parents[2]
RESULTS_PATH = PROJECT_ROOT / "experiments" / "results" / "noise_sweep_results.csv"


def run_experiment(flip_probability: float, shots: int = 5000) -> tuple[float, float]:
    """
    Run one noise-sweep experiment.

    Input(s)
    --------
    - flip_probability : float
        Probability that a measured bit flips during readout.
    - shots : int
        Number of samples used to estimate the noisy distribution.

    Output(s)
    ---------
    - return_value : tuple[float, float]
        Pair containing noisy error and mitigated error, respectively.
    """
    if not isinstance(flip_probability, (int, float)):
        raise TypeError("flip_probability must be a number.")

    flip_probability = float(flip_probability)
    if flip_probability < 0.0 or flip_probability > 1.0:
        raise ValueError("flip_probability must be a number between 0 and 1.")

    if not isinstance(shots, int):
        raise TypeError("shots must be an integer.")
    if shots <= 0:
        raise ValueError("shots must be greater than 0.")

    ideal_circuit = build_single_qubit_measurement_circuit()

    noise_model = MeasurementNoiseModel(flip_probability=flip_probability, seed=None)
    noisy_counts = sample_noisy_counts(ideal_circuit, noise_model, shots)
    noisy_probs = normalize_counts(noisy_counts)

    confusion_matrix = confusion_matrix_from_model(noise_model)
    mitigated_probs = mitigate_single_qubit_counts(noisy_counts, confusion_matrix)

    noisy_error = abs(noisy_probs.get("0", 0.0) - 1.0)
    mitigated_error = abs(mitigated_probs.get("0", 0.0) - 1.0)

    return noisy_error, mitigated_error


def average_experiment(
    flip_probability: float,
    shots: int,
    repeats: int,
) -> tuple[float, float]:
    """
    Average noisy and mitigated errors across repeated experiments.

    Input(s)
    --------
    - flip_probability : float
        Probability that a measured bit flips during readout.
    - shots : int
        Number of samples used in each repeated experiment.
    - repeats : int
        Number of independent repeated experiments to average.

    Output(s)
    ---------
    - return_value : tuple[float, float]
        Pair containing average noisy error and average mitigated error.
    """
    if not isinstance(repeats, int):
        raise TypeError("repeats must be an integer.")
    if repeats <= 0:
        raise ValueError("repeats must be greater than 0.")

    noisy_errors: list[float] = []
    mitigated_errors: list[float] = []

    for _ in range(repeats):
        noisy_error, mitigated_error = run_experiment(flip_probability, shots)
        noisy_errors.append(noisy_error)
        mitigated_errors.append(mitigated_error)

    return (
        sum(noisy_errors) / repeats,
        sum(mitigated_errors) / repeats,
    )


def save_results(
    results: list[dict[str, float]],
    output_path: Path,
) -> None:
    """
    Save noise sweep results to a CSV file.

    Input(s)
    --------
    - results : list[dict[str, float]]
        List of result rows containing flip probability, noisy error, and mitigated error.
    - output_path : Path
        File path where the CSV output should be written.

    Output(s)
    ---------
    - return_value : None
        Writes the results to disk.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=["flip_probability", "noisy_error", "mitigated_error"],
        )
        writer.writeheader()
        writer.writerows(results)


def main() -> None:
    """
    Run a noise sweep, print results, and save them to disk.

    Input(s)
    --------
    - parameter : None
        No inputs.

    Output(s)
    ---------
    - return_value : None
        Prints and saves a table comparing noisy and mitigated error.
    """
    noise_levels = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4]
    shots = 5000
    repeats = 5
    results: list[dict[str, float]] = []

    print("Flip Prob | Noisy Error | Mitigated Error")
    print("------------------------------------------")

    for flip_probability in noise_levels:
        noisy_error, mitigated_error = average_experiment(
            flip_probability,
            shots,
            repeats,
        )
        results.append(
            {
                "flip_probability": flip_probability,
                "noisy_error": round(noisy_error, 6),
                "mitigated_error": round(mitigated_error, 6),
            }
        )
        print(
            f"{flip_probability:8.2f} | "
            f"{noisy_error:11.4f} | "
            f"{mitigated_error:16.4f}"
        )

    save_results(results, RESULTS_PATH)


if __name__ == "__main__":
    main()
