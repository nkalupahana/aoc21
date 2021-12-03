from functools import reduce
from copy import deepcopy

lines = []
with open("day3.txt") as f:
    lines = [line.strip() for line in f]

methods = [lambda a, b: a >= b, lambda a, b: a < b]
results = []
for method in methods:
    idx = 0
    l = deepcopy(lines)
    while True:
        keep = "1" if method(sum([int(line[idx]) for line in l]), len(l) / 2) else "0"
        l = [line for line in l if line[idx] == keep]
        if len(l) == 1:
            break
        
        idx += 1
    
    results.append(int(l[0], 2))

print(reduce(lambda a, b: a * b, results))