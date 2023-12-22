import numpy as np
import math

with open("C:\\Users\\dn\\Desktop\\Prosjektarbeid\\AdventOfCode\\11\\input.txt") as f:
    lines = f.readlines()
# with open("C:\\Users\\dn\\Desktop\\Prosjektarbeid\\AdventOfCode\\11\\test.txt") as f:
#     lines = f.readlines()

rows, columns = [], []

for i, row in enumerate(lines):
    row = row.replace("\n", "")
    if not '#' in row:
        rows.append(row.replace(".", "|"))
    else:
        rows.append(row)

for i in range(0, len(rows[0])):
    col = []
    for row in rows:
        col.append(row[i])
    if not '#' in col:
        columns.append(['|' for _ in range(len(col))])
    else:
        columns.append(col)

correct_image = np.transpose(columns).tolist()

print("Starting image")
for line in lines:
    print(line.replace("\n", ""))

print()

print("Corrected image")
for row in correct_image:
    for col in row:
        print(col, end="")
    print()

print()

def find_distance_sum(add):
    stars = {}
    for i in range(len(correct_image)):
        for j in range(len(correct_image[i])):
            if correct_image[i][j] == '#':
                # print("Extra row count ", columns[j][:i].count('|'))
                # print("Extra column count ", correct_image[i][:j].count('|'))
                # print("Coords ", (i, j))
                stars[len(stars)+1] = (i + columns[j][:i].count('|') * add, j + correct_image[i][:j].count('|') * add)
                # print(f"New coords {stars[len(stars)]}")
                # print()

    sum = 0
    for i in range(1, len(stars)+1):
        for j in range(i+1, len(stars)+1):
            # print(f"Star: {i}", stars[i])
            # print(f"Star: {j}", stars[j])
            # print("Distance: ", abs(stars[i][0]-stars[j][0]) + abs(stars[i][1]-stars[j][1]))
            # print()
            sum += abs(stars[i][0]-stars[j][0]) + abs(stars[i][1]-stars[j][1])

    return sum

print(find_distance_sum(1000000-1))