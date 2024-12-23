from collections import defaultdict

from aocd import data


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


secret_sum = 0
monkeys = []
for secret in data.splitlines():
    secret = int(secret)
    monkey = [secret]

    for _ in range(2000):
        secret = get_random_number(secret)
        monkey.append(secret)

    secret_sum += secret
    monkeys.append(monkey)

price_changes = defaultdict(int)
for secrets in monkeys:
    seen = set()
    i1, i2, i3, i4, i5 = range(5)
    while True:
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

print("Part 1:", secret_sum)
print("Part 2:", max(price_changes.values()))
