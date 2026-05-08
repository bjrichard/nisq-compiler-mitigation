import pytest

from experiments.scripts.compare_circuit_types import (
    absolute_error_p0,
    run_measurement_only_case,
    run_superposition_case,
)


def test_absolute_error_p0() -> None:
    """absolute_error_p0 computes absolute error for P(0)."""
    observed = {"0": 0.8, "1": 0.2}
    ideal = {"0": 1.0, "1": 0.0}

    assert absolute_error_p0(observed, ideal) == pytest.approx(0.2)


def test_run_measurement_only_case_returns_errors() -> None:
    """Measurement-only case returns noisy and mitigated errors."""
    result = run_measurement_only_case(flip_probability=0.2, shots=100)

    assert "noisy_error" in result
    assert "mitigated_error" in result


def test_run_superposition_case_returns_errors() -> None:
    """Superposition case returns noisy and mitigated errors."""
    result = run_superposition_case(flip_probability=0.2, shots=100)

    assert "noisy_error" in result
    assert "mitigated_error" in result
