with open("day13.txt") as f:
    points = set()
    folds = []
    while (line := f.readline()) != "\n":
        points.add(tuple(map(int, line.strip().split(","))))
    
    for line in f.readlines():
        d = line[11:].strip().split("=")
        folds.append((d[0], int(d[1])))

line = folds[0][1]
if folds[0][0] == "x":
    points = {(line - abs(line - p[0]), p[1]) for p in points}
else:
    points = {(p[0], line - abs(line - p[1])) for p in points}

print(len(points))