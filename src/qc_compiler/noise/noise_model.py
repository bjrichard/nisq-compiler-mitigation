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

    @property
    def config(self) -> dict[str, bool | int | float | str]:
        """
        Return configuration metadata for the noise model.

        Input(s)
        --------
        - parameter : None
            No inputs.

        Output(s)
        ---------
        - return_value : dict[str, bool | int | float | str]
            Dictionary containing primitive configuration values.
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
            raise ValueError("Name must be a non-empty string.")

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

    @property
    def config(self) -> dict[str, bool | int | float | str]:
        """
        Return configuration metadata for the noise model.

        Input(s)
        --------
        - parameter : None
            No inputs.

        Output(s)
        ---------
        - return_value : dict[str, bool | int | float | str]
            Dictionary of configuration values using primitive types only.
            Default implementation returns an empty dictionary.
        """
        return {}

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
        """
        raise NotImplementedError("Noise model subclasses must implement apply().")

    def _validate_config(self, config: dict[str, bool | int | float | str]) -> None:
        """
        Validate that config values are primitive types only.

        Input(s)
        --------
        - config : dict[str, bool | int | float | str]
            Configuration dictionary to validate.

        Output(s)
        ---------
        - return_value : None
            Raises TypeError if any config value is not a primitive type.
        """
        for key, value in config.items():
            if not isinstance(value, (bool, int, float, str)):
                raise TypeError(
                    f"config value for key {key!r} must be a primitive type, got {type(value)}."
                )

    @property
    def config_validated(self) -> dict[str, bool | int | float | str]:
        """
        Return validated configuration metadata for the noise model.

        Input(s)
        --------
        - parameter : None
            No inputs.

        Output(s)
        ---------
        - return_value : dict[str, bool | int | float | str]
            Copy of the configuration dictionary after enforcing primitive-only value types.
        """
        config = self.config
        self._validate_config(config)
        return dict(config)

    def __repr__(self) -> str:
        """
        Return a debug representation of the noise model.

        Input(s)
        --------
        - parameter : None
            No inputs.

        Output(s)
        ---------
        - return_value : str
            String representation suitable for debugging.
        """
        return (
            f"{type(self).__name__}(name={self.name!r}, "
            f"config={self.config_validated!r})"
        )
