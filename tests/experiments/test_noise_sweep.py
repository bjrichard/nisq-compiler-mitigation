import pytest

from experiments.scripts.run_noise_sweep import run_experiment


def test_run_experiment_returns_two_floats() -> None:
    """run_experiment returns noisy and mitigated errors as floats."""
    noisy_error, mitigated_error = run_experiment(0.1, shots=100)

    assert isinstance(noisy_error, float)
    assert isinstance(mitigated_error, float)


def test_run_experiment_returns_non_negative_errors() -> None:
    """run_experiment returns non-negative error values."""
    noisy_error, mitigated_error = run_experiment(0.1, shots=100)

    assert noisy_error >= 0.0
    assert mitigated_error >= 0.0


def test_run_experiment_rejects_invalid_flip_probability() -> None:
    """run_experiment rejects flip probabilities outside [0, 1]."""
    with pytest.raises(ValueError):
        run_experiment(-0.1, shots=100)

    with pytest.raises(ValueError):
        run_experiment(1.1, shots=100)


def test_run_experiment_rejects_invalid_shots() -> None:
    """run_experiment rejects non-positive shot counts."""
    with pytest.raises(ValueError):
        run_experiment(0.1, shots=0)

    with pytest.raises(ValueError):
        run_experiment(0.1, shots=-10)


def test_run_experiment_rejects_non_integer_shots() -> None:
    """run_experiment rejects non-integer shot counts."""
    with pytest.raises(TypeError):
        run_experiment(0.1, shots=100.5)  # type: ignore[arg-type]
