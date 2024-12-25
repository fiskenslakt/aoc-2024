from aocd import data

locks = []
keys = []
for schematic in data.split("\n\n"):
    if all(col == "#" for col in schematic.splitlines()[0]):
        locks.append(tuple(pin.count("#") - 1 for pin in zip(*schematic.splitlines())))
    else:
        keys.append(tuple(bitting.count("#") - 1 for bitting in zip(*schematic.splitlines())))

fit_together = 0
for lock in locks:
    for key in keys:
        for pin, bitting in zip(lock, key):
            if pin + bitting >= 6:
                break
        else:
            fit_together += 1

print("Part 1:", fit_together)
print("Part 2: Merry Christmas!")
