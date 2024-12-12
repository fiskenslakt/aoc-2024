from collections import deque, defaultdict

from aocd import data


def bfs(start, plant):
    queue = deque([start])
    region = set([start])

    while queue:
        x, y = queue.popleft()

        for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx, ny = x + i, y + j

            if (nx, ny) in region:
                continue
            elif nx in (-1, len(plot[0])):
                continue
            elif ny in (-1, len(plot)):
                continue
            elif plot[ny][nx] != plant:
                continue

            region.add((nx, ny))
            queue.append((nx, ny))

    return region

def count_corners(x, y, region):
    corners = 0
    # up, left (outside top left corner)
    if ((x, y-1) not in region
            and (x-1, y) not in region):
        corners += 1
    # up, right (outside top right corner)
    if ((x, y-1) not in region
            and (x+1, y) not in region):
        corners += 1
    # down, right (outside bottom right corner)
    if ((x, y+1) not in region
            and (x+1, y) not in region):
        corners += 1
    # down, left (outside bottom left corner)
    if ((x, y+1) not in region
            and (x-1, y) not in region):
        corners += 1

    # same down, diff down-right, same right (inside top left)
    if ((x, y+1) in region
            and (x+1, y+1) not in region
            and (x+1, y) in region):
        corners += 1
    # same down, diff down-left, same left (inside top right)
    if ((x, y+1) in region
            and (x-1, y+1) not in region
            and (x-1, y) in region):
        corners += 1
    # same up, diff up-left, same left (inside bottom right)
    if ((x, y-1) in region
            and (x-1, y-1) not in region
            and (x-1, y) in region):
        corners += 1
    # same up, diff up-right, same right (inside bottom left)
    if ((x, y-1) in region
            and (x+1, y-1) not in region
            and (x+1, y) in region):
        corners += 1

    return corners


plot = data.splitlines()
visited = set()
plants = defaultdict(list)

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

print("Part 1:", price)

bulk_price = 0
for plant, regions in plants.items():
    for region in regions:
        sides = 0
        for x, y in region:
            sides += count_corners(x, y, region)

        bulk_price += len(region) * sides

print("Part 2:", bulk_price)
