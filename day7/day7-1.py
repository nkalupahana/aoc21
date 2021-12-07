import numpy as np

positions = []
with open("day7.txt") as f:
    positions = np.array([int(x) for x in f.readline().strip().split(",")])

print(int(np.sum(abs(positions - np.median(positions)))), int(np.median(positions)))