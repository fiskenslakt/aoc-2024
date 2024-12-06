from aocd import data

guard_map = {}
new_direction = {"^": ">", ">": "v", "v": "<", "<": "^"}

for y, row in enumerate(data.splitlines()):
    for x, col in enumerate(row):
        guard_map[(x, y)] = col

        if col in "<>^v":
            sx, sy = x, y
            starting_direction = col

visited = set()
x, y = sx, sy
direction = starting_direction
while True:
    if direction == "^":
        nx, ny = x, y - 1
    elif direction == "v":
        nx, ny = x, y + 1
    elif direction == "<":
        nx, ny = x - 1, y
    elif direction == ">":
        nx, ny = x + 1, y

    if (nx, ny) not in guard_map:
        break

    if guard_map[(nx, ny)] in ".<>^v":
        visited.add((nx, ny))
        x, y = nx, ny
    elif guard_map[(nx, ny)] == "#":
        direction = new_direction[direction]

positions = 0
for ox, oy in visited:
    if (ox, oy) == (sx, sy):
        continue

    loop = set()

    guard_map[(ox, oy)] = "#"

    x, y = sx, sy
    direction = starting_direction
    loop.add((x, y, direction))
    while True:
        if direction == "^":
            nx, ny = x, y - 1
        elif direction == "v":
            nx, ny = x, y + 1
        elif direction == "<":
            nx, ny = x - 1, y
        elif direction == ">":
            nx, ny = x + 1, y

        if (nx, ny) not in guard_map:
            break

        if guard_map[(nx, ny)] in ".<>^v":
            if (nx, ny, direction) in loop:
                positions += 1
                break
            loop.add((nx, ny, direction))
            x, y = nx, ny
        elif guard_map[(nx, ny)] == "#":
            direction = new_direction[direction]
            if (nx, ny, direction) in loop:
                positions += 1
                break
            loop.add((nx, ny, direction))

    # reset spot to empty
    guard_map[(ox, oy)] = "."

print("Part 1:", len(visited))
print("Part 2:", positions)
