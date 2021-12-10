with open("day10.txt") as f:
    lines = [x.strip() for x in f]

MATCH = {
    "{": "}",
    "[": "]",
    "(": ")",
    "<": ">"
}

POINT = {
    ")" : 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

points = 0
for line in lines:
    data = []
    for x in line:
        if x in MATCH.keys():
            data.append(MATCH[x])
        else:
            if data[-1] == x:
                data.pop()
            else:
                points += POINT[x]
                break

print(points)