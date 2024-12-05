from collections import defaultdict

from aocd import data

raw_rules, raw_updates = data.split("\n\n")

rules = defaultdict(list)
for rule in raw_rules.splitlines():
    page_a, page_b = rule.split("|")
    rules[page_b].append(page_a)

middle_pages_sum = 0
unsorted_middle_pages_sum = 0

for update in raw_updates.splitlines():
    correctly_ordered = True
    pages = update.split(",")
    for i in range(len(pages)-1):
        for j in range(i + 1, len(pages)):
            if pages[j] in rules[pages[i]]:
                correctly_ordered = False
                pages[i], pages[j] = pages[j], pages[i]

    if correctly_ordered:
        middle_pages_sum += int(pages[len(pages)//2])
    else:
        unsorted_middle_pages_sum += int(pages[len(pages)//2])

print("Part 1:", middle_pages_sum)
print("Part 2:", unsorted_middle_pages_sum)
