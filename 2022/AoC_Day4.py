'''Part I: In how many assignment pairs does one range fully contain the other?'''

def checkDataRanges(list):
    sum = 0
    ranges = []
    partI = False
    for pair in list:
        assignmentPair = pair.split(",")
        # example pair: ['92-92', '90-91']
        (min0, max0) = map(int, assignmentPair[0].split("-"))
        (min1, max1) = map(int, assignmentPair[1].split("-"))
        subRanges0 = {x for x in range(min0,max0+1)}
        subRanges1 = {x for x in range(min1,max1+1)}
        if partI:
            if subRanges0.issubset(subRanges1) or subRanges1.issubset(subRanges0):
                sum += 1
        elif subRanges0.intersection(subRanges1):
            sum += 1

    return sum

# Get data
dataString = open('AoC4.txt').read()
listString = [x for x in dataString.split("\n")]
# Manage data
print(checkDataRanges(listString))
