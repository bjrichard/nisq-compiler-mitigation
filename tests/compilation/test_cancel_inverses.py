from qc_compiler.circuits import Circuit, Gate, Qubit
from qc_compiler.compilation.passes import CancelAdjacentInversesPass


def test_x_followed_by_x_cancels() -> None:
    """Adjacent X gates on same target cancel."""
    q0 = Qubit(0)
    circuit = Circuit()
    circuit.add_gate(Gate(name="X", targets=[q0]))
    circuit.add_gate(Gate(name="X", targets=[q0]))

    out = CancelAdjacentInversesPass().run(circuit)
    assert out.gates == []


def test_z_followed_by_z_cancels() -> None:
    """Adjacent Z gates on same target cancel."""
    q0 = Qubit(0)
    circuit = Circuit()
    circuit.add_gate(Gate(name="Z", targets=[q0]))
    circuit.add_gate(Gate(name="Z", targets=[q0]))

    out = CancelAdjacentInversesPass().run(circuit)
    assert out.gates == []


def test_different_targets_do_not_cancel() -> None:
    """Gates with different targets do not cancel."""
    q0 = Qubit(0)
    q1 = Qubit(1)
    circuit = Circuit()
    circuit.add_gate(Gate(name="X", targets=[q0]))
    circuit.add_gate(Gate(name="X", targets=[q1]))

    out = CancelAdjacentInversesPass().run(circuit)
    assert len(out.gates) == 2


def test_mixed_gate_names_do_not_cancel() -> None:
    """Different gate names do not cancel."""
    q0 = Qubit(0)
    circuit = Circuit()
    circuit.add_gate(Gate(name="X", targets=[q0]))
    circuit.add_gate(Gate(name="Z", targets=[q0]))

    out = CancelAdjacentInversesPass().run(circuit)
    assert len(out.gates) == 2


def test_parametrized_gates_do_not_cancel() -> None:
    """Gates with parameters do not cancel."""
    q0 = Qubit(0)
    circuit = Circuit()
    circuit.add_gate(Gate(name="X", targets=[q0], params={"theta": 0.1}))
    circuit.add_gate(Gate(name="X", targets=[q0], params={"theta": 0.1}))

    out = CancelAdjacentInversesPass().run(circuit)
    assert len(out.gates) == 2
