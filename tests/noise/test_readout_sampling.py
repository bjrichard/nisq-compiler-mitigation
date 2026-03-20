import pytest

from qc_compiler.circuits import Circuit, Gate, Qubit
from qc_compiler.noise import bitstring_from_readout, sample_readout


def test_sample_readout_returns_empty_for_no_measurements() -> None:
    """sample_readout returns an empty mapping when no measurements exist."""
    circuit = Circuit()
    assert sample_readout(circuit) == {}


def test_sample_readout_records_measured_qubits_as_zero_by_default() -> None:
    """Measured qubits default to zero when no readout flips occur."""
    q0 = Qubit(0)
    circuit = Circuit()
    circuit.add_gate(Gate(name="MEASURE", targets=[q0]))

    assert sample_readout(circuit) == {0: 0}


def test_sample_readout_applies_readout_flip_before_measurement() -> None:
    """READOUT_FLIP changes the sampled classical bit value."""
    q0 = Qubit(0)
    circuit = Circuit()
    circuit.add_gate(Gate(name="READOUT_FLIP", targets=[q0]))
    circuit.add_gate(Gate(name="MEASURE", targets=[q0]))

    assert sample_readout(circuit) == {0: 1}


def test_sample_readout_handles_multiple_flips() -> None:
    """Two readout flips on the same qubit cancel out."""
    q0 = Qubit(0)
    circuit = Circuit()
    circuit.add_gate(Gate(name="READOUT_FLIP", targets=[q0]))
    circuit.add_gate(Gate(name="READOUT_FLIP", targets=[q0]))
    circuit.add_gate(Gate(name="MEASURE", targets=[q0]))

    assert sample_readout(circuit) == {0: 0}


def test_bitstring_from_readout_orders_by_qubit_index() -> None:
    """bitstring_from_readout orders bits by ascending qubit index."""
    readout = {2: 1, 0: 0, 1: 1}
    assert bitstring_from_readout(readout) == "011"


def test_bitstring_from_readout_rejects_invalid_values() -> None:
    """bitstring_from_readout rejects non-binary bit values."""
    with pytest.raises(ValueError):
        _ = bitstring_from_readout({0: 2})


def test_sample_readout_ignores_unmeasured_flipped_qubits() -> None:
    """Unmeasured qubits do not appear in the returned readout mapping."""
    q0 = Qubit(0)
    circuit = Circuit()
    circuit.add_gate(Gate(name="READOUT_FLIP", targets=[q0]))

    assert sample_readout(circuit) == {}


def test_bitstring_from_readout_rejects_non_integer_keys() -> None:
    """bitstring_from_readout rejects non-integer keys."""
    with pytest.raises(TypeError):
        _ = bitstring_from_readout({"0": 1})  # type: ignore[dict-item]
