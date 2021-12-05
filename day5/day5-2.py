import numpy as np

floor = np.zeros(shape=(1000,1000))
lines = []
with open("day5.txt") as f:
    lines = [line.strip() for line in f]

for line in lines:
    line = line.split(" -> ")
    line = [line.split(",") for line in line]
    l1 = int(line[0][0])
    l2 = int(line[1][0])
    r1 = int(line[0][1])
    r2 = int(line[1][1])

    if l1 == l2:
        for i in range(min(r1, r2), max(r1, r2) + 1):
            floor[l1][i] += 1
    elif r1 == r2:
        for i in range(min(l1, l2), max(l1, l2) + 1):
            floor[i][r1] += 1
    else:
        while r1 != r2:
            floor[l1][r1] += 1
            r1 += 1 if r1 < r2 else -1
            l1 += 1 if l1 < l2 else -1

        floor[l1][r1] += 1

print(len(np.flatnonzero(floor > 1)))
