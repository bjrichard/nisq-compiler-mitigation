from __future__ import annotations

from qc_compiler.circuits.circuit import Circuit


def sample_readout(circuit: Circuit) -> dict[int, int]:
    """
    Sample a classical readout result from a circuit containing measurement gates.

    Input(s)
    --------
    - circuit : Circuit
        Circuit whose measurement-related gates are interpreted to produce a
        classical readout outcome.

    Output(s)
    ---------
    - return_value : dict[int, int]
        Mapping from qubit index to measured classical bit value, restricted to
        values 0 or 1.
    """
    if not isinstance(circuit, Circuit):
        raise TypeError("circuit must be a Circuit instance.")

    bit_values: dict[int, int] = {}

    for gate in circuit.gates:
        if gate.name == "READOUT_FLIP":
            for target in gate.targets:
                current = bit_values.get(target.index, 0)
                bit_values[target.index] = 1 - current

        elif gate.name == "MEASURE":
            for target in gate.targets:
                bit_values.setdefault(target.index, 0)

    return dict(bit_values)


def bitstring_from_readout(readout: dict[int, int]) -> str:
    """
    Convert a readout mapping into an ordered bitstring.

    Input(s)
    --------
    - readout : dict[int, int]
        Mapping from qubit index to classical bit value.

    Output(s)
    ---------
    - return_value : str
        Bitstring ordered by ascending qubit index. Returns an empty string if
        the input mapping is empty.
    """
    if not isinstance(readout, dict):
        raise TypeError("readout must be a dictionary.")

    if len(readout) == 0:
        return ""

    for key, value in readout.items():
        if not isinstance(key, int):
            raise TypeError("readout keys must be integers.")
        if value not in {0, 1}:
            raise ValueError("readout values must be 0 or 1.")

    ordered_indices = sorted(readout.keys())
    return "".join(str(readout[index]) for index in ordered_indices)
