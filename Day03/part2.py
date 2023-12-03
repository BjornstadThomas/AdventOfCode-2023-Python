from Common.utils import read_lines_from_file
from Day03.part1 import get_complete_number

def is_gear_symbol(char):
    """Check if the character is a gear symbol."""
    return char == '*'

def get_adjacent_part_numbers(schematic, x, y):
    """Get all unique part numbers adjacent to the given position."""
    part_numbers = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(schematic) and 0 <= ny < len(schematic[0]) and schematic[nx][ny].isdigit():
                num, _, _ = get_complete_number(schematic, nx, ny)
                if num and num.isdigit():
                    part_numbers.append(int(num))
    return list(set(part_numbers))

def calculate_gear_ratios(schematic):
    """Calculate the sum of gear ratios in the schematic."""
    total_ratio_sum = 0
    visited = set()
    for i in range(len(schematic)):
        for j in range(len(schematic[i])):
            if is_gear_symbol(schematic[i][j]) and (i, j) not in visited:
                part_numbers = get_adjacent_part_numbers(schematic, i, j)
                if len(part_numbers) == 2:
                    gear_ratio = part_numbers[0] * part_numbers[1]
                    total_ratio_sum += gear_ratio
                    print(f"Gear found at ({i}, {j}): Part numbers {part_numbers}, Gear Ratio: {gear_ratio}")
                visited.add((i, j))

    return total_ratio_sum


file_path = 'input.txt'
schematic = read_lines_from_file(file_path)
result = calculate_gear_ratios(schematic)
print("Sum of all gear ratios:", result)
