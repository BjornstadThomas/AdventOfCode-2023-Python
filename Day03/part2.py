from Common.utils import read_lines_from_file
from Day03.part1 import get_complete_number

def is_gear_symbol(char):
    """Check if the character is a gear symbol."""
    return char == '*'

def get_adjacent_part_numbers(schematic, row, col):
    """Get all unique part numbers adjacent to the given position."""
    part_numbers = []

    for row_offset in range(-1, 2):
        for col_offset in range(-1, 2):
            if row_offset == 0 and col_offset == 0:
                continue

            adjacent_row = row + row_offset
            adjacent_col = col + col_offset

            if 0 <= adjacent_row < len(schematic) and 0 <= adjacent_col < len(schematic[0]):
                if schematic[adjacent_row][adjacent_col].isdigit():
                    num, _, _ = get_complete_number(schematic, adjacent_row, adjacent_col)
                    if num.isdigit():
                        part_numbers.append(int(num))

    return list(set(part_numbers))  # Remove duplicates to avoid double counting

def calculate_gear_ratios(schematic):
    """Calculate the sum of gear ratios in the schematic."""
    total_ratio_sum = 0
    visited_gears = set()

    for row in range(len(schematic)):
        for col in range(len(schematic[row])):
            if is_gear_symbol(schematic[row][col]) and (row, col) not in visited_gears:
                part_numbers = get_adjacent_part_numbers(schematic, row, col)
                if len(part_numbers) == 2:
                    gear_ratio = part_numbers[0] * part_numbers[1]
                    total_ratio_sum += gear_ratio
                    print(f"Gear found at ({row}, {col}): Part numbers {part_numbers}, Gear Ratio: {gear_ratio}")
                visited_gears.add((row, col))

    return total_ratio_sum


file_path = 'input.txt'
schematic = read_lines_from_file(file_path)
result = calculate_gear_ratios(schematic)
print("Sum of all gear ratios:", result)
