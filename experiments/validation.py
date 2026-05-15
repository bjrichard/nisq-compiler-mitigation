from __future__ import annotations


def validate_positive_int(
    value: int,
    name: str,
) -> None:
    """
    Validate that a value is a positive integer.

    Input(s)
    --------
    - value : int
        Value to validate.
    - name : str
        Human-readable parameter name.

    Output(s)
    ---------
    - return_value : None
        Raises if validation fails.
    """
    if not isinstance(name, str) or name.strip() == "":
        raise ValueError("name must be a non-empty string.")

    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer.")

    if value <= 0:
        raise ValueError(f"{name} must be greater than 0.")
