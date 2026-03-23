from __future__ import annotations

from qc_compiler.noise.measurement_noise import MeasurementNoiseModel


def single_qubit_confusion_matrix(flip_probability: float) -> list[list[float]]:
    """
    Return the single-qubit readout confusion matrix from a flip probability.

    Input(s)
    --------
    - flip_probability : float
        Probability that a measured bit flips during readout.

    Output(s)
    ---------
    - return_value : list[list[float]]
        Two-by-two matrix where entry (i, j) is the probability of observing
        state j when state i was the true value:
        p00 = P(measure 0 | true 0)
        p01 = P(measure 1 | true 0)
        p10 = P(measure 0 | true 1)
        p11 = P(measure 1 | true 1)
    """
    if not isinstance(flip_probability, (int, float)):
        raise TypeError("flip_probability must be numeric.")

    p = float(flip_probability)
    if not 0.0 <= p <= 1.0:
        raise ValueError("flip_probability must be between 0 and 1.")

    keep_probability = 1.0 - p

    return [
        [keep_probability, p],
        [p, keep_probability],
    ]


def confusion_matrix_from_model(model: MeasurementNoiseModel) -> list[list[float]]:
    """
    Extract the single-qubit confusion matrix from a MeasurementNoiseModel.

    Input(s)
    --------
    - model : MeasurementNoiseModel
        Measurement noise model whose flip probability defines the confusion matrix.

    Output(s)
    ---------
    - return_value : list[list[float]]
        Two-by-two readout confusion matrix derived from the model configuration.
    """
    if not isinstance(model, MeasurementNoiseModel):
        raise TypeError("model must be a MeasurementNoiseModel.")

    flip_probability = model.config["flip_probability"]
    return single_qubit_confusion_matrix(flip_probability)


def is_valid_confusion_matrix(matrix: list[list[float]]) -> bool:
    """
    Check whether a matrix is a valid two-by-two confusion matrix.

    Input(s)
    --------
    - matrix : list[list[float]]
        Candidate matrix to validate.

    Output(s)
    ---------
    - return_value : bool
        True if the matrix is two-by-two, contains probabilities between 0 and 1,
        and each row sums to 1 within a small tolerance. Otherwise False.
    """
    if not isinstance(matrix, list) or len(matrix) != 2:
        return False

    for row in matrix:
        if not isinstance(row, list) or len(row) != 2:
            return False

        for value in row:
            if not isinstance(value, (int, float)):
                return False
            if not 0.0 <= float(value) <= 1.0:
                return False

        if abs(sum(row) - 1.0) > 1.0e-9:
            return False

    return True
