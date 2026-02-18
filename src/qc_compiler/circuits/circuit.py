from __future__ import annotations

from qc_compiler.circuits.gate import Gate


class Circuit:
    """Ordered container of gates representing a quantum circuit IR."""

    def __init__(self) -> None:
        """
        Create an empty circuit.

        Input(s)
        ----------
        - parameter : None
            No inputs.

        Output(s)
        -------
        - return_value : None
            This constructor initializes an empty circuit instance.
        """
        self._gates: list[Gate] = []

    @property
    def gates(self) -> list[Gate]:
        """
        Return the ordered list of gates in the circuit.

        Input(s)
        ----------
        - parameter : None
            No inputs.

        Output(s)
        -------
        - return_value : list[Gate]
            Copy of the ordered list of gates in the circuit.
        """
        return list(self._gates)

    def add_gate(self, gate: Gate) -> None:
        """
        Append a gate to the end of the circuit.

        Input(s)
        ----------
        - gate : Gate
            Gate to append to the circuit.

        Output(s)
        -------
        - return_value : None
            The circuit is updated in-place by appending the gate.
        """
        if not isinstance(gate, Gate):
            raise TypeError("gate must be a Gate instance.")
        self._gates.append(gate)

    def num_qubits(self) -> int:
        """
        Return the register size implied by qubit indices.

        Input(s)
        ----------
        - parameter : None
            No inputs.

        Output(s)
        -------
        - return_value : int
            If the circuit is empty, returns 0. Otherwise returns max qubit index + 1.
        """
        if len(self._gates) == 0:
            return 0

        max_index = -1
        for gate in self._gates:
            for qubit in gate.targets:
                if qubit.index > max_index:
                    max_index = qubit.index

        return max_index + 1

    def num_qubits_used(self) -> int:
        """
        Return the number of unique qubits referenced in the circuit.

        Input(s)
        ----------
        - parameter : None
            No inputs.

        Output(s)
        -------
        - return_value : int
            Count of unique qubit indices appearing in the circuit.
        """
        indices: set[int] = set()
        for gate in self._gates:
            for qubit in gate.targets:
                indices.add(qubit.index)
        return len(indices)

    def __repr__(self) -> str:
        """
        Return a debug representation of the circuit.

        Input(s)
        ----------
        - parameter : None
            No inputs.

        Output(s)
        -------
        - return_value : str
            String representation suitable for debugging.
        """
        return f"Circuit(num_gates={len(self._gates)}, num_qubits={self.num_qubits()})"
