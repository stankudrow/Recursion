from typing import Any


def validate_integer(number: Any) -> None:
    """Validates if an object is of int() type."""

    if not isinstance(number, int):
        raise TypeError(f"{number} is not int")


def validate_non_negative_integer(number: int) -> None:
    """Validates a number to be a non-negative integer."""

    validate_integer(number)
    if number < 0:
        raise ValueError(f"{number} < 0")


def validate_positive_integer(number: Any) -> None:
    """Validates a number to be a positive integer."""

    validate_integer(number)
    if number < 1:
        raise ValueError(f"{number} < 1")
