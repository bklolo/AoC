
# Open file
x = open('AoC5.txt').read()

# Split text by \n
strip = x.split("\n")

# Grab all Boxes
tallestStack = 8                    # change
boxes = strip[0:tallestStack]

# Populate list of boxes
totalColumns = 9                    # change
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
commandsBegin = 10                  # change
commands = strip[commandsBegin:]
print("commands\n", commands)

#############################################
###### Part I: Move crates one-by-one #######
#############################################

def partIMove():
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

# Run commands and print answer
# partIMove()

#############################################
###### Part II: Move multiple crates ########
#############################################

def partIIMove():
    moveAmount = 0
    moveFrom = 0
    moveTo = 0
    offset = 1
    for line in commands:
        multiList = []
        # check for double digit number
        if line[6] != ' ':
            moveAmount = int(line[5:7])
            moveFrom = int(line[13]) - offset
            moveTo = int(line[18]) - offset
        # single digit number
        else:
            moveAmount = int(line[5])
            moveFrom = int(line[12]) - offset
            moveTo = int(line[17]) - offset
        # move n crates into list
        for amt in range(0, moveAmount):
            multiList.append(columns[moveFrom].pop())
        multiList.reverse()
        for e in multiList: ###### not finished
            print("e: ", e)
            columns[moveTo].append(e)
    answer = []
    for item in columns:
        answer.append(item.pop())

    print("answer\n", answer)

# Run commands and print answer
partIIMove()
