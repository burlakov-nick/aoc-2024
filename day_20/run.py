import aoc


def solve(r: aoc.Reader) -> None:
    grid, n, m = r.read_grid_dict_v()
    start = next(k for k, v in grid.items() if v == "S")

    queue = [start]
    visited = {start}
    ptr = 0
    while ptr < len(queue):
        p = queue[ptr]
        ptr += 1
        for to in p.neighbors_4_in_box(n, m):
            if grid[to] != "#" and to not in visited:
                queue.append(to)
                visited.add(to)

    def get_cheats(max_cheat: int):
        for i in range(len(queue)):
            for j in range(len(queue)):
                dist = (queue[i] - queue[j]).dist()
                if dist <= max_cheat:
                    yield j - i - dist

    print("Part One")
    print(sum(1 for x in get_cheats(max_cheat=2) if x >= 100))

    print("Part Two")
    print(sum(1 for x in get_cheats(max_cheat=20) if x >= 100))
