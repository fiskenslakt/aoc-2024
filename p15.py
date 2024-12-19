from collections import deque

from aocd import data


def move_robot(obj, x, y, i, j):
    nx, ny = x + i, y + j
    if warehouse[(nx, ny)] == ".":
        warehouse[(x, y)] = "."
        warehouse[(nx, ny)] = obj
        return True
    elif warehouse[(nx, ny)] == "#":
        return False
    elif warehouse[(nx, ny)] == "O":
        moved = move_robot("O", nx, ny, i, j)
        if moved:
            warehouse[(x, y)] = "."
            warehouse[(nx, ny)] = obj

        return moved


def can_move_up_down(x, y, j):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        if wide_warehouse[(x, y+j)] == "#":
            return False

        if wide_warehouse[(x, y+j)] == "[":
            queue.append((x, y+j))
            queue.append((x+1, y+j))
        elif wide_warehouse[(x, y+j)] == "]":
            queue.append((x, y+j))
            queue.append((x-1, y+j))

    return True


def can_move_left_right(x, y, i):
    x += i
    while wide_warehouse[(x, y)] not in "#.":
        x += i

    return wide_warehouse[(x, y)] == "."


def move_wide_boxes(x, y, i, j):
    nx, ny = x + i, y + j
    if wide_warehouse[(nx, ny)] == ".":
        wide_warehouse[(nx, ny)] = wide_warehouse[(x, y)]
        wide_warehouse[(x, y)] = "."
    elif i:
        move_wide_boxes(nx, ny, i, j)
        wide_warehouse[(nx, ny)] = wide_warehouse[(x, y)]
        wide_warehouse[(x, y)] = "."
    elif wide_warehouse[(nx, ny)] == "[":
        move_wide_boxes(nx, ny, i, j)
        move_wide_boxes(nx+1, ny, i, j)
        wide_warehouse[(nx, ny)] = wide_warehouse[(x, y)]
        wide_warehouse[(x, y)] = "."
    elif wide_warehouse[(nx, ny)] == "]":
        move_wide_boxes(nx, ny, i, j)
        move_wide_boxes(nx-1, ny, i, j)
        wide_warehouse[(nx, ny)] = wide_warehouse[(x, y)]
        wide_warehouse[(x, y)] = "."


warehouse_raw, moves = data.split("\n\n")
moves = moves.replace("\n", "")
warehouse = {}
for y, row in enumerate(warehouse_raw.splitlines()):
    for x, col in enumerate(row):
        warehouse[(x, y)] = col
        if col == "@":
            rx, ry = x, y

max_x, max_y = max(warehouse)
directions = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
x, y = rx, ry
for move in moves:
    i, j = directions[move]

    moved = move_robot("@", x, y, i, j)
    if moved:
        x += i
        y += j

boxes_coords_sum = 0
for y in range(max_y + 1):
    for x in range(max_x + 1):
        if warehouse[(x, y)] == "O":
            boxes_coords_sum += y * 100 + x

print("Part 1:", boxes_coords_sum)

wide_warehouse = {}
for y, row in enumerate(warehouse_raw.splitlines()):
    for x, col in enumerate(row):
        if col == "#":
            wide_warehouse[(x+x, y)] = "#"
            wide_warehouse[(x+x+1, y)] = "#"
        elif col == "@":
            rx, ry = x+x, y
            wide_warehouse[(x+x, y)] = "@"
            wide_warehouse[(x+x+1, y)] = "."
        elif col == ".":
            wide_warehouse[(x+x, y)] = "."
            wide_warehouse[(x+x+1, y)] = "."
        elif col == "O":
            wide_warehouse[(x+x, y)] = "["
            wide_warehouse[(x+x+1, y)] = "]"

x, y = rx, ry
for move in moves:
    i, j = directions[move]

    if (i and can_move_left_right(x, y, i)
            or j and can_move_up_down(x, y, j)):
        move_wide_boxes(x, y, i, j)
        x += i
        y += j

max_x, max_y = max(wide_warehouse)
boxes_coords_sum = 0
for y in range(max_y + 1):
    for x in range(max_x + 1):
        if wide_warehouse[(x, y)] == "[":
            boxes_coords_sum += y * 100 + x

print("Part 2:", boxes_coords_sum)

# display warehouse
# for y in range(max_y + 1):
#     for x in range(max_x + 1):
#         print(wide_warehouse[(x, y)], end="")
#     print()
