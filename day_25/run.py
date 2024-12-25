import aoc
from helpers import transpose, count


def solve(r: aoc.Reader) -> None:
    blocks = r.read_blocks(lambda x: x)
    print("Part One")
    print(sum(1 for lock in [[count(row, "#") - 1 for row in transpose(block)] for block in blocks if block[0] == "#####"] for key in [[count(row, "#") - 1 for row in transpose(block)] for block in blocks if block[0] == "....."] if all(x + y <= 5 for x, y in zip(lock, key))))
