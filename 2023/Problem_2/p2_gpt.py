import re
from functools import reduce

def getMinReqAmounts(game_set, colors):
    counts = {color: 0 for color in colors}
    
    for color in colors:
        occurrences = re.findall(r'(\d+) ' + color, game_set)
        if occurrences:
            counts[color] = max(map(int, occurrences))
    
    return list(counts.values())

with open('2023\\Problem_2\\sample.txt') as file:
    document = file.read().split("\n")

colors = ["red", "blue", "green"]

power = 0

for game_set in document:
    min_req_amounts = getMinReqAmounts(game_set, colors)
    power += reduce(lambda x, y: x * y, min_req_amounts)

print(f"The power of valid games is: {power}")

