from functools import cache

from aocd import data


@cache
def dfs(design):
    if not design:
        return 1

    possible = 0

    for i in range(len(design), 0, -1):
        stripes = design[:i]

        if stripes in towels:
            possible += dfs(design[i:])

    return possible


towels_raw, designs = data.split("\n\n")
towels = set(towels_raw.split(", "))

valid = 0
total_possible = 0
for design in designs.splitlines():
    possible = dfs(design)
    total_possible += possible
    if possible > 0:
        valid += 1

print("Part 1:", valid)
print("Part 2:", total_possible)
