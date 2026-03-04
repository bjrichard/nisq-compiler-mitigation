from __future__ import annotations

from qc_compiler.circuits.circuit import Circuit
from qc_compiler.compilation.pass_base import CompilerPass


class PassManager:
    """Sequential runner for compiler passes."""

    def __init__(self, passes: list[CompilerPass]) -> None:
        """
        Create a pass manager.

        Input(s)
        --------
        - passes : list[CompilerPass]
            Ordered list of compiler passes to apply.

        Output(s)
        ---------
        - return_value : None
            This constructor initializes the pass manager instance.
        """
        if not isinstance(passes, list):
            raise TypeError("Passes must be a list of compiler pass objects.")

        self._passes = list(passes)
        for p in self._passes:
            self._validate_pass(p)

    @staticmethod
    def _validate_pass(p: CompilerPass) -> None:
        """
        Validate that an object satisfies the compiler pass contract.

        Input(s)
        --------
        - p : CompilerPass
            Candidate compiler pass object.

        Output(s)
        ---------
        - return_value : None
            Raises TypeError if the object does not satisfy the pass contract.
        """
        name = getattr(p, "name", None)
        if not isinstance(name, str) or name.strip() == "":
            raise TypeError("Each pass must have a non-empty string 'name' property.")

        config = getattr(p, "config", None)
        if not isinstance(config, dict):
            raise TypeError("Each pass must have a 'config' property returning a dict.")

        run = getattr(p, "run", None)
        if not callable(run):
            raise TypeError("Each pass must define a callable 'run(circuit) -> Circuit'.")

    @property
    def passes(self) -> list[CompilerPass]:
        """
        Return the ordered list of passes.

        Input(s)
        --------
        - parameter : None
            No inputs.

        Output(s)
        ---------
        - return_value : list[CompilerPass]
            Copy of the ordered list of passes.
        """
        return list(self._passes)

    def run(self, circuit: Circuit) -> Circuit:
        """
        Run all passes sequentially on the circuit.

        Input(s)
        --------
        - circuit : Circuit
            Input circuit. Each pass must treat its input as immutable.

        Output(s)
        ---------
        - return_value : Circuit
            Final circuit produced by applying all passes in order.
        """
        if not isinstance(circuit, Circuit):
            raise TypeError("circuit must be a Circuit instance.")

        current = circuit
        for p in self._passes:
            current = p.run(current)
        return current

    def __repr__(self) -> str:
        """
        Return a debug representation of the pass manager.

        Input(s)
        --------
        - parameter : None
            No inputs.

        Output(s)
        ---------
        - return_value : str
            String representation suitable for debugging.
        """
        names = [p.name for p in self._passes]
        return f"PassManager(passes={names})"
