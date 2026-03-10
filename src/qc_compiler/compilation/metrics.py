from __future__ import annotations

from qc_compiler.circuits.circuit import Circuit


def gate_count(circuit: Circuit) -> int:
    """
    Return the total number of gates in a circuit.

    Input(s)
    --------
    - circuit : Circuit
        Circuit whose gates are to be counted.

    Output(s)
    ---------
    - return_value : int
        Total number of gates in the circuit.
    """
    if not isinstance(circuit, Circuit):
        raise TypeError("circuit must be a Circuit instance.")
    return len(circuit.gates)


def gate_counts_by_name(circuit: Circuit) -> dict[str, int]:
    """
    Return the number of gates in a circuit grouped by gate name.

    Input(s)
    --------
    - circuit : Circuit
        Circuit whose gates are to be counted by name.

    Output(s)
    ---------
    - return_value : dict[str, int]
        Mapping from gate name to the number of times that gate appears.
    """
    if not isinstance(circuit, Circuit):
        raise TypeError("circuit must be a Circuit instance.")

    counts: dict[str, int] = {}
    for gate in circuit.gates:
        if gate.name not in counts:
            counts[gate.name] = 0
        counts[gate.name] += 1

    return dict(counts)


def two_qubit_gate_count(circuit: Circuit) -> int:
    """
    Return the number of two-qubit gates in a circuit.

    Input(s)
    --------
    - circuit : Circuit
        Circuit whose two-qubit gates are to be counted.

    Output(s)
    ---------
    - return_value : int
        Number of gates acting on exactly two target qubits.
    """
    if not isinstance(circuit, Circuit):
        raise TypeError("circuit must be a Circuit instance.")

    count = 0
    for gate in circuit.gates:
        if len(gate.targets) == 2:
            count += 1

    return count
