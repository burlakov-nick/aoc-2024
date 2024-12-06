from collections import defaultdict

from typing_extensions import Iterable


def batch(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def transpose[T](list2: list[list[T]]) -> list[list[T]]:
    return list(map(list, zip(*list2)))


def flatten[T](list2: list[list[T]]) -> list[T]:
    return [y for x in list2 for y in x]


def freq[T](xs: list[T]) -> dict[T, int]:
    f = defaultdict(int)
    for x in xs:
        f[x] += 1
    return f


def get_submasks(mask: int) -> Iterable:
    x = mask
    while True:
        yield x
        if x == 0:
            break
        x = (x - 1) & mask
