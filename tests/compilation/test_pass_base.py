import pytest

from qc_compiler.compilation import BaseCompilerPass, CompilerPass
from qc_compiler.circuits import Circuit


class DummyConfiguredPass(BaseCompilerPass):
    """Minimal concrete pass for testing BaseCompilerPass behavior."""

    def __init__(self, threshold: float) -> None:
        super().__init__(name="dummy_configured")
        self._threshold = threshold

    @property
    def config(self) -> dict[str, bool | int | float | str]:
        """Return a primitive-only configuration mapping."""
        return {"threshold": self._threshold}

    def run(self, circuit: Circuit) -> Circuit:
        """Return a new empty circuit (does not mutate input) for testing."""
        _ = circuit
        return Circuit()


class BadConfigPass(BaseCompilerPass):
    """Pass with invalid (non-primitive) config for testing enforcement."""

    def __init__(self) -> None:
        super().__init__(name="bad_config")

    @property
    def config(self) -> dict[str, bool | int | float | str]:
        """Return an invalid config (contains a list)."""
        return {"bad": [1, 2, 3]}  # type: ignore[return-value]

    def run(self, circuit: Circuit) -> Circuit:
        """Return a new empty circuit."""
        _ = circuit
        return Circuit()


def test_base_requires_non_empty_name() -> None:
    """BaseCompilerPass rejects empty or whitespace-only names."""
    with pytest.raises(ValueError):
        _ = BaseCompilerPass(name="")

    with pytest.raises(ValueError):
        _ = BaseCompilerPass(name="   ")


def test_base_repr_includes_class_name_name_and_config() -> None:
    """__repr__ includes subclass name, pass name, and validated config."""
    p = DummyConfiguredPass(threshold=0.5)
    r = repr(p)
    assert "DummyConfiguredPass" in r
    assert "dummy_configured" in r
    assert "threshold" in r


def test_dummy_configured_pass_satisfies_protocol() -> None:
    """DummyConfiguredPass can be used where a CompilerPass is expected."""
    p: CompilerPass = DummyConfiguredPass(threshold=0.25)
    out = p.run(Circuit())
    assert isinstance(out, Circuit)


def test_config_validated_returns_expected_mapping() -> None:
    """config_validated returns a validated copy of the config mapping."""
    p = DummyConfiguredPass(threshold=1.0)
    assert p.config_validated == {"threshold": 1.0}


def test_config_validated_rejects_non_primitives() -> None:
    """config_validated raises TypeError when config contains non-primitive values."""
    p = BadConfigPass()
    with pytest.raises(TypeError):
        _ = p.config_validated
