import pytest

from experiments.summary import format_error_row, format_error_table


def test_format_error_row_returns_expected_string() -> None:
    """format_error_row returns a formatted table row."""
    row = format_error_row("Superposition", 0.12345, 0.01234)

    assert row == "Superposition     |      0.1235 |           0.0123"


def test_format_error_row_rejects_empty_label() -> None:
    """format_error_row rejects empty labels."""
    with pytest.raises(ValueError):
        format_error_row("", 0.1, 0.01)


def test_format_error_table_includes_header_and_rows() -> None:
    """format_error_table returns header, separator, and formatted rows."""
    table = format_error_table(
        [
            ("Measurement-only", 0.2, 0.01),
            ("Superposition", 0.1, 0.02),
        ]
    )

    assert "Circuit Type" in table
    assert "Measurement-only" in table
    assert "Superposition" in table
