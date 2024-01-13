from contextlib import nullcontext as does_not_raise

import pytest

from mathematics.factorial import factorial_iterative, factorial_recursive
from mathematics.fibonacci import fibonacci_iterative, fibonacci_recursive
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
        (2, 2, does_not_raise()),
        (3, 6, does_not_raise()),
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
        assert res_rec == answer
        assert res_iter == answer


@pytest.mark.parametrize(
    ("number", "answer", "expectation"),
    [
        (-1, None, pytest.raises(ValueError)),
        (0, 0, does_not_raise()),
        (1, 1, does_not_raise()),
        (1.5, None, pytest.raises(TypeError)),
        (2, 1, does_not_raise()),
        (3, 2, does_not_raise()),
        (4, 3, does_not_raise()),
        (5, 5, does_not_raise()),
        (6, 8, does_not_raise()),
    ],
)
def test_fibonacci(number, answer, expectation):
    with expectation:
        res_iter = fibonacci_iterative(number)
        res_rec = fibonacci_recursive(number)
        assert res_iter == answer
        assert res_rec == answer


@pytest.mark.parametrize(
    ("number", "answer", "expectation"),
    [
        (-21, None, pytest.raises(ValueError)),
        (4.2, None, pytest.raises(TypeError)),
        (0, 1, pytest.raises(ValueError)),
        (1, 1, does_not_raise()),
        (2, 3, does_not_raise()),
        (3, 6, does_not_raise()),
        (4, 10, does_not_raise()),
        (5, 15, does_not_raise()),
    ],
)
def test_get_nth_triangular_number(number, answer, expectation):
    with expectation:
        res_rec = get_triangular_number_recursive(number)
        res_iter = get_triangular_number_iterative(number)
        assert res_iter == answer
        assert res_rec == answer
