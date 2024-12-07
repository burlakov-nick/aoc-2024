import aoc
from itertools import product
from operator import add, mul


def can_solve(line, allowed_ops):
    expected, *numbers = line
    for operators in product(allowed_ops, repeat=len(numbers) - 1):
        actual = numbers[0]
        for arg, operator in zip(numbers[1:], operators):
            actual = operator(actual, arg)
        if actual == expected:
            return actual
    return False


def solve(r: aoc.Reader) -> None:
    lines = r.read(remove=":")
    print("Part One")
    print(sum(line[0] for line in lines if can_solve(line, [add, mul])))
    print("Part Two")
    concat = lambda x, y: int(str(x) + str(y))
    print(sum(line[0] for line in lines if can_solve(line, [add, mul, concat])))
