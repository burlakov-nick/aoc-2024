import aoc
from vec import V, DIRECTIONS_4 as DIRECTIONS


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


def get_side(v, dir, inside, outside, visited):
    if (v, dir) in visited or v + dir not in inside:
        return 0
    visited.add((v, dir))
    for to in v.neighbors_4():
        if to in outside and to + dir in inside:
            get_side(to, dir, inside, outside, visited)
    return 1


def solve(r: aoc.Reader) -> None:
    grid, n, m = r.read_grid_dict_v()

    visited = set()
    regions = [get_region(p, visited, grid) for p in grid.keys() if p not in visited]

    print("Part One")
    print(sum(len(i) * len(o) for i, o in regions))

    print("Part Two")
    part_2 = 0
    for inside, outside in regions:
        visited = set()
        sides = sum(get_side(v, dir, inside, outside, visited) for v in outside for dir in DIRECTIONS)
        part_2 += len(inside) * sides
    print(part_2)
