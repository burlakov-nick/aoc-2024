import aoc
from iter import freq, transpose


def solve(r: aoc.Reader) -> None:
    xs = transpose(r.read())
    print("Part 1")
    print(sum(abs(x - y) for x, y in zip(sorted(xs[0]), sorted(xs[1]))))

    print("Part 2")
    f = freq(xs[1])
    print(sum(x * f[x] for x in xs[0]))
