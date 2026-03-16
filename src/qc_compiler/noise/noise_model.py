from __future__ import annotations

from typing import Protocol
from qc_compiler.circuits.circuit import Circuit


class NoiseModel(Protocol):
    """
    Structural interface for noise models.
    """

    @property
    def name(self) -> str:
        """
        Return the noise model name.

        Input(s)
        --------
        - parameter : None
            No inputs.

        Output(s)
        ---------
        - return_value : str
            Human-readable identifier for the noise model.
        """
        ...

    def apply(self, circuit: Circuit) -> Circuit:
        """
        Apply a noise model to a circuit.

        Input(s)
        --------
        - circuit : Circuit
            Circuit to which noise should be applied.

        Output(s)
        ---------
        - return_value : Circuit
            New circuit representing the noisy version.
        """
        ...


class BaseNoiseModel:
    """
    Base class providing shared noise model behavior.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a noise model.

        Input(s)
        --------
        - name : str
            Human-readable identifier for the noise model.

        Output(s)
        ---------
        - return_value : None
            Initializes the noise model instance.
        """
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("Noise model name must be a non-empty string.")

        self._name = name

    @property
    def name(self) -> str:
        """
        Return the noise model name.

        Input(s)
        --------
        - parameter : None
            No inputs.

        Output(s)
        ---------
        - return_value : str
            Human-readable identifier for the noise model.
        """
        return self._name

    def apply(self, circuit: Circuit) -> Circuit:
        """
        Apply noise to a circuit.

        Input(s)
        --------
        - circuit : Circuit
            Circuit to which noise should be applied.

        Output(s)
        ---------
        - return_value : Circuit
            Noisy circuit.

        Raises
        ------
        NotImplementedError
            If subclass does not implement the method.
        """
        raise NotImplementedError("Noise model subclasses must implement apply().")
