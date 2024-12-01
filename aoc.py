import importlib
import re
import time
from typing import Callable

from typing_extensions import Any

import grid


class Reader:
    def __init__(self, f):
        self.f = f

    def read_lines(self) -> list[str]:
        return self.f.read().splitlines()

    def read_map_ints(self) -> list[list[int]]:
        return [list(map(int, line)) for line in self.read_lines()]

    def read_map_dict(self) -> dict[tuple[int, int], int]:
        matrix = self.read_map_ints()
        return {(x, y): v for x, y, v in grid.cells(matrix)}

    def read(
        self, sep: str | None = None, parse: Callable | None = None, trim=None
    ) -> list:
        lines = [clean(line, trim) for line in self.read_lines()]
        return [parse(line) if parse else parse_values(line, sep) for line in lines]

    def read_blocks(
        self,
        sep: str | None = None,
        parse: Callable | None = None,
        trim: str | list | None = None,
    ) -> list:
        lines = [clean(line, trim) for line in self.read_lines()]
        blocks = []
        block = []
        for line in lines:
            if not line:
                blocks.append(block)
                block = []
            else:
                block.append(parse(line) if parse else parse_values(line, sep))
        blocks.append(block)
        return blocks


def get_filename(day: int, name: str) -> str:
    return f"day_{day:02d}/{name}.txt"


def run(day: int, sample: bool, test: bool) -> None:
    print(f"Day {day:02d}")
    day_module = importlib.import_module(f"day_{day:02d}")
    if sample:
        print("Run sample")
        with open(get_filename(day, "sample")) as f:
            day_module.solve(Reader(f))
    if test:
        print("Run test")
        with open(get_filename(day, "test")) as f:
            day_module.solve(Reader(f))


def measure(name: str, f: Callable) -> Any:
    start = time.time()
    result = f()
    print(name, "time took", time.time() - start)
    return result


def clean(line: str, trim: str | list | None) -> str:
    if not trim:
        return line
    if isinstance(trim, str):
        return line.replace(trim, " ")
    else:
        for t in trim:
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
