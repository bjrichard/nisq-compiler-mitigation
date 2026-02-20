from qc_compiler.circuits import Circuit, Gate, Qubit
import math


def build_simple_circuit() -> Circuit:
    """
    Build a small example circuit for sanity checking the intermediate representation.

    Input(s)
    ----------
    - parameter : None
        No inputs.

    Output(s)
    -------
    - return_value : Circuit
        A small circuit containing a mix of one-qubit and two-qubit gates.
    """
    q0 = Qubit(0)
    q1 = Qubit(1)
    q2 = Qubit(2)

    circuit = Circuit()
    circuit.add_gate(Gate(name="X", targets=[q0]))
    circuit.add_gate(Gate(name="RZ", targets=[q1], params={"theta": math.pi/3}))
    circuit.add_gate(Gate(name="CX", targets=[q1, q2]))

    return circuit


def main() -> None:
    """
    Print a readable representation of a simple example circuit.

    Input(s)
    ----------
    - parameter : None
        No inputs.

    Output(s)
    -------
    - return_value : None
        Prints the circuit and its gates to standard output.
    """
    circuit = build_simple_circuit()
    print(circuit)
    for gate in circuit.gates:
        print(gate)


if __name__ == "__main__":
    # code to run when executed directly
    main()
