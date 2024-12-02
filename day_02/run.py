import aoc
from itertools import pairwise

def decreasing(xs):
    return all(1 <= x - y <= 3 for x, y in pairwise(xs))

def increasing(xs):
    return all(1 <= y - x <= 3 for x, y in pairwise(xs))

def safe(xs):
    return decreasing(xs) or increasing(xs)

def safe2(xs):
    return any(safe(xs[:drop] + xs[drop + 1:]) for drop in range(len(xs)))

def solve(r: aoc.Reader) -> None:
    lines = r.read()
    print("Part One")
    print(sum(1 for xs in lines if safe(xs)))

    print("Part Two")
    print(sum(1 for xs in lines if safe2(xs)))
