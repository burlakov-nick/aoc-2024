import networkx

import aoc
from helpers import flatten


def solve(r: aoc.Reader) -> None:
    edges = [tuple(x.split("-")) for x in r.read_lines()]
    nodes = list(set(flatten(edges)))

    G = networkx.Graph()
    G.add_edges_from(edges)

    print("Part One")

    result = 0
    for clique in networkx.algorithms.clique.enumerate_all_cliques(G):
        if len(clique) == 3 and any(x.startswith("t") for x in clique):
            result += 1
    print(result)

    print("Part Two")

    max_clique = max(len(c) for c in networkx.find_cliques(G))

    for clique in networkx.algorithms.clique.enumerate_all_cliques(G):
        if len(clique) == max_clique:
            print(",".join(sorted(clique)))
