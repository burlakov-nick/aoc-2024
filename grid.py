from typing_extensions import Iterable


def range_2d(n: int, m: int) -> Iterable[tuple[int, int]]:
    for x in range(n):
        for y in range(m):
            yield x, y


def cells[T](matrix: list[list[T]]) -> Iterable[tuple[int, int, T]]:
    for x, row in enumerate(matrix):
        for y, v in enumerate(row):
            yield x, y, v
