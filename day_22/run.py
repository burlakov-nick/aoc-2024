from collections import defaultdict

import aoc
from helpers import flatten, last, sliding_window

MOD = (1 << 24) - 1


def get_next(x):
    x = ((x << 6) ^ x) & MOD
    x = ((x >> 5) ^ x) & MOD
    x = ((x << 11) ^ x) & MOD
    return x


def generate(x):
    for _ in range(2000):
        prev = x
        x = get_next(x)
        yield x, x % 10, (x % 10) - (prev % 10)


def get_selling_options(x):
    seen = set()
    for p1, p2, p3, p4 in sliding_window(generate(x), 4):
        price_changes = p1[2], p2[2], p3[2], p4[2]
        cost = p4[1]
        if price_changes in seen:
            continue

        seen.add(price_changes)
        yield price_changes, cost


def solve(r: aoc.Reader) -> None:
    xs = flatten(r.read())

    print("Part One")
    print(sum(last(generate(x))[0] for x in xs))

    print("Part Two")
    result = defaultdict(int)
    for x in xs:
        for price_change, cost in get_selling_options(x):
            result[price_change] += cost
    print(max(result.values()))
