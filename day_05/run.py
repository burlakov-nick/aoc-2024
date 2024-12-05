import aoc
from functools import cmp_to_key


def solve(r: aoc.Reader) -> None:
    orders, seqs = r.read_blocks(to_remove=["|", ","])
    part_1, part_2 = 0, 0
    cmp = {
        **{(x, y): -1 for x, y in orders},
        **{(y, x): 1 for x, y in orders},
    }
    for seq in seqs:
        seq2 = sorted(seq, key=cmp_to_key(lambda x, y: cmp[x, y]))
        if seq == seq2:
            part_1 += seq[len(seq) // 2]
        else:
            part_2 += seq2[len(seq) // 2]

    print("Part One")
    print(part_1)
    print("Part Two")
    print(part_2)
