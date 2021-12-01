lines = []
with open("day1.txt") as f:
    lines = f.readlines()
    lines = [int(line.strip()) for line in lines]

WINDOW_SIZE = 3
increased = 0
for i in range(1, len(lines) - WINDOW_SIZE + 1):
    if sum(lines[i:i + WINDOW_SIZE]) > sum(lines[i-1:i + WINDOW_SIZE - 1]):
        increased += 1

print(increased)