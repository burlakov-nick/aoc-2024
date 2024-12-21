import aoc
from vec import V


def solve(r: aoc.Reader) -> None:
    [walls_count], [n, m], *falling = r.read(aoc.parse_ints)
    falling = [V(x, y) for x, y in falling]

    def bfs(nanosecs):
        walls = set(falling[:nanosecs])
        queue = [V(0, 0)]
        dist = {V(0, 0): 0}
        ptr = 0
        while ptr < len(queue):
            p = queue[ptr]
            ptr += 1
            for to in p.neighbors_4_in_box(n, m):
                if to not in walls and to not in dist:
                    queue.append(to)
                    dist[to] = dist[p] + 1
        return dist.get(V(n - 1, m - 1))

    print("Part One")
    print(bfs(walls_count))

    print("Part Two")
    left, right = 0, len(falling)
    while right - left > 1:
        mid = (left + right) >> 1
        if bfs(mid) is None:
            right = mid
        else:
            left = mid
    print(f"{falling[right - 1].x},{falling[right - 1].y}")
