import aoc


def solve(r: aoc.Reader) -> None:
    grid, n, m = r.read_grid_dict_v()
    start = next(k for k, v in grid.items() if v == "S")
    end = next(k for k, v in grid.items() if v == "E")

    def get_min_dists(s, max_steps = 1000000000000, ignore_walls = False):
        queue = [s]
        dist = {s: 0}
        ptr = 0
        while ptr < len(queue):
            p = queue[ptr]
            ptr += 1
            if dist[p] == max_steps:
                continue
            for to in p.neighbors_4_in_box(n, m):
                if (ignore_walls or grid[to] != "#") and to not in dist:
                    queue.append(to)
                    dist[to] = dist[p] + 1
        return dist

    dist_1 = get_min_dists(start)
    dist_2 = get_min_dists(end)
    no_cheats = dist_1[end]

    def get_cheats(max_cheat: int):
        for p1 in dist_1.keys():
            for p2, d in get_min_dists(p1, max_cheat, ignore_walls=True).items():
                if p2 not in dist_2:
                    continue
                yield no_cheats - (dist_1[p1] + dist_2[p2] + d)

    print("Part One")
    print(sum(1 for x in get_cheats(max_cheat=2) if x >= 100))

    print("Part Two")
    print(sum(1 for x in get_cheats(max_cheat=20) if x >= 100))
