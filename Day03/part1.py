from Common.utils import read_lines_from_file

def is_symbol(char):
    """Check if the character is a symbol."""
    return char not in '0123456789.'

def get_complete_number(grid, row, col):
    """Get the complete number at a given position, expanding left and right."""
    # Expand to the left to find the start of the number
    left_bound = col
    while left_bound > 0 and grid[row][left_bound - 1].isdigit():
        left_bound -= 1

    # Expand to the right to find the end of the number
    right_bound = col
    while right_bound < len(grid[row]) - 1 and grid[row][right_bound + 1].isdigit():
        right_bound += 1

    return grid[row][left_bound:right_bound + 1], left_bound, right_bound

def is_adjacent_to_symbol(schematic, row, col, left_bound, right_bound):
    """Check if the number is adjacent to a symbol."""

    for row_offset in range(-1, 2):
        for col_offset in range(-1, 2):
            for index in range(left_bound, right_bound + 1):
                adj_row = row + row_offset
                adj_col = col + col_offset + index - left_bound
                if 0 <= adj_row < len(schematic) and 0 <= adj_col < len(schematic[0]):
                    if is_symbol(schematic[adj_row][adj_col]):
                        return True
    return False

def sum_part_numbers(schematic):
    """Calculate the sum of all part numbers in the schematic."""
    total_sum = 0
    visited = set()

    for row in range(len(schematic)):
        for col in range(len(schematic[row])):
            if schematic[row][col].isdigit() and (row, col) not in visited:
                number, left_bound, right_bound = get_complete_number(schematic, row, col)
                if number and is_adjacent_to_symbol(schematic, row, col, left_bound, right_bound):
                    total_sum += int(number)
                    print(f"Part number found at ({row}, {left_bound}-{right_bound}): {number}, Total Sum: {total_sum}")

                # Mark all digits of the number as visited
                for index in range(left_bound, right_bound + 1):
                    visited.add((row, index))

    return total_sum

# Read the schematic from the file and calculate the sum of part numbers
file_path = 'input.txt'
schematic = read_lines_from_file(file_path)
result = sum_part_numbers(schematic)
print("Sum of all part numbers:", result)
