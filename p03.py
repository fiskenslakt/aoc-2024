import re

from aocd import data

p = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)")

result = 0
more_accurate_result = 0
enabled = True
for a, b, do, dont in p.findall(data):
    if do:
        enabled = True
    elif dont:
        enabled = False

    if a and b:
        product = int(a) * int(b)
        result += product
        if enabled:
            more_accurate_result += product

print("Part 1:", result)
print("Part 2:", more_accurate_result)
