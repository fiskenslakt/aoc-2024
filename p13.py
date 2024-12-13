import re

from aocd import data

# tokens needed to press
A_BUTTON_PRICE = 3
B_BUTTON_PRICE = 1

OFFSET = 10_000_000_000_000

total_tokens = 0
total_tokens_with_offset = 0

for claw_machine in data.split("\n\n"):
    button_a = re.search(r"Button A: X\+(\d+), Y\+(\d+)", claw_machine)
    button_b = re.search(r"Button B: X\+(\d+), Y\+(\d+)", claw_machine)
    prize = re.search(r"Prize: X=(\d+), Y=(\d+)", claw_machine)

    ax = int(button_a[1])
    ay = int(button_a[2])
    bx = int(button_b[1])
    by = int(button_b[2])

    for offset in (0, OFFSET):
        px = int(prize[1]) + offset
        py = int(prize[2]) + offset

        # original equations
        # px = ax * n + bx * m
        # py = ay * n + by * m

        # multiply both equations by button B to eliminate m
        # px * by = ax * n * by + bx * m * by
        # py * bx = ay * n * bx + by * m * bx

        pxby = px * by
        pybx = py * bx
        axby = ax * by
        aybx = ay * bx
        bxby = bx * by

        p = pxby - pybx
        a = axby - aybx

        # solve for n
        n = p / a
        # use n to solve for m
        m = (px - (ax * n)) / bx

        if n.is_integer() and m.is_integer():
            tokens = A_BUTTON_PRICE * int(n) + B_BUTTON_PRICE * int(m)
            if offset == 0:
                total_tokens += tokens
            else:
                total_tokens_with_offset += tokens

print("Part 1:", total_tokens)
print("Part 2:", total_tokens_with_offset)
