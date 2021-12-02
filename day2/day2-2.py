lines = []
with open("day2.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

forward = 0
depth = 0
aim = 0

for line in lines:
    num = int(line.split()[1])
    if "forward" in line:
        forward += num
        depth += num * aim
    elif "down" in line:
        aim += num
    elif "up" in line:
        aim -= num

print(forward * depth)