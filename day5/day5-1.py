import numpy as np

floor = np.zeros(shape=(1000,1000))
lines = []
with open("day5.txt") as f:
    lines = [line.strip() for line in f]

for line in lines:
    line = line.split(" -> ")
    line = [line.split(",") for line in line]
    l1, l2 = sorted([int(line[0][0]), int(line[1][0])])
    r1, r2 = sorted([int(line[0][1]), int(line[1][1])])

    if l1 == l2:
        for i in range(r1, r2 + 1):
            floor[l1][i] += 1
    elif r1 == r2:
        for i in range(l1, l2 + 1):
            floor[i][r1] += 1

print(len(np.flatnonzero(floor > 1)))