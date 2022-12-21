import re
from array import *
x = open('AoC5.txt').read()
strip = re.split("\n", x)
print("Strip \n", strip)

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
print("Cols \n", cols)

############################
def grabBoxes(c, r):
    boxList = []
    for ch in r:
        if not ch.isspace():
            boxList.append(r[c])
    return boxList

colNum = 1
cList = []
for column in range(0, 9): # for each col
    rList = []
    for row in range(0, 8): # for each row
        rList.append(grabBoxes(row, cols[column]))
    cList.append(rList)
print("cList \n", cList)
############################
## the above code grabs letters on a diagonal
## want to scan every row, but iterate cols

'''pseudo code'''
# get input from file as string
# deal with box input
    # add each row to a list
    # use substrings to collect letters from rows
    # put column letters in appropriate lists
    # deal with moves input
