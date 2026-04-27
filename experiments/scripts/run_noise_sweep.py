from __future__ import annotations

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


def run_experiment(flip_probability: float, shots: int = 1000) -> tuple[float, float]:
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

    noise_model = MeasurementNoiseModel(flip_probability=flip_probability, seed=123)
    noisy_counts = sample_noisy_counts(ideal_circuit, noise_model, shots)
    noisy_probs = normalize_counts(noisy_counts)

    confusion_matrix = confusion_matrix_from_model(noise_model)
    mitigated_probs = mitigate_single_qubit_counts(noisy_counts, confusion_matrix)

    noisy_error = abs(noisy_probs.get("0", 0.0) - 1.0)
    mitigated_error = abs(mitigated_probs.get("0", 0.0) - 1.0)

    return noisy_error, mitigated_error


def main() -> None:
    """
    Run a noise sweep and print noisy versus mitigated error.

    Input(s)
    --------
    - parameter : None
        No inputs.

    Output(s)
    ---------
    - return_value : None
        Prints a table comparing noisy and mitigated error.
    """
    noise_levels = [0.0, 0.05, 0.1, 0.2, 0.3, 0.4]
    shots = 1000

    print("Flip Prob | Noisy Error | Mitigated Error")
    print("------------------------------------------")

    for flip_probability in noise_levels:
        noisy_error, mitigated_error = run_experiment(flip_probability, shots)
        print(
            f"{flip_probability:8.2f} | "
            f"{noisy_error:11.4f} | "
            f"{mitigated_error:16.4f}"
        )


if __name__ == "__main__":
    main()
