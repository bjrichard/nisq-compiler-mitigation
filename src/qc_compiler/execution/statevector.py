from __future__ import annotations

import math
import random

from qc_compiler.circuits import Circuit


def simulate_single_qubit_statevector(circuit: Circuit) -> list[complex]:
    """
    Simulate a single-qubit circuit using a statevector.

    Input(s)
    --------
    - circuit : Circuit
        Single-qubit circuit containing supported gates before measurement.

    Output(s)
    ---------
    - return_value : list[complex]
        Two-component statevector [amplitude_0, amplitude_1].
    """
    if not isinstance(circuit, Circuit):
        raise TypeError("circuit must be a Circuit instance.")
    if circuit.num_qubits() > 1:
        raise ValueError("only single-qubit circuits are supported.")

    state = [1.0 + 0.0j, 0.0 + 0.0j]

    for gate in circuit.gates:
        if gate.name == "MEASURE":
            continue

        if len(gate.targets) != 1:
            raise ValueError("only single-qubit gates are supported.")

        if gate.name == "X":
            state = [state[1], state[0]]

        elif gate.name == "Z":
            state = [state[0], -state[1]]

        elif gate.name == "H":
            a0, a1 = state
            factor = 1.0 / math.sqrt(2.0)
            state = [
                factor * (a0 + a1),
                factor * (a0 - a1),
            ]

        else:
            raise ValueError(f"unsupported gate for statevector simulation: {gate.name!r}")

    return state


def sample_single_qubit_statevector(
    state: list[complex],
    rng: random.Random | None = None,
) -> str:
    """
    Sample a bitstring from a single-qubit statevector.

    Input(s)
    --------
    - state : list[complex]
        Two-component statevector [amplitude_0, amplitude_1].
    - rng : random.Random | None
        Optional random number generator for reproducible sampling.

    Output(s)
    ---------
    - return_value : str
        Sampled bitstring, either "0" or "1".
    """
    if not isinstance(state, list) or len(state) != 2:
        raise ValueError("state must be a two-component list.")

    if rng is None:
        rng = random.Random()

    p0 = abs(state[0]) ** 2
    p1 = abs(state[1]) ** 2

    if abs((p0 + p1) - 1.0) > 1.0e-9:
        raise ValueError("state probabilities must sum to 1.")

    return "0" if rng.random() < p0 else "1"


def sample_statevector_counts(
    circuit: Circuit,
    shots: int,
    seed: int | None = None,
) -> dict[str, int]:
    """
    Sample many bitstrings from a simulated single-qubit statevector.

    Input(s)
    --------
    - circuit : Circuit
        Single-qubit circuit to simulate and sample.
    - shots : int
        Number of repeated samples.
    - seed : int | None
        Optional random seed for reproducible sampling.

    Output(s)
    ---------
    - return_value : dict[str, int]
        Mapping from bitstring to observed counts.
    """
    if not isinstance(shots, int) or shots <= 0:
        raise ValueError("shots must be a positive integer.")
    if seed is not None and not isinstance(seed, int):
        raise TypeError("seed must be an int or None.")

    rng = random.Random(seed)
    state = simulate_single_qubit_statevector(circuit)

    counts: dict[str, int] = {}
    for _ in range(shots):
        bitstring = sample_single_qubit_statevector(state, rng)
        counts[bitstring] = counts.get(bitstring, 0) + 1

    return counts
