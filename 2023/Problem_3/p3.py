import re

# Returns xy coordinates of all special characters in the input, sorted by y value
def symbol_locations(grid, specialChars):
    locations = []
    for row_index, line in enumerate(grid):
        for col_index, char in enumerate(line):
            if char in specialChars:
                locations.append((col_index, row_index))
    sorted_locations = sorted(locations, key=lambda coord: coord[1])
    return sorted_locations

def is_part_number(grid, special_coords):
    nums = []
    for digit_y, line in enumerate(grid):
        for match in re.finditer(r'(\d+)', line):
            num_begin, num_end = match.span()
            
            for sp_x, sp_y in special_coords:
                if (num_begin-1 <= sp_x <= num_end) and (digit_y-1 <= sp_y <= digit_y+1):
                    #print(f"Number: {match.group()}, Special Character at: ({sp_x}, {sp_y})")
                    nums.append(match.group())
    return nums

def count_numbers_hit(grid, asterisk_coords):
    asterisk_counts = {}

    for digit_y, line in enumerate(grid):
        for ast_x, ast_y in asterisk_coords:
            if digit_y < ast_y <= digit_y+1:
                # for each number in the current line
                for match in re.finditer(r'(\d+)', line):
                    num_begin, num_end = match.span()
                    if num_begin-1 <= ast_x <= num_end+1:
                        # Increment the count for the current asterisk
                        asterisk_counts[(ast_x, ast_y)] = asterisk_counts.get((ast_x, ast_y), 0) + 1

    return asterisk_counts


# Open the targeted file
with open('2023\\Problem_3\\sample.txt') as file: 
    # Read the contents of the file and split by new line
    grid = file.read().split("\n")

part = 'b'
################# Part A #################
if part == 'a':
    # Get the locations of special characters in the grid
    unique_special_chars = {char for line in grid for char in re.findall(r'[^a-zA-Z0-9\s.]', line)}
    special_coords = symbol_locations(grid, unique_special_chars)

    # Check if digits are touching special characters and print the result
    result = is_part_number(grid, special_coords)

    # Calculate the sum of the results
    total_sum = sum(map(int, result))

    # Print the total sum
    print(total_sum)
################# Part B #################
if part == 'b':
    # Assuming you want to find all asterisks in each line of the grid
    asterisk_coords = [(col_index, row_index) for row_index, line in enumerate(grid) 
                       for col_index, char in enumerate(line) if char == '*']
    count_numbers_hit(grid, asterisk_coords)

asterisk_counts = count_numbers_hit(grid, asterisk_coords)

# Print the counts for each asterisk
for asterisk, count in asterisk_counts.items():
    print(f"Asterisk {asterisk} hits {count} numbers.")