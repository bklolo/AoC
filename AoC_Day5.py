
# Open file
x = open('AoC5.txt').read()

# Split text by \n
strip = x.split("\n")

# Grab all Boxes
tallestStack = 8
boxes = strip[0:tallestStack]

# Populate list of boxes
totalColumns = 9
columnNumber = 1
columns = []
for i in range(0, totalColumns):
    rList = []
    for string in boxes:
        if string[columnNumber] != ' ':
            rList.append(string[columnNumber])
    rList.reverse()
    columns.append(rList)
    columnNumber += 4

# Grab move commands
commandsBegin = 10
commands = strip[commandsBegin:]
print("commands\n", commands)

# Move amount is at commands[5-6]
    # If moveAmount is a double-digit:
        # index of columns += 1
    # Else
        # index of fromCol = moveAmount+7, toCol = movement+12
# Execute commands
moveAmount = 0
moveFrom = 0
moveTo = 0
offset = 1
for line in commands:
    if line[6] != ' ':
        moveAmount = int(line[5:7])
        moveFrom = int(line[13]) - offset
        moveTo = int(line[18]) - offset
    else:
        moveAmount = int(line[5])
        moveFrom = int(line[12]) - offset
        moveTo = int(line[17]) - offset

    for amt in range(0, moveAmount):
        columns[moveTo].append(columns[moveFrom].pop())
answer = []
for item in columns:
    answer.append(item.pop())

print("answer\n", answer)
'''pseudo code'''
# get input from file as string
# deal with box input
    # add each row to a list
    # use substrings to collect letters from rows
    # put column letters in appropriate lists
    # deal with moves input
