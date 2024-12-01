from aocd import data, submit

lines = data.splitlines()

L, R = [], []

for line in lines:
    a, b = map(int, line.split())
    L.append(a)
    R.append(b)

L.sort()
R.sort()

# submit(sum(abs(a-b) for a, b in zip(L,R)))

submit(sum(a*R.count(a) for a in L))
