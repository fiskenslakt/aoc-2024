from aocd import data, submit


def dfs(value, operands, a=None):
    if value == a and not operands:
        return True
    elif not operands:
        return False

    if a is None:
        a, b = operands[:2]
        new_operands = operands[2:]
    else:
        b = operands[0]
        new_operands = operands[1:]

    mul = dfs(value, new_operands, a * b)
    add = dfs(value, new_operands, a + b)

    return mul or add


def dfs2(value, operands, a=None):
    if value == a and not operands:
        return True
    elif not operands:
        return False

    if a is None:
        a, b = operands[:2]
        new_operands = operands[2:]
    else:
        b = operands[0]
        new_operands = operands[1:]

    mul = dfs2(value, new_operands, a * b)
    add = dfs2(value, new_operands, a + b)
    cat = dfs2(value, new_operands, int(str(a) + str(b)))

    return mul or add or cat


t = 0
for equation in data.splitlines():
    value, operands = equation.split(": ")

    if dfs2(int(value), list(map(int, operands.split()))):
        t += int(value)

submit(t)
