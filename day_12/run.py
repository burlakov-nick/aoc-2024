import aoc
from vec import V

DIRECTIONS = [V(-1, 0), V(0, 1), V(1, 0), V(0, -1)]


def get_region(v, visited, grid):
    if v in visited:
        return [], []
    visited.add(v)
    inside, outside = [v], []
    for to in v.neighbors_4():
        if grid.get(to) == grid[v]:
            i, o = get_region(to, visited, grid)
            inside.extend(i)
            outside.extend(o)
        else:
            outside.append(to)
    return inside, outside


def get_corners(inside, outside):
    for v in inside:
        for i in range(4):
            d1, d2 = DIRECTIONS[i], DIRECTIONS[(i + 1) % 4]
            if (
                v + d1 in outside and v + d2 in outside or
                v + d1 in inside and v + d2 in inside and v + d1 + d2 in outside
            ):
                yield v


def solve(r: aoc.Reader) -> None:
    grid, n, m = r.read_grid_dict_v()

    visited = set()
    regions = [get_region(p, visited, grid) for p in grid.keys() if p not in visited]

    print("Part One")
    print(sum(len(inside) * len(outside) for inside, outside in regions))

    print("Part Two")
    print(sum(len(inside) * len(list(get_corners(inside, outside))) for inside, outside in regions))
