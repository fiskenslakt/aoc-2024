from functools import cache
from itertools import pairwise

from aocd import data


def best_paths(start, end, keypad_type):
    if keypad_type == "numerical":
        keypad = numeric_keypad
        locations = numeric_key_locations

    elif keypad_type == "directional":
        keypad = directional_keypad
        locations = direction_key_locations

    sx, sy = locations[start]
    ex, ey = locations[end]

    dx = ex - sx
    dy = ey - sy

    paths = []
    if dx == dy == 0:
        return ["A"]

    if (ex, sy) in keypad:
        paths.append("<>"[dx > 0] * abs(dx) + "^v"[dy > 0] * abs(dy) + "A")
    if (sx, ey) in keypad:
        paths.append("^v"[dy > 0] * abs(dy) + "<>"[dx > 0] * abs(dx) + "A")

    return paths


@cache
def cost(path: str, robot: int, keypad_type: str):
    all_paths = (best_paths(a, b, keypad_type) for a, b in pairwise("A" + path))

    if robot == 0:
        return sum(len(paths[0]) for paths in all_paths)

    costs = []
    for paths in all_paths:
        costs.append(min(cost(path, robot - 1, "directional") for path in paths))

    return sum(costs)


numeric_keypad = {
    (0, 0): "7", (1, 0): "8", (2, 0): "9",
    (0, 1): "4", (1, 1): "5", (2, 1): "6",
    (0, 2): "1", (1, 2): "2", (2, 2): "3",
                 (1, 3): "0", (2, 3): "A",
}

numeric_key_locations = {v: k for k,v in numeric_keypad.items()}

directional_keypad = {
                 (1, 0): "^", (2, 0): "A",
    (0, 1): "<", (1, 1): "v", (2, 1): ">",
}

direction_key_locations = {v: k for k, v in directional_keypad.items()}

directions = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1),
}

complexity_sum = 0
for code in data.splitlines():
    complexity_sum += int(code[:-1]) * cost(code, 2, "numerical")

print("Part 1:", complexity_sum)

complexity_sum = 0
for code in data.splitlines():
    complexity_sum += int(code[:-1]) * cost(code, 25, "numerical")

print("Part 2:", complexity_sum)
