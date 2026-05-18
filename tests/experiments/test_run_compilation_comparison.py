import pytest

from experiments.scripts.run_compilation_comparison import (
    build_unoptimized_circuit,
    probability_error,
    run_experiment,
    summarize_circuit_case,
)
from qc_compiler.circuits import Circuit, Gate, Qubit


def test_build_unoptimized_circuit_contains_four_gates() -> None:
    """Unoptimized circuit contains redundant X gates."""
    circuit = build_unoptimized_circuit()

    assert len(circuit.gates) == 4
    assert [gate.name for gate in circuit.gates] == ["X", "X", "H", "MEASURE"]


def test_probability_error_returns_absolute_difference() -> None:
    """probability_error computes absolute error."""
    error = probability_error(0.7, 0.5)

    assert error == pytest.approx(0.2)


def test_summarize_circuit_case_returns_expected_keys() -> None:
    """summarize_circuit_case returns a result row with expected keys."""
    q0 = Qubit(0)
    circuit = Circuit()
    circuit.add_gate(Gate(name="H", targets=[q0]))
    circuit.add_gate(Gate(name="MEASURE", targets=[q0]))

    row = summarize_circuit_case(
        label="Test",
        circuit=circuit,
        shots=100,
        flip_probability=0.1,
    )

    assert set(row.keys()) == {
        "circuit_type",
        "gate_count",
        "ideal_p0",
        "noisy_error",
        "mitigated_error",
    }


def test_run_experiment_returns_two_rows() -> None:
    """run_experiment returns optimized and unoptimized rows."""
    rows = run_experiment(
        shots=100,
        flip_probability=0.1,
    )

    assert len(rows) == 2


def test_optimized_circuit_has_fewer_gates() -> None:
    """Compiler optimization reduces gate count."""
    rows = run_experiment(
        shots=100,
        flip_probability=0.1,
    )

    gate_counts = {
        row["circuit_type"]: row["gate_count"]
        for row in rows
    }

    assert gate_counts["Optimized"] < gate_counts["Unoptimized"]
