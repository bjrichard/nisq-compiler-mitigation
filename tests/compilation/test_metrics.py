import pytest

from qc_compiler.circuits import Circuit, Gate, Qubit
from qc_compiler.compilation import (
    gate_count,
    gate_counts_by_name,
    two_qubit_gate_count,
)


def test_gate_count_empty_circuit() -> None:
    """gate_count returns zero for an empty circuit."""
    circuit = Circuit()
    assert gate_count(circuit) == 0


def test_gate_count_counts_all_gates() -> None:
    """gate_count returns the total number of gates."""
    q0 = Qubit(0)
    q1 = Qubit(1)
    circuit = Circuit()
    circuit.add_gate(Gate(name="X", targets=[q0]))
    circuit.add_gate(Gate(name="Z", targets=[q1]))
    circuit.add_gate(Gate(name="CX", targets=[q0, q1]))
    assert gate_count(circuit) == 3


def test_gate_counts_by_name_groups_correctly() -> None:
    """gate_counts_by_name groups gates by name."""
    q0 = Qubit(0)
    q1 = Qubit(1)
    circuit = Circuit()
    circuit.add_gate(Gate(name="X", targets=[q0]))
    circuit.add_gate(Gate(name="X", targets=[q1]))
    circuit.add_gate(Gate(name="CX", targets=[q0, q1]))

    counts = gate_counts_by_name(circuit)
    assert counts == {"X": 2, "CX": 1}


def test_two_qubit_gate_count_counts_only_two_qubit_gates() -> None:
    """two_qubit_gate_count counts only gates with exactly two targets."""
    q0 = Qubit(0)
    q1 = Qubit(1)
    circuit = Circuit()
    circuit.add_gate(Gate(name="X", targets=[q0]))
    circuit.add_gate(Gate(name="CX", targets=[q0, q1]))
    circuit.add_gate(Gate(name="CZ", targets=[q0, q1]))
    assert two_qubit_gate_count(circuit) == 2


def test_metrics_reject_non_circuit_inputs() -> None:
    """Metric functions reject non-Circuit inputs."""
    with pytest.raises(TypeError):
        _ = gate_count("not-a-circuit")  # type: ignore[arg-type]

    with pytest.raises(TypeError):
        _ = gate_counts_by_name("not-a-circuit")  # type: ignore[arg-type]

    with pytest.raises(TypeError):
        _ = two_qubit_gate_count("not-a-circuit")  # type: ignore[arg-type]
