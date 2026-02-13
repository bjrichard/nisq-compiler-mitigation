import pytest
from qc_compiler.circuits import Gate, Qubit


def test_gate_constructs() -> None:
    """
    Construct a valid gate with default parameters.

    Input(s)
    ----------
    - parameter : None
        No inputs.

    Output(s)
    -------
    - return_value : None
        Asserts that Gate initializes and exposes expected default state.
    """
    q0 = Qubit(0)
    g = Gate(name="X", targets=[q0])
    assert g.name == "X"
    assert [q.index for q in g.targets] == [0]
    assert g.params == {}


def test_gate_rejects_empty_name() -> None:
    """
    Reject construction when gate name is empty.

    Input(s)
    ----------
    - parameter : None
        No inputs.

    Output(s)
    -------
    - return_value : None
        Asserts that a ValueError is raised for an empty name.
    """
    q0 = Qubit(0)
    with pytest.raises(ValueError):
        _ = Gate(name="", targets=[q0])


def test_gate_rejects_empty_targets() -> None:
    """
    Reject construction when no target qubits are provided.

    Input(s)
    ----------
    - parameter : None
        No inputs.

    Output(s)
    -------
    - return_value : None
        Asserts that a ValueError is raised for an empty target list.
    """
    with pytest.raises(ValueError):
        _ = Gate(name="X", targets=[])


def test_gate_rejects_duplicate_targets() -> None:
    """
    Reject construction when the target list contains duplicate qubits.

    Input(s)
    ----------
    - parameter : None
        No inputs.

    Output(s)
    -------
    - return_value : None
        Asserts that a ValueError is raised for duplicate targets.
    """
    q0 = Qubit(0)
    with pytest.raises(ValueError):
        _ = Gate(name="CX", targets=[q0, q0])


def test_gate_rejects_non_qubit_target() -> None:
    """
    Reject construction when a non-Qubit object appears in targets.

    Input(s)
    ----------
    - parameter : None
        No inputs.

    Output(s)
    -------
    - return_value : None
        Asserts that a TypeError is raised for invalid target types.
    """
    q0 = Qubit(0)
    with pytest.raises(TypeError):
        _ = Gate(name="X", targets=[q0, "nope"])  # type: ignore[list-item]
