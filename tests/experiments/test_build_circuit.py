from qc_compiler.circuits import Circuit

from experiments.scripts.build_simple_circuit import build_simple_circuit


def test_build_simple_circuit_returns_circuit() -> None:
    """build_simple_circuit returns a Circuit with expected basic properties."""
    circuit = build_simple_circuit()
    assert isinstance(circuit, Circuit)
    assert len(circuit.gates) == 3
    assert circuit.num_qubits() == 3
    assert circuit.num_qubits_used() == 3
