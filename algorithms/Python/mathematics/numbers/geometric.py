from mathematics.common import validate_positive_integer


def _get_nth_triangular_number_recursive(nth: int) -> int:
    """The actual recursive implementation."""

    if nth == 1:
        return 1
    return _get_nth_triangular_number_recursive(nth - 1) + nth


def get_triangular_number_recursive(nth: int) -> int:
    """Returns the nth triangular number.

    The indexation starts from zero, so T(1) = 1, T(2) = 3 and so forth.
    """

    validate_positive_integer(nth)
    return _get_nth_triangular_number_recursive(nth)


def get_triangular_number_iterative(nth: int) -> int:
    """Returns the nth triangular number.

    The indexation starts from zero, so T(1) = 1, T(2) = 3 and so forth.
    """

    validate_positive_integer(nth)
    nbr = nth
    for n in range(1, nth):
        nbr += n
    return nbr
