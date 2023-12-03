from Common.utils import read_lines_from_file

def is_symbol(char):
    """Check if the character is a symbol."""
    return char not in '0123456789.'

def get_complete_number(grid, i, j):
    """Get the complete number at a given position, expanding left and right."""
    # Expand to the left to find the start of the number
    left = j
    while left > 0 and grid[i][left - 1].isdigit():
        left -= 1

    # Expand to the right to find the end of the number
    right = j
    while right < len(grid[i]) - 1 and grid[i][right + 1].isdigit():
        right += 1

    return grid[i][left:right + 1], left, right

def is_adjacent_to_symbol(schematic, x, y, left, right):
    """Check if the number is adjacent to a symbol."""
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for j in range(left, right + 1):
                nx, ny = x + dx, y + dy + j - left
                if 0 <= nx < len(schematic) and 0 <= ny < len(schematic[0]):
                    if is_symbol(schematic[nx][ny]):
                        return True
    return False

def sum_part_numbers(schematic):
    """Calculate the sum of all part numbers in the schematic."""
    total_sum = 0
    visited = set()
    for i in range(len(schematic)):
        for j in range(len(schematic[i])):
            if schematic[i][j].isdigit() and (i, j) not in visited:
                number, left, right = get_complete_number(schematic, i, j)
                if number and is_adjacent_to_symbol(schematic, i, j, left, right):
                    total_sum += int(number)
                    print(f"Part number found at ({i}, {left}-{right}): {number}, Total Sum: {total_sum}")
                # Mark all digits of the number as visited
                for k in range(left, right + 1):
                    visited.add((i, k))

    return total_sum


file_path = 'input.txt'
schematic = read_lines_from_file(file_path)
result = sum_part_numbers(schematic)
print("Sum of all part numbers:", result)
