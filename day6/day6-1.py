fish = []
with open("day6.txt") as f:
    fish = [int(x) for x in f.readline().strip().split(",")]

for _ in range(80):
    fish = [x - 1 for x in fish]
    i = 0
    while i < len(fish):
        if fish[i] < 0:
            fish[i] = 6
            fish.append(8)
        i += 1

print(len(fish))