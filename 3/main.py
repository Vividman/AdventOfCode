with open("C:\\Users\\dn\\Desktop\\Prosjektarbeid\\AdventOfCode\\3\\input.txt") as f:
    lines = f.readlines()
# with open("C:\\Users\\dn\\Desktop\\Prosjektarbeid\\AdventOfCode\\3\\test.txt") as f:
#     lines = f.readlines()

part_matrix = []
for line in lines:
    row = []
    for char in line:
        if char != "\n":
            row.append(char)
    part_matrix.append(row)

part_indicator_indexes = []
for i in range(0, len(part_matrix)):
    for j in range(0, len(part_matrix[i])):
        if (not part_matrix[i][j].isnumeric()) and (part_matrix[i][j] != "."):
            part_indicator_indexes.append((i, j))

h = len(part_matrix)-1
l = len(part_matrix[0])-1

parts_index = []
gear_indexes = {}
for coords in part_indicator_indexes:
    symbol = part_matrix[coords[0]][coords[1]]
    gear_ratio = []
    # Top Left
    if coords[0]>0 and coords[1]>0 and part_matrix[coords[0]-1][coords[1]-1].isnumeric():
        parts_index.append((coords[0]-1, coords[1]-1))
        gear_ratio.append((coords[0]-1, coords[1]-1))
    # Top
    if coords[0]>0 and part_matrix[coords[0]-1][coords[1]].isnumeric():
        parts_index.append((coords[0]-1, coords[1]))
        gear_ratio.append((coords[0]-1, coords[1]))
    # Top Right
    if coords[0]>0 and coords[1]<l and part_matrix[coords[0]-1][coords[1]+1].isnumeric():
        parts_index.append((coords[0]-1, coords[1]+1))
        gear_ratio.append((coords[0]-1, coords[1]+1))
    # Right
    if coords[1]<l and part_matrix[coords[0]][coords[1]+1].isnumeric():
        parts_index.append((coords[0], coords[1]+1))
        gear_ratio.append((coords[0], coords[1]+1))
    # Bottom Right
    if coords[0]<h and coords[1]<l and part_matrix[coords[0]+1][coords[1]+1].isnumeric():
        parts_index.append((coords[0]+1, coords[1]+1))
        gear_ratio.append((coords[0]+1, coords[1]+1))
    # Bottom
    if coords[0]<h and part_matrix[coords[0]+1][coords[1]].isnumeric():
        parts_index.append((coords[0]+1, coords[1]))
        gear_ratio.append((coords[0]+1, coords[1]))
    # Bottom Left
    if coords[0]<h and coords[1]>0 and part_matrix[coords[0]+1][coords[1]-1].isnumeric():
        parts_index.append((coords[0]+1, coords[1]-1))
        gear_ratio.append((coords[0]+1, coords[1]-1))
    # Left
    if coords[1]>0 and part_matrix[coords[0]][coords[1]-1].isnumeric():
        parts_index.append((coords[0], coords[1]-1))
        gear_ratio.append((coords[0], coords[1]-1))

    if symbol == "*":
        gear_indexes[coords] = gear_ratio

parts = {}
for coords in parts_index:
    row, col = coords
    # Go back wards until not digit or hit wall
    while col > 0 and part_matrix[row][col].isnumeric():
        col -= 1
    # Go back one if at not digit
    if not part_matrix[row][col].isnumeric():
        col += 1
    part_coords = (row, col)
    number_string = ""
    while col <= l and part_matrix[row][col].isnumeric():
        number_string += str(part_matrix[row][col])
        col += 1
    parts[part_coords] = int(number_string)

potential_gears = {}
for gear in gear_indexes:
    numbers = []
    for ratio in gear_indexes[gear]:
        row, col = ratio
        while col > 0 and part_matrix[row][col].isnumeric():
            col -= 1
        # Go back one if at not digit
        if not part_matrix[row][col].isnumeric():
            col += 1
        part_coords = (row, col)
        number_string = ""
        while col <= l and part_matrix[row][col].isnumeric():
            number_string += str(part_matrix[row][col])
            col += 1
        if int(number_string) not in numbers:
            numbers.append(int(number_string))
    potential_gears[gear] = numbers

sum = 0
new_matrix = []
for row in part_matrix:
    new_matrix.append(row)

for part in parts:
    for i in range(0, len(str(parts[part]))):
        new_matrix[part[0]][part[1]+i] = "-"
    sum += parts[part]
print(f"Sum of parts: {sum}")

gear_ratio_sum = 0
gears = {}
for gear in potential_gears:
    if len(potential_gears[gear]) == 2:
        gear_ratio_sum += potential_gears[gear][0]*potential_gears[gear][1]
        gears[gear] = potential_gears[gear]
print(f"Sum of gear ratios: {gear_ratio_sum}")

# Printing the matrix with part numbers replaced with "-", and gears colored differently than other part identifyers
for i in range(0, len(new_matrix)):
    for j in range(0, len(new_matrix[i])):
        if new_matrix[i][j] == "-":
            print('\033[93m' + str(new_matrix[i][j]) + '\033[0m', end="")
        elif (not new_matrix[i][j].isnumeric() and new_matrix[i][j] != "."):
            if (i, j) in gears:
                print('\033[96m' + str(new_matrix[i][j]) + '\033[0m', end="")
            else: 
                print('\033[91m' + str(new_matrix[i][j]) + '\033[0m', end="")
        else: 
            print(new_matrix[i][j], end="")
    print()