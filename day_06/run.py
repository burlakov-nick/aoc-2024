import aoc
from iter import iter_grid
from vec import V


def solve(r: aoc.Reader) -> None:
    grid, n, m = r.read_grid_dict()
    start = next(v for v in iter_grid(n, m) if grid[v] == "^")
    directions = [V(-1, 0), V(0, 1), V(1, 0), V(0, -1)]

    def walk(pos, dir, visited):
        while 0 <= pos.x < n and 0 <= pos.y < m:
            if (pos, dir) in visited:
                return "LOOP"
            visited.add((pos, dir))
            nxt = pos + directions[dir]
            if grid.get(nxt) == "#":
                dir = (dir + 1) % 4
            else:
                pos = nxt
        return visited

    print("Part One")
    visited = walk(start, 0, set())
    visited = {v for v, dir in visited}
    print(len(visited))

    print("Part Two")
    result = 0
    for v in iter_grid(n, m):
        if grid[v] == "." and v in visited:
            grid[v] = "#"
            if walk(start, 0, set()) == "LOOP":
                result += 1
            grid[v] = "."
    print(result)
