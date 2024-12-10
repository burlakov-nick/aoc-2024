import aoc
from vec import V


def solve(r: aoc.Reader) -> None:
    grid, n, m = r.read_grid_dict_v_int()

    def dfs(p: V):
        if grid[p] == 9:
            yield p
        for nxt in p.neighbors_4_in_box(n, m):
            if grid[nxt] == grid[p] + 1:
                yield from dfs(nxt)

    print("Part One")
    print(sum(len(set(dfs(p))) for p, v in grid.items() if v == 0))

    print("Part Two")
    print(sum(len(list(dfs(p))) for p, v in grid.items() if v == 0))
