import re

with open('1\input.txt') as f:
    lines = f.readlines()

numbers = []
for line in lines:
    number = []
    word = ""
    for letter in line:
        if letter.isdigit(): 
            number.append(int(letter))
            word = ""
        else: word += str(letter)

        if "one" in word: 
            number.append(1)
            word = "e"
        if "two" in word: 
            number.append(2)
            word = "o"
        if "three" in word: 
            number.append(3)
            word = "e"
        if "four" in word: 
            number.append(4)
            word = "r"
        if "five" in word: 
            number.append(5)
            word = "e"
        if "six" in word: 
            number.append(6)
            word = "x"
        if "seven" in word: 
            number.append(7)
            word = "n"
        if "eight" in word: 
            number.append(8)
            word = "t"
        if "nine" in word: 
            number.append(9)
            word = "e"

    numbers.append(number)

print(numbers)

sum = 0
for number in numbers:
    sum += int(str(number[0]) + str(number[-1]))

print(sum)
