lines = []

with open("day9.txt") as f:
    lines = [[int(y) for y in x.strip()] for x in f.readlines()]

risks = 0
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

        risks += point + 1

print(risks)