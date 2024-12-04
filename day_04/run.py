import aoc
from vec import V


DIAGONAL_DIRECTIONS = [V(-1, -1), V(-1, 1), V(1, -1), V(1, 1)]
DIRECTIONS = [V(0, -1), V(0, 1), V(-1, 0), V(1, 0), *DIAGONAL_DIRECTIONS]


def solve(r: aoc.Reader) -> None:
    grid, n1, n2 = r.read_grid_dict()

    print("Part One")

    def match(word: str, start: V, dir: V) -> bool:
        return all(grid.get(start + dir * i) == ch for i, ch in enumerate(word))

    result = sum(
        1
        for dir in DIRECTIONS
        for x in grid.keys()
        if match("XMAS", x, dir)
    )
    print(result)

    print("Part Two")

    def match_mas(a: V) -> bool:
        for dir in DIAGONAL_DIRECTIONS:
            for dir2 in DIAGONAL_DIRECTIONS:
                if dir != dir2 and dir != -dir2:
                    if match("MAS", a - dir, dir) and match("MAS", a - dir2, dir2):
                        return True
        return False

    result = sum(1 for a in grid.keys() if match_mas(a))
    print(result)
