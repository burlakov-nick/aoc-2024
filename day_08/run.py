from itertools import combinations
import aoc
from iter import group_by


def solve(r: aoc.Reader) -> None:
    grid, n, m = r.read_grid_dict_v()
    grid = {p: v for p, v in grid.items() if v != "."}

    def get_antinodes_1(left, right):
        p1 = left * 2 - right
        if p1.in_box(n, m):
            yield p1
        p2 = right * 2 - left
        if p2.in_box(n, m):
            yield p2

        yield left + (left - right)
        yield right + (right - left)

    def get_antinodes_2(left, right):
        p, step = left, left - right
        while p.in_box(n, m):
            yield p
            p += step
        p, step = right, right - left
        while p.in_box(n, m):
            yield p
            p += step

    def count_antinodes(get_antinodes):
        antinodes = set()
        for positions in group_by(grid.keys(), lambda p: grid[p]).values():
            for left, right in combinations(positions, 2):
                antinodes |= set(get_antinodes(left, right))
        return len(antinodes)

    print("Part One")
    print(count_antinodes(get_antinodes_1))

    print("Part Two")
    print(count_antinodes(get_antinodes_2))
