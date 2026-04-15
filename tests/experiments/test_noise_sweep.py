from experiments.scripts.run_noise_sweep import run_experiment


def test_run_experiment_returns_tuple() -> None:
    noisy, mitigated = run_experiment(0.1, shots=100)
    assert isinstance(noisy, float)
    assert isinstance(mitigated, float)
