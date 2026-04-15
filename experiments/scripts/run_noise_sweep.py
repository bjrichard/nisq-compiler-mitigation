from __future__ import annotations

from qc_compiler.circuits import Circuit, Gate, Qubit
from qc_compiler.execution import sample_counts
from qc_compiler.mitigation import (
    confusion_matrix_from_model,
    mitigate_single_qubit_counts,
)
from qc_compiler.noise import MeasurementNoiseModel


def build_circuit() -> Circuit:
    """Single-qubit measurement circuit."""
    q0 = Qubit(0)
    circuit = Circuit()
    circuit.add_gate(Gate(name="MEASURE", targets=[q0]))
    return circuit


def normalize_counts(counts: dict[str, int]) -> dict[str, float]:
    total = sum(counts.values())
    return {k: v / total for k, v in counts.items()}


def sample_noisy_counts(
    circuit: Circuit,
    noise_model: MeasurementNoiseModel,
    shots: int,
) -> dict[str, int]:
    counts: dict[str, int] = {}

    for _ in range(shots):
        noisy_circuit = noise_model.apply(circuit)
        shot_counts = sample_counts(noisy_circuit, shots=1)
        bitstring = next(iter(shot_counts))
        counts[bitstring] = counts.get(bitstring, 0) + 1

    return counts


def run_experiment(flip_probability: float, shots: int = 1000) -> tuple[float, float]:
    """
    Run one experiment and return (noisy_error, mitigated_error).
    """
    circuit = build_circuit()

    noise_model = MeasurementNoiseModel(flip_probability=flip_probability, seed=123)
    noisy_counts = sample_noisy_counts(circuit, noise_model, shots)
    noisy_probs = normalize_counts(noisy_counts)

    cm = confusion_matrix_from_model(noise_model)
    mitigated_probs = mitigate_single_qubit_counts(noisy_counts, cm)

    ideal_p0 = 1.0

    noisy_error = abs(noisy_probs.get("0", 0.0) - ideal_p0)
    mitigated_error = abs(mitigated_probs.get("0", 0.0) - ideal_p0)

    return noisy_error, mitigated_error


def main() -> None:
    """
    Sweep over noise levels and print error comparison.
    """
    noise_levels = [0.0, 0.05, 0.1, 0.2, 0.3, 0.4]
    shots = 1000

    print("Flip Prob | Noisy Error | Mitigated Error")
    print("------------------------------------------")

    for p in noise_levels:
        noisy_err, mitigated_err = run_experiment(p, shots)
        print(f"{p:8.2f} | {noisy_err:11.4f} | {mitigated_err:16.4f}")


if __name__ == "__main__":
    main()
