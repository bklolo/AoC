# get max amount of each color in each game
# multilply maxes of each color together, product
# power += product

# read the document
import re
x = open('2023\\Problem_2\\'+"input"+".txt").read()
document = re.split("\n", x)

# for each gameset within each game, return a list of the minimum # of colors to make the game playable
def getMinReqAmounts(set, colors):
    listOfMinsReq = []
    # Iterate over each color
    for color in colors:
        max = 0
        # find the location of the color
        index = set.find(color)
        while index != -1:
            # get the substring of the current count, int
            count = int(set[index-3:index])
            # keep track of the max of each color
            max = count if count > max else max
            index = set.find(color, index+1)
        # add the max to the list of the min required of each color per game
        listOfMinsReq.append(max)
    return listOfMinsReq


# put games into list of lists
games = []
for line in document:
    sets = []
    sets.append(line)
    games.append(sets)


# Provided maximum amounts of red, green, and blue cubes
colors = ["red", "blue", "green"]

# Part B
maxes = []
product = 1
power = 0

# Iterate over all games
for game in games:
    for game_set in game:
        maxes.append(getMinReqAmounts(game_set, colors))

for set in maxes:
    for num in set:
        product *= num
    power += product
    product = 1

print(f"The power of valid games is: {power}")

