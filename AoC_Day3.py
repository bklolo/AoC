import string
### TODO 1) use only single dictionary
### TODO 2) use 'a' - 'a' + 1 function
def sumPriority(x):
    # half the string
    first_half = x[0: len(x)//2]
    second_half = x[len(x)//2 if len(x) % 2 == 0 else ((len(x)//2)+1):]
    b = [first_half, second_half]
    # find similarities
    for i in first_half:
        if i in second_half:
            return i

def populatePriorities():
    """ chr: Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
        ord: Return the Unicode code point for a one-character string.
    """
    d = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    D = {chr(j): 0 for j in range(ord('A'), ord('Z') + 1)}
    count = 1
    for key in d:
        d[key] = count
        count += 1
    for key in D:
        D[key] = count
        count += 1
    return d, D

# Get data from file
file = open('AoC3.txt')

# Separate data into list items
x = file.read().split("\n")

# Populate priorities
lower, upper = populatePriorities()

# Get duplicates in each napsack
priorityList = []
for item in x:
    priorityList.append(sumPriority(item))

# Apply values to duplicates
sum = 0
for i in priorityList:
    if i in lower:
        sum += lower.get(i)
    if i in upper:
        sum += upper.get(i)
print(sum)
