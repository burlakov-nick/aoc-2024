import networkx
from networkx.algorithms.clique import enumerate_all_cliques, find_cliques

import aoc


def solve(r: aoc.Reader) -> None:
    edges = [tuple(x.split("-")) for x in r.read_lines()]

    graph = networkx.Graph()
    graph.add_edges_from(edges)

    print("Part One")
    print(sum(
        1 for clique in enumerate_all_cliques(graph)
        if len(clique) == 3 and any(x.startswith("t") for x in clique)
    ))

    print("Part Two")
    max_clique = max(len(c) for c in find_cliques(graph))
    for clique in enumerate_all_cliques(graph):
        if len(clique) == max_clique:
            print(",".join(sorted(clique)))
