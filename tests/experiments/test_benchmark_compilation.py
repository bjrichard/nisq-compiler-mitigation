from qc_compiler.circuits import Circuit

from experiments.scripts.benchmark_compilation import build_benchmark_circuit, summarize_circuit


def test_build_benchmark_circuit_returns_circuit() -> None:
    """build_benchmark_circuit returns a Circuit instance."""
    circuit = build_benchmark_circuit()
    assert isinstance(circuit, Circuit)


def test_benchmark_circuit_has_expected_initial_metrics() -> None:
    """Benchmark circuit starts with the expected gate totals."""
    circuit = build_benchmark_circuit()
    summary = summarize_circuit(circuit)

    assert summary["total_gates"] == 6
    assert summary["two_qubit_gates"] == 1
    assert summary["gate_counts_by_name"] == {"X": 3, "Z": 2, "CX": 1}
