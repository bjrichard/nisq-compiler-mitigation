from dataclasses import FrozenInstanceError

import pytest

from experiments.config import (
    DEFAULT_CONFIG,
    ExperimentConfig,
    NOISE_SWEEP_LEVELS,
)


def test_default_config_has_expected_values() -> None:
    """DEFAULT_CONFIG exposes expected default experiment values."""
    assert DEFAULT_CONFIG.shots == 5000
    assert DEFAULT_CONFIG.flip_probability == 0.2
    assert DEFAULT_CONFIG.seed == 123


def test_noise_sweep_levels_are_sorted() -> None:
    """NOISE_SWEEP_LEVELS is monotonically increasing."""
    assert NOISE_SWEEP_LEVELS == sorted(NOISE_SWEEP_LEVELS)


def test_experiment_config_is_frozen() -> None:
    """ExperimentConfig is immutable."""
    config = ExperimentConfig(
        shots=1000,
        flip_probability=0.1,
        seed=1,
    )

    with pytest.raises(FrozenInstanceError):
        config.shots = 2000
