from contextlib import nullcontext as does_not_raise

import pytest

from sequences.reverse_string import reverse_string_iterative, reverse_string_recursive
from sequences.is_palindrome import is_palindrome_iterative, is_palindrome_recursive


@pytest.mark.parametrize(
    ("seq", "answer", "expectation"),
    [
        ("", "", does_not_raise()),
        ("a", "a", does_not_raise()),
        ("12", "21", does_not_raise()),
        (("a", 2), (2, "a"), pytest.raises(TypeError)),
    ],
)
def test_reverse_recursively(seq, answer, expectation):
    with expectation:
        res_rec = reverse_string_recursive(seq)
        res_iter = reverse_string_iterative(seq)
        assert res_rec == res_iter == answer


@pytest.mark.parametrize(
    ("seq", "answer"),
    [
        ([], True),
        ({1}, True),
        ((1, 2), False),
        ((3, 3), True),
        ("abc", False),
        ("aBa", True),
    ],
)
def test_palindrome(seq, answer):
    res_iter = is_palindrome_iterative(seq)
    res_rec = is_palindrome_recursive(seq)
    assert res_iter == res_rec == answer
