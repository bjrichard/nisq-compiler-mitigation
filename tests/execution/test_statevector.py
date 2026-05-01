import pytest

from qc_compiler.circuits import Circuit, Gate, Qubit
from qc_compiler.execution import (
    sample_statevector_counts,
    simulate_single_qubit_statevector,
)


def test_empty_single_qubit_statevector_defaults_to_zero_state() -> None:
    """Empty circuit simulates to the |0> state."""
    circuit = Circuit()
    state = simulate_single_qubit_statevector(circuit)

    assert state == [1.0 + 0.0j, 0.0 + 0.0j]


def test_x_gate_maps_zero_to_one() -> None:
    """X maps |0> to |1>."""
    q0 = Qubit(0)
    circuit = Circuit()
    circuit.add_gate(Gate(name="X", targets=[q0]))

    state = simulate_single_qubit_statevector(circuit)

    assert state == [0.0 + 0.0j, 1.0 + 0.0j]


def test_h_gate_creates_equal_superposition() -> None:
    """H maps |0> to an equal superposition."""
    q0 = Qubit(0)
    circuit = Circuit()
    circuit.add_gate(Gate(name="H", targets=[q0]))

    state = simulate_single_qubit_statevector(circuit)

    assert abs(abs(state[0]) ** 2 - 0.5) < 1.0e-9
    assert abs(abs(state[1]) ** 2 - 0.5) < 1.0e-9


def test_h_h_returns_to_zero_state() -> None:
    """Applying H twice returns |0>."""
    q0 = Qubit(0)
    circuit = Circuit()
    circuit.add_gate(Gate(name="H", targets=[q0]))
    circuit.add_gate(Gate(name="H", targets=[q0]))

    state = simulate_single_qubit_statevector(circuit)

    assert abs(abs(state[0]) ** 2 - 1.0) < 1.0e-9
    assert abs(abs(state[1]) ** 2 - 0.0) < 1.0e-9


def test_sample_statevector_counts_for_h_produces_both_outcomes() -> None:
    """Sampling H|0> produces both 0 and 1 over many shots."""
    q0 = Qubit(0)
    circuit = Circuit()
    circuit.add_gate(Gate(name="H", targets=[q0]))
    circuit.add_gate(Gate(name="MEASURE", targets=[q0]))

    counts = sample_statevector_counts(circuit, shots=200, seed=123)

    assert sum(counts.values()) == 200
    assert set(counts.keys()) == {"0", "1"}


def test_statevector_rejects_multi_qubit_circuit() -> None:
    """Statevector simulator rejects circuits with more than one qubit."""
    q1 = Qubit(1)
    circuit = Circuit()
    circuit.add_gate(Gate(name="X", targets=[q1]))

    with pytest.raises(ValueError):
        simulate_single_qubit_statevector(circuit)
