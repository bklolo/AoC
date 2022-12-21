import re
x = open('AoC5.txt').read()
split = re.split("\n", x)
print(split)
row = []
for i in split:
    row.append(i.replace(' ', '').replace('[', '').replace(']', ''))
print(row)
# res = [list(sub) for sub in x] # each chr in str
# print(res)

row1 = []
row2 = []
row3 = []
row4 = []
row5 = []
row6 = []
row7 = []
row8 = []
row9 = []
rows = []
for item in row:
    rows.append(item[0])
    row2.append(item[1])
    row3.append(item[2])
    row4.append(item[3])
    row5.append(item[4])
    row6.append(item[5])
    row7.append(item[6])
    row8.append(item[7])
    row9.append(item[8])