def reverse_string_recursive(string: str) -> str:
    """Returns the reversed string.

    The function is made to be pure.
    It comes from the functional programming paradigm.
    A pure function is meant to have no side effects.
    In this case our function does not affect the original string.
    """

    def _reverse_string(s1: str, idx: int) -> str:
        """The actual recursive routine."""

        if not idx:
            return ""
        return s1[idx - 1] + _reverse_string(s1, idx - 1)

    if not isinstance(string, str):
        raise TypeError(f"{string} is not of type 'str'")
    return _reverse_string(string, len(string))


def reverse_string_iterative(string: str) -> str:
    """Returns the reversed string.

    The function is made to be pure.
    It comes from the functional programming paradigm.
    A pure function is meant to have no side effects.
    In this case our function does not affect the original string.
    """

    if not isinstance(string, str):
        raise TypeError(f"{string} is not of type 'str'")
    # Lazy enough for not resorting to an idiomatic solution
    return string[::-1]
