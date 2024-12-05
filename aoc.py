import importlib
import re
import time
from typing import Callable

from typing_extensions import Any

import grid
from vec import V


class Reader:
    def __init__(self, f):
        self.f = f

    def read_lines(self) -> list[str]:
        return self.f.read().splitlines()

    def read_grid_dict(self) -> tuple[dict[V, str], int, int]:
        lines = self.read_lines()
        n, m = len(lines), len(lines[0])
        return {V(x, y): lines[x][y] for x in range(n) for y in range(m)}, n, m

    def read_grid_ints(self) -> list[list[int]]:
        return [list(map(int, line)) for line in self.read_lines()]

    def read_grid_int_dict(self) -> dict[tuple[int, int], int]:
        matrix = self.read_grid_ints()
        return {(x, y): v for x, y, v in grid.cells(matrix)}

    def read(
        self, parse: Callable | None = None, remove=None
    ) -> list:
        lines = [clean(line, remove) for line in self.read_lines()]
        return [parse(line) if parse else parse_values(line) for line in lines]

    def read_blocks(
        self,
        parse: Callable | None = None,
        remove: str | list | None = None,
    ) -> list:
        lines = [clean(line, remove) for line in self.read_lines()]
        blocks = []
        block = []
        for line in lines:
            if not line:
                blocks.append(block)
                block = []
            else:
                block.append(parse(line) if parse else parse_values(line))
        blocks.append(block)
        return blocks


def get_filename(day: int, name: str) -> str:
    return f"day_{day:02d}/{name}.txt"


def print_delimeted(s: str, width: int = 80) -> None:
    print(f"°*°*°*°*°*°*°*°*°*{s.center(20)}°*°*°*°*°*°*°*°*°*")


def run(day: int, sample: bool, test: bool) -> None:
    print_delimeted(f"Day {day:02d}")
    day_module = importlib.import_module(f"day_{day:02d}")
    if sample:
        print_delimeted("Run sample")
        with open(get_filename(day, "sample")) as f:
            day_module.solve(Reader(f))
    if test:
        print_delimeted("Run test")
        with open(get_filename(day, "test")) as f:
            day_module.solve(Reader(f))
    print_delimeted("the end")


def measure(name: str, f: Callable) -> Any:
    start = time.time()
    result = f()
    print(name, "time took", time.time() - start)
    return result


def clean(line: str, remove: str | list | None) -> str:
    if not remove:
        return line
    if isinstance(remove, str):
        return line.replace(remove, " ")
    else:
        for t in remove:
            line = line.replace(t, " ")
    return line


def parse_values(s: str, sep: str | None = None) -> list[int | float | str]:
    parts: list[str] = s.split() if sep is None else re.split(sep, s)
    return [parse_value(item) for item in parts if item != ""]


def parse_value(s: str) -> int | float | str:
    i = try_parse_int(s)
    if i is not None:
        return i
    f = try_parse_float(s)
    if f is not None:
        return f
    return s


def try_parse_int(s: str) -> int | None:
    try:
        return int(s)
    except ValueError:
        return None


def try_parse_float(s: str) -> float | None:
    try:
        return float(s)
    except ValueError:
        return None


def ch_to_int(x: str) -> int:
    return (ord(x) - ord("a") + 1) if "a" <= x <= "z" else (ord(x) - ord("A") + 27)
