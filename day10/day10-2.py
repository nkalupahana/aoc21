from statistics import median

with open("day10.txt") as f:
    lines = [x.strip() for x in f]

MATCH = {
    "{": "}",
    "[": "]",
    "(": ")",
    "<": ">"
}

POINT = {
    ")" : 1,
    "]": 2,
    "}": 3,
    ">": 4
}

autocomplete = []
for line in lines:
    data = []
    for x in line:
        if x in MATCH.keys():
            data.append(MATCH[x])
        else:
            if data[-1] == x:
                data.pop()
            else:
                data.clear()
                break
    
    if len(data) != 0:
        points = 0
        data.reverse()
        [points := points * 5 + POINT[x] for x in data]
        autocomplete.append(points)

print(median(autocomplete))