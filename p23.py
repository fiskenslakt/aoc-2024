from collections import defaultdict

from aocd import data


def bron_kerbosch(clique, potential_conns, excluded):
    if not potential_conns and not excluded:
        yield clique

    while potential_conns:
        pc = potential_conns.pop()
        yield from bron_kerbosch(
            clique | {pc},
            potential_conns & graph[pc],
            excluded & graph[pc]
        )
        excluded.add(pc)


graph = defaultdict(set)
distinct_computers = set()
for conn in data.splitlines():
    pc1, pc2 = conn.split("-")
    distinct_computers.add(pc1)
    distinct_computers.add(pc2)
    graph[pc1].add(pc2)
    graph[pc2].add(pc1)

t_computers = set()
for pc1, connections in graph.items():
    if pc1.startswith("t"):
        for pc2 in connections:
            for pc3 in graph[pc2]:
                if pc1 in graph[pc3]:
                    t_computers.add(frozenset((pc1, pc2, pc3)))

print("Part 1:", len(t_computers))

LAN_party = max(bron_kerbosch(set(), distinct_computers, set()), key=len)
print("Part 2:", ",".join(sorted(LAN_party)))
