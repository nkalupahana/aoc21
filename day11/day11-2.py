import numpy as np

lines = []
flashes = 0
with open("day11.txt") as f:
    lines = np.array([[int(y) for y in x.strip()] for x in f.readlines()])

def flash(i, j):
    global flashes

    flashes += 1
    lines[i, j] = 11
    points = [(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i-1, j-1), (i+1, j+1), (i-1, j+1), (i+1, j-1)]
    for point in points:
        if point[0] >= 0 and point[0] < len(lines) and point[1] >= 0 and point[1] < len(lines[0]) and lines[point[0]][point[1]] < 10:
            lines[point[0]][point[1]] += 1
            if lines[point[0]][point[1]] == 10:
                flash(point[0], point[1])

for _ in range(1000):
    lines += 1
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == 10:
                flash(i, j)

    lines[lines == 11] = 0
    if np.all(lines == 0):
        print(_ + 1)
        break