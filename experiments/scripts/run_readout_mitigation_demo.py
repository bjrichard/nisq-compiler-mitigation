from __future__ import annotations

from qc_compiler.circuits import Circuit, Gate, Qubit
from qc_compiler.execution import sample_counts
from qc_compiler.mitigation import (
    confusion_matrix_from_model,
    mitigate_single_qubit_counts,
)
from qc_compiler.noise import MeasurementNoiseModel


def build_single_qubit_measurement_circuit() -> Circuit:
    """
    Build a simple single-qubit circuit with one measurement.

    Input(s)
    --------
    - parameter : None
        No inputs.

    Output(s)
    ---------
    - return_value : Circuit
        Circuit containing a single measurement on qubit 0.
    """
    q0 = Qubit(0)
    circuit = Circuit()
    circuit.add_gate(Gate(name="MEASURE", targets=[q0]))
    return circuit


def normalize_counts(counts: dict[str, int]) -> dict[str, float]:
    """
    Convert counts into probabilities.

    Input(s)
    --------
    - counts : dict[str, int]
        Mapping from bitstring to observed frequency.

    Output(s)
    ---------
    - return_value : dict[str, float]
        Mapping from bitstring to empirical probability.
    """
    if not isinstance(counts, dict):
        raise TypeError("counts must be a dictionary.")

    total = sum(counts.values())
    if total <= 0:
        raise ValueError("counts must sum to a positive value.")

    return {bitstring: count / total for bitstring, count in counts.items()}


def sample_noisy_counts(
    circuit: Circuit,
    noise_model: MeasurementNoiseModel,
    shots: int,
) -> dict[str, int]:
    """
    Sample noisy measurement outcomes multiple times.

    Input(s)
    --------
    - circuit : Circuit
        Ideal circuit to sample.
    - noise_model : MeasurementNoiseModel
        Noise model applied independently on each shot.
    - shots : int
        Number of repeated samples.

    Output(s)
    ---------
    - return_value : dict[str, int]
        Mapping from bitstring to observed noisy counts.
    """
    if not isinstance(circuit, Circuit):
        raise TypeError("circuit must be a Circuit instance.")
    if not isinstance(noise_model, MeasurementNoiseModel):
        raise TypeError("noise_model must be a MeasurementNoiseModel instance.")
    if not isinstance(shots, int) or shots <= 0:
        raise ValueError("shots must be a positive integer.")

    counts: dict[str, int] = {}

    for _ in range(shots):
        noisy_circuit = noise_model.apply(circuit)
        shot_counts = sample_counts(noisy_circuit, shots=1)
        bitstring = next(iter(shot_counts))
        counts[bitstring] = counts.get(bitstring, 0) + 1

    return counts


def main() -> None:
    """
    Run a simple readout-noise mitigation demo.

    Input(s)
    --------
    - parameter : None
        No inputs.

    Output(s)
    ---------
    - return_value : None
        Prints ideal, noisy, and mitigated single-qubit distributions.
    """
    shots = 1000
    ideal_circuit = build_single_qubit_measurement_circuit()

    ideal_counts = sample_counts(ideal_circuit, shots=shots)
    ideal_probs = normalize_counts(ideal_counts)

    noise_model = MeasurementNoiseModel(flip_probability=0.2, seed=123)
    noisy_counts = sample_noisy_counts(ideal_circuit, noise_model, shots)
    noisy_probs = normalize_counts(noisy_counts)

    confusion_matrix = confusion_matrix_from_model(noise_model)
    mitigated_probs = mitigate_single_qubit_counts(noisy_counts, confusion_matrix)

    error_noisy = abs(noisy_probs["0"] - ideal_probs["0"])
    error_mitigated = abs(mitigated_probs["0"] - ideal_probs["0"])

    print("Ideal probabilities")
    print("-------------------")
    print(ideal_probs)
    print()

    print("Noisy observed probabilities")
    print("----------------------------")
    print(noisy_probs)
    print()

    print("Mitigated probabilities")
    print("-----------------------")
    print(mitigated_probs)
    print()

    print("Absolute error in P(0)")
    print("----------------------")
    print(f"Noisy: {error_noisy}")
    print(f"Mitigated: {error_mitigated}")


if __name__ == "__main__":
    main()
