with open("day13.txt") as f:
    points = set()
    folds = []
    while (line := f.readline()) != "\n":
        points.add(tuple(map(int, line.strip().split(","))))
    
    for line in f.readlines():
        d = line[11:].strip().split("=")
        folds.append((d[0], int(d[1])))

for axis, line in folds:
    if axis == "x":
        points = {(line - abs(line - p[0]), p[1]) for p in points}
    else:
        points = {(p[0], line - abs(line - p[1])) for p in points}

for row in range(max(point[1] for point in points) + 1):
    for column in range(max(point[0] for point in points) + 1):
        print("■" if (column, row) in points else " ", end="")

    print("")
