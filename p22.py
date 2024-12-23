from collections import defaultdict

from aocd import data, submit

# data = """1
# 10
# 100
# 2024"""

# data = """1
# 2
# 3
# 2024"""

# data = """123"""


def get_random_number(secret):
    n = secret * 64
    secret ^= n
    secret %= 16777216
    n = secret // 32
    secret ^= n
    secret %= 16777216
    n = secret * 2048
    secret ^= n
    secret %= 16777216
    return secret


# def get_price(secrets: list[int], price_changes: tuple[int] | None = None):
#     all_price_changes = set()
#     i1, i2, i3, i4, i5 = range(5)
#     while True:
#         n1 = (secrets[i2] % 10) - (secrets[i1] % 10)
#         n2 = (secrets[i3] % 10) - (secrets[i2] % 10)
#         n3 = (secrets[i4] % 10) - (secrets[i3] % 10)
#         n4 = (secrets[i5] % 10) - (secrets[i4] % 10)

#         all_price_changes.add((n1, n2, n3, n4))

#         if price_changes and (n1, n2, n3, n4) == price_changes:
#             return secrets[i5] % 10

#         i1 += 1
#         i2 += 1
#         i3 += 1
#         i4 += 1
#         i5 += 1

#         if i5 == len(secrets):
#             break

#     if price_changes is None:
#         return all_price_changes
#     else:
#         return 0


secret_sum = 0
monkeys = defaultdict(list)
for secret in data.splitlines():
    secret = int(secret)
    original_secret = secret
    monkeys[original_secret].append(secret)
    for _ in range(2000):
        secret = get_random_number(secret)
        monkeys[original_secret].append(secret)

    secret_sum += secret

# submit(secret_sum)
print("Part 1:", secret_sum)

price_changes = defaultdict(int)
for og, secrets in monkeys.items():
    # print("doing: ", og)
    seen = set()
    i1, i2, i3, i4, i5 = range(5)
    while True:
        # print(f"{i5=}")
        n1 = (secrets[i2] % 10) - (secrets[i1] % 10)
        n2 = (secrets[i3] % 10) - (secrets[i2] % 10)
        n3 = (secrets[i4] % 10) - (secrets[i3] % 10)
        n4 = (secrets[i5] % 10) - (secrets[i4] % 10)

        deltas = (n1, n2, n3, n4)

        if deltas not in seen:
            seen.add(deltas)
            price_changes[deltas] += secrets[i5] % 10

        i1 += 1
        i2 += 1
        i3 += 1
        i4 += 1
        i5 += 1

        if i5 == len(secrets):
            break

# import pudb;pu.db
# print(get_price(monkeys[1], (-2,1,-1,3)))
# print(get_price(monkeys[2], (-2,1,-1,3)))
# print(get_price(monkeys[3], (-2,1,-1,3)))
# print(get_price(monkeys[2024], (-2,1,-1,3)))
# get_price(monkeys[123], (-1,-1,0,2))

# print(max(price_changes, key=price_changes.get))
print("Part 2:", max(price_changes.values()))
submit(max(price_changes.values()))
