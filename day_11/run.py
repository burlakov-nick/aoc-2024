import functools
import aoc


@functools.cache
def calc(x, n):
    if n == 0:
        return 1

    if x == 0:
        return calc(1, n - 1)

    s = str(x)
    if len(s) % 2 == 0:
        left, right = int(s[:len(s) // 2]), int(s[len(s) // 2:])
        return calc(left, n - 1) + calc(right, n - 1)

    return calc(x * 2024, n - 1)


def solve(r: aoc.Reader) -> None:
    xs = r.read()[0]

    print("Part One")
    print(sum(calc(x, 25) for x in xs))

    print("Part Two")
    print(sum(calc(x, 75) for x in xs))
