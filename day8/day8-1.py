lines = []
with open("day8.txt") as f:
    lines = [x.strip().split(" | ")[1] for x in f.readlines()]


count = 0
for line in lines:
    for line in line.split(" "):
        print(line)
        if len(line) == 2 or len(line) == 4 or len(line) == 3 or len(line) == 7:
            count += 1

print(count)