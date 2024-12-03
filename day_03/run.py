import aoc
import re


def solve(r: aoc.Reader) -> None:
    lines = r.read_lines()

    print("Part One")
    res = 0
    for line in lines:
        for x, y in re.findall(r"mul\((\d+),(\d+)\)", line):
            res += int(x) * int(y)
    print(res)

    print("Part Two")
    res, enabled = 0, True
    for line in lines:
        for x, y, do, dont in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", line):
            if do:
                enabled = True
            elif dont:
                enabled = False
            elif enabled:
                res += int(x) * int(y)
    print(res)
