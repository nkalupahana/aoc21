from statistics import mean
import numpy as np

positions = []
with open("day7.txt") as f:
    positions = np.array([int(x) for x in f.readline().strip().split(",")])

min, mline = float("inf"), 0
for line in range(max(positions)):
    diff = np.sum(abs(positions - line))

    if diff < min:
        min, mline = diff, line

print(min, mline)