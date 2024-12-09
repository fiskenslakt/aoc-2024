from aocd import data, submit

# data = "2333133121414131402"

fs = []
is_block = True
block_id = 0
block_files = []
free_space = []
for digit in data:
    if is_block:
        block_files.append(digit)
        for _ in range(int(digit)):
            fs.append(block_id)
        block_id += 1
    else:
        free_space.append(digit)
        for _ in range(int(digit)):
            fs.append(None)

    is_block = not is_block

# print("".join(str(i) if i is not None else "." for i in fs))

# i = 0
# j = len(fs) - 1
# while True:
#     while fs[i] is not None:
#         i += 1

#     while fs[j] is None:
#         j -= 1

#     if i >= j:
#         break

#     fs[i], fs[j] = fs[j], fs[i]
j = len(fs) - 1
# import pudb;pu.db
for block_size, block_id in zip(block_files[::-1], range(block_id-1, 0, -1)):
    while fs[j] != block_id:
        j -= 1
        if j < 0:
            break

    if j < 0:
        break

    # search for suitable empty space
    for i in range(len(fs)):
        if fs[i] is None:
            possible_space = fs[i : i + int(block_size)]
            if len(possible_space) == int(block_size) and all(b is None for b in possible_space):
                break
    else:
        continue

    # move block to empty space
    if i < j:
        for _ in range(int(block_size)):
            fs[i], fs[j] = fs[j], fs[i]
            i += 1
            j -= 1

# print("".join(str(i) if i is not None else "." for i in fs))

t = 0

for i, d in enumerate(fs):
    if d is None:
        continue
    t += i * int(d)

submit(t)
# print(block_files)
# print(free_space)
