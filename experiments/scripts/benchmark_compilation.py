from qc_compiler.circuits import Circuit, Gate, Qubit
from qc_compiler.compilation import gate_count, gate_counts_by_name, two_qubit_gate_count
from qc_compiler.compilation.passes import CancelAdjacentInversesPass


def build_benchmark_circuit() -> Circuit:
    """
    Build a small circuit for benchmarking a compilation pass.

    Input(s)
    --------
    - parameter : None
        No inputs.

    Output(s)
    ---------
    - return_value : Circuit
        A circuit containing cancellable and non-cancellable gate patterns.
    """
    q0 = Qubit(0)
    q1 = Qubit(1)

    circuit = Circuit()
    circuit.add_gate(Gate(name="X", targets=[q0]))
    circuit.add_gate(Gate(name="X", targets=[q0]))
    circuit.add_gate(Gate(name="Z", targets=[q1]))
    circuit.add_gate(Gate(name="Z", targets=[q1]))
    circuit.add_gate(Gate(name="CX", targets=[q0, q1]))
    circuit.add_gate(Gate(name="X", targets=[q1]))

    return circuit


def summarize_circuit(circuit: Circuit) -> dict[str, object]:
    """
    Return a summary of basic circuit metrics.

    Input(s)
    --------
    - circuit : Circuit
        Circuit to summarize.

    Output(s)
    ---------
    - return_value : dict[str, object]
        Mapping containing basic circuit metrics and gate counts by name.
    """
    return {
        "total_gates": gate_count(circuit),
        "two_qubit_gates": two_qubit_gate_count(circuit),
        "gate_counts_by_name": gate_counts_by_name(circuit),
    }


def main() -> None:
    """
    Build a benchmark circuit, run a compiler pass, and print before/after metrics.

    Input(s)
    --------
    - parameter : None
        No inputs.

    Output(s)
    ---------
    - return_value : None
        Prints a simple benchmark report to standard output.
    """
    circuit_before = build_benchmark_circuit()
    pass_instance = CancelAdjacentInversesPass()
    circuit_after = pass_instance.run(circuit_before)

    summary_before = summarize_circuit(circuit_before)
    summary_after = summarize_circuit(circuit_after)

    print("Initial circuit")
    print("---------------")
    print(f"Total gates: {summary_before['total_gates']}")
    print(f"Two-qubit gates: {summary_before['two_qubit_gates']}")
    print(f"Gate counts by name: {summary_before['gate_counts_by_name']}")
    print()

    print(f"After {pass_instance.name}")
    print("-" * (6 + len(pass_instance.name)))
    print(f"Total gates: {summary_after['total_gates']}")
    print(f"Two-qubit gates: {summary_after['two_qubit_gates']}")
    print(f"Gate counts by name: {summary_after['gate_counts_by_name']}")


if __name__ == "__main__":
    main()
