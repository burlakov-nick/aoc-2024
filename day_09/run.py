import aoc
from sortedcollections import SortedSet


def part_1(line):
    xs = []
    for i, length in enumerate(line):
        id = i // 2 if i % 2 == 0 else None
        for _ in range(int(length)):
            xs.append(id)

    left, right = 0, len(xs) - 1
    while True:
        while xs[left] is not None and left < right:
            left += 1
        while xs[right] is None and left < right:
            right -= 1
        if left == right:
            break
        xs[left] = xs[right]
        xs[right] = None

    return sum(i * val for i, val in enumerate(xs) if val is not None)


def part_2(line) -> int:
    free, busy = SortedSet(), []
    start = 0
    for i, length in enumerate(line):
        if i % 2 == 0:
            id = i // 2
            busy.append((start, int(length), id))
        else:
            free.add((start, int(length)))
        start += int(length)

    new_busy = []
    for busy_start, busy_length, id in reversed(busy):
        free_start, free_length = next(((s, l) for s, l in free if l >= busy_length and s < busy_start), (None, None))
        if free_start is None:
            new_busy.append((busy_start, busy_length, id))
            continue
        new_busy.append((free_start, busy_length, id))
        free.remove((free_start, free_length))
        if free_length > busy_length:
            free.add((free_start + busy_length, free_length - busy_length))

    res = 0
    for start, length, id in new_busy:
        for i in range(start, start + length):
            res += i * id
    return res


def solve(r: aoc.Reader) -> None:
    line = r.read_lines()[0]
    print("Part One")
    print(part_1(line))
    print("Part Two")
    print(part_2(line))
