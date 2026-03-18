import pytest

from qc_compiler.circuits import Circuit, Gate, Qubit
from qc_compiler.noise import MeasurementNoiseModel


def test_measurement_noise_requires_valid_probability() -> None:
    """MeasurementNoiseModel validates flip_probability range."""
    with pytest.raises(ValueError):
        MeasurementNoiseModel(flip_probability=-0.1)

    with pytest.raises(ValueError):
        MeasurementNoiseModel(flip_probability=1.1)


def test_measurement_noise_rejects_non_numeric_probability() -> None:
    """MeasurementNoiseModel rejects non-numeric flip probabilities."""
    with pytest.raises(TypeError):
        MeasurementNoiseModel(flip_probability="bad")  # type: ignore[arg-type]


def test_measurement_noise_leaves_circuit_unchanged_when_probability_zero() -> None:
    """Zero flip probability inserts no readout_flip gates."""
    q0 = Qubit(0)
    circuit = Circuit()
    circuit.add_gate(Gate(name="X", targets=[q0]))
    circuit.add_gate(Gate(name="MEASURE", targets=[q0]))

    model = MeasurementNoiseModel(flip_probability=0.0, seed=123)
    noisy = model.apply(circuit)

    assert [gate.name for gate in noisy.gates] == ["X", "MEASURE"]


def test_measurement_noise_inserts_flip_before_measurement_when_probability_one() -> None:
    """Unit flip probability always inserts readout_flip before measurement."""
    q0 = Qubit(0)
    circuit = Circuit()
    circuit.add_gate(Gate(name="MEASURE", targets=[q0]))

    model = MeasurementNoiseModel(flip_probability=1.0, seed=123)
    noisy = model.apply(circuit)

    assert [gate.name for gate in noisy.gates] == ["READOUT_FLIP", "MEASURE"]


def test_measurement_noise_only_affects_measurement_gates() -> None:
    """Readout flips are only inserted before measurement gates."""
    q0 = Qubit(0)
    circuit = Circuit()
    circuit.add_gate(Gate(name="X", targets=[q0]))
    circuit.add_gate(Gate(name="Z", targets=[q0]))

    model = MeasurementNoiseModel(flip_probability=1.0, seed=123)
    noisy = model.apply(circuit)

    assert [gate.name for gate in noisy.gates] == ["X", "Z"]
