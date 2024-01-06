from mathematics.common import validate_non_negative_integer


def _get_nth_triangular_number_recursive(nth: int) -> int:
    if not nth:
        return 1
    return _get_nth_triangular_number_recursive(nth - 1) + nth


def get_triangular_number_recursive(nth: int) -> int:
    """Returns the nth triangular number.

    The indexation starts from zero, so T(0) = 1, T(1) = 3 and so forth.
    """

    validate_non_negative_integer(nth)
    return _get_nth_triangular_number_recursive(nth)


def get_triangular_number_iterative(nth: int) -> int:
    """Returns the nth triangular number.

    The indexation starts from zero, so T(0) = 1, T(1) = 3 and so forth.
    """

    validate_non_negative_integer(nth)
    sum_ = 1
    for _ in range(1, nth):
        sum_ += sum_ + 1
    return sum_
