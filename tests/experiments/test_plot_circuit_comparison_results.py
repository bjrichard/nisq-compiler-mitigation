from pathlib import Path

from experiments.scripts.plot_circuit_comparison_results import (
    extract_series,
    load_results,
)


def test_load_results_reads_csv(tmp_path: Path) -> None:
    """load_results reads CSV rows."""
    path = tmp_path / "results.csv"

    path.write_text(
        "circuit_type,flip_probability,noisy_error,mitigated_error\n"
        "measurement_only,0.2,0.2,0.01\n"
    )

    rows = load_results(path)

    assert len(rows) == 1
    assert rows[0]["circuit_type"] == "measurement_only"


def test_extract_series_returns_matching_rows() -> None:
    """extract_series filters rows by circuit type."""
    rows = [
        {
            "circuit_type": "measurement_only",
            "flip_probability": "0.2",
            "noisy_error": "0.2",
            "mitigated_error": "0.01",
        },
        {
            "circuit_type": "superposition",
            "flip_probability": "0.2",
            "noisy_error": "0.1",
            "mitigated_error": "0.02",
        },
    ]

    flip_probs, noisy_errors, mitigated_errors = extract_series(
        rows,
        "superposition",
    )

    assert flip_probs == [0.2]
    assert noisy_errors == [0.1]
    assert mitigated_errors == [0.02]
