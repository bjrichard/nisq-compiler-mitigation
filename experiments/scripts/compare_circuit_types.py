from __future__ import annotations

from experiments.scripts.run_readout_mitigation_demo import (
    build_single_qubit_measurement_circuit,
    normalize_counts,
    sample_noisy_counts,
)
from experiments.scripts.run_statevector_readout_mitigation_demo import (
    build_single_qubit_superposition_circuit,
    sample_noisy_statevector_counts,
)
from experiments.summary import format_error_table

from qc_compiler.execution import sample_counts, sample_statevector_counts
from qc_compiler.mitigation import (
    confusion_matrix_from_model,
    mitigate_single_qubit_counts,
)
from qc_compiler.noise import MeasurementNoiseModel

from experiments.config import DEFAULT_CONFIG


def absolute_error_p0(
    observed_probs: dict[str, float],
    ideal_probs: dict[str, float],
) -> float:
    """
    Return absolute error in the probability of observing 0.

    Input(s)
    --------
    - observed_probs : dict[str, float]
        Observed or mitigated probability distribution.
    - ideal_probs : dict[str, float]
        Ideal probability distribution.

    Output(s)
    ---------
    - return_value : float
        Absolute error in P(0).
    """
    return abs(observed_probs.get("0", 0.0) - ideal_probs.get("0", 0.0))


def run_measurement_only_case(
    flip_probability: float,
    shots: int,
) -> dict[str, float]:
    """
    Run mitigation experiment for a measurement-only circuit.

    Input(s)
    --------
    - flip_probability : float
        Probability of readout bit flip.
    - shots : int
        Number of samples.

    Output(s)
    ---------
    - return_value : dict[str, float]
        Error summary for noisy and mitigated distributions.
    """
    circuit = build_single_qubit_measurement_circuit()
    ideal_counts = sample_counts(circuit, shots=shots)
    ideal_probs = normalize_counts(ideal_counts)

    noise_model = MeasurementNoiseModel(flip_probability=flip_probability, seed=123)
    noisy_counts = sample_noisy_counts(circuit, noise_model, shots)
    noisy_probs = normalize_counts(noisy_counts)

    confusion_matrix = confusion_matrix_from_model(noise_model)
    mitigated_probs = mitigate_single_qubit_counts(noisy_counts, confusion_matrix)

    return {
        "noisy_error": absolute_error_p0(noisy_probs, ideal_probs),
        "mitigated_error": absolute_error_p0(mitigated_probs, ideal_probs),
    }


def run_superposition_case(
    flip_probability: float,
    shots: int,
) -> dict[str, float]:
    """
    Run mitigation experiment for a single-qubit superposition circuit.

    Input(s)
    --------
    - flip_probability : float
        Probability of readout bit flip.
    - shots : int
        Number of samples.

    Output(s)
    ---------
    - return_value : dict[str, float]
        Error summary for noisy and mitigated distributions.
    """
    circuit = build_single_qubit_superposition_circuit()
    ideal_counts = sample_statevector_counts(circuit, shots=shots, seed=123)
    ideal_probs = normalize_counts(ideal_counts)

    noise_model = MeasurementNoiseModel(flip_probability=flip_probability, seed=456)
    noisy_counts = sample_noisy_statevector_counts(
        circuit,
        noise_model,
        shots=shots,
        seed=123,
    )
    noisy_probs = normalize_counts(noisy_counts)

    confusion_matrix = confusion_matrix_from_model(noise_model)
    mitigated_probs = mitigate_single_qubit_counts(noisy_counts, confusion_matrix)

    return {
        "noisy_error": absolute_error_p0(noisy_probs, ideal_probs),
        "mitigated_error": absolute_error_p0(mitigated_probs, ideal_probs),
    }


def main() -> None:
    """
    Compare deterministic and superposition mitigation behavior.

    Input(s)
    --------
    - parameter : None
        No inputs.

    Output(s)
    ---------
    - return_value : None
        Prints noisy and mitigated error for two circuit types.
    """
    flip_probability = DEFAULT_CONFIG.flip_probability
    shots = DEFAULT_CONFIG.shots

    measurement = run_measurement_only_case(flip_probability, shots)
    superposition = run_superposition_case(flip_probability, shots)

    print(
        format_error_table(
            [
                (
                    "Measurement-only",
                    measurement["noisy_error"],
                    measurement["mitigated_error"],
                ),
                (
                    "Superposition",
                    superposition["noisy_error"],
                    superposition["mitigated_error"],
                ),
            ]
        )
    )


if __name__ == "__main__":
    main()
