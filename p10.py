from collections import deque

from aocd import data


def bfs(start):
    rating = 0
    queue = deque([start])
    trailtails = set()

    while queue:
        x, y = queue.popleft()

        if graph[(x, y)] == 9:
            rating += 1
            trailtails.add((x, y))

        for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx, ny = x + i, y + j

            if (nx, ny) not in graph:
                continue

            a = graph[(x, y)]
            b = graph[(nx, ny)]
            if b - 1 == a:
                queue.append((nx, ny))

    return len(trailtails), rating


graph = {}
trailheads = []

for y, row in enumerate(data.splitlines()):
    for x, col in enumerate(row):
        graph[(x, y)] = int(col)
        if col == "0":
            trailheads.append((x, y))

score_sum = 0
rating_sum = 0
for trailhead in trailheads:
    score, rating = bfs(trailhead)
    score_sum += score
    rating_sum += rating

print("Part 1:", score_sum)
print("Part 2:", rating_sum)
