from __future__ import annotations

from qc_compiler.circuits import Circuit, Gate, Qubit
from qc_compiler.noise.readout_sampling import sample_readout, bitstring_from_readout
from qc_compiler.noise import NoiseModel, MeasurementNoiseModel
from qc_compiler.mitigation import (
                                    confusion_matrix_from_model,
                                    mitigate_single_qubit_counts,
                                   )


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
        raise TypeError(
            "counts must be a dictionary with bitstrings as keys and integer counts as values."
        )

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

def sample_noisy_bitstring(
                           circuit: Circuit,
                           noise_model: NoiseModel | None = None,
                          ) -> str:
    """
    Sample a single bitstring outcome from an ideal or noisy circuit.

    Input(s)
    --------
    - circuit : Circuit
        Ideal circuit to sample.
    - noise_model : NoiseModel | None
        Optional noise model applied independently to this shot.

    Output(s)
    ---------
    - return_value : str
        Bitstring sampled from the circuit after optional noise application.
    """
    if not isinstance(circuit, Circuit):
        raise TypeError("circuit must be a Circuit instance.")

    if noise_model is not None:
        sampled_circuit = noise_model.apply(circuit)
    else:
        sampled_circuit = circuit

    readout = sample_readout(sampled_circuit)
    return bitstring_from_readout(readout)

def sample_noisy_counts(
    circuit: Circuit,
    noise_model: NoiseModel | None = None,
    shots: int = 1,
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
    if noise_model is not None and not hasattr(noise_model, "apply"):
        raise TypeError("noise_model must define an apply(circuit) method or be None.")
    if not isinstance(shots, int) or shots <= 0:
        raise ValueError("shots must be a positive integer.")

    counts: dict[str, int] = {}

    for _ in range(shots):
        bitstring = sample_noisy_bitstring(circuit, noise_model)
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
    ideal_counts = sample_noisy_counts(ideal_circuit, None, shots)
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
