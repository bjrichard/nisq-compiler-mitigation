import pytest

from qc_compiler.circuits import Circuit, Gate, Qubit
from qc_compiler.execution import sample_counts


def test_sample_counts_returns_dict() -> None:
    """sample_counts returns a dictionary of counts."""
    q0 = Qubit(0)
    circuit = Circuit()
    circuit.add_gate(Gate(name="MEASURE", targets=[q0]))

    counts = sample_counts(circuit, shots=10)

    assert isinstance(counts, dict)
    assert sum(counts.values()) == 10


def test_sample_counts_single_outcome_without_noise() -> None:
    """Without noise, repeated sampling yields deterministic results."""
    q0 = Qubit(0)
    circuit = Circuit()
    circuit.add_gate(Gate(name="MEASURE", targets=[q0]))

    counts = sample_counts(circuit, shots=20)

    assert counts == {"0": 20}


def test_sample_counts_with_readout_flip() -> None:
    """READOUT_FLIP affects sampled outcomes."""
    q0 = Qubit(0)
    circuit = Circuit()
    circuit.add_gate(Gate(name="READOUT_FLIP", targets=[q0]))
    circuit.add_gate(Gate(name="MEASURE", targets=[q0]))

    counts = sample_counts(circuit, shots=10)

    assert counts == {"1": 10}


def test_sample_counts_rejects_invalid_shots() -> None:
    """Invalid shot counts raise errors."""
    q0 = Qubit(0)
    circuit = Circuit()
    circuit.add_gate(Gate(name="MEASURE", targets=[q0]))

    with pytest.raises(ValueError):
        sample_counts(circuit, shots=0)

    with pytest.raises(ValueError):
        sample_counts(circuit, shots=-5)
