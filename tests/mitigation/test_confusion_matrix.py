import pytest

from qc_compiler.mitigation import (
    confusion_matrix_from_model,
    is_valid_confusion_matrix,
    single_qubit_confusion_matrix,
)
from qc_compiler.noise import MeasurementNoiseModel


def test_confusion_matrix_identity_when_no_noise() -> None:
    """Zero flip probability yields the identity confusion matrix."""
    cm = single_qubit_confusion_matrix(0.0)
    assert cm == [[1.0, 0.0], [0.0, 1.0]]


def test_confusion_matrix_symmetric_for_half_probability() -> None:
    """Flip probability 0.5 yields a uniform confusion matrix."""
    cm = single_qubit_confusion_matrix(0.5)
    assert cm == [[0.5, 0.5], [0.5, 0.5]]


def test_confusion_matrix_rejects_invalid_probability() -> None:
    """Invalid flip probabilities raise errors."""
    with pytest.raises(ValueError):
        single_qubit_confusion_matrix(-0.1)

    with pytest.raises(ValueError):
        single_qubit_confusion_matrix(1.1)


def test_confusion_matrix_from_model_matches_probability() -> None:
    """Model-derived confusion matrix matches the underlying flip probability."""
    model = MeasurementNoiseModel(flip_probability=0.2, seed=123)
    cm = confusion_matrix_from_model(model)

    assert cm == [[0.8, 0.2], [0.2, 0.8]]


def test_is_valid_confusion_matrix_accepts_valid_matrix() -> None:
    """Valid two-by-two probability matrices are accepted."""
    matrix = [[0.8, 0.2], [0.2, 0.8]]
    assert is_valid_confusion_matrix(matrix) is True


def test_is_valid_confusion_matrix_rejects_invalid_shape() -> None:
    """Matrices with invalid shape are rejected."""
    assert is_valid_confusion_matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]) is False
    assert is_valid_confusion_matrix([[1.0, 0.0]]) is False


def test_is_valid_confusion_matrix_rejects_invalid_probabilities() -> None:
    """Matrices with entries outside [0, 1] are rejected."""
    assert is_valid_confusion_matrix([[1.2, -0.2], [0.2, 0.8]]) is False


def test_is_valid_confusion_matrix_rejects_rows_not_summing_to_one() -> None:
    """Matrices whose rows do not sum to one are rejected."""
    assert is_valid_confusion_matrix([[0.7, 0.4], [0.2, 0.8]]) is False


def test_confusion_matrix_from_model_rejects_wrong_type() -> None:
    """confusion_matrix_from_model rejects non-MeasurementNoiseModel inputs."""
    with pytest.raises(TypeError):
        confusion_matrix_from_model("not-a-noise-model")  # type: ignore[arg-type]


def test_confusion_matrix_rejects_non_numeric_input() -> None:
    """Non-numeric flip probabilities raise TypeError."""
    with pytest.raises(TypeError):
        single_qubit_confusion_matrix("bad")  # type: ignore[arg-type]
