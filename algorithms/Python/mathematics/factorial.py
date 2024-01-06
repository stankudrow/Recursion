from functools import lru_cache

from mathematics.common import validate_non_negative_integer


def _rec_fact(nbr: int) -> int:
    """Returns the (nbr)!"""

    if nbr < 2:
        return 1
    return nbr * _rec_fact(nbr - 1)


@lru_cache
def factorial_recursive(number: int) -> int:
    """Returns the factorial of a non-negative integer."""

    validate_non_negative_integer(number)
    return _rec_fact(number)


def factorial_iterative(number: int) -> int:
    """Returns the factorial of a non-negative integer."""

    validate_non_negative_integer(number)
    if number < 2:
        return 1
    factorial: int = 2
    for factor in range(3, number + 1):
        factorial *= factor
    return factorial
