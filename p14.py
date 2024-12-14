import re

from aocd import data, submit

WIDTH = 101
HEIGHT = 103

# data = """p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
# p=3,0 v=-2,-2
# p=7,6 v=-1,-3
# p=3,0 v=-1,-2
# p=9,3 v=2,3
# p=7,3 v=-1,2
# p=2,4 v=2,-3
# p=9,5 v=-3,-3"""

robots = []

for line in data.splitlines():
    px, py, vx, vy = map(int, re.findall(r"(-?\d+)", line))

    robots.append({"px": px, "py": py, "vx": vx, "vy": vy})

for second in range(100):
    for robot in robots:
        robot["px"] = (robot["vx"] + robot["px"]) % WIDTH
        robot["py"] = (robot["vy"] + robot["py"]) % HEIGHT

q1 = q2 = q3 = q4 = 0
for robot in robots:
    # print(robot["px"], robot["py"])
    if robot["px"] < WIDTH // 2:
        if robot["py"] < HEIGHT // 2:
            q1 += 1
        elif robot["py"] > HEIGHT // 2:
            q3 += 1
    elif robot["px"] > WIDTH // 2:
        if robot["py"] < HEIGHT // 2:
            q2 += 1
        elif robot["py"] > HEIGHT // 2:
            q4 += 1

submit(q1 * q2 * q3 * q4)
