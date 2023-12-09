from Common.utils import read_lines_from_file


def calculate_and_print_differences(sequence, level=0):
    """
    Calculates differences between consecutive numbers in a sequence and prints them.

    Args:
    sequence (list[int]): A sequence of numbers.
    level (int): Recursion level for formatting debug output.

    Returns:
    list[int]: The list of differences.
    """
    differences = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]

    spaces = "  " * level
    formatted_sequence = "  ".join(map(str, sequence))
    formatted_differences = "  ".join(map(str, differences))
    print(f"{spaces}{formatted_sequence}")
    print(f"{spaces}  {formatted_differences}")

    return differences


def calculate_next_value(sequence, level=0):
    """
    Recursively calculates the next value in a sequence based on differences between consecutive numbers.

    Args:
    sequence (list[int]): A sequence of numbers.
    level (int): Recursion level for formatting debug output.

    Returns:
    int: The next value in the sequence.
    """
    if len(set(sequence)) == 1:
        return sequence[0]

    differences = calculate_and_print_differences(sequence, level)
    return sequence[-1] + calculate_next_value(differences, level + 1)


lines = read_lines_from_file("input.txt")
input_data = [[int(num) for num in line.split()] for line in lines]
total_sum = sum(calculate_next_value(row) for row in input_data)
print(f"\nPart 1: Total sum of next values: {total_sum}")
