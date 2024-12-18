from collections import defaultdict, deque

from aocd import data

MAX_COORD = 70


def bfs(start, end):
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        (x, y), steps = queue.popleft()

        if (x, y) == end:
            return steps

        for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx, ny = x+i, y+j

            if nx < 0 or nx > MAX_COORD:
                continue
            if ny < 0 or ny > MAX_COORD:
                continue

            if memory_space[(nx, ny)] == "." and (nx, ny) not in visited:
                queue.append(((nx, ny), steps+1))
                visited.add((nx, ny))


incoming_bytes = []
for line in data.splitlines():
    x, y = map(int, line.split(","))
    incoming_bytes.append((x, y))

memory_space = defaultdict(lambda: ".")
for byte, (x, y) in enumerate(incoming_bytes, 1):
    memory_space[(x, y)] = "#"
    steps = bfs((0, 0), (MAX_COORD, MAX_COORD))
    if steps is None:
        break
    elif byte == 1024:
        print("Part 1:", steps)

print(f"Part 2: {x},{y}")
