import string

'''Part I: Find the duplicate in each rucksack half and sum priorities'''
### TODO 1) use only single dictionary
### TODO 2) use 'a' - 'a' + 1 function

def findDuplicate(x):
    # half the string
    first_half = x[0: len(x)//2]
    second_half = x[len(x)//2 if len(x) % 2 == 0 else ((len(x)//2)+1):]
    b = [first_half, second_half]
    # find similarities
    for i in first_half:
        if i in second_half:
            return i

def charPriorityDict():
    """ chr: Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
        ord: Return the Unicode code point for a one-character string.
    """
    dict = {}
    count = 1
    
    for i in range(ord('a'), ord('z') + 1):
        dict[chr(i)] = count
        count += 1
    for j in range(ord('A'), ord('Z') + 1):
        dict[chr(j)] = count
        count += 1
    
    return dict


# Get data from file
file = open('AoC3.txt')
# Separate data into list items
x = file.read().split("\n")
# Create dict of letter:priority
dict = charPriorityDict()
# Get duplicates in each napsack
duplicateLetters = []
for item in x:
    duplicateLetters.append(findDuplicate(item))
    
# Apply values to duplicates
sum = 0
for letter in duplicateLetters:
    if letter in dict:
        sum += dict.get(letter)
    # if i in lower:
        # sum += lower.get(i)
    # if i in upper:
        # sum += upper.get(i)

# Print sum
print(sum)

'''Part II: Find the common item in each group of three rucksacks'''
# Using x from above,
# Create groups of three out of the data input strings
sum = 0
N = 3
subList = [x[n:n+N] for n in range(0, len(x), N)]
# Search for a common item in each group of three
for group in subList:
    # compare to find same item
    letterSet = set(group[0]).intersection(group[1], group[2])
    for i in letterSet:
        letter = i
    # search dict for letter
    sum += dict.get(letter)
# Print sum
print(sum)
