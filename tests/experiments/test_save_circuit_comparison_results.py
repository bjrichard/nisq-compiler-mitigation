import csv
from pathlib import Path

from experiments.scripts.save_circuit_comparison_results import (
    save_results,
)


def test_save_results_writes_csv(tmp_path: Path) -> None:
    """save_results writes comparison rows to CSV."""
    output_path = tmp_path / "results.csv"

    rows = [
        {
            "circuit_type": "measurement_only",
            "flip_probability": 0.2,
            "noisy_error": 0.2,
            "mitigated_error": 0.01,
        }
    ]

    save_results(rows, output_path)

    with output_path.open("r") as csvfile:
        reader = csv.DictReader(csvfile)
        loaded_rows = list(reader)

    assert len(loaded_rows) == 1
    assert loaded_rows[0]["circuit_type"] == "measurement_only"
