fish = [0] * 9
with open("day6.txt") as f:
    days = [int(x) for x in f.readline().strip().split(",")]
    for day in days:
        fish[day] += 1

for _ in range(256):
    num = fish.pop(0)
    fish[6] += num
    fish.append(num)

print(sum(fish))