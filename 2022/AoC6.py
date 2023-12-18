input = open("AoC6.txt").read()
input_sample = open("AoC6_sample.txt").read()

# Shift list left
def shiftListLeft(sequence):
    sequence.reverse()
    sequence.pop()
    sequence.reverse()

# Print the index of the last item of 'length' non-duplicates
def indexOfLastNonduplicate(string, length):
    sequence = []
    count = 0
    for idx, letter in enumerate(string):
        # for each letter, put into list
        if count < length:
            while letter in sequence:
                shiftListLeft(sequence)
                count -= 1
            else:
                sequence.append(letter)
                count += 1

        else:
            print(idx)
            break
'''Part I: return the index of the last item of 4 non-duplicate items'''
print("Part I: ")
indexOfLastNonduplicate(input, 4)
'''Part II: return the index of the last item of 14 non-duplicate items'''
print("Part II: ")
indexOfLastNonduplicate(input, 14)
