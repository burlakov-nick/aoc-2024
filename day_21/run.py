from collections import defaultdict

from sortedcontainers import SortedSet

import aoc
import helpers
from vec import V

INF = 1000000000000000000000000000000000000000
NUMERIC_LINES = ["789", "456", "123", " 0A"]
DIRECTIONAL_LINES = [" ^A", "<v>"]
NUMERIC_GRID = {V(x, y): v for x, y, v in helpers.cells(NUMERIC_LINES) if v != " "}
DIRECTIONAL_GRID = {V(x, y): v for x, y, v in helpers.cells(DIRECTIONAL_LINES) if v != " "}
DIRECTIONAL_GRID_KEY_TO_POSITION = {v: V(x, y) for x, y, v in helpers.cells(DIRECTIONAL_LINES) if v != " "}
DIRECTIONS = {"^": V(-1, 0), "<": V(0, -1), ">": V(0, 1), "v": V(1, 0)}
NUMERIC_START = V(3, 2)
DIRECTIONAL_KEYS = "A<^v>"


def dijkstra(start, end, get_next):
    dist = defaultdict(lambda: INF)
    queue = SortedSet()

    def update(s: tuple, new_dist: int):
        if dist[s] > new_dist:
            if queue.count((dist[s], s)):
                queue.remove((dist[s], s))
            dist[s] = new_dist
            queue.add((dist[s], s))

    update(start, 0)

    while len(queue) > 0:
        cur_dist, state = queue.pop(0)
        if state == end:
            break
        for new_state, cost in get_next(state):
            update(new_state, cur_dist + cost)

    return dist[end]


def add_one_directional_keypad(cost: dict) -> dict:
    new_cost = defaultdict(lambda: INF)

    def get_next(p):
        directional_key, previous_direction = p
        for next_direction in "^v<>":
            next_directional_key = DIRECTIONAL_GRID_KEY_TO_POSITION[directional_key] + DIRECTIONS[next_direction]
            if next_directional_key in DIRECTIONAL_GRID:
                yield (DIRECTIONAL_GRID[next_directional_key], next_direction), cost[previous_direction, next_direction]
        yield (directional_key, "A"), cost[previous_direction, "A"]

    for i in DIRECTIONAL_KEYS:
        for j in DIRECTIONAL_KEYS:
            new_cost[i, j] = dijkstra((i, "A"), (j, "A"), get_next) if i != j else 1

    return new_cost


def get_shortest_path(line, cost):
    def get_next(state):
        prefix, prev_directional, numeric_position = state

        if line[prefix] == NUMERIC_GRID[numeric_position]:
            yield (prefix + 1, "A", numeric_position), cost[prev_directional, "A"]

        for next_directional in "^v<>":
            numeric_direction = DIRECTIONS[next_directional]
            if numeric_position + numeric_direction in NUMERIC_GRID:
                yield (prefix, next_directional, numeric_position + numeric_direction), cost[prev_directional, next_directional]

    start = (0, "A", NUMERIC_START)
    end = (len(line), "A", NUMERIC_START)
    return dijkstra(start, end, get_next)


def solve(r: aoc.Reader) -> None:
    lines = r.read_lines()

    print("Part One")

    cost = defaultdict(lambda: INF)
    for p1, prev_action in DIRECTIONAL_GRID.items():
        for p2, next_action in DIRECTIONAL_GRID.items():
            cost[prev_action, next_action] = 1 + (p1 - p2).dist()

    for _ in range(1):
        cost = add_one_directional_keypad(cost)
    print(sum(get_shortest_path(line, cost) * aoc.parse_ints(line)[0] for line in lines))

    print("Part Two")

    for _ in range(23):
        cost = add_one_directional_keypad(cost)
    print(sum(get_shortest_path(line, cost) * aoc.parse_ints(line)[0] for line in lines))
