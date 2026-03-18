from __future__ import annotations

import random

from qc_compiler.circuits.circuit import Circuit
from qc_compiler.circuits.gate import Gate
from qc_compiler.noise.noise_model import BaseNoiseModel


class MeasurementNoiseModel(BaseNoiseModel):
    """Noise model that inserts classical readout flips before measurement."""

    def __init__(self, flip_probability: float, seed: int | None = None) -> None:
        """
        Initialize a measurement noise model.

        Input(s)
        --------
        - flip_probability : float
            Probability that a measured bit is flipped during readout.
            Must satisfy 0.0 <= flip_probability <= 1.0.
        - seed : int | None
            Optional random seed for reproducibility.

        Output(s)
        ---------
        - return_value : None
            Initializes the measurement noise model instance.
        """
        super().__init__(name="measurement_noise")

        if not isinstance(flip_probability, (int, float)):
            raise TypeError("flip_probability must be a float.")
        if not 0.0 <= float(flip_probability) <= 1.0:
            raise ValueError("flip_probability must be between 0.0 and 1.0.")

        if seed is not None and not isinstance(seed, int):
            raise TypeError("seed must be an int or None.")

        self._flip_probability = float(flip_probability)
        self._rng = random.Random(seed)

    @property
    def config(self) -> dict[str, bool | int | float | str]:
        """
        Return measurement noise model configuration metadata.

        Input(s)
        --------
        - parameter : None
            No inputs.

        Output(s)
        ---------
        - return_value : dict[str, bool | int | float | str]
            Primitive configuration values describing the noise model.
        """
        return {"flip_probability": self._flip_probability}

    def apply(self, circuit: Circuit) -> Circuit:
        """
        Apply measurement noise to a circuit.

        Input(s)
        --------
        - circuit : Circuit
            Circuit to which measurement noise should be applied.

        Output(s)
        ---------
        - return_value : Circuit
            New circuit in which synthetic readout_flip gates may be inserted
            immediately before measurement gates.
        """
        if not isinstance(circuit, Circuit):
            raise TypeError("circuit must be a Circuit instance.")

        noisy_circuit = Circuit()

        for gate in circuit.gates:
            if gate.name == "MEASURE":
                for target in gate.targets:
                    if self._rng.random() < self._flip_probability:
                        noisy_circuit.add_gate(
                            Gate(name="READOUT_FLIP", targets=[target])
                        )
            noisy_circuit.add_gate(gate)

        return noisy_circuit
