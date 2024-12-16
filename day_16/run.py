from collections import defaultdict, namedtuple
from sortedcontainers.sorteddict import SortedSet
import aoc
from vec import V


INF = 1000000000000000000000000


def solve(r: aoc.Reader) -> None:
    grid, n, m = r.read_grid_dict_v()

    print("Part One")
    start = next(p for p in grid.keys() if grid[p] == "S")
    end = next(p for p in grid.keys() if grid[p] == "E")
    dist = defaultdict(lambda: INF)
    queue = SortedSet()
    prev = defaultdict(list)

    def update(s: tuple[V, V], new_dist: int, p: tuple[V, V] | None):
        if dist[s] > new_dist:
            if queue.count((dist[s], s)):
                queue.remove((dist[s], s))
            prev[s] = [p]
            dist[s] = new_dist
            queue.add((dist[s], s))
        elif dist[s] == new_dist:
            prev[s].append(p)

    update((start, V(0, 1)), 0, None)

    while len(queue) > 0:
        cur_dist, (pos, dir) = queue.pop(0)

        if grid[pos + dir] != "#":
            next_state = (pos + dir, dir)
            update(next_state, cur_dist + 1, (pos, dir))

        next_state = (pos, dir.clockwise())
        update(next_state, cur_dist + 1000, (pos, dir))

        next_state = (pos, dir.counter_clockwise())
        update(next_state, cur_dist + 1000, (pos, dir))

    shortest_dist = min(d for (pos, _), d in dist.items() if pos == end)
    print(shortest_dist)

    print("Part Two")

    visited = set()
    def dfs(p):
        if not p or p in visited:
            return
        visited.add(p)
        for next in prev[p]:
            dfs(next)

    for (pos, dir) in dist.keys():
        if pos == end and dist[(pos, dir)] == shortest_dist:
            dfs((pos, dir))

    print(len({pos for pos, dir in visited}))
