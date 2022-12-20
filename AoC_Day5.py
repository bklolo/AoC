import re
from array import *
x = open('AoC5.txt').read()
strip = re.split("\n", x)
# print(strip)
cols = []
count = 0
for line in strip:
    row = []
    if count < 8:
        row.append(line[1])
        row.append(line[5])
        row.append(line[9])
        row.append(line[13])
        row.append(line[17])
        row.append(line[21])
        row.append(line[25])
        row.append(line[29])
        row.append(line[33])
        count += 1
        cols.append(row)
print(cols)

row1 = []
row2 = []
row3 = []
row4 = []
row5 = []
row6 = []
row7 = []
row8 = []
row9 = []
rows = []
for item in cols:
    row1.append(item[0])
    row2.append(item[1])
    row3.append(item[2])
    row4.append(item[3])
    row5.append(item[4])
    row6.append(item[5])
    row7.append(item[6])
    row8.append(item[7])
    row9.append(item[8])

print(row3)

for x in row3:
    if x == ' ':
        row3.remove(x)
print(row3)
'''
a = []
for x in strip:
    b = []
    if x != "\n":
        b.append(x)
    a.append(b)
print(a)
# res = [list(sub) for sub in test_list]
'''
'''pseudo code'''
# get input from file as string
# deal with box input
# create list of each column
# use substrings to collect boxes
# for each line (\n) of file
# put column letters in appropriate lists
# deal with moves input
