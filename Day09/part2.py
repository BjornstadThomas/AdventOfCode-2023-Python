from Common.utils import read_lines_from_file
from part1 import calculate_and_print_differences


def calculate_previous_value(sequence, level=0):
    """
    Recursively calculates the previous value in a sequence based on differences between consecutive numbers.

    Args:
    sequence (list[int]): A sequence of numbers.
    level (int): Recursion level for formatting debug output.

    Returns:
    int: The previous value in the sequence.
    """
    if len(set(sequence)) == 1:
        return sequence[0]

    differences = calculate_and_print_differences(sequence, level)
    return sequence[0] - calculate_previous_value(differences, level + 1)


lines = read_lines_from_file("input.txt")
input_data = [[int(num) for num in line.split()] for line in lines]
total_sum = sum(calculate_previous_value(row) for row in input_data)
print(f"\nPart 2: Total sum of previous values: {total_sum}")
