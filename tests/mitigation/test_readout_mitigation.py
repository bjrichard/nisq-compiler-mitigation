import pytest

from qc_compiler.mitigation import (
    invert_2x2_matrix,
    mitigate_single_qubit_counts,
    single_qubit_confusion_matrix,
)


def test_invert_identity_matrix() -> None:
    """Inverse of identity is identity."""
    matrix = [[1.0, 0.0], [0.0, 1.0]]
    assert invert_2x2_matrix(matrix) == matrix


def test_invert_valid_confusion_matrix() -> None:
    """Inverse exists for valid confusion matrices with p != 0.5."""
    matrix = single_qubit_confusion_matrix(0.2)
    inv = invert_2x2_matrix(matrix)

    assert isinstance(inv, list)
    assert len(inv) == 2


def test_invert_singular_matrix_raises() -> None:
    """Singular matrices (p=0.5) cannot be inverted."""
    matrix = single_qubit_confusion_matrix(0.5)
    with pytest.raises(ValueError):
        invert_2x2_matrix(matrix)


def test_mitigation_identity_case() -> None:
    """Identity confusion matrix leaves counts unchanged."""
    counts = {"0": 80, "1": 20}
    cm = [[1.0, 0.0], [0.0, 1.0]]

    result = mitigate_single_qubit_counts(counts, cm)

    assert result["0"] == pytest.approx(0.8)
    assert result["1"] == pytest.approx(0.2)


def test_mitigation_recovers_true_distribution() -> None:
    """Mitigation approximately recovers true distribution."""
    true_probs = {"0": 0.9, "1": 0.1}
    cm = single_qubit_confusion_matrix(0.2)

    # simulate noisy observation
    p_obs_0 = 0.9 * 0.8 + 0.1 * 0.2
    p_obs_1 = 0.9 * 0.2 + 0.1 * 0.8

    counts = {
        "0": int(p_obs_0 * 1000),
        "1": int(p_obs_1 * 1000),
    }

    mitigated = mitigate_single_qubit_counts(counts, cm)

    assert mitigated["0"] == pytest.approx(true_probs["0"], abs=0.05)
    assert mitigated["1"] == pytest.approx(true_probs["1"], abs=0.05)
