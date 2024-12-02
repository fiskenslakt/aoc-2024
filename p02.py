from itertools import pairwise

from aocd import data


def is_bad(l1, l2, direction):
    if l1 == l2 or abs(l1 - l2) > 3:
        return True
    elif direction == "increasing" and l1 - l2 > 0:
        return True
    elif direction == "decreasing" and l1 - l2 < 0:
        return True
    else:
        return False


safe = 0
almost_safe = 0
for report in data.splitlines():
    levels = list(map(int, report.split()))
    diffs = [l1 - l2 for l1, l2 in pairwise(levels)]

    if (all(d > 0 and abs(d) <= 3 for d in diffs)
            or all(d < 0 and abs(d) <= 3 for d in diffs)):
        safe += 1
        continue

    neg = [d for d in diffs if d < 0]
    pos = [d for d in diffs if d > 0]
    if len(neg) > len(pos):
        direction = "increasing"
    else:
        direction = "decreasing"

    for r in range(len(levels)):
        problem_dampened_report = levels[:r] + levels[r+1:]
        for l1, l2 in pairwise(problem_dampened_report):
            if is_bad(l1, l2, direction):
                break
        else:
            almost_safe += 1
            break

print("Part 1:", safe)
print("Part 2:", safe + almost_safe)
