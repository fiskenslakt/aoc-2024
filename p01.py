from aocd import data

left_list = []
right_list = []

for line in data.splitlines():
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

left_list.sort()
right_list.sort()

total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))
similarity_score = sum(left * right_list.count(left) for left in left_list)

print("Part 1:", total_distance)
print("Part 2:", similarity_score)
