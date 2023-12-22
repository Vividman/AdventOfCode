import time

with open("C:\\Users\\dn\\Desktop\\Prosjektarbeid\\AdventOfCode\\5\\input.txt") as f:
    lines = f.readlines()
# with open("C:\\Users\\dn\\Desktop\\Prosjektarbeid\\AdventOfCode\\5\\test.txt") as f:
#     lines = f.readlines()

parts = "".join(lines).split("\n\n")

seeds_part = parts[0]
almanac = {}
for part in parts[1:]:
    key, values = part.split(":")
    ranges = []
    for value in values.strip().split("\n"):
        val_range = value.split(" ")
        ranges.append([int(val) for val in val_range])
    almanac[key.replace(" map", "")] = ranges

lowest_id = float('inf')
seeds = [int(s) for s in seeds_part.split(": ")[1].split(" ")]
start_time = time.time()
for i in range(0, len(seeds), 2):
    start = int(seeds[0+i])
    length = int(seeds[1+i])
    print(f"[{start}, {start + length}], {length}")
    for seed in range(start, start+length):
        next_id = seed
        for key in almanac:
            for val_range in almanac[key]:
                if next_id >= val_range[1] and next_id < val_range[1]+val_range[2]:
                    next_id = val_range[0] + (next_id - val_range[1])
                    break
        if lowest_id > next_id:
            lowest_id = next_id
            print(lowest_id)

print(f"Time taken in millis: {start_time - time.time()}")
print(f"Lowest ID: {lowest_id}")
