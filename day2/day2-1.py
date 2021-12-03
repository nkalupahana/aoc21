lines = []
with open("day2.txt") as f:
    lines = [line.strip() for line in f]

forward = 0
depth = 0

# This is so dumb. I love it.
# (obviously one for loop would also work for this, but I wanted to learn how to do it this way)
[forward := forward + int(item.split()[1]) for item in lines if "forward" in item]
[depth := depth - int(item.split()[1]) for item in lines if "up" in item]
[depth := depth + int(item.split()[1]) for item in lines if "down" in item]

print(forward * depth)