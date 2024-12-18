from collections import defaultdict, deque

from aocd import data, submit

MAX_COORD = 70
# MAX_COORD = 6

# data = """5,4
# 4,2
# 4,5
# 3,0
# 2,1
# 6,3
# 2,4
# 1,5
# 0,6
# 3,3
# 2,6
# 5,1
# 1,2
# 5,5
# 2,5
# 6,5
# 1,4
# 0,4
# 6,4
# 1,1
# 6,1
# 1,0
# 0,5
# 1,6
# 2,0"""


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
for x, y in incoming_bytes:
    memory_space[(x, y)] = "#"
    steps = bfs((0, 0), (MAX_COORD, MAX_COORD))
    if steps is None:
        break
# print(steps)
print(f"{x},{y}")
submit(f"{x},{y}")


