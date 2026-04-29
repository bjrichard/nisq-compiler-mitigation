from pathlib import Path

from experiments.scripts.plot_noise_sweep import load_results


def test_load_results_reads_csv(tmp_path: Path) -> None:
    path = tmp_path / "data.csv"
    path.write_text(
        "flip_probability,noisy_error,mitigated_error\n"
        "0.1,0.1,0.02\n"
    )

    flip, noisy, mitigated = load_results(path)

    assert flip == [0.1]
    assert noisy == [0.1]
    assert mitigated == [0.02]
