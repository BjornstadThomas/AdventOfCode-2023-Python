from Common.utils import read_lines_from_file


def extract_calibration_values(lines):
    total = 0

    # Iterate over all the lines
    for line in lines:
        # Extract first and last digit
        first_digit = next((char for char in line if char.isdigit()), None)
        last_digit = next((char for char in reversed(line) if char.isdigit()), None)

        # Sum everything up
        if first_digit and last_digit:
            value = int(first_digit + last_digit)
            total += value

    return total


def day1_solution(file_path):
    lines = read_lines_from_file(file_path)
    return extract_calibration_values(lines)


file_path = 'input.txt'
result = day1_solution(file_path)

#print("Part 1:", result)
