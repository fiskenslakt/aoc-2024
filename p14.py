import re
from itertools import count

from aocd import data

WIDTH = 101
HEIGHT = 103

robots = []
for line in data.splitlines():
    px, py, vx, vy = map(int, re.findall(r"(-?\d+)", line))
    robots.append({"px": px, "py": py, "vx": vx, "vy": vy})

q1 = q2 = q3 = q4 = 0
for robot in robots:
    x, y = robot["px"], robot["py"]
    x = (x + robot["vx"] * 100) % WIDTH
    y = (y + robot["vy"] * 100) % HEIGHT
    if x < WIDTH // 2:
        if y < HEIGHT // 2:
            q1 += 1
        elif y > HEIGHT // 2:
            q3 += 1
    elif x > WIDTH // 2:
        if y < HEIGHT // 2:
            q2 += 1
        elif y > HEIGHT // 2:
            q4 += 1

most_adjacent = 0
tree = 0
try:
    for second in count(start=1):
        for robot in robots:
            robot["px"] = (robot["vx"] + robot["px"]) % WIDTH
            robot["py"] = (robot["vy"] + robot["py"]) % HEIGHT

        adjacent = 0
        for r1 in robots:
            for r2 in robots:
                if r1["px"] == r2["px"]:
                    if r1["py"] in (r2["py"]-1, r2["py"]+1):
                        adjacent += 1
                elif r1["py"] == r2["py"]:
                    if r1["px"] in (r2["px"]-1, r2["px"]+1):
                        adjacent += 1

        if adjacent > most_adjacent:
            most_adjacent = adjacent
            tree = second
            for y in range(HEIGHT):
                for x in range(WIDTH):
                    for robot in robots:
                        if robot["px"] == x and robot["py"] == y:
                            print("#", end="")
                            break
                    else:
                        print(".", end="")
                print()
            print()
except KeyboardInterrupt:
    print("Part 1:", q1 * q2 * q3 * q4)
    print("Part 2:", tree)
