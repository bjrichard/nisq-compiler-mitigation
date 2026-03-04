from __future__ import annotations

from qc_compiler.circuits.circuit import Circuit
from qc_compiler.circuits.gate import Gate
from qc_compiler.compilation.pass_base import BaseCompilerPass


class CancelAdjacentInversesPass(BaseCompilerPass):
    """Cancel adjacent self-inverse single-qubit gates on the same target."""

    def __init__(self) -> None:
        """
        Initialize the cancellation pass.

        Input(s)
        --------
        - parameter : None
            No inputs.

        Output(s)
        ---------
        - return_value : None
            Initializes the pass instance.
        """
        super().__init__(name="cancel_adjacent_inverses")

    def run(self, circuit: Circuit) -> Circuit:
        """
        Cancel adjacent self-inverse gates on identical targets.

        Input(s)
        --------
        - circuit : Circuit
            Input circuit to be transformed. The input circuit is not mutated.

        Output(s)
        ---------
        - return_value : Circuit
            A new circuit with eligible adjacent inverse pairs removed.
        """
        if not isinstance(circuit, Circuit):
            raise TypeError("circuit must be a Circuit instance.")

        out = Circuit()
        i = 0
        gates = circuit.gates

        while i < len(gates):
            if i + 1 < len(gates) and self._is_cancellable_pair(gates[i], gates[i + 1]):
                i += 2
                continue

            out.add_gate(gates[i])
            i += 1

        return out

    def _is_cancellable_pair(self, g1: Gate, g2: Gate) -> bool:
        """
        Return True if two adjacent gates form a cancellable pair.

        Input(s)
        --------
        - g1 : Gate
            First gate in the adjacent pair.
        - g2 : Gate
            Second gate in the adjacent pair.

        Output(s)
        ---------
        - return_value : bool
            True if the pair is self-inverse on the same target with empty params.
        """
        if g1.name not in {"X", "Z"}:
            return False
        if g2.name != g1.name:
            return False
        if g1.params != {} or g2.params != {}:
            return False

        t1 = [q.index for q in g1.targets]
        t2 = [q.index for q in g2.targets]
        return t1 == t2
