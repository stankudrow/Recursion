"""The implementations of the linear search algorithm."""


from typing import Any, Sequence


def linsearch_iterative(seq: Sequence[Any], item: Any) -> int | None:
    """Returns the index of the item if it is in the sequence.

    The index for the first occurence if returned.
    If the item is not in the sequence, None is returned.

    Parameters
    ----------
    seq : Sequence[Any]
        where to search
    item : Any
        what to search

    Returns
    -------
    int | None
        the index of the item if found else None.
    """

    for idx, elem in enumerate(seq):
        if elem == item:
            return idx
    return None


def linsearch_recursive(seq: Sequence[Any], item: Any) -> int | None:
    """Returns the index of the item if it is in the sequence.

    The index for the first occurence if returned.
    If the item is not in the sequence, None is returned.

    Parameters
    ----------
    seq : Sequence[Any]
        where to search
    item : Any
        what to search

    Returns
    -------
    int | None
        the index of the item if found else None.
    """

    def _linsearch(start: int, length: int) -> int | None:
        # De Morgan's laws, please check them out on your own
        if not (length and start < length):
            return None
        if seq[start] == item:
            return start
        return _linsearch(start + 1, length)

    return _linsearch(0, len(seq))
