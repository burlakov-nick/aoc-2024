from functools import cache
import aoc


def solve(r: aoc.Reader) -> None:
    towels, _, *patterns = r.read_lines()
    towels = towels.split(", ")

    @cache
    def calc(pattern, prefix):
        if prefix == len(pattern):
            return 1

        return sum(
            calc(pattern, prefix + len(towel))
            for towel in towels
            if towel == pattern[prefix:prefix + len(towel)]
        )

    print("Part One")
    print(sum(1 for pattern in patterns if calc(pattern, 0) > 0))

    print("Part Two")
    print(sum(calc(pattern, 0) for pattern in patterns))
