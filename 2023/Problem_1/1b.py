import re

x = open('2023\\Problem_1\\input.txt').read()
document = re.split("\n", x)

valid_digits = {"one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}
row = []
l = []
sum=0
# Convert words to digits and append to row list
for line in document:
    line_digits = [None] * len(line)                                # dynamic list
    for word, digit in valid_digits.items():
        word_index = line.find(word)    
        # if word in line, add it to line_digits[index] = word
        while word_index != -1:
            line_digits[word_index] = digit
            word_index = line.find(word, word_index + 1)
    # iterate over each character in the line
    for index, char in enumerate(line):
        # check if the character is a digit
        if char.isdigit():
            line_digits[index] = char
    # Combine both numeric and converted digits in the same list
    l = [i for i in line_digits if i is not None]
    row.append(l)

sum=0
count = 0
for item in row:
    count+=1
    
    first = item[0]
    last = item[-1]
    num = first+last
    print("line: ", count, " item: ", item, " num: ", num)
    sum += int(num)

print(sum)
