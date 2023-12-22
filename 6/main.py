import math

with open("C:\\Users\\dn\\Desktop\\Prosjektarbeid\\AdventOfCode\\6\\input.txt") as f:
    lines = f.readlines()
# with open("C:\\Users\\dn\\Desktop\\Prosjektarbeid\\AdventOfCode\\6\\test.txt") as f:
#     lines = f.readlines()


times_string = "".join(lines[0].split(":")[1].strip().split())
# times = [int(t) for t in times_string.split(" ")]
times = int(times_string)

records_string = "".join(lines[1].split(": ")[1].strip().split()) 
# records = [int(r) for r in records_string.split(" ")]
records = int(records_string)

def curve(time, x):
    return -x**2 + time*x

def abc(time, record):
    root = time**2 - 4*record
    x1 = math.ceil((-time + math.sqrt(root)) / (-2))
    if curve(time, x1) == record:
        x1 += 1
    x2 = math.floor((-time - math.sqrt(root)) / (-2))
    if curve(time, x2) == record:
        x2 -= 1
    return (x1, x2)

# ways = []
# for i in range(len(times)):
#     minmax = abc(times[i], records[i])
#     ways.append(minmax[1]-minmax[0]+1)

# print(math.prod(ways))

minmax = abc(times, records)
print(minmax[1]-minmax[0]+1)