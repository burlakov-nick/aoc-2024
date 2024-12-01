from typing_extensions import Iterable


def cells[T](matrix: list[list[T]]) -> Iterable[tuple[int, int, T]]:
    for x, row in enumerate(matrix):
        for y, v in enumerate(row):
            yield x, y, v
