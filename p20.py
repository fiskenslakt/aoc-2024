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

cheats = defaultdict(int)

for time in bfs((sx, sy), (ex, ey)):
    cheats[time] += 1

amount_of_races_that_save_100_picoseconds = 0

for picoseconds, races in cheats.items():
    if max_picoseconds - picoseconds >= 100:
        amount_of_races_that_save_100_picoseconds += races

submit(amount_of_races_that_save_100_picoseconds)
