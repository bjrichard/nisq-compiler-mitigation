from __future__ import annotations

from qc_compiler.circuits.circuit import Circuit
from qc_compiler.noise.readout_sampling import (
    bitstring_from_readout,
    sample_readout,
)


def sample_counts(circuit: Circuit, shots: int) -> dict[str, int]:
    """
    Sample measurement outcomes multiple times and return counts.

    Input(s)
    --------
    - circuit : Circuit
        Circuit to sample.
    - shots : int
        Number of repeated samples.

    Output(s)
    ---------
    - return_value : dict[str, int]
        Mapping from bitstring to observed counts.
    """
    if not isinstance(circuit, Circuit):
        raise TypeError("circuit must be a Circuit instance.")

    if not isinstance(shots, int) or shots <= 0:
        raise ValueError("shots must be a positive integer.")

    counts: dict[str, int] = {}

    for _ in range(shots):
        readout = sample_readout(circuit)
        bitstring = bitstring_from_readout(readout)

        if bitstring not in counts:
            counts[bitstring] = 0
        counts[bitstring] += 1

    return dict(counts)
