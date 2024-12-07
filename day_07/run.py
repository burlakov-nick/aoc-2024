import aoc
from itertools import product


def can_solve(line, allowed_operations):
    expected, *numbers = line
    for operators in product(allowed_operations, repeat=len(numbers) - 1):
        actual = numbers[0]
        for arg, operator in zip(numbers[1:], operators):
            if operator == "*":
                actual *= arg
            elif operator == "+":
                actual += arg
            else:
                actual = int(str(actual) + str(arg))
        if actual == expected:
            return True
    return False


def solve(r: aoc.Reader) -> None:
    lines = r.read(remove=":")
    print("Part One")
    print(sum(line[0] for line in lines if can_solve(line, "+*")))
    print("Part Two")
    print(sum(line[0] for line in lines if can_solve(line, "+*|")))
