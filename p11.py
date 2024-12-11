from collections import defaultdict
from functools import cache

from aocd import data


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


stones = defaultdict(int)
for stone in data.split():
    stones[stone] += 1

for blink in range(1, 76):
    new_stones = defaultdict(int)

    for stone, amount in stones.items():
        new_stone_a, new_stone_b = get_stone(stone)
        new_stones[new_stone_a] += amount
        if new_stone_b is not None:
            new_stones[new_stone_b] += amount

    stones = new_stones

    if blink == 25:
        print("Part 1:", sum(stones.values()))

print("Part 2:", sum(stones.values()))
