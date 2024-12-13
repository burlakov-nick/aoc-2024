import aoc

INF = 10000000000000


def calc(a1, b1, c1, a2, b2, c2):
    d = a1 * b2 - b1 * a2
    if d == 0:
        return 0
    x = -(c1 * b2 - b1 * c2) // d
    y = -(a1 * c2 - c1 * a2) // d
    if x * a1 + y * b1 + c1 == 0 and x * a2 + y * b2 + c2 == 0:
        return x * 3 + y
    return 0


def solve(r: aoc.Reader) -> None:
    test = r.read_blocks(aoc.parse_ints)

    print("Part One")
    print(sum(calc(ax, bx, -cx, ay, by, -cy) for (ax, ay), (bx, by), (cx, cy) in test))

    print("Part Two")
    print(sum(calc(ax, bx, -cx-INF, ay, by, -cy-INF) for (ax, ay), (bx, by), (cx, cy) in test))
