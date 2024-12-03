from aocd import data, submit

import re

# data = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''
# data = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''

p = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)")

# x = 0
# for a, b in p.findall(data):
#     x += int(a) * int(b)
# print(p.findall(data))
# submit(sum(p.findall()))
# submit(x)

x = 0
DO = True
for a, b, do, dont in p.findall(data):
    if do:
        DO = True
    elif dont:
        DO = False

    if DO and a.isnumeric() and b.isnumeric():
        x += int(a) * int(b)

submit(x)
