from heapq import heappop, heappush

from aocd import data, submit

data = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""


def best_path(start, end):
    queue = [(0, start, ">")]
    visited = {(start, ">")}

    while queue:
        score, (x, y), facing = heappop(queue)

        if (x, y) == end:
            return score

        if facing == ">":
            if maze[(x+1, y)] == ".":
                heappush(queue, (score + 1, (x+1, y), ">"))
            if ((x, y), "^") not in visited:
                visited.add(((x, y), "^"))
                heappush(queue, (score + 1000, (x, y), "^"))
            if ((x, y), "v") not in visited:
                visited.add(((x, y), "v"))
                heappush(queue, (score + 1000, (x, y), "v"))
        elif facing == "<":
            if maze[(x-1, y)] == ".":
                heappush(queue, (score + 1, (x-1, y), "<"))
            if ((x, y), "^") not in visited:
                visited.add(((x, y), "^"))
                heappush(queue, (score + 1000, (x, y), "^"))
            if ((x, y), "v") not in visited:
                visited.add(((x, y), "v"))
                heappush(queue, (score + 1000, (x, y), "v"))
        elif facing == "^":
            if maze[(x, y-1)] == ".":
                heappush(queue, (score + 1, (x, y-1), "^"))
            if ((x, y), "<") not in visited:
                visited.add(((x, y), "<"))
                heappush(queue, (score + 1000, (x, y), "<"))
            if ((x, y), ">") not in visited:
                visited.add(((x, y), ">"))
                heappush(queue, (score + 1000, (x, y), ">"))
        elif facing == "v":
            if maze[(x, y+1)] == ".":
                heappush(queue, (score + 1, (x, y+1), "v"))
            if ((x, y), "<") not in visited:
                visited.add(((x, y), "<"))
                heappush(queue, (score + 1000, (x, y), "<"))
            if ((x, y), ">") not in visited:
                visited.add(((x, y), ">"))
                heappush(queue, (score + 1000, (x, y), ">"))


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


best_score = best_path(start, end)
submit(best_score)
# print(best_score)
