"""https://en.wikipedia.org/wiki/Fibonacci_sequence"""


from functools import lru_cache

from mathematics.common import validate_non_negative_integer


@lru_cache
def fibonacci_recursive(nth: int) -> int:
    """Returns the nth Fibonacci number."""

    def _fibrec(nbr: int) -> int:
        """Actual recursive implementation."""

        if not nbr:
            return 0
        if nbr < 3:
            return 1
        return _fibrec(nbr - 2) + _fibrec(nbr - 1)

    validate_non_negative_integer(nth)
    return _fibrec(nth)


def fibonacci_iterative(nth: int) -> int:
    """Returns the nth Fibonacci number."""

    validate_non_negative_integer(nth)
    fibcurr, fibnext = 0, 1
    for _ in range(nth):
        fibcurr, fibnext = fibnext, fibcurr + fibnext
    return fibcurr
