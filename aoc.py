import importlib
import re
import time
from typing import Callable

from typing_extensions import Any

import helpers
from vec import V


class Reader:
    def __init__(self, f):
        self.f = f

    def read_lines(self) -> list[str]:
        return self.f.read().splitlines()

    # rethink this 4 methods
    def read_grid_str(self) -> tuple[list[list[str]], int, int]:
        lines = self.read_lines()
        n, m = len(lines), len(lines[0])
        return [[ch for ch in row] for row in lines], n, m

    def read_grid_int(self) -> list[list[int]]:
        return [list(map(int, line)) for line in self.read_lines()]

    def read_grid_int_dict(self) -> dict[tuple[int, int], int]:
        matrix = self.read_grid_int()
        return {(x, y): v for x, y, v in helpers.cells(matrix)}

    def read_grid_dict_v(self) -> tuple[dict[V, str], int, int]:
        g, n, m = self.read_grid_str()
        return {V(x, y): g[x][y] for x, y, v in helpers.cells(g)}, n, m

    def read_grid_dict_v_int(self) -> tuple[dict[V, int], int, int]:
        g, n, m = self.read_grid_str()
        return {V(x, y): int(g[x][y]) for x, y, v in helpers.cells(g)}, n, m

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


def print_delimited(s: str) -> None:
    print(f"°*°*°*°*°*°*°*°*°*{s.center(20)}°*°*°*°*°*°*°*°*°*")


def run(day: int, sample: bool, test: bool) -> None:
    print_delimited(f"Day {day:02d}")
    day_module = importlib.import_module(f"day_{day:02d}")
    if sample:
        print_delimited("Run sample")
        with open(get_filename(day, "sample")) as f:
            day_module.solve(Reader(f))
    if test:
        print_delimited("Run test")
        with open(get_filename(day, "test")) as f:
            day_module.solve(Reader(f))
    print_delimited("the end")


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


def parse_ints(s: str) -> list[int]:
    return [int(x) for x in re.findall(r"-?\d+", s)]


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
