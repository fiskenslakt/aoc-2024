from collections import defaultdict
from heapq import heappop, heappush

from aocd import data

new_pos = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}


def best_path(start, end):
    queue = [(0, start, ">", {start})]
    visited = defaultdict(lambda: float("inf"))
    best_score = None
    best_paths = []

    while queue:
        score, (x, y), facing, path = heappop(queue)

        if (x, y) == end and best_score is None:
            best_score = score
            best_paths.append(path)
        elif (x, y) == end and score == best_score:
            best_paths.append(path)
        elif best_score and score > best_score:
            return best_score, best_paths

        if facing == ">":
            if maze[(x+1, y)] == ".":
                if score + 1 <= visited[(x+1, y, facing)]:
                    visited[(x+1, y, facing)] = score + 1
                    heappush(queue, (score + 1, (x+1, y), ">", path | {(x+1, y)}))
            for new_dir in "^v":
                i, j = new_pos[new_dir]
                if maze[(x+i, y+j)] == "#" or (x+i, y+j) in path:
                    continue
                if score + 1000 <= visited[(x, y, new_dir)]:
                    visited[(x, y, new_dir)] = score + 1000
                    heappush(queue, (score + 1000, (x, y), new_dir, path))
        elif facing == "<":
            if maze[(x-1, y)] == ".":
                if score + 1 <= visited[(x-1, y, facing)]:
                    visited[(x-1, y, facing)] = score + 1
                    heappush(queue, (score + 1, (x-1, y), "<", path | {(x-1, y)}))
            for new_dir in "^v":
                i, j = new_pos[new_dir]
                if maze[(x+i, y+j)] == "#" or (x+i, y+j) in path:
                    continue
                if score + 1000 <= visited[(x, y, new_dir)]:
                    visited[(x, y, new_dir)] = score + 1000
                    heappush(queue, (score + 1000, (x, y), new_dir, path))
        elif facing == "^":
            if maze[(x, y-1)] == ".":
                if score + 1 <= visited[(x, y-1, facing)]:
                    visited[(x, y-1, facing)] = score + 1
                    heappush(queue, (score + 1, (x, y-1), "^", path | {(x, y-1)}))
            for new_dir in "<>":
                i, j = new_pos[new_dir]
                if maze[(x+i, y+j)] == "#" or (x+i, y+j) in path:
                    continue
                if score + 1000 <= visited[(x, y, new_dir)]:
                    visited[(x, y, new_dir)] = score + 1000
                    heappush(queue, (score + 1000, (x, y), new_dir, path))
        elif facing == "v":
            if maze[(x, y+1)] == ".":
                if score + 1 <= visited[(x, y+1, facing)]:
                    visited[(x, y+1, facing)] = score + 1
                    heappush(queue, (score + 1, (x, y+1), "v", path | {(x, y+1)}))
            for new_dir in "<>":
                i, j = new_pos[new_dir]
                if maze[(x+i, y+j)] == "#" or (x+i, y+j) in path:
                    continue
                if score + 1000 <= visited[(x, y, new_dir)]:
                    visited[(x, y, new_dir)] = score + 1000
                    heappush(queue, (score + 1000, (x, y), new_dir, path))


maze = {}
for y, row in enumerate(data.splitlines()):
    for x, col in enumerate(row):
        if col == "S":
            start = (x, y)
            maze[(x, y)] = "."
        elif col == "E":
            end = (x, y)
            maze[(x, y)] = "."
        else:
            maze[(x, y)] = col

best_score, paths = best_path(start, end)
print("Part 1:", best_score)
tiles_in_best_paths = len(set.union(*paths))
print("Part 2:", tiles_in_best_paths)
