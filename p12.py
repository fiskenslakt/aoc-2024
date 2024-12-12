from collections import deque, defaultdict

from aocd import data, submit

# data = """RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE"""

def bfs(start, plant):
    queue = deque([start])
    region = set([start])

    while queue:
        x, y = queue.popleft()

        for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx, ny = x + i, y + j

            if (nx, ny) in region:
                continue
            elif nx < 0 or nx == len(plot[0]):
                continue
            elif ny < 0 or ny == len(plot):
                continue
            elif plot[ny][nx] != plant:
                continue

            region.add((nx, ny))
            queue.append((nx, ny))

    return region

plot = data.splitlines()
visited = set()
plants = defaultdict(list)
# import pudb;pu.db
for y, row in enumerate(plot):
    for x, plant in enumerate(row):
        coord = (x, y)
        if coord not in visited:
            region = bfs(coord, plant)
            visited |= region
            plants[plant].append(region)

price = 0
for plant, regions in plants.items():
    for region in regions:
        perimeter = 0
        for x, y in region:
            for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = x + i, y + j

                if (nx, ny) not in visited:
                    perimeter += 1
                elif plot[ny][nx] != plant:
                    perimeter += 1

        price += len(region) * perimeter

submit(price)
