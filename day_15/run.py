from itertools import count, dropwhile, takewhile
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
    if replacements:
        new_lines = []
        for line in lines:
            for old, new in replacements:
                line = line.replace(old, new)
            new_lines.append(line)
        lines = new_lines
    grid_lines: list[str] = list(takewhile(lambda l: l != "", lines))
    move_lines = lines[len(grid_lines) + 1:]
    grid = {V(x, y): grid_lines[x][y] for x, y, v in helpers.cells(grid_lines)}
    n, m = len(grid_lines), len(grid_lines[0])
    moves = "".join((m for m in move_lines))
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


def calc(grid, moves, n, m):
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
    grid, moves, n, m = parse(lines)
    print(calc(grid, moves, n, m))

    print("Part Two")
    grid, moves, n, m = parse(lines, replacements=[("#", "##"), ("O", "[]"), (".", ".."), ("@", "@.")])
    print(calc(grid, moves, n, m))
