import math

with open("C:\\Users\\dn\\Desktop\\Prosjektarbeid\\AdventOfCode\\8\\input.txt") as f:
    lines = f.readlines()
# with open("C:\\Users\\dn\\Desktop\\Prosjektarbeid\\AdventOfCode\\8\\test.txt") as f:
#     lines = f.readlines()

directions = "".join(lines[0].split())

map = {}
for line in lines[2:]:
    k, v = line.split(" = ")
    map[k] = v.replace("(", "").replace(")", "").replace("\n", "").split(", ")


def steps(start):
    roundabout = 0
    pos = start
    while pos[-1] != "Z":
        for i, direction in enumerate(directions):
            if direction == "L":
                pos = map[pos][0]
            else: pos = map[pos][1]
            if pos[-1] == "Z":
                return len(directions) * roundabout + (i+1)
        roundabout += 1

if __name__ == "__main__":
    print(f"Steps from AAA to ZZZ: {steps("AAA")}")

    start = [pos for pos in map if pos[-1] == "A"]

    steps = [steps(pos) for pos in start]

    while len(steps) > 1:
        steps.append(math.lcm(steps.pop(), steps.pop()))

    print(f"Ghostly interdimentional steps: {steps[0]}")

    