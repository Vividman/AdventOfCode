with open("C:\\Users\\dn\\Desktop\\Prosjektarbeid\\AdventOfCode\\9\\input.txt") as f:
    lines = f.readlines()
# with open("C:\\Users\\dn\\Desktop\\Prosjektarbeid\\AdventOfCode\\9\\test.txt") as f:
#     lines = f.readlines()

readings = [[int(num) for num in line.split(" ")] for line in lines]

def predict_next_value(reading:list):
    values = [reading]
    while not only_zeroes(values[-1]):
        new_values = []
        for i in range(len(values[-1])):
            if i<(len(values[-1])-1):
                new_values.append(values[-1][i+1]-values[-1][i])
        values.append(new_values)

    values[-1].append(0)

    for i in range(-2, -(len(values)+1), -1):
        values[i].append(values[i][-1]+values[i+1][-1])

    return values[0][-1]

def only_zeroes(list:list):
    for num in list:
        if num != 0: 
            return False
    return True

sum = 0
sum_back = 0
for reading in readings:
    sum += predict_next_value(reading)
    reading.reverse()
    sum_back += predict_next_value(reading)

print(f"Sum of future values: {sum}")
print(f"Sum of past values: {sum_back}")