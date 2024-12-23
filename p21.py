from functools import cache
from itertools import pairwise

from aocd import data, submit

# data = """029A
# 980A
# 179A
# 456A
# 379A"""


def path_efficiency(path):
    efficiency = len(path)  # lower is better
    for b1, b2 in pairwise(path):
        efficiency += b1 != b2

    ax, ay = (2, 0)
    x, y = direction_key_locations[path[-1]]
    dist_from_a = abs(x - ax) + abs(y - ay)
    return efficiency, dist_from_a


@cache
def dfs(start: tuple[int, int], end: str, path: tuple, seen: tuple, keypad_type: str):
    if keypad_type == "numeric":
        keypad = numeric_keypad
    elif keypad_type == "directional":
        keypad = directional_keypad

    if keypad[start] == end:
        return path

    sx, sy = start
    paths = []
    for direction in "<>^v":
        i, j = directions[direction]
        nx, ny = (sx + i, sy + j)
        if (nx, ny) in keypad and (nx, ny) not in seen:
            new_path = dfs((sx + i, sy + j), end, path + (direction,), seen + ((nx,ny),), keypad_type)
            if new_path is not None:
                paths.append(new_path)

    paths.sort(key=path_efficiency)
    if paths:
        return paths[0]


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
    start = (2, 3)
    first_robot = []
    for button in code:
        path = dfs(start, button, (), (start), "numeric")
        start = numeric_key_locations[button]
        first_robot.extend(path)
        first_robot.append("A")
    start = (2, 0)
    second_robot = []
    for button in first_robot:
        path = dfs(start, button, (), (start), "directional")
        start = direction_key_locations[button]
        second_robot.extend(path)
        second_robot.append("A")

    start = (2, 0)
    third_robot = []
    for button in second_robot:
        path = dfs(start, button, (), (start), "directional")
        start = direction_key_locations[button]
        third_robot.extend(path)
        third_robot.append("A")

    complexity_sum += int(code[:-1]) * len(third_robot)

submit(complexity_sum)
