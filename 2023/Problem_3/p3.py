# Import the regular expression module
import re

# Open the file 'sample.txt' and read its contents, splitting them into lines
with open('2023\\Problem_3\\input.txt') as file: 
    grid = file.read().split("\n")

def symbol_locations(grid, specialChars):
    locations = []
    # Iterate over each row and line in the grid
    for row_index, line in enumerate(grid):
        # Iterate over each column and character in the line
        for col_index, char in enumerate(line):
            # Check if the character is one of the specified symbols
            if char in specialChars:
                # If yes, add the (row, column) index to the locations list
                locations.append((col_index, row_index))
    # sort special_coords by its y value to prevent searching for chars in rows that are too far away
    sorted_locations = sorted(locations, key=lambda coord: coord[1])

    return sorted_locations

def is_touching_asterisk(grid, special_coords):
    # The list of part numbers to be returned
    part_numbers = []
    # The xy directions to check against special_coorsd per digit
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    # Enumerate grid, keeping track of the row index while iterating over the current line string
    for row_index, line in enumerate(grid):
        # Iterate over special_coords that are within or 1 more than the current row
        for symbol_x, symbol_y in filter(lambda coord: row_index - 1 <= coord[1] <= row_index + 1, special_coords):
            # Find all occurrences of digits in the line
            for match in re.finditer(r'(\d+)', line):
                # Boolean to prevent duplicate values
                numFound = False
                # Enumerate each number, keeping track of the start index (digit not needed but good for debugging)
                for digit_index, digit in enumerate(match.group()):
                    x = match.start() + digit_index
                    y = row_index
                    # Iterate over directions, checking against special_coords
                    for x_dir, y_dir in directions:
                        # Checking coords surrounding current digit
                        new_x, new_y = x + x_dir, y + y_dir
                        # If the coords match, append the number to the list
                        if (new_x, new_y) == (symbol_x, symbol_y) and not numFound:
                            part_numbers.append(int(match.group()))
                            # Toggle boolean to prevent duplicate values
                            numFound = True
    return part_numbers




# Get the locations of asterisks in the grid
unique_special_chars = {char for line in grid for char in re.findall(r'[^a-zA-Z0-9\s.]', line)}
symbol_coords = symbol_locations(grid, unique_special_chars)

# Check if digits are touching asterisks and print the result
result = is_touching_asterisk(grid, symbol_coords)

# Calculate the sum of the results. A set automatically removes duplicates
total_sum = sum(set(result))

# Print the total sum
print(total_sum)
