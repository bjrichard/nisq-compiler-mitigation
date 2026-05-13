from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ExperimentConfig:
    """
    Configuration for experiment execution.

    Input(s)
    --------
    - shots : int
        Number of measurement samples.
    - flip_probability : float
        Readout bit-flip probability.
    - seed : int
        Random seed for reproducibility.

    Output(s)
    ---------
    - return_value : None
        Immutable experiment configuration object.
    """

    shots: int
    flip_probability: float
    seed: int


DEFAULT_CONFIG = ExperimentConfig(
    shots=5000,
    flip_probability=0.2,
    seed=123,
)


NOISE_SWEEP_LEVELS = [
    0.0,
    0.05,
    0.1,
    0.15,
    0.2,
    0.25,
    0.3,
    0.35,
    0.4,
]
