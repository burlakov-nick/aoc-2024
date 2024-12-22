from collections import defaultdict, deque
from itertools import islice

from typing_extensions import Callable, Iterable


def range_2d(n: int, m: int) -> Iterable[tuple[int, int]]:
    for x in range(n):
        for y in range(m):
            yield x, y


def cells[T](matrix) -> Iterable:
    for x, row in enumerate(matrix):
        for y, v in enumerate(row):
            yield x, y, v


def batch(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def transpose[T](list2: list[list[T]]) -> list[list[T]]:
    return list(map(list, zip(*list2)))


def flatten[T](list2: list[list[T]]) -> list[T]:
    return [y for x in list2 for y in x]


def last[T](xs: Iterable[T]) -> T:
    result = None
    for x in xs:
        result = x
    return result


def sliding_window[T](xs: Iterable[T], n: int) -> tuple:
    iterator = iter(xs)
    window = deque(islice(iterator, n - 1), maxlen=n)
    for x in iterator:
        window.append(x)
        yield tuple(window)


def group_by(xs: Iterable, key: Callable) -> dict:
    r = defaultdict(list)
    for x in xs:
        r[key(x)].append(x)
    return r


def frequencies[T](xs: Iterable[T]) -> dict[T, int]:
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
