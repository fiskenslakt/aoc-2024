from itertools import combinations

from aocd import data

city_map = {}
antennas = set()
antinodes = set()
antinodes2 = set()

for y, row in enumerate(data.splitlines()):
    for x, col in enumerate(row):
        city_map[(x, y)] = col
        if col.isalnum():
            antennas.add((x, y))

for a, b in combinations(antennas, 2):
    if city_map[a] == city_map[b]:
        x1, y1 = a
        x2, y2 = b
        mx = x2 - x1
        my = y2 - y1

        node1 = (x1 - mx, y1 - my)
        node2 = (x2 + mx, y2 + my)
        if node1 in city_map:
            antinodes.add(node1)
        if node2 in city_map:
            antinodes.add(node2)

        nx, ny = a
        while True:
            nx -= mx
            ny -= my

            if (nx, ny) in city_map:
                antinodes2.add((nx, ny))
            else:
                break

        nx, ny = b
        while True:
            nx += mx
            ny += my

            if (nx, ny) in city_map:
                antinodes2.add((nx, ny))
            else:
                break

print("Part 1:", len(antinodes))
print("Part 2:", len(antinodes2 | antennas))

