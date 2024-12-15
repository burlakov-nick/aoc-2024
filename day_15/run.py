import aoc
import helpers
from vec import V


DIRECTIONS = {
    '^': V(-1, 0),
    'v': V(1, 0),
    '>': V(0, 1),
    '<': V(0, -1)
}


def parse(lines: list[str], replacements = None):
    empty_index = lines.index("")
    grid, moves = lines[:empty_index], lines[empty_index + 1:]
    n, m = len(grid), len(grid[0])
    grid = {V(x, y): grid[x][y] for x, y in helpers.range_2d(n, m)}
    moves = "".join((m for m in moves))
    return grid, moves, n, m


def get_boxes_to_move(grid, p, dir, visited):
    if grid[p] not in ("O", "[", "]") or p in visited:
        return
    visited.add(p)
    yield p
    yield from get_boxes_to_move(grid, p + dir, dir, visited)
    if grid[p] == "[":
        yield from get_boxes_to_move(grid, p + V(0, 1), dir, visited)
    if grid[p] == "]":
        yield from get_boxes_to_move(grid, p + V(0, -1), dir, visited)


def try_move(grid, to_move, dir) -> bool:
    can_move = all(grid[p + dir] != "#" for p in to_move)
    if not can_move:
        return False

    old = {p: grid[p] for p in to_move}
    for p in to_move:
        grid[p] = "."
    for p in to_move:
        grid[p + dir] = old[p]
    return True


def calc(lines):
    grid, moves, n, m = parse(lines)
    robot = next(p for p in grid.keys() if grid[p] == "@")
    for move in moves:
        dir = DIRECTIONS[move]
        to_move = {robot, *get_boxes_to_move(grid, robot + dir, dir, visited=set())}
        if try_move(grid, to_move, dir):
            robot = robot + dir
    return sum(p.x * 100 + p.y for p in grid.keys() if grid[p] in ("O", "["))


def solve(r: aoc.Reader) -> None:
    lines = r.read_lines()

    print("Part One")
    print(calc(lines))

    print("Part Two")
    lines = [l.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.") for l in lines]
    print(calc(lines))
