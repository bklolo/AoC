def is_touching_asterisk(grid, x, y):
    # Define bounds
    height, width = len(grid), len(grid[0])
    # Define surrounding cells
    directions = [(-1, -1), (-1, 0), (-1, 1),  (0, -1), (0, 1),  (1, -1), (1, 0), (1, 1)]

    # Initialize a set to store the collected numbers
    collected_numbers = set()

    # Check surrounding cells for numbers
    for xdir, ydir in directions:
        # Move current cell to new row/col
        new_row, new_col = x + xdir, y + ydir
        # Check that cell is within bounds
        while 0 <= new_row < height and 0 <= new_col < width:
            current_cell = grid[new_row][new_col]
            
            # If the cell contains a digit, collect the full number
            if current_cell.isdigit():
                number = ""


                # Add the collected number to the set
                collected_numbers.add(number)
            
            new_row += xdir

    return collected_numbers

# Example usage:
input_grid = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

# Check if any number is touching the asterisk at grid[1][3]
result = is_touching_asterisk(input_grid, 1, 3)
print("Collected numbers:", result)
