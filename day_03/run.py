import aoc
import re


def solve(r: aoc.Reader) -> None:
    line = "".join(r.read_lines())

    print("Part One")
    res = 0
    for x, y in re.findall(r"mul\((\d+),(\d+)\)", line):
        res += int(x) * int(y)
    print(res)

    print("Part Two")
    res, enabled = 0, True
    for x, y, do, dont in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", line):
        if do:
            enabled = True
        elif dont:
            enabled = False
        elif enabled:
            res += int(x) * int(y)
    print(res)
