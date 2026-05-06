from __future__ import annotations

from qc_compiler.circuits import Circuit, Gate, Qubit
from qc_compiler.execution import sample_statevector_counts
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


def build_single_qubit_superposition_circuit() -> Circuit:
    """
    Build a single-qubit circuit that prepares a superposition state.

    Input(s)
    --------
    - parameter : None
        No inputs.

    Output(s)
    ---------
    - return_value : Circuit
        Circuit that applies H then measures.
    """
    q0 = Qubit(0)
    circuit = Circuit()
    circuit.add_gate(Gate(name="H", targets=[q0]))
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

    for bitstring, count in counts.items():
        if not isinstance(bitstring, str):
            raise TypeError("bitstring keys must be strings.")
        if not isinstance(count, int):
            raise TypeError("count values must be integers.")
        if count < 0:
            raise ValueError("count values must be non-negative.")

    total = sum(counts.values())
    if total <= 0:
        raise ValueError("counts must sum to a positive value.")

    return {bitstring: count / total for bitstring, count in counts.items()}


def sample_noisy_statevector_counts(
    circuit: Circuit,
    noise_model: MeasurementNoiseModel,
    shots: int,
    seed: int | None = None,
) -> dict[str, int]:
    """
    Sample statevector outcomes with independent readout noise.

    Input(s)
    --------
    - circuit : Circuit
        Ideal circuit to sample using statevector simulation.
    - noise_model : MeasurementNoiseModel
        Measurement noise model applied independently to each sampled bitstring.
    - shots : int
        Number of repeated samples.
    - seed : int | None
        Optional random seed for reproducible ideal sampling.

    Output(s)
    ---------
    - return_value : dict[str, int]
        Mapping from bitstring to noisy observed counts.
    """
    if not isinstance(circuit, Circuit):
        raise TypeError("circuit must be a Circuit instance.")
    if not isinstance(noise_model, MeasurementNoiseModel):
        raise TypeError("noise_model must be a MeasurementNoiseModel instance.")
    if not isinstance(shots, int) or shots <= 0:
        raise ValueError("shots must be a positive integer.")
    if seed is not None and not isinstance(seed, int):
        raise TypeError("seed must be an int or None.")

    ideal_counts = sample_statevector_counts(circuit, shots=shots, seed=seed)
    counts: dict[str, int] = {}

    for bitstring, count in ideal_counts.items():
        for _ in range(count):
            noisy_bitstring = noise_model.apply_to_bitstring(bitstring)
            counts[noisy_bitstring] = counts.get(noisy_bitstring, 0) + 1

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
    ideal_circuit = build_single_qubit_superposition_circuit()

    ideal_counts = sample_statevector_counts(ideal_circuit, shots=shots, seed=123)
    ideal_probs = normalize_counts(ideal_counts)

    noise_model = MeasurementNoiseModel(flip_probability=0.2, seed=456)
    noisy_counts = sample_noisy_statevector_counts(
        ideal_circuit,
        noise_model,
        shots,
        seed=123,
    )
    noisy_probs = normalize_counts(noisy_counts)

    confusion_matrix = confusion_matrix_from_model(noise_model)
    mitigated_probs = mitigate_single_qubit_counts(noisy_counts, confusion_matrix)

    error_noisy = abs(noisy_probs.get("0", 0.0) - ideal_probs.get("0", 0.0))
    error_mitigated = abs(
        mitigated_probs.get("0", 0.0) - ideal_probs.get("0", 0.0)
    )

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
