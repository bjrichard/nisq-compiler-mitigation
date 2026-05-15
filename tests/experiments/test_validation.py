import pytest

from experiments.validation import validate_positive_int


def test_validate_positive_int_accepts_valid_value() -> None:
    """validate_positive_int accepts positive integers."""
    validate_positive_int(5, "shots")


def test_validate_positive_int_rejects_non_integer() -> None:
    """validate_positive_int rejects non-integer values."""
    with pytest.raises(TypeError):
        validate_positive_int(1.5, "shots")


def test_validate_positive_int_rejects_non_positive_value() -> None:
    """validate_positive_int rejects non-positive integers."""
    with pytest.raises(ValueError):
        validate_positive_int(0, "shots")


def test_validate_positive_int_rejects_empty_name() -> None:
    """validate_positive_int rejects empty parameter names."""
    with pytest.raises(ValueError):
        validate_positive_int(5, "")
