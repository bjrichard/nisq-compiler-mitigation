import pytest

from qc_compiler.circuits import Circuit, Gate, Qubit


def test_empty_circuit_has_zero_qubits() -> None:
    """Empty circuit reports zero qubits and no gates."""
    circuit = Circuit()
    assert circuit.num_qubits() == 0
    assert circuit.num_qubits_used() == 0
    assert circuit.gates == []


def test_add_gate_preserves_order() -> None:
    """Gates are stored in insertion order."""
    circuit = Circuit()
    q0 = Qubit(0)
    q1 = Qubit(1)
    g1 = Gate(name="X", targets=[q0])
    g2 = Gate(name="Z", targets=[q1])

    circuit.add_gate(g1)
    circuit.add_gate(g2)

    gates = circuit.gates
    assert gates[0].name == "X"
    assert gates[1].name == "Z"


def test_num_qubits_is_max_index_plus_one() -> None:
    """num_qubits returns max qubit index + 1."""
    circuit = Circuit()
    q0 = Qubit(0)
    q2 = Qubit(2)

    circuit.add_gate(Gate(name="X", targets=[q2]))
    circuit.add_gate(Gate(name="Z", targets=[q0]))

    assert circuit.num_qubits() == 3
    assert circuit.num_qubits_used() == 2


def test_add_gate_rejects_non_gate() -> None:
    """Adding non-Gate objects raises TypeError."""
    circuit = Circuit()
    with pytest.raises(TypeError):
        circuit.add_gate("not-a-gate")  # type: ignore[arg-type]
