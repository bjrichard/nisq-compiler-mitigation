from __future__ import annotations

from qc_compiler.mitigation.confusion_matrix import is_valid_confusion_matrix


def invert_2x2_matrix(matrix: list[list[float]]) -> list[list[float]]:
    """
    Compute the inverse of a 2x2 matrix.

    Input(s)
    --------
    - matrix : list[list[float]]
        Two-by-two matrix.

    Output(s)
    ---------
    - return_value : list[list[float]]
        Inverse of the input matrix.

    Raises
    ------
    ValueError
        If the matrix is singular.
    """
    if not is_valid_confusion_matrix(matrix):
        raise ValueError("matrix must be a valid 2x2 confusion matrix.")

    a, b = matrix[0]
    c, d = matrix[1]

    det = a * d - b * c
    if abs(det) < 1e-12:
        raise ValueError("matrix is singular and cannot be inverted.")

    inv_det = 1.0 / det

    return [
        [d * inv_det, -b * inv_det],
        [-c * inv_det, a * inv_det],
    ]


def mitigate_single_qubit_counts(
    counts: dict[str, int],
    confusion_matrix: list[list[float]],
) -> dict[str, float]:
    """
    Apply readout error mitigation to single-qubit measurement counts.

    Input(s)
    --------
    - counts : dict[str, int]
        Observed counts mapping bitstring ("0" or "1") to frequency.
    - confusion_matrix : list[list[float]]
        Two-by-two readout confusion matrix.

    Output(s)
    ---------
    - return_value : dict[str, float]
        Corrected (mitigated) probability distribution over {"0", "1"}.
    """
    if not isinstance(counts, dict):
        raise TypeError("counts must be a dictionary.")

    if not is_valid_confusion_matrix(confusion_matrix):
        raise ValueError("confusion_matrix must be valid.")

    total = sum(counts.values())
    if total == 0:
        raise ValueError("counts must not be empty.")

    p_obs = [
        counts.get("0", 0) / total,
        counts.get("1", 0) / total,
    ]

    inv = invert_2x2_matrix(confusion_matrix)

    p_true = [
        inv[0][0] * p_obs[0] + inv[0][1] * p_obs[1],
        inv[1][0] * p_obs[0] + inv[1][1] * p_obs[1],
    ]

    return {
        "0": p_true[0],
        "1": p_true[1],
    }
