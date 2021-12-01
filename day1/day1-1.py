lines = []
with open("day1.txt") as f:
    lines = f.readlines()
    lines = [int(line.strip()) for line in lines]

increased = 0
for i in range(1, len(lines)):
    if lines[i] > lines[i-1]:
        increased += 1

print(increased)