from collections import defaultdict

from aocd import data, submit

r, u = data.split("\n\n")

rules = defaultdict(list)

for rule in r.splitlines():
    a, b = rule.split("|")
    rules[b].append(a)

t = 0
unsorted = []

for update in u.splitlines():
    pages = update.split(",")
    for i in range(len(pages)-1):
        for j in range(i + 1, len(pages)):
            if pages[j] in rules[pages[i]]:
                unsorted.append(pages)
                break
        else:
            continue
        break
    else:
        t += int(pages[len(pages)//2])

# submit(t)
t2 = 0
for pages in unsorted:
    for i in range(len(pages)-1):
        for j in range(i + 1, len(pages)):
            if pages[j] in rules[pages[i]]:
                pages[i], pages[j] = pages[j], pages[i]

    t2 += int(pages[len(pages)//2])

submit(t2)
