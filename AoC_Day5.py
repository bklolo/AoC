import re

x = open('AoC5.txt').read()
strip = re.split("\n", x)
a = []
for x in strip:
    b = []
    if x != "\n":
        b.append(x)
    a.append(b)
print(a)
# res = [list(sub) for sub in test_list]

'''pseudo code'''
# get input from file as string
# deal with box input
    # create list for each column
    # for each line (\n) of file
        # put column letters in appropriate lists
# deal with moves input