import re
x = open('2023\\Problem_1\\input.txt').read()
document = re.split("\n", x)

row = []
for line in document:
    current_number = ""
    for letter in line:
        if letter.isnumeric():
            current_number += letter
    if current_number:
        row.append(current_number)
#print(row)

sum=0
for item in row:
    first = item[0]
    last = item[-1]
    num = first+last
    sum += int(num)

print(sum)

