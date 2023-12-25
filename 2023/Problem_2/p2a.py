# provided a document of games, with sets, with # of colored cubes
# and a number of each cube: 12 red cubes, 13 green cubes, and 14 blue cubes

# read the document
import re
x = open('2023\\Problem_2\\'+"input"+".txt").read()
document = re.split("\n", x)

def getCount(set, colors, max_amounts):
    color_pass = True
    # Iterate over each color
    for color in colors:
        # find the location of the color
        index = set.find(color)
        while index != -1:
            # get the substring of the current count, int
            count = int(set[index-3:index])
            # if the count < the max amount, true
            color_pass = True if count <= max_amounts[color] else False
            # if count > max, return false
            if not color_pass:
                return color_pass
            # find next location of color in set
            else: index = set.find(color, index+1)
    return color_pass


# put games into list of lists
games = []
for line in document:
    sets = []
    sets.append(line)
    games.append(sets)


# Provided maximum amounts of red, green, and blue cubes
max_amounts = {"red":12,"blue":14,"green":13}
colors = ["red", "blue", "green"]
# Initialize a sum to store game numbers
valid_game_sum = 0

# Iterate over all game sets
for game_number, game_sets in enumerate(games, start=1):
    # And for each set in the game,
    for set in game_sets:
        # compare the max allowed amount to the number of each color
        color_pass = getCount(set, colors, max_amounts)
        # If counts did not exceed the max amounts, add game number to sum
        if color_pass:
            valid_game_sum += game_number

print(f"The sum of valid game numbers is: {valid_game_sum}")

