import aoc
from grid import range_2d


def solve(r: aoc.Reader) -> None:
    grid, n, m = r.read_grid_str()

    sx, sy = next((x, y) for x, y in range_2d(n, m) if grid[x][y] == "^")
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def walk(x, y, dir, visited):
        while 0 <= x < n and 0 <= y < m:
            if (x, y, dir) in visited:
                return "LOOP"
            visited.add((x, y, dir))
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "#":
                dir = (dir + 1) % 4
            else:
                x, y = nx, ny
        return visited

    print("Part One")
    visited = walk(sx, sy, 0, set())
    visited = {(x, y) for x, y, dir in visited}
    print(len(visited))

    print("Part Two")
    result = 0
    for x, y in range_2d(n, m):
        if grid[x][y] == "." and (x, y) in visited:
            grid[x][y] = "#"
            if walk(sx, sy, 0, set()) == "LOOP":
                result += 1
            grid[x][y] = "."
    print(result)
