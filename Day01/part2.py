from Common.utils import read_lines_from_file

def extract_real_calibration_values(lines):

    mapping = {
        'one': 'one1one', 'two': 'two2two', 'three': 'three3three',
        'four': 'four4four', 'five': 'five5five', 'six': 'six6six',
        'seven': 'seven7seven', 'eight': 'eight8eight', 'nine': 'nine9nine'
    }

    total = 0

    #Iterate over all the lines
    for line in lines:
        # Apply mapping before processing
        for key, value in mapping.items():
            line = line.replace(key, value)

        #Extract first and last digit
        first_digit = next((char for char in line if char.isdigit()), None)
        last_digit = next((char for char in reversed(line) if char.isdigit()), None)

        #Sum everything up
        if first_digit and last_digit:
            value = int(first_digit + last_digit)
            total += value

    return total


def day1_solution(file_path):
    lines = read_lines_from_file(file_path)
    return extract_real_calibration_values(lines)

file_path = 'input.txt'
result = day1_solution(file_path)

print("Part 2:", result)
