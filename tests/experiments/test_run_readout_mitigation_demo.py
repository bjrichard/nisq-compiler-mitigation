from experiments.scripts.run_readout_mitigation_demo import (
    build_single_qubit_measurement_circuit,
    normalize_counts,
    sample_noisy_counts,
)
from qc_compiler.circuits import Circuit
from qc_compiler.noise import MeasurementNoiseModel


def test_build_single_qubit_measurement_circuit_returns_circuit() -> None:
    """The demo circuit builder returns a Circuit."""
    circuit = build_single_qubit_measurement_circuit()
    assert isinstance(circuit, Circuit)
    assert len(circuit.gates) == 1
    assert circuit.gates[0].name == "MEASURE"


def test_normalize_counts_returns_probabilities() -> None:
    """normalize_counts converts counts to a probability distribution."""
    counts = {"0": 80, "1": 20}
    probs = normalize_counts(counts)

    assert probs == {"0": 0.8, "1": 0.2}


def test_sample_noisy_counts_returns_valid_total() -> None:
    """sample_noisy_counts returns counts summing to the requested number of shots."""
    circuit = build_single_qubit_measurement_circuit()
    noise_model = MeasurementNoiseModel(flip_probability=0.2, seed=123)

    counts = sample_noisy_counts(circuit, noise_model, shots=100)

    assert sum(counts.values()) == 100
    assert set(counts.keys()).issubset({"0", "1"})
