import pytest
from qc_compiler.compilation import CompilerPass, CompilerPassBase
from qc_compiler.circuits import Circuit


class DummyConfiguredPass(CompilerPassBase):
    """Minimal concrete pass for testing base behavior."""

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


def test_base_requires_non_empty_name() -> None:
    """CompilerPassBase rejects empty or whitespace-only names."""
    try:
        _ = CompilerPassBase(name="")
        assert False, "Expected ValueError"
    except ValueError:
        pass
    # Condensed version:
    #with pytest.raises(ValueError):
        #_ = CompilerPass(name="")


def test_base_repr_includes_class_name_name_and_config() -> None:
    """__repr__ includes subclass name, pass name, and config."""
    p = DummyConfiguredPass(threshold=0.5)
    r = repr(p)
    assert "DummyConfiguredPass" in r
    assert "dummy_configured" in r
    assert "threshold" in r


def test_dummy_configured_pass_satisfies_protocol() -> None:
    """DummyConfiguredPass can be treated as a CompilerPass."""
    p: CompilerPass = DummyConfiguredPass(threshold=0.25)
    out = p.run(Circuit())
    assert isinstance(out, Circuit)


def test_config_values_are_primitives() -> None:
    """Pass config values are restricted to primitive types."""
    p = DummyConfiguredPass(threshold=1.0)
    for value in p.config.values():
        assert isinstance(value, (bool, int, float, str))


class BadConfigPass(CompilerPassBase):
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


def test_validated_config_rejects_non_primitives() -> None:
    """validated_config raises TypeError when config contains non-primitive values."""
    p = BadConfigPass()
    with pytest.raises(TypeError):
        _ = p.validated_config
