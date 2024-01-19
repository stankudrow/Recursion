from contextlib import nullcontext as does_not_raise

import pytest

from sequences.reverse_string import (
    reverse_string_iterative,
    reverse_string_recursive,
)
from sequences.is_palindrome import (
    is_palindrome_iterative,
    is_palindrome_recursive,
)
from sequences.search.linear_search import (
    linsearch_iterative,
    linsearch_recursive,
)
from sequences.search.binary_search import (
    binsearch_iterative,
    binsearch_recursive,
)


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
        assert res_rec == answer
        assert res_iter == answer


@pytest.mark.parametrize(
    ("seq", "answer"),
    [
        ([], True),
        ([1], True),
        ((1, 2), False),
        ((3, 3), True),
        ("abc", False),
        ("aBa", True),
        ("aBba", False),
        (["c", "d", "d", "c"], True),
    ],
)
def test_palindrome(seq, answer):
    res_iter = is_palindrome_iterative(seq)
    res_rec = is_palindrome_recursive(seq)
    assert res_iter == answer
    assert res_rec == answer


@pytest.mark.parametrize(
    ("sequence", "element", "answer"),
    [
        ([], 1, None),
        ([1], 2, None),
        ([1, 1], 1, 0),
        ([1, 2, 3], 3, 2),
        ((1, 2, 2, 3, 3, 3), 3, 3),
    ],
)
def test_linear_search(sequence, element, answer):
    res_iter = linsearch_iterative(sequence, element)
    res_rec = linsearch_recursive(sequence, element)
    assert res_iter == answer == res_rec


@pytest.mark.parametrize(
    ("sequence", "element", "answer"),
    [
        ([], 1, None),
        ([1], 2, None),
        ([1, 2], 1, 0),
        ([1, 2], 2, 1),
        ([1, 2, 3], 1, 0),
        ([1, 2, 3], 2, 1),
        ([1, 2, 3], 3, 2),
        ([1, 1, 1], 1, 1),
        ([2, 2, 2], 1, None),
        ([1, 2, 2, 3, 3, 3], 3, 4),
    ],
)
def test_binary_search(sequence, element, answer):
    res_iter = binsearch_iterative(sequence, element)
    res_rec = binsearch_recursive(sequence, element)
    assert res_iter == answer == res_rec
