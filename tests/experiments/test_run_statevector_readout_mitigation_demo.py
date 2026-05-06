from experiments.scripts.run_statevector_readout_mitigation_demo import (
    build_single_qubit_superposition_circuit,
    normalize_counts,
    sample_noisy_statevector_counts,
)
from qc_compiler.circuits import Circuit
from qc_compiler.noise import MeasurementNoiseModel


def test_build_single_qubit_superposition_circuit_returns_circuit() -> None:
    """The superposition circuit builder returns a Circuit."""
    circuit = build_single_qubit_superposition_circuit()

    assert isinstance(circuit, Circuit)
    assert [gate.name for gate in circuit.gates] == ["H", "MEASURE"]


def test_normalize_counts_returns_probabilities() -> None:
    """normalize_counts converts counts to a probability distribution."""
    counts = {"0": 80, "1": 20}
    probs = normalize_counts(counts)

    assert probs == {"0": 0.8, "1": 0.2}


def test_sample_noisy_statevector_counts_preserves_total_shots() -> None:
    """sample_noisy_statevector_counts returns counts summing to shots."""
    circuit = build_single_qubit_superposition_circuit()
    noise_model = MeasurementNoiseModel(flip_probability=0.2, seed=123)

    counts = sample_noisy_statevector_counts(
        circuit,
        noise_model,
        shots=100,
        seed=456,
    )

    assert sum(counts.values()) == 100
    assert set(counts.keys()).issubset({"0", "1"})
