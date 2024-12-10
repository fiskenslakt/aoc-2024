from collections import deque

from aocd import data, submit

def bfs(x, y):
    score = 0
    queue = deque([(x, y)])
    trailtails = set()

    while queue:
        x, y = queue.popleft()

        if graph[(x, y)] == "9": # and (x, y) not in trailtails:
            score += 1
            trailtails.add((x, y))

        for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx, ny = x + i, y + j

            if (nx, ny) not in graph:
                continue

            a = graph[(x, y)]
            b = graph[(nx, ny)]
            if int(b) - 1 == int(a):
                queue.append((nx, ny))

    return score


graph = {}
trailheads = []

for y, row in enumerate(data.splitlines()):
    for x, col in enumerate(row):
        graph[(x, y)] = col
        if col == "0":
            trailheads.append((x, y))

score_sum = 0
for x, y in trailheads:
    score = bfs(x, y)
    score_sum += score

submit(score_sum)
