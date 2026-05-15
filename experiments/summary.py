from __future__ import annotations


def format_error_row(
    label: str,
    noisy_error: float,
    mitigated_error: float,
) -> str:
    """
    Format one experiment error summary row.

    Input(s)
    --------
    - label : str
        Human-readable experiment label.
    - noisy_error : float
        Error before mitigation.
    - mitigated_error : float
        Error after mitigation.

    Output(s)
    ---------
    - return_value : str
        Formatted summary row.
    """
    if not isinstance(label, str) or label.strip() == "":
        raise ValueError("label must be a non-empty string.")

    if not isinstance(noisy_error, (int, float)):
        raise TypeError("noisy_error must be numeric.")

    if not isinstance(mitigated_error, (int, float)):
        raise TypeError("mitigated_error must be numeric.")

    return f"{label:<17} | {noisy_error:11.4f} | {mitigated_error:16.4f}"


def format_error_table(rows: list[tuple[str, float, float]]) -> str:
    """
    Format experiment error rows as a table.

    Input(s)
    --------
    - rows : list[tuple[str, float, float]]
        Rows containing label, noisy error, and mitigated error.

    Output(s)
    ---------
    - return_value : str
        Multi-line formatted table.
    """
    if not isinstance(rows, list):
        raise TypeError("rows must be a list.")

    header = "Circuit Type      | Noisy Error | Mitigated Error"
    separator = "--------------------------------------------------"

    lines = [header, separator]

    for label, noisy_error, mitigated_error in rows:
        lines.append(
            format_error_row(
                label,
                noisy_error,
                mitigated_error,
            )
        )

    return "\n".join(lines)
