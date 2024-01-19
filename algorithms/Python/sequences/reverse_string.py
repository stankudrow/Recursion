"""Algorithms for reversing the order of a string."""


def reverse_string_recursive(string: str) -> str:
    """Returns the reversed sequence."""

    def _reverse(s: str, idx: int) -> str:
        """The actual recursive implementation."""

        if not idx:
            return ""
        return s[idx - 1] + _reverse(s, idx - 1)

    if not isinstance(string, str):
        raise TypeError(f"{string} is not of type 'str'")
    return _reverse(string, len(string))


def reverse_string_iterative(string: str) -> str:
    """Returns the reversed string."""

    if not isinstance(string, str):
        raise TypeError(f"{string} is not of type 'str'")
    # actually, string[::-1] will do
    rev = ""
    for idx in range(len(string) - 1, -1, -1):
        rev += string[idx]
    return rev
