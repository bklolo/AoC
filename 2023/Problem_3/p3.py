
with open('2023\\Problem_3\\sample.txt') as file: 
    grid = file.read().split("\n")

def is_touching_asterisk(grid, row, col):
    # Define bounds
    height, width = len(grid), len(grid[0])
    # Define the eight possible directions to check (above, below, diagonal)
    directions = [(-1, -1), (-1, 0), (-1, 1), (  0, -1), (0, 1),   (1, -1), (1, 0), (1, 1)]

    # for each row in grid, scan for an asterisk
    for row_index, row in enumerate(grid):
        cell = []
        # Check if an asterisk is present in the row
        if '*' in row:
            # when an asterisk is found, get the row/col location
            col_index = row.index('*')
            cell = [row_index, col_index]

            # check surrounding cells for numbers
            for xdir, ydir in directions:
                
                new_row, new_col = (row_index + xdir), (col_index + ydir)
                
                # check if the new row and col are in bounds
                if 0 <= new_row < height and 0 <= new_col < width:
                    
                    value = grid[new_row][new_col]
                    
                    # check if the cell holds a digit
                    if value.isDigit():
                        number = value
                        # create left and right of the number for "."
                        left_col, right_col = new_col-1, new_col+1
                        while right_col < width and value == '.':
                            number += value
                            right_col += 1
    # if number found
        # check left and right of number for .
        # if digit, collect full number

# Check if the number at row 2, column 3 is touching an asterisk
part_numbers = []
result = is_touching_asterisk(grid, 0, 0)
print(result)  # Output: True

