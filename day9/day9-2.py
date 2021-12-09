from functools import reduce

lines = []
with open("day9.txt") as f:
    lines = [[int(y) for y in x.strip()] for x in f.readlines()]

def find(i, j):
    if i < 0 or j < 0 or i >= len(lines) or j >= len(lines[0]):
        return 0

    if lines[i][j] == 9:
        return 0

    lines[i][j] = 9
    return 1 + find(i, j + 1) + find(i, j - 1) + find(i + 1, j) + find(i - 1, j)

regions = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        point = lines[i][j]
        if i != 0 and lines[i - 1][j] <= point:
            continue
        
        if i != len(lines) - 1 and lines[i + 1][j] <= point:
            continue

        if j != 0 and lines[i][j - 1] <= point:
            continue

        if j != len(lines[i]) - 1 and lines[i][j + 1] <= point:
            continue

        regions.append(find(i, j))

regions.sort()
print(reduce(lambda x,y: x * y, regions[-3:]))