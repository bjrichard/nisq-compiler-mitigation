from __future__ import annotations
from qc_compiler.circuits.qubit import Qubit


class Gate:
    """Quantum gate operation applied to one or more target qubits."""

    def __init__(
        self,
        name: str,
        targets: list[Qubit],
        params: dict[str, float | int] | None = None,
    ) -> None:
        """
        Create a quantum gate operation.

        Input(s)
        ----------
        - name : str
            Gate identifier (e.g., "X", "Z", "CX"). Must be non-empty.
        - targets : list[Qubit]
            Target qubits the gate applies to. Must be non-empty and contain unique qubits.
        - params : dict[str, float | int] | None
            Optional parameter dictionary (e.g., {"theta": 1.23}). If None, treated as empty.

        Output(s)
        -------
        - return_value : None
            This constructor initializes the gate instance.
        """
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("name must be a non-empty string.")

        if not isinstance(targets, list) or len(targets) == 0:
            raise ValueError("targets must be a non-empty list of Qubit objects.")

        for target in targets:
            if not isinstance(target, Qubit):
                raise TypeError("targets must contain only Qubit objects.")

        # Enforce uniqueness by qubit index (avoids duplicate targets like [q0, q0]).
        indices = [q.index for q in targets]
        if len(set(indices)) != len(indices):
            raise ValueError("targets must not contain duplicate qubits.")

        # Avoid the mutable-default-argument pitfall by using None and materializing a new dict.
        if params is None:
            params = {}

        if not isinstance(params, dict):
            raise TypeError("params must be a dict or None.")

        self._name = name
        self._targets = list(targets)
        self._params = dict(params)

    @property
    def name(self) -> str:
        """
        Return the gate name.

        Input(s)
        ----------
        - parameter : None
            No inputs.

        Output(s)
        -------
        - return_value : str
            Gate identifier string.
        """
        return self._name

    @property
    def targets(self) -> list[Qubit]:
        """
        Return the target qubits.

        Input(s)
        ----------
        - parameter : None
            No inputs.

        Output(s)
        -------
        - return_value : list[Qubit]
            Copy of the target qubits list.
        """
        return list(self._targets)

    @property
    def params(self) -> dict[str, float | int]:
        """
        Return gate parameters.

        Input(s)
        ----------
        - parameter : None
            No inputs.

        Output(s)
        -------
        - return_value : dict[str, float | int]
            Copy of the parameter dictionary.
        """
        return dict(self._params)

    def __repr__(self) -> str:
        """
        Return a debug representation of the gate.

        Input(s)
        ----------
        - parameter : None
            No inputs.

        Output(s)
        -------
        - return_value : str
            String representation suitable for debugging.
        """
        target_indices = [q.index for q in self._targets]
        return f"Gate(name={self.name!r}, targets={target_indices}, params={self._params})"
