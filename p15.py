from aocd import data, submit

# data = """########
# #..O.O.#
# ##@.O..#
# #...O..#
# #.#.O..#
# #...O..#
# #......#
# ########

# <^^>>>vv<v>>v<<"""

# data = """##########
# #..O..O.O#
# #......O.#
# #.OO..O.O#
# #..O@..O.#
# #O#..O...#
# #O..O..O.#
# #.OO.O.OO#
# #....O...#
# ##########

# <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
# vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
# ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
# <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
# ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
# ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
# >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
# <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
# ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
# v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""


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
# import pudb;pu.db
for move in moves:
    i, j = directions[move]

    moved = move_robot("@", rx, ry, i, j)
    if moved:
        rx += i
        ry += j

# display warehouse
# for y in range(max_y + 1):
#     for x in range(max_x + 1):
#         print(warehouse[(x, y)], end="")
#     print()

boxes_coords_sum = 0
for y in range(max_y + 1):
    for x in range(max_x + 1):
        if warehouse[(x, y)] == "O":
            boxes_coords_sum += y * 100 + x

submit(boxes_coords_sum)
