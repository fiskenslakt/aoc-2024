from aocd import data, submit

# data = '''MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX'''

crossword = data.splitlines()
xmas = 0
# import pudb;pu.db
for y, line in enumerate(crossword):
    for x, char in enumerate(line):
        if char != "X":
            continue
        for i, j in ((1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)):
            nx = x
            ny = y
            for c in 'MAS':
                nx = nx + i
                ny = ny + j

                if (0 <= nx < len(line)
                        and 0 <= ny < len(crossword)):
                    if crossword[ny][nx] != c:
                        break
                else:
                    break
            else:
                xmas += 1

# submit(xmas)
mas = 0
for y, line in enumerate(crossword):
    for x, char in enumerate(line):
        # if x == 140 and y == 5:
        #     import pudb;pu.db
        if char != "A":
            continue
        if x == 0 or x == len(line) - 1 or y == 0 or y == len(crossword) - 1:
            continue

        x1, y1 = x-1, y-1
        x2, y2 = x+1, y-1
        x3, y3 = x-1, y+1
        x4, y4 = x+1, y+1

        # print(x2, y2)
        # print(len(line), len(crossword))

        if (crossword[y1][x1] == "M"
            and crossword[y2][x2] == "M"
            and crossword[y3][x3] == "S"
            and crossword[y4][x4] == "S"):
            mas += 1

        elif (crossword[y1][x1] == "S"
            and crossword[y2][x2] == "M"
            and crossword[y3][x3] == "S"
            and crossword[y4][x4] == "M"):
            mas += 1

        elif (crossword[y1][x1] == "S"
            and crossword[y2][x2] == "S"
            and crossword[y3][x3] == "M"
            and crossword[y4][x4] == "M"):
            mas += 1

        elif (crossword[y1][x1] == "M"
            and crossword[y2][x2] == "S"
            and crossword[y3][x3] == "M"
            and crossword[y4][x4] == "S"):
            mas += 1

submit(mas)
