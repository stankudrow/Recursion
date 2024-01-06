from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest

from strings.reverse_string import reverse_string_iterative, reverse_string_recursive


@pytest.mark.parametrize(
    ("string", "answer", "expectation"),
    [
        ("", "", does_not_raise()),
        ("a", "a", does_not_raise()),
        ("ab", "ba", does_not_raise()),
        (("a", 2), (2, "a"), pytest.raises(TypeError)),
    ],
)
def test_reverse_string_recursively(string, answer, expectation):
    with expectation:
        res_rec = reverse_string_recursive(string)
        res_iter = reverse_string_iterative(string)
        res_rec == res_iter == answer
