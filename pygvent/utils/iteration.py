import itertools

from typing import Iterable, T, Tuple


def pairwise(iterable: Iterable[T]) -> Iterable[Tuple[T, T]]:
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)
