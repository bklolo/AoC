import re
# Input string representing a game set
game_set = "3 red, 5 blue, 2 green"

# List of colors we are interested in
colors = ["red", "blue", "green"]

# Initialize an empty dictionary to store counts for each color
counts = {color: 0 for color in colors}

# Iterate over each color
for color in colors:
    # Use regular expression to find all occurrences of count + color in the game set
    occurrences = re.findall(r'(\d+) ' + color, game_set)

    # If occurrences are found, update the count with the maximum value
    if occurrences:
        counts[color] = max(map(int, occurrences))

# Display the result
print(counts)
