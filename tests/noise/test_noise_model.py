import pytest

from qc_compiler.circuits import Circuit
from qc_compiler.noise import BaseNoiseModel, NoiseModel


class DummyNoiseModel(BaseNoiseModel):
    """Minimal concrete noise model for testing."""

    def __init__(self) -> None:
        super().__init__(name="dummy_noise")

    def apply(self, circuit: Circuit) -> Circuit:
        """Return a new empty circuit."""
        _ = circuit
        return Circuit()


def test_base_requires_non_empty_name() -> None:
    """BaseNoiseModel rejects empty names."""
    with pytest.raises(ValueError):
        BaseNoiseModel(name="")


def test_dummy_noise_model_satisfies_protocol() -> None:
    """DummyNoiseModel can be treated as a NoiseModel."""
    m: NoiseModel = DummyNoiseModel()

    out = m.apply(Circuit())
    assert isinstance(out, Circuit)


def test_noise_model_has_name_property() -> None:
    """Noise model exposes a readable name."""
    m = DummyNoiseModel()
    assert m.name == "dummy_noise"


def test_noise_model_default_config_is_empty_dict() -> None:
    """BaseNoiseModel provides an empty default config."""
    m = DummyNoiseModel()
    assert m.config == {}
    assert m.config_validated == {}
