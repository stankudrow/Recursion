from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest

from mathematics.factorial import factorial_iterative, factorial_recursive
from mathematics.geometric_numbers import (
    get_triangular_number_iterative,
    get_triangular_number_recursive,
)


@pytest.mark.parametrize(
    ("number", "answer", "expectation"),
    [
        (-1, None, pytest.raises(ValueError)),
        (0, 1, does_not_raise()),
        (1, 1, does_not_raise()),
        (4, 24, does_not_raise()),
        (5.0, 120, pytest.raises(TypeError)),
        # increase if you dare
        (5000, None, pytest.raises(RecursionError)),
    ],
)
def test_factorial(number, answer, expectation):
    with expectation:
        res_rec = factorial_recursive(number)
        res_iter = factorial_iterative(number)
        res_rec == res_iter == answer


@pytest.mark.parametrize(
    ("number", "answer", "expectation"),
    [
        (-21, None, pytest.raises(ValueError)),
        (4.2, None, pytest.raises(TypeError)),
        (0, 1, does_not_raise()),
        (1, 3, does_not_raise()),
        (2, 6, does_not_raise()),
        (3, 10, does_not_raise()),
    ],
)
def test_get_nth_triangular_number(number, answer, expectation):
    with expectation:
        res_rec = get_triangular_number_recursive(number)
        res_iter = get_triangular_number_iterative(number)
        res_rec == res_iter == answer
