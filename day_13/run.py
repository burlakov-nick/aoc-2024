import re
import aoc
from helpers import range_2d


def intersect(a1, b1, c1, a2, b2, c2):
    d = a1 * b2 - b1 * a2
    if d == 0:
        return 0, 0
    x = -(c1 * b2 - b1 * c2) // d
    y = -(a1 * c2 - c1 * a2) // d
    if x * a1 + y * b1 + c1 == 0 and x * a2 + y * b2 + c2 == 0:
        return x, y
    return 0, 0


def solve(r: aoc.Reader) -> None:
    test = r.read_blocks(aoc.parse_ints)

    print("Part One")
    res = 0
    for (ax, ay), (bx, by), (cx, cy) in test:
        i, j = intersect(ax, bx, -cx, ay, by, -cy)
        res += i * 3 + j
    print(res)

    print("Part Two")
    res = 0
    for (ax, ay), (bx, by), (cx, cy) in test:
        cx += 10000000000000
        cy += 10000000000000
        i, j = intersect(ax, bx, -cx, ay, by, -cy)
        res += i * 3 + j
    print(res)
