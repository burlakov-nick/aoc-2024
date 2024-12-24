import operator
from functools import cache
import aoc

operators = {"AND": operator.and_, "XOR": operator.xor, "OR": operator.or_}


def validate_gates(x_gates, y_gates, z_gates, gates):
    def find_gate(left, op, right):
        result = next((k for k, v in gates.items() if v == (left, op, right) or v == (right, op, left)), None)
        if not result:
            raise RuntimeError(f"Not found gate for {left} {op} {right}")
        return result

    carrying_gates = []
    for i in range(len(z_gates) - 1):
        x_gate, y_gate, z_gate = x_gates[i], y_gates[i], z_gates[i]
        left, op, right = gates[z_gate]

        if i == 0:
            assert (left, op, right) == (x_gate, "XOR", y_gate)
            carrying_gates.append(find_gate(x_gate, "AND", y_gate))
            continue

        assert op == "XOR"

        xor_gate = find_gate(x_gate, "XOR", y_gate)
        and_gate = find_gate(x_gate, "AND", y_gate)

        carry_help_gate = find_gate(xor_gate, "AND", carrying_gates[i - 1])
        carrying_gate = find_gate(and_gate, "OR", carry_help_gate)

        result_gate = find_gate(xor_gate, "XOR", carrying_gates[i - 1])
        assert result_gate == z_gate

        carrying_gates.append(carrying_gate)


def solve(r: aoc.Reader) -> None:
    inputs, gates = r.read_blocks(remove=[": ", "->", " "])

    inputs = {input: value for input, value in inputs}
    gates = {output: (min(left, right), op, max(left, right)) for left, op, right, output in gates}
    x_gates = sorted([x for x in inputs.keys() if x.startswith("x")])
    y_gates = sorted([x for x in inputs.keys() if x.startswith("y")])
    z_gates = sorted([x for x in gates.keys() if x.startswith("z")])

    print("Part One")

    @cache
    def calc(x):
        if x in inputs:
            return inputs[x]
        left, op, right = gates[x]
        res = operators[op](calc(left), calc(right))
        # this toposort print is useful for second part
        # print(left, op, right, "->", x)
        return res

    print(sum((calc(gate) << i) for i, gate in enumerate(z_gates)))

    print("Part Two")

    def swap(left, right):
        left_old, right_old = gates[left], gates[right]
        gates[right] = left_old
        gates[left] = right_old

    # just look at toposort and run validation, and things will make sense immediately
    swap("cnk", "qwf")
    swap("z14", "vhm")
    swap("z27", "mps")
    swap("z39", "msq")
    print(",".join(sorted(["cnk", "qwf", "z14", "vhm", "z27", "mps", "z39", "msq"])))

    validate_gates(x_gates, y_gates, z_gates, gates)
