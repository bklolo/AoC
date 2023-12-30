import re

def symbol_locations(grid, symbols={'*', '$', '#', '+'}):
    return [(col_index, row_index) for row_index, line in enumerate(grid)
            for col_index, char in enumerate(line) if char in symbols]

def is_touching_asterisk(grid, symbol_coords):
    part_numbers = set()
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for asterisk_x, asterisk_y in symbol_coords:
        for row_index, line in enumerate(grid):
            for match in re.finditer(r'(\d+)', line):
                for digit_index, digit in enumerate(match.group()):
                    x, y = match.start() + digit_index, row_index
                    for x_dir, y_dir in directions:
                        new_x, new_y = x + x_dir, y + y_dir
                        if (new_x, new_y) == (asterisk_x, asterisk_y):
                            part_numbers.add(int(match.group()))
                            print(f"Digit {match.group()} is touching a symbol.")
    return part_numbers

with open('2023\\Problem_3\\sample.txt') as file:
    grid = file.read().split("\n")

symbol_coords = symbol_locations(grid)
result = is_touching_asterisk(grid, symbol_coords)
total_sum = sum(result)

print(total_sum)
