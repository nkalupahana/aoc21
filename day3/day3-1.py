lines = []
with open("day3.txt") as f:
    lines = [line.strip() for line in f]

counts = [0] * 12
for line in lines:
    for i in range(12):
        counts[i] += int(line[i])

counts = ["1" if count > len(lines) / 2 else "0" for count in counts]
gamma = int("".join(counts), 2)
epsilon = int("".join(["1" if count == "0" else "0" for count in counts]), 2)
print(gamma * epsilon)