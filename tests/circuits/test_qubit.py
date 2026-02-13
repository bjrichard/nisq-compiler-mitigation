import pytest

from qc_compiler.circuits import Qubit

def test_qubit_equality_same_index() -> None:
    """
    Test equality of two Qubit instances with the same index.

    Input(s)
    ----------
    - parameter : None
        No external inputs. Creates two Qubit instances internally.

    Output(s)
    -------
    - return_value : None
        Asserts that two Qubit objects with identical indices compare equal.
    """
    q1 = Qubit(0)
    q2 = Qubit(0)
    assert q1 == q2

def test_qubit_inequality_different_index() -> None:
    """
    Test inequality of two Qubit instances with different indices.

    Input(s)
    ----------
    - parameter : None
        No external inputs. Creates two Qubit instances internally.

    Output(s)
    -------
    - return_value : None
        Asserts that Qubit objects with different indices compare unequal.
    """
    q1 = Qubit(0)
    q2 = Qubit(1)
    assert q1 != q2

def test_qubit_not_equal_to_non_qubit() -> None:
    """
    Test that a Qubit instance does not compare equal to a non-Qubit object.

    Input(s)
    ----------
    - parameter : None
        No external inputs. Creates one Qubit instance internally.

    Output(s)
    -------
    - return_value : None
        Asserts that comparison with a non-Qubit object returns False.
    """
    q = Qubit(0)
    assert q != 0
