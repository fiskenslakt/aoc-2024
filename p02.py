from aocd import data, submit

# data = '''7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9'''


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
safe2 = 0
for line in data.splitlines():
    levels = list(map(int, line.split()))

    diffs = [a - b for a, b in zip(levels, levels[1:])]

    if (all(x > 0 and abs(x) <= 3 for x in diffs)
            or all(x < 0 and abs(x) <= 3 for x in diffs)):
        safe += 1
        safe2 += 1
        continue

    bad = False
    neg = [x for x in diffs if x < 0]
    pos = [x for x in diffs if x > 0]
    if len(neg) > len(pos):
        direction = "increasing"
    else:
        direction = "decreasing"
    for r in range(len(levels)):
        new_levels = [x for i, x in enumerate(levels) if i != r]
        for l1, l2 in zip(new_levels, new_levels[1:]):
            if is_bad(l1, l2, direction):
                break
        else:
            safe2 += 1
            break
    # i = 0
    # j = 1
    # import pudb;pu.db
    # while i < len(levels) - 1:
    #     if not is_bad(levels[i], levels[j], direction):
    #         i = j
    #         if j + 1 < len(levels):
    #             j += 1
    #         else:
    #             continue
    #     elif bad:
    #         break
    #     else:
    #         bad = True
    #         if j + 1 < len(levels):
    #             j += 1
    #         else:
    #             i = j
    # else:
    #     safe2 += 1

    # if (len(neg) > 1 and not len(pos) > 1
    #         or len(pos) > 1 and not len(neg) > 1):
    #     big = [x for x in diffs if abs(x) > 3]
    #     if len(big) <= 1:
    #         safe2 += 1
    #         print(line, "safe")
    #         continue
    # print(line, "unsafe")

# submit(safe)
submit(safe2)
# print(safe)
# print(safe2)
