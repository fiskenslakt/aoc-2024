from aocd import data

crossword = {(x, y): c
             for y, row in enumerate(data.splitlines())
             for x, c in enumerate(row)}

max_x, max_y = max(crossword)

xmas = 0
x_mas = 0
for y in range(max_y + 1):
    for x in range(max_x + 1):
        if crossword.get((x, y)) == "X":
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    nx = x
                    ny = y
                    for c in "MAS":
                        nx += i
                        ny += j
                        if crossword.get((nx, ny)) != c:
                            break
                    else:
                        xmas += 1
        elif crossword.get((x, y)) == "A":
            if ("".join(crossword.get((x+i, y+i), "") for i in (-1, 1)) in ("SM", "MS")
                    and "".join(crossword.get((x-i, y+i), "") for i in (-1, 1)) in ("SM", "MS")):
                x_mas += 1

print("Part 1:", xmas)
print("Part 2:", x_mas)
