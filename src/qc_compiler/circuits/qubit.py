from __future__ import annotations


class Qubit:
    """Logical qubit identified by a non-negative integer index."""

    def __init__(self, index: int) -> None:
        """
        Create a logical qubit.

        Input(s)
        ----------
        - index : int
            Unique, non-negative identifier for the qubit.

        Output(s)
        -------
        - return_value : None
            This constructor initializes the qubit instance.
        """
        if not isinstance(index, int):
            raise TypeError("index must be an int.")
        if index < 0:
            raise ValueError("index must be non-negative.")

        self._index = index

    @property
    def index(self) -> int:
        """
        Return the qubit index.

        Input(s)
        ----------
        - parameter : None
            No inputs.

        Output(s)
        -------
        - return_value : int
            The non-negative integer identifier for the qubit.
        """
        return self._index

    def __eq__(self, other: object) -> bool:
        """
        Check equality with another object.

        Input(s)
        ----------
        - other : object
            Object to compare against.

        Output(s)
        -------
        - return_value : bool
            True if other is a Qubit with the same index, else False.
        """
        if not isinstance(other, Qubit):
            return False
        return self.index == other.index

    def __repr__(self) -> str:
        """
        Return a debug representation of the qubit.

        Input(s)
        ----------
        - parameter : None
            No inputs.

        Output(s)
        -------
        - return_value : str
            String representation suitable for debugging.
        """
        return f"Qubit(index={self.index})"
