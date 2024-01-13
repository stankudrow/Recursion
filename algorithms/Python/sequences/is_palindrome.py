"""Detects if a sequence is palindromic."""


from typing import Sequence


def is_palindrome_recursive(seq: Sequence) -> bool:
    """Returns True if the sequence is a palindrome.

    Parameters
    ----------
    seq : Sequence

    Returns
    -------
    bool
    """

    def _is_pal(left_idx: int, right_idx: int) -> bool:
        """The actual a bit optimised version."""

        if (right_idx - left_idx) < 1:
            return True
        if seq[left_idx] != seq[right_idx]:
            return False
        return _is_pal(left_idx + 1, right_idx - 1)

    length = len(seq)
    right_index = length - 1 if length else 0
    return _is_pal(0, right_index)


def is_palindrome_iterative(seq: Sequence) -> bool:
    """Returns True if the sequence is a palindrome.

    Parameters
    ----------
    seq : Sequence

    Returns
    -------
    bool
    """

    length: int = len(seq)
    for index in range(length // 2):
        if seq[index] != seq[-(index + 1)]:
            return False
    return True
