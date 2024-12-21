from collections import deque, defaultdict

from aocd import data, submit

# data = """###############
# #...#...#.....#
# #.#.#.#.#.###.#
# #S#...#.#.#...#
# #######.#.#.###
# #######.#.#...#
# #######.#.###.#
# ###..E#...#...#
# ###.#######.###
# #...###...#...#
# #.#####.#.###.#
# #.#...#.#.#...#
# #.#.#.#.#.#.###
# #...#...#...###
# ###############"""


def bfs(start, end):
    # (x, y), picoseconds, cheated, previous pos
    queue = deque([(start, 0, False, start)])
    disabled_walls = set()
    times = []

    while queue:
        (x, y), picoseconds, cheated, (px, py) = queue.popleft()

        if (x, y) == end:
            times.append(picoseconds)
            continue

        for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx, ny = x+i, y+j

            if (nx, ny) == (px, py):
                continue

            if racetrack.get((nx, ny)) == "#" and racetrack.get((nx+i, ny+j), "#") != "#":
                if not cheated and (nx, ny) not in disabled_walls:
                    disabled_walls.add((nx, ny))
                    queue.append(((nx+i, ny+j), picoseconds + 2, True, (x, y)))
            elif racetrack.get((nx, ny)) in ".E":
                queue.append(((nx, ny), picoseconds + 1, cheated, (x, y)))

    return times


racetrack = {}
max_picoseconds = 1  # Include end
for y, row in enumerate(data.splitlines()):
    for x, col in enumerate(row):
        if col == "S":
            sx, sy = x, y
        elif col == "E":
            ex, ey = x, y
        elif col == ".":
            max_picoseconds += 1

        racetrack[(x, y)] = col

x, y = sx, sy
px, py = x, y
path = [(x, y)]
while (x, y) != (ex, ey):
    for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        nx, ny = x + i, y + j

        if (nx, ny) == (px, py):
            continue

        if racetrack[(nx, ny)] in ".E":
            px, py = x, y
            x, y = nx, ny
            path.append((x, y))
            continue
# import pudb;pu.db
ans = 0
x = defaultdict(int)
for i, (x1, y1) in enumerate(path):
    for j, (x2, y2) in enumerate(path[i+1:], start=i+1):
        picoseconds = abs(x1 - x2) + abs(y1 - y2)
        if picoseconds <= 20 and j - i - picoseconds >= 100:
            ans += 1
            # x[j - i - picoseconds] += 1
# print(x)

submit(ans)

# cheats = defaultdict(int)

# for time in bfs((sx, sy), (ex, ey)):
#     cheats[time] += 1

# amount_of_races_that_save_100_picoseconds = 0

# for picoseconds, races in cheats.items():
#     if max_picoseconds - picoseconds >= 100:
#         amount_of_races_that_save_100_picoseconds += races

# print("Part 1:", amount_of_races_that_save_100_picoseconds)
