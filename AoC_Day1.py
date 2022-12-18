

def calsPerElf(cals):
    sum = first = second = third = 0

    for x in cals:
        if x != "":
            x = int(x)
            sum += x
        else:
            if sum > first:
                third = second
                second = first
                first = sum
            elif sum > second:
                third = second
                second = sum
            elif sum > third:
                third = sum
            sum = 0

    return first+second+third


f = open("AoC1.txt")

x = f.read().split("\n")

ans = calsPerElf(x)

print(ans)