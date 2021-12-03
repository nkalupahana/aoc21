from functools import reduce
from copy import deepcopy

lines = []
with open("day3.txt") as f:
    lines = [line.strip() for line in f]

oxygen = deepcopy(lines)
co2 = deepcopy(lines)

# Oxygen calc
idx = 0
while True:
    keep = "1" if sum([int(line[idx]) for line in oxygen]) >= (len(oxygen) / 2) else "0"
    oxygen = [line for line in oxygen if line[idx] == keep]
    if len(oxygen) == 1:
        break
    idx += 1

oxygen = int(oxygen[0], 2)

# CO2 calc
idx = 0
while True:
    keep = "1" if sum([int(line[idx]) for line in co2]) < (len(co2) / 2) else "0"
    co2 = [line for line in co2 if line[idx] == keep]
    if len(co2) == 1:
        break
    idx += 1

co2 = int(co2[0], 2)
print(oxygen * co2)
