import pytest

from qc_compiler.compilation import PassManager, BaseCompilerPass
#from qc_compiler.compilation.pass_base import BaseCompilerPass
from qc_compiler.circuits import Circuit, Gate, Qubit


class _AppendXPass(BaseCompilerPass):
    """Test-only pass that appends an X gate on a specific qubit."""

    def __init__(self, qubit_index: int) -> None:
        super().__init__(name=f"append_x_{qubit_index}")
        self._qubit_index = qubit_index

    def run(self, circuit: Circuit) -> Circuit:
        q = Qubit(self._qubit_index)
        out = Circuit()
        for g in circuit.gates:
            out.add_gate(g)
        out.add_gate(Gate(name="X", targets=[q]))
        return out


def test_pass_manager_runs_passes_in_order() -> None:
    """PassManager applies passes sequentially in the given order."""
    pm = PassManager(passes=[_AppendXPass(0), _AppendXPass(1)])
    result = pm.run(Circuit())
    assert [g.targets[0].index for g in result.gates] == [0, 1]


def test_pass_manager_rejects_non_pass_entries() -> None:
    """PassManager rejects non-CompilerPass entries."""
    with pytest.raises(TypeError):
        _ = PassManager(passes=[_AppendXPass(0), "not-a-pass"])  # type: ignore[list-item]


def test_pass_manager_rejects_non_circuit_input() -> None:
    """PassManager.run rejects non-Circuit inputs."""
    pm = PassManager(passes=[_AppendXPass(0)])
    with pytest.raises(TypeError):
        _ = pm.run("not-a-circuit")  # type: ignore[arg-type]
