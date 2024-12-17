import aoc
from helpers import flatten


def eval(registers, program):
    ptr = 0

    def combo(x):
        if x <= 3:
            return x
        return registers[x - 4]

    outputs = []
    while ptr + 2 <= len(program):
        op, arg = program[ptr], program[ptr + 1]
        match op:
            case 0:
                registers[0] //= 1 << combo(arg)
            case 1:
                registers[1] ^= arg
            case 2:
                registers[1] = combo(arg) % 8
            case 3:
                if registers[0] != 0:
                    ptr = arg - 2
            case 4:
                registers[1] ^= registers[2]
            case 5:
                outputs.append(combo(arg) % 8)
            case 6:
                registers[1] = registers[0] // (1 << combo(arg))
            case 7:
                registers[2] = registers[0] // (1 << combo(arg))
        ptr += 2
    return outputs


def solve(r: aoc.Reader) -> None:
    a, b, c, *program = flatten(r.read(aoc.parse_ints))

    print("Part One")
    print(",".join(str(x) for x in eval([a, b, c], program)))

    print("Part Two")

    def rec(iter, a):
        if iter == len(program):
            return a
        target = program[len(program) - 1 - iter]
        for cur_a in range(8):
            cur_b = cur_a ^ 2
            cur_c = ((a + cur_a) >> cur_b) % 8
            cur_b = (cur_b ^ 7 ^ cur_c) % 8
            if cur_b == target and (found := rec(iter + 1, (a + cur_a) << 3)):
                return found
        return None

    a = rec(0, 0) >> 3
    print(a)
    print(eval([a, b, c], program))
    assert eval([a, b, c], program) == program
