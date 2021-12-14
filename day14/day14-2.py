from collections import Counter
import time

with open("day14.txt") as f:
    letters = [x for x in f.readline().strip()]
    f.readline()

    matches = {}
    data = {}
    for line in f:
        line = line.strip().split(" -> ")
        matches[line[0]] = line[1]
        data[line[0]] = 0

for i in range(len(letters) - 1):
    k = letters[i] + letters[i + 1]
    if k not in data:
        data[k] = 0
    data[k] += 1

for _ in range(40):
    ndata = {}
    for k, v in data.items():
        if (k[0] + matches[k]) not in ndata:
            ndata[k[0] + matches[k]] = 0

        if (matches[k] + k[1]) not in ndata:
            ndata[matches[k] + k[1]] = 0
        
        ndata[k[0] + matches[k]] += v
        ndata[matches[k] + k[1]] += v

    data = ndata

counting = {}
for k, v in data.items():
    if k[0] not in counting:
        counting[k[0]] = 0

    if k[1] not in counting:
        counting[k[1]] = 0
    
    counting[k[0]] += v

c = Counter(counting).most_common()
print(c[0][1] - c[-1][1] + 1)