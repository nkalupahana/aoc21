from collections import Counter

with open("day14.txt") as f:
    letters = [x for x in f.readline().strip()]
    f.readline()

    matches = {}
    for line in f:
        line = line.strip().split(" -> ")
        matches[line[0]] = line[1]

for _ in range(10):
    narr = []
    for i in range(len(letters) - 1):
        narr.append(matches[letters[i] + letters[i + 1]])     

    res = letters + narr
    res[::2] = letters
    res[1::2] = narr
    letters = res

c = Counter(letters).most_common()
print(c[0][1] - c[-1][1])