from aocd import data

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

two_picosecond_cheats = 0
twenty_picosecond_cheats = 0

for i, (x1, y1) in enumerate(path):
    for j, (x2, y2) in enumerate(path[i+1:], start=i+1):
        picoseconds = abs(x1 - x2) + abs(y1 - y2)
        if picoseconds == 2 and j - i - picoseconds >= 100:
            two_picosecond_cheats += 1
        if picoseconds <= 20 and j - i - picoseconds >= 100:
            twenty_picosecond_cheats += 1

print("Part 1:", two_picosecond_cheats)
print("Part 2:", twenty_picosecond_cheats)
