from Common.utils import read_lines_from_file

def calculate_card_points(winning_numbers, player_numbers):
    """Calculate the points for a single card."""

    matches = [num for num in player_numbers if num in winning_numbers]
    if not matches:
        return 0

    return 2 ** (len(matches) - 1)

def total_scratchcard_points(file_path):
    """Calculate the total points from all scratchcards."""

    total_points = 0
    lines = read_lines_from_file(file_path, delimiter='|')
    for parts in lines:

        #Remove text "Card X:" and process the numbers given
        winning_numbers = set(map(int, parts[0].split(':')[1].split()))
        player_numbers = list(map(int, parts[1].split()))
        total_points += calculate_card_points(winning_numbers, player_numbers)

    return total_points


file_path = 'input.txt'
result = total_scratchcard_points(file_path)
print("Total points from scratchcards:", result)
