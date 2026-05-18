from __future__ import annotations

import csv
from pathlib import Path

from experiments.config import DEFAULT_CONFIG
from experiments.summary import format_error_table
from experiments.validation import validate_positive_int
from qc_compiler.circuits import Circuit, Gate, Qubit
from qc_compiler.compilation import PassManager
from qc_compiler.compilation.passes import CancelAdjacentInversesPass
from qc_compiler.execution import sample_statevector_counts
from qc_compiler.mitigation import (
    confusion_matrix_from_model,
    mitigate_single_qubit_counts,
)
from qc_compiler.noise import MeasurementNoiseModel


PROJECT_ROOT = Path(__file__).resolve().parents[2]

RESULTS_PATH = (
    PROJECT_ROOT
    / "experiments"
    / "results"
    / "compilation_comparison_results.csv"
)


def build_unoptimized_circuit() -> Circuit:
    """
    Build a circuit containing redundant adjacent inverse gates.

    Input(s)
    --------
    - parameter : None
        No inputs.

    Output(s)
    ---------
    - return_value : Circuit
        Circuit containing redundant adjacent X operations.
    """
    q0 = Qubit(0)

    circuit = Circuit()
    circuit.add_gate(Gate(name="X", targets=[q0]))
    circuit.add_gate(Gate(name="X", targets=[q0]))
    circuit.add_gate(Gate(name="H", targets=[q0]))
    circuit.add_gate(Gate(name="MEASURE", targets=[q0]))

    return circuit


def normalize_counts(counts: dict[str, int]) -> dict[str, float]:
    """
    Convert counts into probabilities.

    Input(s)
    --------
    - counts : dict[str, int]
        Mapping from bitstring to observed count.

    Output(s)
    ---------
    - return_value : dict[str, float]
        Mapping from bitstring to empirical probability.
    """
    total = sum(counts.values())
    if total <= 0:
        raise ValueError("counts must sum to a positive value.")

    return {bitstring: count / total for bitstring, count in counts.items()}


def probability_error(
    probability: float,
    ideal_probability: float,
) -> float:
    """
    Compute absolute probability error.

    Input(s)
    --------
    - probability : float
        Observed probability.
    - ideal_probability : float
        Expected ideal probability.

    Output(s)
    ---------
    - return_value : float
        Absolute error.
    """
    return abs(probability - ideal_probability)


def sample_noisy_statevector_counts(
    circuit: Circuit,
    noise_model: MeasurementNoiseModel,
    shots: int,
    seed: int | None = None,
) -> dict[str, int]:
    """
    Sample ideal statevector outcomes and apply readout noise to each bitstring.

    Input(s)
    --------
    - circuit : Circuit
        Circuit to simulate.
    - noise_model : MeasurementNoiseModel
        Measurement noise model applied to sampled bitstrings.
    - shots : int
        Number of samples.
    - seed : int | None
        Optional random seed for ideal statevector sampling.

    Output(s)
    ---------
    - return_value : dict[str, int]
        Noisy observed bitstring counts.
    """
    validate_positive_int(shots, "shots")

    ideal_counts = sample_statevector_counts(
        circuit,
        shots=shots,
        seed=seed,
    )

    noisy_counts: dict[str, int] = {}

    for bitstring, count in ideal_counts.items():
        for _ in range(count):
            noisy_bitstring = noise_model.apply_to_bitstring(bitstring)
            noisy_counts[noisy_bitstring] = (
                noisy_counts.get(noisy_bitstring, 0) + 1
            )

    return noisy_counts


def summarize_circuit_case(
    label: str,
    circuit: Circuit,
    shots: int,
    flip_probability: float,
) -> dict[str, float | str | int]:
    """
    Summarize noisy and mitigated error for one circuit.

    Input(s)
    --------
    - label : str
        Human-readable circuit label.
    - circuit : Circuit
        Circuit to evaluate.
    - shots : int
        Number of samples.
    - flip_probability : float
        Readout flip probability.

    Output(s)
    ---------
    - return_value : dict[str, float | str | int]
        Summary row for the experiment.
    """
    validate_positive_int(shots, "shots")

    ideal_counts = sample_statevector_counts(
        circuit,
        shots=shots,
        seed=DEFAULT_CONFIG.seed,
    )
    ideal_probs = normalize_counts(ideal_counts)
    ideal_p0 = ideal_probs.get("0", 0.0)

    noise_model = MeasurementNoiseModel(
        flip_probability=flip_probability,
        seed=DEFAULT_CONFIG.seed,
    )

    noisy_counts = sample_noisy_statevector_counts(
        circuit,
        noise_model,
        shots,
        seed=DEFAULT_CONFIG.seed,
    )
    noisy_probs = normalize_counts(noisy_counts)

    confusion_matrix = confusion_matrix_from_model(noise_model)
    mitigated_probs = mitigate_single_qubit_counts(
        noisy_counts,
        confusion_matrix,
    )

    noisy_error = probability_error(
        noisy_probs.get("0", 0.0),
        ideal_p0,
    )
    mitigated_error = probability_error(
        mitigated_probs.get("0", 0.0),
        ideal_p0,
    )

    return {
        "circuit_type": label,
        "gate_count": len(circuit.gates),
        "ideal_p0": round(ideal_p0, 6),
        "noisy_error": round(noisy_error, 6),
        "mitigated_error": round(mitigated_error, 6),
    }


def run_experiment(
    shots: int,
    flip_probability: float,
) -> list[dict[str, float | str | int]]:
    """
    Compare unoptimized and optimized circuits.

    Input(s)
    --------
    - shots : int
        Number of measurement samples.
    - flip_probability : float
        Readout flip probability.

    Output(s)
    ---------
    - return_value : list[dict[str, float | str | int]]
        Experiment result rows.
    """
    validate_positive_int(shots, "shots")

    unoptimized = build_unoptimized_circuit()

    pass_manager = PassManager(
        passes=[CancelAdjacentInversesPass()]
    )
    optimized = pass_manager.run(unoptimized)

    return [
        summarize_circuit_case(
            "Unoptimized",
            unoptimized,
            shots,
            flip_probability,
        ),
        summarize_circuit_case(
            "Optimized",
            optimized,
            shots,
            flip_probability,
        ),
    ]


def save_results(
    rows: list[dict[str, float | str | int]],
    output_path: Path,
) -> None:
    """
    Save experiment results.

    Input(s)
    --------
    - rows : list[dict[str, float | str | int]]
        Result rows.
    - output_path : Path
        CSV output path.

    Output(s)
    ---------
    - return_value : None
        Writes results to disk.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=[
                "circuit_type",
                "gate_count",
                "ideal_p0",
                "noisy_error",
                "mitigated_error",
            ],
        )

        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    """
    Run compilation comparison experiment.

    Input(s)
    --------
    - parameter : None
        No inputs.

    Output(s)
    ---------
    - return_value : None
        Prints and saves experiment results.
    """
    rows = run_experiment(
        shots=DEFAULT_CONFIG.shots,
        flip_probability=DEFAULT_CONFIG.flip_probability,
    )

    print(
        format_error_table(
            [
                (
                    str(row["circuit_type"]),
                    float(row["noisy_error"]),
                    float(row["mitigated_error"]),
                )
                for row in rows
            ]
        )
    )

    save_results(rows, RESULTS_PATH)


if __name__ == "__main__":
    main()
