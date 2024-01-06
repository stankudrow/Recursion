from mathematics.common import validate_non_negative_integer


def _rec_fact(nbr: int) -> int:
    """Returns the (nbr)!"""

    if nbr in (0, 1):
        return 1
    return nbr * _rec_fact(nbr - 1)


def factorial_recursive(number: int) -> int:
    """Returns the factorial of a non-negative integer."""

    validate_non_negative_integer(number)
    return _rec_fact(number)


def factorial_iterative(number: int) -> int:
    """Returns the factorial of a non-negative integer."""

    validate_non_negative_integer(number)
    for nbr in range(number - 1, 2, -1):
        number *= nbr
