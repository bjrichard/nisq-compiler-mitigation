from __future__ import annotations

from typing import Protocol

from qc_compiler.circuits.circuit import Circuit

class CompilerPass(Protocol):
    """
    Structural interface for compiler passes.

    Any class that provides the required properties and run method
    can be treated as a CompilerPass.
    """

    @property
    def name(self) -> str:
        """
        Return the pass name.

        Input(s)
        ----------
        - parameter : None
            No inputs.

        Output(s)
        -------
        - return_value : str
            Human-readable identifier for the pass.
        """
        ...

    @property
    def config(self) -> dict[str, bool | int | float | str]:
        """
        Return pass configuration metadata.

        Input(s)
        ----------
        - parameter : None
            No inputs.

        Output(s)
        -------
        - return_value : dict[str, bool | int | float | str]
            Dictionary containing primitive configuration values.
            Values must be JSON-serializable primitives.
        """
        ...

    def run(self, circuit: Circuit) -> Circuit:
        """
        Transform a circuit and return a new circuit.

        Input(s)
        ----------
        - circuit : Circuit
            Input circuit to be transformed. Implementations must not
            mutate the input circuit.

        Output(s)
        -------
        - return_value : Circuit
            A new Circuit instance representing the transformed circuit.
        """
        ...

class CompilerPassBase:
    """
    Default base class implementing shared compiler pass behavior.
    Compiler passes transform circuits.

    Subclasses should override:
        - run()
        - config (if configuration exists)

    This class enforces:
        - non-empty pass name
        - primitive-only configuration contract
        - standardized debug representation
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a compiler pass base instance.

        Input(s)
        ----------
        - name : str
            Human-readable identifier for the pass. Must be non-empty.

        Output(s)
        -------
        - return_value : None
            Initializes internal state for the compiler pass.
        """
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("name must be a non-empty string.")
        self._name = name

    @property
    def name(self) -> str:
        """
        Return the pass name.

        Input(s)
        ----------
        - parameter : None
            No inputs.

        Output(s)
        -------
        - return_value : str
            Human-readable identifier for the pass.
        """
        return self._name

    @property
    def config(self) -> dict[str, bool | int | float | str]:
        """
        Return pass configuration metadata for logging and reproducibility.

        Input(s)
        ----------
        - parameter : None
            No inputs.

        Output(s)
        -------
        - return_value : dict[str, bool | int | float | str]
            Dictionary of configuration values using primitive types only.
            Default implementation returns an empty dictionary.
        """
        return {}

    def run(self, circuit: Circuit) -> Circuit:
        """
        Transform a circuit and return the new, transformed circuit.

        Input(s)
        ----------
        - circuit : Circuit
            Input circuit to be transformed. Implementations must not mutate it.

        Output(s)
        -------
        - return_value : Circuit
            Transformed circuit. Implementations must return a new Circuit instance.
        """
        raise NotImplementedError("CompilerPassBase subclasses must implement run().")

    def _validate_config(self, config: dict[str, bool | int | float | str]) -> None:
        """
        Validate that config values are primitive types only.

        Input(s)
        ----------
        - config : dict[str, bool | int | float | str]
            Configuration dictionary to validate.

        Output(s)
        -------
        - return_value : None
            Raises TypeError if any value is not a primitive type.
        """
        for key, value in config.items():
            if not isinstance(value, (bool, int, float, str)):
                raise TypeError(
                    f"config value for key {key!r} must be a primitive type, got {type(value)}."
                )

    @property
    def validated_config(self) -> dict[str, bool | int | float | str]:
        """
        Return validated configuration metadata for the pass.

        Input(s)
        ----------
        - parameter : None
            No inputs.

        Output(s)
        -------
        - return_value : dict[str, bool | int | float | str]
            Configuration dictionary after enforcing primitive-only value types.
        """
        config = self.config
        self._validate_config(config)
        return dict(config)

    def __repr__(self) -> str:
        """
        Return a debug representation of the compiler pass.

        Input(s)
        ----------
        - parameter : None
            No inputs.

        Output(s)
        -------
        - return_value : str
            String representation suitable for debugging.
        """
        # type(self).__name__ <-> self.__class__.__name__
        return (
            f"{type(self).__name__}(name={self.name!r}, "
            f"config={self.validated_config!r})"
        )
