import pytest

from experiments.scripts.run_readout_mitigation_demo import (
    build_single_qubit_measurement_circuit,
    normalize_counts,
    sample_noisy_bitstring,
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


def test_sample_noisy_bitstring_without_noise_returns_zero() -> None:
    """Ideal single-shot sampling returns the expected bitstring."""
    circuit = build_single_qubit_measurement_circuit()
    bitstring = sample_noisy_bitstring(circuit)
    assert bitstring == "0"


def test_sample_noisy_counts_without_noise_is_deterministic() -> None:
    """Ideal multi-shot sampling yields only the zero bitstring."""
    circuit = build_single_qubit_measurement_circuit()
    counts = sample_noisy_counts(circuit, None, shots=20)
    assert counts == {"0": 20}


def test_sample_noisy_counts_returns_valid_total() -> None:
    """sample_noisy_counts returns counts summing to the requested number of shots."""
    circuit = build_single_qubit_measurement_circuit()
    noise_model = MeasurementNoiseModel(flip_probability=0.2, seed=123)

    counts = sample_noisy_counts(circuit, noise_model, shots=100)

    assert sum(counts.values()) == 100
    assert set(counts.keys()).issubset({"0", "1"})


def test_sample_noisy_counts_sums_to_shots_with_noise() -> None:
    """Noisy multi-shot sampling returns counts summing to the requested shots."""
    circuit = build_single_qubit_measurement_circuit()
    noise_model = MeasurementNoiseModel(flip_probability=0.2, seed=123)
    counts = sample_noisy_counts(circuit, noise_model, shots=100)
    assert sum(counts.values()) == 100
    assert set(counts.keys()).issubset({"0", "1"})


def test_sample_noisy_counts_rejects_invalid_shots() -> None:
    """sample_noisy_counts rejects invalid shot counts."""
    circuit = build_single_qubit_measurement_circuit()

    with pytest.raises(ValueError):
        sample_noisy_counts(circuit, None, shots=0)

    with pytest.raises(ValueError):
        sample_noisy_counts(circuit, None, shots=-5)
