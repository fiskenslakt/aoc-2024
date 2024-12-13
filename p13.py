import re
from functools import cache

from aocd import data, submit

# tokens needed to press
A_BUTTON_PRICE = 3
B_BUTTON_PRICE = 1



# data = """Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176

# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450

# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279"""


@cache
def dfs(ax, ay, bx, by, px, py, tokens, x, y, a_presses, b_presses):
    if x == px and y == py:
        return tokens
    elif x > px or y > py:
        return float("inf")

    a_press = dfs(ax, ay, bx, by, px, py, tokens + A_BUTTON_PRICE, x + ax, y + ay, a_presses + 1, b_presses)
    b_press = dfs(ax, ay, bx, by, px, py, tokens + B_BUTTON_PRICE, x + bx, y + by, a_presses, b_presses + 1)

    return min(a_press, b_press)


total_tokens = 0
# import pudb;pu.db
for claw_machine in data.split("\n\n"):
    machine = {}
    machine["A"] = re.search(r"Button A: X\+(\d+), Y\+(\d+)", claw_machine).groups()
    machine["B"] = re.search(r"Button B: X\+(\d+), Y\+(\d+)", claw_machine).groups()
    machine["prize"] = re.search(r"Prize: X=(\d+), Y=(\d+)", claw_machine).groups()

    ax = int(machine["A"][0])
    ay = int(machine["A"][1])
    bx = int(machine["B"][0])
    by = int(machine["B"][1])
    px = int(machine["prize"][0])
    py = int(machine["prize"][1])

    tokens = dfs(ax, ay, bx, by, px, py, 0, 0, 0, 0, 0)
    if isinstance(tokens, int):
        total_tokens += tokens

submit(total_tokens)
