from aocd import data


def dfs(value, operands, a=None, cat=False):
    if value == a and not operands:
        return True
    elif a and value < a:
        return False
    elif not operands:
        return False

    if a is None:
        a, b = operands[:2]
        new_operands = operands[2:]
    else:
        b = operands[0]
        new_operands = operands[1:]

    mul = dfs(value, new_operands, a * b, cat)
    add = dfs(value, new_operands, a + b, cat)
    if cat:
        cat = dfs(value, new_operands, int(str(a) + str(b)), cat)
    else:
        cat = False

    return mul or add or cat


calibration_result1 = 0
calibration_result2 = 0
for equation in data.splitlines():
    test_value, raw_operands = equation.split(": ")
    value = int(test_value)
    operands = list(map(int, raw_operands.split()))

    if dfs(value, operands):
        calibration_result1 += value
    if dfs(value, operands, cat=True):
        calibration_result2 += value

print("Part 1:", calibration_result1)
print("Part 2:", calibration_result2)
