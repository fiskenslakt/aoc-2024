import re
from functools import cache

from aocd import data


@cache
def dfs(wire):
    if wire in graph:
        input_a, gate, input_b = graph[wire]
    elif wire in initial_wires:
        return initial_wires[wire]

    if gate == "AND":
        return dfs(input_a) & dfs(input_b)
    elif gate == "OR":
        return dfs(input_a) | dfs(input_b)
    elif gate == "XOR":
        return dfs(input_a) ^ dfs(input_b)


p = re.compile(r"(\w+) (AND|OR|XOR) (\w+) -> (\w+)")

wires, gates = data.split("\n\n")

initial_wires = {}
for wire in wires.splitlines():
    wire_name, value = wire.split(": ")
    initial_wires[wire_name] = int(value)

bits = []
graph = {}
for gate in gates.splitlines():
    m = p.search(gate)
    graph[m[4]] = (m[1], m[2], m[3])
    if m[4].startswith("z"):
        bits.append(m[4])

bits.sort(reverse=True)
binary_number = []
for bit in bits:
    digit = str(dfs(bit))
    binary_number.append(digit)

print("Part 1:", int("".join(binary_number), 2))

incorrect_outputs = []
for output in graph:
    if output.startswith("z") and output != "z45":
        input_a, gate, input_b = graph[output]
        if gate != "XOR":
            incorrect_outputs.append(output)
    elif not output.startswith("z"):
        input_a, gate, input_b = graph[output]
        if input_a[1:] == "00":
            continue
        if input_a[0] not in "xy" and input_b[0] not in "xy":
            if gate == "XOR":
                incorrect_outputs.append(output)
        elif gate == "XOR":
            for gate2 in graph.values():
                if output in gate2 and gate2[1] == "XOR":
                    break
            else:
                incorrect_outputs.append(output)
        elif gate == "AND":
            for gate2 in graph.values():
                if output in gate2 and gate2[1] == "OR":
                    break
            else:
                incorrect_outputs.append(output)

print("Part 2:", ",".join(sorted(incorrect_outputs)))
