from collections import deque, defaultdict
from functools import cache

from aocd import data, submit


@cache
def get_stone(cur_stone):
    if len(cur_stone) % 2 == 0:
        stone_a = cur_stone[:len(cur_stone)//2]
        stone_b = str(int(cur_stone[len(cur_stone)//2:]))
        return stone_a, stone_b
    elif cur_stone == "0":
        return "1", None
    else:
        return str(int(cur_stone) * 2024), None


# with open("/Users/derek/.config/aocd/github.fiskenslakt.269893/2024_11_input.txt") as f:
#     data = f.read().strip()

# data = "125 17"

# stones = deque(data.split())
stones = defaultdict(int)
for stone in data.split():
    stones[stone] += 1
# import pudb;pu.db
for blink in range(75):
    new_stones = defaultdict(int)

    for stone, amount in stones.items():
        new_stone_a, new_stone_b = get_stone(stone)
        new_stones[new_stone_a] += amount
        if new_stone_b is not None:
            new_stones[new_stone_b] += amount

    stones = new_stones

print(sum(stones.values()))

#     stone_amount = len(stones)
#     print(blink, stone_amount, len(set(stones)))

#     for _ in range(stone_amount):
#         stone_a, stone_b = get_stone(stones[0])
#         if stone_b is None:
#             stones[0] = stone_a
#             stones.rotate(-1)
#         else:
#             stones[0] = stone_b
#             stones.appendleft(stone_a)
#             stones.rotate(-2)
#         # if len(stones[0]) % 2 == 0:
#         #     stone_a = stones[0][:len(stones[0])//2]
#         #     stone_b = str(int(stones[0][len(stones[0])//2:]))

#         #     stones[0] = stone_b
#         #     stones.appendleft(stone_a)

#         #     stones.rotate(-2)

#         # elif stones[0] == "0":
#         #     stones[0] = "1"

#         #     stones.rotate(-1)
#         # else:
#         #     stones[0] = str(int(stones[0]) * 2024)

#         #     stones.rotate(-1)

# # print(len(stones))
