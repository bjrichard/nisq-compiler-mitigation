from experiments.paths import (
    CIRCUIT_COMPARISON_PLOT_PATH,
    CIRCUIT_COMPARISON_RESULTS_PATH,
    EXPERIMENTS_DIR,
    NOISE_SWEEP_PLOT_PATH,
    NOISE_SWEEP_RESULTS_PATH,
    PROJECT_ROOT,
    RESULTS_DIR,
)


def test_project_root_points_to_repo_root() -> None:
    """PROJECT_ROOT points to the repository root."""
    assert (PROJECT_ROOT / "experiments").exists()
    assert (PROJECT_ROOT / "src").exists()


def test_experiments_and_results_dirs_are_nested_correctly() -> None:
    """Experiment directories are derived from PROJECT_ROOT."""
    assert EXPERIMENTS_DIR == PROJECT_ROOT / "experiments"
    assert RESULTS_DIR == EXPERIMENTS_DIR / "results"


def test_result_paths_have_expected_filenames() -> None:
    """Result path constants use expected filenames."""
    assert NOISE_SWEEP_RESULTS_PATH.name == "noise_sweep_results.csv"
    assert NOISE_SWEEP_PLOT_PATH.name == "noise_sweep_plot.png"
    assert CIRCUIT_COMPARISON_RESULTS_PATH.name == "circuit_comparison_results.csv"
    assert CIRCUIT_COMPARISON_PLOT_PATH.name == "circuit_comparison_plot.png"
