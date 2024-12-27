import aoc
from helpers import transpose, count


def solve(r: aoc.Reader) -> None:
    blocks = r.read_blocks(lambda x: x)
    print("Part One")
    to_heights = lambda block: [count(row, "#") - 1 for row in transpose(block)]
    locks = [to_heights(block) for block in blocks if block[0] == "#####"]
    keys = [to_heights(block) for block in blocks if block[0] == "....."]
    print(sum(1 for lock in locks for key in keys if all(x + y <= 5 for x, y in zip(lock, key))))
